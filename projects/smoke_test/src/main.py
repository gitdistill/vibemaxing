from maxpylang.maxpatch import MaxPatch
import os
from maxpatcher.vibe import Patcher

def build():
    vibe_patch = Patcher()
    osc = vibe_patch.add("cycle~ 440")
    amp = vibe_patch.add("gain~")
    dac = vibe_patch.add("ezdac~")
    vibe_patch.link(osc, amp)
    vibe_patch.link_stereo(amp, dac)
    vibe_patch.save("dist/smoke_test.maxpat")

if __name__ == "__main__":
    build()
