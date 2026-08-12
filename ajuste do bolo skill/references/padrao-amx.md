# Padrao AMX Para Modernizar Simuladores

## Resultado Esperado

O simulador deve sair do estado cru, travado e quadrado para uma experiencia:

- direta;
- fluida;
- premium;
- com formulario facil de achar;
- com prova social logo depois;
- sem perder API, webhook, tracking e regras comerciais.

## Ordem Das Secoes

Aplicar por padrao:

1. Header
2. Hero / primeira estrutura visual
3. Simulador / formulario
4. Prova social / depoimentos / clientes / resultados
5. Beneficios / processo / FAQ
6. Footer

O formulario deve ficar logo abaixo do hero. A prova social deve ficar logo abaixo do formulario.

## Caixa Do Formulario

Usar uma caixa centralizada, sem painel lateral pesado.

Recomendacoes:

- largura maxima entre `720px` e `820px`;
- progress bar ou indicador de etapa;
- altura minima estavel para nao pular layout;
- borda/sombra premium conforme identidade do cliente;
- botoes claros: voltar, continuar, enviar;
- botao de continuar/enviar bloqueado ate a etapa ser valida.

Remover blocos laterais pretos ou textos longos ao lado do questionario, salvo pedido contrario do usuario.

## Animacoes React

Se o projeto for React e nao tiver biblioteca de animacao, adicionar:

```bash
npm install framer-motion lenis
```

Variantes recomendadas:

```ts
export const revealViewport = {
  once: true,
  amount: 0.22,
  margin: "0px 0px -80px 0px",
};

export const revealContainer = {
  hidden: {},
  visible: {
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.08,
    },
  },
};

export const fadeUp = {
  hidden: {
    opacity: 0,
    y: 34,
    filter: "blur(10px)",
  },
  visible: {
    opacity: 1,
    y: 0,
    filter: "blur(0px)",
    transition: {
      duration: 0.9,
      ease: [0.16, 1, 0.3, 1],
    },
  },
};

export const scaleReveal = {
  hidden: {
    opacity: 0,
    scale: 0.96,
    y: 26,
    filter: "blur(10px)",
  },
  visible: {
    opacity: 1,
    scale: 1,
    y: 0,
    filter: "blur(0px)",
    transition: {
      duration: 0.85,
      ease: [0.16, 1, 0.3, 1],
    },
  },
};
```

Transicao de etapa do formulario:

```tsx
<AnimatePresence mode="wait">
  <motion.div
    key={currentStep}
    initial={{ opacity: 0, y: 18, filter: "blur(8px)" }}
    animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
    exit={{ opacity: 0, y: -12, filter: "blur(8px)" }}
    transition={{ duration: 0.38, ease: [0.16, 1, 0.3, 1] }}
    className="min-h-[260px]"
  >
    {renderStep()}
  </motion.div>
</AnimatePresence>
```

## Smooth Scroll E Inercia Aprovada

Este e o padrao aprovado pelo cliente:

```ts
const ENABLE_WHEEL_MOMENTUM = true;
const WHEEL_LERP = 0.055;
const SETTLE_DISTANCE = 0.45;
```

Importante:

- `WHEEL_LERP = 0.055` deixa a inercia discreta e fluida.
- Nao usar `0.0275` neste padrao, porque a cauda fica forte demais.
- Nao zerar a inercia, porque o site volta a parecer travado.
- Nao aumentar `wheelMultiplier`; manter `wheelMultiplier: 1`.
- A distancia de cada giro do mouse deve continuar normal.

Config Lenis:

```ts
const lenis = new Lenis({
  autoRaf: true,
  lerp: 0.075,
  anchors: true,
  smoothWheel: false,
  wheelMultiplier: 1,
  syncTouch: false,
});
```

O momentum customizado deve:

- escutar `wheel` com `{ capture: true, passive: false }`;
- normalizar `deltaMode`;
- chamar `preventDefault()` apenas no scroll principal da pagina;
- preservar comportamento nativo em `input`, `textarea`, `select`, `[role='listbox']`, dialogs, poppers e areas com scroll interno;
- respeitar elementos com `data-scroll-momentum="off"`;
- atualizar `targetScroll += deltaY`, sem multiplicar o delta;
- animar com `window.scrollTo(0, currentScroll + distance * WHEEL_LERP)`.

CSS global:

```css
html {
  scroll-behavior: smooth;
}

html[data-smooth-scroll="lenis"] {
  scroll-behavior: auto;
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
}
```

## Helper De Anchor

Usar uma unica funcao para header e CTA do hero:

```ts
export const smoothScrollToSection = (id: string) => {
  const element = document.getElementById(id);
  if (!element) return;

  const lenis = (window as { __siteLenis?: { scrollTo: (target: Element) => void } }).__siteLenis;
  if (lenis) {
    lenis.scrollTo(element);
    return;
  }

  element.scrollIntoView({ behavior: "smooth", block: "start" });
};
```

O nome global pode ser adaptado por cliente, por exemplo `__amxLenis`, `__siteLenis` ou outro nome neutro.

## Checklist De Qualidade

Antes de entregar localhost:

- formulario logo abaixo do hero;
- prova social logo abaixo do formulario;
- API/webhook/tracking preservados;
- inercia em `0.055`;
- distancia do scroll normal;
- anchors suaves;
- sem painel lateral pesado;
- mobile sem texto sobreposto;
- `lint` e `build` executados quando existirem;
- localhost respondendo `200`.

Antes de deploy:

- conferir dominio/projeto certo;
- nao publicar em outro cliente;
- commitar somente arquivos da mudanca;
- acompanhar workflow/deploy ate terminar;
- testar dominio publico e API quando aplicavel.
