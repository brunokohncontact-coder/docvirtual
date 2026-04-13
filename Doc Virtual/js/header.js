/**
 * header.js
 * Header adaptativo: alterna entre tema escuro e claro
 * conforme a seção visível, e gerencia o menu mobile.
 *
 * Seções claras devem ter o atributo: data-bg="light"
 */
(function () {
  const header       = document.getElementById('header');
  const lightSections = document.querySelectorAll('[data-bg="light"]');

  /* --- Tema adaptativo --- */
  function updateTheme() {
    const h = header.offsetHeight;
    let isLight = false;

    lightSections.forEach(section => {
      const rect = section.getBoundingClientRect();
      if (rect.top < h && rect.bottom > 0) isLight = true;
    });

    if (isLight) {
      header.classList.add('header-light', 'shadow-lg', 'shadow-black/10');
    } else {
      header.classList.remove('header-light');
      if (window.scrollY > 50) {
        header.classList.add('shadow-lg', 'shadow-black/20');
      } else {
        header.classList.remove('shadow-lg', 'shadow-black/20');
      }
    }
  }

  window.addEventListener('scroll', updateTheme, { passive: true });
  updateTheme();

  /* --- Menu mobile --- */
  const btn  = document.getElementById('mobile-menu-btn');
  const menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;

  btn.addEventListener('click', () => menu.classList.toggle('hidden'));
  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => menu.classList.add('hidden'));
  });
})();
