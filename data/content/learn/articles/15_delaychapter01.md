---
description: Managing simple delays withtapin~andtapout~
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/15_delaychapter01/
title: Simple Delay Lines
---

Download Series Content and Patchers
# MSP Delay Tutorial 1: Delay Lines
## Effects achieved with delayed signals
One of the most basic yet versatile techniques of audio processing is to delay a signal and mix the delayed version with the original signal. The delay time can range from a few milliseconds to several seconds, limited only by the amount of RAM you have available to store the delayed signal.
When the delay time is just a few milliseconds, the original and delayed signals interfere and create a subtle filtering effect but not a discrete echo. When the delay time is about 100 ms we hear a ‘slapback’ echo effect in which the delayed copy follows closely behind the original. With longer delay times, we hear the two signals as discrete events, as if the delayed version were reflecting off a distant mountain.
This tutorial patch delays each channel of a stereo signal independently, and allows you to adjust the delay times and the balance between direct signal and delayed signal.
## Creating a delay line: tapin~ and tapout~
The MSP object [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") is a buffer that is continuously updated so that it always stores the most recently received signal. The amount of signal it stores is determined by a typed-in argument. For example, a [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") object with a typed-in argument of `1000` stores the most recent one second of signal received in its inlet.
![](https://docs.cycling74.com/images/8faed13e62bc4f20a547f3a735dccc4e_293.webp) A 1-second delay buffer tapped 500 and 1000 ms in the past
The only object to which the outlet of [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") should be connected is a [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") object. This connection links the [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") object to the buffer stored by [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~"). The [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") object ‘taps into’ the delayed signal at certain points in the past. In the above example, [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") gets the signal from [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") that occurred 500 ms ago and sends it out the left outlet; it also gets the signal delayed by 1000 ms and sends that out its right outlet. It should be obvious that [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") can't get signal delayed beyond the length of time stored in [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~").
## A patch for mixing original and delayed signals
The tutorial patch sends the sound coming into the computer to two places: directly to the output of the computer and to a [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") - [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") delay pair. You can control how much signal you hear from each place for each of the stereo channels, mixing original and delayed signal in whatever proportion you want.
  * Turn audio on and send some sound in the input jacks of your computer. Set the [number box](https://docs.cycling74.com/reference/number/) marked ‘Output Level’ to a comfortable listening level. Set the ‘Left Delay Time’ [number box](https://docs.cycling74.com/reference/number/) to `500` and the ‘Right Delay Time’ to `1000`.


At this point you don't hear any delayed signal because the ‘Direct Level’ for each channel is set at `1` and the ‘Delay Level’ for each channel is set at `0`. The signal is being delayed, but you simply don't hear it because its amplitude is scaled to 0.
![](https://docs.cycling74.com/images/cb21ddb77545f53adc2961264cb02c2e_435.webp) Direct signal is on full; delayed signal is turned down to 0
The [slider](https://docs.cycling74.com/reference/slider/ "slider") in the left part of the Patcher window serves as a balance fader between a ‘Dry’ (all direct) output signal and a ‘Wet’ (fully processed) output signal.
  * Drag the [slider](https://docs.cycling74.com/reference/slider/ "slider") to the halfway point so that both the direct and delayed signal amplitudes are at `0.5`. You hear the original signal in both channels, mixed with a half-second delay in the left channel and a one-second delay in the right channel.

![](https://docs.cycling74.com/images/788f5cace530e421e9e4e00bb50e415c_505.webp) Equal balance between direct signal and delayed signal
  * You can try a variety of different delay time combinations and wet-dry levels. Try very short delay times for subtle comb filtering effects. Try creating rhythms with the two delay times (with, for example, delay times of 375 and 500 ms).


Changing the parameters while the sound is playing can result in clicks in the sound because this patch does not protect against discontinuities. You could create a version of this patch that avoids this problem by interpolating between parameter values with [line~](https://docs.cycling74.com/reference/line~/ "line~") or [number~](https://docs.cycling74.com/reference/number~/ "number~") objects.
In future tutorial chapters, you will see how to create delay feedback, how to use continuously variable delay times for flanging and pitch effects, and other ways of altering sound using delays, filters, and other processing techniques.
## Summary
The [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") object is a continuously updated buffer which always stores the most recently received signal. Any connected [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") object can use the signal stored in [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~"), and access the signal from any time in the past (up to the limits of the [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") object's storage). A signal delayed with [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") and [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") can be mixed with the undelayed signal to create discrete echoes, early reflections, or comb filtering effects.
## See Also
  * [tapin~ - Input to a delay line](https://docs.cycling74.com/reference/tapin~/)
  * [tapout~ - Output from a delay line](https://docs.cycling74.com/reference/tapout~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
