/* Headlight that follows the cursor.
 *
 * The locomotive sits in a near-black stage. Two copies of the same PNG are
 * stacked: a heavily darkened one that is always visible, and a full-brightness
 * one on top that is masked by a soft radial gradient centred on the cursor.
 * Moving the cursor moves the hole in the mask, so light appears to sweep
 * across the train, fading off at the edges instead of cutting off.
 *
 * Two beam cones are anchored at the headlamps and rotated to aim wherever the
 * cursor is, which is what sells it as a light source on the train rather than
 * a torch held over a picture.
 *
 * Only custom properties and transforms are written per frame -- no canvas, no
 * layout work -- so this stays cheap.
 */
'use strict';

(function () {
  const stage = document.getElementById('loco');
  if (!stage) return;

  const lit = stage.querySelector('.loco-lit');
  const beamL = stage.querySelector('.beam-l');
  const beamR = stage.querySelector('.beam-r');

  // Lamp centres as a fraction of the (square) source image, read off the art:
  // the twin main lamps in the centre housing.
  const LAMPS = [
    { x: 0.479, y: 0.490, el: beamL },
    { x: 0.522, y: 0.490, el: beamR },
  ];

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduceMotion.matches) {
    // No sweeping light; just show the train evenly lit and stop.
    stage.classList.add('static-light');
    return;
  }

  let rect = stage.getBoundingClientRect();
  let art = artBox();

  // background-size: contain on a square image => the drawn art is a centred
  // square of side min(w, h). Lamp positions must be measured against that
  // box, not the stage, or they drift when the stage aspect changes.
  function artBox() {
    const side = Math.min(rect.width, rect.height);
    return { side, left: (rect.width - side) / 2, top: (rect.height - side) / 2 };
  }

  function remeasure() {
    rect = stage.getBoundingClientRect();
    art = artBox();
  }

  // Target position (where the cursor is) and current (what we draw), so the
  // beam eases instead of snapping.
  let targetX = rect.width * 0.5;
  let targetY = rect.height * 0.85;
  let curX = targetX;
  let curY = targetY;
  let raf = 0;

  function onMove(e) {
    targetX = e.clientX - rect.left;
    targetY = e.clientY - rect.top;
    if (!raf) raf = requestAnimationFrame(tick);
  }

  function tick() {
    curX += (targetX - curX) * 0.18;
    curY += (targetY - curY) * 0.18;

    stage.style.setProperty('--mx', curX.toFixed(1) + 'px');
    stage.style.setProperty('--my', curY.toFixed(1) + 'px');

    for (const lamp of LAMPS) {
      const lx = art.left + lamp.x * art.side;
      const ly = art.top + lamp.y * art.side;
      const dx = curX - lx;
      const dy = curY - ly;
      const dist = Math.hypot(dx, dy);
      const angle = Math.atan2(dy, dx);

      lamp.el.style.left = lx + 'px';
      lamp.el.style.top = ly + 'px';
      // Reach a little past the cursor so the cone does not stop dead at it.
      lamp.el.style.width = (dist * 1.15 + 40) + 'px';
      lamp.el.style.transform =
        `translateY(-50%) rotate(${angle}rad)`;
    }

    if (Math.abs(targetX - curX) > 0.3 || Math.abs(targetY - curY) > 0.3) {
      raf = requestAnimationFrame(tick);
    } else {
      raf = 0;
    }
  }

  window.addEventListener('mousemove', onMove, { passive: true });
  window.addEventListener('scroll', remeasure, { passive: true });
  window.addEventListener('resize', () => { remeasure(); tick(); }, { passive: true });

  // Dim the beams when the pointer leaves the window entirely.
  document.addEventListener('mouseleave', () => stage.classList.add('idle'));
  document.addEventListener('mouseenter', () => stage.classList.remove('idle'));

  stage.classList.add('live');
  tick();

  // The PNG is the whole effect; if it is missing, drop the stage rather than
  // leaving an empty black band on the page.
  const probe = new Image();
  probe.onerror = () => stage.remove();
  probe.src = '/static/train-front.png';
})();
