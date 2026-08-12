---
name: modernize-simulator-site
description: Modernize existing lead-generation simulator and landing page repositories that feel crude, rigid, slow, or visually outdated. Use when Codex is asked to transform an old client simulator into the polished AMX-style flow: smooth/inertial scrolling, animated sections, a centered multi-step form directly below the hero, social proof immediately after the form, preserved lead/API behavior, responsive layout, localhost preview, testing, and optional deployment only after approval.
---

# Modernize Simulator Site

## Overview

Transform an existing simulator site into the polished AMX-style experience while preserving the client's business logic, tracking, API destinations, form fields, copy, branding, and deploy target.

Read `references/amx-style-model.md` when implementing the visual/scroll pattern or when the existing repository resembles the AMX simulator family.

## Operating Rules

- Preserve existing lead submission behavior, API URLs, webhook destinations, conversion tracking, thank-you flow, environment variables, and validation rules unless the user explicitly asks to change them.
- Never publish to another client's project. Before deploy, inspect remotes, workflows, hosting config, Pages/Vercel/Netlify/Cloudflare settings, domains, and project names.
- Do not deploy after modernization unless the user explicitly asks for deploy. Default to localhost preview.
- Treat every test lead as production-visible unless proven otherwise. Use clearly marked test names and report that test data was sent.
- Keep changes scoped to layout, motion, scroll, section ordering, and small support utilities unless functional defects block the request.

## Workflow

1. Inspect the repository.
   - Identify framework, routing, build tool, styling system, form component, API service, tracking service, thank-you route, and deploy workflow.
   - Search with `rg` for terms like `simulador`, `Simulator`, `form`, `lead`, `webhook`, `trackLead`, `pixel`, `capi`, `thank`, `obrigado`, `deploy`, `pages`, `vercel`, and `wrangler`.

2. Preserve the working funnel.
   - Map current form fields and submission payload before editing.
   - Keep all required fields and masks unless the user asks otherwise.
   - Keep the success navigation and error handling working.
   - If there is a server-side conversion API, test it separately only when safe and requested.

3. Rebuild the page order.
   - Put the hero/top visual first.
   - Put the simulator/form section immediately after the hero.
   - Put social proof/testimonials/client proof immediately after the simulator.
   - Move benefits, process, FAQ, footer, and other supporting sections below social proof.
   - Update header navigation so the simulator CTA is prominent and anchor scrolling uses the smooth-scroll helper.

4. Modernize the simulator UI.
   - Remove heavy side panels, black explainer blocks, and instructional clutter beside the form unless the brand specifically requires them.
   - Use one centered form box with clear progress, strong spacing, stable dimensions, and a sharp but premium visual frame.
   - Animate step transitions with fade/slide/blur, but keep inputs stable and readable.
   - Ensure buttons are disabled until the current step is valid.

5. Add AMX-style motion and scroll.
   - Prefer the repository's existing animation library. In React projects without one, add `framer-motion` and `lenis`.
   - Add global CSS smooth scrolling and a JS scroll momentum layer.
   - Keep wheel distance normal; add inertia after the wheel stops. Do not multiply every wheel tick.
   - Respect `prefers-reduced-motion`, form controls, selects, dialogs, nested scroll areas, and any element marked to opt out.

6. Polish sections.
   - Add staggered reveal animations to hero, form, social proof, benefits, and footer.
   - Use visual assets already in the repo. Do not make a generic marketing page.
   - Avoid nested cards, oversized dashboard/card clutter, single-hue palettes, overlapping text, and viewport-scaled font sizes.
   - Keep cards at 8px radius or less unless the existing design system requires otherwise.

7. Validate locally.
   - Run dependency install only if needed.
   - Run lint/typecheck/build using the repo's scripts.
   - Start localhost on an available port and give the user the URL.
   - Smoke test the form path. If Playwright is available, use it to test the real route, field progression, submit button, network response, and thank-you page.

8. Deploy only on request.
   - Reconfirm the correct client domain/project from local config and remote hosting metadata.
   - Build first.
   - Commit intentionally.
   - Push or deploy using the repository's actual production path.
   - Watch the deploy finish and run public smoke tests.

## React/Vite Implementation Notes

- Add shared motion variants in a small utility like `src/lib/motion.ts`.
- Add a smooth scroll helper like `src/lib/smoothScroll.ts` so header links and hero CTAs use the same behavior.
- Add a hook like `src/hooks/use-scroll-momentum.ts` and call it once near the root app component.
- Prefer IDs like `id="simulador"` only when they match the existing app language; otherwise adapt to the current repo.
- Keep environment variables in existing names. Do not invent new API variables if one already exists.

## Completion Checklist

- Simulator appears immediately after the hero.
- Social proof/testimonials appear immediately after the simulator.
- Form has no bulky side explainer panel unless intentionally retained.
- Scroll feels smooth with visible inertia tail and normal wheel distance.
- Header/CTA anchors scroll smoothly.
- Existing lead submission still sends the same required information to the right destination.
- Lint/build pass or failures are clearly reported.
- Localhost URL is provided.
- Deploy is not performed unless explicitly requested.
