# media-assets

Arquivos públicos de mídia (imagens, PDFs, vídeos) usados para agendar posts nas redes sociais. As ferramentas de agendamento buscam o arquivo por link público, por isso o repositório é aberto. Não coloque aqui nada confidencial.

Os arquivos ficam aqui para sempre: nunca são apagados, nem depois que o post é publicado. Além disso, a cópia definitiva de cada peça fica na pasta local do projeto (veja a seção "Cópia local e guarda dos arquivos").

## Regra de organização (vale para toda marca nova)

Cada marca tem a sua própria pasta. Dentro dela, uma pasta por mês e, dentro do mês, uma pasta por rede social.

```
<marca>/<AAAA-MM>/<rede>/<marca>_<AAAA-MM-DD>_<formato>_<tema>.<extensão>
```

Exemplo:

```
hotmarcas/2026-11/linkedin/hotmarcas_2026-11-05_documento_3-sinais.pdf
hotmarcas/2026-11/linkedin/hotmarcas_2026-11-05_imagem_nome-5-anos.jpg
hotmarcas/2026-11/instagram/hotmarcas_2026-11-05_carrossel1_capa.png
```

### Como preencher cada parte

1. **marca**: nome da marca em minúsculas, sem acento, sem espaço (`hotmarcas`).
2. **AAAA-MM**: mês da publicação (`2026-11`).
3. **rede**: `instagram`, `linkedin`, `facebook`, `tiktok`, `youtube`, `x`, `pinterest`.
4. **data no nome do arquivo**: dia previsto da publicação (`2026-11-05`).
5. **formato**: tipo da peça. Use `reel`, `story`, `carrossel1` (número de carrossel quando houver mais de um no dia), `foto`, `imagem`, `documento`, `video`.
6. **tema**: 2 a 4 palavras que resumem o conteúdo, ligadas por hífen (`3-sinais`, `nome-5-anos`).
7. **extensão**: a do arquivo real (`.jpg`, `.png`, `.pdf`, `.mp4`).

### Regras gerais

1. Só letras minúsculas, números, hífen e sublinhado. Sem acento, sem espaço.
2. Um carrossel tem uma pasta própria dentro da rede, com as lâminas numeradas: `hotmarcas_2026-11-05_carrossel1_01.png`, `..._02.png`.
3. Nova versão de uma peça: acrescente `_v2`, `_v3` ao final do nome. Não apague a anterior.
4. Não renomeie nem mova um arquivo que ainda esteja agendado. O link muda e o post pode falhar.
5. O link público segue este padrão:
   `https://raw.githubusercontent.com/<usuário>/media-assets/main/<caminho do arquivo>`

## Arquivos antigos

Os arquivos soltos na raiz do repositório (`*.mp4`, `post-*.jpg`) são de outro projeto e ficam como estão.


## Cópia local e guarda dos arquivos

Este repositório guarda de forma permanente todas as peças enviadas ao agendador, e o link público de cada uma continua funcionando. A cópia definitiva de cada peça também fica na pasta local do projeto.

### Pasta local

O caminho completo da pasta local não fica registrado aqui, porque este repositório é público. Use sempre o caminho do projeto da marca no computador de quem publica e, ao mostrar o caminho em qualquer lugar, oculte o nome de usuário (`C:\Users\***\...`). Cada marca tem a sua pasta local, que é informada no chat e não neste arquivo.

### Antes de subir

1. Salve a peça na pasta local do projeto (veja "Pasta local" acima). Se a marca ainda não tiver pasta local, pergunte antes de subir.
2. Só depois suba o mesmo arquivo para este repositório.
3. Use o link público para agendar o post no Metricool.

### Depois da publicação

Regra fixa, definida em 24/11/2026: **manter todos os arquivos, sempre.**

1. Não remova arquivo deste repositório depois da publicação. Nenhuma peça é apagada, nem as já publicadas.
2. Nunca renomeie nem mova um arquivo, publicado ou agendado. O link muda e o post pode falhar.
3. Os arquivos soltos na raiz (`*.mp4`, `post-*.jpg`) são de outro projeto e ficam como estão.
4. Mesmo assim, salve a cópia local antes de subir, como indicado em "Antes de subir".

## Skills

A pasta `skills/` guarda as instruções reutilizáveis de produção. Hoje: `skills/linkedin-video-style/SKILL.md` (vídeos de LinkedIn no estilo dashboard). Não coloque aqui caminhos locais nem dados confidenciais.
