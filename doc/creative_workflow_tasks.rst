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

.. _creative_workflow_tasks_ref:

Creative Workflow Tasks
=======================

This task list decomposes the roadmap in :ref:`creative_workflow_plan_ref`
into work packages that can be implemented and reviewed one at a time.

Foundation
----------

CW-01
  Inventory the current clip transform, properties, export, and AI code paths
  so the new workflow can reuse what already exists instead of guessing at the
  right seams.

CW-02
  Write down the data boundaries for project canvas state, clip framing state,
  export preset state, and MCP state.

CW-03
  Identify which current actions should remain clip-local, which should move to
  canvas-level controls, and which should remain advanced-only.

Framing and canvas
------------------

CW-04
  Design the project canvas model and the corresponding UI controls for aspect
  ratio, canvas size, and framing presets.

CW-05
  Add a visible separation between canvas adjustments and clip-layer
  transforms so the user can normalize the project frame without rewriting the
  clip itself.

CW-06
  Define the fit, fill, anchor, and preserve-layout behaviors for clips inside
  the canvas.

CW-07
  Make sure static offset corrections can be applied without creating
  unnecessary keyframes.

Properties dock
---------------

CW-08
  Group clip and effect properties into human categories such as Common,
  Framing, Color, Motion, Audio, Effects, and Advanced.

CW-09
  Collapse low-use sections by default and add a path for quickly surfacing
  favorite properties.

CW-10
  Add section-level reset actions so users can undo a category without clearing
  the entire clip.

CW-11
  Keep the advanced property view available for edge cases, but hide it behind
  an explicit choice.

Exporter
--------

CW-12
  Rework the export dialog so width, height, codec, and quality are obvious
  first-class controls instead of buried decisions.

CW-13
  Replace the coarse quality labels with a slider or equivalent control that
  gives a better sense of the compression tradeoff.

CW-14
  Expose CPU, GPU, and Auto processor choices clearly and show the selected
  hardware backend when one is available.

CW-15
  Map the new export controls onto the existing export backend so the feature
  lands as a UI and workflow improvement before it becomes a backend rewrite.

MCP bridge
----------

CW-16
  Define a minimal MCP resource set for project state, selected media metadata,
  representative frames, and export settings.

CW-17
  Add read-only tools that let an agent inspect a local image or video path and
  summarize what is relevant for framing or export decisions.

CW-18
  Add safe write tools that apply confirmed project changes without requiring
  the agent to edit the project file directly.

CW-19
  Make the bridge local-first and explicit about any operation that changes the
  project.

QA and docs
-----------

CW-20
  Add regression coverage for the new canvas, properties, and export flows.

CW-21
  Capture before-and-after examples for the workflows that motivated the work,
  especially the AI source alignment case.

CW-22
  Update the user guide so the new abstractions are described in the same terms
  the UI uses.

CW-23
  Add a short migration note that explains what changed for users who already
  rely on clip keyframes and the existing transform actions.

Suggested execution order
-------------------------

1. Finish CW-01 through CW-03 so the boundaries are clear.
2. Land CW-04 through CW-07 so the framing problem is solved first.
3. Land CW-08 through CW-11 so the properties panel stops fighting the user.
4. Land CW-12 through CW-15 so export becomes understandable again.
5. Land CW-16 through CW-19 to give the agent a real local surface.
6. Finish CW-20 through CW-23 so the new workflow is testable and documented.

Parallelism is possible inside each group, but the groups should stay in this
order because later work depends on the earlier contracts.
