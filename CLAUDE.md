# Anton — Estúdio Criativo

Site em duas partes, com dois registros deliberadamente diferentes:

1. **`index.html`** — identidade. Criativa, única, foge do padrão nav→hero→grid.
2. **`sites.html`** — landing de funil para o serviço de criação de sites, voltada
   a tráfego pago. Minimalista, contemporânea, direta.

## Arquivos do projeto

```
index.html   — site institucional / portfólio (one-page, vitrine de vidro)
sites.html   — landing page de funil do serviço "criação de sites" (minimalista)
style.css    — estilos compartilhados, variáveis CSS da identidade
script.js    — nav scroll, menu mobile, reveal animations, form, FAQ
serve.py     — servidor local sem cache (ver "Como rodar localmente")
CLAUDE.md    — este arquivo
```

## Identidade visual

Paleta oficial da marca (brand board fornecido pelo cliente/designer):

| Token CSS    | Hex       | Nome              | Uso                                      |
|--------------|-----------|-------------------|-------------------------------------------|
| `--linho`    | `#F2EDE6` | Linho             | Fundo principal (claro, quente)           |
| `--areia`    | `#D8CCBA` | Areia             | Painéis claros / destaque sobre vinho     |
| `--bege`     | `#A18E7A` | Bege queimado     | Texto secundário / bordas                 |
| `--cafe`     | `#3A2A22` | Café              | Texto principal sobre fundo claro         |
| `--vermelho` | `#7A1F24` | Vermelho profundo | Acento — identidade                       |
| `--vinho`    | `#4B1D24` | Vinho             | O momento exato da oferta/pedido          |
| `--grafite`  | `#2E2E2E` | Grafite           | Rodapé / chrome estrutural                |

**Lógica de cor — importante, mudou:** o vinho não é mais "a página inteira do
funil". Ele marca **o momento exato do pedido comercial**, só isso — em
`index.html` é o CTA que leva pro `sites.html`; em `sites.html` é só o bloco de
CTA final (`#contato`). O resto de `sites.html` é claro/linho. Isso é
proposital: o vinho precisa continuar raro pra significar algo.

**Tipografia:** `Switzer` (Fontshare, `--font-struct`) para estrutura — nav,
botões, rótulos, headings curtos. `Baskervville` (Google Fonts, `--font-voice`)
para voz — frase do hero, citações, assinatura. Baskervville só tem regular +
itálico (sem bold real); hierarquia vem de tamanho/itálico, nunca negrito
sintético.

## O vidro é só do index.html — conceito de vitrine

Depois de idas e vindas, a regra final: **o liquid glass vive só no
`index.html`**, como conceito — a marca vista através de um painel de vidro,
como a vitrine de um ateliê — não como efeito de UI solto. `sites.html` não
tem vidro nenhum (não combina com o registro minimalista/direto de landing).

- `.glass` / `.glass--dark` → cartão funcional quieto (cards de trabalho,
  foto da seção Sobre) — hairline + fundo sólido, sem blur, em qualquer página.
- `.glass-card` / `.glass-card--dark` → vidro de destaque de verdade
  (`backdrop-filter`, `border-radius` grande via `--radius-card`), **só existe
  no `index.html`**: o hero (`.vitrine`) e o CTA (`.cta-band__panel`). Sempre
  sobre `.blob-field` (manchas de cor desfocadas) — sem isso atrás, o blur não
  tem o que desfocar.

Referências que embasam a base quieta por baixo do vidro (`referências.txt`):
Norm Architects, Vincent Van Duysen, Andrew Trotter, FRAMA, MK27, Bernardes,
Pedro Kok, Olívia Dal Piva, Apparatus Studio, Colin King, Faye Toogood,
Atelier Cph, Henry Wilson, Ferm Living, Aesop, Casey Dunn.

## index.html — estrutura (foge do padrão)

- **Nav (`.nav--overlay`)** — sem barra horizontal em nenhum tamanho de tela.
  Só a marca "ANTON" + um gatilho de menu; o menu abre em tela cheia
  (itálico, editorial), igual em mobile e desktop — não é o nav+links padrão.
- **Hero (`.hero--vitrine`)** — split assimétrico, não um bloco centralizado:
  de um lado (`.hero__frame`) só o eyebrow e "role para ver", plano, sobre o
  grão de papel; do outro (`.vitrine`) um painel de vidro alto contendo a
  frase da marca — como olhar pela vitrine de um ateliê.
