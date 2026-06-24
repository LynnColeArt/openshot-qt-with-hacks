---
work_package_id: WP06
title: QA, Docs, and Regression Hardening
dependencies:
- WP01
- WP02
- WP03
- WP04
- WP05
requirement_refs:
- FR-001
- FR-002
- FR-003
- FR-004
- FR-005
- FR-006
- FR-007
- FR-008
- FR-009
- FR-010
- NFR-001
- NFR-002
- NFR-003
- NFR-004
- NFR-005
- C-001
- C-002
- C-003
- C-004
- C-005
tracker_refs: []
planning_base_branch: develop
merge_target_branch: develop
branch_strategy: Planning artifacts for this mission were generated on develop. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into develop unless the human explicitly redirects the landing branch.
subtasks:
- T020
- T021
- T022
- T023
phase: Phase 6 - QA and docs
assignee: ''
agent: ''
history:
- at: '2026-06-23T14:56:36Z'
  actor: system
  action: Prompt generated via /spec-kitty.tasks
agent_profile: ''
authoritative_surface: src/tests/
create_intent:
- src/tests/test_export.py
- src/tests/test_mcp_bridge.py
execution_mode: code_change
model: ''
owned_files:
- src/tests/test_timeline_helpers.py
- src/tests/test_color_grade_editor.py
- src/tests/test_export.py
- src/tests/test_mcp_bridge.py
- doc/creative_workflow_vision.rst
- doc/creative_workflow_plan.rst
- doc/creative_workflow_tasks.rst
- doc/creative_workflow_milestones.rst
- doc/creative_workflow_mission_breakdown.rst
- doc/creative_workflow_issues.rst
role: ''
tags: []
task_type: implement
---

# Work Package Prompt: WP06 - QA, Docs, and Regression Hardening

## Do This First: Load Agent Profile

Load the best-fit profile for testing and documentation work before reading
the rest of the prompt.

- **Profile**: ``
- **Role**: ``
- **Agent/tool**: ``

If a profile has not been selected yet, run `spec-kitty agent profile list`
and choose the best fit for regression and docs work.

## Objective

Protect the new workflow with tests, documentation, and a clear migration note.

This WP should make sure the new surfaces are:

- testable,
- understandable,
- and safe for existing users who already rely on clip-centric workflows.

## Context

The earlier WPs will have changed how several pieces of the editor feel. This
WP is where we make sure the mission lands as a coherent workflow instead of a
set of disconnected UI tweaks.

## Branch Strategy

- **Planning base branch**: `develop`
- **Merge target branch**: `develop`

Keep the diff within tests and docs. If a small implementation fix is needed
to make the validation story truthful, keep it minimal and explain it in the
review notes.

## Subtasks & Detailed Guidance

### Subtask T020 - Add regression tests for the workflow

- **Purpose**: Cover the canvas, properties, reset, export, and keyframe
  flows with targeted tests.
- **Steps**:
  - Add or expand unit tests for the important state transitions.
  - Keep the tests focused on user-visible behavior.
  - Validate the new scope distinctions.
- **Files**:
  - `src/tests/test_timeline_helpers.py`
  - `src/tests/test_color_grade_editor.py`
  - `src/tests/test_export.py`
  - `src/tests/test_mcp_bridge.py`
- **Parallel?**: Primarily sequential with the docs work once the behavior is
  stable.
- **Notes**: Use the tests to protect the semantics, not just the code paths.

### Subtask T021 - Update the user-facing docs

- **Purpose**: Make sure the docs use the same language as the UI.
- **Steps**:
  - Update the mission docs and the repo docs to describe project canvas vs
    clip transform, property categories, color scope, and export controls.
  - Keep the wording aligned with the actual labels in the UI.
- **Files**:
  - `doc/creative_workflow_vision.rst`
  - `doc/creative_workflow_plan.rst`
  - `doc/creative_workflow_tasks.rst`
  - `doc/creative_workflow_milestones.rst`
  - `doc/creative_workflow_mission_breakdown.rst`
  - `doc/creative_workflow_issues.rst`
- **Parallel?**: Can overlap with T022 once the terminology is stable.
- **Notes**: If the UI labels change, the docs must change with them.

### Subtask T022 - Write the migration note

- **Purpose**: Explain what changed for users who already rely on keyframes
  and the current look tools.
- **Steps**:
  - Describe what remains unchanged.
  - Call out the new project-canvas model and the new reset behavior.
  - Keep the migration note short and practical.
- **Files**:
  - `doc/creative_workflow_mission_breakdown.rst`
  - `doc/creative_workflow_plan.rst`
- **Parallel?**: Can overlap with T021 once the content outline is agreed.
- **Notes**: The note should reduce surprise, not market the feature.

### Subtask T023 - Run validation and capture follow-ups

- **Purpose**: Finish with the repository validation commands and capture any
  follow-up issues in the Spec Kitty bug note.
- **Steps**:
  - Run the repository tests and doc build.
  - Record any Spec Kitty tooling issues or mission follow-ups.
  - Make sure the final notes are ready for handoff.
- **Files**:
  - `kitty-specs/creative-workflow-control-surface-01KVTEXD/spec-kitty-bugs.md`
- **Parallel?**: Runs after the tests and docs are in place.
- **Notes**: This is the last hardening pass before handoff.

## Test Strategy

- Run `python3 -m unittest discover -s src/tests -t src/tests --quiet`.
- Run `cd doc && make html`.
- Verify the user-facing docs and the migration note match the UI language.

## Risks & Mitigations

- Risk: the tests cover only implementation details.
- Mitigation: test the visible behavior and the state boundaries.

- Risk: the docs drift away from the UI.
- Mitigation: keep the same terminology in the docs, prompts, and review notes.

## Review Guidance

- Confirm the regression tests protect the new canvas, properties, reset, and
  export flows.
- Confirm the docs use the same words that the UI uses.
- Confirm the migration note explains the change without overstating it.

## Activity Log

- 2026-06-23T14:56:36Z - system - Prompt created.
