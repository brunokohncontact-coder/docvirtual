/**
 * smooth-scroll.js
 * Scroll com lerp (interpolação linear) para sensação premium.
 * EASE: 0.05 = mais suave · 0.07 = padrão · 0.12 = mais ágil
 *
 * Expõe: window.SmoothScroll.scrollTo(y)
 */
window.SmoothScroll = (function () {
  // Touch/mobile: momentum nativo já é suave — não interferir
  if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
    return { scrollTo: (y) => window.scrollTo({ top: y, behavior: 'smooth' }) };
  }

  let sTarget  = window.scrollY;
  let sCurrent = window.scrollY;
  const EASE   = 0.07;
  let running  = false;

  const maxScroll = () => document.documentElement.scrollHeight - window.innerHeight;
  const clamp     = (v) => Math.max(0, Math.min(v, maxScroll()));

  function tick() {
    const diff = sTarget - sCurrent;
    if (Math.abs(diff) < 0.05) {
      sCurrent = sTarget;
      window.scrollTo(0, sCurrent);
      running = false;
      return;
    }
    sCurrent += diff * EASE;
    window.scrollTo(0, sCurrent);
    requestAnimationFrame(tick);
  }

  function run() {
    if (!running) { running = true; requestAnimationFrame(tick); }
  }

  // Wheel
  window.addEventListener('wheel', (e) => {
    e.preventDefault();
    let delta = e.deltaY;
    if (e.deltaMode === 1) delta *= 24;
    if (e.deltaMode === 2) delta *= window.innerHeight;
    sTarget = clamp(sTarget + delta);
    run();
  }, { passive: false });

  // Teclado
  window.addEventListener('keydown', (e) => {
    const h = window.innerHeight;
    const map = { ArrowDown: 80, ArrowUp: -80, PageDown: h * 0.9, PageUp: -h * 0.9 };
    if (map[e.key] !== undefined) { e.preventDefault(); sTarget = clamp(sTarget + map[e.key]); run(); }
    if (e.key === 'End')  { e.preventDefault(); sTarget = maxScroll(); run(); }
    if (e.key === 'Home') { e.preventDefault(); sTarget = 0; run(); }
    if (e.key === ' ' && !e.shiftKey) { e.preventDefault(); sTarget = clamp(sTarget + h * 0.9); run(); }
    if (e.key === ' ' &&  e.shiftKey) { e.preventDefault(); sTarget = clamp(sTarget - h * 0.9); run(); }
  });

  // Sincroniza com scroll externo (botão voltar, resize)
  window.addEventListener('scroll', () => {
    if (!running) { sTarget = window.scrollY; sCurrent = window.scrollY; }
  }, { passive: true });

  return {
    scrollTo(y) { sTarget = clamp(y); run(); }
  };
})();
