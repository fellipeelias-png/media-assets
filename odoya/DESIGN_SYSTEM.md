# Odoya Store — Design System (resumo para geração de artes)

Fonte completa: artifact "Odoya Store | Brand kit and voice" no claude.ai
(https://claude.ai/artifact/H5HnAQbtBuRnDjkEC9TduY). Este arquivo é um resumo
local para o Claude Code usar ao gerar artes (Pinterest, posts, etc), já que
o Claude Code não tem acesso aos artifacts do claude.ai.

Versão: v1, 4 Nov 2026 (copiado do projeto Odoya Store no claude.ai em 9 Nov 2026).

## Cores

- `night-900` `#0f0f39`, `night-700` `#1b195a` — fundos indigo
- Gradiente de título, esquerda para direita: `sky-300` `#88aaff` → `violet-300` `#a38dff` → `orchid-300` `#d283e2`
- `gold-400` `#f2c94c` — um acento por área, nunca em excesso
- Texto branco
- `mist` `#c9c7ef` — legendas e textos secundários

## Tipografia

- Títulos: Anton, uppercase, preenchimento em gradiente
- Corpo: Barlow
- Posts com foto: Amatic SC no título e Quicksand no corpo (provisório, confirmar antes de usar)

## Layout

- Tamanho padrão: 1080 x 1350
- Cabeçalho: "ODOYA STORE", linha fina (hairline), contador de slide
- Elemento gráfico: linha de flower-of-life
- Botões em formato pill
- Rodapé no último slide: "LINK IN BIO · ODOYAMARKETPLACE"
- Carrossel padrão de 4 peças: capa com pessoa, detalhe, especificações + preço "From", fechamento com "Shop now on Etsy" e "Share with a friend"

## Voz e copy

- Todo texto público em inglês
- Nunca usar travessão (em dash)
- Título: 2 a 5 palavras. Corpo: 1 a 3 linhas curtas
- Tom: calmo, curioso, respeitoso, direto
- Ordem: produto primeiro, depois conceito, depois uma única CTA
- Preço sempre com o rótulo "From" ou "Starts from"
- UFO, 2027 e qualquer afirmação espiritual como "believers say", nunca como fato ou promessa
- Nunca prometer proteção ou sorte
- Respeitar as fontes culturais (Orishas, Thunderbird, Adinkra, Ubuntu); nunca dizer "made by native artists"
- Evitar hype e palavras de enchimento: unlock, elevate, journey, game-changer, "more than just a shirt"

## Regras de conteúdo (todas as peças Odoya)

- Conteúdo de Instagram (story ou carrossel) sempre com no mínimo 3 peças, nesta ordem: foto do produto, explicação do produto e conceito, CTA
- Preço sempre com o rótulo "starts from" acima do valor, em toda peça sem exceção
- 100% do conteúdo (posts, artes, copy) em inglês
- Posts de Instagram usam o visual indigo (não o azul-oceano do site odoya.store)
- Vídeo ou post com pessoa gerada por IA vestindo as camisetas precisa do aviso de IA (nos vídeos, no final)
- Capa/thumbnail de vídeo ou Reel sempre mostra o produto, com o mesmo enquadramento e altura do modelo em todas as capas, para manter o feed uniforme
- Links para a loja sempre usam o endereço odoyamarketplace.etsy.com (sem encurtador); parâmetros UTM são permitidos
- Sem URL na legenda do Instagram (não é clicável); usar "link in bio". Facebook pode usar o link clicável
- Sempre tentar ligar o desenho a algo estelar (galáxia, nebulosa, estrelas) no vídeo, legenda ou fato
- Copy sem travessão, sem cara de texto gerado por IA; frases curtas e diretas

## Ferramentas de geração de arte (t-shirt)

- Ideogram é a ferramenta principal: Style → Design, Magic Prompt → OFF, Color → hex navy específico (ex. `#0d1b3e`), Background → White, Aspect Ratio → 3:4 para diagramas multi-view
- Higgsfield / Recraft V4.1 é a opção secundária para line art técnica: modelo utility_vector, mesmas specs de cor e fundo, resolução 2k
- Nunca usar Flux sem pedir autorização ao Fellipe antes
- rembg (modelo u2netp) para remover fundo de recortes de modelo

## Aplicação da estampa na camiseta (regra crítica)

Toda estampa aplicada em camiseta (flat lay, mock, capa) precisa copiar exatamente
a distância e o tamanho da ilustração na foto oficial da Etsy daquele produto, sem
distorção. Sempre medir na foto da Etsy (largura da estampa em relação à largura da
camiseta, distância do topo ou da gola, centralização) e conferir o resultado contra
ela antes de entregar.

## Observações

- Este resumo cobre o essencial para gerar artes consistentes. Para decisões de
  copy mais detalhadas (CTA por rede, hashtags, estrutura de legenda, UTM) ver
  `claude/odoya-social-template.md` e `claude/odoya-calm-autumn-hygge.md` no
  projeto Odoya Store do claude.ai.
- Mantenha este arquivo sincronizado manualmente: se o brand kit mudar no
  claude.ai, atualize aqui também.
