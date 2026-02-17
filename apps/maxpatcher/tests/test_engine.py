import unittest
import sys
import os

class TestEngine(unittest.TestCase):
    def test_engine_import(self):
        """Test that maxpylang can be imported from the engine directory."""
        # Calculate path to engine
        engine_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'engine'))
        
        # Add to sys.path
        if engine_path not in sys.path:
            sys.path.insert(0, engine_path)
            
        try:
            import maxpylang
            from maxpylang import maxpatch
        except ImportError as e:
            self.fail(f"Could not import maxpylang from engine: {e}")

if __name__ == '__main__':
    unittest.main()
