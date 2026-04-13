/**
 * doc-stack.js
 * 3D interactive document stack — IntersectionObserver spread + mouse tilt + click.
 */
(function () {
  const wrapper = document.getElementById('doc-stack-wrapper');
  const stack   = document.getElementById('doc-stack');
  const cards   = Array.from(document.querySelectorAll('.doc-card'));
  const hint    = document.getElementById('stack-hint');

  if (!wrapper || !stack || !cards.length) return;

  /* ── Posições espalhadas (fan) ─────────────────────────────────── */
  const spread = [
    { z:  90, ry: -12, rz: -5, tx: -24, ty: -8  },
    { z:  45, ry:  -6, rz: -2, tx: -12, ty: -4  },
    { z:   0, ry:   0, rz:  0, tx:   0, ty:  0  },
    { z: -45, ry:   6, rz:  2, tx:  12, ty:  4  },
    { z: -90, ry:  12, rz:  5, tx:  24, ty:  8  },
  ];

  /* ── Posições empilhadas (pilha) ───────────────────────────────── */
  const stacked = cards.map((_, i) => ({
    z: -i * 6, ry: 0, rz: 0, tx: i * 2, ty: i * 2
  }));

  let isSpread = false;

  function setTransform(card, p) {
    card.style.transform =
      `translateX(calc(-50% + ${p.tx}px)) ` +
      `translateY(calc(-50% + ${p.ty}px)) ` +
      `translateZ(${p.z}px) ` +
      `rotateY(${p.ry}deg) ` +
      `rotateZ(${p.rz}deg)`;
  }

  function stackAll() {
    cards.forEach((c, i) => {
      c.style.transition = 'transform 0.7s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s';
      c.style.zIndex = cards.length - i;
      setTransform(c, stacked[i]);
    });
    isSpread = false;
    if (hint) hint.style.opacity = '1';
  }

  function spreadAll() {
    cards.forEach((c, i) => {
      c.style.transition = 'transform 0.8s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s';
      c.style.zIndex = i + 1;
      setTransform(c, spread[i]);
    });
    isSpread = true;
    if (hint) hint.style.opacity = '0';
  }

  function bringForward(idx) {
    cards.forEach((c, i) => {
      c.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s';
      if (i === idx) {
        c.style.zIndex = 100;
        c.style.transform =
          `translateX(-50%) translateY(-55%) ` +
          `translateZ(150px) rotateY(0deg) rotateZ(0deg)`;
      } else {
        c.style.zIndex = i + 1;
        setTransform(c, spread[i]);
      }
    });
  }

  /* ── Click ─────────────────────────────────────────────────────── */
  cards.forEach((card, idx) => {
    card.addEventListener('click', () => {
      if (!isSpread) { spreadAll(); return; }
      bringForward(idx);
    });
  });

  /* ── Mouse tilt ─────────────────────────────────────────────────── */
  wrapper.addEventListener('mousemove', (e) => {
    const r  = wrapper.getBoundingClientRect();
    const nx = (e.clientX - r.left)  / r.width  - 0.5;
    const ny = (e.clientY - r.top)   / r.height - 0.5;
    stack.style.transition = 'transform 0.08s linear';
    stack.style.transform  = `rotateX(${-ny * 14}deg) rotateY(${nx * 18}deg)`;
  });

  wrapper.addEventListener('mouseleave', () => {
    stack.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    stack.style.transform  = 'rotateX(0deg) rotateY(0deg)';
  });

  /* ── IntersectionObserver — dispara o spread no scroll ─────────── */
  const io = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting && !isSpread) {
      setTimeout(spreadAll, 350);
      io.disconnect();
    }
  }, { threshold: 0.3 });

  io.observe(wrapper);
  stackAll();
})();
