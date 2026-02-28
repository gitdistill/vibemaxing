---
description: Metering MSP audio within the patcher
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/14_analysischapter01/
title: Signals and Meters
---

Download Series Content and Patchers
# MSP Analysis Tutorial 1: Signals and Meters
This chapter demonstrates several MSP objects for observing the numerical value of signals and translating those values into Max messages.
## Display the value of a signal: [number~](https://docs.cycling74.com/reference/number~/ "number~")
  * Turn audio on and send some sound into the input jacks of the computer.


Every 250 milliseconds the [number~](https://docs.cycling74.com/reference/number~/ "number~") objects at the top of the Patcher display the current value of the signal coming in each channel, and the [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") objects show a graphic representation of the peak amplitude value in the past 250 milliseconds, like an analog LED display.
![](https://docs.cycling74.com/images/24fa0b95e594801e35438ffc8bad0d13_227.webp)
_Current signal value is shown by number~; peak amplitude is shown by meter~_
The signal coming into [number~](https://docs.cycling74.com/reference/number~/ "number~") is sent out its right outlet as a `float` once every time it's displayed. This means it is possible to sample the signal value and send it as a message to other Max objects.
The [number~](https://docs.cycling74.com/reference/number~/ "number~") object is actually like two objects in one. In addition to receiving signal values and sending them out the right outlet as a `float`, [number~](https://docs.cycling74.com/reference/number~/ "number~") also functions as a floating-point [number box](https://docs.cycling74.com/reference/number/) that sends a `signal` (instead of a `float`) out its left outlet.
  * Move the mod wheel of your MIDI keyboard or drag on the right side of the [number~](https://docs.cycling74.com/reference/number~/ "number~") marked ‘Amplitude’. This sets the value of the signal being sent out the [number~](https://docs.cycling74.com/reference/number~/ "number~") object's left outlet. The signal is connected to the right inlet of two [*~](https://docs.cycling74.com/reference/*~/ "*~") objects, to control the amplitude of the signal sent to the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~").

![](https://docs.cycling74.com/images/1a6d4c8ea71c148edea8712a332203f0_252.webp)
_float input to number~ sets the value of the signal sent out the left outlet_
A [number~](https://docs.cycling74.com/reference/number~/ "number~") object simultaneously converts any signal it receives into `float` s sent out the right outlet, and converts any `float` it receives into a signal sent out the left outlet. Although it can perform both tasks at the same time, it can only display one value at a time. The value displayed by [number~](https://docs.cycling74.com/reference/number~/ "number~") depends on which _display mode_ it is in. When a small waveform appears in the left part of the [number~](https://docs.cycling74.com/reference/number~/ "number~"), it is in _Signal Output Mode_ , and shows the value of the signal going out the left outlet.
![](https://docs.cycling74.com/images/7d07ce6b45904713ebf7935ece25f089_504.webp)
_The two display modes of number~_
You can restrict [number~](https://docs.cycling74.com/reference/number~/ "number~") to one display mode or the other by selecting the object in an unlocked Patcher and choosing **Get Info...** from the Object menu.
![](https://docs.cycling74.com/images/287a9cbb61a02761c99226896b3aca33_491.webp)
_Allowed display modes can be chosen in the number~ Inspector_
At least one display mode must be checked. By default, both display modes are allowed, as shown in the above example. If both display modes are allowed, you can switch from one display mode to the other in a locked Patcher by clicking on the left side of the [number~](https://docs.cycling74.com/reference/number~/ "number~"). The output of [number~](https://docs.cycling74.com/reference/number~/ "number~") continues regardless of what display mode it's in.
In the tutorial patch you can see the two display modes of [number~](https://docs.cycling74.com/reference/number~/ "number~"). The [number~](https://docs.cycling74.com/reference/number~/ "number~") objects at the top of the Patcher window are in _Signal Monitor Mode_ because we are using them to show the value of the incoming signal. The ‘Amplitude’ [number~](https://docs.cycling74.com/reference/number~/ "number~") is in _Signal Output Mode_ because we are using it to send a signal and we want to see the value of that signal. (New values can be entered into a [number~](https://docs.cycling74.com/reference/number~/ "number~") by typing or by dragging with the mouse only when it is in _Signal Output_ display mode.) Since each of these [number~](https://docs.cycling74.com/reference/number~/ "number~") objects is serving only one function, each has been restricted to only one display mode in the Inspector window.
  * Click on the left side of the [number~](https://docs.cycling74.com/reference/number~/ "number~") objects. They don't change display mode because they have been restricted to one mode or the other in the Inspector window.


## Interpolation with [number~](https://docs.cycling74.com/reference/number~/ "number~")
The [number~](https://docs.cycling74.com/reference/number~/ "number~") object has an additional useful feature. It can be made to interpolate between input values to generate a ramp signal much like the [line~](https://docs.cycling74.com/reference/line~/ "line~") object. If [number~](https://docs.cycling74.com/reference/number~/ "number~") receives a non-zero number in its right inlet, it uses that number as an amount of time, in milliseconds, to interpolate linearly to the new value whenever it receives a number in the left inlet. This is equivalent to sending a list to [line~](https://docs.cycling74.com/reference/line~/ "line~").
![](https://docs.cycling74.com/images/8db6d2a6868d6f7f4356235a315099ab_490.webp)
_number~ can send a linear ramp signal from its old value to a new value_
Unlike [line~](https://docs.cycling74.com/reference/line~/ "line~"), however, [number~](https://docs.cycling74.com/reference/number~/ "number~") does not need to receive the interpolation time value more than once; it remembers the interpolation time and uses it for each new number received in the left inlet. This feature is used for the ‘Amplitude’ [number~](https://docs.cycling74.com/reference/number~/ "number~") so that it won't cause discontinuous changes of amplitude in the output signal.
## Peak amplitude: [meter~](https://docs.cycling74.com/reference/meter~/ "meter~")
The [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") object periodically displays the peak amplitude it has received since the last display. At the same time it also sends the peak signal value out its outlet as a `float`. The output value is always a positive number, even if the peak value was negative.
![](https://docs.cycling74.com/images/3846d48d278b977c7815b3364070a63c_341.webp)
_meter~ displays the peak signal amplitude and sends it out as a float_
[meter~](https://docs.cycling74.com/reference/meter~/ "meter~") is useful for observing the peak amplitude of a signal (unlike [number~](https://docs.cycling74.com/reference/number~/ "number~"), which displays and sends out the _instantaneous_ amplitude of the signal). Since [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") is intended for audio signals, it expects to receive a signal in the range -1 to 1. If that range is exceeded, [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") displays a red ‘clipping’ LED as its maximum.
  * If you want to see the clipping display, increase the amplitude of the output signal until it exceeds 1. (Then return it to a desirable level.)


The default interval of time between the display updates of [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") is 250 milliseconds, but the display interval can be altered with the `interval` message. A shorter display interval makes the LED display more accurate, while a longer interval gives you more time to read its visual and numerical output.
  * You can try out different display intervals by changing the number in the [number box](https://docs.cycling74.com/reference/number/) marked ‘Display Interval’ in the lower left corner of the Patcher window.


By the way, the display interval of a [number~](https://docs.cycling74.com/reference/number~/ "number~") object can be set in the same manner (as well as via its Inspector window).
## Signal Probing
You don't have to include [number~](https://docs.cycling74.com/reference/number~/ "number~") and [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") objects in your patch unless they are needed for the user interface. You can measure any audio signal at any time with the signal probe feature.
  * Check `Probing` in the `Debug` menu


Now when audio is on you can point the mouse at an audio patchcord and see a balloon with a signal measurement and a meter display. This allows you to check the health of the signal anywhere in the patch.
![](https://docs.cycling74.com/images/dd0a1768a008e3cbafb4bc70248bb303_110.webp)
Probing for Signals
## Use a signal to generate Max messages: [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~")
The [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") object sends out the current value of a signal, as does the right inlet of [number~](https://docs.cycling74.com/reference/number~/ "number~"). With [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~"), though, you can turn the output on and off, or request output of a single value by sending it a `bang`. When you send a non-zero number in the right inlet, [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") uses that number as a millisecond time interval, and begins periodically reporting the value of the signal in its left inlet. Sending in a time interval of `0` stops [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~").
This right half of the tutorial patch shows a simple example of how a signal waveform might be used to generate MIDI data. We'll sample a sub-audio cosine wave to obtain pitch values for MIDI note messages.
  * Use the [number~](https://docs.cycling74.com/reference/number~/ "number~") to set the output amplitude to `0`. In the [number box](https://docs.cycling74.com/reference/number/) objects at the top of the patch, set the ‘Rate’ number box to `0.14` and set the ‘Depth’ [number box](https://docs.cycling74.com/reference/number/) to `0.5`. Click on the message box `200` to start [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") reporting signal values every fifth of a second.


Because [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") is reporting the signal value every fifth of a second, and the period of the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object is about 7 seconds, the melody will describe one cycle of a sinusoidal wave every 35 notes. Since the amplitude of the wave is 0.5, the melody will range from 36 to 84 (60±24).
  * Experiment with different ‘Rate’ and ‘Depth’ values for the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~"). Since [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") is sampling at a rate of 5 Hz (once every 200 ms), its Nyquist rate is 2.5 Hz, so that limits the effective frequency of the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") (any greater frequency will be ‘folded over’). Click on the `0`[message](https://docs.cycling74.com/reference/message/ "message") box to stop [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~").


## Amplitude modulation
  * Set the tremolo depth to `0.5` and the tremolo rate to `4`. Increase the output amplitude to a desirable listening level.


The [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object is modulating the amplitude of the incoming sound with a 4 Hz tremolo.
  * Experiment with faster (audio range) rates of modulation to hear the timbral effect of amplitude modulation. To hear ring modulation, set the modulation depth to 1. To remove the modulation effect, simply set the depth to 0.


## View a signal excerpt: [capture~](https://docs.cycling74.com/reference/capture~/ "capture~")
The [capture~](https://docs.cycling74.com/reference/capture~/ "capture~") object is comparable to the Max object [capture](https://docs.cycling74.com/reference/capture/ "capture"). It stores many signal values (the most recently received 4096 samples, by default), so that you can view an entire excerpt of a signal as text.
  * Set the tremolo depth to 1, and set the tremolo rate to 172. Double-click on the [capture~](https://docs.cycling74.com/reference/capture~/ "capture~") object to open a text window containing the last 4096 samples.


This object is useful for seeing precisely what has occurred in a signal over time. (4096 samples is about 93 milliseconds at a sampling rate of 44.1 kHz.) You can type in an argument to specify how many samples you want to view, and [capture~](https://docs.cycling74.com/reference/capture~/ "capture~") will store that many samples (assuming there is enough RAM available in Max. There are various arguments and messages for controlling exactly what will be stored by [capture~](https://docs.cycling74.com/reference/capture~/ "capture~"). See its description in the MSP Reference Manual for details.
## Summary
The [capture~](https://docs.cycling74.com/reference/capture~/ "capture~") object stores a short excerpt of a signal to be viewed as text. The [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") object periodically displays the peak level of a signal and sends the peak level out its outlet as a `float`. The [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") object sends out a `float` to report the current value of a signal. [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") reports the signal value once when it receives a `bang`, and it can also report the signal value periodically if it receives a non-zero interval time in its right inlet.
The [number~](https://docs.cycling74.com/reference/number~/ "number~") object is like a combination of a `float`[number box](https://docs.cycling74.com/reference/number/), [sig~](https://docs.cycling74.com/reference/sig~/ "sig~"), and [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~"), all at once. A signal received in its left inlet is sent out the right outlet as a `float`, as with [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~"). A `float` or `int` received in its left inlet sets the value of the signal going out its left outlet, as with [sig~](https://docs.cycling74.com/reference/sig~/ "sig~"). Both of these activities can go on at once in the same [number~](https://docs.cycling74.com/reference/number~/ "number~") object, although [number~](https://docs.cycling74.com/reference/number~/ "number~") can only _display_ one value at a time. When [number~](https://docs.cycling74.com/reference/number~/ "number~") is in _Signal Output Mode_ , it displays the value of the outgoing signal.
[number~](https://docs.cycling74.com/reference/number~/ "number~") can also function as a signal ramp generator, like the [line~](https://docs.cycling74.com/reference/line~/ "line~") object. If a non-zero number has been received in the right inlet (representing interpolation time in milliseconds), whenever [number~](https://docs.cycling74.com/reference/number~/ "number~") receives a `float`, its output signal interpolates linearly between the old and new values.
These objects (along with a few others such as [sig~](https://docs.cycling74.com/reference/sig~/ "sig~")[floating-point number box](https://docs.cycling74.com/reference/flonum/) and [avg~](https://docs.cycling74.com/reference/avg~/ "avg~")) comprise the primary links between MSP and Max. They convert signals to numerical Max messages, or vice versa.
## See Also
  * [capture~ - Store a signal to view as text](https://docs.cycling74.com/reference/capture~/)
  * [meter~ - Visual peak level indicator](https://docs.cycling74.com/reference/meter~/)
  * [number~ - Signal monitor and constant generator](https://docs.cycling74.com/reference/number~/)
  * [snapshot~ - Convert signal values to numbers](https://docs.cycling74.com/reference/snapshot~/)



Kind
    Tutorial 

Categories
    Audio     Analysis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
