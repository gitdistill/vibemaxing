from __future__ import annotations
import os
from maxpylang.maxpatch import MaxPatch
from maxpylang.maxobject import MaxObject

class Patcher:
    """
    A Coordinator for Max/MSP patches, wrapping the MaxPyLang engine.
    It provides a high-level API for object creation, layout, and connections.
    """

    def __init__(self, template: str | None = None):
        """
        Initialize a new patcher.
        If template is None, the engine defaults to its internal empty template.
        """
        # We'll allow MaxPyLang to handle the default template for now.
        self._patch = MaxPatch(template=template)

    @property
    def engine_patch(self) -> MaxPatch:
        """Access the underlying MaxPyLang MaxPatch instance."""
        return self._patch

    def add(self, text: str, position: list[float] | None = None, **kwargs) -> MaxObject:
        """
        Adds an object to the patch.
        
        Args:
            text: The in-box text (e.g., 'cycle~ 440').
            position: Optional [x, y] coordinates. If None, it uses the MaxPyLang's auto-placement.
            **kwargs: Additional attributes for the MaxObject.
        """
        if position is None:
            # Use MaxPyLang's place method for auto-layout
            # It returns a list of placed objects. We only place one at a time.
            # Passing kwargs to place may not work if they're not recognized by place.
            # For now, only passing text. Further refinement may be needed for kwargs.
            placed_objs = self._patch.place(text, spacing_type="grid") # Removed kwargs for now
            obj = placed_objs[0]
        else:
            # If position is specified, use place_obj directly
            obj = self._patch.place_obj(text, position=position, **kwargs)
        
        return obj

    def link(self, src: MaxObject, dest: MaxObject, out_idx: int = 0, in_idx: int = 0):
        """
        Connects a source object outlet to a destination object inlet.
        
        Args:
            src: The source MaxObject.
            dest: The destination MaxObject.
            out_idx: The index of the source outlet (default 0).
            in_idx: The index of the destination inlet (default 0).
        """
        try:
            self._patch.connect((src.outs[out_idx], dest.ins[in_idx]))
        except IndexError as e:
            raise IndexError(f"Failed to connect {src.name} (out {out_idx}) to {dest.name} (in {in_idx}): {e}")

    def link_stereo(self, src: MaxObject, dest: MaxObject, out_indices: tuple[int, int] = (0, 1), in_indices: tuple[int, int] = (0, 1)):
        """Helper to connect two outlets to two inlets (stereo/dual-mono)."""
        self.link(src, dest, out_indices[0], in_indices[0])
        self.link(src, dest, out_indices[1], in_indices[1])

    def save(self, path: str):
        """Saves the patch to the specified path."""
        # Ensure the directory exists
        path_obj = os.path.abspath(path)
        os.makedirs(os.path.dirname(path_obj), exist_ok=True)
        self._patch.save(path)

    def __repr__(self):
        return f"<vibe.Patcher objects={len(self._patch._objs)}>"
