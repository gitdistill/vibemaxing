import unittest
import os
import shutil
import sys
import subprocess

# Add maxpatcher to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from maxpatcher import cli, core

class TestBuildCommand(unittest.TestCase):
    project_name = "build_test_project"
    project_dir = os.path.join("projects", project_name)

    def setUp(self):
        """Create a fresh project before each test."""
        if os.path.exists(self.project_dir):
            shutil.rmtree(self.project_dir)
        core.create_project(self.project_name)

    def tearDown(self):
        """Clean up the created project directory."""
        if os.path.exists(self.project_dir):
            shutil.rmtree(self.project_dir)

    def test_build_generates_maxpat(self):
        """Test that `maxpatcher build <name>` runs the user script and generates a .maxpat."""
        # The default main.py created by 'new' saves to "dist/my-blinker.maxpat"
        expected_maxpat = os.path.join(self.project_dir, "dist", "my-blinker.maxpat")
        
        # Ensure it doesn't exist yet
        if os.path.exists(expected_maxpat):
            os.remove(expected_maxpat)

        # Simulate CLI arguments: maxpatcher build build_test_project
        sys.argv = ['maxpatcher', 'build', self.project_name]
        
        try:
            cli.main()
        except SystemExit:
            pass

        # Assertions
        self.assertTrue(os.path.isfile(expected_maxpat), f"Build did not generate {expected_maxpat}")

if __name__ == '__main__':
    unittest.main()
