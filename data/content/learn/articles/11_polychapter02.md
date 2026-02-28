---
description: Scheduled polyphonic synthesis and parallel thread allocation
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/11_polychapter02/
title: Granular synthesis
---

Download Series Content and Patchers
# Polyphony Tutorial 2: Granular Synthesis
## Granular synthesis
In this tutorial we'll look at using the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object to generate large amounts of polyphony in order to play the contents of one [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") of sample data. We'll leverage the ability of MSP to play sample data from the same [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") at multiple arbitrary speeds and time points to explore the technique of _granular synthesis_
Put simply, granular synthesis is the use of very short (or, sometimes, less short) sonic events called 'grains' to generate complex textures. While the musical and written literature on the technique is beyond the scope of this tutorial (see Curtis Roads' _Microsound_ (MIT Press: 2004) for a great exploration of this topic), we'll cover the basics here. While classic granular synthesis relies on the use of very small amounts of wavetable data, the technique we'll explore in this tutorial uses sample data taken arbitrarily from soundfiles.
In our tutorial patcher, we'll create an algorithmic playback system based on constrained random values to control the following parameters of a polyphonic sample playback engine: rate, onset point, duration, pitch, amplitude. We'll also look at how adjusting envelopes changes the sonic output.
## Experimenting with the patcher
Take a look at the tutorial patcher. There are several numbered areas, each of which controls part of our granular synthesis engine. The patcher area labeled `1` is the _grain emitter_ proper: a [metro](https://docs.cycling74.com/reference/metro/ "metro") object schedules and fires `bang` messages into a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object that has loaded 100 voices of an abstraction named `polygrain~`. Area `2` allows us to check our CPU usage depending on the parameters of our synthesizer. Area `3` and `4` set the synthesis parameters - the sample we're using, which area of it to draw from for grains, and the parameters of the grain playback system in the `polygrain~` abstraction.
  * In patcher area `1`, turn on the audio and turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider. At the top of the patcher, click the [button](https://docs.cycling74.com/reference/button/ "button") object a few times and listen to the results. Sending a `bang` into the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object generates a single 'grain' of audio. Turn on the [metro](https://docs.cycling74.com/reference/metro/ "metro") object by clicking the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") at the top of the patcher.


The [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object in our patcher generates grains: single bursts of sample playback which we can control dynamically by adjusting parameters. The [metro](https://docs.cycling74.com/reference/metro/ "metro") and [button](https://docs.cycling74.com/reference/button/ "button") objects control the grain emitter. Each time the [metro](https://docs.cycling74.com/reference/metro/ "metro") fires, it sends a `bang` into the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~"), prepended by the `note` message, which assigns the `bang` to the first available voice within the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~"). In addition, each `bang` from the [metro](https://docs.cycling74.com/reference/metro/ "metro") object schedules the next one by adjusting the speed of the [metro](https://docs.cycling74.com/reference/metro/ "metro"). The [random](https://docs.cycling74.com/reference/random/ "random") object generates a random value which is then put through a [scale](https://docs.cycling74.com/reference/scale/ "scale") object with a variable output range, defined by the `speedmin` and `speedmax` parameters found in patcher area `4`.
## Checking CPU
  * With the grain emitter enabled (i.e. the [metro](https://docs.cycling74.com/reference/metro/ "metro") object set to run), turn on the [metro](https://docs.cycling74.com/reference/metro/ "metro") in patcher area `2`. The [number](https://docs.cycling74.com/reference/number/ "number") box at the bottom of the patcher logic should output a number. Turn off the grain emitter at the top and watch the results. Turn it on again.


The [adstatus](https://docs.cycling74.com/reference/adstatus/ "adstatus") object allows us to control and view aspects of the MSP audio driver currently running. All of the viewable attributes of the _Audio Status_ window (available under the Max **Options** menu) can be accessed via the [adstatus](https://docs.cycling74.com/reference/adstatus/ "adstatus") object. The `cpu` mode of the [adstatus](https://docs.cycling74.com/reference/adstatus/ "adstatus") object (set by its argument) instructs the object to receive `bang` messages and output the current CPU usage of MSP. Notice that when the grain emitter is turned off, the CPU usage drops to `0.`. This is because our [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") abstraction mutes itself when its playback has finished. When no notes are firing, all of the copies of the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") abstraction should be muted.
## Adjusting parameters
  * In patcher area `3`, highlight an area of the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") objects to select part of the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") named `thegrain`. Notice that when you drag on either of the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") objects, both of them highlight in the same regions. The rightmost outlet of the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object allows us to _link_ them together so that you can use more than one of the objects to work with a multi-channel [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"). Load a different sample using the [message](https://docs.cycling74.com/reference/message/ "message") boxes above the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object and highlight different regions of the sample. The highlighted regions of the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") controls where the grain emitter draws its sample data.
  * In patcher area `4`, use the [preset](https://docs.cycling74.com/reference/preset/ "preset") object to try out different parameters for our grain emitter, then try entering your own values. The _Grain rate_[number](https://docs.cycling74.com/reference/number/ "number") boxes control the speed range of the [metro](https://docs.cycling74.com/reference/metro/ "metro") in patcher area `1`. The _Grain duration_ controls the ranges for how long each grain plays for inside the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~"). The _Grain pitch_ values provide a range for what speed the grains play at. The _Grain amplitude_ controls set the volume range of the grain emitter, and the _Grain slope_ sets the sharpness of the attack and decay on each grain's envelope. Notice how different densities of grains changes the sound as well as the CPU usage of the grains.


Before we look at our [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") abstraction, notice the effect of longer and shorter grain rates and durations on the CPU usage. Longer grain durations and shorter grain rates result in more voices inside the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") being active at any one time - either they are fired more frequently, or they take longer to 'free' themselves, or both. The result is a higher CPU usage.
  * In patcher area `1`, enable the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object attached to the [message](https://docs.cycling74.com/reference/message/ "message") box labeled `parallel $1`. Restart the audio by turning the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") off and on. Notice the effect, if any, on the CPU.


Depending on your computer architecture, you can take advantage of multiple cores in your computer's CPU (or multiple processors if you have a multi-processor machine) by dividing the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object's resources over multiple _threads_. In essence, this divides the instances of the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object across the different cores or processors of your computer, allowing sets of voices to run in parallel. Depending on your computer's CPU architecture, this may provide a significant boost in performance.
## Inside the patch
  * Double-click the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object to view an instance of the abstraction named `polygrain~`. Take a look around the patcher.


The `polygrain~` abstraction recieves a single `bang` (via the [in](https://docs.cycling74.com/reference/in/ "in") object at the top of the patcher) and uses it to generate a grain of audio, using the MSP logic at the bottom of the abstraction. The [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object at the top of the patch clearly sets up the order of events for generating our grain:
First, the [thispoly~](https://docs.cycling74.com/reference/thispoly~/ "thispoly~") object receives a `mute 0` and `1` message in immediate succession. This turns _on_ (unmutes) the signal processing in the instance, and sets it's state to 'busy', so that it won't receive any more note messages until the grain is finished.
Next, a `bang` is dispatched to generate a random _amplitude_ for the grain, which goes into the right side of the [*~](https://docs.cycling74.com/reference/*~/ "*~") object labeled 'how loud is this grain?'. This [*~](https://docs.cycling74.com/reference/*~/ "*~") controls the scaling for the output of the [line~](https://docs.cycling74.com/reference/line~/ "line~") object above that sets the grain envelope.
Third, a random _pitch_ is selected which is transformed into a duration multiplier for the [line~](https://docs.cycling74.com/reference/line~/ "line~") objects controlling the playback of the sample and its amplitude envelope. The [!/](https://docs.cycling74.com/reference/!%2F/ "!/") object divides the incoming pitch into `1.`, so that a requested pitch of `2.` tells the objects downstream to multiply their durations by `0.5` (half as long, and up an octave).
Fourth, a random _duration_ is generated, which sets up the parameters for the [line~](https://docs.cycling74.com/reference/line~/ "line~") objects so that they generate the appropriately scaled and offset values for the grain length.
Finally, a grain is triggered by generating a random _start point_ based on the highlighted areas in the [waveform~](https://docs.cycling74.com/reference/waveform~/ "waveform~") object in the main patcher. This `bang` eventually generates two messages which command the two [line~](https://docs.cycling74.com/reference/line~/ "line~") objects to generate the playback curve for the [play~](https://docs.cycling74.com/reference/play~/ "play~") object and the amplitude envelope for the [*~](https://docs.cycling74.com/reference/*~/ "*~") objects.
Once the 'envelope' [line~](https://docs.cycling74.com/reference/line~/ "line~") is finished, it sends a `bang` to `mute` the instance and set it to 'free' (`0`), so it can receive a new message.
  * Under the **File** menu in Max, select _Modify Read Only_. This will allow you to unlock the copy of the `simplegrain~` abstraction you are viewing. Unlock the patcher, and place 'watchpoints' on some of the patchcords to monitor their values. In the _Watchpoints_ window, you should see how different values in the grain settings in the main patcher translate into values for the synthesis algorithm at work here.


## Summary
The [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object allows you to have a large number of instances of a single, simple MSP patcher. You can use [send](https://docs.cycling74.com/reference/send/ "send") and [receive](https://docs.cycling74.com/reference/receive/ "receive") to communicate to all instances of a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") abstraction, which can be distributed across multiple cores or processors with the `parallel` message. The [adstatus](https://docs.cycling74.com/reference/adstatus/ "adstatus") object allows you to access and change aspects of the MSP audio driver; the `cpu` argument to the object lets you see how much of your computer's CPU you are using with a patcher.
## See Also
  * [adstatus - Report and control audio driver settings](https://docs.cycling74.com/reference/adstatus/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
