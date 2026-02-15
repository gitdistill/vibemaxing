import unittest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

# Add apps/maxpatcher to sys.path so we can import maxpatcher
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestCLI(unittest.TestCase):
    def test_entry_point(self):
        """Test that the CLI entry point exists and runs."""
        try:
            from maxpatcher import cli
        except ImportError:
            self.fail("Could not import maxpatcher.cli")

        # Capture output to prevent printing during test
        captured_output = StringIO()
        with redirect_stdout(captured_output), redirect_stderr(captured_output):
            with self.assertRaises(SystemExit) as cm:
                # Simulate running with --help
                sys.argv = ['maxpatcher', '--help']
                cli.main()
            
            # Expect exit code 0 for help
            self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()
