import os
import unittest
from maxpatcher.vibe import Patcher
from maxpylang.maxobject import MaxObject

class TestVibePatcher(unittest.TestCase):
    """Tests for the vibe.Patcher class."""

    def test_patcher_initialization(self):
        """Test that Patcher initializes with an underlying MaxPatch."""
        p = Patcher()
        self.assertIsNotNone(p.engine_patch)

    def test_patcher_add_object(self):
        """Test that adding an object works and increments the count."""
        p = Patcher()
        obj = p.add("cycle~ 440")
        self.assertIsInstance(obj, MaxObject)
        self.assertEqual(obj.name, "cycle~")
        # Internal _objs dict in MaxPatch should have one entry
        self.assertEqual(len(p.engine_patch._objs), 1)

    def test_patcher_link(self):
        """Test that linking two objects works and creates a patchcord."""
        p = Patcher()
        osc = p.add("cycle~ 440")
        amp = p.add("gain~")
        p.link(osc, amp)
        
        # Check if a connection exists in the underlying patch
        # MaxPyLang stores patchcords in the JSON dict when get_json() is called
        lines = p.engine_patch.dict['patcher']['lines']
        self.assertEqual(len(lines), 1)

    def test_patcher_save(self):
        """Test that saving the patch creates a file."""
        p = Patcher()
        p.add("bang")
        save_path = "tests/test_save.maxpat"
        p.save(save_path)
        self.assertTrue(os.path.exists(save_path))
        # Cleanup
        if os.path.exists(save_path):
            os.remove(save_path)

    def test_auto_layout_grid_placement(self):
        """
        Test that objects are automatically placed in a grid-like fashion,
        checking for horizontal progression and vertical wrapping.
        """
        p = Patcher()
        # Add enough objects to ensure wrapping occurs on a typical Max patcher canvas
        # Default canvas width from empty_template.json is approx 1300, grid spacing 80
        # 1300 / 80 = ~16 objects per row
        num_objects = 20
        objs = []
        for i in range(num_objects):
            # Using a generic object like "float" that is relatively small
            objs.append(p.add(f"float {i}")) 
        
        # Check positions of first few objects to ensure horizontal progression
        # Note: MaxPyLang's place_grid starts at x_space, then increments.
        # So first object is at [x_space, y_space]
        first_obj_pos = objs[0]._dict["box"]["patching_rect"][:2]
        second_obj_pos = objs[1]._dict["box"]["patching_rect"][:2]
        
        # Assert horizontal progression
        self.assertGreater(second_obj_pos[0], first_obj_pos[0])
        self.assertEqual(second_obj_pos[1], first_obj_pos[1]) # Should be on the same row
        
        # Check for vertical wrapping (e.g., object 17 should be on a new row)
        # Assuming grid spacing of 80x80 (default)
        # First row roughly 16 objects. So 17th object should be on a new row.
        obj_index_that_wraps = 16 # (0-indexed 16th object means 17th actual object)
        obj_before_wrap_pos = objs[obj_index_that_wraps - 1]._dict["box"]["patching_rect"][:2]
        obj_after_wrap_pos = objs[obj_index_that_wraps]._dict["box"]["patching_rect"][:2]
        
        self.assertLess(obj_after_wrap_pos[0], obj_before_wrap_pos[0]) # X should be smaller, implying reset
        self.assertGreater(obj_after_wrap_pos[1], obj_before_wrap_pos[1]) # Y should be greater, implying new row
        
        # Also ensure the first object starts at a reasonable position (not 0,0)
        self.assertGreater(first_obj_pos[0], 0)
        self.assertGreater(first_obj_pos[1], 0)


if __name__ == "__main__":
    unittest.main()
