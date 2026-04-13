/**
 * form.js
 * Formulário de orçamento: filtro inteligente de tamanho,
 * submissão, máscara de telefone e tooltip do WhatsApp.
 *
 * handleFormSubmit() e showSizeDetails() são globais (usadas nos onsubmit/onchange do HTML).
 */

/* --- Detalhes dinâmicos por tamanho de projeto --- */
function showSizeDetails() {
  const size   = document.getElementById('form-size').value;
  const detail = document.getElementById('size-detail');
  const text   = document.getElementById('size-detail-text');

  const messages = {
    'pequeno':   'Projetos de até 10 caixas geralmente são concluídos em 3–5 dias úteis. Ideal para arquivos departamentais ou acervos específicos.',
    'medio':     'Projetos de 10 a 50 caixas são nosso volume mais comum. Prazo médio de 2–3 semanas com equipe dedicada.',
    'grande':    'Projetos de 50 a 200 caixas recebem gerente de projeto exclusivo e cronograma detalhado. Podemos operar in-loco na sua empresa.',
    'enterprise':'Projetos enterprise recebem tratamento VIP: equipe dedicada, gerente de projeto, operação in-loco e SLA personalizado. Agende uma visita técnica.',
    'nao-sei':   'Sem problema! Nosso consultor fará uma avaliação gratuita do seu acervo e estimará o volume. Basta preencher o restante do formulário.'
  };

  if (messages[size]) {
    text.textContent = messages[size];
    detail.classList.remove('hidden');
  } else {
    detail.classList.add('hidden');
  }
}

/* --- Submissão do formulário --- */
function handleFormSubmit(e) {
  e.preventDefault();

  const formData = {
    name:    document.getElementById('form-name').value,
    email:   document.getElementById('form-email').value,
    phone:   document.getElementById('form-phone').value,
    company: document.getElementById('form-company').value,
    segment: document.getElementById('form-segment').value,
    size:    document.getElementById('form-size').value,
    message: document.getElementById('form-message').value,
  };

  // TODO: integrar com RD Station / EmailJS / backend
  console.log('Lead capturado:', formData);

  document.getElementById('quote-form').classList.add('hidden');
  const success = document.getElementById('form-success');
  success.classList.remove('hidden');

  if (window.SmoothScroll) {
    const top = success.getBoundingClientRect().top + window.scrollY - 80;
    SmoothScroll.scrollTo(top);
  }
}

/* --- Máscara de telefone --- */
document.addEventListener('DOMContentLoaded', () => {
  const phoneInput = document.getElementById('form-phone');
  if (!phoneInput) return;

  phoneInput.addEventListener('input', function () {
    let v = this.value.replace(/\D/g, '').slice(0, 11);
    if      (v.length > 6) v = `(${v.slice(0,2)}) ${v.slice(2,7)}-${v.slice(7)}`;
    else if (v.length > 2) v = `(${v.slice(0,2)}) ${v.slice(2)}`;
    else if (v.length > 0) v = `(${v}`;
    this.value = v;
  });

  /* --- Tooltip do WhatsApp (aparece após 5s) --- */
  setTimeout(() => {
    const tooltip = document.getElementById('wa-tooltip');
    if (!tooltip) return;
    tooltip.classList.remove('hidden');
    setTimeout(() => tooltip.classList.add('hidden'), 8000);
  }, 5000);
});
