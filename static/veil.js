/* Page-wide darkness that the cursor lifts.
 *
 * #veil is a near-opaque black sheet over the background video. Its CSS mask
 * has a transparent hole at (--gx, --gy); wherever that hole sits, the veil
 * disappears and the video behind shows through. Moving the cursor therefore
 * looks like carrying a light across a dark scene.
 *
 * Only two custom properties are written per frame, and the mask is composited
 * by the GPU, so this costs almost nothing.
 */
'use strict';

(function () {
  const veil = document.getElementById('veil');
  if (!veil) return;

  const root = veil.style;
  const coarse = window.matchMedia('(pointer: coarse)');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  // With no cursor there is nothing to track, and a page that stays fully
  // black would just look broken. Dim it evenly and stop.
  function checkFallback() {
    const off = coarse.matches || reduce.matches;
    veil.classList.toggle('no-cursor', off);
    return off;
  }
  if (checkFallback()) return;
  coarse.addEventListener('change', checkFallback);
  reduce.addEventListener('change', checkFallback);

  let targetX = window.innerWidth * 0.5;
  let targetY = window.innerHeight * 0.42;
  let curX = targetX;
  let curY = targetY;
  let radius = 300;
  let targetRadius = 300;
  let raf = 0;

  function onMove(e) {
    targetX = e.clientX;
    targetY = e.clientY;
    if (!raf) raf = requestAnimationFrame(tick);
  }

  function tick() {
    // Ease so a fast flick smears into a sweep rather than teleporting.
    curX += (targetX - curX) * 0.16;
    curY += (targetY - curY) * 0.16;
    radius += (targetRadius - radius) * 0.12;

    root.setProperty('--gx', curX.toFixed(1) + 'px');
    root.setProperty('--gy', curY.toFixed(1) + 'px');
    root.setProperty('--gr', radius.toFixed(1) + 'px');

    const settled = Math.abs(targetX - curX) < 0.4
      && Math.abs(targetY - curY) < 0.4
      && Math.abs(targetRadius - radius) < 0.4;
    raf = settled ? 0 : requestAnimationFrame(tick);
  }

  window.addEventListener('mousemove', onMove, { passive: true });

  // Clicking flares the light briefly.
  window.addEventListener('mousedown', () => {
    targetRadius = 430;
    if (!raf) raf = requestAnimationFrame(tick);
  }, { passive: true });
  window.addEventListener('mouseup', () => {
    targetRadius = 300;
    if (!raf) raf = requestAnimationFrame(tick);
  }, { passive: true });

  // Pointer gone: close the light down to near nothing rather than freezing
  // a bright spot in place.
  document.addEventListener('mouseleave', () => {
    targetRadius = 90;
    if (!raf) raf = requestAnimationFrame(tick);
  });
  document.addEventListener('mouseenter', () => {
    targetRadius = 300;
    if (!raf) raf = requestAnimationFrame(tick);
  });

  tick();
})();
