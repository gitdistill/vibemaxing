# MaxPyLang API Reference

This document summarizes the core classes and methods in the `maxpylang` library for generating MaxMSP patches programmatically. 

## `MaxPatch`

The equivalent of a patcher file (`.maxpat`) in MaxMSP. It serves as the canvas and manager for all objects and connections.

### Instantiation

```python
import maxpylang as mp

# Create an empty patch
patch = mp.MaxPatch()

# Load an existing patch
patch = mp.MaxPatch(load_file="existing_patch.maxpat")
```

### Core Methods

#### `place(*objs, **kwargs) -> list[MaxObject]`

Places objects on the patch. Returns a list of the created `MaxObject` instances.

**Arguments:**
- `*objs`: One or more strings representing the Max objects to create (e.g., `"cycle~ 440"`, `"metro 500"`).
- `randpick=False`: If True, pick `num_objs` randomly from `*objs`. If False, places all objects in `*objs`.
- `num_objs=1`: Number of objects to place (or a list of multipliers if `randpick=False`).
- `spacing_type="grid"`: How to position objects. Options: `"grid"`, `"random"`, `"custom"`, `"vertical"`.
- `spacing=[80.0, 80.0]`: Spacing dimension depending on `spacing_type`. For grid, it's `[x, y]`. For vertical, it's a number.
- `starting_pos=[x, y]`: The `[x, y]` coordinates to start placing from.

**Examples:**
```python
# Grid placement
oscs = patch.place("cycle~ 220", "cycle~ 330", "cycle~ 440", spacing_type="grid", spacing=[100, 80])

# Vertical placement
metro = patch.place("metro 500", "button", "random 100", spacing_type="vertical", spacing=50)
```

#### `connect(*connections, verbose=True)`

Connects the outlets of objects to the inlets of other objects.

**Arguments:**
- `*connections`: A list of tuples/lists defining the connections. Format: `[source_outlet, dest_inlet, [optional_midpoints]]`.

**Example:**
```python
# Connect osc outlet 0 to dac inlet 0
patch.connect([osc.outs[0], dac.ins[0]])

# With midpoints for a curved patchcord
patch.connect([obj1.outs[0], obj2.ins[0], [[100, 200], [150, 250]]])
```

#### `delete(objs=None, cords=None, verbose=True)`

Deletes objects and/or patchcords from the patch. Deleting an object automatically removes its connected patchcords.

**Arguments:**
- `objs`: List of object ID strings to delete (e.g., `['obj-1', 'obj-2']`).
- `cords`: List of connections to remove, formatted as `[source_outlet, dest_inlet]`.

#### `replace(curr_obj_num: str, new_obj, retain=True, **new_attribs)`

Replaces an object in the patch with a different object.

**Arguments:**
- `curr_obj_num`: ID string of the current object to replace (e.g., `'obj-5'`).
- `new_obj`: String specification or `MaxObject` of the new object.
- `retain`: If `True`, retains all attributes in common and attempts to retain patchcords.

**Example:**
```python
# Replace 'obj-3' with a phasor~ object, keeping connections if possible
patch.replace('obj-3', 'phasor~ 440')
```

#### `set_position(new_x, new_y, from_place=False)`

Sets the current "cursor" position `[x, y]` from which the next objects will be placed.

#### `reorder(verbose=False)`

Re-numbers all objects in the patch starting from 1 (e.g., `'obj-1'`, `'obj-2'`). Useful after deleting or replacing multiple objects.

#### `save(filename="default.maxpat", verbose=True, check=True)`

Saves the patcher to a `.maxpat` file. Overwrites if the file already exists.

```python
patch.save("my_generated_patch.maxpat")
```

#### `check(*flags)`

Checks the patch for unknowns, missing JS scripts, or unlinked abstractions. 
Flags: `"unknowns"`, `"js"`, `"abstractions"`. Called automatically on `save()`.

---

## `MaxObject`

Represents an individual MaxMSP object (e.g., `cycle~`, `+`, `random`).

### Key Properties

- `ins`: A list of the object's `Inlet`s. Accessed by 0-based index. Example: `my_obj.ins[0]`.
- `outs`: A list of the object's `Outlet`s. Accessed by 0-based index. Example: `my_obj.outs[0]`.
- `name`: String of the object's class name.

### Core Methods

#### `edit(text_add="append", text=None, **extra_attribs)`

Edits an object by adding/replacing arguments and attributes.

**Arguments:**
- `text_add`: `'append'` (default) keeps current args and appends new ones. `'replace'` erases current args and sets new ones.
- `text`: String of arguments/attributes to parse and add (e.g., `"440 @active 1"`).
- `**extra_attribs`: Key-value attribute settings (e.g., `fontface=1`, `color=[1.0, 0.0, 0.0, 1.0]`).

#### `move(x, y)`

Moves the object to the specified `[x, y]` pixel coordinates on the patching canvas.

#### `link(link_file=None)`

Links a JavaScript file or abstraction file to the object (only for `js` objects or abstractions). Updates the text field to reflect the filename.

## `Inlet` & `Outlet`

Represent the inlets and outlets of a `MaxObject`. 
They are primarily used to pass into `patch.connect()`.

```python
# Accessing an outlet
source_outlet = obj1.outs[0]

# Accessing an inlet
dest_inlet = obj2.ins[1] 

# Connecting them
patch.connect([source_outlet, dest_inlet])
```