---
description: Using noise generators with filters
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/08_filterchapter04/
title: Subtractive synthesis
---

Download Series Content and Patchers
# Filter Tutorial 4: Subtractive Synthesis
In this chapter, we'll look at using filters creatively with a group of MSP audio generators that create different kinds of [noise~](https://docs.cycling74.com/reference/noise~/ "noise~"). Noise generation is a core component of _subtractive synthesis_ , a sound design methodology that works by taking complex signsl and sculpting them with filters, subtracting energy from the original signal (compare this with additive synthesis, which works in the opposite fashion). Along the way, we'll discuss ways to shape this noise using an object that creates and controls a _bank_ of parallel filters.
## Noise
Take a look at our tutorial patcher. It consists of three patcher regions. If we look at the area labeled `1`, we can see that we have three new MSP objects connected through [*~](https://docs.cycling74.com/reference/*~/ "*~") objects to the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~").
  * Start the audio in the tutorial patcher. Adjust the [number](https://docs.cycling74.com/reference/number/ "number") box that controls the volume for the [noise~](https://docs.cycling74.com/reference/noise~/ "noise~") object and listen to the result. Turn it down and turn up the volume for the [pink~](https://docs.cycling74.com/reference/pink~/ "pink~") object. Do the same for the [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object. Click in the [number](https://docs.cycling74.com/reference/number/ "number") box that is connected to the inlet of the [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object (labeled 'Frequency'). Type `100` and hit return. Try `1000` and hit return. Experiment with other values.


The [noise~](https://docs.cycling74.com/reference/noise~/ "noise~"), [pink~](https://docs.cycling74.com/reference/pink~/ "pink~"), and [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") objects all generate _noise_ at a signal rate. Noise, at its essence, is a type of random number generation; as a result, these objects behave in a similar manner to Max objects such as [random](https://docs.cycling74.com/reference/random/ "random") and [drunk](https://docs.cycling74.com/reference/drunk/ "drunk").
The [noise~](https://docs.cycling74.com/reference/noise~/ "noise~") object generates _white noise_ , which means that all possible frequencies in the audio spectrum are equally represented over time. The process of generating white noise digitally is quite simple: every sample, pick a random number between `-1` and `1` :
![](https://docs.cycling74.com/images/495e010d2536aca1b65a465c82569ff9_351.webp)
_A waveform and spectrogram plot of white noise._
The [pink~](https://docs.cycling74.com/reference/pink~/ "pink~") object generates _pink noise_ , which means that every _octave_ in the audio spectrum has equal weight. This is sometimes referred to as _1/f_ noise, as the probability of a frequency occuring is the inverse of its value, e.g. frequencies of 100 Hz are twice as probable as 200 Hz. The aural difference between the two is fairly obvious: white noise has far more high frequency content and sounds 'harsher' than pink noise:
![](https://docs.cycling74.com/images/cfeecf963062607d37d454bfd9bbb53a_351.webp)
_Pink (1/f) noise: waveform and spectrogram._
The [rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object is a random number generator that generates a signal, picking a new random value for that signal at a variable rate. It takes an argument (or a value at its inlet) to set the frequency of the random number selection. A frequency of `44100` makes the object indistinguishable from white noise. This allows us to create _band-limited_ noise that has an upper boundary we can specify:
![](https://docs.cycling74.com/images/f4648cd4444e12659edab305ba867a63_351.webp)
_A[rand~](https://docs.cycling74.com/reference/rand~/ "rand~") object picking values at `1000` Hz: waveform and spectrogram._
## Filtering noise
Because noise has such broadband frequency content, it can be filtered and sculpted to create very precise timbres. The compositional technique of subtractive synthesis relies on this attribute of noise generation; it's often easier (or more efficient) to start with noise and filter it down then attempt to create the desired timbre through adding oscillators.
  * Turn down the volumes in patcher area `1` and take a look at patcher area `2`. Turn up the volume using the [number](https://docs.cycling74.com/reference/number/ "number") box at the bottom of the signal chain (controlling the [*~](https://docs.cycling74.com/reference/*~/ "*~") object connected to the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~")). Click in the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Frequency' connected to the [phasor~](https://docs.cycling74.com/reference/phasor~/ "phasor~") object, type `0.1` and hit return. Type a higher frequency (e.g. `3.0`) and hit return. Experiment with different values.


Patcher area `2` contains a [noise~](https://docs.cycling74.com/reference/noise~/ "noise~") object sending its signal into a [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") filter. The frequency of the lowpass filter is being modulated by a [phasor~](https://docs.cycling74.com/reference/phasor~/ "phasor~"), which we've scaled to ramp between `100` and `600` at the frequency we specify. As a result, the cutoff frequency of the filter sweeps at regular intervals. This is an example of an _LFO_ , or _low-frequency oscillator_ , being used to modulate a parameter of an audio processing system. As you can hear, the [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") object attenuates the high frequencies output from the [noise~](https://docs.cycling74.com/reference/noise~/ "noise~") object. In addition, the resonance value of the [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") causes the filter to have a peak just below its cutoff frequency, giving a notably 'pitched' sound to the filtered noise.
## Banks of filters
  * Turn down the volume on area `2` in the tutorial patcher and take a look at area `3`. One-by-one, turn up and down the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") sliders connected to the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") object.


The [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object stands for _Fast, Fixed, Filter Bank_. Unlike the [cascade~](https://docs.cycling74.com/reference/cascade~/ "cascade~") object, which implements a number of [biquad~](https://docs.cycling74.com/reference/biquad~/ "biquad~") filters in series, the [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object arranges a number of [reson~](https://docs.cycling74.com/reference/reson~/ "reson~") objects in _parallel_ , which is to say that the settings of one filter will not affect any of the others. The [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object takes a number of arguments which set its behavior: the _number_ of filters, the _base frequency_ of the filter bank, the _ratio_ between filters, and the _Q_ of the filters. All of the parameters of the object with the exception of the number of filters can be changed with Max messages; the number is fixed because, as we can see, each filter connects to a separate outlet. This allows us to create filter banks, where we can 'tap' each bandpass filter individually:
![](https://docs.cycling74.com/images/6678a9a890a60edf6806c4963d7eb4a9_351.webp)
_Output of the lowest and highest two filters in our[fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~")object: waveform and spectrogram._
  * Using the mouse, click and drag on the [dial](https://docs.cycling74.com/reference/dial/ "dial") object in patcher area `3`. This has the audible effect of shifting the entire filter bank upwards or downwards. Turn up different [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") sliders to hear the results.


The value from the [dial](https://docs.cycling74.com/reference/dial/ "dial") is interpreted as a MIDI pitch, converted to frequency (via the [mtof](https://docs.cycling74.com/reference/mtof/ "mtof")) object, and used to format the `freqRatio` message to the [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object. The `freqRatio` message takes two arguments: the center frequency of the first (lowest) filter, and the _ratio_ between it and subsequent filters. The letter `H`, when used as the ratio, tells the [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object to set the filters in the bank to _harmonic_ multiples of the base frequency. So the message `freqRatio 100. H` would set our ten filters up to be centered to `100` Hz increments.
  * Click in the [number box](https://docs.cycling74.com/reference/number/) objects connected to the [pak](https://docs.cycling74.com/reference/pak/ "pak") object. Type `200.` in the lefthand [number](https://docs.cycling74.com/reference/number/ "number") box, and `1.5` in the righthand [number](https://docs.cycling74.com/reference/number/ "number") box. Click on the [number](https://docs.cycling74.com/reference/number/ "number") box connect to the `message` box containing the message `QAll $1`. Enter the value `100.` and hit return. Turn up and down the different [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") sliders to hear the results.


We can easily set our filters in a frequency ratio other than a harmonic series. Setting our base frequency to `200.` and our ratio to `1.5` results in a bank of ten filters set to the frequencies `200, 300, 450, 675, 1012.5, 1518.75, 2278.125, 3417.1875, 5125.78125, 7688.671875, and 11533.0078125` Hz, respectively. Other popular ratios include 1.4142 (21/2) and 1.25992 (21/3) for half octave and one third octave spacing. As with the [reson~](https://docs.cycling74.com/reference/reson~/ "reson~") object, we have direct control over the _Q_ of these filters. A Q of `100` results in a bandwidth of 1/100 the frequency, creating narrow, pitched filters.
  * Click the `message` box to the right of patcher area `3` that contains a series of lists. Listen to the results by adjusting the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") sliders.


The [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object takes many other messages, enabling us to set the filters not in ratio at all. Sending lists in the format `filter_# frequency Q` allows us to set each filter in the bank individually. In our example, we've set the ten filters to frequencies from a musical chord.
## Metering
Next to each [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider in patcher area `3` is a user-interface object that registers the amplitude of the signal connected to it. These [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") objects allow us to see the level from each filter in the [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~")_pre-fader_ , i.e. before we listen to it.
  * Turn down all the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") sliders in patcher area `3`. Click in the [number](https://docs.cycling74.com/reference/number/ "number") box that triggers the `Qall` message. Type `0.5` and hit return. Type `10.` and hit return. Listen to the results and notice the effect of the Q on the gain of each filter, and look at how the [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") objects respond.


Because the [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object works in parallel, the output gain of all the filters in the bank will typically be _greater_ than the gain of the incoming signal. Depending on the Q values and the frequencies used, the potential volume output from the [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") can be quite high. The [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") object lets you observe your volumes visually in the patcher window _before_ you listen (and potentially hurt your ears).
## Summary
MSP has three simple-to-use noise generator objects, which generate white noise ([noise~](https://docs.cycling74.com/reference/noise~/ "noise~")), pink noise ([pink~](https://docs.cycling74.com/reference/pink~/ "pink~")), and band-limited random signals ([rand~](https://docs.cycling74.com/reference/rand~/ "rand~")). These objects are ideal candidates for filtering. The [fffb~](https://docs.cycling74.com/reference/fffb~/ "fffb~") object implements a fixed filter bank of parallel bandpass filters which can be controlled via ratios of a base frequency or individually. The [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") object allows you to visually see the amplitude of any part of the MSP signal path, and is incredibly useful for metering and debugging your audio patchers.
## See Also
  * [noise~ - White noise generator](https://docs.cycling74.com/reference/noise~/)
  * [pink~ - Pink noise generator](https://docs.cycling74.com/reference/pink~/)
  * [rand~ - Band-limited random signal](https://docs.cycling74.com/reference/rand~/)
  * [fffb~ - Fast fixed filter bank](https://docs.cycling74.com/reference/fffb~/)
  * [meter~ - Visual peak level indicator](https://docs.cycling74.com/reference/meter~/)



Kind
    Tutorial 

Categories
    Audio     Synthesis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
