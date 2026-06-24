# Tasks: Creative Workflow Control Surface

**Mission**: creative-workflow-control-surface-01KVTEXD
**Branch**: `kitty/mission-creative-workflow-control-surface-01KVTEXD` -> target `develop`
**Plan**: [plan.md](plan.md) | **Spec**: [spec.md](spec.md)

---

## Subtask Index

| ID | Description | WP | Parallel |
|---|---|---|---|
| T001 | Inventory the current timeline, properties, export, keyframe, and color surfaces and record what already exists | WP01 | - |
| T002 | Freeze the boundary matrix for project canvas, clip state, export state, and MCP state | WP01 | - |
| T003 | Capture the rollout risks, validation checklist, and follow-up questions for the implementation plan | WP01 | - |
| T004 | Define the project canvas model and how aspect ratio, expand, fit, fill, and anchor should behave | WP02 | - |
| T005 | Add project-frame controls and separate them from clip-layer transforms in the timeline surfaces | WP02 | [P] |
| T006 | Make static alignment corrections possible without forcing per-clip keyframe hacks | WP02 | [P] |
| T007 | Add regression coverage for canvas/framing and static-alignment flows | WP02 | - |
| T008 | Group clip and effect properties into categorized sections and hide low-use sections by default | WP03 | - |
| T009 | Make the color grading toolkit easier to reach and clearly label whether it applies to a clip or a broader scope | WP03 | [P] |
| T010 | Add `Reset Clip` to clear clip-assigned state while preserving timing and crop | WP03 | - |
| T011 | Add tests and documentation for properties grouping, color scope, and reset behavior | WP03 | - |
| T012 | Rework the export dialog so width, height, and codec are first-class controls | WP04 | - |
| T013 | Replace coarse quality labels with a finer-grained slider and a clearer quality readout | WP04 | [P] |
| T014 | Expose CPU, GPU, and Auto processor choices and show the selected backend clearly | WP04 | [P] |
| T015 | Add exporter tests and documentation for quality and processor mapping | WP04 | - |
| T016 | Define the minimal MCP resource surface for project state, media inspection, and export settings | WP05 | - |
| T017 | Add local read-only inspection helpers for image and video paths | WP05 | [P] |
| T018 | Add safe write actions that only apply confirmed project changes | WP05 | - |
| T019 | Add bridge tests and notes for local-first, confirmation-based behavior | WP05 | - |
| T020 | Add regression tests for the new canvas, properties, reset, export, and keyframe flows | WP06 | - |
| T021 | Update the user-facing docs so the new abstractions use the same words as the UI | WP06 | [P] |
| T022 | Add a migration note for users who already rely on clip keyframes and the current look tools | WP06 | [P] |
| T023 | Run the repository validation commands and capture any Spec Kitty follow-ups in the bug note | WP06 | - |

---

## Work Package 1 - Freeze Contracts and Inventory

**Goal**: Capture the current behavior and lock down the state boundaries before implementation begins.
**Independent Test**: The inventory and boundary matrix name the current surfaces, the state categories are unambiguous, and the plan can be traced back to the repo reality.
**Prompt**: [WP01-freeze-contracts-and-inventory.md](tasks/WP01-freeze-contracts-and-inventory.md)
**Requirement Refs**: FR-001 through FR-010, NFR-001 through NFR-005, C-001 through C-005

### Included Subtasks

- [ ] T001 Inventory the current surfaces and note the existing code paths
- [ ] T002 Freeze the boundary matrix for project canvas, clip state, export state, and MCP state
- [ ] T003 Capture rollout risks, validation checks, and open questions

### Implementation Notes

- Ground the inventory in the current repository surfaces, not in assumptions.
- Call out where the app already has partial support, such as color grading,
  keyframes, and export quality controls.
- Keep this work read-only against product code.

### Parallel Opportunities

- T001 and T002 can be split if one person is gathering code-path evidence
  while another writes the boundary matrix.

### Dependencies

- None.

### Risks & Mitigations

- Risk: later work reclassifies clip state without noticing.
- Mitigation: keep the boundary matrix explicit and reference it in every
  later WP prompt.

---

## Work Package 2 - Project Canvas and Framing

**Goal**: Introduce a first-class project frame and make static alignment easy without abusing clip animation.
**Independent Test**: A project can change aspect ratio or expand the canvas without turning the correction into per-clip keyframes.
**Prompt**: [WP02-project-canvas-and-framing.md](tasks/WP02-project-canvas-and-framing.md)
**Requirement Refs**: FR-001, FR-005, FR-008, FR-010, NFR-001, NFR-002, C-001, C-002

