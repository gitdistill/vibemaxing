# MaxPyLang Knowledge Base

This document tracks technical findings, patterns, and constraints discovered while analyzing the `MaxPyLang` library. It serves as a durable reference for the "Junior Programmer" agent.

## Core Concepts

- **Imperative Generation:** MaxPyLang uses a Python-first approach to generate `.maxpat` files.
- **Source of Truth:** The `.py` script is the primary source of truth; the `.maxpat` is a build artifact.
- **Round-tripping:** The library can load existing `.maxpat` files, allowing for programmatic modification of hand-built patches.

## API Patterns

### 1. Object Placement
- **Method:** `patch.place("object_name args", **extra_attribs)`
- **Return Type:** Always returns a **list** of objects, even if only one is placed.
- **Generative Features:** Supports `randpick=True` with `weights` and `num_objs` to create probabilistic object distributions.
- **Layout Engines:**
    - **Grid:** Automatically wraps to new rows based on the patcher's `rect` width.
    - **Vertical:** Stacks objects downward.
    - **Custom:** Accepts specific `[[x, y]]` coordinates for each object.
    - **Random:** Scatters objects within the patcher canvas.
- **Cursor State:** The patch maintains a `_curr_position` [x, y] to handle automatic layout.
- **Validation:** Calls `obj.notknown()` during placement and prints a `PatchError` if metadata is missing.

### 2. Connections
- **Method:** `patch.connect([out_obj.outs[i], in_obj.ins[j], (optional_midpoints)])`
- **Stateful Tracking:** `Inlet` and `Outlet` objects maintain internal lists of `_sources` and `_destinations`, allowing for bidirectional graph traversal in Python.
- **Midpoints:** Supports optional [x, y] coordinates for patchcord segments.
- **Type Safety (Gap):** The library's `check_connection_typing` is currently a placeholder.
- **Max Behavior Note:** While Max itself won't crash when connecting incompatible ports (e.g., Signal to Message), it will silently fail to make the connection. MaxPyLang will write the cord to the file regardless, but it will be invalid/non-functional in the Max environment.

### 3. Internal Representation & Management
- **Object Storage:** `patch.objs` is a dictionary keyed by Max object IDs (e.g., `"obj-1"`).
- **Metadata Database:** Located in `maxpylang/data/`.
    - `OBJ_IO/`: Functional specifications of inlet/outlet counts and types. Handles dynamic xlets based on creation arguments (e.g., `sfplay~` adding a `bang` outlet).
    - `OBJ_INFO/`: Detailed object templates containing:
        - `default`: A skeletal Max JSON "box" definition.
        - `args`: Lists of required and optional positional arguments.
        - `attribs`: List of valid `@` attributes for that object, including references to `COMMON` attribute sets.
- **Templating:** New patches are initialized from an `empty_template.json`.
- **Refactoring Tools:** 
    - `replace(id, new_spec, retain=True)`: Swaps an object while attempting to preserve patchcords and common attributes.
    - `reorder()`: Re-numbers all object IDs sequentially starting from 1.
    - `delete(objs)`: Removes specified objects and their associated cords.
- **Discovery:** `patch.get_unknowns()` identifies objects missing from the internal metadata database.
- **Inspection:** `patch.inspect()` provides a way to read current object states, positions, and connections.
- **Patcher Dictionary:** The full patcher dictionary is accessible via the `patch.dict` property. This dictionary mirrors the final `.maxpat` JSON structure. For example, the patcher's dimensions are at `patch.dict['patcher']['rect']`.

## Constraints & Gaps

- **Object Awareness:** The library treats Max objects as strings; no built-in validation for object existence or argument correctness.
- **Manual Indexing:** High risk of "off-by-one" errors in complex patches without external documentation 
- **UI/Presentation:** Documentation on Presentation Mode and advanced UI layout is currently skeleton-only (empty docs).
- **Advanced Topics Gap:** Key documentation for "Unknown Objects", "Linked Files" (abstractions/JS), and "External Packages" is currently empty in the source docs, though functionality exists in the code.
- **Silent Failures:** Incompatible connections (e.g., Signal to Message) are written to the file by MaxPyLang but ignored by Max, creating a silent failure mode that requires external validation.
- **Unreliable Defaults:** Do not assume the default inlet/outlet count for objects. `gain~` and `*~` both default to a single inlet/outlet. Some objects, like `biquad~`, require creation arguments. Always consult the `OBJ_INFO` or `OBJ_IO` data, or load the `maxpert` skill.

## Known Workflows

1.  **The Factory:** Generating large-scale, repetitive, or algorithmic structures (e.g., 100 random oscillators).
2.  **The Modifier:** Loading an existing patch to add "utility" objects (e.g., adding a `peakamp~` and `meter~` to every DAC).
