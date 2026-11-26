# Interface quality checklist

Read this when shaping or reviewing a change to interactions, forms, motion or content handling. It condenses [Emil Kowalski's design engineering skill](https://github.com/emilkowalski/skills) and [Vercel's web interface guidelines](https://github.com/vercel-labs/web-interface-guidelines) into checks, so those skills need not be loaded whole. A repo's accepted decisions win: for example, keep its sentence-case labels over Vercel's title case.

## Motion

- Decide whether it should animate at all. Anything seen 100+ times a day (shortcuts, command palettes, list navigation) does not; keyboard-triggered actions never animate.
- Every animation has a purpose: spatial continuity, state change, feedback or avoiding a jarring jump. "It looks nice" on a frequent action is not one.
- Easing: entering and exiting use a strong ease-out, moving on screen uses ease-in-out, hover and colour use ease, and constant motion is linear. Never ease-in for UI. Reuse the repo's owned curves before adding one.
- Duration: press 100–160ms, tooltips 125–200ms, dropdowns 150–250ms, modals and drawers 200–500ms. Other UI stays under 300ms.
- Pressable elements respond on `:active` with a subtle scale (0.95–0.98). Nothing enters from `scale(0)`: start near 0.95 with opacity.
- Popovers scale from their trigger (`transform-origin`); modals stay centred. After one tooltip opens, its neighbours open instantly.
- Prefer transitions over keyframes for anything that can be retriggered, so it stays interruptible. Animate only `transform` and `opacity`; never `transition: all`.
- Honour `prefers-reduced-motion`, and stop decorative loops under it.

## Accessibility and focus

- Use semantic elements first: `<button>` for actions and `<a>`/`Link` for navigation, never a clickable `div`. Headings are hierarchical.
- Icon-only buttons get `aria-label`, decorative icons get `aria-hidden`, images get `alt` (empty when decorative), and async messages use `aria-live="polite"`.
- Every interactive element shows a visible `:focus-visible` ring. Never remove an outline without a replacement, and never let a sticky bar cover the focused element.
- Gestures (drag, swipe) always have a tap or keyboard alternative. Never disable zoom.

## Forms

- Every control has a clickable label, a meaningful `name`, the right `type`/`inputmode` and `autocomplete`. Never block paste. Turn spellcheck off for emails and codes.
- The submit button stays enabled until the request starts, then shows progress. Errors sit next to their field, say how to fix it, and the first one gets focus.
- Warn before leaving with unsaved changes. Destructive actions need a confirmation or an undo window.

## Content and layout

- Plan for short, typical and very long content: truncate, clamp or wrap, and give flex children `min-w-0`. Handle empty, loading and error states without broken UI.
- Cap reading measure near 65 characters. Use `text-wrap: balance` on headings and tabular figures for changing or compared numbers.
- Use `…` and curly quotes; loading labels end in `…`. Format dates, numbers and plurals with `Intl`.
- Images have width and height. Lazy-load below the fold and prioritise the hero image.
- Use flex and grid rather than JS measurement. No layout reads during render, and virtualise lists over about 50 rows.
- Full-bleed layouts respect safe-area insets; sheets and drawers use `overscroll-behavior: contain`.
- State worth sharing (tabs, filters, pages) lives in the URL.

## Themes

- Dark themes set `color-scheme: dark`, `theme-color` matches the page background, and native selects get explicit colours.
- Hover, active and focus states each increase contrast over rest, in every supported theme.

## Reviewing with this list

Report each finding as `file:line`, what is wrong and the fix. For polish changes, a small Before / After / Why table makes the reasoning easy to accept or reject. Check the rendered result, not only the code.
