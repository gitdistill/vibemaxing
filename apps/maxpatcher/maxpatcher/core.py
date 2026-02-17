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
    
    env = os.environ.copy()
    current_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{engine_path}{os.pathsep}{current_pythonpath}"
    
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

