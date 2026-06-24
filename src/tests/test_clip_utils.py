"""
 @file
 @brief Unit tests for clip utility helpers
 @author Jonathan Thomas <jonathan@openshot.org>

 @section LICENSE

 Copyright (c) 2008-2026 OpenShot Studios, LLC
 (http://www.openshotstudios.com). This file is part of
 OpenShot Video Editor (http://www.openshot.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.

 OpenShot Video Editor is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with OpenShot Library.  If not, see <http://www.gnu.org/licenses/>.
 """

import os
import sys
import unittest

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

import openshot  # noqa: E402
from classes.clip_utils import reset_clip_data  # noqa: E402


class ClipUtilsTests(unittest.TestCase):
    def test_reset_clip_data_preserves_timing_and_crop_but_clears_other_state(self):
        clip = {
            "id": "clip-1",
            "position": 12.0,
            "start": 3.0,
            "end": 9.0,
            "duration": 6.0,
            "scale": openshot.SCALE_CROP,
            "gravity": openshot.GRAVITY_TOP_LEFT,
            "effects": [
                {"class_name": "Crop", "left": 0.1, "top": 0.2},
                {"class_name": "Blur", "horizontal_radius": {"Points": []}},
                {"class_name": "Mask", "brightness": {"Points": []}},
            ],
            "alpha": {"Points": [{"co": {"X": 1.0, "Y": 0.25}, "interpolation": openshot.LINEAR}]},
            "scale_x": {"Points": [{"co": {"X": 1.0, "Y": 2.0}, "interpolation": openshot.LINEAR}]},
            "scale_y": {"Points": [{"co": {"X": 1.0, "Y": 0.5}, "interpolation": openshot.LINEAR}]},
            "location_x": {"Points": [{"co": {"X": 1.0, "Y": 10.0}, "interpolation": openshot.LINEAR}]},
            "location_y": {"Points": [{"co": {"X": 1.0, "Y": -7.0}, "interpolation": openshot.LINEAR}]},
            "rotation": {"Points": [{"co": {"X": 1.0, "Y": 33.0}, "interpolation": openshot.LINEAR}]},
            "shear_x": {"Points": [{"co": {"X": 1.0, "Y": 0.4}, "interpolation": openshot.LINEAR}]},
            "shear_y": {"Points": [{"co": {"X": 1.0, "Y": -0.4}, "interpolation": openshot.LINEAR}]},
            "origin_x": {"Points": [{"co": {"X": 1.0, "Y": 0.2}, "interpolation": openshot.LINEAR}]},
            "origin_y": {"Points": [{"co": {"X": 1.0, "Y": 0.8}, "interpolation": openshot.LINEAR}]},
            "time": {"Points": [{"co": {"X": 1.0, "Y": 2.0}, "interpolation": openshot.LINEAR}]},
            "volume": {"Points": [{"co": {"X": 1.0, "Y": 0.25}, "interpolation": openshot.LINEAR}]},
            "has_audio": {"Points": [{"co": {"X": 1.0, "Y": 0.0}, "interpolation": openshot.LINEAR}]},
            "has_video": {"Points": [{"co": {"X": 1.0, "Y": 0.0}, "interpolation": openshot.LINEAR}]},
            "channel_filter": {"Points": [{"co": {"X": 1.0, "Y": 2.0}, "interpolation": openshot.LINEAR}]},
            "channel_mapping": {"Points": [{"co": {"X": 1.0, "Y": 3.0}, "interpolation": openshot.LINEAR}]},
            "ui": {"audio_data": [1, 2, 3]},
        }

        changed = reset_clip_data(clip)

        self.assertTrue(changed)
        self.assertEqual(clip["position"], 12.0)
        self.assertEqual(clip["start"], 3.0)
        self.assertEqual(clip["end"], 9.0)
        self.assertEqual(clip["duration"], 6.0)
        self.assertEqual(clip["scale"], openshot.SCALE_FIT)
        self.assertEqual(clip["gravity"], openshot.GRAVITY_CENTER)
        self.assertEqual([effect["class_name"] for effect in clip["effects"]], ["Crop"])
        self.assertEqual(clip["alpha"]["Points"][0]["co"]["Y"], 1.0)
        self.assertEqual(clip["scale_x"]["Points"][0]["co"]["Y"], 1.0)
        self.assertEqual(clip["scale_y"]["Points"][0]["co"]["Y"], 1.0)
        self.assertEqual(clip["location_x"]["Points"][0]["co"]["Y"], 0.0)
        self.assertEqual(clip["location_y"]["Points"][0]["co"]["Y"], 0.0)
        self.assertEqual(clip["rotation"]["Points"][0]["co"]["Y"], 0.0)
        self.assertEqual(clip["shear_x"]["Points"][0]["co"]["Y"], 0.0)
        self.assertEqual(clip["shear_y"]["Points"][0]["co"]["Y"], 0.0)
        self.assertEqual(clip["origin_x"]["Points"][0]["co"]["Y"], 0.5)
        self.assertEqual(clip["origin_y"]["Points"][0]["co"]["Y"], 0.5)
        self.assertEqual(clip["time"]["Points"][0]["co"]["Y"], 1.0)
        self.assertEqual(clip["volume"]["Points"][0]["co"]["Y"], 1.0)
        self.assertEqual(clip["has_audio"]["Points"][0]["co"]["Y"], -1.0)
        self.assertEqual(clip["has_video"]["Points"][0]["co"]["Y"], -1.0)
        self.assertEqual(clip["channel_filter"]["Points"][0]["co"]["Y"], -1.0)
        self.assertEqual(clip["channel_mapping"]["Points"][0]["co"]["Y"], -1.0)
        self.assertEqual(clip["ui"]["audio_data"], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
