---
description: Scaling values for MIDI control of audio patchers
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/10_midichapter01/
title: Mapping MIDI to MSP
---

Download Series Content and Patchers
# MIDI Tutorial 1: Mapping MIDI to MSP
In this group of tutorials, we'll look at different strategies for integrating MIDI control into MSP patchers. Commercial hardware synthesizers and samplers typically implement MIDI in some form or another in fairly standardized ways; software systems that mimic these devices (such as Max patches) can use all the same routing and mapping systems to successfully control our sound-producing systems with MIDI controllers.
A review of the tutorials that cover[MIDI objects](https://docs.cycling74.com/learn/articles/10_midichapter01/)in Max may be useful before reading these tutorials.
  * To use the tutorial patchers in this section of the tutorial, make sure you have a correctly configured MIDI controller connected to your computer. The tutorials in this section use a variety of MIDI messages as example input; if your controller lacks any of these features, you can simulate their input with user interface objects in the tutorial.


## MIDI, Redux
The MIDI standard was developed to enable the control of electronic music devices through the use of a simple serial communications standard that would be easy to implement on any platform and could be used by anyone. As music performance equipment has evolved in the 25 years since, MIDI has remained a standard-issue interface protocol for nearly all music-making equipment, whether we're talking about hardware or software. Whether you're interested in routing a keyboard, slider box, or software sequencer in Max, you need to deal with translating MIDI messages into numbers that make sense for MSP.
  * Take a look at the tutorial patcher. The patcher logic consists of an FM synthesis abstraction called `simpleFM~` controlled by a number of signal objects, the values of which are set by floating-point [number](https://docs.cycling74.com/reference/number/ "number") boxes. Turn on the audio in the patcher and turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider. Familiarize yourself with the way the audio portion of the patcher works by trying different values is in the [number](https://docs.cycling74.com/reference/number/ "number") boxes labeled `1` through `5`.


Our patcher uses frequency modulation synthesis as we looked at earlier in the tutorials, with the addition of a circuit that provides _vibrato_ to the main frequency of the synthesizer. The [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object labeled `Vibrato rate` is scaled by the `Vibrato depth` control to oscillate the main frequency (the output of the [line~](https://docs.cycling74.com/reference/line~/ "line~") object on the right of the patcher. Unlike a vibrato circuit which _adds_ the output of a modulating oscillator to a constant frequency, this patcher logic _multiplies_ the constant frequency by the output of the oscillator treated as an exponent by the [pow~](https://docs.cycling74.com/reference/pow~/ "pow~") object. A vibrato depth of `1`, therefore, has the equivalent of turning off the vibrato (raising `1` to any power yields `1`, which leaves our main frequency untouched). A depth of `2` scales the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object to the range of `0.5` to `2.0`, scaling the main frequency up and down by an octave.
The `Octave bend` value on the left allows us to use a value as a frequency multiplier in a range where each unit of value transposes the pitch by an octave. Like the vibrato circuit, it uses an exponential scaling logic; a value of `0.` as the bend amount raises `2` to the power of `0.`, yielding a multiplier of `1.` for the frequency. An octave bend of `1.` yields a multiple of `2.`; a bend of `-1.` yields a multiple of `0.5`.
## Scaling MIDI for signal control
  * Configure a MIDI continuous controller connected to your computer so that it sends CC#1 on any MIDI channel (the modulation wheel on a keyboard controller is a good candidate for this mapping). From the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object labeled `A`, select option `1` ('Octave Pitch Bend'). Move your controller and listen to and watch the result.


The Max [ctlin](https://docs.cycling74.com/reference/ctlin/ "ctlin") object transmits our controller through the [slider](https://docs.cycling74.com/reference/slider/ "slider") object in the patcher and from there through a [scale](https://docs.cycling74.com/reference/scale/ "scale") object. The [gate](https://docs.cycling74.com/reference/gate/ "gate") object allows us to route the controller to different destination [number](https://docs.cycling74.com/reference/number/ "number") boxes in the patcher. Notice that, with the default scaling, our MIDI number range (`0` to `127`) maps to a floating-point value between `0.` and `1.`
When working with MIDI messages, the general rule of thumb is that they transmit integers which are typically in the range of `0` to `127`. While these values make sense within the MIDI domain, when applied to signal values these ranges are usually wrong. When we want to control an oscillator, we need to think in terms of _frequency_ (cycles per second or Hz), not the _pitch_ that MIDI note numbers refer to. When thinking about _amplitude_ , we might want these numbers scaled between `0.` and `1.` to control the output of a [*~](https://docs.cycling74.com/reference/*~/ "*~") object. The [scale](https://docs.cycling74.com/reference/scale/ "scale") object is an important utility object in Max for performing these calculations.
  * In the [preset](https://docs.cycling74.com/reference/preset/ "preset") object at the right of the patcher, click the first circle. The values for the [scale](https://docs.cycling74.com/reference/scale/ "scale") object should change so that the `xmin` and `xmax` values read `0` and `127`; the `ymin` and `ymax` values should read `0.` and `2.` Move the MIDI controller and notice the difference.


Using the settings controlled by this preset, we can take a MIDI controller and use it to give us an octave bend range of two octaves. Setting the controller to its lowest value will leave our FM synthesizer untransposed. Moving it all the way up will cause the frequency to output two octaves higher, at `880` Hz.
  * Click in the [number](https://docs.cycling74.com/reference/number/ "number") box labeled `ymin` and enter the value of `-2.` Move your MIDI controller and notice the difference.


The [scale](https://docs.cycling74.com/reference/scale/ "scale") object can map any range to any other range, including negative values. Now our controller leaves the synthesizer untransposed in the _middle_ of its range; moving it downwards and upwards gives us two octaves of shift in either direction.
  * Click the other [preset](https://docs.cycling74.com/reference/preset/ "preset") states available and try them out; each one contains a different mapping and routing:


  1. Octave Pitch Bend. The controller outputs values from `0.` to `2.`
  2. Vibrato Rate. The controller outputs values from `2.` to `0.`, inverting the scaling so that it runs from high to low.
  3. Vibrato Depth. The controller scales its input to run from `1.` to `100.`
  4. Modulation Index. The MIDI gets scaled from `0.` to `20.`
  5. Amplitude. The MIDI goes from `0.` to `1.` with an _exponential scaling_ factor of `1.06`. Using this value means that upper values of the MIDI range control a wider part of the mapping than lower values.


Notice that different MSP parameters in our patch require different scalings, none of which directly correspond to the default values of MIDI controllers.
  * In patcher area `B`, look at the [number](https://docs.cycling74.com/reference/number/ "number") boxes below the [notein](https://docs.cycling74.com/reference/notein/ "notein") object. Play some notes on a MIDI keyboard connected to your computer.


When dealing with pitch in MIDI values, a utility Max object called [mtof](https://docs.cycling74.com/reference/mtof/ "mtof") allows us to convert directly to frequency. The [stripnote](https://docs.cycling74.com/reference/stripnote/ "stripnote") object in this patch is necessary to prevent double-triggering of values due to the note-off events generated by the keyboard. Notice that because our MSP synth in this patch is monophonic, only one note can be sounded at a time.
## Summary
Working with MIDI controllers within the Max environment is extremely simple. Using these values with MSP patches requires an understanding of how to _map_ the MIDI values appropriately for the different parameters of a digital signal network. The Max [scale](https://docs.cycling74.com/reference/scale/ "scale") and [mtof](https://docs.cycling74.com/reference/mtof/ "mtof") objects are incredibly useful for performing this function, and allow you to map MIDI input into appropriate ranges for any number of applications.
## See Also
  * [scale - Map an input range of values to an output range](https://docs.cycling74.com/reference/scale/)
  * [mtof - Convert a MIDI note number to frequency](https://docs.cycling74.com/reference/mtof/)



Kind
    Tutorial 

Category
    MIDI 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
