---
name: receita-de-bolo-site
description: Receita de bolo para criar ou reconstruir sites completos a partir de uma pasta de cliente. Use quando Codex precisar abrir uma pasta no VS Code ou em outro ambiente, identificar automaticamente arquivos de notas, fotos, logos, clientes contemplados, numeros de empresa, WhatsApp, links, localizacao, beneficios, provas sociais, perguntas de formulario e conteudo comercial, para refazer o site do zero com base nos materiais encontrados, mantendo localhost para aprovacao e deploy somente quando solicitado.
---

# Receita De Bolo Site

## Objetivo

Usar os arquivos de uma pasta de cliente como fonte de verdade para reconstruir um site completo do zero: conteudo, imagens, WhatsApp, formulario, prova social, beneficios, localizacao e chamadas comerciais.

Antes de implementar, leia `references/roteiro-de-reconstrucao.md`. Quando precisar inventariar rapidamente uma pasta, use `scripts/inventario_site.py`.

## Regra Principal

Nao inventar dados comerciais quando houver arquivo na pasta que possa conter essa informacao. Primeiro procurar, depois inferir, e so depois perguntar ao usuario quando for essencial.

## Fluxo Obrigatorio

1. Inventariar a pasta.
   - Listar arquivos e subpastas com `rg --files` ou ferramenta equivalente.
   - Procurar pastas como `clientes contemplados`, `contemplados`, `clientes`, `depoimentos`, `prints`, `resultados`, `logos`, `imagens`, `assets`, `fotos`, `notas`, `anotacoes`, `textos`, `conteudo`.
   - Rodar `python <skill>/scripts/inventario_site.py .` se Python estiver disponivel.

2. Extrair informacoes do cliente.
   - Nome da empresa/marca.
   - Segmento/oferta principal.
   - Telefone comercial.
   - WhatsApp escrito em texto ou em link.
   - Link de WhatsApp existente.
   - Localizacao/cidade/endereco/area atendida.
   - Instagram, site antigo, email e outras redes.
   - Provas sociais: clientes contemplados, fotos, depoimentos, resultados, prints, numeros e cases.
   - Beneficios, diferenciais, garantias, processo e objeções.

3. Gerar WhatsApp corretamente.
   - Se houver link pronto, preservar.
   - Se houver apenas numero, gerar link `https://wa.me/55DDDNUMERO` para Brasil quando o contexto for brasileiro.
   - Remover espacos, parenteses, hifens e caracteres nao numericos.
   - Se o numero ja tiver codigo do pais, nao duplicar `55`.
   - Opcionalmente adicionar mensagem pre-preenchida quando fizer sentido.

4. Definir estrutura do site.
   - Header com logo/nome e CTA de WhatsApp.
   - Hero com promessa clara, CTA e imagem real quando houver.
   - Simulador/formulario ou bloco principal logo acima da dobra seguinte quando o negocio exigir captacao.
   - Prova social cedo: clientes contemplados, depoimentos, resultados e fotos.
   - Beneficios e diferenciais.
   - Como funciona/processo.
   - Localizacao/area de atendimento.
   - FAQ ou objeções.
   - Footer com contato, WhatsApp, endereco e redes.

5. Criar ou refazer o projeto.
   - Se ja existir app, respeitar stack, scripts e padroes locais.
   - Se for do zero, escolher stack simples e adequada ao ambiente existente.
   - Usar assets reais da pasta antes de buscar ou gerar imagens.
   - Evitar landing page vazia: a primeira tela ja deve ser o site utilizavel.
   - Criar formulario funcional quando o repo ja tiver backend/API ou quando o usuario pedir; caso contrario, usar CTA para WhatsApp.

6. Fazer perguntas padrao quando faltarem dados criticos.
   - Qual e o objetivo principal do site?
   - Qual acao o visitante deve tomar: WhatsApp, formulario, ligacao ou compra?
   - Qual publico-alvo?
   - Qual cidade/regiao atendida?
   - Qual oferta principal?
   - Existe alguma promessa, garantia ou diferencial que precisa aparecer?
   - O site deve preservar alguma API, pixel, webhook, dominio ou deploy existente?

7. Validar.
   - Rodar lint/typecheck/build quando houver scripts.
   - Subir localhost e passar a URL.
   - Conferir se imagens carregam.
   - Conferir se WhatsApp abre com o numero correto.
   - Conferir se formulario envia para o destino certo quando houver.
   - Conferir mobile e desktop.

8. Deploy somente se o usuario pedir.
   - Confirmar dominio, repositorio, branch, projeto de hospedagem e cliente correto.
   - Nunca publicar em projeto de outro cliente.
   - Fazer build antes.
   - Acompanhar deploy terminar.
   - Fazer smoke test publico.

## Prioridade De Fontes

1. Arquivos de notas e texto dentro da pasta.
2. Nomes de arquivos e pastas.
3. Imagens, prints e logos.
4. Codigo existente.
5. Configuracoes `.env.example`, workflows e hosting.
6. Perguntas ao usuario.

## Padrao De Resposta Ao Usuario

Depois do localhost:

```text
Feito. Recriei o site usando os arquivos da pasta: logo/imagens/notas/clientes contemplados/WhatsApp/localizacao.

Localhost:
http://127.0.0.1:PORTA/

Validei: build/lint/local 200.
```

Se faltarem dados:

```text
Achei quase tudo, mas faltou confirmar: numero de WhatsApp e cidade atendida. O resto ja deixei estruturado com base nos arquivos encontrados.
```
