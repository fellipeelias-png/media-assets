---
name: linkedin-video-style
description: Cria vídeos de LinkedIn da série Claude for Growth no estilo dashboard rodando (marca Fellipe), nos formatos 4:5 e 1:1, com legenda em primeira pessoa e primeiro comentário fixo.
---

# Vídeo de LinkedIn: dashboard rodando

Use quando o pedido for um vídeo para a série de posts do Fellipe Araujo sobre Claude para times B2B. Não serve para vídeo promocional nem para narrativa com metáfora (cozinha, frutas, etc.).

## Princípios

1. O vídeo é um dashboard de trabalho rodando. Mostra o processo acontecendo, com informação clara, e termina em uma frase de conclusão.
2. Direto ao ponto. Sem história, sem metáfora, sem tom de anúncio.
3. Nenhuma métrica inventada. Se o número não foi medido, não aparece. Estatística de terceiros só com fonte verificada.
4. Toda afirmação em primeira pessoa precisa ser experiência real dele.
5. Texto na tela maior que o padrão de vídeo de rede social, porque ele pediu informação clara (isso passa do limite de 8 palavras do prompt-mestre, e foi aprovado).

## Especificação técnica

1. Duração 30 s, 30 fps, 900 quadros. Formatos 1080x1350 (4:5) e 1080x1080 (1:1).
2. Estrutura no tempo: gancho 0 a 2,8 s; dashboard 2,9 a 20,4 s; conclusão 20,1 a 26 s; cartão final 26,1 a 30 s.
3. Moldura: barra superior "CLAUDE FOR GROWTH", selo RUNNING que vira COMPLETE, cronômetro e barra de progresso.
4. Corpo: três cartões empilhados (entrada, processamento, saída), cada um mudando de estado ao longo do tempo.
5. Margens de segurança de 72 px em todos os lados. Nada de texto cortado.
6. Conclusão em três linhas curtas. Cartão final: "Save this →", "try it today", "Fellipe Araujo", "fellipearaujo.com".

## Marca

1. Fundo #07090d, painel #0C0E12, linhas #1A1D23 e #2A2E37.
2. Texto #F3F5F8, texto secundário #9AA1AC.
3. Destaque turquesa #2DD4BF, violeta #8a7cf5, gradiente turquesa para violeta. Vermelho #F87171 só para alertas.
4. Inter 800 nos títulos, JetBrains Mono nos rótulos e valores.
5. Não usar branco e azul.

## Produção

1. Uma página HTML/SVG animada por `window.renderAt(t)`, com um arquivo de configuração por post (painéis, células, estados e frases).
2. Quadros capturados com Playwright e codificados com ffmpeg (libx264, crf 17, preset veryfast, yuv420p).
3. Antes de entregar, extrair quadros de cada MP4 final (gancho, meio, conclusão, cartão final) e conferir texto cortado, margens e legibilidade nos dois formatos.

## Legenda e agendamento

1. Primeira pessoa, falando do que ele faz para empresas. Sem emojis e sem travessões.
2. Um convite para falar com ele, uma pergunta de fechamento e três hashtags.
3. Primeiro comentário fixo em toda a série: "How I work with teams on this: fellipearaujo.com".
4. Agendar no Metricool (marca Fellipe Personal, fuso Europe/Paris) só com um sim explícito dele.
5. Arquivos: salvar primeiro na pasta local do projeto; subir ao repositório público só como ponte para o agendador; remover depois da publicação (regras no README).
