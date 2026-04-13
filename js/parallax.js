/**
 * parallax.js
 * Parallax do hero — move o #hero-bg a 30% da velocidade do scroll,
 * criando profundidade sem afetar o conteúdo em primeiro plano.
 */
(function () {
  const heroBg = document.getElementById('hero-bg');
  if (!heroBg) return;

  function update() {
    heroBg.style.transform = `translateY(${window.scrollY * 0.3}px)`;
  }

  window.addEventListener('scroll', update, { passive: true });
  update();
})();
