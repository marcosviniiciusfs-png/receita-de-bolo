# Guia Receita De Bolo: Simulador Do Zero

Este guia explica o fluxo completo para criar, configurar, testar e publicar um simulador de captacao de leads do zero.

A ideia e simples: qualquer pessoa da equipe deve conseguir abrir a pasta de um cliente, entender os arquivos, montar o site, configurar WhatsApp, webhook, Meta Pixel, Meta CAPI, pagina de conversao e Cloudflare sem adivinhar o que fazer.

## Visao Geral Do Fluxo

O simulador tem 5 pecas principais:

1. Site/front-end: onde o usuario ve a landing page e preenche o simulador.
2. Formulario: coleta nome, WhatsApp, cidade e respostas comerciais.
3. Webhook de lead: envia os dados para CRM, Make, Zapier, planilha ou sistema do cliente.
4. Meta Pixel e Meta CAPI: registram PageView e Lead para campanhas da Meta.
5. Deploy: publica o site e a API em dominios/subdominios corretos.

Fluxo ideal:

```text
Usuario entra no site
  -> Meta Pixel registra PageView
  -> Usuario preenche simulador
  -> Front envia Lead para API/Worker
  -> Worker envia lead para webhook do cliente
  -> Worker envia evento Lead para Meta CAPI
  -> Site manda usuario para /obrigado
  -> Meta consegue medir conversao real
```

## 1. Antes De Criar O Site

Abra a pasta do cliente e procure:

- logo;
- imagens;
- pasta de clientes contemplados;
- depoimentos;
- prints;
- arquivo de notas;
- numero da empresa;
- WhatsApp;
- link de WhatsApp;
- localizacao;
- cidade/regiao atendida;
- beneficios;
- diferenciais;
- perguntas do simulador;
- dominio;
- webhook;
- pixel ou token da Meta.

Use:

```bash
rg --files
rg -n -i "whatsapp|telefone|contato|endereco|localizacao|cidade|instagram|cliente|contemplado|depoimento|resultado|beneficio|diferencial|simulador|webhook|pixel|capi|api" .
```

Se estiver usando a skill `receita de bolo skill`, rode:

```bash
python "receita de bolo skill/scripts/inventario_site.py" .
```

O objetivo e nao inventar informacao que ja existe na pasta.

## 2. Estrutura Do Site

Ordem recomendada:

1. Header com logo e botao de WhatsApp.
2. Hero com promessa principal.
3. Simulador/formulario logo abaixo do hero.
4. Prova social: clientes contemplados, depoimentos, prints e resultados.
5. Beneficios e diferenciais.
6. Como funciona.
7. Localizacao ou area atendida.
8. FAQ.
9. Footer com contato.

Para simuladores, o formulario deve aparecer cedo. Se o formulario ficar la embaixo, o usuario clica demais e converte menos.

## 3. Perguntas Padrao Do Simulador

Use as perguntas existentes quando o cliente ja tiver um funil.

Se for do zero, comece com:

```text
1. O que voce quer conquistar?
2. Em quanto tempo pretende comprar/contratar?
3. Qual valor deseja simular?
4. Possui entrada/investimento inicial?
5. Qual parcela ou valor mensal ideal?
6. Qual sua cidade?
7. Nome completo.
8. WhatsApp.
```

Adapte por segmento:

- Imovel: casa, apartamento, terreno, cidade, valor de credito, entrada.
- Veiculo: carro, moto, caminhao, valor, entrada, parcela.
- Servico local: necessidade, urgencia, bairro/cidade, contato.
- Consultoria: objetivo, prazo, nivel atual, contato.

## 4. WhatsApp

Se houver link pronto, preserve.

Se houver so o numero, gere o link.

Exemplo:

```text
(92) 99999-0000
```

vira:

```text
https://wa.me/5592999990000
```

Regra:

1. Remova tudo que nao for numero.
2. Se tiver 10 ou 11 digitos no Brasil, adicione `55`.
3. Se ja comecar com `55`, nao duplique.
4. Use `https://wa.me/NUMERO`.

Com mensagem:

```text
https://wa.me/5592999990000?text=Ola%2C%20vim%20pelo%20site%20e%20quero%20fazer%20uma%20simulacao.
```

## 5. Webhook De Lead

O webhook e o endereco que recebe o lead.

Pode ser:

- Make;
- Zapier;
- CRM;
- Google Sheets;
- backend do cliente;
- outro sistema comercial.

O front-end nao deve chamar o webhook diretamente quando houver dados sensiveis ou quando precisar tambem enviar Meta CAPI. O ideal e:

```text
Front-end -> Worker/API -> Webhook do cliente
```

Payload minimo:

