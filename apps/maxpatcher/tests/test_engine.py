import unittest
import sys
import os

class TestEngine(unittest.TestCase):
    def test_engine_import(self):
        """Test that maxpylang can be imported from the engine directory."""
        # Calculate path to engine
        engine_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'engine'))
        mock_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'mocks'))
        
        # Add to sys.path
        if engine_path not in sys.path:
            sys.path.insert(0, engine_path)
            
        # Add mocks to path for tabulate
        if mock_path not in sys.path:
            sys.path.insert(0, mock_path)
            
        try:
            import maxpylang
            from maxpylang import maxpatch
        except ImportError:
            self.fail("Could not import maxpylang from engine")

if __name__ == '__main__':
    unittest.main()
