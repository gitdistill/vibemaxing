import os
import json

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
        f.write(f"# {project_name}\\n\\nYour new Vibemaxing project.")

    print(f"Project '{project_name}' created successfully at {project_dir}")

