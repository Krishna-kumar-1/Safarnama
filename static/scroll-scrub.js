/* Scroll-scrubbed background video.
 *
 * Instead of playing, the video's playhead is bound to scroll position: the
 * top of the page is frame 0, the bottom is the last frame. Scrolling the
 * results list "drives" the train.
 *
 * Two details make this smooth rather than janky:
 *   - train-scrub.mp4 is encoded with every frame as a keyframe (-g 1), so
 *     seeking to an arbitrary time is one decode instead of replaying from
 *     the previous keyframe hundreds of frames back.
 *   - The playhead eases toward the scroll target instead of snapping to it,
 *     so a flung scroll reads as motion rather than a strobe.
 *
 * It deliberately does NOT add scroll distance or pin anything -- the search
 * form stays exactly where it was and is usable without scrolling at all.
 * Falls back to the static poster image whenever the video can't or shouldn't
 * run, so the page never ends up with an empty background.
 */
'use strict';

(function () {
  const video = document.getElementById('bg-video');
  if (!video) return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  // Metered connections and phones pay real money/battery for 5.6MB.
  const conn = navigator.connection || {};
  const tooExpensive = conn.saveData === true
    || /2g/.test(conn.effectiveType || '')
    || window.matchMedia('(pointer: coarse)').matches;

  if (reduceMotion.matches || tooExpensive) {
    video.remove();          // poster image behind it is already in place
    return;
  }

  video.src = video.dataset.src;   // deferred so it never blocks first paint
  video.load();

  let duration = 0;
  let target = 0;      // where scroll says the playhead should be
  let current = 0;     // where it actually is, chasing target
  let ticking = false;

  function scrollFraction() {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    if (scrollable <= 0) return 0;
    return Math.min(Math.max(window.scrollY / scrollable, 0), 1);
  }

  function onScroll() {
    if (!duration) return;
    target = scrollFraction() * duration;
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(tick);
    }
  }

  function tick() {
    // Ease 15% of the remaining gap per frame.
    current += (target - current) * 0.15;

    if (Math.abs(target - current) < 0.005) {
      current = target;
      ticking = false;
    } else {
      requestAnimationFrame(tick);
    }

    // Seeking while a seek is in flight throws the decoder away; skip instead.
    if (!video.seeking) {
      try {
        video.currentTime = current;
      } catch (err) {
        // Some browsers throw if the range isn't buffered yet; the next
        // scroll event will retry once more data has arrived.
      }
    }
  }

  video.addEventListener('loadedmetadata', () => {
    duration = video.duration || 0;
    video.classList.add('ready');   // fade in over the poster
    onScroll();
  });

  video.addEventListener('error', () => {
    video.remove();                 // leave the poster showing
  });

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });

  // Results render after a fetch and change the page height, which changes
  // what "bottom of page" means; recompute when that happens.
  const results = document.getElementById('results');
  if (results && 'ResizeObserver' in window) {
    new ResizeObserver(onScroll).observe(results);
  }
})();
