---
description: MC includes a number of objects that are useful for combining, separating, and transforming multichannel signals.
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_signals_newobjects/
title: MC Signal Manipulation Objects
---

# MC Signal Manipulation Objects
MC includes a number of objects that are useful for combining, separating, and transforming multichannel signals. These objects do not use the MC Wrapper but are useful in conjunction with wrapper-based objects.
## Creating Multi-Channel Signals
[mc.pack~](https://docs.cycling74.com/reference/mc.pack~ "mc.pack~") accepts numbers, single-channel signals, or multichannel signals and produces a multichannel signal with a designated number of outputs. This can be used to group separate single-channel sources into a single multichannel patch cord.
![](https://docs.cycling74.com/images/35d0f56c63cbf24ae705e4d980fc47f3_293.webp)
If you want to create a multichannel signal from numbers, you can also use the wrapper-based object [mc.sig~](https://docs.cycling74.com/reference/mc.sig~ "mc.sig~") or the even simpler [mc.list~](https://docs.cycling74.com/reference/mc.list~ "mc.list~").
![](https://docs.cycling74.com/images/1df823031894f199374b122f479012e3_358.webp)
## Separating Multi-Channel Signals into Single Channels
To separate a multichannel signal into one or more individual signal outputs, use [mc.unpack~](https://docs.cycling74.com/reference/mc.unpack~ "mc.unpack~"). The argument to [mc.unpack~](https://docs.cycling74.com/reference/mc.unpack~ "mc.unpack~") determines the number of individual signal outlets.
If the multi-channel input to [mc.unpack~](https://docs.cycling74.com/reference/mc.unpack~ "mc.unpack~") contains fewer channels than the number of outlets, the extra outlets will produce a zero signal. If the multichannel input contains more channels than the number of outlets, the additional input channels are ignored. 
![](https://docs.cycling74.com/images/af22b6cb378ec4d46e385a84f343812f_278.webp)
## Combining and Separating Multi-Channel Signals
If you have several multi-channel signals you would like to group into a single multichannel signal, use the [mc.combine~](https://docs.cycling74.com/reference/mc.combine~ "mc.combine~") object. [mc.combine~](https://docs.cycling74.com/reference/mc.combine~ "mc.combine~") produces an output multichannel signal containing the total number of input channels in the inputs. The argument to [mc.combine~](https://docs.cycling74.com/reference/mc.combine~ "mc.combine~") specifies the number of inputs.
To separate a multichannel signal into two or more multichannel signals, use [mc.separate~](https://docs.cycling74.com/reference/mc.separate~ "mc.separate~"). Arguments to [mc.separate~](https://docs.cycling74.com/reference/mc.separate~ "mc.separate~") specify the channel counts in its output signals.
![](https://docs.cycling74.com/images/13047f69fe5912f2192663f822052aa8_369.webp)
## Adding and Removing Channels
To make a multi-channel signal that copies a single-channel input, use [mc.dup~](https://docs.cycling74.com/reference/mc.dup~ "mc.dup~"). The argument specifies the number of copies produced.
To force a multichannel output to have a set number of channels, use [mc.separate~](https://docs.cycling74.com/reference/mc.separate~ "mc.separate~") with one argument specifying that number of channels. Additional channels are split off to the right outlet, but you don't need to connect that outlet to anything. If there are fewer channels in the input than you specify in the argument, the output will be padded with zero signals.
![](https://docs.cycling74.com/images/83b46a73c0bd3901a9ffc02e84b80b2b_214.webp)
To mix all channels of a multichannel signal to fewer channels, use [mc.mixdown~](https://docs.cycling74.com/reference/mc.mixdown~ "mc.mixdown~"). [mc.stereo~](https://docs.cycling74.com/reference/mc.stereo~ "mc.stereo~") is a stereo-specific version of the [mc.mixdown~](https://docs.cycling74.com/reference/mc.mixdown~ "mc.mixdown~") object. A single mixed channel can be obtained by using [mc.op~](https://docs.cycling74.com/reference/mc.op~ "mc.op~") with the `@op` attribute set to `sum`.
![](https://docs.cycling74.com/images/68a7727066d980a43b476e62c869c82d_377.webp)
## Transforming Signals
MC includes several objects that you can use to change how channels within multi-channel patch cords are organized, including [mc.interleave~](https://docs.cycling74.com/reference/mc.interleave~ "mc.interleave~"), [mc.deinterleave~](https://docs.cycling74.com/reference/mc.deinterleave~ "mc.deinterleave~"), and [mc.transpose~](https://docs.cycling74.com/reference/mc.transpose~ "mc.transpose~"). Some applications of these objects are described in [MC Channel Topology](https://docs.cycling74.com/userguide/mc/mc_channel_topology/).
