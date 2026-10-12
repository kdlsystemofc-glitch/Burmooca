# PROGRESSO.md — Burmooca

## 12/10/2026 — Adaptação da base (Mr. Macário Burger)

Feito:
- `DIFERENCAS.md` (conteúdo, imagens, paleta, assinatura, o que se mantém).
- Projeto copiado da base (`src/`, `scripts/`, `site/` sem nenhuma imagem do cliente anterior); `node_modules` = junção.
- Conteúdo 100% do `CLIENTE.MD`; **sem fotos reais** (pedido do usuário): só o logo real; comida/chapa ilustrativas (IA, da base), trava de publicação ativa.
- Paleta nova em `src/css/tokens.css`, assinatura em `src/css/theme.css`; `style.css` sem nenhuma cor fixa (só tokens).
- Componentes novos em CSS/SVG: selo de nota real, cartões de avaliação, ícones do tema, fundos do rodapé, logo no header/rodapé.
- Correções sobre a base: build agora considera seções que cruzam a dobra (CSS crítico + fontes); selo circular escondido em ≤ 640 px (encostava no h1, também na base); link inline do rodapé com alvo de 44 px.
- Revisão visual: página inteira 1440 e 390 (`screenshots/final/`), até 2 rodadas de correção por cliente.

Testes (mesma bateria da base):
- `npm run build`: CSS crítico idêntico ao completo em 13 resoluções.
- `test_responsive` (12 telas): rolagem lateral, console, alvos de toque, zoom 200% — OK.
- `test_phase_a`, `test_phase_c`, `test_*_motion` (5 seções): OK, sem erros de console.
- `auditoria_final` (Chromium + WebKit × 15 telas × 5 modos): 135/135 (rodada 2; a rodada 1 teve 63 falhas, todas pelo link @burmooca com 15 px de altura — corrigido).
- Contraste WCAG: todos os pares de texto ≥ 4,5:1; gráficos ≥ 3:1.
- Lighthouse mobile, modo produção, mediana de 3: Performance **94**, Acessibilidade 100, Boas práticas 100, SEO 100, LCP 3,16 s, CLS 0 (base: 92).

Falta (ver `PENDENCIAS-CLIENTE.md`): fotos reais (bloqueante), confirmações de horário/links/WhatsApp, domínio, `og-image.jpg` (regerar após as fotos), commit (pasta não é repositório git).
