# Advanced MaxPyLang Examples

This document demonstrates common patterns for generating complex MaxMSP patches programmatically using Python and `maxpylang`.

## 1. Generating Multiple Objects in Parallel

You can pass `num_objs` to `patch.place()` to generate multiple instances of the same object. The function will return a list of `MaxObject` instances. This is very useful for polyphony or multi-channel routing.

```python
import maxpylang as mp

patch = mp.MaxPatch()
num_notes = 12

# Create 12 parallel metro and random objects
# By default, they will be laid out in a grid
mtr = patch.place("metro 100", num_objs=num_notes, starting_pos=[0, 315])
rnd = patch.place("random 500", num_objs=num_notes, starting_pos=[0, 345])

# You can iterate over them with zip() to connect them in parallel
for m, r in zip(mtr, rnd):
    patch.connect([m.outs[0], r.ins[0]])
```

## 2. Dynamic Object Strings

Sometimes you need an object to have arguments that scale dynamically (e.g. an `unpack` object that un-packs `n` values). You can build the object string dynamically before placing it.

```python
import maxpylang as mp

patch = mp.MaxPatch()
num_notes = 12

# We want an unpack object that looks like: "unpack 0. 0. 0. ..." 
unpack_str = "unpack"
for i in range(num_notes):
    unpack_str += " 0."

# Place the dynamically generated object string
unp = patch.place(unpack_str, num_objs=1)[0]
```

## 3. Fan-out / Fan-in Connections (1-to-many, many-to-1)

Connecting a single outlet to multiple inlets, or routing multiple outlets into a single inlet.

```python
import maxpylang as mp

patch = mp.MaxPatch()

# 1-to-many: Connecting a single toggle to many metronomes
tg = patch.place("toggle")[0]
mtr = patch.place("metro 100", num_objs=5)

for m in mtr:
    patch.connect([tg.outs[0], m.ins[0]])

# Many-to-1: Connecting multiple gains to a single multiplier
gn = patch.place("gain~", num_objs=5)
mult = patch.place("*~ 0.05")[0]

for g in gn:
    patch.connect([g.outs[0], mult.ins[0]])
```

## 4. Connecting sequentially from a multi-outlet object

If an object has many outlets (like `unpack`), you can iterate over its `.outs` array by index.

```python
import maxpylang as mp

patch = mp.MaxPatch()
num_notes = 5

unp = patch.place("unpack 0. 0. 0. 0. 0.")[0]
gains = patch.place("gain~", num_objs=num_notes)

# Route each unpack outlet to a different gain inlet
for i, g in enumerate(gains):
    patch.connect([unp.outs[i], g.ins[0]])
```

## 5. Modifying Existing Patches

MaxPyLang allows you to manipulate existing patches programmatically. You can load a patch, find objects, edit them, or dynamically replace them.

```python
import maxpylang as mp

# Load an existing patch
patch = mp.MaxPatch(load_file="my_patch.maxpat")

# Replace an object, retaining its attributes and patchcords
# This is useful for upgrading or swapping logic nodes
patch.replace('obj-3', 'phasor~ 440')

# Edit an object's arguments or attributes dynamically
my_obj = patch.objs['obj-5']
my_obj.edit(text_add="append", text="@active 1")

# Clean up patch by removing unused nodes and re-numbering IDs
patch.delete(objs=['obj-10', 'obj-11'])
patch.reorder()
patch.save("my_modified_patch.maxpat")
```