# Creative Workflow Control Surface Plan

This plan turns the mission spec into a concrete implementation shape. It is
written to keep the current OpenShot behavior honest while making room for the
new control surfaces the user asked for.

## Purpose

The app already solves a real problem for Linux creators, but the current UI
still forces several different kinds of work through the same clip-transform
and keyframe surfaces.

This mission is about separating those concerns:

- framing versus clip transforms,
- properties versus raw schema dumps,
- reset flows versus destructive edits,
- export preferences versus render backend details,
- and local pairing versus remote or implicit control.

## Current Inventory Snapshot

The codebase is not starting from zero. The plan should build on the current
partial surfaces rather than replacing them:

- `src/windows/views/timeline.py` already exposes `No Transform`,
  `Reset Layout`, `Reset Look`, color presets, and `Adjust Colors`.
- `src/windows/views/properties_tableview.py` already special-cases
  `colorgrade_curve` and `colorgrade_wheels`, including dedicated edit and
  reset actions.
- `src/windows/color_grade_editor.py` already has a detailed wheels editor with
  Global, Shadows, Midtones, and Highlights controls plus reset and enable
  toggles.
- `src/windows/views/timeline_backend/qwidget/keyframe.py` and
  `keyframe_panel.py` already support drag, delete, interpolation, selection,
  and nested color-grade keyframe movement.
- `src/windows/export.py` already exposes width, height, codec, quality
  presets, bitrate mapping, and hardware codec detection.

Those surfaces are useful, but they are still too fragmented for the workflow
described in the spec.

## State Boundaries

The most important planning decision is to freeze the state model before any UI
rewrite begins.

- Project canvas state owns the project frame, canvas size, aspect ratio, and
  frame-level fit/fill/anchor behavior.
- Clip state owns clip-local transforms, effects, keyframes, look tools, and
  color adjustments.
- Selection state is ephemeral and should not be treated as project data.
- Export state owns the output dimensions, codec, quality, and processor mode.
- MCP state owns local inspection context and must remain read-first,
  confirmation-based, and explicit about writes.

That boundary line must stay visible in every later work package.

## Execution Phases

### Phase 1: Discovery and contracts

Goal:
Capture the current implementation reality and write down the boundary matrix.

Deliverables:

- `research.md` with the inventory evidence,
- `data-model.md` with the state boundaries,
- `quickstart.md` with the validation checklist,
- and `spec-kitty-bugs.md` with the Spec Kitty issues worth sending to Robert.

Exit criteria:

- Every later work package can cite a stable definition of project canvas,
  clip state, export state, selection state, and MCP state.

### Phase 2: Framing and canvas

Goal:
Make project framing first-class without turning it into a second clip
transform system.

Deliverables:

- aspect-ratio controls that operate on the project canvas,
- a visible distinction between canvas geometry and clip geometry,
- and support for static alignment changes without forcing keyframes.

Exit criteria:

- A user can correct mismatched source framing once instead of building a
  keyframe hack for every clip.

### Phase 3: Properties and reset flow

Goal:
Replace the flat properties experience with a categorized inspector and add a
safe `Reset Clip` action.

Deliverables:

- grouped properties by intent,
- clear scope labels for clip, selection, or project,
- dedicated access to the color tools,
- and `Reset Clip` that preserves timing and crop while clearing other
  clip-assigned state.

Exit criteria:

- A user can find the right setting faster and recover from a bad clip edit
  without losing timeline placement.

### Phase 4: Color grading and keyframes

Goal:
Make color work feel like a focused toolkit instead of a buried special case.

Deliverables:

- a manageable color grading surface with clear scope,
- better access to the keyframe inspector,
- and a layout that makes layering and fine-tuning easier to reason about.

Exit criteria:

- Color edits are understandable at a glance and do not require timeline
  surgery for static corrections.

### Phase 5: Exporter redesign

Goal:
Expose the decisions the user actually cares about when exporting.

Deliverables:

- width and height as first-class controls,
- codec selection that is visible and concrete,
- a finer-grained quality control than low/medium/high labels,
- and explicit CPU, GPU, or Auto processing choice.

Exit criteria:

- The dialog clearly answers how large, what codec, how much quality, and
  where the work will run.

### Phase 6: MCP pairing bridge

Goal:
Add a local pairing surface that can inspect real project state and apply
confirmed changes safely.

Deliverables:

- local read-only inspection for image and video paths,
- project and export state visibility,
- and a limited set of explicit write actions.

Exit criteria:

- The bridge is local-first, inspectable, and impossible to confuse with a
  hidden remote control.

### Phase 7: QA and docs

Goal:
Keep the new control surface understandable and maintainable.

Deliverables:

- regression coverage for the new boundaries,
- updated user-facing docs,
- and a migration note for users who already rely on the current clip-centric
  workflows.

Exit criteria:

- The new terminology in the docs matches the UI and the underlying state
  model.

## Risks

- Boundary drift: later work could accidentally reclassify clip state as
  project state.
- False reset semantics: `Reset Clip` could accidentally behave like the
  existing `No Transform` or `Reset Look` actions.
- Export confusion: a nicer UI could still hide the actual encode tradeoff.
- MCP safety: the pairing bridge could become too powerful if writes are not
  explicitly confirmed.

## Validation Approach

- Ground all planning language in the code inventory.
- Reuse existing partial support where it already exists.
- Keep the docs and the future UI vocabulary aligned.
- Treat the data-model boundary matrix as the contract for later work.

## Handoff Notes

- `research.md` should answer "what exists today?"
- `data-model.md` should answer "what belongs where?"
- `quickstart.md` should answer "how do we sanity-check the plan?"
- `spec-kitty-bugs.md` should answer "what should Robert know?"

