/**
 * app.js
 * Ponto de entrada — inicializa componentes globais:
 * ícones Lucide, animações de scroll e links de âncora.
 *
 * Carregado por último, após todos os outros módulos.
 */
document.addEventListener('DOMContentLoaded', () => {

  /* --- Ícones Lucide --- */
  if (typeof lucide !== 'undefined') lucide.createIcons();

  /* --- Scroll Animations (IntersectionObserver) --- */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.observe-animate').forEach(el => observer.observe(el));

  /* --- Anchor Links com smooth scroll --- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const el = document.querySelector(this.getAttribute('href'));
      if (!el) return;
      const top = el.getBoundingClientRect().top + window.scrollY - 80;
      if (window.SmoothScroll) {
        SmoothScroll.scrollTo(top);
      } else {
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

});
