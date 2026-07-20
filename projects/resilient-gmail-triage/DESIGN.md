# Test Mail Console Design

## Intent

Quiet operations console for a person testing an email automation in a bright office. The interface should feel closer to a reliable admin tool than to a campaign sender.

## Register

Product UI, restrained color strategy.

## Color tokens

```css
:root {
  --color-bg: oklch(1 0 0);
  --color-surface: oklch(0.97 0.008 200);
  --color-surface-strong: oklch(0.93 0.012 200);
  --color-ink: oklch(0.22 0.025 220);
  --color-muted: oklch(0.47 0.025 220);
  --color-primary: oklch(0.55 0.11 200);
  --color-primary-hover: oklch(0.48 0.11 200);
  --color-accent: oklch(0.39 0.13 265);
  --color-success: oklch(0.48 0.12 150);
  --color-warning: oklch(0.66 0.14 75);
  --color-error: oklch(0.52 0.18 25);
}
```

Filled primary and error controls use white text. Pale semantic surfaces use dark text.

## Typography

Use the system sans stack. Body text is 16px with 1.5 line height. UI labels are 14px to 15px. Page title is 30px on desktop and 26px on small screens. No display font and no uppercase tracking.

## Layout

A compact top bar shows tool name, transport and fixed recipient. The main content uses two columns on wide screens: scenario selection on the left, preview and send controls on the right. Below 860px it becomes one column. Maximum content width is 1180px.

## Components

- Segmented mode switch: prepared scenarios, custom message, random scenario.
- Scenario rows use checkboxes, category, expected urgency and a short description. Rows are not independent decorative cards.
- Preview uses a plain bordered document surface with subject and body.
- Batch action always shows the exact number of selected messages and asks for an explicit confirmation.
- Status log is an ordered list with timestamp, result and message identifier.
- Empty, loading, validation, success and failure states use text plus an icon or label, never color alone.

## Interaction

State transitions use 160ms ease-out. Buttons expose loading and disabled states. Focus outlines are 3px and clearly offset. Reduced-motion mode disables transitions. Destructive or high-volume actions are confirmed inline, not in a modal.

## Responsive behavior

At small widths, controls become full width, metadata wraps naturally and preview remains readable without horizontal scrolling. Touch targets are at least 44px high.
