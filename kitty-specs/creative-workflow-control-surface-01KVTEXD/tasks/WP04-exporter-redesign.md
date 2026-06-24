---
work_package_id: WP04
title: Exporter Redesign
dependencies:
- WP01
requirement_refs:
- FR-006
- FR-007
- NFR-004
- C-004
tracker_refs: []
planning_base_branch: develop
merge_target_branch: develop
branch_strategy: Planning artifacts for this mission were generated on develop. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into develop unless the human explicitly redirects the landing branch.
subtasks:
- T012
- T013
- T014
- T015
phase: Phase 4 - Exporter redesign
assignee: ''
agent: ''
history:
- at: '2026-06-23T14:56:36Z'
  actor: system
  action: Prompt generated via /spec-kitty.tasks
agent_profile: ''
authoritative_surface: src/windows/export.py
create_intent: []
execution_mode: code_change
model: ''
owned_files:
- src/windows/export.py
- src/windows/ui/export.ui
role: ''
tags: []
task_type: implement
---

# Work Package Prompt: WP04 - Exporter Redesign

## Do This First: Load Agent Profile

Load the best-fit implementer profile for Qt dialog and encoder-mapping work
before reading the rest of the prompt.

- **Profile**: ``
- **Role**: ``
- **Agent/tool**: ``

If a profile has not been selected yet, run `spec-kitty agent profile list`
and choose the best fit for export-dialog work.

## Objective

Make the exporter answer the creator's key questions immediately:

- how big is the export,
- what codec is it using,
- how much quality am I trading away,
- and which processor will do the work.

## Context

The export dialog already has simple and advanced paths, quality handling, and
processor-aware code. This WP should reshape the UI so the existing backend is
easier to understand rather than replacing the backend outright.

## Branch Strategy

- **Planning base branch**: `develop`
- **Merge target branch**: `develop`

Keep the diff constrained to `src/windows/export.py` and `src/windows/ui/export.ui`.

## Subtasks & Detailed Guidance

### Subtask T012 - Rework the size and codec controls

- **Purpose**: Make width, height, and codec first-class export decisions.
- **Steps**:
  - Move the important size/codec fields into the primary export view.
  - Keep the existing advanced behavior available without forcing it first.
  - Ensure the dialog makes it obvious which export profile is active.
- **Files**:
  - `src/windows/export.py`
  - `src/windows/ui/export.ui`
- **Parallel?**: This is the base for the quality and processor changes.
- **Notes**: The user should not have to decode a preset name to understand
  the export size.

### Subtask T013 - Add a fine-grained quality control

- **Purpose**: Replace the coarse low/medium/high story with a slider or
  equivalent control that makes the compression tradeoff legible.
- **Steps**:
  - Map the slider or stepped control onto the current bitrate/quality logic.
  - Make the control readable at a glance.
  - Preserve any existing settings behavior that users rely on.
- **Files**:
  - `src/windows/export.py`
  - `src/windows/ui/export.ui`
- **Parallel?**: Can overlap with T014 once the control mapping is agreed.
- **Notes**: The control should communicate tradeoff, not just a label.

### Subtask T014 - Expose CPU/GPU/Auto processor selection

- **Purpose**: Make the processing backend visible and selectable.
- **Steps**:
  - Add processor choice to the dialog in a way the user can understand at a
    glance.
  - Show which backend is selected before export starts.
  - Handle the GPU-unavailable path clearly and gracefully.
- **Files**:
  - `src/windows/export.py`
  - `src/windows/ui/export.ui`
- **Parallel?**: Can overlap with T013 after the backend mapping is clear.
- **Notes**: The UI must not imply GPU support when it is not available.

### Subtask T015 - Add exporter validation

- **Purpose**: Lock the mapping between the new UI and the existing export
  backend.
- **Steps**:
  - Add tests for size, quality, and processor settings.
  - Add a doc note that explains how the new controls map to the current
    export logic.
- **Files**:
  - `src/tests/test_export.py` (new, if needed)
  - `src/tests/test_timeline_helpers.py`
  - `doc/creative_workflow_plan.rst`
- **Parallel?**: Runs after the dialog changes are in place.
- **Notes**: Keep the tests focused on visible settings and backend mapping.

## Test Strategy

- Run the exporter-related unit tests.
- Verify the dialog still reaches the existing export backend.
- Manually confirm that the selected processor is visible before export.

## Risks & Mitigations

- Risk: the exporter looks simpler but hides the actual tradeoff.
- Mitigation: keep quality and processor selection explicit and readable.

- Risk: the dialog implies encoder support that the platform does not have.
- Mitigation: fall back clearly and label the selected backend.

## Review Guidance

- Confirm that width, height, codec, quality, and processor are all visible.
- Confirm that the quality control is more granular than low/medium/high.
- Confirm that the processor choice matches what the backend can actually do.

## Activity Log

- 2026-06-23T14:56:36Z - system - Prompt created.
