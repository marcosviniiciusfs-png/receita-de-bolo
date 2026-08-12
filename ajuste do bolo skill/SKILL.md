---
name: skill-modernizacao
description: Moderniza simuladores e landing pages de captacao de leads que estao crus, travados, quadrados ou com rolagem ruim, aplicando o padrao AMX: formulario multi-etapas logo abaixo do hero, prova social imediatamente depois do formulario, animacoes fluidas, smooth scroll, inercia discreta fixa em 0.055, preservacao de API/webhook/tracking/campos existentes, localhost para aprovacao e deploy somente quando o usuario pedir.
---

# skill_modernização

## Objetivo

Transformar simuladores antigos no padrao visual e de fluidez aprovado no projeto AMX, sem quebrar o funil comercial existente.

Ao usar esta skill, leia tambem `references/padrao-amx.md` antes de implementar animacoes, ordem das secoes ou scroll.

## Regras Obrigatorias

- Preservar API, webhook, pixel, Conversions API, eventos, payloads, campos, mascaras, validacoes, pagina de obrigado e variaveis de ambiente existentes.
- Nao trocar destino de leads, dominio, projeto de hospedagem ou workflow de deploy sem confirmacao explicita.
- Nao fazer deploy ate o usuario pedir. Primeiro entregar localhost para aprovacao.
- Se testar envio real de lead, usar nome claramente marcado como teste e avisar o usuario.
- Manter a distancia natural do scroll. Nao aumentar o quanto cada giro do mouse empurra a pagina.
- Usar inercia discreta com `WHEEL_LERP = 0.055`. Este e o padrao aprovado.

## Fluxo De Trabalho

1. Mapear o projeto.
   - Identificar framework, roteamento, build, CSS, formulario, servico de leads, tracking, obrigado e deploy.
   - Procurar com `rg` por `simulador`, `Simulator`, `form`, `lead`, `webhook`, `trackLead`, `pixel`, `capi`, `obrigado`, `thank`, `deploy`, `pages`, `vercel`, `netlify`, `wrangler`.

2. Preservar o funil.
   - Antes de editar, entender os campos e o payload enviados.
   - Manter nomes de campos, requisitos, mascaras, envio, tratamento de erro e navegacao de sucesso.
   - Nao reescrever API se o problema for visual.

3. Reordenar a pagina.
   - Header primeiro.
   - Hero ou primeira estrutura visual logo depois.
   - Simulador/formulario imediatamente abaixo do hero.
   - Prova social, depoimentos, clientes ou resultados imediatamente abaixo do formulario.
   - Beneficios, processo, FAQ e footer descem para depois da prova social.

4. Modernizar o formulario.
   - Remover painel lateral pesado, especialmente blocos pretos explicativos do tipo "responda com calma", a menos que o usuario peca para manter.
   - Usar uma caixa centralizada de formulario, com progresso, espacamento bom e altura estavel.
   - Animar a troca de etapas com fade, slide curto e blur leve.
   - Manter botoes claros: voltar, continuar e enviar.
   - Desabilitar continuar/enviar quando a etapa atual estiver invalida.

5. Aplicar fluidez AMX.
   - Em React, se nao existir biblioteca de motion, adicionar `framer-motion` e `lenis`.
   - Criar helper unico para scroll de anchors/CTAs.
   - Criar hook global de scroll momentum.
   - Fixar `WHEEL_LERP = 0.055`.
   - Manter `wheelMultiplier: 1` para nao aumentar a distancia do giro.
   - Respeitar inputs, selects, dialogs, listboxes, areas com scroll interno e `prefers-reduced-motion`.

6. Polir as secoes.
   - Aplicar reveals em hero, formulario, prova social, beneficios e footer.
   - Usar assets reais existentes do cliente.
   - Evitar cards dentro de cards, textos sobrepostos, fontes gigantes em paineis pequenos e paleta de uma cor so.
   - Em interfaces operacionais/comerciais, preferir visual premium, direto e escaneavel.

7. Validar em localhost.
   - Rodar lint/typecheck/build conforme scripts do repo.
   - Subir localhost em porta livre.
   - Testar scroll no mouse: deve ficar fluido, com inercia discreta, sem cauda exagerada.
   - Testar o formulario ate a etapa final.
   - Passar a URL local para o usuario aprovar.

8. Deploy somente se pedido.
   - Confirmar remoto, branch, workflow, dominio e projeto correto do cliente.
   - Nunca publicar em projeto de outro cliente.
   - Buildar antes.
   - Commitar apenas os arquivos da mudanca.
   - Fazer push/deploy no caminho real do repo.
   - Acompanhar o deploy terminar.
   - Fazer smoke test publico.

## Padrao De Entrega

Ao finalizar localhost, responder curto:

```text
Feito. Mantive API/webhook/tracking, coloquei simulador abaixo do hero, prova social logo depois, e scroll com inercia AMX em 0.055.

Localhost:
http://127.0.0.1:PORTA/

Validei: lint/build/local 200.
```

Ao finalizar deploy, informar dominio, commit, checks e qualquer aviso relevante.
