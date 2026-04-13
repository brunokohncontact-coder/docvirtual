/**
 * tabs.js
 * Sistema de abas das soluções por vertical.
 * switchTab() é exposta globalmente para uso nos onclick do HTML.
 */
function switchTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
  document.getElementById('tab-' + tabId).classList.add('active');

  document.querySelectorAll('.tab-btn').forEach(btn => {
    const isActive = btn.dataset.tab === tabId;
    btn.classList.toggle('bg-blue-600',        isActive);
    btn.classList.toggle('text-white',         isActive);
    btn.classList.toggle('shadow-lg',          isActive);
    btn.classList.toggle('shadow-blue-500/20', isActive);
    btn.classList.toggle('bg-white',           !isActive);
    btn.classList.toggle('text-gray-600',      !isActive);
    btn.classList.toggle('hover:bg-gray-100',  !isActive);
    btn.classList.toggle('border',             !isActive);
    btn.classList.toggle('border-gray-200',    !isActive);
  });
}
