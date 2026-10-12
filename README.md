# Burmooca — landing page

Adaptação da base `BASE/Mr. Macário Burger/` (mesma arquitetura, motion, acessibilidade e pipeline de build).
O que mudou e por quê: **`DIFERENCAS.md`**. Estado e testes: `PROGRESSO.md`.

> ⚠️ **Não publicar ainda:** fotos de comida/chapa são ilustrativas (IA). Ver `PENDENCIAS-CLIENTE.md`, item 1.

- Ver: abrir `site/index.html` ou `python -m http.server 8000 -d site`.
- Editar só `src/` (`index.html`, `css/tokens.css` = paleta, `css/theme.css` = assinatura do cliente,
  `css/style.css` = estrutura compartilhada) e rodar `npm run build`.
- `node_modules` é uma junção para o da base (`mklink /J`).
- Testes: os mesmos da base (`scripts/test_*.py`, `scripts/auditoria_final.py`, `scripts/lighthouse_runs.py`).
