"""
 @file
 @brief Unit tests for properties table grouping helpers
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
from collections import OrderedDict

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from windows.views.properties_tableview import (  # noqa: E402
    color_grade_scope_label,
    color_grade_scope_title,
    group_properties_by_intent,
    property_section_for,
    property_section_metadata,
)


class PropertiesTableViewTests(unittest.TestCase):
    def test_property_section_for_uses_creator_friendly_grouping(self):
        self.assertEqual(property_section_for("start", {"type": "float"}, "clip"), "Timing")
        self.assertEqual(property_section_for("scale_x", {"type": "float"}, "clip"), "Transform")
        self.assertEqual(property_section_for("colorgrade_curve", {"type": "colorgrade_curve"}, "clip"), "Color")
        self.assertEqual(property_section_for("volume", {"type": "float"}, "clip"), "Audio")
        self.assertEqual(property_section_for("reader", {"type": "reader"}, "clip"), "Source")
        self.assertEqual(property_section_for("left", {"type": "float"}, "effect"), "Effects")
        self.assertEqual(property_section_for("custom", {"type": "string"}, "clip"), "Advanced")

    def test_group_properties_by_intent_keeps_common_sections_first(self):
        properties = OrderedDict([
            ("custom", {"name": "Custom", "type": "string"}),
            ("start", {"name": "Start", "type": "float"}),
            ("scale_x", {"name": "Scale X", "type": "float"}),
            ("volume", {"name": "Volume", "type": "float"}),
            ("colorgrade_curve", {"name": "Color", "type": "colorgrade_curve"}),
            ("reader", {"name": "Reader", "type": "reader"}),
            ("left", {"name": "Left", "type": "float"}),
        ])

        grouped = group_properties_by_intent(properties, "effect")

        self.assertEqual(list(grouped.keys()), [
            "Timing",
            "Transform",
            "Color",
            "Audio",
            "Effects",
            "Source",
            "Advanced",
        ])
        self.assertEqual([key for key, _prop in grouped["Timing"]], ["start"])
        self.assertEqual([key for key, _prop in grouped["Transform"]], ["scale_x"])
        self.assertEqual([key for key, _prop in grouped["Color"]], ["colorgrade_curve"])
        self.assertEqual([key for key, _prop in grouped["Audio"]], ["volume"])
        self.assertEqual([key for key, _prop in grouped["Effects"]], ["left"])
        self.assertEqual([key for key, _prop in grouped["Source"]], ["reader"])
        self.assertEqual([key for key, _prop in grouped["Advanced"]], ["custom"])

    def test_property_section_metadata_marks_advanced_collapsed_by_default(self):
        self.assertFalse(property_section_metadata("Timing")["collapsed"])
        self.assertTrue(property_section_metadata("Advanced")["collapsed"])

    def test_color_grade_scope_label_reflects_selection_size(self):
        self.assertEqual(color_grade_scope_label([]), "Timeline")
        self.assertEqual(color_grade_scope_label([1]), "Clip")
        self.assertEqual(color_grade_scope_label([1, 2]), "Selection")

    def test_color_grade_scope_title_includes_the_edit_scope(self):
        self.assertEqual(color_grade_scope_title("Color Wheels", []), "Color Wheels - Timeline")
        self.assertEqual(color_grade_scope_title("Color Wheels", [1]), "Color Wheels - Clip")


if __name__ == "__main__":
    unittest.main()