```json
{
  "nome": "Maria Cliente",
  "telefone": "5592999990000",
  "whatsapp": "(92) 99999-0000",
  "cidade": "Manaus",
  "origem": "simulador_cliente",
  "tipo_bem": "Carro",
  "valor_pretendido": "R$ 150.000,00",
  "valor_pretendido_numero": 150000,
  "valor_entrada": "R$ 15.000,00",
  "valor_entrada_numero": 15000,
  "parcela_ideal": "R$ 1.800,00",
  "parcela_ideal_numero": 1800,
  "source_url": "https://cliente.seudominio.com.br/",
  "event_id": "lead_abc123",
  "received_at": "2026-08-12T12:00:00.000Z"
}
```

Sempre enviar:

- nome;
- WhatsApp;
- cidade;
- respostas do simulador;
- origem;
- data/hora;
- URL de origem;
- `event_id`.

## 6. Meta Pixel

O Meta Pixel fica no site/front-end.

Ele serve para registrar eventos no navegador:

- PageView: quando a pessoa abre a pagina.
- Lead: quando o formulario e enviado com sucesso.

Instalar no front-end:

- em `index.html`, quando for site simples;
- em componente global, layout ou provider, quando for React/Next/Vite;
- sempre uma unica vez.

Exemplo conceitual:

```html
<!-- Meta Pixel base code aqui -->
```

Depois, no envio com sucesso:

```ts
window.fbq?.("track", "Lead", {}, { eventID: eventId });
```

Importante: o evento Lead nao deve disparar so porque a pessoa clicou no botao. Ele deve disparar quando o envio deu certo.

## 7. Meta CAPI

Meta CAPI significa Conversions API.

Ela e o envio server-side do evento para a Meta. Em vez de depender so do navegador, o servidor/Worker tambem envia o evento.

Por que usar:

- melhora confiabilidade;
- reduz perda por bloqueadores;
- melhora medicao;
- ajuda otimizacao das campanhas;
- registra leads mesmo quando o navegador falha.

Fluxo:

```text
Front-end envia evento para Worker
Worker envia Lead para webhook
Worker envia Lead para Meta CAPI
Worker responde sucesso para front
Front manda usuario para /obrigado
```

Dados importantes para CAPI:

- `event_name`: normalmente `PageView` ou `Lead`;
- `event_time`;
- `event_id`;
- `event_source_url`;
- `action_source`: `website`;
- `user_data`: telefone, nome, sobrenome, cidade, IP, user agent, fbp/fbc quando houver;
- `custom_data`: tipo de lead, valor, categoria, oferta.

Para telefone, nome, cidade e email, o Worker deve normalizar e aplicar hash SHA-256 antes de mandar para Meta quando necessario.

## 8. Deduplicacao Pixel + CAPI

Se o mesmo Lead for enviado pelo Pixel e pela CAPI, os dois precisam usar o mesmo `event_id`.

Exemplo:

```text
event_id = lead_123
Pixel Lead usa lead_123
CAPI Lead usa lead_123
```

Isso ajuda a Meta entender que e o mesmo lead, nao dois leads diferentes.

## 9. Pagina De Conversao / Obrigado

A pagina de conversao normalmente e:

```text
/obrigado
/sucesso
/thank-you
```

Por que ela existe:

- confirma que o lead foi enviado;
- evita que o usuario envie de novo sem querer;
- facilita medir conversao por URL;
- permite criar conversao personalizada na Meta;
- deixa a experiencia mais profissional.

Regra:

```text
Formulario enviado com sucesso -> salvar flag local opcional -> navegar para /obrigado
```

Nao deixe `/obrigado` ser acessada como conversao falsa se isso atrapalhar medicao. Em apps React, pode usar `sessionStorage` para permitir a pagina apenas depois do envio real.

Exemplo:

```ts
sessionStorage.setItem("lead_submission_success", "true");
navigate("/obrigado", { replace: true });
```

Na pagina:

```ts
const canShow = sessionStorage.getItem("lead_submission_success") === "true";
```

## 10. Onde Criar Conversao Na Meta

No Events Manager/Meta:

1. Criar ou escolher o Pixel/Dataset do cliente.
2. Instalar Pixel no site.
3. Configurar CAPI no Worker.
4. Testar eventos PageView e Lead.
5. Criar conversao personalizada se necessario.

Formas comuns de conversao:

- evento `Lead`;
- URL contem `/obrigado`;
- evento `Lead` + dominio correto.

Preferencia:

```text
Usar evento Lead real apos envio do formulario.
```

URL `/obrigado` pode ser usada como apoio, principalmente para validar e criar regra simples.

## 11. Cloudflare: O Que Fica Onde

Existem duas partes:

1. Front-end/site: Pages, GitHub Pages, Vercel, Netlify ou outro.
2. API/CAPI: Cloudflare Worker.

Modelo recomendado por cliente:

