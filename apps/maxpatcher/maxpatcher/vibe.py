from maxpylang import maxpatch

def get_patcher_center(patch: maxpatch.MaxPatch):
    """
    Calculates the center coordinates of the patcher window.

    Args:
        patch (MaxPatch): The patch to find the center of.

    Returns:
        tuple[float, float]: The (x, y) coordinates of the center.
    """
    rect = patch.dict['patcher']['rect'] # returns [x1, y1, x2, y2]
    center_x = (rect[0] + rect[2]) / 2
    center_y = (rect[1] + rect[3]) / 2
    return (center_x, center_y)

def connect_stereo(patch: maxpatch.MaxPatch, src, dest):
    """
    (NOT IMPLEMENTED) Connects the first two outlets of a source object 
    to the first two inlets of a destination object.
    """
    raise NotImplementedError("connect_stereo requires object introspection, pending intelligence module.")

def make_ui_row(patch: maxpatch.MaxPatch, objs: list):
    """
    (NOT IMPLEMENTED) Connects a list of objects in a row, from left to right.
    """
    raise NotImplementedError("make_ui_row is not implemented yet.")
