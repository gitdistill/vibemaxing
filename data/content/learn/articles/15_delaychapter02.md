---
description: Using feedback in MSP delay networks
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/15_delaychapter02/
title: Delay Lines with Feedback
---

Download Series Content and Patchers
# MSP Delay Tutorial 2: Delay Lines with Feedback
## Delay emulates reflection
You can delay a signal for a specific amount of time using the [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") and [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") objects. The [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") object is a continually updated buffer that stores the most recent signal it has received, and [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") accesses that buffer at one or more specific points in the past.
![](https://docs.cycling74.com/images/6b1529f8fd9ef2af50e56c5b24c16d4c_358.webp) Delaying a signal with tapin~ and tapout~
Combining a sound with a delayed version of itself is a simple way of emulating a sound wave reflecting off of a wall before reaching our ears; we hear the direct sound followed closely by the reflected sound. In the real world some of the sound energy is actually absorbed by the reflecting wall, and we can emulate that fact by reducing the amplitude of the delayed sound, as shown in the following example.
![](https://docs.cycling74.com/images/8be33822e49efbaff6cc9d1cb5ac03a0_331.webp) Scaling the amplitude of a delayed signal, to emulate absorption
**Technical detail:** Different materials absorb sound to varying degrees, and most materials absorb sound in a way that is frequency-dependent. In general, high frequencies get absorbed more than low frequencies. That fact is being ignored here.
## Delaying the delayed signal
Also, in the real world there's usually more than one surface that reflects sound. In a room, for example, sound reflects off of the walls, ceiling, floor, and objects in the room in myriad ways, and the reflections are in turn reflected off of other surfaces. One simple way to model this ‘reflection of reflections’ is to feed the delayed signal back into the delay line (after first ‘absorbing’ some of it).
![](https://docs.cycling74.com/images/e24f4dc96836c33982af454210bbd4d3_290.webp) Delay with feedback
A single feedback delay line like the one above is too simplistic to sound much like any real world acoustical situation, but it can generate a number of interesting effects. Stereo delay with feedback is implemented in the example patch for this tutorial. Each channel of audio input is delayed, scaled, and fed back into the delay line.
![](https://docs.cycling74.com/images/f3376f517c8aa415827063ce1112e0e3_439.webp) Stereo delay with individual delay times and feedback amounts
  * Set the [number box](https://docs.cycling74.com/reference/number/) marked ‘Output Level’ to `0.25`, and move the [slider](https://docs.cycling74.com/reference/slider/ "slider") to its middle position so that the ‘Direct Level’ and ‘Delay Level’ [number box](https://docs.cycling74.com/reference/number/) objects read `0.5`. Turn audio on, and send some sound into the audio input of the computer. Experiment with different delay times and feedback amounts. For example, you can use the settings shown above to achieve a blurring effect. Increase the feedback amounts for a greater resonant ringing at the rate of feedback (1000 divided by the delay time). Increase the delay times to achieve discrete echoes. You can vary the Dry/Wet mix with the [slider](https://docs.cycling74.com/reference/slider/ "slider").


Note that any time you feed audio signal back into a system, you have a potential for overloading the system. That's why it's important to scale the signal by some factor less than 1.0 (with the [*~](https://docs.cycling74.com/reference/*~/ "*~") objects and the ‘Feedback’ [number box](https://docs.cycling74.com/reference/number/) objects) before feeding it back into the delay line. Otherwise the delayed sound will continue indefinitely and even increase as it is added to the new incoming audio.
## Controlling amplitude: normalize~
Since this patch contains user-variable level settings (notably the feedback levels) and since we don't know what sound will be coming into the patch, we can't really predict how we will need to scale the final output level. If we had used a [*~](https://docs.cycling74.com/reference/*~/ "*~") object just before the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") to scale the output amplitude, we could set the output level, but if we later increase the feedback levels, the output amplitude could become excessive. The [normalize~](https://docs.cycling74.com/reference/normalize~/ "normalize~") object is good for handling such unpredictable situations.
The [normalize~](https://docs.cycling74.com/reference/normalize~/ "normalize~") object allows you to specify a peak (maximum) amplitude that you want sent out its outlet. It looks at the peak amplitude of its input, and calculates the factor by which it must scale the signal in order to keep the peak amplitude at the specified maximum. So, with [normalize~](https://docs.cycling74.com/reference/normalize~/ "normalize~") the peak amplitude of the output will never exceed the specified maximum.
![](https://docs.cycling74.com/images/de5d1bbd6d3293d12ac6e4878da741d7_502.webp) normalize~ sends out the current input * peak output / peak input
One potential drawback of [normalize~](https://docs.cycling74.com/reference/normalize~/ "normalize~") is that a single loud peak in the input signal can cause [normalize~](https://docs.cycling74.com/reference/normalize~/ "normalize~") to scale the entire signal way down, even if the rest of the input signal is very soft. You can give [normalize~](https://docs.cycling74.com/reference/normalize~/ "normalize~") a new peak input value to use, by sending a number or a `reset` message in the left inlet.
  * Turn audio off and close the Patcher window before proceeding to the next chapter.


## Summary
One way to make multiple delayed versions of a signal is to feed the output of [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") back into the input of [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~"), in addition to sending it to the DAC. Because the fed back delayed signal will be added to the current incoming signal at the inlet of [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~"), it's a good idea to reduce the output of [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") before feeding it back to [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~").
In a patch involving addition of signals with varying amplitudes, it's often difficult to predict the amplitude of the summed signal that will go to the DAC. One way to control the amplitude of a signal is with [normalize~](https://docs.cycling74.com/reference/normalize~/ "normalize~"), which uses the peak amplitude of an incoming signal to calculate how much it should reduce the amplitude before sending the signal out.
## See Also
  * [normalize~ - Scale on the basis of maximum amplitude](https://docs.cycling74.com/reference/normalize~/)
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
