.. Copyright (c) 2008-2026 OpenShot Studios, LLC
 (http://www.openshotstudios.com). This file is part of
 OpenShot Video Editor (http://www.openshot.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.

.. OpenShot Video Editor is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

.. OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

.. You should have received a copy of the GNU General Public License
 along with OpenShot Library.  If not, see <http://www.gnu.org/licenses/>.

.. _creative_workflow_plan_ref:

Creative Workflow Plan
======================

This page turns :ref:`creative_workflow_vision_ref` into a staged roadmap.
The goal is to reduce daily friction for experimental and AI-heavy film work
without forcing a rewrite of the entire application.

Scope
-----

The plan is intentionally narrow:

- keep the current Qt editor,
- preserve existing clip-level editing behavior,
- introduce a stronger framing model around the project canvas,
- simplify the properties dock by grouping controls by intent,
- redesign export controls so size, codec, quality, and processor are obvious,
- and add a local pairing surface through MCP.

Non-goals
---------

This plan does not assume:

- a full language port,
- a new rendering engine,
- removal of current clip transforms,
- or a simultaneous redesign of every dialog in the app.

The first pass should make the current workflow less awkward while keeping the
underlying model close to what already works.

Guiding principles
------------------

1. Separate static alignment from animated motion.
2. Keep project framing distinct from clip transforms.
3. Hide complexity until the user asks for it.
4. Prefer reversible changes and explicit resets.
5. Keep the agent local and inspectable.

Roadmap
-------

Phase 1: Discovery and contracts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step is to map the current behavior and define boundaries.

Deliverables
  A clear contract for project canvas, clip framing, properties grouping,
  exporter settings, and MCP integration points.

Outcome
  The team knows which state belongs to the project, which state belongs to a
  clip, and which state belongs to an export preset or agent action.

Phase 2: Framing and canvas
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This phase introduces a first-class canvas or framing object that is separate
from clip geometry.

Deliverables
  Canvas resize behavior, aspect-ratio handling, anchor/fill/fit controls, and
  a visible distinction between project frame and clip layout.

Outcome
  Users can normalize AI-generated sources to the same frame without turning
  every correction into a keyframe animation.

Phase 3: Properties by intent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The properties dock should become a categorized inspector instead of a flat
schema view.

Deliverables
  Grouped sections, sensible defaults, section reset controls, search, and a
  better advanced-mode story.

Outcome
  Common editing actions become faster, and the deep settings stay available
  without dominating the UI.

Phase 4: Exporter redesign
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The exporter should expose the decisions people actually care about.

Deliverables
  Width and height, codec choice, a real quality slider, CPU/GPU/Auto
  selection, and clearer feedback about hardware acceleration.

Outcome
  The user can judge output size and fidelity at a glance instead of decoding
  a preset name.

Phase 5: MCP pairing bridge
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A local MCP bridge can make the editor easier to pair with.

Deliverables
  Read-only project and media inspection, representative frame sampling, safe
  write actions, and confirmation before changes are applied.

Outcome
  An agent can inspect local media, discuss framing or export choices, and help
  apply edits against real project state.

Phase 6: QA and documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The final phase is about hardening and explaining the new workflow.

Deliverables
  Regression checks, sample workflows, updated docs, and a migration note for
  users who already rely on the current clip-centric tools.

Outcome
  The new workflow feels intentional rather than bolted on.

Suggested release order
-----------------------

1. Phase 1 gives the contract.
2. Phase 2 solves the daily alignment pain.
3. Phase 3 reduces property clutter.
4. Phase 4 improves export confidence.
5. Phase 5 adds the pairing bridge.
6. Phase 6 makes the whole thing sustainable.

That order keeps the highest-friction user problem in front while leaving room
for the later workflow improvements to land cleanly.

See also
--------

- :ref:`creative_workflow_milestones_ref`
- :ref:`creative_workflow_mission_breakdown_ref`
- :ref:`creative_workflow_issues_ref`
