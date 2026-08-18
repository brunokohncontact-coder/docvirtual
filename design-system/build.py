# -*- coding: utf-8 -*-
"""Monta o bundle do design system da Doc Virtual no formato do Claude Design.

Cada preview e um HTML autocontido: os SVGs entram inline, entao o card
renderiza mesmo que o pane nao resolva caminhos relativos. A primeira linha de
cada arquivo carrega o marcador @dsCard que alimenta o indice do pane.
"""
import os, re, json

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(REPO, 'assets/img/logo/svg')
OUT = os.path.join(REPO, 'design-system')

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Inter:wght@400;500;600;700&family=Didact+Gothic&display=swap">')
BASE_CSS = """
    :root { color-scheme: light; }
    body { margin: 0; font-family: Inter, system-ui, sans-serif; background: #ffffff;
           color: #102a43; -webkit-font-smoothing: antialiased; }
    a { color: #2563eb; } a:hover { color: #1d4ed8; }
    .eyebrow { font-size: 11px; font-weight: 600; letter-spacing: 0.14em;
               text-transform: uppercase; color: #829ab1; }
    .h { font-size: 26px; font-weight: 700; letter-spacing: -0.02em; color: #102a43; }
    .lead { font-size: 14px; line-height: 1.6; color: #486581; }
    .meta { font-size: 12px; color: #829ab1; }
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
    .panel { border: 1px solid #d9e2ec; background: #ffffff; }
"""

_svg_cache = {}

def svg(name, width, extra_style=''):
    """SVG inline, com a largura forcada por style (sobrepoe width/height do arquivo)."""
    if name not in _svg_cache:
        _svg_cache[name] = open(os.path.join(SVG_DIR, name + '.svg')).read().strip()
    s = _svg_cache[name]
    style = f'width: {width}px; height: auto; display: block; {extra_style}'.strip()
    return re.sub(r'^<svg ', f'<svg style="{style}" ', s, count=1)

