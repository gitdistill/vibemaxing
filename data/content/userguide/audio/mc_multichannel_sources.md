---
description: Techniques for using MC objects to record and play from buffers
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_multichannel_sources/
title: MC Recording and Playback
---

# MC Recording and Playback
## Buffer Playback with mc.* Objects
The **mc.*** versions of the objects create multiple parallel versions of the audio playback objects. By changing parameters to each of the devices, you can create complex results with relatively little patching. For example, you can use [mc.groove~](https://docs.cycling74.com/reference/mc.groove~ "mc.groove~") modified by the `deviate` wrapper message to create a swarming effect.
![](https://docs.cycling74.com/images/85a71d4d223170a36f335188a197a736_400.webp)
## Buffer Playback with mcs.* Objects
Using the **mcs.*** objects for buffer playback makes it easier to integrate audio streams with other MC objects. The mcs.* objects implement multichannel inlets and outlets that can be further manipulated with MC objects or routed to multi-speaker audio systems.
For example, we can use the multichannel output of the [mcs.groove~](https://docs.cycling74.com/reference/mcs.groove~ "mcs.groove~") object as source material for a dual-channel fade-in patch. Since the multichannel audio is directly manipulated by the _mc.*~_ object, a multichannel signal will control the output levels of our file player.
![](https://docs.cycling74.com/images/ab0eaf76e08cbaf3c8d86de803513d47_308.webp)
## Recording
Use the [mc.sfrecord~](https://docs.cycling74.com/reference/mc.sfrecord~ "mc.sfrecord~") object to record a multi-channel signal directly to disk.
![](https://docs.cycling74.com/images/91089a16b6035a4a5bb4afa6b7279122_475.webp)
You can also record into a multichannel [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object using the [mc.record~](https://docs.cycling74.com/reference/mc.record~ "mc.record~") object.
