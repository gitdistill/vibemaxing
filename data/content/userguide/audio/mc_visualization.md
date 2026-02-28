---
description: Cycling '74 Online Documentation. Browse and search the Max Documentation and Reference online
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_visualization/
title: MC Visualization and Probing
---

# MC Visualization and Probing
Multichannel signals can be visualized using the following objects:
  * [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") - standard LED-like metering
  * [levelmeter~](https://docs.cycling74.com/reference/levelmeter~/ "levelmeter~") - VU metering
  * [number~](https://docs.cycling74.com/reference/number~/ "number~") - displays the numerical value a signal
  * [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") - oscilliscope-like signal display
  * [spectroscope~](https://docs.cycling74.com/reference/spectroscope~/ "spectroscope~") - displays the spectral content of a signal


## Selecting a Display Channel
The [number~](https://docs.cycling74.com/reference/number~/ "number~"), [levelmeter~](https://docs.cycling74.com/reference/levelmeter~/ "levelmeter~"), [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") and [spectroscope~](https://docs.cycling74.com/reference/spectroscope~/ "spectroscope~") objects will adapt to show all multichannel signals, but will only display or foreground one channel at a time. Use the _channel display selector_ to bring one of the channels into focus.
  * Click on one of the channel display selector indicators to switch to the chosen channel.

![](https://docs.cycling74.com/images/475dc244f3a233826958917b7f94f277_466.webp)
The [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") and [levelmeter~](https://docs.cycling74.com/reference/levelmeter~/ "levelmeter~") objects have an _inactivealpha_ attribute that controls the relative brightness of unselected channels.
![](https://docs.cycling74.com/images/67aa7946a163fdd0b7e2e982bb3da609_473.webp)
## Signal Probing
The Signal Probe works with MC signals.
  * Enable _Signal Probe_ in the _Debug_ menu
  * Move the cursor over a multi-channel patch cord to view the signals it contains:

![](https://docs.cycling74.com/images/89718e7849a1e43b7a923aab1afe93f3_369.webp)
  * Press the _down-arrow key_ to switch to one of the alternative displays:

![](https://docs.cycling74.com/images/859409c45bac2efed78fbfd68705eb2b_386.webp)
