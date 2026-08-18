# Logos — Doc Virtual

Versões vetoriais da marca **Doc Virtual** e do lockup **Doc Virtual GED**.
Até aqui o repositório só tinha `assets/img/Logo-site.png` e `Logo-site-branco.png`,
ambos em 150 × 43 px — resolução insuficiente para qualquer uso fora do header do
site, e sem nenhuma versão do GED.

Os SVGs são a fonte de verdade: contorno único, sem máscara e sem fonte embutida
(o lettering está convertido em curvas), então abrem igual em navegador, Illustrator,
Figma e Adobe Express, e recolorem trocando um único `fill`.

## Arquivos

| Arquivo | Uso |
| --- | --- |
| `doc-virtual` | Marca principal. Fundos claros. |
| `doc-virtual-branco` | Fundos escuros, foto, vídeo. |
| `doc-virtual-navy` | Monocromática. Impressão em 1 cor, fax, carimbo, gravação. |
| `doc-virtual-ged` | Lockup da plataforma GED. Fundos claros. |
| `doc-virtual-ged-branco` | Lockup GED em fundos escuros. |
| `doc-virtual-ged-navy` | Lockup GED monocromático. |
| `simbolo-doc` | Só o símbolo. Avatar, favicon, selo, app. |
| `simbolo-doc-branco` | Símbolo em fundos escuros. |
| `simbolo-doc-navy` | Símbolo monocromático. |

`svg/` para qualquer aplicação (escala sem perda). `png/` com fundo transparente e
400 px de altura, para quem precisa de bitmap (PowerPoint, e‑mail, redes sociais).

## Cores

| Cor | Hex | Onde |
| --- | --- | --- |
| Azul Doc | `#054B90` | extremo claro do degradê da nuvem |
| Azul Navy | `#00366D` | extremo escuro do degradê, "GED", versão monocromática |
| Cinza lettering | `#737373` | palavra "virtual" |
| Branco | `#FFFFFF` | letras "doc" vazadas, versão para fundo escuro |

O degradê da nuvem é linear, do canto superior esquerdo (azul Doc) para o inferior
direito (navy).

## Tipografia

O lettering "virtual" e a assinatura "GED" usam **Didact Gothic** — geométrica de
caixa baixa com "a" de um andar, a que mais se aproxima do desenho original da marca.
Nos arquivos ela já está convertida em curvas; a fonte só é necessária para criar
peças novas com o mesmo lettering (disponível no Google Fonts).

## Área de respiro

Reserve em volta do logo, de todos os lados, uma margem igual a **metade da altura do
símbolo** (a nuvem). Nada — texto, foto, borda, outro logo — entra nessa área.

## Tamanho mínimo

| | Digital | Impresso |
| --- | --- | --- |
| Marca completa | 110 px de largura | 30 mm |
| Lockup GED | 150 px de largura | 40 mm |
| Símbolo | 24 px | 8 mm |

## O que não fazer

- Não redesenhar, reescrever ou trocar a fonte do lettering.
- Não mudar as cores nem aplicar o degradê em outra direção.
- Não distorcer: redimensione sempre travando a proporção.
- Não aplicar a versão colorida sobre fundo escuro ou sobre foto sem contraste —
  use a versão branca.
- Não adicionar sombra, contorno, brilho ou rotação.
- Não separar o símbolo do lettering para recriar a marca; se precisar só do símbolo,
  use os arquivos `simbolo-doc`.
