---
name: maxpylang
description: Core workflow and guidelines for programmatically generating MaxMSP patches (.maxpat) using the Python `maxpylang` library. Use this skill whenever you need to generate, modify, or inspect MaxMSP patches using Python code.
---

# MaxPyLang Patch Generator

This skill helps you programmatically generate or modify MaxMSP patches using the `maxpylang` Python library. It covers the core workflow of instantiating patches, placing objects, connecting them, modifying existing patches, and saving to disk.

## Core Concepts

The `maxpylang` library abstracts a Max patch as a `MaxPatch` object. This canvas holds individual `MaxObject`s, which communicate with each other via `Inlet`s and `Outlet`s. 

### Basic "Hello World" Workflow

Every basic script follows this pattern:
1. Create or load the patch
2. Place or modify objects
3. Connect or clean up inlets and outlets
4. Save the patch

```python
import maxpylang as mp

# 1. Create a new patch (or load one with `load_file="patch.maxpat"`)
patch = mp.MaxPatch()

# 2. Place objects
# patch.place() always returns a list, even for single objects
osc = patch.place("cycle~ 440")[0]
dac = patch.place("ezdac~")[0]

# 3. Connect them
# Connections are defined as a tuple/list: [source_outlet, dest_inlet]
patch.connect([osc.outs[0], dac.ins[0]])

# 4. Save the patch
# This will overwrite if the file already exists
patch.save("hello_world.maxpat")
```

## References for Complex Tasks

To keep context efficient, the deeper documentation and complex examples are separated into reference files. **You MUST use your `read` tool to load these files when you need their specific knowledge.**

- **API Reference**: `references/api_reference.md`
  - Read this when you need exact method signatures for `patch.place()` (e.g. grid spacing, vertical layout) or `patch.connect()`.
- **Advanced Examples**: `references/advanced_examples.md`
  - Read this when you need to generate multiple objects in parallel (using `num_objs`), handle dynamic strings (like `unpack` with variable outputs), fan-in/fan-out complex patch cords programmatically, or modify existing patches.

## Key Rules

- `patch.place()` ALWAYS returns a list of objects. To grab a single object, you must append `[0]`.
- Objects have zero-indexed `.ins` and `.outs` array properties for their inlets and outlets. 
- You do not need to manually delete a `.maxpat` file before saving. The `.save()` method overwrites the file cleanly.