- **Essência** — as 3 frases não ficam empilhadas alinhadas; cada uma tem um
  recuo maior que a anterior (`.essencia__stack .essencia__line:nth-child()`),
  formando uma escada visual em vez de um bloco de texto uniforme.
- **Trabalho (`.work__rows`)** — casos em linhas editoriais alternadas
  (imagem/texto, texto/imagem), não um grid 2+1. Cada caso tem uma frase de
  contexto — não é só nome + categoria.
- **Sobre** — foto + bio, 2 colunas, inalterado.
- **CTA (`.cta-band`)** — mesma composição assimétrica do hero, mas em vinho:
  o painel de vidro escuro é o único outro lugar com essa linguagem.
- **Contato / Footer** — inalterados, quietos.

## sites.html — estrutura (minimalista, contemporânea, sem vidro)

Trimada de 10 para 7 seções de conteúdo — menos blocos, mais espaço, uma
prova só em vez de grids de cards:

1. **Hero** — claro, sem vidro, sem blob. Título grande, um CTA, uma linha de
   confiança em texto simples (não chips/pílulas).
2. **Prova rápida** (`#prova`) — substitui "para quem é" + "prova em campo":
   um parágrafo + 3 nomes de case como links simples com hairline, não cards.
3. **O que você recebe** — checklist, reduzido de 6 para 4 itens.
4. **Como funciona** — 4 passos, agora sobre fundo claro (antes era vinho).
5. **Depoimento** — 1 citação grande (antes eram 2 em grid).
6. **Investimento** — inalterado.
7. **FAQ** — reduzido de 5 para 4 perguntas.
8. **CTA final** — **o único bloco vinho da página inteira**, sólido, sem
   vidro. É o momento do pedido.
9. **Footer (`.footer--light`)** — claro, para não duplicar o peso escuro
   logo depois do CTA vinho.

## Placeholders para substituir

- [ ] E-mail `ola@seudominio.com.br` e telefone `(00) 00000-0000`
- [ ] Link do WhatsApp em `sites.html` (`https://wa.me/5500000000000`)
- [ ] Cases do portfólio ("Estúdio Cravo", "Consultório Lattes", "Editora Norte") → projetos reais + imagens
- [ ] Foto da seção Sobre (`.about__photo`) → substituir placeholder por `<img>`
- [ ] Bio da seção Sobre → texto real
- [ ] Depoimento de `sites.html` → citação real de cliente
- [ ] Links de redes sociais no footer (`#`) → Instagram / LinkedIn / Behance reais
- [ ] Integrar formulário de contato (`#contactForm`) com backend real (EmailJS / Formspree / servidor)
- [ ] Adicionar favicon (usar o monograma "A" do brand board)
- [ ] SEO: Open Graph, schema markup

## Como rodar localmente

Abrir `index.html` diretamente no navegador — não precisa de servidor.

Para servidor local, use `serve.py` (evita cache do navegador):
```bash
python serve.py 8080
```

## Deploy — servidor "sites-Anton" (Linode)

- **IP público:** `172.233.177.66` (sem domínio ainda — acesso direto pelo IP)
- **Servidor web:** nginx, rodando como `default_server` na porta 80
- **Diretório do site:** `/var/www/anton/` (site próprio da Anton — deixa
  espaço pra outros clientes futuros virarem `/var/www/<cliente>/` + seu
  próprio server block em `/etc/nginx/sites-available/`)
- **Config nginx:** `/etc/nginx/sites-available/anton`

Redeploy depois de editar os arquivos localmente:
```bash
scp index.html sites.html style.css script.js root@172.233.177.66:/var/www/anton/
```
Não precisa reiniciar o nginx pra isso — arquivos estáticos são servidos
direto do disco a cada request.

Pendências de infraestrutura (fora do alcance de SSH, precisam do painel Linode):
- [ ] Apontar um domínio real e configurar `server_name` (hoje é `_`, pega qualquer host)
- [ ] HTTPS (Let's Encrypt/certbot) — sem domínio ainda não dá pra emitir certificado
- [ ] Firewall Cloud (ID 70334877) já libera a porta 80 — confirmar 443 quando o HTTPS entrar