```text
Site:
https://cliente.simulead.com.br

API/CAPI:
https://api-cliente.simulead.com.br/events
```

Ou, se ainda nao tiver dominio:

```text
https://cliente-conversions-api.sua-conta.workers.dev/events
```

Para producao, prefira dominio/subdominio do cliente ou da operacao.

## 12. Subdominio No Cloudflare Por Simulador

Para cada simulador, crie nomes claros:

```text
cliente.simulead.com.br
api-cliente.simulead.com.br
```

Exemplo:

```text
amx.simulead.com.br
api-amx.simulead.com.br
```

Por que separar:

- cada cliente tem webhook diferente;
- cada cliente pode ter Pixel diferente;
- evita misturar leads;
- fica mais facil debugar;
- CORS fica mais seguro;
- deploy fica organizado.

## 13. Worker Da API/CAPI

Arquivos recomendados:

```text
cloudflare/
  cliente-conversions-api/
    src/
      index.ts
    wrangler.jsonc
```

`wrangler.jsonc` exemplo:

```jsonc
{
  "name": "cliente-conversions-api",
  "main": "src/index.ts",
  "compatibility_date": "2026-08-12",
  "workers_dev": true,
  "observability": {
    "enabled": true
  },
  "vars": {
    "META_PIXEL_ID": "PIXEL_ID_AQUI",
    "META_GRAPH_API_VERSION": "v25.0",
    "ALLOWED_ORIGINS": "https://cliente.simulead.com.br,http://localhost:5173,http://127.0.0.1:5173"
  }
}
```

Secrets:

```bash
wrangler secret put META_CAPI_ACCESS_TOKEN --config cloudflare/cliente-conversions-api/wrangler.jsonc
wrangler secret put LEAD_DESTINATION_WEBHOOK_URL --config cloudflare/cliente-conversions-api/wrangler.jsonc
```

Nunca colocar token da Meta ou URL sensivel de webhook direto no front-end.

## 14. Endpoints Da API

Minimo:

```text
GET /health
POST /events
OPTIONS /events
```

`GET /health`:

```json
{
  "ok": true,
  "service": "cliente-conversions-api"
}
```

`POST /events` recebe:

```json
{
  "event_name": "Lead",
  "event_id": "lead_abc123",
  "event_source_url": "https://cliente.simulead.com.br/",
  "lead_data": {},
  "user_data": {},
  "custom_data": {}
}
```

O Worker deve:

1. Validar origem CORS.
2. Validar payload.
3. Se for Lead, enviar para webhook.
4. Enviar evento para Meta CAPI.
5. Responder com status claro.

Resposta ideal:

```json
{
  "success": true,
  "lead_webhook": {
    "success": true,
    "status": 200
  },
  "meta": {
    "success": true,
    "status": 200
  }
}
```

## 15. CORS

O Worker deve aceitar apenas origens esperadas:

```text
https://cliente.simulead.com.br
http://localhost:5173
http://127.0.0.1:5173
```

Nao usar `*` em producao quando ha formulario de lead.

Se o front-end mudar de dominio, atualizar `ALLOWED_ORIGINS`.

## 16. Custom Domain Ou Route No Worker

Se o Worker for a origem da API, use custom domain:

```jsonc
{
  "routes": [
    {
      "pattern": "api-cliente.simulead.com.br",
      "custom_domain": true
    }
  ]
}
```

Depois:

```bash
npx wrangler deploy --config cloudflare/cliente-conversions-api/wrangler.jsonc
```

Se o Worker estiver na frente de um servidor existente, use route com DNS proxied.

Regra simples:

```text
Worker e a propria API? custom_domain.
Worker fica na frente de uma origem ja existente? route.
```

## 17. Variavel Do Front-End

No front-end, criar:

```text
VITE_META_CAPI_URL=https://api-cliente.simulead.com.br/events
```

Ou no `.env.example`:

```text
VITE_META_CAPI_URL=
```

No codigo:

```ts
const META_CAPI_URL = import.meta.env.VITE_META_CAPI_URL;
```

Se `VITE_META_CAPI_URL` nao existir, o PageView pode falhar silenciosamente, mas o Lead deve avisar erro se o envio for obrigatorio.

## 18. Front-End: Envio Do Lead

O front deve:

1. Validar campos.
2. Criar `event_id`.
3. Disparar Pixel Lead com esse `event_id`.
4. Enviar payload para Worker.
5. Esperar sucesso do Worker.
6. Ir para `/obrigado`.

Pseudo fluxo:

```ts
const eventId = createEventId("Lead");

window.fbq?.("track", "Lead", {}, { eventID: eventId });

const response = await fetch(import.meta.env.VITE_META_CAPI_URL, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    event_name: "Lead",
    event_id: eventId,
    event_source_url: window.location.href,
    lead_data: formData,
    user_data: {
      ph: formData.whatsapp,
      fn: firstName,
      ln: lastName,
      ct: formData.city
    },
    custom_data: {
      content_name: "Simulador",
      lead_type: "simulador_cliente"
    }
  })
});

if (!response.ok) {
  throw new Error("Falha ao registrar lead.");
}

navigate("/obrigado", { replace: true });
```

