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

// Load API Keys from .env or environment
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
  return [...new Set(keys)].filter(Boolean);
}

const keys = getApiKeys();
const defaultKey = keys.length ? keys[0] : '';
if (defaultKey) sdk.configure(defaultKey);

async function main() {
  const args = process.argv.slice(2);
  const action = args[0];

  try {
    if (action === 'pnr') {
      const pnr = args[1];
      const res = await sdk.checkPNRStatus(pnr);
      console.log(JSON.stringify(res));
    } else if (action === 'track') {
      const train = args[1];
      const date = args[2] || undefined;
      const res = await sdk.trackTrain(train, date);
      console.log(JSON.stringify(res));
    } else if (action === 'seats') {
      const train = args[1];
      const from = args[2];
      const to = args[3];
      const date = args[4];
      const coach = args[5] || '3A';
      const quota = args[6] || 'GN';
      const res = await sdk.getAvailability(train, from, to, date, coach, quota);
      console.log(JSON.stringify(res));
    } else if (action === 'station') {
      const stn = args[1];
      const hours = parseInt(args[2] || '4', 10);
      const res = await sdk.liveAtStation(stn, hours);
      console.log(JSON.stringify(res));
    } else {
      console.log(JSON.stringify({ success: false, error: 'Unknown action: ' + action }));
    }
  } catch (err) {
    console.log(JSON.stringify({ success: false, error: err.message }));
  }
}

main();
