---
description: Using audio waveshaping for signal distortion
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/09_dynamicschapter03/
title: Distortion
---

Download Series Content and Patchers
# Dynamics Tutorial 3: Distortion
In this tutorial, we'll look at the use of _waveshaping_ to modify an input signal, simulating the distortion present in overdriven amplifiers. In the realm of analogue audio, all amplifiers introduce some form of distortion into the signal. The ability to creatively harness this by deliberately overdriving distortion circuits is difficult to simulate in a digital audio environment, as the natural artifacts and nonlinearities that render tube and transistor amplifier distortion so interesting are absent in the digital signal path. One way to overcome this is to simulate the distortion caused by amplifiers by using lookup tables to change the dynamic response of an input signal. Unlike the previous tutorials, which look at dynamics from a macro- (or envelope) perspective, this tutorial looks at sound amplitudes on a sample-by-sample basis.
A review of the tutorial that covers[waveshaping synthesis](https://docs.cycling74.com/learn/articles/07_samplingchapter05/)may be useful to understand how the [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object works in MSP.
## Splitting bands
One of the attributes of cool-sounding distortion circuits is that they are _frequency-dependent_ as well as _amplitude-dependent_ in their behavior; that is to say, the way in which they shape an input signal depends not only on how loud the sound comes in, but also the frequency components in that sound. Some distortion circuits process high frequencies far more harshly than bass frequencies; some distort a narrow range of frequencies in the mid-range and leave high sounds relatively pure. In order to simulate this, we create an MSP signal chain that splits our input signal into three bands for low, medium, and high frequencies.
  * Take a look at the tutorial patcher. Start the audio by clicking the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") and turn on the [metro](https://docs.cycling74.com/reference/metro/ "metro") object labeled '1)' by clicking the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object. There are three [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") sliders at the bottom of the patch. Raise these each in turn, and you should hear a random sequence of vibraphone notes, with the first [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider controlling the bass, the second controlling the mid-range, and the third controlling the high frequencies.


The state-variable ([svf~](https://docs.cycling74.com/reference/svf~/ "svf~") --- colored red) object in our patcher takes the output of our sample playback logic and applies four filters to the signal simultaneously: a lowpass filter (output from the left outlet), a highpass filter (output from the second outlet), a bandpass filter (output from the third outlet), and a bandreject or notch filter (output form the last outlet). We're only interested in the first three, which roughly correspond to the bass, middle, and treble of our input signal.
## Applying distortion
  * Turn down all but the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider controlling the low frequencies. On the right of the tutorial patcher, draw in the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object labeled 'Low'. Start by manually retracing the shape that's already in there (a diagonal line running from bottom to top). Notice that even the slightest deviation changes the sound and adds noise. Try drawing a zig-zag shape across the waveform:

![](https://docs.cycling74.com/images/696c6d94dfe5b95fca0a8673b6bb9196_227.webp) A freehand waveshape
A transfer function with multiple zero-crossing points will have the result of adding additional harmonics to any relatively periodic waveform. In amplifier distortion, this is an important component of the 'warm' effect of tube amplification.
  * Click the [button](https://docs.cycling74.com/reference/button/ "button") object labeled 'Reset' under the 'Low' [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~"). The sound (and the shape) should return to normal. Turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider representing the mid-range frequencies. In the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object labeled 'Mid', draw a diagonal slash across the middle of the waveform:

![](https://docs.cycling74.com/images/9e68e424d04db3d1b4acaf1f5e3da32b_212.webp) Distortion around zero-crossings
Notice how the mid-range now has a harsh overdriven sound to it. What we've done in drawing that shape is introduce a set of additional zero-crossings around the normal zero point in the waveform. The result of this will be nonlinearities in the mid-range signal whenever its sample amplitude comes close to zero. This simulates the properties of many solid state transistor distortion circuits (such as guitar pedals), which 'kink' the signal at specific intervals to generate high harmonics from the signal.
  * 'Reset' the 'Mid' waveshape by clicking the [button](https://docs.cycling74.com/reference/button/ "button"), and turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider representing the high frequencies. Draw a series of sharp peaks along the waveform opposite from the normal curve:

![](https://docs.cycling74.com/images/d8a3779098b6cce213278b228046f91b_217.webp) Introducing random non-linearities
This type of waveshape creates a harsh distortion similar to the way digital distortion effects work. By introducing noise (random activity) into the waveshape, we create the potential for completely arbitrary distortion effects that resemble less an amplifier circuit than a 'digital' effects process.
## Resetting and smoothing
  * Double-click any one of the [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") objects that are triggered by the 'Reset' [button](https://docs.cycling74.com/reference/button/ "button") objects (`resetlow, resetmid, resethi`). Look at the contents of the subpatch.


The MSP [peek~](https://docs.cycling74.com/reference/peek~/ "peek~") object, you may recall, allows us to programmatically fill [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") objects with samples according to patcher logic in Max. The [uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object, when it receives a `bang`, sets up a chain of `8192` events that fill the appropriate [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object with an ascending ramp of values from `-1` to `1`. When the [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object uses this curve, the incoming signal gets passed unchanged.
  * Close this patcher and open any of the [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") objects that are triggered by the 'Smooth' [button](https://docs.cycling74.com/reference/button/ "button") objects (`smoothlow, smoothmid, smoothhi`)


The smoothing subpatches, which are triggered whenever you release the mouse from drawing in the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object, triggers an [uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object that takes each sample currently in the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") and averages it with its previous sample, creating a smoother curve than would be possible by freehand drawing.
  * Close the subpatch, and unlock the main tutorial patcher. Disconnect the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") objects from the [zl](https://docs.cycling74.com/reference/zl/ "zl") objects below them. Lock the patcher and draw some curves. You'll find that the distortion effects you create are much much more pronounced. If you want to, click the [button](https://docs.cycling74.com/reference/button/ "button") objects that smooth the shapes manually. The more you click them, the more averaged out our waveshapes become.
  * In the middle of the tutorial patcher, click the [message](https://docs.cycling74.com/reference/message/ "message") box that reads `replace bass.aiff`. Now the sound generated by our sampler will be that of an electric bass guitar. Play with the different waveshaping techniques we looked at earlier. If you like, modify the `Cutoff frequency` of the [svf~](https://docs.cycling74.com/reference/svf~/ "svf~") object with the [number](https://docs.cycling74.com/reference/number/ "number") box in the middle of the patcher. This will let you choose where the midrange distortion effect is most prominent.


## Summary
Waveshaping is an exciting synthesis technique that allows you to create complex timbres by running an oscillator through a lookup table; when used as a signal-processing technique with complex audio input, it can be used to simulate all manner of distortion effects. Because real-life amplifier distortion changes depending on the frequency content of the input signal, one way to simulate this distortion is to split an audio signal into several frequency bands and waveshape each one independently. While it's possible to scientifically measure and model the responses of different distortion circuits, freehand drawing in the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object allows us to experiment with different curves and hear them directly. 

Kind
    Tutorial 

Categories
    Audio     Synthesis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
