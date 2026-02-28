---
description: Creating networks of filters
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/08_filterchapter05/
title: Parallel and serial filters
---

Download Series Content and Patchers
# Filter Tutorial 5: Parallel Filters
In this tutorial, we'll look at creating _networks_ of filters to make complex, time-varying timbres using an oscillator input.
## The impulse
Look at the tutorial patch. It contains a few sound-producing objects connected to a network of filter objects: three [reson~](https://docs.cycling74.com/reference/reson~/ "reson~") objects in parallel and a [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") object in series with their outputs. The audio input for the filter network comes from a [receive~](https://docs.cycling74.com/reference/receive~/ "receive~") object named `filterin`, allowing us to generate signals for our filters remotely.
  * Start the audio in the tutorial patcher. At the bottom of the patcher, adjust the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Dry Volume'. In the area of the patcher labeled `1`, click the [button](https://docs.cycling74.com/reference/button/ "button") attached to the [click~](https://docs.cycling74.com/reference/click~/ "click~") object. As per its name, you should hear a click!


The [click~](https://docs.cycling74.com/reference/click~/ "click~") object generates a constant signal of `0`. When you sent it a `bang` message, it outputs a _single sample_ of value `1`, then returns to sending `0` 's. This is called an _impulse_ , and in an ideal world generates an even spread of energy across all frequencies; we could think of it as the shortest possible burst of white noise we can create in our digital system. Sending a click through a filter returns a sound that has the exact frequency characteristics of that filter. We call this taking the _impulse response_ of a signal chain.
  * Click on a note in the [kslider](https://docs.cycling74.com/reference/kslider/ "kslider") object at the top of the tutorial patcher in the area labeled `2`. You should hear a sawtooth wave fade in and out with a smooth envelope.


The [saw~](https://docs.cycling74.com/reference/saw~/ "saw~") object in our patcher is in a signal chain where it has an envelope (controlled by a [function](https://docs.cycling74.com/reference/function/ "function"), a [line~](https://docs.cycling74.com/reference/line~/ "line~"), and a [*~](https://docs.cycling74.com/reference/*~/ "*~") object). If we adjust the [function](https://docs.cycling74.com/reference/function/ "function") object, we can change the shape of the note that gets fired each time we click on a key in the [kslider](https://docs.cycling74.com/reference/kslider/ "kslider") object.
## A network of filters
  * Turn down the 'Dry Volume' and turn up the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Filtered Volume' at the bottom of the patcher. In the patcher area labeled `3`, click in the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Vowel'. Enter `0` in the [number](https://docs.cycling74.com/reference/number/ "number") box and hit return. The[number box](https://docs.cycling74.com/reference/number/) objects connected to the [line~](https://docs.cycling74.com/reference/line~/ "line~") objects below should read `270., 2290., and 3010.`. Click on the [kslider](https://docs.cycling74.com/reference/kslider/ "kslider") to play some notes. Click in the 'Vowel' [number](https://docs.cycling74.com/reference/number/ "number") box and enter different values between `0` and `9` and listen to the results. Double-click the [coll](https://docs.cycling74.com/reference/coll/ "coll") object named `formants` and look at the contents.


The [coll](https://docs.cycling74.com/reference/coll/ "coll") object in our patcher contains ten lists of frequency values which correspond to the average _formats_ for vowels in the English language ("ooo", "eee", "ah", etc.). In human speech, our lungs project air through our vocal chords, which modulate the air pressure into a regular waveform. Our mouth shapes this waveform, filtering the signal based on the shape of our mouth. These vocalizations can be modeled as sets of three bandpass filters tuned to different frequencies, creating a simalcrum of the sound our voice makes. The shaping of a sound in this manner is called _formant_ filtering, and can be created in MSP using the circuit in our tutorial patcher.
  * In the lower-right of the tutorial patcher, adjust the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Q' to `30.`. Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box attached to the [metro](https://docs.cycling74.com/reference/metro/ "metro") object above labeled `Random?`. Play some notes on the [kslider](https://docs.cycling74.com/reference/kslider/ "kslider").


Tightening the Q on our format filters makes the sound more obviously 'vocal', as the resonation of the filters cuts out any extraneous energy from our sawtooth waveform.
  * In the patcher area labeled `4`, adjust the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Cutoff frequency' to `5000`. Play some notes. Adjust it down to something low, like `200`.


The output of our formant filters feed into a lowpass filter controlled by a [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") object. This cuts the treble from our sawtooth after it passes through the bandpass network of the [reson~](https://docs.cycling74.com/reference/reson~/ "reson~") objects. Changing this value also changes the quality of the vocal model.
  * Adjust the values of the patcher to experiment with different ways to create a 'singing voice' out of a sawtooth wave and a filter network. The [line~](https://docs.cycling74.com/reference/line~/ "line~") objects in the patcher attached to the filters control the interpolation between settings. If you unlock the patcher and change the second value in the [message](https://docs.cycling74.com/reference/message/ "message") boxes, you can make the transitions smoother or more abrubt. Using the [click~](https://docs.cycling74.com/reference/click~/ "click~") object, see how the different filter settings sound when driven by an impulse.


## Summary
The filter objects in MSP can be connected into networks of filters that can be used in all manner of interesting ways. Bandpass filters (such as [reson~](https://docs.cycling74.com/reference/reson~/ "reson~")) can be used in parallel to simulate the 'formants' of instruments or human speech. The [click~](https://docs.cycling74.com/reference/click~/ "click~") object allows you to test the _impulse response_ of a filter network by sending a single positive sample through it, generating a pure impression of the frequency response of the filter.
## See Also
  * [click~ - Create an impulse](https://docs.cycling74.com/reference/click~/)



Kind
    Tutorial 

Categories
    Audio     Synthesis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
