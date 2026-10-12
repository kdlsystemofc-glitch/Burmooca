# assets.md — Origem de cada imagem (Burmooca)

> **Por decisão desta etapa, nenhuma foto real do cliente é exibida.** Do acervo do cliente (`imagens/`) só o
> logo entra no site. As fotos de comida e da chapa são as imagens ilustrativas da base, **geradas por IA, que não
> retratam o cliente**. O build avisa NÃO PUBLICAR enquanto `imagensAprovadasParaPublicar` for `false`.

| Arquivo em `site/assets/` | Origem | Classificação |
| :--- | :--- | :--- |
| `logo-150.webp`, `favicon.ico`, `apple-touch-icon.png`, `icons/*` | `imagens/imgi_2_*` (logo real, 150x150) → `reserva/logo-original.jpg`, via `scripts/gen_icons.py` | **real**. Ícones de 180–512 px são ampliação simples (Lanczos) de 150 px: pedir o original. Nenhuma IA. |
| menu-burguinho-* (cheeseburger da base) | plate da base (Gemini) | **ilustrativa, gerada por IA — NÃO é foto do cliente. Trocar antes de publicar.** |
| `hero-burger-*`, `menu-burguinho-*`, `menu-fries-*` | plates da base (Gemini) | **ilustrativas, geradas por IA — trocar.** |
| `griddle-craft-*` | plate da base (Gemini), usado só como fundo (`alt=""`) | **ilustrativa, gerada por IA — trocar ou aprovar como fundo.** |
| edge-top.svg / edge-bottom.svg — onda creme + faixa verde-alface (scripts/gen_edges.py burmooca) | SVG gerado por código | decorativo (permitido) |
| `paper-noise.*` | ruído sintético da base | decorativo (permitido) |
| SVG inline no HTML: xícara de café, zigue-zague de ketchup, mini-hambúrguer do logo; selo de nota; fundos do rodapé | código (CSS/SVG) | decorativo (permitido) |

Removidos em relação à base (não fazem sentido ou eram de outro cliente): dados 3D, neon de bife, batatas voadoras
(recorte do mockup), troféu com "5.0" gravado, fotos de "mesa de jogos" com pessoas inventadas, diner do rodapé,
`og-image.jpg` (regerar com `scripts/gen_og_image.py` depois da troca das fotos).

**Fotos reais disponíveis para a troca** (em `imagens/`, não usadas): imgi_10 / imgi_21 / imgi_24 (lanches), imgi_26 (hot dog com fritas), imgi_19 (milkshake), imgi_11 (coxinhas), imgi_14 / imgi_18 / imgi_22 (pratos do almoço), imgi_15 (equipe — exige autorização de imagem).
Ao trocar: recortar/limpar/ampliar só a partir do arquivo real e marcar aqui como
"recriada por IA — confirmar com o cliente antes de publicar".
