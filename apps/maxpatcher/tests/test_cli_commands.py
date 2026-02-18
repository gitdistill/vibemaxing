import unittest
import subprocess
import os
import shutil

# Assuming the maxpatcher CLI is available on the path,
# or we can invoke it via python -m maxpatcher.cli
CLI_PATH = "python3 -m maxpatcher.cli"
PROJECTS_ROOT = "projects"

class TestCliCommands(unittest.TestCase):

    def setUp(self):
        # Ensure the smoke_test project exists
        smoke_test_src_dir = os.path.join(PROJECTS_ROOT, "smoke_test", "src")
        os.makedirs(smoke_test_src_dir, exist_ok=True)
        # Create a dummy main.py if it doesn't exist, or ensure it's in its initial state
        with open(os.path.join(smoke_test_src_dir, "main.py"), "w") as f:
            f.write("""from maxpylang.maxpatch import MaxPatch
import os

def build():
    patch = MaxPatch()
    osc = patch.place_obj("cycle~ 440")
    amp = patch.place_obj("gain~")
    dac = patch.place_obj("ezdac~")
    patch.connect((osc.outs[0], amp.ins[0]))
    patch.connect((amp.outs[0], dac.ins[0]))
    patch.connect((amp.outs[1], dac.ins[1]))
    patch.save("dist/smoke_test.maxpat")

if __name__ == "__main__":
    build()
""")
        # Ensure a clean dist directory for smoke_test
        self.smoke_test_dist_dir = os.path.join(PROJECTS_ROOT, "smoke_test", "dist")
        if os.path.exists(self.smoke_test_dist_dir):
            shutil.rmtree(self.smoke_test_dist_dir)
        os.makedirs(self.smoke_test_dist_dir, exist_ok=True)
        self.smoke_test_output_path = os.path.join(self.smoke_test_dist_dir, "smoke_test.maxpat")

    def tearDown(self):
        # Clean up the dist directory after tests
        if os.path.exists(self.smoke_test_dist_dir):
            shutil.rmtree(self.smoke_test_dist_dir)


    def test_build_smoke_test_vibe_api(self):
        """
        Test building the smoke_test project after updating to the vibe Patcher API.
        This test initially expects to pass (if vibe is integrated), but might fail
        if there are issues with the CLI environment setup for vibe.
        """
        # Overwrite main.py with the vibe Patcher API content for this test
        vibe_main_py_content = """from maxpylang.maxpatch import MaxPatch
import os
from maxpatcher.vibe import Patcher

def build():
    vibe_patch = Patcher()
    osc = vibe_patch.add("cycle~ 440")
    amp = vibe_patch.add("gain~")
    dac = vibe_patch.add("ezdac~")
    vibe_patch.link(osc, amp)
    vibe_patch.link_stereo(amp, dac)
    vibe_patch.save("dist/smoke_test.maxpat")

if __name__ == "__main__":
    build()
"""
        smoke_test_src_dir = os.path.join(PROJECTS_ROOT, "smoke_test", "src")
        with open(os.path.join(smoke_test_src_dir, "main.py"), "w") as f:
            f.write(vibe_main_py_content)

        # Clear dist directory for this test
        if os.path.exists(self.smoke_test_dist_dir):
            shutil.rmtree(self.smoke_test_dist_dir)
        os.makedirs(self.smoke_test_dist_dir, exist_ok=True)

        command = f"{CLI_PATH} build smoke_test"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=False)
        
        self.assertEqual(result.returncode, 0, f"CLI command failed with output: {result.stderr}")
        self.assertTrue(os.path.exists(self.smoke_test_output_path), "smoke_test.maxpat was not created.")

if __name__ == "__main__":
    unittest.main()
