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

.. _creative_workflow_mission_breakdown_ref:

Creative Workflow Mission Breakdown
===================================

This is a Spec Kitty-style decomposition of the creative workflow work. It is
not a live mission file, but it uses the same shape: objective, work packages,
dependencies, risks, and exit criteria.

Mission objective
-----------------

Reduce the daily friction of experimental and AI-heavy editing by making
framing, properties, export, and pairing behavior feel like one coherent
workflow.

Mission boundary
----------------

Keep the existing Qt editor and the existing clip-level editing model. Improve
the abstraction layers around it instead of rewriting the entire application.

The app already has partial reset, color, keyframe, and export surfaces. WP-1
should inventory those seams before later work packages change their behavior.

Work packages
-------------

WP-1: Freeze the contracts
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
  CW-01 through CW-03.

Dependency
  None.

Goal
  Identify which state belongs to the project frame, which belongs to the clip,
  which belongs to the exporter, and which belongs to the agent surface while
  cataloging the current partial implementations.

Exit criteria
  The team can point at every important setting and say where it lives, and
  the current partial surfaces are documented well enough that later WPs do not
  reinterpret them by accident.

Risk
  If this step is skipped, later UX work will silently reclassify behavior
  instead of improving it.

WP-2: Make framing first-class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
  CW-04 through CW-07.

Dependency
  WP-1.

Goal
  Introduce a project canvas model that is visibly separate from clip-layer
  transforms.

Exit criteria
  Users can normalize inconsistent source framing without turning a static
  offset into keyframes.

Risk
  This is the most important model change in the whole plan. It should land
  before cosmetic work tries to paper over the problem.

WP-3: Organize properties by intent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
  CW-08 through CW-11.

Dependency
  WP-1, with strong benefit from WP-2.

Goal
  Replace the flat properties dump with categorized sections that match user
  intent and add ``Reset Clip`` as a safe recovery path.

Exit criteria
  Common controls are visible quickly, deep controls are still reachable, the
  dock no longer reads like an internal schema viewer, and the reset story is
  explicit about what clip state gets preserved.

Risk
  If categories are too broad, the panel will still feel noisy. If they are too
  narrow, the panel becomes a maze.

WP-4: Clarify export
^^^^^^^^^^^^^^^^^^^^

Scope
  CW-12 through CW-15.

Dependency
  WP-1.

Goal
  Make size, codec, quality, and CPU/GPU selection understandable without
  making the user decode preset names.

Exit criteria
  The exporter can answer the questions "how big", "what codec", "how much
  quality", and "where is the work happening" at a glance.

Risk
  UI changes should map to the existing export backend first, so the feature can
  land before any deeper encoder refactor.

WP-5: Add the pairing bridge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
  CW-16 through CW-19.

Dependency
  WP-1, WP-2, WP-4.

Goal
  Let a local agent inspect media, summarize relevant frames, and apply
  confirmed project changes safely.

Exit criteria
  A user can drop in a local path, discuss the framing/export implications, and
  have the agent act on the same project state.

Risk
  The bridge must remain local-first and conservative by default. Write actions
  should never be implicit.

WP-6: Harden and explain
^^^^^^^^^^^^^^^^^^^^^^^^

Scope
  CW-20 through CW-23.

Dependency
  All prior work packages.

Goal
  Make the workflow testable, documented, and understandable to users who are
  already used to the existing clip-centric model.

Exit criteria
  The new workflow has examples, regression coverage, and a migration note.

Risk
  If this is rushed, the new controls will feel like hidden expert features
  instead of an intentional product direction.

Review gates
------------

1. Do not silently change the meaning of existing clip controls.
2. Keep the project frame and the clip transform separate.
3. Favor reversible actions and explicit resets.
4. Keep the MCP bridge local and confirmation-based.
5. Preserve the current behavior for users who do not opt into the new flow.

Tradeoffs
---------

- The fastest way to land value is to change the UI before changing the backend.
- The most important user pain is framing alignment, so that work should come
  before exporter polish.
- The most future-proof step is the contract freeze, because every later page
  depends on it.
- The safest agent surface is read-first, write-second, local-only throughout.

This breakdown should be enough to turn the plan into a real implementation
sequence without losing the shape of the product.
