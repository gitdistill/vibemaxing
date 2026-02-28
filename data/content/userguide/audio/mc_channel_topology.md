---
description: Mixing channels from synthesis to physical outputs, including mixing down to stereo
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_channel_topology/
title: MC Channel Topology
---

# MC Channel Topology
Multichannel patch cords are useful as a way to organize audio signals. MC includes several objects that you can use to change how signals are organized.
For example, if you are using [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~") with a stereo synth plug-in that has 10 instances, that object will have two multichannel outputs with 10 channels each. The multichannel patch cord on the left has the "left" outputs for all 10 synths and the multichannel patch cord on the right has the "right" outputs for all 10 synths.
![](https://docs.cycling74.com/images/e17d988d160dcb83e77fe309008fd882_350.webp)
If want to mix all the synths to stereo, you will need to produce a two-channel signal routed to [mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~"). To mix the signals as expected, use [mc.interleave~](https://docs.cycling74.com/reference/mc.interleave~ "mc.interleave~") to produce a 20-channel signal that alternates the left and right channels.
![](https://docs.cycling74.com/images/dc5dd15097db2d7a21fb5cae032487ea_352.webp)
You can feed this 20-channel signal to [mc.stereo~](https://docs.cycling74.com/reference/mc.stereo~ "mc.stereo~"), which (by default) will add the odd-numbered channels (1, 3, 5...) to its first (or "left" output) and even-numbered channels (2, 4, 6...) to its second (or "right" output). The resulting signal can be connected directly to [mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~").
![](https://docs.cycling74.com/images/8298518ae925fd3f7195148e9afd67dc_360.webp)
Use [mc.deinterleave~](https://docs.cycling74.com/reference/mc.deinterleave~ "mc.deinterleave~") to transform an interleaved signal back to two non-interleaved signals. This is useful for separating signals for the inputs to [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~"), [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~"), or [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~").
The [mc.transpose~](https://docs.cycling74.com/reference/mc.transpose~ "mc.transpose~") object provides a more general way to reorganize multichannel signals. If you have four instances of [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") in an [mc.groove~](https://docs.cycling74.com/reference/mc.groove~ "mc.groove~") object playing back stereo samples, it provides you with two four-channel patch cords separating left and right channels. It may be more useful to have four two-channel patch cords, each of which has the left and right channels for the four instances. This can be accomplished with [mc.transpose~](https://docs.cycling74.com/reference/mc.transpose~ "mc.transpose~"):
![](https://docs.cycling74.com/images/bbc2d90a67cdbdddcdc6b11f26f1b1f1_316.webp)
Now you can add individual effects on a per-MC-instance basis, using [mcs.vst~](https://docs.cycling74.com/reference/mcs.vst~ "mcs.vst~") as shown here:
![](https://docs.cycling74.com/images/defb540c47c092a918cf927fa00d63a5_437.webp)
