# Clean component baseline

The default look for new components and for restyling existing ones. It fills gaps only: a repo's accepted brand, tokens, typefaces and written design decisions win on any point they cover. It describes how a component is painted. It does not authorize changing a layout, navigation, a public page's composition or brand identity; those need their own request.

The test is the rendered screen, not the rule list. If a part can be removed and the screen still explains itself, remove it.

## Surfaces and depth

- Use one hairline per edge. A border or a soft ring, never both, and never a border plus a resting shadow.
- Resting components are flat. Keep shadows for things that truly float: menus, popovers, dialogs, toasts.
- Add a card only when it groups data that belongs together. Do not nest panels to create hierarchy; use space first.
- Keep one radius family, with nested corners smaller than their parent.
- No gradients, glows, glass or decorative blur on components. A brand moment that the repo has deliberately accepted is the product's decision, so keep it.

## Colour

Neutral is not automatically right: decide colour on every screen and show the decision in the render.

- Chrome is neutral: navigation, toolbars, tables and ordinary buttons.
- Each screen has at most one action in the brand colour, the thing the user came to do. Other actions are ink, outline or ghost.
- Status carries meaning through a small coloured dot plus plain text, with a filled pill only for an accepted exception. Good, waiting and failed stay distinguishable without relying on hue alone.
- Colour belongs to meaning and to content, such as previews, artwork, avatars and provider logos. Do not use tinted panels as decoration.

## Type

- Use one typeface and a short scale. A page title is about 24px semibold; everything else is usually 13-14px.
- Medium weight is the default emphasis. Keep semibold for titles and key numbers.
- Section labels are plain, muted and sentence case. Avoid uppercase eyebrow labels and bold group labels.
- Numbers in tables and stats use tabular figures.
- Copy is short and plain, with sentence case on titles and buttons.

## Controls

- One height per size across buttons, inputs, selects and tabs, so a row of mixed controls lines up.
- Controls have flat fills with a clear hover and a visible keyboard focus ring. A small press response is enough; respect reduced motion.
- Group related filters behind one control rather than boxing each. Use icons at one size, and only when they help recognition.
- Keep input boundaries visible enough to find. Do not lighten them below what the repo's contrast rules accept.

## Lists, empty and loading

- Prefer a table or a list with hairline row dividers over a grid of cards. A row has one primary text, and everything else is muted.
- An empty state is a small icon, one short line and at most one action. Avoid large illustrations and oversized icons.
- Loading mirrors the final shape with skeletons. A missing value is a quiet placeholder, not "N/A".

## Review

Check the render in light, dark and narrow widths, with long and short content, keyboard focus and reduced motion. Then ask:

1. Is anything drawing an edge that spacing could draw?
2. Which single thing on this screen has colour, and is that the right one?
3. Can each control sit beside its neighbours and line up?
4. Does a shadow appear on something that is not floating?
5. Did this change alter a layout, a page's composition or the brand when it should only have restyled?

Never copy another product's tokens, class strings or components to reach this look. Borrow the relationships, and check the licence before reading a reference's source closely.
