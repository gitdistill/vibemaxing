import unittest
import os
import shutil
import maxpatcher.intelligence

class TestIntelligence(unittest.TestCase):

    def setUp(self):
        # Create a temporary cache directory for testing
        self.test_cache_dir = os.path.join(os.getcwd(), "tests/temp_cache")
        os.makedirs(self.test_cache_dir, exist_ok=True)
        # Monkeypatch CACHE_DIR in the intelligence module
        self.original_cache_dir = maxpatcher.intelligence.CACHE_DIR
        maxpatcher.intelligence.CACHE_DIR = self.test_cache_dir

    def tearDown(self):
        # Clean up the temporary cache directory
        if os.path.exists(self.test_cache_dir):
            shutil.rmtree(self.test_cache_dir)
        # Restore the original CACHE_DIR
        maxpatcher.intelligence.CACHE_DIR = self.original_cache_dir

    def test_save_and_get_doc(self):
        """Test that saving and then getting documentation works correctly."""
        test_data = {
            "name": "cycle~",
            "inlets": 1,
            "outlets": 1,
            "description": "Sine wave oscillator"
        }
        maxpatcher.intelligence.save_object_doc("cycle~", test_data)
        
        # Verify the file exists
        self.assertTrue(os.path.exists(os.path.join(self.test_cache_dir, "cycle~.json")))
        
        # Load and verify the data
        loaded_data = maxpatcher.intelligence.get_object_doc("cycle~")
        self.assertEqual(loaded_data, test_data)

    def test_get_nonexistent_doc(self):
        """Test that getting non-existent documentation returns None."""
        self.assertIsNone(maxpatcher.intelligence.get_object_doc("unknown_object"))

if __name__ == "__main__":
    unittest.main()
