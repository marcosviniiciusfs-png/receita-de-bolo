# Roteiro De Reconstrucao De Site A Partir De Pasta De Cliente

## 1. Inventario Inicial

Comece entendendo a pasta antes de mexer no codigo.

Comandos uteis:

```bash
rg --files
rg -n -i "whatsapp|telefone|contato|endereco|endereço|localizacao|localização|cidade|instagram|email|cliente|contemplado|depoimento|resultado|beneficio|benefício|diferencial|garantia|simulador|formulario|formulário|pixel|webhook|api" .
```

Pastas prioritarias:

- `clientes contemplados`
- `contemplados`
- `clientes`
- `depoimentos`
- `prova social`
- `prints`
- `resultados`
- `antes e depois`
- `logos`
- `logo`
- `imagens`
- `fotos`
- `assets`
- `notas`
- `anotacoes`
- `anotações`
- `textos`
- `conteudo`
- `conteúdo`

Extensoes importantes:

- Texto: `.txt`, `.md`, `.docx`, `.rtf`, `.csv`, `.json`
- Imagens: `.png`, `.jpg`, `.jpeg`, `.webp`, `.avif`, `.svg`
- Videos: `.mp4`, `.mov`, `.webm`
- Config: `.env`, `.env.example`, `.yml`, `.yaml`, `.json`, `.toml`

## 2. Dados Que Devem Ser Extraidos

Monte mentalmente ou em notas esta ficha:

```text
Marca:
Segmento:
Oferta principal:
Publico-alvo:
WhatsApp:
Link WhatsApp:
Telefone:
Email:
Instagram:
Endereco/localizacao:
Area atendida:
Clientes contemplados/provas:
Beneficios:
Diferenciais:
Perguntas do formulario:
Destino do formulario/API:
Pixel/tracking:
Dominio/deploy:
```

## 3. WhatsApp

Procurar padroes:

```text
wa.me
api.whatsapp.com
whatsapp
wpp
zap
telefone
contato
(00) 00000-0000
00 00000-0000
+55
```

Gerar link:

1. Remover tudo que nao for numero.
2. Se o numero brasileiro tiver 10 ou 11 digitos, prefixar `55`.
3. Se ja comecar com `55` e tiver 12 ou 13 digitos, manter.
4. Usar `https://wa.me/NUMERO`.

Exemplo:

```text
(92) 99999-0000 -> https://wa.me/5592999990000
```

Mensagem opcional:

```text
https://wa.me/5592999990000?text=Ol%C3%A1%2C%20vim%20pelo%20site%20e%20quero%20mais%20informa%C3%A7%C3%B5es.
```

## 4. Clientes Contemplados E Prova Social

Se houver pasta de clientes contemplados, usar como uma das secoes mais importantes do site.

Tipos de material:

- fotos de clientes;
- prints de conversa;
- imagens de entrega;
- nomes de clientes;
- resultados numericos;
- depoimentos em texto;
- logos de empresas atendidas;
- comprovantes ou cards antigos.

Transformar em:

- grid de depoimentos;
- carrossel de fotos;
- faixa de logos;
- numeros de prova social;
- cards de casos;
- secao "Clientes contemplados".

Nunca inventar nomes reais de clientes. Se houver imagens sem texto, usar legendas genericas seguras, como "Cliente contemplado" ou "Resultado entregue".

## 5. Perguntas Padrao Para Simuladores

Quando o site tiver simulador ou formulario de captacao, preservar perguntas existentes. Se estiver criando do zero e o usuario nao forneceu perguntas, usar perguntas adaptaveis:

- O que voce quer conquistar?
- Em quanto tempo pretende comprar/contratar?
- Qual valor deseja simular?
- Possui entrada ou investimento inicial?
- Qual parcela ou faixa mensal ideal?
- Qual sua cidade?
- Nome completo.
- WhatsApp.

Adaptar ao segmento:

- Imovel: tipo de imovel, valor de credito, entrada, cidade.
- Veiculo: carro/moto/caminhao, valor, entrada, parcela.
- Servico local: necessidade, urgencia, bairro/cidade, contato.
- Educacao/consultoria: objetivo, prazo, nivel atual, contato.

## 6. Estrutura Recomendada Do Site

Ordem padrao:

1. Header com logo/nome e CTA.
2. Hero com promessa clara e CTA.
3. Bloco principal de conversao: formulario, simulador ou WhatsApp.
4. Prova social.
5. Beneficios.
6. Como funciona.
7. Galeria/imagens reais.
8. Localizacao/area atendida.
9. FAQ.
10. Footer.

Se o site for altamente visual, usar imagens reais cedo. Se for operacional ou B2B, manter layout mais direto e escaneavel.

## 7. Copy Base

Hero:

```text
Headline: [Marca] ajuda voce a [resultado principal] com [diferencial].
Subheadline: Atendimento em [cidade/regiao], com analise personalizada e contato rapido pelo WhatsApp.
CTA: Falar no WhatsApp / Fazer simulacao / Quero atendimento
```

Beneficios:

```text
Atendimento personalizado
Analise rapida
Processo transparente
Opcoes alinhadas ao seu objetivo
Suporte do inicio ao fim
```

Prova social:

```text
Clientes contemplados
Resultados reais
Historias de quem ja foi atendido
Empresas/clientes que confiam
```

## 8. Regras De Design

- Criar o site real, nao uma landing generica explicando recursos.
- Usar imagens e assets da pasta.
- Evitar texto sobreposto no mobile.
- Evitar card dentro de card.
- Evitar paleta dominada por uma unica cor sem contraste.
- Usar componentes estaveis: grids responsivos, alturas minimas, aspect-ratio em imagens.
- CTAs devem apontar para WhatsApp ou formulario correto.
- Header deve facilitar voltar ao CTA principal.

## 9. Preservacao Tecnica

Antes de alterar:

- identificar se existe `.env` ou `.env.example`;
- verificar serviços de lead;
- verificar pixel/CAPI/analytics;
- verificar rotas de obrigado;
- verificar deploy/workflows;
- verificar dominio do cliente.

Nao alterar:

- URLs de API;
- webhooks;
- tokens/secrets;
- dominios de producao;
- nome de projeto de deploy;
- tracking/pixel.

## 10. Validacao

Minimo:

- build/lint quando existir;
- localhost respondendo;
- WhatsApp correto;
- imagens carregando;
- mobile sem quebra visual.

Ideal:

- teste E2E com Playwright quando formulario/API forem importantes;
- envio de lead teste apenas com autorizacao ou quando o usuario pedir teste real;
- smoke test publico depois de deploy.
