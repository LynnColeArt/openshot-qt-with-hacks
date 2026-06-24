# Research Notes: Creative Workflow Control Surface

This document captures the code-path inventory that informed the plan.

## Existing surfaces worth reusing

- `src/windows/views/timeline.py` already owns the clip context menu and
  several clip-level transformations, including look presets, color actions,
  crop/rotate/layout resets, and the `Adjust_Colors_Triggered` helper.
- `src/windows/views/properties_tableview.py` already has live color-grade
  curve and wheels editors, plus the dock wiring for the wheels panel.
- `src/windows/color_grade_editor.py` already contains the detailed curve and
  wheels UI logic instead of forcing color work through generic properties.
- `src/windows/export.py` already has a split between simple and advanced
  export behavior, with quality and encoder logic that can be made more
  readable.
- `src/windows/views/timeline_backend/qwidget/keyframe_panel.py` and
  `src/windows/views/timeline_backend/qwidget/keyframe.py` already handle the
  timeline keyframe panel, context menus, and keyframe editing mechanics.
- `src/classes/color_presets.py` already contains reusable color grade preset
  payload helpers and scope-specific color preset definitions.

## Notable current behavior

- The timeline already has `No_Transform_Triggered`, which resets rotation,
  crop, and layout together.
- The timeline already has `Reset_Look_Triggered`, which removes clip look
  effects that are managed by the look menu.
- The timeline already has `Color_Triggered`, which applies or resets color
  grade presets on selected clips.
- The properties dock already distinguishes color grade curve and wheels
  properties from ordinary rows, but the panel still needs better grouping and
  scope clarity.
- The exporter already maps quality names to bitrate/encoder settings, but the
  dialog does not yet present quality as a fine-grained slider with a clearer
  at-a-glance interpretation.

## Key takeaway

The mission does not need a new editor engine. It needs clearer boundaries,
better presentation, and a few small helper surfaces to keep project framing,
clip transforms, properties, export, and local pairing from colliding.