### Included Subtasks

- [ ] T004 Define the project canvas model and aspect/fill/anchor behaviors
- [ ] T005 Add project-frame controls and separate them from clip-layer transforms
- [ ] T006 Make static alignment corrections possible without keyframe hacks
- [ ] T007 Add regression coverage for canvas/framing and alignment flows

### Implementation Notes

- Keep the project canvas separate from clip geometry, even if the first
  version is exposed through a small helper module or dock.
- Treat static alignment as a first-class case, not as a special animation.

### Parallel Opportunities

- T005 and T006 can be split once the canvas contract is written.

### Dependencies

- Depends on WP01.

### Risks & Mitigations

- Risk: the new frame model becomes a second clip-transform UI.
- Mitigation: keep the canvas controls distinct and make scope obvious.

---

## Work Package 3 - Properties, Color, and Reset

**Goal**: Make the properties dock categorized, make color grading easier to reach, and add `Reset Clip`.
**Independent Test**: A user can find properties by category, open the color tools with a clear scope, and reset a clip without losing timing or crop.
**Prompt**: [WP03-properties-color-and-reset.md](tasks/WP03-properties-color-and-reset.md)
**Requirement Refs**: FR-002, FR-003, FR-004, FR-005, FR-008, NFR-002, NFR-004, NFR-005, C-003

### Included Subtasks

- [ ] T008 Group properties into categorized sections and hide low-use sections by default
- [ ] T009 Make the color grading toolkit easy to reach and clearly scoped
- [ ] T010 Add `Reset Clip` while preserving timing and crop
- [ ] T011 Add tests and docs for properties grouping, color scope, and reset behavior

### Implementation Notes

- Reuse the existing color-grade editor instead of inventing a second editor.
- Make `Reset Clip` explicit about what it does not change.
- Keep the advanced property surface available for edge cases.

### Parallel Opportunities

- T008 and T009 can overlap after the category model is agreed.

### Dependencies

- Depends on WP01.

### Risks & Mitigations

- Risk: the properties panel becomes a noisy schema dump again.
- Mitigation: collapse low-use sections and keep scope labels visible.

---

## Work Package 4 - Exporter Redesign

**Goal**: Make export size, codec, quality, and processor choice visible and understandable.
**Independent Test**: The export dialog clearly exposes width, height, codec, quality, and CPU/GPU/Auto selection.
**Prompt**: [WP04-exporter-redesign.md](tasks/WP04-exporter-redesign.md)
**Requirement Refs**: FR-006, FR-007, NFR-004, C-004

### Included Subtasks

- [ ] T012 Rework the dialog so width, height, and codec are first-class
- [ ] T013 Replace coarse quality labels with a finer-grained slider and readout
- [ ] T014 Expose CPU, GPU, and Auto processor choices and show the selected backend clearly
- [ ] T015 Add exporter tests and documentation for quality and processor mapping

### Implementation Notes

- Map the new controls onto the current export backend first.
- If GPU processing is unavailable, fall back clearly and tell the user what
  happened.

### Parallel Opportunities

- T013 and T014 can progress in parallel once the control mapping is agreed.

### Dependencies

- Depends on WP01.

### Risks & Mitigations

- Risk: the UI looks better but hides the actual encode tradeoffs.
- Mitigation: keep the quality control interpretable at a glance and validate
  the backend mapping.

---

## Work Package 5 - MCP Pairing Bridge

**Goal**: Provide a local, inspectable pairing bridge for media and project state.
**Independent Test**: An agent can inspect local media and project state, then apply only confirmed writes.
**Prompt**: [WP05-mcp-pairing-bridge.md](tasks/WP05-mcp-pairing-bridge.md)
**Requirement Refs**: FR-009, NFR-003, NFR-004, C-005

### Included Subtasks

- [ ] T016 Define the minimal MCP resource surface for project and media data
- [ ] T017 Add local read-only inspection helpers for local image/video paths
- [ ] T018 Add safe write actions that only apply confirmed changes
- [ ] T019 Add tests and notes for local-first, confirmation-based behavior

### Implementation Notes

- Default to read-only.
- Keep the bridge local-first and explicit about every write.

### Parallel Opportunities

- T016 and T017 can overlap once the resource contract is fixed.

### Dependencies

- Depends on WP01, WP02, and WP04.

### Risks & Mitigations

- Risk: the bridge becomes a hidden remote control.
- Mitigation: keep it local, inspectable, and confirmation-based.

