# Quickstart: Creative Workflow Control Surface

## Validation scenarios

### 1. Normalize mismatched AI-generated clips

1. Open a project with several clips that are nearly aligned but not identical.
2. Use the project canvas/framing controls instead of keyframing every clip.
3. Confirm the common frame is visible and reversible.

### 2. Find and edit effects without hunting

1. Select a clip with effects attached.
2. Open the properties dock.
3. Confirm the categories are organized by intent and that advanced controls do
   not dominate the panel.

### 3. Reset a clip without losing timing

1. Right-click a clip.
2. Choose `Reset Clip`.
3. Confirm clip effects and keyframes are removed while timing and crop remain.

### 4. Export with clearer tradeoffs

1. Open the exporter.
2. Confirm width, height, codec, quality, and processor are visible.
3. Confirm the quality control feels like a fine-grained slider rather than a
   low/medium/high preset.

### 5. Pair locally with an agent

1. Provide a local image or video path.
2. Inspect the file and project state through the pairing surface.
3. Confirm that any write action is explicit and confirmed.

## Repository validation commands

```bash
python3 -m unittest discover -s src/tests -t src/tests --quiet
cd doc && make html
```
