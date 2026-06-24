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

.. _creative_workflow_vision_ref:

Creative Workflow Vision
========================

This note captures a recurring workflow problem for experimental and AI-heavy
film projects: the editor needs to help normalize source media, frame it
consistently, and export it with less friction. It is a working direction note,
not a commitment that every item here is already implemented.

Why this matters
-----------------

OpenShot already fills an important gap for Linux users: it is the most
capable free editor in a space that still leaves many creative workflows behind.
For art films, experimental music videos, and AI-assisted montage work, the
main pain point is not basic trimming. The pain point is source alignment.

Different generators and tools do not always agree on what ``16:9`` means.
They are close, but not identical. That creates a daily manual correction loop:

- some clips need a small vertical shift,
- some need a crop to line up with neighboring sources,
- some need a static scale or anchor correction,
- and some need a start and end keyframe pair just to fake a fixed offset.

That last case is the important clue. When a clip is only wrong by a constant
offset, keyframes are the wrong abstraction. The editor is forcing a static
framing problem through an animation tool.

What already works well
-----------------------

OpenShot already has some strong building blocks:

- clip resize and crop controls are quick and direct,
- the timeline supports visual clip manipulation,
- existing property editing already exposes keyframe-driven control,
- the color tools are richer than many free editors,
- and the application already has an experimental AI workflow surface.

Those strengths are worth preserving. The goal is not to replace them. The goal
is to separate concerns so the editor can handle framing, animation, export, and
AI-assisted pairing without making every problem look the same.

Current partial support
^^^^^^^^^^^^^^^^^^^^^^^

The repository already has several partial surfaces that should be treated as
reuse points instead of being redesigned from scratch:

- the timeline menu already exposes ``No Transform``, ``Reset Layout``,
  ``Reset Look``, color presets, and ``Adjust Colors``,
- the properties dock already special-cases ``colorgrade_curve`` and
  ``colorgrade_wheels``,
- the color-grade editor already provides scoped wheels rows plus reset and
  enable controls,
- the keyframe UI already supports drag, delete, interpolation, and nested
  color-grade keyframes,
- and the exporter already has width, height, codec, quality, and backend
  detection plumbing.

These are partial surfaces, not the final abstraction, but they prove the app
already has the right seams in place.

The missing abstractions
------------------------

Framing and canvas
^^^^^^^^^^^^^^^^^^^

The editor needs a first-class notion of the canvas or project frame that is
separate from individual clip transforms.

That would let the user:

- change aspect ratio by dragging the canvas boundary,
- expand the canvas while preserving aspect ratio,
- keep clip-layer transforms independent from project framing,
- and apply reusable framing presets to groups of clips.

For this workflow, ``Framing`` is a better mental model than ``Resize``. Resize
sounds geometric. Framing sounds compositional.

Properties by category
^^^^^^^^^^^^^^^^^^^^^^

The properties dock should not read like a raw schema dump.

The user also wants a right-click ``Reset Clip`` action that clears clip-
assigned state without changing timing or crop.

Most users will never touch most fields, so the panel should be organized around
intent:

- Common
- Framing
- Color
- Motion
- Audio
- Effects
- Advanced

The key rules are:

- show only sections relevant to the selected object,
- collapse the noisy sections by default,
- keep the common controls visible and fast,
- and allow advanced fields to stay available without dominating the UI.

Exporter controls
^^^^^^^^^^^^^^^^^

The exporter should make the important decisions obvious at a glance.

The controls that matter most are:

- output width and height,
- codec,
- quality as a real slider instead of low/medium/high labels,
- and processor selection between CPU, GPU, and Auto.

The quality control should communicate an actual tradeoff, not just a preset
name. The user should be able to see whether they are getting smaller files,
better fidelity, or a compromise in between.

GPU selection should also be explicit. If a hardware encoder is available, the
user should know what it is. If not, the UI should say so clearly and fall back
gracefully.

MCP pairing bridge
^^^^^^^^^^^^^^^^^^

A local Model Context Protocol bridge could make this workflow much easier to
pair on.

The useful path is simple:

- drop in an image or video path,
- let the agent inspect metadata and representative frames,
- discuss framing or export changes with the agent,
- and apply changes only after confirmation.

That means the agent can help with real project state instead of only giving
advice. For this kind of work, the best MCP surface would expose:

- selected media metadata,
- project canvas and export settings,
- clip framing and property data,
- and a small set of safe write actions.

Guiding rules
-------------

1. Keep clip transforms and project framing distinct.
2. Make static alignment fixes static whenever possible.
3. Use keyframes when the content actually changes over time.
4. Reduce property clutter by grouping by intent.
5. Show export cost and quality more clearly.
6. Default to local, inspectable, reversible operations.

What success looks like
-----------------------

This workflow feels successful when the user can:

- drop in AI-generated clips from several sources,
- normalize them to the same frame without wrestling the timeline,
- make a handful of human-readable adjustments in a categorized properties
  panel,
- export with a clear understanding of size, codec, quality, and processor,
- and discuss changes with an agent that can see the same local project state.

That is the product shape this note is trying to preserve.

See also
--------

- :ref:`creative_workflow_milestones_ref`
- :ref:`creative_workflow_mission_breakdown_ref`
- :ref:`creative_workflow_issues_ref`
- :ref:`creative_workflow_plan_ref`
- :ref:`creative_workflow_tasks_ref`
