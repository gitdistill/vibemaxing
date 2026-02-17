import unittest
import os
import json
import shutil
import sys

# Add maxpatcher to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from maxpatcher import core

class TestValidator(unittest.TestCase):
    project_name = "validator_test_project"
    project_dir = os.path.join("projects", project_name)

    def setUp(self):
        if os.path.exists(self.project_dir):
            shutil.rmtree(self.project_dir)
        core.create_project(self.project_name)

    def tearDown(self):
        if os.path.exists(self.project_dir):
            shutil.rmtree(self.project_dir)

    def test_validate_valid_json(self):
        """Test that a valid .maxpat (JSON) passes validation."""
        patch_path = os.path.join(self.project_dir, "dist", "valid.maxpat")
        os.makedirs(os.path.dirname(patch_path), exist_ok=True)
        
        valid_data = {
            "patcher": {
                "fileversion": 1,
                "rect": [0, 0, 100, 100],
                "boxes": [],
                "lines": []
            }
        }
        with open(patch_path, 'w') as f:
            json.dump(valid_data, f)
            
        is_valid, message = core.validate_patch(patch_path)
        self.assertTrue(is_valid)
        self.assertIn("Valid Max JSON", message)

    def test_validate_invalid_json(self):
        """Test that invalid JSON fails validation."""
        patch_path = os.path.join(self.project_dir, "dist", "invalid.maxpat")
        with open(patch_path, 'w') as f:
            f.write("{ invalid json: [ }")
            
        is_valid, message = core.validate_patch(patch_path)
        self.assertFalse(is_valid)
        self.assertIn("Invalid JSON", message)

    def test_validate_missing_patcher_key(self):
        """Test that JSON missing the 'patcher' key fails validation."""
        patch_path = os.path.join(self.project_dir, "dist", "missing_key.maxpat")
        with open(patch_path, 'w') as f:
            json.dump({"not_a_patcher": {}}, f)
            
        is_valid, message = core.validate_patch(patch_path)
        self.assertFalse(is_valid)
        self.assertIn("Missing 'patcher' root key", message)

if __name__ == '__main__':
    unittest.main()
