# Receita de Bolo

Repositorio publico com skills reutilizaveis para reconstruir e modernizar sites/simuladores de clientes.

## Guia Do Simulador Do Zero

Leia este guia para entender o fluxo completo de um simulador: site, formulario, webhook, Meta Pixel, Meta CAPI, pagina de conversao, Worker/API, Cloudflare, subdominio, testes e deploy.

[GUIA_SIMULADOR_DO_ZERO.md](GUIA_SIMULADOR_DO_ZERO.md)

## Pastas

### receita de bolo skill

Skill geral para criar ou reconstruir um site do zero a partir dos arquivos dentro da pasta do cliente.

Use quando a equipe precisar que a IA procure:

- pasta de clientes contemplados;
- notas e arquivos de texto;
- numero da empresa;
- WhatsApp e link de WhatsApp;
- localizacao;
- beneficios;
- provas sociais;
- perguntas padrao de formulario;
- imagens, logos e assets.

Prompt recomendado:

```text
Use $receita-de-bolo-site para analisar esta pasta de cliente e reconstruir o site do zero seguindo a receita.
```

### ajuste do bolo skill

Skill para modernizar simuladores no padrao AMX aprovado, com inercia discreta em `WHEEL_LERP = 0.055`.

Use quando o simulador ja existe, mas esta cru, travado, quadrado ou mal organizado.

Prompt recomendado:

```text
Use $skill-modernizacao para modernizar este simulador no padrao AMX com inercia 0.055.
```

### bolo prêmium

Skill premium para deixar o site com a versao mais intensa e cinematica do padrao AMX, incluindo a inercia mais forte da primeira versao aprovada.

Use quando quiser o site mais fluido, animado e com mais presenca visual.

Prompt recomendado:

```text
Use $modernize-simulator-site para transformar este simulador antigo no modelo premium AMX.
```

## Como Usar

Copie a pasta da skill desejada para a pasta de skills do ambiente da equipe, ou aponte a IA diretamente para o `SKILL.md` da pasta escolhida.

Cada pasta contem um `SKILL.md` proprio e, quando necessario, arquivos em `references/` e `scripts/`.

## Regras Importantes

- Primeiro localhost, depois deploy somente quando o cliente aprovar.
- Sempre preservar API, webhook, pixel, formularios e destino dos leads.
- Sempre confirmar o projeto/dominio certo antes de deploy.
- Nunca publicar em projeto de outro cliente.
