// -*- coding: utf-8 -*-
const fs = require('fs');
const path = require('path');

// Redirect old domain in SDK to official new api.railkit.in
const originalFetch = global.fetch;
global.fetch = async (url, options) => {
  const newUrl = url.replace('https://railkit-api.rajivdubey.dev', 'https://api.railkit.in');
  return originalFetch(newUrl, options);
};

const sdk = require('./index.obfuscated.js');

// Load all API Keys from .env or environment
function getApiKeys() {
  const envFile = path.resolve(__dirname, '../../.env');
  let keys = [];
  if (process.env.RAILKIT_API_KEYS) {
    keys.push(...process.env.RAILKIT_API_KEYS.split(',').map(k => k.trim()).filter(Boolean));
  }
  if (process.env.RAILKIT_API_KEY) {
    keys.push(process.env.RAILKIT_API_KEY.trim());
  }
  if (fs.existsSync(envFile)) {
    const lines = fs.readFileSync(envFile, 'utf8').split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (trimmed.startsWith('RAILKIT_API_KEYS=')) {
        const val = trimmed.split('=')[1].replace(/['"]/g, '');
        keys.push(...val.split(',').map(k => k.trim()).filter(Boolean));
      } else if (trimmed.startsWith('RAILKIT_API_KEY=')) {
        const val = trimmed.split('=')[1].replace(/['"]/g, '').trim();
        if (val) keys.push(val);
      }
    }
  }
  const cleanKeys = [...new Set(keys)].filter(Boolean);
  return cleanKeys;
}

const keyPool = getApiKeys();

// Multi-Key Failover Executor
async function executeWithFailover(fn) {
  let lastError = null;

  for (let i = 0; i < keyPool.length; i++) {
    const key = keyPool[i];
    try {
      sdk.configure(key);
      const res = await fn();
      if (res && res.success) {
        return res;
      }
      
      const errStr = res && res.error ? String(res.error).toLowerCase() : '';
      lastError = res ? res.error : 'Unknown error';
      
      // If PNR or resource simply not found on IRCTC, do not loop through all keys
      if (
        errStr.includes('not found') ||
        errStr.includes('no pnr data') ||
        errStr.includes('invalid pnr') ||
        errStr.includes('404') ||
        errStr.includes('flushed') ||
        errStr.includes('expired')
      ) {
        return {
          success: false,
          is_expired: true,
          error: "PNR record not found. (IRCTC flushes old PNR records from active database after journey completion)."
        };
      }

      // If error is specifically related to quota/rate limit/inactivity, failover to next key in pool
      if (
        errStr.includes('limit') ||
        errStr.includes('quota') ||
        errStr.includes('inactive') ||
        errStr.includes('exceeded') ||
        errStr.includes('429') ||
        errStr.includes('401') ||
        errStr.includes('403') ||
        errStr.includes('unauthorized')
      ) {
        continue;
      }
      
      return res;
    } catch (err) {
      lastError = err.message;
    }
  }

  return { success: false, error: lastError || 'All API keys exhausted or rate-limited.' };
}

async function main() {
  const args = process.argv.slice(2);
  const action = args[0];

  try {
    if (action === 'pnr') {
      const pnr = args[1];
      const res = await executeWithFailover(() => sdk.checkPNRStatus(pnr));
      console.log(JSON.stringify(res));
    } else if (action === 'track') {
      const train = args[1];
      const date = args[2] || undefined;
      const res = await executeWithFailover(() => sdk.trackTrain(train, date));
      console.log(JSON.stringify(res));
    } else if (action === 'seats') {
      const train = args[1];
      const from = args[2];
      const to = args[3];
      const date = args[4];
      const coach = args[5] || '3A';
      const quota = args[6] || 'GN';
      const res = await executeWithFailover(() => sdk.getAvailability(train, from, to, date, coach, quota));
      console.log(JSON.stringify(res));
    } else if (action === 'station') {
      const stn = args[1];
      const hours = parseInt(args[2] || '4', 10);
      const res = await executeWithFailover(() => sdk.liveAtStation(stn, hours));
      console.log(JSON.stringify(res));
    } else if (action === 'pool-status') {
      console.log(JSON.stringify({ success: true, count: keyPool.length, keys: keyPool.map(k => k.slice(0, 14) + '...') }));
    } else {
      console.log(JSON.stringify({ success: false, error: 'Unknown action: ' + action }));
    }
  } catch (err) {
    console.log(JSON.stringify({ success: false, error: err.message }));
  }
}

main();
