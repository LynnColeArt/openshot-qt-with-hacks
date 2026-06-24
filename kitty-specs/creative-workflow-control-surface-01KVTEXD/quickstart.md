# Creative Workflow Quickstart

This WP is documentation and contract freezing only. There are no product code
tests to run here. The goal is to make sure the mission artifacts stay aligned
with the current repository reality.

## Read First

Before changing anything else, read these files together:

- `spec.md`
- `plan.md`
- `research.md`
- `data-model.md`
- `doc/creative_workflow_vision.rst`
- `doc/creative_workflow_plan.rst`
- `doc/creative_workflow_tasks.rst`

If those files use different terminology for the same concept, stop and fix
the wording before moving on.

## Mission Sanity Checks

1. Confirm that the current code inventory matches the research notes.
2. Confirm that the boundary matrix distinguishes project canvas state from
   clip state.
3. Confirm that `Reset Clip` is described as preserving timing and crop.
4. Confirm that export quality is described as a real tradeoff, not only as
   `Low`, `Med`, or `High`.
5. Confirm that the MCP surface is local-first and confirmation-based.

## Useful Commands

These commands are helpful when refreshing the inventory or checking that the
mission artifacts still resolve correctly.

```bash
uv run --project /home/lynn/projects/spec-kitty python -m specify_cli agent context resolve --action tasks --mission creative-workflow-control-surface-01KVTEXD --json
```

```bash
uv run --project /home/lynn/projects/spec-kitty python -m specify_cli agent mission check-prerequisites --json --paths-only --include-tasks --mission creative-workflow-control-surface-01KVTEXD
```

```bash
rg -n "No_Transform_Triggered|Reset_Look_Triggered|Adjust_Colors_Triggered" src/windows/views/timeline.py
rg -n "colorgrade_curve|colorgrade_wheels|Reset_Color_Grade_Action_Triggered" src/windows/views/properties_tableview.py
rg -n "calculate_all_formats_bitrate|cboSimpleQuality|txtWidth|txtHeight" src/windows/export.py
```

## Scenario Validation

- A user should be able to see that the app already has partial reset and
  color-grade support.
- A future `Reset Clip` action should not be mistaken for `No Transform` or
  `Reset Look`.
- The plan should make it obvious which settings are clip-local and which ones
  are project-level.
- The exporter discussion should stay focused on width, height, codec,
  quality, and processor choice.

## Tooling Note

The global `spec-kitty` launcher in this environment still errors on missing
`tomli_w`. Use the project-local runtime shown above when you need a reliable
command path.