## 19. Testes Obrigatorios

Antes de deploy:

```bash
npm run lint
npm run build
```

Testar API:

```bash
curl https://api-cliente.simulead.com.br/health
```

Testar CORS:

```bash
curl -i -X OPTIONS https://api-cliente.simulead.com.br/events \
  -H "Origin: https://cliente.simulead.com.br" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type"
```

Testar Lead com dados marcados:

```text
Nome: Teste Deploy Cliente
WhatsApp: numero de teste
Cidade: cidade de teste
Origem: simulador_teste
```

Se usar Playwright, testar:

- abre site;
- chega no simulador;
- preenche etapas;
- envia;
- recebe 200 da API;
- vai para `/obrigado`.

## 20. Deploy Do Site

Antes de publicar:

1. Confirmar cliente.
2. Confirmar dominio.
3. Confirmar branch.
4. Confirmar projeto de deploy.
5. Confirmar variaveis de ambiente.
6. Confirmar Worker/API.

Nunca publicar AMX em projeto Nortecon, nem cliente A em projeto B.

Checklist:

```text
Repo correto:
Branch correta:
Dominio correto:
Projeto Cloudflare/Pages/Vercel correto:
VITE_META_CAPI_URL correto:
Webhook correto:
Pixel correto:
```

## 21. Deploy Do Worker

Fluxo:

```bash
npx wrangler deploy --config cloudflare/cliente-conversions-api/wrangler.jsonc --dry-run
npx wrangler deploy --config cloudflare/cliente-conversions-api/wrangler.jsonc
```

Depois testar:

```bash
curl https://api-cliente.simulead.com.br/health
```

E fazer um lead teste completo.

## 22. Receita Rapida Para Cada Novo Cliente

1. Criar pasta/repo do cliente.
2. Colocar logo, imagens, clientes contemplados e notas.
3. Rodar inventario.
4. Criar site com hero, simulador, prova social, beneficios e footer.
5. Criar Worker de CAPI/webhook.
6. Configurar secrets.
7. Configurar `VITE_META_CAPI_URL`.
8. Instalar Pixel.
9. Criar `/obrigado`.
10. Testar local.
11. Testar API.
12. Fazer deploy.
13. Testar dominio publico.
14. Conferir eventos na Meta.
15. Entregar link ao cliente.

## 23. Problemas Comuns

### Lead nao chega no webhook

Verificar:

- secret `LEAD_DESTINATION_WEBHOOK_URL`;
- status retornado pelo Worker;
- payload enviado;
- logs do webhook;
- CORS;
- se o front esta usando a URL certa.

### Meta CAPI falha

Verificar:

- `META_CAPI_ACCESS_TOKEN`;
- `META_PIXEL_ID`;
- versao da Graph API;
- user_data;
- resposta da Meta;
- se evento esta com `event_name` valido.

### Conversao duplicada

Verificar:

- Pixel e CAPI usam o mesmo `event_id`;
- Lead nao dispara duas vezes;
- botao fica desabilitado enquanto envia;
- pagina `/obrigado` nao dispara Lead so por acesso direto, a menos que seja intencional.

### CORS bloqueia

Verificar:

- dominio do site esta em `ALLOWED_ORIGINS`;
- localhost usado esta na lista;
- request usa `Content-Type: application/json`;
- Worker responde `OPTIONS`.

### Deploy foi para projeto errado

Parar e corrigir antes de mandar para cliente.

Verificar:

- `git remote -v`;
- workflow;
- projeto Pages/Vercel/Netlify;
- dominio publicado;
- DNS.

## 24. Fontes Oficiais

- Cloudflare Workers routes e dominios: https://developers.cloudflare.com/workers/configuration/routing/
- Cloudflare Workers custom domains: https://developers.cloudflare.com/workers/configuration/routing/custom-domains/
- Cloudflare Pages custom domains: https://developers.cloudflare.com/pages/configuration/custom-domains/
- Meta Pixel: https://developers.facebook.com/docs/meta-pixel/
- Meta Conversions API: https://developers.facebook.com/docs/marketing-api/conversions-api/
- Meta deduplicacao Pixel + CAPI: https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/

## 25. Regra Final

O simulador so esta pronto quando:

- o site abre;
- o formulario funciona;
- o lead chega no destino certo;
- a Meta recebe evento;
- a pagina de obrigado aparece;
- o dominio e do cliente certo;
- o deploy foi testado;
- alguem consegue explicar o fluxo sem depender de quem programou.
