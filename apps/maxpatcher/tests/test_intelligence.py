import unittest
import os
import shutil
import sys
from unittest.mock import patch, MagicMock

# Add maxpatcher to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from maxpatcher import core

class TestIntelligence(unittest.TestCase):
    project_name = "sync_test_project"

    def setUp(self):
        if os.path.exists(f"projects/{self.project_name}"):
            shutil.rmtree(f"projects/{self.project_name}")
        core.create_project(self.project_name)

    def tearDown(self):
        if os.path.exists(f"projects/{self.project_name}"):
            shutil.rmtree(f"projects/{self.project_name}")

    def test_sync_project_updates_metadata(self):
        """Test that sync command updates the project's last_sync timestamp."""
        # Initial check - we'll check if the function exists and runs without error
        # In a real scenario, this would interact with Context7
        success = core.sync_project(self.project_name)
        self.assertTrue(success)
        
        vibe_path = f"projects/{self.project_name}/.vibe.json"
        import json
        with open(vibe_path, 'r') as f:
            config = json.load(f)
        
        self.assertIn("last_sync", config.get("metadata", {}))

if __name__ == '__main__':
    unittest.main()
