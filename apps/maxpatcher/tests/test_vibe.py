import unittest
import sys
import os

# Add maxpatcher to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# We need the actual engine to test the helpers
engine_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'engine'))
if engine_path not in sys.path:
    sys.path.insert(0, engine_path)

from maxpylang import maxpatch
from maxpatcher import vibe

class TestVibeModule(unittest.TestCase):

    def test_vibe_importable(self):
        """Test that the vibe helper module can be imported."""
        # This test implicitly passes if the import above succeeds
        self.assertTrue(True)

    def test_get_patcher_center(self):
        """Test the get_patcher_center helper function."""
        p = maxpatch.MaxPatch()
        # Default patcher rect is [34.0, 87.0, 1372.0, 779.0]
        # Center should be ((34+1372)/2, (87+779)/2) = (703, 433)
        
        center = vibe.get_patcher_center(p)
        self.assertEqual(center, (703.0, 433.0))

if __name__ == '__main__':
    unittest.main()
