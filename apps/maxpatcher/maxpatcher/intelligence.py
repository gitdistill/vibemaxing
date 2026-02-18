import os
import json

# Correctly resolve the global cache directory
CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "cache", "objects"))

def get_object_doc(object_name: str) -> dict | None:
    """Loads object documentation from the global cache."""
    # Ensure the object name is sanitized for filenames
    # (Simplified for now, just replace / with _)
    safe_name = object_name.replace("/", "_")
    cache_path = os.path.join(CACHE_DIR, f"{safe_name}.json")
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None
    return None

def save_object_doc(object_name: str, data: dict):
    """Saves object documentation to the global cache."""
    # Ensure the object name is sanitized for filenames
    safe_name = object_name.replace("/", "_")
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"{safe_name}.json")
    with open(cache_path, 'w') as f:
        json.dump(data, f, indent=4)