def card(path, group, name, subtitle, w, h, body):
    marker = (f'<!-- @dsCard group="{group}" name="{name}" subtitle="{subtitle}" '
              f'width="{w}" height="{h}" -->')
    html = f"""{marker}
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{name} — Doc Virtual</title>
{FONTS}
<style>{BASE_CSS}
    .frame {{ width: {w}px; height: {h}px; box-sizing: border-box; padding: 36px 40px;
              display: flex; flex-direction: column; gap: 22px; }}
</style>
</head>
<body>
<div class="frame">
{body}
</div>
</body>
</html>
"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(html)
    return dict(name=name, path=f'design-system/{path}', subtitle=subtitle,
                group=group, viewport=dict(width=w, height=h))

def head(eyebrow, title, lead=None):
    out = (f'<div style="display: flex; flex-direction: column; gap: 6px">'
           f'<div class="eyebrow">{eyebrow}</div><div class="h">{title}</div>')
    if lead:
        out += f'<div class="lead" style="max-width: 620px; margin-top: 2px">{lead}</div>'
    return out + '</div>'

cards = []

# ---------------------------------------------------------------- marca ----
cards.append(card(
    'marca/logo-doc-virtual.html', 'Marca', 'Logo Doc Virtual',
    'Colorida, branca e monocromática', 760, 440,
    head('Marca', 'Doc Virtual',
         'Marca da empresa. Assinatura padrão em site, propostas, contratos e '
         'apresentações institucionais.') +
    f'''
  <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center;
              background: #f0f4f8; border: 1px solid #d9e2ec">
    {svg('doc-virtual', 420)}
  </div>
  <div style="display: flex; justify-content: space-between; align-items: baseline">
    <div class="meta mono">assets/img/logo/svg/doc-virtual.svg</div>
    <div class="meta">Mínimo 110 px · 30 mm</div>
  </div>'''))

cards.append(card(
    'marca/logo-doc-virtual-ged.html', 'Marca', 'Logo Doc Virtual GED',
    'Lockup da plataforma', 880, 440,
    head('Marca', 'Doc Virtual GED',
         'Marca da plataforma: a Doc Virtual seguida de divisor e da assinatura GED em '
         'navy. Usada dentro do produto e nas peças da campanha da plataforma.') +
    f'''
  <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center;
              background: #f0f4f8; border: 1px solid #d9e2ec">
    {svg('doc-virtual-ged', 520)}
  </div>
  <div style="display: flex; justify-content: space-between; align-items: baseline">
    <div class="meta mono">assets/img/logo/svg/doc-virtual-ged.svg</div>
    <div class="meta">Mínimo 150 px · 40 mm</div>
  </div>'''))

cards.append(card(
    'marca/simbolo.html', 'Marca', 'Símbolo',
    'Nuvem isolada para avatar e favicon', 620, 420,
    head('Marca', 'Símbolo',
         'A nuvem com o lettering “doc” funciona sozinha em avatar, favicon e selo. '
         'Nunca é remontada com o lettering digitado em outra fonte.') +
    f'''
  <div style="flex-grow: 1; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));
              gap: 1px; background: #d9e2ec; border: 1px solid #d9e2ec">
    <div style="background: #f0f4f8; display: flex; align-items: center; justify-content: center; padding: 22px">{svg('simbolo-doc', 110)}</div>
    <div style="background: #102a43; display: flex; align-items: center; justify-content: center; padding: 22px">{svg('simbolo-doc-branco', 110)}</div>
    <div style="background: #ffffff; display: flex; align-items: center; justify-content: center; padding: 22px">{svg('simbolo-doc-navy', 110)}</div>
  </div>
  <div class="meta">Mínimo 24 px · 8 mm</div>'''))

rows = [('Marca', 'doc-virtual', 230), ('Plataforma', 'doc-virtual-ged', 270),
        ('Símbolo', 'simbolo-doc', 100)]
grid = ''
for label, base, w in rows:
    grid += f'''
    <div style="background: #ffffff; padding: 16px; display: flex; flex-direction: column;
                justify-content: center; gap: 3px">
      <div style="font-size: 13px; font-weight: 600">{label}</div>
      <div class="meta mono" style="font-size: 11px">{base}</div>
    </div>
    <div style="background: #f0f4f8; display: flex; align-items: center; justify-content: center; padding: 26px">{svg(base, w)}</div>
    <div style="background: #102a43; display: flex; align-items: center; justify-content: center; padding: 26px">{svg(base + '-branco', w)}</div>
    <div style="background: #ffffff; display: flex; align-items: center; justify-content: center; padding: 26px">{svg(base + '-navy', w)}</div>'''

cards.append(card(
    'marca/variacoes.html', 'Marca', 'Variações',
    'Colorida, branca e monocromática × marca, GED e símbolo', 1120, 720,
    head('Marca', 'Variações',
         'A escolha é do fundo, não do gosto: colorida em fundo claro, branca em fundo '
         'escuro ou foto, monocromática quando só há uma cor disponível.') +
    f'''
  <div style="flex-grow: 1; display: grid; grid-template-columns: 140px repeat(3, minmax(0, 1fr));
              gap: 1px; background: #d9e2ec; border: 1px solid #d9e2ec">
    <div style="background: #ffffff"></div>
    <div style="background: #ffffff; padding: 12px 16px"><div style="font-size: 13px; font-weight: 600">Colorida</div><div class="meta">Fundo claro</div></div>
    <div style="background: #ffffff; padding: 12px 16px"><div style="font-size: 13px; font-weight: 600">Branca</div><div class="meta">Fundo escuro, foto</div></div>
    <div style="background: #ffffff; padding: 12px 16px"><div style="font-size: 13px; font-weight: 600">Monocromática</div><div class="meta">Impressão em 1 cor</div></div>{grid}
  </div>
  <div class="meta">Na branca e na monocromática o lettering “doc” é vazado: quem aparece dentro das letras é o fundo.</div>'''))

# --------------------------------------------------------- fundamentos ----
def swatch(hex_, nome, nota):
    return f'''
    <div class="panel" style="display: flex; flex-direction: column">
      <div style="height: 84px; background: {hex_}"></div>
      <div style="padding: 12px 14px; display: flex; flex-direction: column; gap: 2px">
        <div style="font-size: 13px; font-weight: 600">{nome}</div>
        <div class="mono" style="font-size: 12px; color: #486581">{hex_}</div>
        <div class="meta" style="line-height: 1.45; margin-top: 2px">{nota}</div>
      </div>
    </div>'''

ramp = ''.join(f'<div style="flex-grow: 1; background: {c}"></div>' for c in
               ['#f0f4f8', '#d9e2ec', '#bcccdc', '#9fb3c8', '#829ab1', '#627d98',
                '#486581', '#334e68', '#243b53', '#102a43', '#0a1929'])
accent = ''.join(f'<div style="flex-grow: 1; background: {c}"></div>' for c in
                 ['#60a5fa', '#3b82f6', '#2563eb', '#1d4ed8'])

cards.append(card(
    'fundamentos/cores.html', 'Fundamentos', 'Cores',
    'Marca + tokens navy e accent', 1120, 550,
    head('Fundamentos', 'Cores') +
    f'''
  <div style="display: flex; flex-direction: column; gap: 10px">
    <div class="eyebrow">Cores da marca</div>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px">
      {swatch('#054B90', 'Azul Doc', 'Extremo claro do degradê da nuvem')}
      {swatch('#00366D', 'Azul Navy', 'Extremo escuro, assinatura GED e versão monocromática')}
      {swatch('#737373', 'Cinza lettering', 'Palavra “virtual”')}
      <div class="panel" style="display: flex; flex-direction: column">
        <div style="height: 84px; background: linear-gradient(135deg, #054B90 0%, #00366D 100%)"></div>
        <div style="padding: 12px 14px; display: flex; flex-direction: column; gap: 2px">
          <div style="font-size: 13px; font-weight: 600">Degradê da nuvem</div>
          <div class="mono" style="font-size: 12px; color: #486581">135°</div>
          <div class="meta" style="line-height: 1.45; margin-top: 2px">Sempre do canto superior esquerdo para o inferior direito</div>
        </div>
      </div>
    </div>
  </div>
  <div style="display: flex; flex-direction: column; gap: 10px">
    <div class="eyebrow">Paleta do produto</div>
    <div style="display: flex; gap: 18px">
      <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px">
        <div style="display: flex; height: 52px; border: 1px solid #d9e2ec">{ramp}</div>
        <div style="display: flex; justify-content: space-between">
          <div style="font-size: 12px; font-weight: 500; color: #334e68">navy · 50 → 950</div>
          <div class="meta mono">#f0f4f8 → #0a1929</div>
        </div>
      </div>
      <div style="width: 320px; display: flex; flex-direction: column; gap: 6px">
        <div style="display: flex; height: 52px; border: 1px solid #d9e2ec">{accent}</div>
        <div style="display: flex; justify-content: space-between">
          <div style="font-size: 12px; font-weight: 500; color: #334e68">accent · 400 → 700</div>
          <div class="meta mono">#60a5fa → #1d4ed8</div>
        </div>
      </div>
    </div>
  </div>
  <div class="lead" style="border-top: 1px solid #d9e2ec; padding-top: 14px; max-width: none">O azul do logo e o accent do produto são cores diferentes e não se substituem: o logo nunca é pintado de <span class="mono" style="font-size: 13px; color: #102a43">#2563eb</span>, e botão não é pintado de <span class="mono" style="font-size: 13px; color: #102a43">#054B90</span>.</div>'''))

cards.append(card(
    'fundamentos/tipografia.html', 'Fundamentos', 'Tipografia',
    'Didact Gothic na marca, Inter no resto', 1120, 640,
    head('Fundamentos', 'Tipografia',
         'Duas fontes com papéis separados: uma desenha a marca, a outra escreve tudo o resto.') +
    '''
  <div style="flex-grow: 1; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px">
    <div class="panel" style="display: flex; flex-direction: column">
      <div style="padding: 24px 26px 20px; border-bottom: 1px solid #d9e2ec">
        <div class="eyebrow">Marca</div>
        <div style="font-size: 21px; font-weight: 600; margin-top: 4px">Didact Gothic</div>
        <div class="meta" style="margin-top: 2px">Google Fonts · um peso</div>
      </div>
      <div style="padding: 24px 26px; display: flex; flex-direction: column; gap: 14px; flex-grow: 1">
        <div style="font-family: 'Didact Gothic', system-ui, sans-serif; font-size: 46px; line-height: 1.15">virtual</div>
        <div style="font-family: 'Didact Gothic', system-ui, sans-serif; font-size: 26px; color: #00366D; letter-spacing: 0.06em">GED</div>
        <div style="font-family: 'Didact Gothic', system-ui, sans-serif; font-size: 15px; color: #486581; line-height: 1.5">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div>
      </div>
      <div style="padding: 16px 26px 20px; border-top: 1px solid #d9e2ec" class="lead">Nos arquivos do logo ela já está convertida em curvas — a fonte só é necessária para criar peças novas com o mesmo lettering.</div>
    </div>
    <div class="panel" style="display: flex; flex-direction: column">
      <div style="padding: 24px 26px 20px; border-bottom: 1px solid #d9e2ec">
        <div class="eyebrow">Interface e texto</div>
        <div style="font-size: 21px; font-weight: 600; margin-top: 4px">Inter</div>
        <div class="meta" style="margin-top: 2px">400 · 500 · 600 · 700</div>
      </div>
      <div style="padding: 24px 26px; display: flex; flex-direction: column; gap: 16px; flex-grow: 1">
        <div style="display: flex; align-items: baseline; gap: 18px"><div class="mono" style="width: 84px; font-size: 11px; color: #829ab1">40 / 700</div><div style="font-size: 30px; font-weight: 700; letter-spacing: -0.02em">Título</div></div>
        <div style="display: flex; align-items: baseline; gap: 18px"><div class="mono" style="width: 84px; font-size: 11px; color: #829ab1">20 / 600</div><div style="font-size: 19px; font-weight: 600">Subtítulo de seção</div></div>
        <div style="display: flex; align-items: baseline; gap: 18px"><div class="mono" style="width: 84px; font-size: 11px; color: #829ab1">15 / 400</div><div style="font-size: 15px; color: #334e68">Corpo de texto, altura de linha 1,6.</div></div>
        <div style="display: flex; align-items: baseline; gap: 18px"><div class="mono" style="width: 84px; font-size: 11px; color: #829ab1">11 / 600</div><div class="eyebrow" style="color: #627d98">Rótulo</div></div>
      </div>
      <div style="padding: 16px 26px 20px; border-top: 1px solid #d9e2ec" class="lead">Já é a fonte do site. Todo texto fora do logo usa Inter — inclusive quando o nome “Doc Virtual” aparece escrito, e não como marca.</div>
    </div>
  </div>'''))

cards.append(card(
    'fundamentos/respiro-e-tamanho-minimo.html', 'Fundamentos', 'Respiro e tamanho mínimo',
    'x = metade da altura do símbolo', 1120, 620,
    head('Fundamentos', 'Área de respiro e tamanho mínimo') +
    f'''
  <div style="flex-grow: 1; display: grid; grid-template-columns: minmax(0, 1.45fr) minmax(0, 1fr); gap: 26px">
    <div class="panel" style="display: flex; flex-direction: column">
      <div style="padding: 18px 24px 14px; border-bottom: 1px solid #d9e2ec; display: flex; align-items: baseline; gap: 12px">
        <div style="font-size: 15px; font-weight: 600">Área de respiro</div>
        <div class="meta">x = metade da altura do símbolo</div>
      </div>
      <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; background: #f0f4f8; padding: 28px">
        <div style="position: relative; padding: 43px; border: 1px dashed #627d98; background: rgba(37, 99, 235, 0.09)">
          {svg('doc-virtual', 300, 'background: #ffffff; outline: 1px solid #9fb3c8;')}
          <div style="position: absolute; left: 0; right: 0; top: 0; height: 43px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: #2563eb">x</div>
          <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 43px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: #2563eb">x</div>
          <div style="position: absolute; top: 0; bottom: 0; left: 0; width: 43px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: #2563eb">x</div>
          <div style="position: absolute; top: 0; bottom: 0; right: 0; width: 43px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: #2563eb">x</div>
        </div>
      </div>
      <div style="padding: 16px 24px 18px; border-top: 1px solid #d9e2ec" class="lead">Nada entra na faixa marcada — nem texto, nem foto, nem borda, nem outro logo. Em cabeçalho apertado, reduza o logo antes de reduzir o respiro.</div>
    </div>
    <div class="panel" style="display: flex; flex-direction: column">
      <div style="padding: 18px 24px 14px; border-bottom: 1px solid #d9e2ec; font-size: 15px; font-weight: 600">Tamanho mínimo</div>
      <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: center; gap: 22px; padding: 24px">
        <div style="display: flex; align-items: center; gap: 18px">
          <div style="width: 160px">{svg('doc-virtual', 110)}</div>
          <div><div style="font-size: 13px; font-weight: 600">Marca</div><div class="lead" style="font-size: 13px">110 px · 30 mm</div></div>
        </div>
        <div style="height: 1px; background: #d9e2ec"></div>
        <div style="display: flex; align-items: center; gap: 18px">
          <div style="width: 160px">{svg('doc-virtual-ged', 150)}</div>
          <div><div style="font-size: 13px; font-weight: 600">Lockup GED</div><div class="lead" style="font-size: 13px">150 px · 40 mm</div></div>
        </div>
        <div style="height: 1px; background: #d9e2ec"></div>
        <div style="display: flex; align-items: center; gap: 18px">
          <div style="width: 160px">{svg('simbolo-doc', 24)}</div>
          <div><div style="font-size: 13px; font-weight: 600">Símbolo</div><div class="lead" style="font-size: 13px">24 px · 8 mm</div></div>
        </div>
      </div>
      <div style="padding: 16px 24px 18px; border-top: 1px solid #d9e2ec" class="lead">Abaixo disso as linhas do documento dentro do “o” fecham e a marca vira um borrão.</div>
    </div>
  </div>'''))

X = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="flex-shrink: 0; margin-top: 1px">'
     '<circle cx="8" cy="8" r="7" stroke="#b91c1c" stroke-width="1.4"/>'
     '<path d="M5.5 5.5l5 5M10.5 5.5l-5 5" stroke="#b91c1c" stroke-width="1.4" stroke-linecap="round"/></svg>')

def dont(inner, texto, bg='#f0f4f8'):
    return f'''
    <div class="panel" style="display: flex; flex-direction: column">
      <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center;
                  background: {bg}; padding: 22px; overflow: hidden">{inner}</div>
      <div style="padding: 12px 16px 14px; border-top: 1px solid #d9e2ec; display: flex; gap: 9px;
                  align-items: flex-start; min-height: 64px; box-sizing: border-box">
        {X}<div style="font-size: 13px; color: #334e68; line-height: 1.5">{texto}</div>
      </div>
    </div>'''

remontado = (f'<div style="display: flex; align-items: center; gap: 12px">{svg("simbolo-doc", 62)}'
             f'<div style="font-size: 28px; font-weight: 600; color: #737373">virtual</div></div>')

cards.append(card(
    'fundamentos/usos-incorretos.html', 'Fundamentos', 'Usos incorretos',
    'Seis erros recorrentes', 1120, 720,
    head('Fundamentos', 'Usos incorretos',
         'Todos têm a mesma solução: pegar o arquivo certo em '
         '<span class="mono" style="font-size: 13px; color: #102a43">assets/img/logo/</span>.') +
    f'''
  <div style="flex-grow: 1; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));
              grid-template-rows: repeat(2, minmax(0, 1fr)); gap: 20px">
    {dont(svg('doc-virtual', 210, 'transform: scaleX(1.35); transform-origin: center;'), 'Não distorcer. Redimensione sempre travando a proporção.')}
    {dont(svg('doc-virtual', 210, 'filter: hue-rotate(115deg) saturate(1.6);'), 'Não trocar as cores nem inverter o sentido do degradê.')}
    {dont(svg('doc-virtual', 210), 'Não usar a colorida em fundo escuro — o “virtual” some. Use a branca.', '#102a43')}
    {dont(svg('doc-virtual', 210, 'filter: drop-shadow(4px 6px 5px rgba(16, 42, 67, 0.55));'), 'Não aplicar sombra, contorno ou brilho.')}
    {dont(remontado, 'Não remontar a marca digitando “virtual” em outra fonte.')}
    {dont(svg('doc-virtual-ged', 230, 'transform: rotate(-9deg);'), 'Não girar. A marca é sempre horizontal.')}
  </div>'''))

# --------------------------------------------------- assets + manifesto ----
os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
for f in sorted(os.listdir(SVG_DIR)):
    open(os.path.join(OUT, 'assets', f), 'w').write(open(os.path.join(SVG_DIR, f)).read())

open(os.path.join(OUT, '_register_assets.json'), 'w').write(
    json.dumps(cards, ensure_ascii=False, indent=2) + '\n')

print(f'{len(cards)} cards + {len(os.listdir(os.path.join(OUT, "assets")))} assets')
for c in cards:
    print(f'  {c["group"]:12s} {c["path"]}')
