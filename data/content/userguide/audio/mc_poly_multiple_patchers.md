---
description: Load multiple distinct patchers with mc.poly~
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_poly_multiple_patchers/
title: Polyphony with Multiple Patchers
---

# Polyphony with Multiple Patchers
Both the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") and [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") objects can contain different patchers for each voice. The names of the voice patches are set using the `@patchernames` attribute.
![](https://docs.cycling74.com/images/740b0e75a1c4a04e1270c8b197e77abd_508.webp)
You can use [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") to load a bank of patchers to use as audio effects operating in parallel on each channel of a multichannel signal. If you want to mix the output of all the effects, you can do that later with [mc.mixdown~](https://docs.cycling74.com/reference/mc.mixdown~ "mc.mixdown~") or [mc.op~](https://docs.cycling74.com/reference/mc.op~ "mc.op~").
![](https://docs.cycling74.com/images/c5e9d4e6b0e85fff915d77f6c0b10bc2_328.webp)