---

## Work Package 6 - QA, Docs, and Regression Hardening

**Goal**: Protect the workflow with regression coverage, docs, and migration notes.
**Independent Test**: The targeted tests pass, the docs build, and the new terms are used consistently.
**Prompt**: [WP06-qa-docs-and-regression-hardening.md](tasks/WP06-qa-docs-and-regression-hardening.md)
**Requirement Refs**: all FRs, NFR-001 through NFR-005, C-001 through C-005

### Included Subtasks

- [ ] T020 Add regression tests for the canvas, properties, reset, export, and keyframe flows
- [ ] T021 Update the user-facing docs to match the new UI language
- [ ] T022 Add a migration note for users who already rely on keyframes and look tools
- [ ] T023 Run the validation commands and capture Spec Kitty follow-ups in the bug note

### Implementation Notes

- Cover the user scenarios from the spec, not just the happy path.
- Make sure the docs describe scope clearly: clip, selection, or project.

### Parallel Opportunities

- T021 and T022 can proceed in parallel once the new terminology is settled.

### Dependencies

- Depends on all prior WPs.

### Risks & Mitigations

- Risk: the new UI is technically correct but still confusing.
- Mitigation: keep the user docs and migration note aligned with the control
  labels.

---

## Dependency & Execution Summary

- Sequence: WP01 -> WP02 -> WP03 -> WP04 -> WP05 -> WP06
- Parallelism is safest inside each WP after the shared contract is written.
- The MVP-shaping user pain is the project framing and static alignment flow,
  so WP02 should land early.

## Requirements Coverage Summary

| Requirement ID | Covered By Work Package(s) |
|----------------|----------------------------|
| FR-001 | WP01, WP02 |
| FR-002 | WP01, WP03 |
| FR-003 | WP01, WP03 |
| FR-004 | WP01, WP03 |
| FR-005 | WP01, WP02, WP03 |
| FR-006 | WP01, WP04 |
| FR-007 | WP01, WP04 |
| FR-008 | WP01, WP02, WP03 |
| FR-009 | WP01, WP05 |
| FR-010 | WP01, WP02 |
| NFR-001 | WP01, WP02 |
| NFR-002 | WP01, WP02, WP03 |
| NFR-003 | WP01, WP05 |
| NFR-004 | WP01, WP03, WP04, WP05 |
| NFR-005 | WP01, WP02, WP03, WP04, WP05, WP06 |
| C-001 | WP01, WP02 |
| C-002 | WP01, WP02 |
| C-003 | WP01, WP03 |
| C-004 | WP01, WP04 |
| C-005 | WP01, WP05 |

## Subtask Index (Reference)

| Subtask ID | Summary | Work Package | Priority | Parallel? |
|------------|---------|--------------|----------|-----------|
| T001 | Inventory current surfaces and note what already exists | WP01 | P0 | No |
| T002 | Freeze the boundary matrix for state ownership | WP01 | P0 | No |
| T003 | Capture rollout risks and validation checks | WP01 | P0 | No |
| T004 | Define project canvas behavior | WP02 | P0 | No |
| T005 | Add project-frame controls | WP02 | P0 | Yes |
| T006 | Make static alignment easy | WP02 | P0 | Yes |
| T007 | Add regression coverage for canvas/framing | WP02 | P0 | No |
| T008 | Group properties by category | WP03 | P0 | No |
| T009 | Surface color grading with clear scope | WP03 | P0 | Yes |
| T010 | Add `Reset Clip` | WP03 | P0 | No |
| T011 | Add tests/docs for properties and reset | WP03 | P0 | No |
| T012 | Rework size and codec controls | WP04 | P1 | No |
| T013 | Add a finer-grained quality slider | WP04 | P1 | Yes |
| T014 | Expose CPU/GPU/Auto processor choice | WP04 | P1 | Yes |
| T015 | Add exporter tests/docs | WP04 | P1 | No |
| T016 | Define MCP resource surface | WP05 | P2 | No |
| T017 | Add read-only local inspection helpers | WP05 | P2 | Yes |
| T018 | Add safe write actions | WP05 | P2 | No |
| T019 | Add bridge tests/notes | WP05 | P2 | No |
| T020 | Add regression tests for the workflow | WP06 | P1 | No |
| T021 | Update docs with the new language | WP06 | P1 | Yes |
| T022 | Write the migration note | WP06 | P1 | Yes |
| T023 | Run validation and capture follow-ups | WP06 | P1 | No |
