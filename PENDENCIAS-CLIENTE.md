# PENDENCIAS-CLIENTE.md — Burmooca

Nenhuma bloqueia o código; todas bloqueiam a publicação.

1. **Fotos (bloqueante).** O site usa fotos ilustrativas geradas por IA (herdadas da base). Escolher fotos reais
   para: hero, 3 destaques do cardápio e fundo da faixa escura. Sugestões em `assets.md`. Depois: trocar os
   arquivos/`srcset`, rodar `scripts/gen_image_steps.py`, `npm run build`, `scripts/gen_og_image.py` e mudar
   `imagensAprovadasParaPublicar` para `true` em `cliente.config.json`.
2. Horário: confirmar seg a sáb 7h–17h (e se há horário estendido: o Google cita "Outros horários").
3. WhatsApp (11) 94569-0950 recebe pedidos? Ou o botão principal deve ir para o Goomer?
4. Link do cardápio: confirmar https://burmooca.goomer.app.
5. O que é o "Chamantá" (destaque do Google) e preços dos destaques, se quiserem exibir.
6. Arquivo original do logo (só temos 150x150 do Instagram).

Efeito de cada dado: `cliente.config.json` (horário, preço e cardápio só vão ao JSON-LD com `"confirmado": true`;
os textos visíveis correspondentes estão comentados em `src/index.html`). Domínio: campo `dominio`.
