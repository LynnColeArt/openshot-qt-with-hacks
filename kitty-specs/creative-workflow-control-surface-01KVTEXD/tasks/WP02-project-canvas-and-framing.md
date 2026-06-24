---
work_package_id: WP02
title: Project Canvas and Framing
dependencies:
- WP01
requirement_refs:
- FR-001
- FR-005
- FR-008
- FR-010
- NFR-001
- NFR-002
- C-001
- C-002
tracker_refs: []
planning_base_branch: develop
merge_target_branch: develop
branch_strategy: Planning artifacts for this mission were generated on develop. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into develop unless the human explicitly redirects the landing branch.
subtasks:
- T004
- T005
- T006
- T007
phase: Phase 2 - Framing and canvas
assignee: ''
agent: ''
history:
- at: '2026-06-23T14:56:36Z'
  actor: system
  action: Prompt generated via /spec-kitty.tasks
agent_profile: ''
authoritative_surface: src/windows/views/timeline_backend/
create_intent:
- src/windows/views/timeline_backend/project_canvas.py
execution_mode: code_change
model: ''
owned_files:
- src/windows/views/timeline_backend/project_canvas.py
- src/windows/views/timeline_backend/qwidget/base.py
- src/windows/views/timeline_backend/qwidget/keyframe.py
- src/windows/views/timeline_backend/qwidget/keyframe_panel.py
- src/windows/views/timeline_backend/paint/keyframepanel.py
- src/classes/clip_utils.py
role: ''
tags: []
task_type: implement
---

# Work Package Prompt: WP02 - Project Canvas and Framing

## Do This First: Load Agent Profile

Load the best-fit implementer profile for Qt/Python UI work before reading the
rest of the prompt.

- **Profile**: ``
- **Role**: ``
- **Agent/tool**: ``

If a profile has not been selected yet, run `spec-kitty agent profile list`
and choose one appropriate for desktop UI implementation work.

## Objective

Introduce a first-class project canvas/framing model that can be resized or
re-aspected without pretending to be per-clip animation.

This WP should make the following ideas real:

- the project frame is distinct from clip transforms,
- static alignment corrections are cheap and visible,
- project-frame changes are reversible,
- and the current direct clip-resize workflow still feels intact.

## Context

The current timeline backend already owns:

- clip geometry and keyframe display,
- track layout and selection handling,
- and the panel logic that draws and manipulates keyframes.

The mission wants to add a separate project-framing concept without wrecking
that behavior. The easiest route is to add a small canvas/framing abstraction
and then teach the timeline surface how to display it clearly.

## Branch Strategy

- **Planning base branch**: `develop`
- **Merge target branch**: `develop`

This WP will land as a code change. Keep the diff constrained to canvas and
framing surfaces so review stays manageable.

## Subtasks & Detailed Guidance

### Subtask T004 - Define the project canvas model

- **Purpose**: Give the app a distinct project-frame model and the rules for
  resizing, aspect-ratio changes, fit/fill behavior, and anchoring.
- **Steps**:
  - Add the canvas model or helper layer that stores project frame geometry.
  - Define how aspect-ratio dragging differs from expanding the canvas while
    preserving ratio.
  - Make the model explicit about whether the user is editing the project or a
    clip.
- **Files**:
  - `src/windows/views/timeline_backend/project_canvas.py`
  - `src/classes/clip_utils.py`
- **Parallel?**: This is the foundation for T005 and T006.
- **Notes**: The canvas model must not be a second copy of clip transforms.

### Subtask T005 - Add project-frame controls

- **Purpose**: Surface the new framing controls in the UI.
- **Steps**:
  - Add controls to the relevant timeline or dock surface for project framing.
  - Make the current scope obvious when the user is editing the project frame.
  - Ensure the UI can show the current aspect-ratio mode and whether the frame
    is being expanded or re-aspected.
- **Files**:
  - `src/windows/views/timeline_backend/qwidget/base.py`
  - `src/windows/views/timeline_backend/qwidget/keyframe_panel.py`
  - `src/windows/views/timeline_backend/qwidget/keyframe.py`
  - `src/windows/views/timeline_backend/paint/keyframepanel.py`
  - `src/windows/views/timeline_backend/project_canvas.py`
- **Parallel?**: Can proceed alongside T006 once T004 is settled.
- **Notes**: Keep the existing clip resize interactions direct and familiar.

### Subtask T006 - Make static alignment explicit

- **Purpose**: Stop forcing static alignment corrections through keyframe hacks.
- **Steps**:
  - Distinguish static offsets from animated motion in the framing workflow.
  - Make it clear when an edit is a constant correction versus a timeline
    animation.
  - Ensure any static offset tools remain undo-friendly.
- **Files**:
  - `src/windows/views/timeline_backend/qwidget/base.py`
  - `src/windows/views/timeline_backend/qwidget/keyframe.py`
  - `src/windows/views/timeline_backend/qwidget/keyframe_panel.py`
  - `src/classes/clip_utils.py`
- **Parallel?**: Can overlap with T005 after the shared canvas rules are
  defined.
- **Notes**: The goal is to normalize mismatched AI sources without keyframe
  surgery.

### Subtask T007 - Add regression coverage

- **Purpose**: Protect the new framing behavior from regressions.
- **Steps**:
  - Add tests for project-frame changes, aspect-ratio handling, and static
    alignment flows.
  - Add smoke checks for the existing clip resize behavior so it stays direct.
  - Verify the timeline still handles normal clip transforms correctly.
- **Files**:
  - `src/tests/test_timeline_helpers.py`
  - `src/tests/test_keyframe_scaler.py`
  - `src/tests/test_timeline_canvas.py` (new, if needed)
- **Parallel?**: Runs after the implementation pieces are in place.
- **Notes**: If a new test module is needed, keep it focused on the canvas
  boundary and alignment semantics.

## Test Strategy

- Run the relevant unit tests under `src/tests/`.
- Confirm the new frame model works with the current timeline UI.
- Manually verify that clip resizing still feels direct.

## Risks & Mitigations

- Risk: the project frame turns into a second clip-transform layer.
- Mitigation: keep project framing explicitly separate in the model and the UI.

- Risk: the timeline becomes harder to understand for users who only want to
  do straightforward clip resizing.
- Mitigation: leave the current resize workflow intact and make the new canvas
  controls additive.

## Review Guidance

- Confirm that static alignment is handled as a static case, not as fake
  motion.
- Confirm that the project canvas is not storing per-clip animation data.
- Confirm that current clip resizing still behaves the way OpenShot users
  expect.

## Activity Log

- 2026-06-23T14:56:36Z - system - Prompt created.
