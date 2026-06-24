# Spec Kitty Notes for Robert

## Observed issue 1: Global launcher path fails on `tomli_w`

While checking the updated Spec Kitty install, the machine-wide launcher at
`/home/lynn/.local/bin/spec-kitty` failed with:

- `ModuleNotFoundError: No module named 'tomli_w'`

The same environment could import `tomli_w` from the updated Spec Kitty repo
venv, which suggests the launcher is resolving a stale or mismatched Python
environment instead of the repo-local one.

## Observed issue 2: `verify-setup` reports corrupt lane metadata

`uv run spec-kitty verify-setup` completed, but it warned about:

- a corrupt `lanes.json` entry in `064-complete-mission-identity-cutover`
- managed skill drift / missing files in the generated `.agents` and `.claude`
  surfaces

That may be expected cleanup drift, but it is worth a look if the runtime is
supposed to be fully self-healing after a version refresh.

## Observed issue 3: `finalize-tasks` fails when the coordination branch is already checked out

The dry-run validator passed, but the real `finalize-tasks` command failed when
it tried to create a coordination worktree for `kitty/mission-creative-workflow-control-surface-01KVTEXD`.
The error was:

- `git worktree add /home/lynn/projects/openshot-qt/.worktrees/creative-workflow-control-surface-01KVTEXD-coord kitty/mission-creative-workflow-control-surface-01KVTEXD`
- exit status `128`

This looks like a topology mismatch: the branch is already checked out in the
root worktree, so the task finalizer cannot create a second worktree for the
same branch. The validator should probably detect that state and either reuse
the existing checkout or emit a clearer instruction before attempting `git
worktree add`.
