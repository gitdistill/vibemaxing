---
description: Objects and documentation for spatialization in MC
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_spatialization/
title: MC Spatialization
---

# MC Spatialization
One of the applications for which MC is especially adept is working with multi-speaker systems and spatialization. Multichannel source material can be transported to objects and manipulated as a single unit, greatly reducing the amount of patching required to work with large sets of audio routings and outputs.
## Topics
You can learn more about issues related to spatialization by reviewing the following:
[MC and Max for Live](https://docs.cycling74.com/userguide/mc/mc_maxforlive_interface/)
[MC Channel Topology](https://docs.cycling74.com/userguide/mc/mc_channel_topology/)
[MC Recording and Playback](https://docs.cycling74.com/userguide/mc/mc_multichannel_sources/)
[MC Dynamic Routing](https://docs.cycling74.com/userguide/mc/mc_dynamic_routing/)
## Objects
In addition to the mc.* and mcs.* objects that perform multichannel audio manipulation, objects that are particularly useful for spatialization include:
  * [mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~")
  * [mc.adc~](https://docs.cycling74.com/reference/mc.adc~ "mc.adc~")
  * mc.plugin~
  * mc.plugout~
  * [mc.combine~](https://docs.cycling74.com/reference/mc.combine~ "mc.combine~")
  * [mc.separate~](https://docs.cycling74.com/reference/mc.separate~ "mc.separate~")
  * [mc.interleave~](https://docs.cycling74.com/reference/mc.interleave~ "mc.interleave~")
  * [mc.deinterleave~](https://docs.cycling74.com/reference/mc.deinterleave~ "mc.deinterleave~")
  * [mc.transpose~](https://docs.cycling74.com/reference/mc.transpose~ "mc.transpose~")
  * [mc.mixdown~](https://docs.cycling74.com/reference/mc.mixdown~ "mc.mixdown~")


## Examples
  * [MC Granular](https://docs.cycling74.com/userguide/mc/mc_spatialization/openfilelink) - A 16-channel granular synthesizer mixed to two channels
  * [Max for Live Channels](https://docs.cycling74.com/userguide/mc/mc_spatialization/openfilelink) - Output mapping for Max for Live


