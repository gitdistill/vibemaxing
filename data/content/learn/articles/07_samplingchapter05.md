---
description: Using sample data as a lookup table
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/07_samplingchapter05/
title: Waveshaping Synthesis
---

Download Series Content and Patchers
# Synthesis Tutorial 5: Waveshaping
In this tutorial, we'll look at a latent (but very useful) attribute of samples, which is that they can be used as lookup tables to transform the shape of other waveforms. This process is called _waveshaping_ , and is used in synthesis to generate complex spectra from a sinusoidal input. It's also the basic signal processing technique behind many types of amplitude-dependent distortion, and can be used to model the non-linearities of different kinds of amplifier.
## Using a stored wavetable as a transfer function
Take a look at the tutorial patcher. The basic sound-generating circuit in the upper-left of the patcher should look familiar, with one new object ([lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~")) inserted into the chain. We have a [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object going through an amplifier ([*~](https://docs.cycling74.com/reference/*~/ "*~")) to the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~").
  * Turn on the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") object and adjust the [number](https://docs.cycling74.com/reference/number/ "number") box labeled `amplitude`. You should hear a sine wave at `220` Hz.


The new object in this signal chain at first seems to be doing nothing, and in terms of what we hear, it isn't... yet. The [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object interprets a piece of sample memory stored in a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object as a _transfer function_ , with the beginning of the sample used representing input values of `-1` and the end of the sample used representing values of `1.` Incoming values are scaled across this _X_ axis, and the resulting audio comes from the corresponding values along the _Y_ axis.
In our patch, the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") named `waveform` is serving as a _lookup table_ (or transfer function) for the incoming sine wave. When the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object generates a `-1`, for example, _whatever sample value_ is at the beginning of the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") comes out of the [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object. When our [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") hits `1`, the [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object reads from the end of the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") to find its outgoing sample.
  * Double-click the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object at the bottom of the tutorial patcher. Notice that the waveform loaded in is a simple ramp. Because our waveshape (the sample in the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") is a linear ramp with the beginning of the sample at `-1` and the end at `1`, our [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object sounds unchanged.


The [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object takes three possible arguments: the first is the name of the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") to use as its waveshape; the second and third are the start and end points (in _samples_ to use within the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") as the boundaries of the transfer function. Because we want our [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") to be exactly `512` samples long in our patcher, we created it with the argument of `10.66667` milliseconds. How did we get this number. At the right of the patcher, you can see the [sampstoms~](https://docs.cycling74.com/reference/sampstoms~/ "sampstoms~") object, which allows us to convert from samples to milliseconds.
## The [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object
Look at the graphical object at the top of the tutorial patcher. Notice that it contains the same shape that is loaded into our [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"). The [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object allows us to view, select regions of, and directly modify the contents of a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") with a drawing tool.
  * Using your mouse, doodle in the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object's display. Notice how different shapes affect the output sound. Try drawing smooth curves, then jagged ones, then ones with lots of plateaus (straight horizontal lines). Notice that even slight variations in the shape have tremendous impact on the spectrum generated by the [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object.


The [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object is operating in `draw` mode, where you can literally modify a sample loaded into a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") with your mouse. Other modes allow you to select regions, the boundaries of which can be used as Max messages for other objects.
## Setting sample values with Max messages: [peek~](https://docs.cycling74.com/reference/peek~/ "peek~")
  * Click on the [button](https://docs.cycling74.com/reference/button/ "button") labeled `A` in the tutorial patcher. Our waveshape (and our sound) should return to normal.


The way we got the default waveshape in our tutorial patcher is through the logic controlled by the [uzi](https://docs.cycling74.com/reference/uzi/ "uzi") below the [button](https://docs.cycling74.com/reference/button/ "button") labeled `A`. The [uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object, you may recall, generates a lot of data instantly depending on its argument. The right outlet of the object generates a numeric ramp from `1` to its argument. We've subtracted `1` from that value to generate a stream of Max numbers from `0` to `511` when you click the [button](https://docs.cycling74.com/reference/button/ "button"). These numbers are then sent to the middle and left inlets of a [peek~](https://docs.cycling74.com/reference/peek~/ "peek~") object. The middle inlet receives a number that has been scaled into the range of `-1` to `1` (via the [scale](https://docs.cycling74.com/reference/scale/ "scale") object), then the left inlet receives the number unchanged. The [peek~](https://docs.cycling74.com/reference/peek~/ "peek~") object allows us to manually set the sample values within a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") via Max messages. The left inlet (which is "hot", and actually performs the operation) sets _which_ sample we're changing to the most recent value received by the middle inlet. In section `A`, the [uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object generates a stream of numbers that fill our entire [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") with an ascending ramp, e.g. 
Sample Value 0 -1. 1 -0.996086 2 -0.992172 3 -0.988258 4 -0.984344 5 -0.980431 ... 508 0.988258 509 0.992172 510 0.996086 511 1.
## For the math geeks in the room
  * Click on the other [button](https://docs.cycling74.com/reference/button/ "button") objects in the patcher (labeled `B`, `C`, and `D`). Notice how the waveshape in the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") changes, and note how it affects the sound. Each waveshape seems to _multiply_ the frequency of the sound generated by the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object. The logic at `B` makes our `220` Hz wave sound at `440`, `C` at `660`, and `D` at `880`.


The equations that the [expr](https://docs.cycling74.com/reference/expr/ "expr") objects are doing in these parts of the patch generate special types of transfer functions called _Chebyshev polynomials_. These functions are interesting in that they have the ability to transform sinusoidal input to different harmonic multiples. The four Chebyshev polynomials in our tutorial are:
y = x ([uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object `A`, leaves the input unchanged) y = 2*x^2-1 ([uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object `B`, doubles the frequency) y = 4*x^3-3*x ([uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object `C`, triples the frequency) y = 8*x^4-8*x^3+1 ([uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object `D`, quadruples the frequency)
In practice, what they do looks like this:
![](https://docs.cycling74.com/images/fb4e76373fa999079c8aa7bc0db24aea_558.webp) Our four Chebyshev polynomials and their effect on a cosine input
  * Click on the `read` messages in patcher area `E`. These will load 512-sample audio files into our waveshape [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"). Notice their effect on the sound:

![](https://docs.cycling74.com/images/3318494f10a15ee252206f508063f7d8_558.webp) Waveshaping through gtr512.aiff and blp512.aiff, respectively.
  * Now that you know a bit more about the expected behavior of the waveshaping distortion, return to drawing in the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object to see what kind of results you can achieve.


## Summary
The [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object allows you to use a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") as a transfer function to perform a process called _waveshaping_ on an input sound. Different shapes cause different distortions of the spectra and can create very complex timbres. The [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object allows you to directly view and modify the contents of an MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") using your mouse, and the [peek~](https://docs.cycling74.com/reference/peek~/ "peek~") object allows you to set sample values programmatically with Max messages. Some transfer functions (such as Chebyshev polynomials) have special properties when used as a waveshaping function on a sinusoidal input.
## See Also
  * [lookup~ - Transfer function lookup table](https://docs.cycling74.com/reference/lookup~/)
  * [waveform~ - buffer~ viewer and editor](https://docs.cycling74.com/reference/waveform~/)
  * [peek~ - Read and write sample values](https://docs.cycling74.com/reference/peek~/)
  * [sampstoms~ - Convert time from samples to milliseconds](https://docs.cycling74.com/reference/sampstoms~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
