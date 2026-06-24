# Spec Kitty Bug Notes

These are the issues worth sending to Robert while we are working through the
mission.

## 1. Global launcher fails to start

- Repro: run `spec-kitty upgrade --agent-check --json`
- Result: `ModuleNotFoundError: No module named 'tomli_w'`
- Impact: the global launcher cannot start, so the project-local runtime is the
  reliable path for mission commands.
- Workaround: use `uv run --project /home/lynn/projects/spec-kitty python -m specify_cli ...`

## 2. Finalize-tasks collided with an already-checked-out branch

- Repro: attempt mission finalization when the coordination branch is already
  checked out in the repo root.
- Result: the worktree creation step fails unless the coordination workspace is
  allowed to force-add the branch.
- Impact: mission finalization gets blocked before the lane worktree exists.
- Status: fixed locally in the Spec Kitty checkout by allowing the coordination
  workspace to use `git worktree add --force` in that collision case.

## 3. Setup verification reported stale lane and skill state

- Repro: run the Spec Kitty setup verification flow after the launcher issue.
- Result: `lanes.json` and managed skill metadata can show as corrupt or out of
  sync.
- Impact: the tooling can look unhealthy even when the underlying mission docs
  are fine.
- Note: treat this as generated-state hygiene, not an OpenShot product bug.

