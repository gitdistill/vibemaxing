---
description: Managing audio input and output from mc.poly~
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_poly_newfeatures/
title: Polyphony Using mc.poly~
---

# Polyphony Using [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~")
The [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object manages polyphony for multiple instances of a patcher. The [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object always _copies_ audio inputs to each patcher instance, and _mixes_ the output of each patcher instance together at the object's outlets.
The [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") object uses multichannel signals to operate in a more flexible way. A multichannel input to [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") assigns the audio for each channel to its corresponding patcher instance ([poly~](https://docs.cycling74.com/reference/poly~/ "poly~") voice). The first audio input channel in the signal is passed to an [in~](https://docs.cycling74.com/reference/in~/ "in~") object within the first patcher instance, the second audio input channel in the signal is passed to an [in~](https://docs.cycling74.com/reference/in~/ "in~") object in the second patcher instance, and so on.
Similarly, the output fed to [out~](https://docs.cycling74.com/reference/out~/ "out~") objects in a patcher inside [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") is not mixed with the other patchers, it comes directly out to the corresponding channel of a multichannel signal.
Here is a patcher that simply passes audio input arriving at an [in~](https://docs.cycling74.com/reference/in~/ "in~") directly an [out~](https://docs.cycling74.com/reference/out~/ "out~"):
![](https://docs.cycling74.com/images/55cfc8774fb980c7fb3855a5e11e7467_159.webp)
Here is a comparison of [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") and [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") using simple numbers as input to four instances of this patcher loaded in each object. For the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") case, we feed a single-channel signal of 1 to the object and it produces a single-channel output:
![](https://docs.cycling74.com/images/85137f491e2c9e4407914e5a4f0ffb7d_217.webp)
Note that the output is 4, representing the sum of all the patchers mixing their inputs together.
For the [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") case, we will feed in a four-channel multichannel signal consisting of 1 in the first channel and 0 in the other three channels.
![](https://docs.cycling74.com/images/da5d65ebab1bcca5c366008be1fa6478_330.webp)
In this case, the output multichannel signal is equal to the input multichannel signal.
One use of [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") would be to load a simple patcher to use as an audio effect operating in parallel on each channel of a multichannel signal. If you want to mix the output of all the effects, you can do that later with [mc.mixdown~](https://docs.cycling74.com/reference/mc.mixdown~ "mc.mixdown~") or [mc.op~](https://docs.cycling74.com/reference/mc.op~ "mc.op~").
![](https://docs.cycling74.com/images/d5fdf98ba1b4eed5f3597c5434e8947f_345.webp)
