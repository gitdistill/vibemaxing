---
description: The Ableton DSP package is a collection of objects that bring Ableton Live devices and high-level DSP components into Max
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/abl/
title: Ableton DSP
---

# Ableton DSP
The Ableton DSP package is a collection of objects that bring Ableton Live devices and high-level DSP components into Max. From oscillators to modulators and filters to reverbs, these objects provide building blocks that speed up patch creation.
![A Max patcher with a midiin object connected to abl.device.drift~ which routes to abl.dsp.darkhall~ and abl.device.limiter~ with attrui objects to change various parameters like oscillator types, reverb mix, and limiter ceiling.](https://docs.cycling74.com/images/12ccacf7a25083f75b79430b4f226c40_694.webp)
## abl.device vs. abl.dsp
The prefixes "abl.device" and "abl.dsp" are used to distinguish between objects that wrap entire Live devices and objects that wrap DSP components. For instance, [abl.device.utility~](https://docs.cycling74.com/reference/abl.device.utility~ "abl.device.utility~") has the same functionality as the Live [Utility](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#utility) device, whereas [abl.dsp.ramp~](https://docs.cycling74.com/reference/abl.dsp.ramp~ "abl.dsp.ramp~") wraps one of the modulators in Live's [Meld](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#meld) instrument and [abl.dsp.shimmer~](https://docs.cycling74.com/reference/abl.dsp.shimmer~ "abl.dsp.shimmer~") wraps one of Live's [Hybrid Reverb](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#hybrid-reverb) audio effects.
## Inlets and attributes
In most Ableton DSP objects, there are a select number of parameters that can be changed as either attributes or signals. For example, the `@ratio` attribute of [abl.dsp.harmonicfm~](https://docs.cycling74.com/reference/abl.dsp.harmonicfm~ "abl.dsp.harmonicfm~") can be controlled via the third inlet. When a signal is connected to the inlet, the attribute will become disabled while the signal takes over control. If the signal is disconnected, the attribute will re-enable.
![A Max patcher with two abl.dsp.harmonicfm~ objects showing the ratio attribute with an attrui. The second abl.dsp.harmonicfm~ object has a signal routed to the third inlet, and the attached attrui shows the ratio attribute grayed out.](https://docs.cycling74.com/images/9dc7add0a504be3a790c4f8e58dd5031_677.webp)
## Internal smoothing
Unlike most Max objects, Ableton DSP objects offer internal parameter smoothing. Whenever a float-type attribute is changed at event-rate (from an [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") or float inlet, for example), a short ramp is applied instead of immediately stepping to the new value. This mitigates "zipper noise" as attributes are changed at event-rate. However, if you control a parameter at signal rate by attaching a signal to an inlet, no extra smoothing is applied.
