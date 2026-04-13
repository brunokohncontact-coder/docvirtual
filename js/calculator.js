/**
 * calculator.js
 * Calculadora de liberação de espaço.
 * calculateSpace() e shareCalculation() são globais (usadas nos onclick do HTML).
 */
function calculateSpace() {
  const boxes  = parseInt(document.getElementById('box-count').value);
  const costSqm = parseInt(document.getElementById('cost-sqm').value);

  const sqmPerBox   = 0.12;
  const pagesPerBox = 2500;
  const totalArea   = (boxes * sqmPerBox).toFixed(1);
  const monthly     = Math.round(totalArea * costSqm);
  const yearly      = monthly * 12;

  document.getElementById('box-count-display').textContent = boxes;
  document.getElementById('cost-display').textContent      = 'R$ ' + costSqm;
  document.getElementById('result-area').textContent       = totalArea;
  document.getElementById('result-monthly').textContent    = 'R$ ' + monthly.toLocaleString('pt-BR');
  document.getElementById('result-yearly').textContent     = 'R$ ' + yearly.toLocaleString('pt-BR');
  document.getElementById('result-pages').textContent      = (boxes * pagesPerBox).toLocaleString('pt-BR');

  // Atualiza preenchimento visual das barras
  const boxRange  = document.getElementById('box-count');
  const costRange = document.getElementById('cost-sqm');
  boxRange.style.setProperty('--range-progress',  ((boxes - 5)    / (500 - 5)   * 100) + '%');
  costRange.style.setProperty('--range-progress', ((costSqm - 50) / (400 - 50) * 100) + '%');
}

function shareCalculation() {
  const boxes   = document.getElementById('box-count').value;
  const area    = document.getElementById('result-area').textContent;
  const monthly = document.getElementById('result-monthly').textContent;
  const yearly  = document.getElementById('result-yearly').textContent;

  const text =
    `Doc Virtual — Calculadora de Liberação de Espaço\n\n` +
    `Com ${boxes} caixas-box, poderíamos liberar ${area} m².\n` +
    `Economia estimada: ${monthly}/mês (${yearly}/ano).\n\n` +
    `Simule você também: docvirtual.com.br`;

  if (navigator.share) {
    navigator.share({ title: 'Calculadora Doc Virtual', text });
  } else {
    navigator.clipboard.writeText(text).then(() =>
      alert('Dados copiados! Cole e envie para sua equipe.')
    );
  }
}

// Inicializa ao carregar
document.addEventListener('DOMContentLoaded', calculateSpace);
