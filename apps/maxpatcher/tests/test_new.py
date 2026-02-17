import unittest
import os
import shutil
import json
import sys

# Add maxpatcher to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from maxpatcher import cli

class TestNewCommand(unittest.TestCase):

    project_name = "test_project"
    project_dir = os.path.join("projects", project_name)

    def tearDown(self):
        """Clean up the created project directory after each test."""
        if os.path.exists(self.project_dir):
            shutil.rmtree(self.project_dir)

    def test_new_project_creates_files(self):
        """Test that `maxpatcher new <name>` creates the correct file structure."""
        # Simulate CLI arguments
        sys.argv = ['maxpatcher', 'new', self.project_name]
        
        # Run the command
        try:
            cli.main()
        except SystemExit as e:
            # We expect a sys.exit, but we want to check the files first
            pass

        # Assertions
        self.assertTrue(os.path.isdir(self.project_dir), "Project directory was not created.")
        
        # Check for .vibe.json
        vibe_json_path = os.path.join(self.project_dir, ".vibe.json")
        self.assertTrue(os.path.isfile(vibe_json_path), ".vibe.json was not created.")
        
        with open(vibe_json_path, 'r') as f:
            data = json.load(f)
            self.assertEqual(data.get("name"), self.project_name)

        # Check for src/main.py
        main_py_path = os.path.join(self.project_dir, "src", "main.py")
        self.assertTrue(os.path.isfile(main_py_path), "src/main.py was not created.")
        
        # Check for dist/ directory
        dist_path = os.path.join(self.project_dir, "dist")
        self.assertTrue(os.path.isdir(dist_path), "dist/ directory was not created.")

if __name__ == '__main__':
    unittest.main()
