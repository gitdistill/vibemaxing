import os
import json
import subprocess
import sys

DEFAULT_MAIN_PY = """from maxpylang import maxpatch

# Create a new patch
p = maxpatch.MaxPatch()

# Create objects
metro = p.place("metro 500", num_objs=1, starting_pos=[100, 100])[0]
counter = p.place("counter", num_objs=1, starting_pos=[100, 150])[0]
button = p.place("button", num_objs=1, starting_pos=[100, 200])[0]

# Connect objects
p.connect([metro.outs[0], counter.ins[0]])
p.connect([counter.outs[0], button.ins[0]])

# Save the patch
p.save("dist/my-blinker.maxpat")
"""

def create_project(project_name: str):
    """
    Scaffolds a new maxpatcher project directory and its necessary files.
    """
    project_dir = os.path.join("projects", project_name)
    src_dir = os.path.join(project_dir, "src")
    dist_dir = os.path.join(project_dir, "dist")
    
    # Create directories
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dist_dir, exist_ok=True)
    
    # Create .vibe.json
    vibe_config = {
        "name": project_name,
        "version": "0.0.1",
        "type": "max-patch",
        "paths": {
            "src": "src/main.py",
            "dist": "dist/"
        }
    }
    with open(os.path.join(project_dir, ".vibe.json"), 'w') as f:
        json.dump(vibe_config, f, indent=2)
        
    # Create src/main.py
    with open(os.path.join(src_dir, "main.py"), 'w') as f:
        f.write(DEFAULT_MAIN_PY)
        
    # Create README.md
    with open(os.path.join(project_dir, "README.md"), 'w') as f:
        f.write(f"# {project_name}\n\nYour new Vibemaxing project.")

    print(f"Project '{project_name}' created successfully at {project_dir}")

def build_project(project_name: str):
    """
    Builds a project by executing its main script with injected environment paths.
    """
    project_dir = os.path.join("projects", project_name)
    if not os.path.exists(project_dir):
        print(f"Error: Project '{project_name}' not found.")
        return

    vibe_config_path = os.path.join(project_dir, ".vibe.json")
    if not os.path.exists(vibe_config_path):
        print(f"Error: .vibe.json not found in {project_dir}")
        return

    with open(vibe_config_path, 'r') as f:
        config = json.load(f)

    src_path = os.path.join(project_dir, config['paths']['src'])
    
    # Prepare environment with MaxPyLang engine on PYTHONPATH
    # We assume we are running from root
    engine_path = os.path.abspath(os.path.join(os.getcwd(), "apps/maxpatcher/engine"))
    maxpatcher_app_path = os.path.abspath(os.path.join(os.getcwd(), "apps/maxpatcher"))
    
    env = os.environ.copy()
    current_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{engine_path}{os.pathsep}{maxpatcher_app_path}{os.pathsep}{current_pythonpath}"
    
    print(f"Building {project_name} (Executing {src_path})...")
    
    # Run the user's main script
    # Change working directory to project root so relative paths in script work
    script_rel_path = config['paths']['src']
    try:
        result = subprocess.run(
            [sys.executable, script_rel_path],
            env=env,
            cwd=project_dir,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Build Failed:\nSTDOUT: {e.stdout}\nSTDERR: {e.stderr}")
        raise

def validate_patch(patch_path: str):
    """
    Validates a Max/MSP patch file (checks for valid JSON and necessary root key).
    """
    if not os.path.exists(patch_path):
        return False, f"Error: File {patch_path} not found."

    try:
        with open(patch_path, 'r') as f:
            data = json.load(f)
            
        if "patcher" not in data:
            return False, "Error: Missing 'patcher' root key."
            
        return True, "Success: Valid Max JSON patch."
    except json.JSONDecodeError as e:
        return False, f"Error: Invalid JSON: {str(e)}"

def validate_project(project_name: str):
    """
    Finds all .maxpat files in a project's dist folder and validates them.
    """
    project_dir = os.path.join("projects", project_name)
    if not os.path.exists(project_dir):
        print(f"Error: Project '{project_name}' not found.")
        return

    vibe_config_path = os.path.join(project_dir, ".vibe.json")
    if not os.path.exists(vibe_config_path):
        print(f"Error: .vibe.json not found in {project_dir}")
        return

    with open(vibe_config_path, 'r') as f:
        config = json.load(f)

    dist_dir = os.path.join(project_dir, config['paths']['dist'])
    if not os.path.exists(dist_dir):
        print(f"Error: Distribution directory {dist_dir} does not exist.")
        return

    print(f"Validating project '{project_name}'...")
    found_any = False
    for root, _, files in os.walk(dist_dir):
        for file in files:
            if file.endswith(".maxpat"):
                found_any = True
                full_path = os.path.join(root, file)
                is_valid, msg = validate_patch(full_path)
                print(f"  [{'PASS' if is_valid else 'FAIL'}] {file}: {msg}")
    
    if not found_any:
        print("No .maxpat files found in distribution folder.")

def sync_project(project_name: str):
    """
    Synchronizes the project by checking for object documentation in the global cache.
    Updates project metadata with 'last_sync'.
    """
    import datetime
    from . import intelligence
    project_dir = os.path.join("projects", project_name)
    vibe_config_path = os.path.join(project_dir, ".vibe.json")

    if not os.path.exists(vibe_config_path):
        print(f"Error: .vibe.json not found in {project_dir}")
        return False

    try:
        with open(vibe_config_path, 'r') as f:
            config = json.load(f)

        src_path = os.path.join(project_dir, config['paths']['src'])
        if os.path.exists(src_path):
            with open(src_path, 'r') as f:
                content = f.read()
            
            # Simple regex-less extraction for now (very naive)
            # Find common object names in the script
            common_objects = ["cycle~", "gain~", "ezdac~", "metro", "counter", "button", "bang"]
            found_objects = [obj for obj in common_objects if obj in content]
            
            print(f"Synchronizing project '{project_name}'...")
            for obj in found_objects:
                doc = intelligence.get_object_doc(obj)
                if doc:
                    print(f"  [CACHED] {obj}")
                else:
                    print(f"  [MISSING] {obj} (Ask the agent to sync this object)")
        
        if "metadata" not in config:
            config["metadata"] = {}
        
        config["metadata"]["last_sync"] = datetime.datetime.now().isoformat()
        
        with open(vibe_config_path, 'w') as f:
            json.dump(config, f, indent=4)
        
        print(f"Project '{project_name}' metadata updated.")
        return True
    except Exception as e:
        print(f"Error during sync: {e}")
        return False

