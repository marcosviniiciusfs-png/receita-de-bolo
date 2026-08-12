# Guia De Uso: Bolo Mais Humano

Esta pasta traz a skill `humanizer`, criada originalmente por `blader/humanizer`, para deixar textos menos com cara de IA e mais naturais.

Use esta skill depois que o site ja tiver estrutura, conteudo e informacoes corretas. Ela nao serve para inventar beneficios, depoimentos, numeros, clientes, datas ou promessas. Ela serve para reescrever o texto mantendo os fatos.

## Quando Usar

Use em:

- textos de hero;
- beneficios;
- depoimentos editados;
- secoes "como funciona";
- FAQ;
- textos de README;
- mensagens de WhatsApp;
- explicacoes para cliente;
- copy do simulador.

## Quando Nao Usar

Nao use para:

- criar dados que nao existem;
- inventar prova social;
- trocar informacao tecnica;
- alterar API, webhook, pixel ou instrucoes de deploy;
- esconder detalhes importantes;
- deixar tudo informal demais quando o cliente precisa de tom profissional.

## Prompt Basico

```text
Use $humanizer para humanizar este texto, mantendo os fatos e sem inventar informacoes:

[cole o texto aqui]
```

## Prompt Para Sites De Cliente

```text
Use $humanizer para reescrever esta copy de site com linguagem mais humana, clara e comercial, sem parecer texto de IA. Preserve nomes, numeros, cidade, beneficios reais, WhatsApp e promessas existentes. Nao invente fatos.

[cole a copy aqui]
```

## Prompt Para Receita De Bolo

```text
Use $humanizer depois de aplicar a receita de bolo. Humanize os textos do site mantendo as informacoes encontradas na pasta do cliente: nome da empresa, localizacao, WhatsApp, beneficios, prova social e perguntas do simulador.
```

## Fluxo Recomendado

1. Use `receita de bolo skill` para encontrar arquivos, notas, WhatsApp, localizacao e provas sociais.
2. Monte o site ou simulador.
3. Valide se todos os fatos estao corretos.
4. Use `bolo mais humano` para melhorar a linguagem.
5. Revise se a skill nao removeu informacoes importantes.
6. Rode localhost e mostre ao cliente/equipe.

## Checklist Antes De Aprovar

- O texto ficou mais natural?
- Continua vendendo bem?
- Nao inventou dados?
- Nao removeu WhatsApp, cidade, valores ou CTA?
- Nao ficou informal demais para o cliente?
- O CTA continua claro?

## Origem E Licenca

Origem: https://github.com/blader/humanizer

Licenca original: MIT. O arquivo `LICENSE` original foi mantido nesta pasta.
