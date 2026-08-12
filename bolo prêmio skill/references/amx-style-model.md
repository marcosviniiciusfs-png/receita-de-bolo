# AMX-Style Simulator Modernization Model

## Target Feel

The finished site should feel fluid, premium, and direct: the visitor sees the brand/offer, reaches the simulator quickly, fills a focused multi-step form, then immediately sees proof that real clients trust the company.

Avoid the old "crude simulator" feel: rigid sections, square static form buried far down the page, too many clicks before value, heavy explainer panels, abrupt native scrolling, and no section motion.

## Section Order

Use this order unless the client brief says otherwise:

1. Header
2. Hero or first visual structure
3. Simulator/form section
4. Social proof/testimonials/client logos/results
5. Benefits/process/why choose us
6. Footer

The simulator should be directly under the first visual/hero structure. Social proof should be directly under the simulator.

## Simulator Box

Use a single centered form box:

- Max width around `720px` to `820px`.
- Clear progress indicator and current step label.
- Stable min height so step changes do not jump the layout.
- Sharp/premium border and shadow if the brand fits it.
- No large black side panel or "answer calmly" block next to the form unless requested.
- Buttons: back on the left, continue/submit on the right.
- Disable continue/submit until the current step is valid.

Preserve all current field names and submission payloads. Only change presentation unless the user asks for new funnel logic.

## Motion Pattern

For React projects, prefer `framer-motion` when no motion system exists.

Useful variants:

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
  hidden: { opacity: 0, y: 34, filter: "blur(10px)" },
  visible: {
    opacity: 1,
    y: 0,
    filter: "blur(0px)",
    transition: { duration: 0.9, ease: [0.16, 1, 0.3, 1] },
  },
};

export const scaleReveal = {
  hidden: { opacity: 0, scale: 0.96, y: 26, filter: "blur(10px)" },
  visible: {
    opacity: 1,
    scale: 1,
    y: 0,
    filter: "blur(0px)",
    transition: { duration: 0.85, ease: [0.16, 1, 0.3, 1] },
  },
};
```

Use `AnimatePresence` for simulator step transitions:

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

## Scroll Momentum Pattern

The AMX scroll feel uses normal wheel distance plus an inertia tail. Do not make each wheel tick jump farther.

Core constants:

```ts
const WHEEL_LERP = 0.0275;
const SETTLE_DISTANCE = 0.45;
```

Use Lenis for anchor/programmatic smooth scroll, but disable Lenis wheel smoothing when custom wheel momentum is implemented:

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

Custom wheel behavior should:

- Listen to `wheel` with `{ capture: true, passive: false }`.
- Normalize `deltaMode` for line/page deltas.
- `preventDefault()` only for page-level wheel scrolling.
- Update `targetScroll += deltaY`, clamped to document bounds.
- Animate `window.scrollTo(0, current + (target - current) * WHEEL_LERP)`.
- Preserve native behavior for inputs, textareas, selects, Radix/listbox poppers, dialogs, nested scroll areas, ctrl/meta/alt wheel, and opt-out elements.
- Set `document.documentElement.dataset.smoothScroll = "lenis"` while active.
- Respect `prefers-reduced-motion: reduce`.

CSS:

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

## Smooth Anchor Helper

Use one helper for header links and hero CTAs:

```ts
export const smoothScrollToSection = (id: string) => {
  const element = document.getElementById(id);
  if (!element) return;

  const lenis = (window as { __amxLenis?: { scrollTo: (target: Element) => void } }).__amxLenis;
  if (lenis) {
    lenis.scrollTo(element);
    return;
  }

  element.scrollIntoView({ behavior: "smooth", block: "start" });
};
```

Adapt the global property name to the client or project if `__amxLenis` is too brand-specific.

## Validation

Minimum:

- `npm run lint` or repo equivalent.
- `npm run build` or repo equivalent.
- Localhost preview.
- Manual scroll test: wheel movement should continue briefly after release.
- Manual form test through final step.

Preferred:

- Playwright test that opens localhost or production, reaches the simulator, fills all fields, submits test data, waits for the conversion/API response, and confirms the thank-you page.

Report any production-visible test leads clearly.
