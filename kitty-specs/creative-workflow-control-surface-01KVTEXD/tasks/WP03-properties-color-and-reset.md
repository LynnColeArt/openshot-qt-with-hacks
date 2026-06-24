---
work_package_id: WP03
title: Properties, Color, and Reset
dependencies:
- WP01
requirement_refs:
- FR-002
- FR-003
- FR-004
- FR-005
- FR-008
- NFR-002
- NFR-004
- NFR-005
- C-003
tracker_refs: []
planning_base_branch: develop
merge_target_branch: develop
branch_strategy: Planning artifacts for this mission were generated on develop. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into develop unless the human explicitly redirects the landing branch.
subtasks:
- T008
- T009
- T010
- T011
phase: Phase 3 - Properties, color, and reset
assignee: ''
agent: "python-pedro"
shell_pid: "324410"
history:
- at: '2026-06-23T14:56:36Z'
  actor: system
  action: Prompt generated via /spec-kitty.tasks
agent_profile: ''
authoritative_surface: src/windows/views/timeline.py
create_intent: []
execution_mode: code_change
model: ''
owned_files:
- src/windows/views/timeline.py
- src/windows/views/properties_tableview.py
- src/windows/color_grade_editor.py
- src/classes/color_presets.py
- src/windows/views/menu.py
role: ''
tags: []
task_type: implement
---

# Work Package Prompt: WP03 - Properties, Color, and Reset

## Do This First: Load Agent Profile

Load the best-fit implementer profile for Qt/Python UI and editor-state work
before reading the rest of the prompt.

- **Profile**: ``
- **Role**: ``
- **Agent/tool**: ``

If a profile has not been selected yet, run `spec-kitty agent profile list`
and choose the one that best fits properties-dock and timeline-menu work.

## Objective

Rework the properties dock into a categorized inspector, make the color
grading toolkit easier to reach and understand, and add a `Reset Clip` action
that clears clip-assigned state without changing timing or crop.

## Context

The app already has a color-grade editor and a timeline with look/color
context-menu actions. The missing piece is a clear presentation and scope
story:

- properties should be grouped by intent instead of dumped as a raw schema,
- color grading should make scope obvious,
- and clip reset should be a safe, explicit recovery action.

## Branch Strategy

- **Planning base branch**: `develop`
- **Merge target branch**: `develop`

Keep the implementation centered on the existing properties and timeline menu
surfaces. Avoid broad refactors outside the UI/state path for this work.

## Subtasks & Detailed Guidance

### Subtask T008 - Group properties by intent

- **Purpose**: Replace the flat-looking property view with categorized
  sections that match how creators think.
- **Steps**:
  - Define the categories and their default collapsed/expanded behavior.
  - Keep common controls easy to reach.
  - Push lower-use and advanced controls out of the way until the user asks
    for them.
- **Files**:
  - `src/windows/views/properties_tableview.py`
  - `src/windows/views/menu.py`
- **Parallel?**: Mostly sequential with T009 because both affect how the dock
  reads.
- **Notes**: Categories that are too broad will still feel noisy.

### Subtask T009 - Surface color grading clearly

- **Purpose**: Make the existing color-grading toolkit easy to find and make
  its editing scope obvious.
- **Steps**:
  - Reuse the current color-grade curve and wheels UI instead of replacing it.
  - Make it obvious whether the user is editing a clip, a selection, or the
    broader project/timeline scope.
  - Keep the live update behavior and the color-grade dock in sync.
- **Files**:
  - `src/windows/views/properties_tableview.py`
  - `src/windows/color_grade_editor.py`
  - `src/classes/color_presets.py`
  - `src/windows/views/menu.py`
- **Parallel?**: Can overlap with T008 after the category model is agreed.
- **Notes**: The goal is reachability and clarity, not new color math.

### Subtask T010 - Add `Reset Clip`

- **Purpose**: Add a clip-context action that clears clip-assigned state while
  preserving timing, trim, and crop.
- **Steps**:
  - Add the menu action on the clip context menu.
  - Remove effects, keyframes, and other clip-assigned state in one undoable
    action.
  - Make sure crop survives unless the user chooses a more destructive action.
- **Files**:
  - `src/windows/views/timeline.py`
  - `src/windows/views/menu.py`
  - `src/classes/clip_utils.py`
- **Parallel?**: Should follow the scope rules from T008/T009.
- **Notes**: This action must be explicit about what it preserves.

### Subtask T011 - Add tests and docs

- **Purpose**: Protect the properties, color, and reset behavior with tests and
  user-facing notes.
- **Steps**:
  - Add regression tests for the category grouping and reset semantics.
  - Add a small doc note that explains the new scope language.
  - Keep the docs in sync with the UI labels.
- **Files**:
  - `src/tests/test_properties_tableview.py` (new, if needed)
  - `src/tests/test_color_grade_editor.py`
  - `src/tests/test_timeline_helpers.py`
- **Parallel?**: Runs after the UI/state work is in place.
- **Notes**: Focus on behavior that users can observe directly.

## Test Strategy

- Add unit tests for reset semantics and the color-grade helper behavior.
- Confirm the categorized inspector still updates correctly when the selected
  clip changes.
- Manually verify that `Reset Clip` preserves timing and crop.

## Risks & Mitigations

- Risk: the dock becomes a maze of sections and sub-sections.
- Mitigation: keep the default view calm and collapse low-use sections.

- Risk: `Reset Clip` removes too much or too little state.
- Mitigation: define the preserved state explicitly in the tests and the
  review checklist.

## Review Guidance

- Confirm that the properties panel is categorized by intent instead of being
  a raw schema dump.
- Confirm that the color toolkit is easier to reach and that scope is visible.
- Confirm that `Reset Clip` preserves timing and crop.

## Activity Log

- 2026-06-23T14:56:36Z - system - Prompt created.
- 2026-06-24T06:16:32Z – python-pedro – shell_pid=324410 – Assigned agent via action command
