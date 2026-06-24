# Data Model: Creative Workflow Control Surface

## Core entities

### Project canvas

- Represents the project-wide frame and aspect-ratio geometry.
- Stores width, height, aspect-ratio behavior, and fit/fill/anchor choices.
- Must remain distinct from any individual clip transform.

### Clip state

- Represents per-clip state such as position, scale, rotation, crop, effects,
  and keyframes.
- `Reset Clip` clears clip-assigned state but keeps timing and crop unless the
  user explicitly chooses a different action.

### Property group

- Represents an inspector section such as Common, Framing, Color, Motion,
  Audio, Effects, or Advanced.
- Groups are a UI organization concept, not a new persistence layer.

### Color scope

- Represents whether a color-grade change applies to a selected clip, a
  selection, or the whole project/timeline.
- The UI needs to state this scope clearly at the point of editing.

### Export profile

- Represents width, height, codec, quality, and processor choice.
- The exporter should show the profile in a way that makes tradeoffs obvious.

### Pairing bridge session

- Represents a local inspection/write session used by MCP.
- Reads local media and project state first, then applies explicit confirmed
  edits only when the user approves them.

## Boundary rules

- Project canvas changes should not be stored as clip animation hacks.
- Clip reset must not alter timeline timing.
- Export controls should map onto the current export backend before any deeper
  render-engine refactor.
- MCP writes should be opt-in and local-first.

## Canonical user questions

- "Is this project frame or clip transform?"
- "Which scope am I editing right now?"
- "What am I losing if I reset this clip?"
- "How big, how compressed, and how encoded will this export be?"
- "Can my agent inspect the same local state I am seeing?"
