# Specification: Creative Workflow Control Surface

**Mission ID:** 01KVTEXDY2799KPQPY8MD3NTET  
**Slug:** `creative-workflow-control-surface-01KVTEXD`  
**Mission type:** software-dev  
**Target branch:** `develop`  
**Status:** Draft

## Overview / Context

OpenShot already gives Linux creators something rare: a free editor that can
handle real work. For art films, experimental musical edits, and AI-heavy
video projects, the problem is usually not basic trimming. The problem is that
the editor still forces too many distinct workflows through the same small set
of clip transforms and timeline keyframes.

This mission captures a set of related control-surface improvements:

- a dedicated effects properties panel that is organized by intent instead of
  by raw schema,
- a color grading toolkit that makes fine-grained color changes manageable,
- a `Reset Clip` action that clears clip-assigned state without changing timing
  or cropping,
- a clearer exporter that exposes dimensions, codec, quality, and processor
  choice,
- a canvas/framing model that is separate from clip-layer transforms,
- better keyframe access for alignment and animation work,
- and a local pairing surface through MCP so an agent can inspect real project
  state.

The recurring daily pain point is source alignment. Different tools do not
agree on what `16:9` means, and the resulting clips are usually close rather
than identical. Today, the user often has to fake a static framing correction
with keyframes at the start, or at both start and finish. That is the wrong
abstraction for a lot of these cases. The editor should make static alignment
cheap, visible, and reversible.

## User Scenarios & Testing

### Scenario 1: Normalize mismatched AI-generated clips

- A user imports clips produced by different generators.
- The clips are close, but not perfectly aligned in frame.
- The user adjusts a project canvas or framing control once instead of
  keyframing every clip individually.
- The result lines up cleanly across the timeline without hiding the problem in
  animation data.

### Scenario 2: Find and edit effects without hunting

- A user selects a clip with several effects assigned.
- The properties dock shows only the categories that matter for that object.
- The user can expand a category, inspect a control, and change it directly.
- Advanced properties remain available, but they do not dominate the panel.

### Scenario 3: Reset a clip without losing timing

- A user right-clicks a clip and chooses `Reset Clip`.
- The clip keeps its position, duration, trim, and crop.
- All clip-assigned effects, keyframes, and other non-timing clip settings are
  removed.
- The timeline timing does not change.

### Scenario 4: Export with more confidence

- A user opens the exporter.
- Width, height, codec, quality, and CPU/GPU/Auto processing are visible at a
  glance.
- The quality control feels like a real slider instead of a three-label preset.
- The user can tell which processor will be used before export starts.

### Scenario 5: Pair with an agent locally

- A user drops a local image or video path into a pairing flow.
- The agent can inspect metadata and representative frames.
- The user and agent discuss framing or export changes using the same local
  project state.
- Any write action is explicit and confirmed.

## Domain Language

| Term | Canonical meaning | Avoid |
|------|-------------------|-------|
| Project canvas | The project-level frame and aspect-ratio geometry, separate from clip transforms | "canvas size" when the project frame is meant |
| Clip transform | Per-clip position, scale, rotation, crop, and timing-adjacent adjustments | "canvas transform" |
| Static alignment | A constant framing correction that does not represent animation over time | "fake motion" |
| Effects properties panel | A categorized inspector for clip/effect settings organized by intent | "raw property dump" |
| Color grading toolkit | A dedicated surface for fine-grained color changes with explicit scope | "more color knobs" |
| Reset Clip | A right-click action that clears clip-assigned state but preserves timing and crop | "delete clip" |
| Quality slider | A continuous or fine-grained exporter control that communicates the tradeoff clearly | "low/medium/high" only |
| Processor selection | A choice between CPU, GPU, and Auto export processing | "hardware mode" |
| MCP pairing bridge | A local inspection/write bridge that lets an agent discuss real project state | "remote assistant hook" |

## Guiding Principles

1. Keep project framing separate from clip transforms.
2. Make static corrections static when possible.
3. Show the user scope clearly: clip, selection, or whole timeline.
4. Hide complexity until it is asked for.
5. Preserve the editor's existing strengths, especially clip resizing.
6. Keep the agent local, inspectable, and reversible.

## Requirements

### Functional Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| FR-001 | The editor provides a first-class project canvas/framing model that is separate from per-clip transforms. Canvas-level changes must support both dragging the aspect ratio and expanding the canvas while preserving aspect ratio. | Draft |
| FR-002 | The effects properties panel is grouped by category or intent, not shown as a flat schema dump. Common controls stay visible, advanced controls are collapsed by default, and the panel only surfaces sections relevant to the selected object. | Draft |
| FR-003 | The color grading toolkit exposes granular color controls in a manageable layout and clearly indicates whether the user is working on a selected clip, a selection range, or the whole timeline/project. | Draft |
| FR-004 | The right-click `Reset Clip` action removes clip-assigned effects, keyframes, and other non-timing clip state while preserving timeline timing, trim, crop, and placement. | Draft |
| FR-005 | Keyframes are easier to access and layer through a dedicated inspector or equivalent surface so users do not need to bury simple alignment corrections in timeline surgery. | Draft |
| FR-006 | The exporter exposes width, height, codec, quality, and processor choice as first-class controls. The quality control is fine-grained enough to communicate tradeoffs between smaller files and higher fidelity, and the processor choice includes CPU, GPU, and Auto. | Draft |
| FR-007 | The exporter makes the selected processing backend visible before export begins and falls back clearly when GPU processing is unavailable. | Draft |
| FR-008 | The UI makes it obvious when a user is editing clip-local state versus project-local state, especially in framing and color workflows. | Draft |
| FR-009 | A local MCP pairing bridge can inspect project state and selected media from local paths and can apply confirmed changes through a small, safe set of actions. | Draft |
| FR-010 | Existing clip resizing remains intact and should continue to feel direct; this mission extends the workflow instead of replacing the current clip-resize model. | Draft |

