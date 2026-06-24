# Creative Workflow Research Notes

These notes record what is already present in the repository so later work
packages can reuse the existing seams instead of guessing at them.

## Inventory Table

| File | Observed behavior | Why it matters |
|------|-------------------|----------------|
| `src/windows/views/timeline.py` | The timeline context menu already has `No Transform`, `Reset Layout`, `Reset Look`, color presets, and `Adjust Colors`. `No Transform` currently clears rotation, crop, and layout together. | This is the closest existing reset surface, but it is not the same thing as the planned `Reset Clip`. |
| `src/windows/views/properties_tableview.py` | The properties table has explicit handling for `colorgrade_curve` and `colorgrade_wheels`, opens dedicated edit surfaces, and has a reset action that preserves enabled keyframes. | The properties dock already knows about color grading, but it is still a flat table with special cases. |
| `src/windows/color_grade_editor.py` | The color-grade wheels editor has Global, Shadows, Midtones, and Highlights rows, a reset button, and an enable toggle in the panel version. | There is already a meaningful grading toolkit to build on. |
| `src/windows/views/timeline_backend/qwidget/keyframe.py` and `keyframe_panel.py` | Keyframes can be selected, dragged, deleted, interpolated, and moved in nested color-grade data structures. | Keyframe access is already strong internally, even if the UI is still too hidden. |
| `src/windows/export.py` | Export already exposes width, height, codec selection, `Low`/`Med`/`High` quality presets, bits-per-pixel mapping for All Formats, and hardware codec detection. | The exporter already has the raw materials for a better UI; the issue is presentation and control clarity. |

## What Already Exists

### Timeline and reset surface

- `No Transform` resets rotation, crop, and layout together.
- `Reset Layout` exists as a separate layout action.
- `Reset Look` removes look-managed effects.
- Color presets and the `Adjust Colors` action are already part of the clip menu.

### Properties and color grading

- The properties dock already has special handling for curve and wheels data.
- `Edit Color Grade` opens the curve editor or the wheels dock depending on the property type.
- `Reset Color Grade` preserves enabled keyframes while resetting the curve or wheels payload.
- The wheels editor already supports scoped rows and an enabled/disabled toggle.

### Keyframes

- The timeline layer can drag and delete keyframes.
- The keyframe panel already tracks selection, snapping, interpolation, and deletion.
- Color-grade keyframes are handled as nested data instead of a single flat list.

### Export

- Width and height are already direct numeric inputs.
- The quality picker is still coarse, using `Low`, `Med`, and `High`.
- `calculate_all_formats_bitrate()` maps those labels to bits-per-pixel values.
- The export code already recognizes several hardware-accelerated codec families.

## Gaps and Implications

- There is no first-class project canvas model yet.
- There is no `Reset Clip` action that clears clip-assigned state while
  preserving timing and crop.
- The properties dock is still mostly a flat table, which makes low-use fields
  too visible.
- The color tools are strong but not organized around a clear scope model.
- Export quality still reads like a preset name instead of a continuous or
  fine-grained tradeoff.
- There is no local MCP pairing bridge in the current tree.

## Planning Takeaways

1. Keep project canvas and clip transforms separate.
2. Reuse the existing color-grade editors instead of replacing them.
3. Treat `No Transform` and `Reset Look` as partial existing helpers, not as a
   substitute for `Reset Clip`.
4. Use the export backend that already exists, but make the user-facing choices
   much clearer.
5. Treat keyframe access as a UX problem, not a lack of underlying machinery.

