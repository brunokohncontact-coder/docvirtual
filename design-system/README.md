# Design system — Doc Virtual

Bundle pronto para subir no projeto de design system da Doc Virtual no
[Claude Design](https://claude.ai/design). Cobre a seção de marca: os dois logos,
as variações, cor, tipografia, área de respiro e usos incorretos.

## Por que ele está aqui e não lá

O push é feito pela ferramenta `DesignSync`, que exige uma autorização de
design-system concedida por login interativo (`/design-login`). A sessão que gerou
estes arquivos rodava num container remoto, sem terminal interativo, então a
escrita no projeto não pôde ser feita de lá. O bundle ficou versionado aqui para
que o push seja um passo só, de um ambiente autorizado.

## Estrutura

```
design-system/
  marca/
    logo-doc-virtual.html          marca principal
    logo-doc-virtual-ged.html      lockup da plataforma
    variacoes.html                 3 versões × 3 marcas
    simbolo.html                   nuvem isolada
  fundamentos/
    cores.html                     cores da marca + tokens navy/accent
    tipografia.html                Didact Gothic + Inter
    respiro-e-tamanho-minimo.html  área de respiro e mínimos
    usos-incorretos.html           seis erros recorrentes
  assets/                          os 9 SVGs (cópia de assets/img/logo/svg/)
  _register_assets.json            fallback de registro explícito
  build.py                         regera tudo a partir de assets/img/logo/svg/
```

Cada preview é um HTML autocontido: os SVGs entram **inline**, então o card
renderiza mesmo que o pane não resolva caminhos relativos. As únicas dependências
externas são as fontes do Google Fonts (Inter e Didact Gothic), com stack de
fallback declarada.

A primeira linha de cada preview carrega o marcador que alimenta o índice do
Design System pane:

```html
<!-- @dsCard group="Marca" name="Logo Doc Virtual" subtitle="..." width="760" height="440" -->
```

O atributo `group` é o que a documentação da ferramenta descreve; `name`,
`subtitle`, `width` e `height` foram incluídos espelhando os campos que
`register_assets` aceita. **Se o pane ignorar esses quatro**, os cards ainda
entram — só ficam sem rótulo/dimensão. Nesse caso use `_register_assets.json`,
que traz os mesmos metadados no formato do `register_assets` legado.

## Como subir

De um ambiente com a autorização de design-system (Claude Code local com
`/design-login` feito, ou um workspace semeado pelo "Send to Claude Code Web"):

1. `list_projects` — achar o projeto do design system da Doc Virtual.
2. `get_project` — confirmar que ele é `type: PROJECT_TYPE_DESIGN_SYSTEM`
   (o tipo é imutável; empurrar para um projeto comum não o transforma em
   design system).
3. `finalize_plan` — `writes: ["marca/**/*.html", "fundamentos/**/*.html", "assets/**/*.svg"]`,
   `localDir` apontando para esta pasta.
4. `write_files` — 17 arquivos (8 previews + 9 SVGs), usando `localPath`.
5. Se os cards não aparecerem rotulados, `register_assets` com o conteúdo de
   `_register_assets.json` (ajustando `path` para ser relativo ao projeto, sem o
   prefixo `design-system/`).

Os caminhos em `_register_assets.json` estão relativos à raiz do repo. Se o
projeto no Claude Design receber esta pasta como raiz, remova o prefixo
`design-system/`.

## Manutenção

Os SVGs em `assets/` são cópia de `assets/img/logo/svg/`, que é a fonte de
verdade da marca. Ao mexer no logo, atualize lá primeiro e rode `python3
design-system/build.py` — os previews têm o SVG embutido, então precisam ser
regerados junto. O script usa só a biblioteca padrão do Python.

A mesma seção de marca existe também como canvas visual (artifact do Claude
Design canvas), útil para revisar e exportar PNG/PDF sem subir nada.
