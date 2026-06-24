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

.. _creative_workflow_issues_ref:

Creative Workflow Issues
========================

This page turns the task decomposition into a suggested backlog of issues with
priority and dependencies. The titles below are written as if they will become
GitHub issues later.

.. list-table::
   :widths: 10 40 22 28
   :header-rows: 1

   * - Priority
     - Suggested issue title
     - Depends on
     - Maps to
   * - P0
     - Inventory the current timeline, properties, export, keyframe, and color surfaces
     - None
     - CW-01
   * - P0
     - Freeze the project canvas, clip, export, and MCP state boundaries
     - Inventory issue above
     - CW-02
   * - P0
     - Decide which current actions stay clip-local and which become canvas-level
     - State boundaries issue
     - CW-03
   * - P0
     - Introduce a first-class project canvas and framing model
     - State boundaries issue
     - CW-04, CW-05
   * - P0
     - Allow static alignment fixes without forcing keyframes
     - Canvas/framing issue
     - CW-06, CW-07
   * - P1
     - Group clip and effect properties by intent
     - State boundaries issue, canvas/framing issue
     - CW-08
   * - P1
     - Add property section collapse, ``Reset Clip``, and color-scope labels
     - Properties grouping issue
     - CW-09, CW-10, CW-11
   * - P1
     - Redesign the export dialog around size, codec, quality, and processor
     - State boundaries issue
     - CW-12, CW-13
   * - P1
     - Expose CPU, GPU, and Auto processor selection clearly
     - Export dialog redesign issue
     - CW-14, CW-15
   * - P2
     - Define the MCP resource surface for project and media inspection
     - State boundaries issue, canvas/framing issue
     - CW-16
   * - P2
     - Add read-only local media inspection tools for pairing
     - MCP resource surface issue
     - CW-17
   * - P2
     - Add safe write actions that apply confirmed changes
     - Read-only MCP issue
     - CW-18, CW-19
   * - P1
     - Add regression coverage for canvas, properties, and export flows
     - Feature issues above
     - CW-20
   * - P1
     - Write the migration note and workflow examples
     - Feature issues above
     - CW-21, CW-22, CW-23

Priority guide
--------------

- ``P0``: blocks the product shape or changes the core mental model.
- ``P1``: delivers important user value once the core model exists.
- ``P2``: improves the pairing surface and can follow after the UI model is
  stable.

Dependency guide
-----------------

- Anything that changes the meaning of clip or canvas state depends on the
  contract issues first.
- Properties work depends on the new frame model being understood.
- Export work can proceed after the export state boundaries are defined.
- MCP work should wait until the local project state is stable enough to read
  and mutate safely.

This backlog is intentionally sequential at the top and more flexible toward
the end.
