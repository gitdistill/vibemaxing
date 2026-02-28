---
description: Using variable-length delays to create a chorus effect
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/15_delaychapter05/
title: Chorus
---

Download Series Content and Patchers
# MSP Delay Tutorial 5: Chorus
## The chorus effect
Why does a chorus of singers sound different from a single singer? No matter how well trained a group of singers may be, they don't sing identically. They're not all singing precisely the same pitch in impeccable unison, so the random, unpredictable phase cancellations that occur as a result of these slight pitch differences are thought to be the source of the _chorus**effect_.
We've already seen in the preceding chapter how slight pitch shifts can be introduced by varying the delay time of a signal. When we mix this signal with its original undelayed version, we create interference between the two signals, resulting in a constantly varying filtering effect known as flanging. A less predictable effect called chorusing can be achieved by substituting a random fluctuation of the delay time in place of the sinusoidal fluctuation we used for flanging.
## Low-frequency noise: rand~
The [noise~](https://docs.cycling74.com/reference/noise~/ "noise~") object (introduced in Tutorial 3) produces a signal in which every sample has a randomly chosen value between -1 and 1; the result is _white noise_ , with roughly equal energy at every frequency. This white noise is not an appropriate signal to use for modulating the delay time, though, because it would randomly change the delay time so fast (every sample, in fact) that it would just sound like added noise. What we really want is a modulating signal that changes more gradually, but still unpredictably.
The [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object chooses random numbers between -1 and 1, but does so less frequently than every sample. You can specify the frequency at which it chooses a new random value. In between those randomly chosen samples, [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") interpolates linearly from one value to the next to produce an unpredictable but more contiguous signal.
![](https://docs.cycling74.com/images/a1964b0d8dff46deea5414834483539b_501.webp) Random values chosen every sample Choosing values less frequently
The output of [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") is therefore still noise, but its spectral energy is concentrated most strongly in the frequency region below the frequency at which it chooses its random numbers. This ‘low-frequency noise’ is a suitable signal to use to modulate the delay time for a chorusing effect.
![](https://docs.cycling74.com/images/37cf3ffd19a0a8e9e15ebfa99ce1acd7_562.webp) Unpredictable variations using rand~
The tutorial patch for this chapter is substantially similar to the flanging patch in the previous chapter. The main difference between the two signal networks is that the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object for flanging has been replaced by a [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object for chorusing. The [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") object in this patch is just for visualizing the modulating effect of the [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object.
## Multiple delays for improved chorus effect 
We can improve this chorus effect by increasing the number of slightly different signals we combine. One way to do this —as we have done in this patch— is to feed the randomly delayed signal back into the delay line, where it's combined with new incoming signal. The output of [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") will thus be a combination of the new variably delayed (and variably pitch shifted) signal and the previously (but differently) delayed/shifted signal.
![](https://docs.cycling74.com/images/e6b01ab02a4831897d7e03d544929d99_340.webp) Increasing the number of ‘voices’ using feedback to the delay line
The balance between these signals is determined by the settings for ‘LFeedback’ and ‘RFeedback’, and the combination of these signals and the undelayed signal is balanced by the ‘DryWetMix’ value. To obtain the fullest ‘choir’ with this patch, we chose delay times (17 ms and 23 ms) and a modulation rate (8 Hz, a period of 125 ms) that are all mutually prime numbers, so that they are never in sync with each other.
**Technical detail:** One can obtain an even richer chorus effect by increasing the number of different delay taps in [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~"), and applying a different random modulation to each delay time.
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") to turn audio on. Send some sound into the audio input of the computer to hear the chorusing effect. Experiment by changing the values for the different parameters. For a radically different effect, try some extreme values (longer delay times, more feedback, much greater chorus depth, very slow and very fast modulation rates, etc.).


## Summary
The _chorus effect_ is achieved by combining multiple copies of a sound -- each one delayed and pitch shifted slightly differently -- with the original undelayed sound. This can be done by continual slight random modulation of the delay time of two or more different delay taps. The [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object sends out a signal of linear interpolation between random values (in the range -1 to 1) chosen at a specified rate; this signal is appropriate for the type of modulation required for chorusing. Feeding the delayed signal back into the delay line increases the complexity and richness of the chorus effect. As with most processing effects, interesting results can also be obtained by choosing ‘outrageous’ extreme values for the different parameters of the signal network.
## See Also
  * [rand~ - Band-limited random signal](https://docs.cycling74.com/reference/rand~/)
  * [tapout~ - Output from a delay line](https://docs.cycling74.com/reference/tapout~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
