---
work_package_id: WP05
title: MCP Pairing Bridge
dependencies:
- WP01
- WP02
- WP04
requirement_refs:
- FR-009
- NFR-003
- NFR-004
- C-005
tracker_refs: []
planning_base_branch: develop
merge_target_branch: develop
branch_strategy: Planning artifacts for this mission were generated on develop. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into develop unless the human explicitly redirects the landing branch.
subtasks:
- T016
- T017
- T018
- T019
phase: Phase 5 - MCP pairing bridge
assignee: ''
agent: ''
history:
- at: '2026-06-23T14:56:36Z'
  actor: system
  action: Prompt generated via /spec-kitty.tasks
agent_profile: ''
authoritative_surface: src/classes/mcp_bridge/
create_intent:
- src/classes/mcp_bridge/__init__.py
- src/classes/mcp_bridge/bridge.py
- src/classes/mcp_bridge/resources.py
- src/classes/mcp_bridge/inspectors.py
- src/windows/mcp_bridge_dialog.py
execution_mode: code_change
model: ''
owned_files:
- src/classes/mcp_bridge/__init__.py
- src/classes/mcp_bridge/bridge.py
- src/classes/mcp_bridge/resources.py
- src/classes/mcp_bridge/inspectors.py
- src/windows/mcp_bridge_dialog.py
role: ''
tags: []
task_type: implement
---

# Work Package Prompt: WP05 - MCP Pairing Bridge

## Do This First: Load Agent Profile

Load the best-fit implementer profile for local-inspection and safe-write
bridge work before reading the rest of the prompt.

- **Profile**: ``
- **Role**: ``
- **Agent/tool**: ``

If a profile has not been selected yet, run `spec-kitty agent profile list`
and choose the one best suited to local bridge work.

## Objective

Create a local MCP pairing surface that can inspect project state and local
media, then apply confirmed changes safely.

This bridge should help with the user's AI-heavy workflow without turning the
editor into a remote-control service.

## Context

The mission wants an agent to be able to reason about actual local media and
project state:

- inspect a video or image path,
- look at project and export state,
- and only then apply a bounded, explicit write action.

The bridge must remain local-first and inspectable.

## Branch Strategy

- **Planning base branch**: `develop`
- **Merge target branch**: `develop`

Keep the diff confined to the bridge modules and any small UI entry point that
is needed to surface the bridge.

## Subtasks & Detailed Guidance

### Subtask T016 - Define the minimal MCP resource surface

- **Purpose**: Decide what the bridge should expose before any tool is built.
- **Steps**:
  - Define the resource set for project state, media metadata, frame samples,
    and export settings.
  - Keep the surface minimal and local.
  - Make read-only access the default.
- **Files**:
  - `src/classes/mcp_bridge/resources.py`
  - `src/classes/mcp_bridge/bridge.py`
- **Parallel?**: This is the base for T017 and T018.
- **Notes**: Avoid broad or implicit access patterns.

### Subtask T017 - Add read-only inspection helpers

- **Purpose**: Let the agent inspect local image and video paths safely.
- **Steps**:
  - Add helpers that can summarize file metadata and representative frames.
  - Keep the inspection path local and side-effect free.
  - Make it easy to pair on framing and export decisions.
- **Files**:
  - `src/classes/mcp_bridge/inspectors.py`
  - `src/classes/mcp_bridge/bridge.py`
- **Parallel?**: Can overlap with T016 once the resource names are fixed.
- **Notes**: If a helper needs a new UI surface, keep it tiny.

### Subtask T018 - Add safe write actions

- **Purpose**: Apply confirmed project changes without requiring the agent to
  edit project files directly.
- **Steps**:
  - Define a bounded set of write actions.
  - Require explicit confirmation before mutating project state.
  - Keep the write path inspectable and local.
- **Files**:
  - `src/classes/mcp_bridge/bridge.py`
  - `src/windows/mcp_bridge_dialog.py`
- **Parallel?**: Follows from the resource contract.
- **Notes**: Do not let the bridge become a hidden automation path.

### Subtask T019 - Add bridge validation

- **Purpose**: Protect the bridge's safety and locality guarantees.
- **Steps**:
  - Add tests for the resource surface and confirmation behavior.
  - Add a note explaining the local-first contract.
- **Files**:
  - `src/tests/test_mcp_bridge.py` (new, if needed)
  - `doc/creative_workflow_plan.rst`
- **Parallel?**: Runs after the bridge surface is implemented.
- **Notes**: Emphasize safety and explicit confirmation in the tests.

## Test Strategy

- Run the bridge-related unit tests.
- Confirm the bridge can inspect local state without network dependence.
- Confirm every write path requires confirmation.

## Risks & Mitigations

- Risk: the bridge behaves like a remote control service.
- Mitigation: keep it local-first and read-first, with explicit writes only.

- Risk: the agent gains more access than the user intended.
- Mitigation: keep the resource surface minimal and bounded.

## Review Guidance

- Confirm that the bridge can inspect local media and project state.
- Confirm that every mutation is explicit and confirmable.
- Confirm that nothing about the bridge requires a network service.

## Activity Log

- 2026-06-23T14:56:36Z - system - Prompt created.
