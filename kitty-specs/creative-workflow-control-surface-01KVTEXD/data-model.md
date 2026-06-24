# Creative Workflow State Boundaries

This document freezes the boundary matrix for the mission. Later work packages
should treat it as the contract for what belongs where.

## Core Rule

If a change affects project framing, it belongs to project canvas state.
If a change affects a specific clip, it belongs to clip state.
If a change only describes the current selection, it belongs to UI/session
state.
If a change only affects export output, it belongs to export state.
If a change happens through the agent bridge, it must stay local-first and
explicit about writes.

## State Matrix

| Surface | Owned state | Persistence | Writable by | Notes |
|---------|-------------|-------------|-------------|-------|
| Project canvas | Canvas size, aspect ratio, framing mode, anchor, fit, fill, and project-level layout rules | Project document / timeline-level settings | Canvas/framing UI | This is the new first-class frame surface. It must not become a second copy of clip transforms. |
| Clip state | Trim, timing, placement, crop, transform, look presets, effects, color adjustments, and clip keyframes | Clip data | Clip transforms, properties, keyframe tools, reset actions | `Reset Clip` should clear this category except for the timing/trim/crop/placement parts the user wants to keep. |
| Selection state | Selected clips, selected properties, active scope, and current edit target | Session-only | Timeline and properties UI | Never persist this as project data. It should be cheap to change and safe to discard. |
| Export state | Width, height, codec, quality, target mode, and processor choice | Export dialog / export profile | Export UI | This is a session or profile choice, not a project-canvas choice. |
| MCP state | Local media paths, metadata, representative frames, and confirmed action intent | Bridge session | MCP adapter / pairing bridge | Read access should be the default. Writes must be explicit and confirmed. |

## Scope Labels

The UI and docs should use the same scope language everywhere:

- `clip`
- `selection`
- `project` or `timeline`
- `export`
- `local path`

Those labels should be visible at the point where the user is making the
change.

## Reset Semantics

### Existing partial resets

- `No Transform` currently resets rotation, crop, and layout together.
- `Reset Look` currently clears look-managed effects.
- `Reset Color Grade` currently restores the curve or wheels payload while
  preserving enabled keyframes.

### Planned `Reset Clip`

`Reset Clip` should:

- preserve timeline placement, timing, trim, and crop,
- clear clip-assigned effects and keyframes,
- clear look and color adjustments assigned to the clip,
- clear other clip-local settings that are not part of timing or crop,
- and complete as a single undo-friendly action.

It should not change the project canvas or export settings.

## Reversibility Rules

- Any destructive-looking operation should be one undo step if the UI can
  reasonably support it.
- Read-only surfaces should stay read-only until a write action is explicitly
  confirmed.
- The agent bridge must never infer permission from a dropped file path alone.

## Scope Examples

- Changing aspect ratio for the whole composition belongs to the project
  canvas.
- Nudging one clip into place belongs to clip state.
- Choosing a GPU encoder belongs to export state.
- Inspecting a local video path belongs to MCP state.
- Selecting a set of clips so the properties dock knows what to show belongs to
  selection state.

