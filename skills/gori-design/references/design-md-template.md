# DESIGN.md template

Pere's default shape for a product's `DESIGN.md` (26 November 2026). Use it when a UI product has no design document, or when the user asks to renovate one. Fill the character, colour values and type from the user's decisions and the repo's accepted context; never invent them. A repo's accepted decisions win where they differ, and a value the user has not chosen stays marked open.

```markdown
# Design

## Character
<two or three sentences the user agreed: who it is for, how it should feel, what it avoids>

## Colours (semantic tokens only)
background / foreground · card / card-foreground · primary / primary-foreground ·
secondary / secondary-foreground · muted / muted-foreground · accent / accent-foreground ·
destructive · border · input · ring
<one line per token: its role, and its light and dark value; the values live in the theme file>

## Spacing (4px base)
xs 4px · sm 8px · md 16px · lg 24px · xl 32px · 2xl 48px · 3xl 64px

## Radius
sm 6px · md 8px · lg 12px · xl 16px · full 9999px

## Type
<typeface, size scale, weights and their roles>

## Strict rules
- Never invent pixel values or hex colours outside the tokens above.
- Cards use padding md (16px) and an internal gap of sm (8px) by default.
- Prefer gap on flex and grid containers.
- Keep radius consistent across related components.
- More space between major sections than inside components.

## Themes and widths
<supported themes; the widths every change is checked at: desktop and 390px>

## Component and layout owners
<where tokens, primitives and page frames live, so changes reuse them>
```

The token names are the shadcn/ui semantic set, so Tailwind classes such as `bg-card` or `text-muted-foreground` map one to one. Keep the theme file as the only place a colour value is written. A lint or test that rejects raw hex and arbitrary pixel values in components enforces the first strict rule better than prose does.
