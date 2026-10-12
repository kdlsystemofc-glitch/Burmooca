# DIFERENCAS.md — Burmooca × base (Mr. Macário Burger)

Base: `BASE/Mr. Macário Burger/` (`site/`, `src/`, `DESIGN.md`). Dados deste cliente: `CLIENTE.MD` e `imagens/`.

> **Decisão desta etapa (pedido do usuário):** as fotos reais de `imagens/` **não** foram usadas no site.
> Do material do cliente entram só **logo, cores, textos e contexto**. As fotos de comida e da chapa no site
> são as imagens **ilustrativas** da base (geradas por IA, genéricas). Elas não retratam o Burmooca, todos os
> `alt` dizem "Imagem ilustrativa" e o build mantém a trava `imagensAprovadasParaPublicar: false`
> (NÃO PUBLICAR enquanto não forem trocadas por fotos reais ou aprovadas por escrito).

## 1. Conteúdo: tudo vem do CLIENTE.MD deste cliente

| Item | Base (Mr. Macário) | Burmooca | Fonte |
| :--- | :--- | :--- | :--- |
| Nome / h1 | MR. MACÁRIO BURGER | BURMOOCA · HAMBURGUERIA (+ "restaurante e hamburgueria" para leitores de tela) | Google, Instagram |
| Endereço | R. Dom Macário, 1063 – Vila da Saúde | R. Visc. de Laguna, 193 – Mooca, 03112-110 | Google |
| Telefone | (11) 96514-2258 | (11) 94569-0950 (ligação + WhatsApp) | Google + bio ("WhatsApp: (11) 94569-0950") |
| Horário | Qua a dom 18:45–23:30 | **Seg a sáb, 7h–17h** (café e almoço) | Bio + Google ("Fecha 17:00") |
| Preço | R$ 20–40 (selo visível) | R$ 40–60 só no JSON-LD pendente — **não** aparece no texto | Google (26 pessoas) |
| Nota | 5,0 (63) | **4,8 (107)** | Google |
| Serviços | local, retirada, entrega | Refeição no local · Drive-through · Entrega sem contato | Google |
| Destaques | Mr Smash Duplo, Mr Burguinho | Chamantá, Batata Frita (citados em texto, não como legenda de foto) | Google |
| Cardápio | oia.99app.com (só domínio) | burmooca.goomer.app (botão "Ver cardápio completo") | Google |
| Extra | — | "Abrimos à noite para eventos privados, consulte!!" | Bio |
| Avaliações | Francisco/Pedro/Maria | Davi Perez, Nina Maria (literais) + frase do resumo do Google na fita | Google |
| Instagram | @mrmacarioburger | @burmooca (4.251 seguidores → "4,2 MIL") | Web |

Textos **removidos** por serem invenção da base/mockup: "100% CARNE FRESCA", "BOM DEMAIS / ARTESANAL",
"TOTAL: R$ 34,90", "MESA 04 / PONTO DA CHAPA", "CROSTA MAILLARD", "THE GRIDDLE CRAFT", "THE BOARD GAME LOUNGE",
"FOOTER & CONVERSION". No lugar: dados reais (endereço, serviços, horário, nota) ou frases literais das avaliações
("na medida certa", "porção generosa de fritas").

Também removidos do código publicado: os nomes globais `MrMacarioMotion/MrMacarioSections` (viraram
`SiteMotion/SiteSections`), comentários com o nome do cliente anterior e o manifest.

## 2. Imagens

| Slot | Base | Burmooca | Classe |
| :--- | :--- | :--- | :--- |
| Logo (header, selo do hero, rodapé, favicons) | logo Macário ampliado | **logo real** `imgi_2` (150 px, só redimensionado) | real |
| Hero | hambúrguer duplo IA | cheeseburger IA da base (outro arquivo, para não repetir o hero de outro cliente) | ilustrativa — trocar |
| 3 destaques | burger/burguinho/batata IA | os mesmos plates IA, em outra ordem | ilustrativa — trocar |
| Faixa escura | chapa IA | chapa IA (só fundo, `alt=""`) | ilustrativa — trocar |
| Dados 3D, neon de bife, batatas voadoras | plates IA / recorte do mockup | **removidos** → SVG inline: xícara de café, zigue-zague de ketchup, mini-hambúrguer do logo | decorativo (CSS/SVG) |
| Troféu "5.0" | plate IA com "5.0" gravado | **removido** (a nota aqui é 4,8) → selo de nota em CSS com o número real | decorativo |
| Fotos "mesa de jogos" | pessoas inventadas por IA | **removidas** → cartões com avaliações reais | — |
| Diner do rodapé | salão inventado por IA | **removido** → fundo CSS | — |

Regra de ouro preservada: nada que represente o cliente foi gerado. O que é ilustrativo está marcado no HTML,
no `alt`, em `assets.md` e trava o build.

## 3. Variação obrigatória

### Paleta (mesma estrutura de função/contraste, tons novos)

| Função | Base | Burmooca | Por quê (dado real) |
| :--- | :--- | :--- | :--- |
| Fundo claro | creme `#f4ede3` | creme-manteiga `#f7f0de` | pão do logo |
| Faixa escura | `#0b0e13` | preto `#121212` | fundo preto do logo |
| Conversão (rodapé) | vermelho diner `#bd3b2b` | **verde-alface** `#1d5634` | onda verde do logo; o vermelho fica só como ketchup |
| Letreiro gigante | dourado | **preto** com sombra mostarda | letras/fundo do logo |
| CTA | verde WhatsApp | **mostarda** `#f5b31c` (texto preto) | pão do logo |
| Selos | menta / coral / azul | alface / tomate / mostarda | recheio do logo |

Contraste: todos os pares de texto ≥ 4,5:1 (tabela em `PROGRESSO.md`).

### Dispositivo de assinatura

- Base: papel rasgado na faixa escura + rolo de filme no rodapé.
- Burmooca: **o próprio desenho do logo** — bordas da faixa escura em onda de alface (`edge-*.svg`) e
  faixa do rodapé em **zigue-zague de ketchup sobre mostarda**. O logo do Burmooca é exatamente pão + zigue-zague
  vermelho + onda verde; usar isso como assinatura liga o site à marca e o afasta visualmente das outras
  hamburguerias da carteira (La Famiglia e Sogra também ficam na Zona Leste).

### Ajuste de conteúdo pelo contexto

O Burmooca é **restaurante e hamburgueria, de dia** (café e almoço, 7h–17h), diferente da base (noite).
A faixa escura deixou de ser "técnica da chapa" e virou "CAFÉ, ALMOÇO & HAMBÚRGUER" com o horário no selo; a xícara
substitui os dados. A seção de salão/jogos (tema do outro cliente) virou seção de avaliações.

## 4. O que se mantém

- Arquitetura de 5 seções (hero, destaques, faixa escura, prova social, rodapé de conversão), full-bleed.
- Motion: mesmo núcleo e mesmas timelines por seção (só seletores dos slots decorativos e a cor do brilho, que
  agora vem do token `--cta-rgb`). Modos completo/reduzido/pausado, pausa em aba oculta, botão de pausa.
- Tipografia: Bebas Neue / Montserrat / Plus Jakarta Sans / Caveat (auto-hospedadas). Não troquei: o logo já usa
  uma serifada pesada própria e a Bebas mantém o contraste com ela.
- Acessibilidade: um `<h1>`, alvos ≥ 44 px, `aria-hidden` nos decorativos, `prefers-reduced-motion`.
- Performance: CSS crítico medido + verificado em 13 resoluções, `srcset`, motion só após o `load`.
