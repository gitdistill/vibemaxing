---
description: Best practices for building multichannel delay systems with MC
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_audio_delays/
title: Multichannel Delay Systems
---

# Multichannel Delay Systems
The [mc.tapin~](https://docs.cycling74.com/reference/mc.tapin~ "mc.tapin~") and [mc.tapout~](https://docs.cycling74.com/reference/mc.tapout~ "mc.tapout~") objects let you build networks of multichannel delay lines. The [mc.tapin~](https://docs.cycling74.com/reference/mc.tapin~ "mc.tapin~") object auto-adapts to the number of channels in the multichannel patch cord connected to its input, creating individual delay memories for each input channel. Connected [mc.tapout~](https://docs.cycling74.com/reference/mc.tapout~ "mc.tapout~") objects create one or more multichannel taps of this multichannel delay line.
![](https://docs.cycling74.com/images/49b613863db085b04e2e96c30b47e692_320.webp)
## Multichannel Delay Time Control
Using multichannel signals fed to the input(s) of [mc.tapout~](https://docs.cycling74.com/reference/mc.tapout~ "mc.tapout~") that represent delay times, you can control the individual delay times of each of the channels in each multichannel tap.
Here is an example where we use a four-channel delay line with two output taps. Each tap has a four-channel multichannel signal controlling its delay times. The result is eight outputs, each with its own unique delay time.
![](https://docs.cycling74.com/images/9b949a3c8b9070992d443a558d9b3231_624.webp)
## Multichannel Feedback Control
You can feed the signals from [mc.tapout~](https://docs.cycling74.com/reference/mc.tapout~ "mc.tapout~") back into the input of [mc.tapin~](https://docs.cycling74.com/reference/mc.tapin~ "mc.tapin~") to create multichannel feedback delays. By multiplying the output gains with [mc.multigain~](https://docs.cycling74.com/reference/mc.multigain~ "mc.multigain~") you can control the feedback levels of each channel individually.
![](https://docs.cycling74.com/images/864a783583350cd5e83f6f62f22e7519_657.webp)
Note that the multichannel inputs to [mc.tapin~](https://docs.cycling74.com/reference/mc.tapin~ "mc.tapin~") are automatically added to the audio input coming from the [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~").