### Non-Functional Requirements

| ID | Requirement | Threshold / measure | Status |
|----|-------------|---------------------|--------|
| NFR-001 | Backward compatibility | Existing projects open without conversion work and existing clip resize behavior continues to function. | Draft |
| NFR-002 | Reversibility | Any new reset or framing action must be undo-friendly and not require destructive edits. | Draft |
| NFR-003 | Local-first behavior | Core editing and inspection workflows work locally on Linux without a network dependency. | Draft |
| NFR-004 | Clear affordances | Scope, processor, and export tradeoffs are visible at the point of use instead of being hidden in secondary dialogs. | Draft |
| NFR-005 | Regression safety | The new UI surfaces must have coverage for clip framing, reset behavior, exporter controls, and state-scope separation. | Draft |

### Constraints

| ID | Constraint | Status |
|----|------------|--------|
| C-001 | Keep the current Qt application and its existing clip-resize interaction model. | Draft |
| C-002 | Do not turn the project canvas into a second copy of clip transforms; the two concepts must remain distinct. | Draft |
| C-003 | `Reset Clip` must not change timeline timing or crop unless the user chooses a different action explicitly. | Draft |
| C-004 | The mission is a UI/workflow improvement, not a full render-engine rewrite or language port. | Draft |
| C-005 | MCP integration, if pursued, must remain local-first and explicit about any write action. | Draft |

## Implementation Phases

### Phase 1: Discovery and contracts

Map the current clip transform, property, export, and AI-related code paths.
Define what belongs to the project canvas, what belongs to the clip, and what
belongs to export settings or agent actions.

### Phase 2: Framing and canvas

Introduce the project canvas/framing model and make aspect ratio changes
possible without abusing per-clip keyframes.

### Phase 3: Properties and reset flow

Rework the properties dock into intent-based categories and add `Reset Clip`
as a safe, explicit recovery action.

### Phase 4: Color grading and keyframes

Build a color toolkit that feels closer to a dedicated grading surface and make
keyframes easier to inspect, layer, and reason about.

### Phase 5: Exporter redesign

Expose width, height, codec, quality, and CPU/GPU/Auto selection in a way that
is easy to understand at a glance.

### Phase 6: MCP pairing bridge

Add a local bridge that can inspect media, project state, and selected frames,
then apply confirmed changes safely.

### Phase 7: QA and docs

Add regression coverage, update the user-facing documentation, and document
the migration path for users who already rely on current clip-centric tools.

## Success Criteria

- Users can normalize AI-generated clips to a common frame without having to
  build a keyframe hack for every source.
- The properties dock feels categorized and manageable instead of like a raw
  schema browser.
- `Reset Clip` clears the right state and leaves timing alone.
- Export settings clearly show size, codec, quality, and processor choice.
- The editor still feels good for direct clip resizing.
- Color editing has a clear scope model, like per-clip versus whole timeline.
- If the MCP bridge is implemented, an agent can inspect local media and talk
  through changes without leaving the local project context.

## Key Entities

- **Project canvas** - the overall framing surface for the editor
- **Clip state** - per-clip transforms, effects, keyframes, and similar local
  settings
- **Color scope** - whether a grading edit applies to one clip, a selection, or
  the whole project
- **Export profile** - the chosen width, height, codec, quality, and processor
- **Pairing bridge** - a local inspection and confirmation surface for an agent

## Assumptions

- The current clip resize workflow is a strength and should remain direct.
- The user wants a categorized UI, not just more raw controls.
- The main pain is workflow clarity, not a request to replace the application
  architecture.
- The MCP bridge is a useful follow-on surface even if it lands after the core
  editor controls.

## Out of Scope

- A full rewrite of the application in another language.
- A new render engine or media backend.
- Replacing the current timeline interaction model outright.
- Cloud-hosted or remote-only agent integration.
- Reworking every dialog in the application at once.

## Traceability

This mission is grounded in the user-facing docs already added to the repo:

- `doc/creative_workflow_vision.rst`
- `doc/creative_workflow_plan.rst`
- `doc/creative_workflow_tasks.rst`
- `doc/creative_workflow_milestones.rst`
- `doc/creative_workflow_mission_breakdown.rst`
- `doc/creative_workflow_issues.rst`

Those docs provide the longer-form decomposition. This Spec Kitty mission is
the canonical planning artifact that will drive the follow-on `plan` and
`tasks` steps.
