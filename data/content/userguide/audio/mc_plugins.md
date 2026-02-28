---
description: In MC, you can work with multiple copies of a plug-in to produce multiple channels of audio, or use multi-channel inputs and output with a single copy of the plug-in.
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_plugins/
title: Using Plug-ins with MC
---

# Using Plug-ins with MC
In MC, you can work with multiple copies of a plug-in to produce multiple channels of audio, or use multi-channel inputs and output with a single copy of the plug-in.
## Single Plug-in, Multi-Channel Signals
The [mcs.vst~](https://docs.cycling74.com/reference/mcs.vst~ "mcs.vst~") object allows you to work with a single instance of a plug-in, but have multi-channel inputs and outputs. In the most basic case, you can create an [mcs.vst~](https://docs.cycling74.com/reference/mcs.vst~ "mcs.vst~") with a favorite stereo VST effect, and have a 2-channel MC signal routed into and out of the effect.
![](https://docs.cycling74.com/images/7b2fbbd378990ea74402b234c28fe16a_203.webp)
If the plug-in is capable of more than two input or output channels, you can define the input and output channel counts with the first two arguments to [mcs.vst~](https://docs.cycling74.com/reference/mcs.vst~ "mcs.vst~").
## Multiple Copies of a Plug-in
The [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~") object works like other [MC Wrapper](https://docs.cycling74.com/userguide/mc/mc_wrapper/) objects: it contains multiple instances of a plug-in within a single Max object. The number of instances will auto-adapt to the number of inputs.
The number of inputs and outputs to the plug-in are defined by the channel argument(s) to [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~"), and each of the inlets and outlets will be a multichannel signal.
For example, a [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~") defined to have two I/O channels and four instances will produce two four-channel signals containing the "left" and "right" inputs to the four plug-in instances.
![](https://docs.cycling74.com/images/50f5ac07e5dfa0ad495b67160c96e275_207.webp)
When using a VST instrument plug-in, you will need to define the number of MC output channels to be used, preferably as a typed-in `@chans` argument, since you won't be sending the plug-in any audio inputs.
![](https://docs.cycling74.com/images/720e18557fb492db15ba7d23c2167bb5_382.webp)
## Accessing Parameters of Individual Plug-in Instances
When using [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~") to host multiple copies of the same plug-in, you may want to change the parameters of each copy to different settings. This can be done using the `mcisolate` attribute of the [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~") object, as well as the [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target") and [mc.targetlist](https://docs.cycling74.com/reference/mc.targetlist "mc.targetlist") objects to route messages to a single instance of the plug-in.
To alter individual instances of a plug-in's parameters:
  * Enable the `mcisolate` attribute of [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~") using a typed-in argument, [message](https://docs.cycling74.com/reference/message/ "message") box, or [attrui](https://docs.cycling74.com/reference/attrui/ "attrui").
  * Using [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target") or [mc.targetlist](https://docs.cycling74.com/reference/mc.targetlist "mc.targetlist"), send a `setvalue` message followed by the instance number and desired parameter name to [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~"). This will change the parameter for the targeted instance only.
  * To target all instances of the [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~") object, you can target using voice number 0 (zero), or disable the `mcisolate` attribute to distribute the change to all instances of the plug-in.

![](https://docs.cycling74.com/images/696f96a18d2eb9abbba3fa0f3d286a74_502.webp)
When `mcisolate` is off, any parameter change for any voice - or any change to the user interface of the plug-in - will result in that parameter being changed in all of the instances of the plug-in.
## Working with Max for Live Devices
Max for Live devices are hosted similarly to VST plug-ins, using the [mcs.amxd~](https://docs.cycling74.com/reference/mcs.amxd~ "mcs.amxd~") object for a single instance, and [mc.amxd~](https://docs.cycling74.com/reference/mc.amxd~ "mc.amxd~") for multiple-instance applications.
![](https://docs.cycling74.com/images/dbdb2ac2d6530469882613ccd71ffcec_500.webp)
If you are showing the device's interface in your patcher (by toggling on the _Show View In Patcher_ attribute), you can choose the instance of the device that is displayed by using the `displaychan` attribute.
