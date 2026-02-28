---
description: Working with more than two audio outputs in MSP
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/13_panningchapter03/
title: Multi-channel panning
---

Download Series Content and Patchers
# MSP panning Tutorial 3: Multi-channel panning
This tutorial discusses panning around four channels and blendiing four sound sources.
## Panning in Quad
Even though "Quad Sound" went out of style in the '80s, there are still many situations where sound needs to be distributed to four locations. For instance, four of the six signals in 5.1 movie soundtracks are located in the four corners of the theater. (The other two being dialog center and low frequency effects). The preferred controller for four channel panning is a joystick or a two dimensional control such as [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider").
  * Open the `Quad_pan` subpatcher and start the window audio.


If you don't have a four channel listening environment, you should open `Audio Status` in the Options menu and select _I/O Mappings_. Route channel 3 to output 1 and channel 4 to output 2.
The signal_source subpatch has three sources in it—a simple tone generator, a short audio file, and an [adc~](https://docs.cycling74.com/reference/adc~/ "adc~") object so you can apply your own test signal. You can choose the source with a [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") and use the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") to start the tone generator and audio file. The output of this patch is a four channel [dac~](https://docs.cycling74.com/reference/dac~/ "dac~"), but since four channel listening environments are not all that common, channels 3 and 4 are piped through [cverb~](https://docs.cycling74.com/reference/cverb~/ "cverb~") objects so they will have a distinct (somewhat distant) sound in stereo.
  * Select the `tones` option in the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") and set the toggle to start playing.


Begin exploring the patch by moving the circle in the [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") left and right while keeping it at the bottom of the frame. The pan function is linear, derived by scaling the [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") X output to 0-1 and taking the square root. This is the same as the `pow($f1, 0.5)` formula shown in [Stereo Panning](https://docs.cycling74.com/learn/articles/13_panningchapter02/). As before, the value derived is applied to the right channel and and `pow((1-$f1), 0.5)` is applied to the left channel. But there is a twist, as you can see by moving the circle up in the [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider"). Both values are multiplied by similar values derived from the Y axis. The result of this is the sound is also panned forward and back. Each of the four channels is controlled by some combination of X and Y or 1-X and 1-Y. The colors in the patch should make the control pathways easy to follow. Note that the Y values are attached to the right inlet of each [*~](https://docs.cycling74.com/reference/*~/ "*~") object and must be accompanied by `bangs` to update the calculation when they change.
## Stereo to quad
Now try the music example with the play option. Note that these are mono signals (left channel only). To inject a stereo signal into a quad space, you need to combine a balance control with the front to back panning. This is shown in the `Stereo_quad_pan` subpatch. When you open it up, it should look familiar. All we had to do was include a stereo signal souorce and route the left and right channels as shown. I also changed to a 4.5 dB panning law for left and right, but that is optional. (Again, see [Stereo Panning](https://docs.cycling74.com/learn/articles/13_panningchapter02/).) This kind of circuit is found in many automobile sound systems.
## Mixing four sources
Two dimensional controls are also found in some synthesizers where they are used to blend waveforms, a technique called _vector synthesis_ or _morphing_ depending on the nature of the signals. The `Quad_mix` subpatch contains an instrument that works in this way. The heart of the patch is the same set of calculations used above, although they have been encapsulated into the `Quad_level_control` subpatch here. The new part of the patch is a simple beep instrument with a possibility of four waveforms blended by the [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") object. You can set the duration of the notes to explore the effect of moving the control while a note plays.
## Summary
This tutorial demonstrates the principles of working with four channel sound, either distributing sound to four separate speakers or combining sounds from four sources. The main control used is the [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") object, which is the Max version of a joystick.
## See Also
  * [pictslider -](https://docs.cycling74.com/reference/pictslider/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
