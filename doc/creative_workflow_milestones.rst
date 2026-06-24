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

.. _creative_workflow_milestones_ref:

Creative Workflow Milestones
============================

This page turns :ref:`creative_workflow_plan_ref` into a compact milestone
table. The estimates are sequencing aids, not commitments.

.. list-table::
   :widths: 12 26 22 14 26
   :header-rows: 1

   * - Milestone
     - Focus
     - Depends on
     - Rough size
     - Exit criteria
   * - M1
     - Discovery and contracts
     - None
     - Small
     - State boundaries are written down and reviewed.
   * - M2
     - Framing and canvas
     - M1
     - Large
     - The project frame can be changed without collapsing clip-level edits.
   * - M3
     - Properties by intent
     - M1, M2
     - Medium
     - Common controls are grouped and the noisy fields are no longer flat.
   * - M4
     - Exporter redesign
     - M1
     - Medium
     - Width, height, codec, quality, and processor are obvious at a glance.
   * - M5
     - MCP pairing bridge
     - M1, M2, M4
     - Medium
     - The agent can inspect local project state and apply confirmed changes.
   * - M6
     - QA and documentation
     - M2, M3, M4, M5
     - Small
     - The new workflow is documented, testable, and migration-aware.

How to read this table
----------------------

- ``Small`` means one focused pass with limited surface area.
- ``Medium`` means a work package that probably needs implementation plus review.
- ``Large`` means the work changes a core mental model and should land before
  the more polished UX work that depends on it.

Suggested overlap
-----------------

- M3 can start once the property boundaries are known, even if M2 is still in
  flight.
- M4 is largely independent of the framing work, as long as the export model is
  kept honest.
- M5 should wait for the main data boundaries so the bridge can stay local and
  safe.
- M6 should be last so the docs describe the final workflow rather than the
  interim one.

The main sequencing idea is simple: solve the frame first, then tidy the
controls around it, then expose the workflow to pairing and documentation.
