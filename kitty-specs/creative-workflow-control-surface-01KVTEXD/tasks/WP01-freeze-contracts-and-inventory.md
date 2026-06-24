---
work_package_id: WP01
title: Freeze Contracts and Inventory
dependencies: []
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
- T001
- T002
- T003
phase: Phase 1 - Discovery and contracts
assignee: ''
agent: ''
history:
- at: '2026-06-23T14:56:36Z'
  actor: system
  action: Prompt generated via /spec-kitty.tasks
agent_profile: ''
authoritative_surface: kitty-specs/creative-workflow-control-surface-01KVTEXD/
create_intent: []
execution_mode: planning_artifact
model: ''
owned_files:
- doc/creative_workflow_vision.rst
- doc/creative_workflow_plan.rst
- doc/creative_workflow_tasks.rst
- doc/creative_workflow_mission_breakdown.rst
- doc/creative_workflow_issues.rst
- doc/index.rst
- kitty-specs/creative-workflow-control-surface-01KVTEXD/plan.md
- kitty-specs/creative-workflow-control-surface-01KVTEXD/research.md
- kitty-specs/creative-workflow-control-surface-01KVTEXD/data-model.md
- kitty-specs/creative-workflow-control-surface-01KVTEXD/quickstart.md
- kitty-specs/creative-workflow-control-surface-01KVTEXD/spec-kitty-bugs.md
role: ''
tags: []
task_type: plan
---

# Work Package Prompt: WP01 - Freeze Contracts and Inventory

## Do This First: Load Agent Profile

Use `/ad-hoc-profile-load` with a planning/profile choice that matches the
mission's documentation-heavy scope before reading the rest of this prompt.

- **Profile**: ``
- **Role**: ``
- **Agent/tool**: ``

If no profile has been selected yet, run `spec-kitty agent profile list` and
choose the best fit for planning and inventory work.

## Objective

Inventory the current OpenShot surfaces that matter for the mission and freeze
the state-boundary contract that later WPs must respect.

This WP does not change product code. Its job is to make sure the plan and
downstream task prompts are grounded in reality:

- what already exists,
- what is already partially implemented,
- what counts as project state versus clip state,
- and what must stay local or reversible.

## Context

Use the current repository and the mission docs as the source of truth:

- `kitty-specs/creative-workflow-control-surface-01KVTEXD/spec.md`
- `kitty-specs/creative-workflow-control-surface-01KVTEXD/plan.md`
- `kitty-specs/creative-workflow-control-surface-01KVTEXD/research.md`
- `kitty-specs/creative-workflow-control-surface-01KVTEXD/data-model.md`
- `doc/creative_workflow_plan.rst`
- `doc/creative_workflow_tasks.rst`
- `doc/creative_workflow_mission_breakdown.rst`

The current codebase already contains:

- a QWidget timeline with context-menu actions,
- a properties dock with color-grade curve/wheels editors,
- a keyframe panel and keyframe context menus,
- and an exporter dialog with existing quality and processor logic.

The most important outcome here is a clean contract, not implementation work.

## Branch Strategy

- **Planning base branch**: `develop`
- **Merge target branch**: `develop`

This WP only edits planning artifacts in `kitty-specs/` and the related mission
docs. It should not touch product source files.

## Subtasks & Detailed Guidance

### Subtask T001 - Inventory current surfaces

- **Purpose**: Identify the code paths and docs that already implement or hint
  at the requested workflow.
- **Steps**:
  - Review `src/windows/views/timeline.py`, `src/windows/views/properties_tableview.py`,
    `src/windows/color_grade_editor.py`, `src/windows/export.py`, and the
    keyframe modules.
  - Note where current features already exist, such as color grading, look
    presets, keyframe editing, crop/layout reset, and export quality mapping.
  - Write down the exact file paths and a short summary of the current
    behavior.
- **Files**:
  - `kitty-specs/creative-workflow-control-surface-01KVTEXD/research.md`
  - `kitty-specs/creative-workflow-control-surface-01KVTEXD/plan.md`
- **Parallel?**: Can overlap with T002 after the inventory target list is set.
- **Notes**: Prefer evidence over memory; if a behavior already exists, say so
  explicitly.

### Subtask T002 - Freeze the boundary matrix

- **Purpose**: Define what is project canvas state, clip state, export state,
  selection state, and MCP state.
- **Steps**:
  - Write the boundary rules in `data-model.md`.
  - Make scope language explicit: clip, selection, project/timeline, export,
    local media path.
  - Call out which actions must remain reversible and which ones are
    read-only.
- **Files**:
  - `kitty-specs/creative-workflow-control-surface-01KVTEXD/data-model.md`
  - `kitty-specs/creative-workflow-control-surface-01KVTEXD/plan.md`
- **Parallel?**: Can overlap with T001 once the source list is known.
- **Notes**: This matrix should be stable enough that every later WP can cite
  it without re-litigating the semantics.

### Subtask T003 - Capture risks and validation checks

- **Purpose**: Record the implementation risks and the validation commands that
  future WPs should use.
- **Steps**:
  - Summarize the core risks for framing, properties, reset, export, and MCP.
  - Add the validation scenarios to `quickstart.md`.
  - Add the Spec Kitty issue notes so they can be sent to Robert if needed.
- **Files**:
  - `kitty-specs/creative-workflow-control-surface-01KVTEXD/quickstart.md`
  - `kitty-specs/creative-workflow-control-surface-01KVTEXD/spec-kitty-bugs.md`
- **Parallel?**: Best done after T001/T002 so the risks reflect the actual
  boundaries.
- **Notes**: Keep the notes short and actionable; the goal is to unblock the
  implementation WPs, not to create a second spec.

## Test Strategy

- There are no product tests in this WP.
- Sanity-check the mission artifacts for internal consistency.
- Keep the validation commands in `quickstart.md` aligned with the repo
  reality.

## Risks & Mitigations

- Risk: later WPs inherit fuzzy state boundaries.
- Mitigation: keep the boundary matrix concrete and re-use the terminology in
  every later prompt.

- Risk: the inventory misses already-existing partial implementations.
- Mitigation: record current behavior even when it is incomplete, especially
  the existing color-grade and keyframe surfaces.

## Review Guidance

- Confirm that the plan explains the real repository surfaces instead of
  inventing a new architecture.
- Confirm that the boundary matrix distinguishes project canvas from clip
  transforms.
- Confirm that the bug note captures the Spec Kitty issues worth sending to
  Robert.

## Activity Log

- 2026-06-23T14:56:36Z - system - Prompt created.
- 2026-06-24T05:01:30Z – user – WP01 planning docs and inventory are complete
