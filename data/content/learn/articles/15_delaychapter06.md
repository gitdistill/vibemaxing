---
description: Using comb filters to create resonation effects
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/15_delaychapter06/
title: Comb Filtering
---

Download Series Content and Patchers
# MSP Delay Tutorial 6: Comb Filter
## Comb filter: comb~
The minimum delay time that can be used for feedback into a delay line using [tapin~](https://docs.cycling74.com/reference/tapin~/ "tapin~") and [tapout~](https://docs.cycling74.com/reference/tapout~/ "tapout~") is determined by the signal vector size. However, many interesting filtering formulae require feedback using delay times of only a sample or two. Such filtering processes have to be programmed within a single MSP object.
An example of such an object is [comb~](https://docs.cycling74.com/reference/comb~/ "comb~"), which implements a formula for _comb filtering_. Generally speaking, an audio filter is a frequency-dependent amplifier; it boosts the amplitude of some frequency components of a signal while reducing other frequencies. A comb filter accentuates and attenuates the input signal at regularly spaced frequency intervals -- that is, at integer multiples of some fundamental frequency.
**Technical detail:** The fundamental frequency of a comb filter is the inverse of the delay time. For example, if the delay time is 2 milliseconds (1/500 of a second), the accentuation occurs at intervals of 500 Hz (500, 1000, 1500, etc.), and the attenuation occurs between those frequencies. The extremity of the filtering effect depends on the factor (between 0 and 1) by which the feedback is scaled. As the scaling factor approaches 1, the accentuation and attenuation become more extreme. This causes the sonic effect of resonance (a ‘ringing’ sound) at the harmonics of the fundamental frequency.
The [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") object sends out a signal that is a combination of a) the input signal, b) the input signal it received a certain time ago, and c) the output signal it sent that same amount of time ago (which would have included prior delays). In the inlets of [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") we can specify the desired amount of each of these three (_a_ , _b_ , and _c_), as well as the delay time (we'll call it _d_).
![](https://docs.cycling74.com/images/33fb158112a09144797541076ac830fc_402.webp) You can adjust all the parameters of the comb filter
****:::info **Technical detail:** At any given moment in time (we'll call that moment t), [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") uses the value of the input signal (xt), to calculate the output yt in the following manner:yt = axt + bx(t-d) + cy(t-d)The bx(t-d) term in the equation is called the _feedforward_ and the cy(t-d) term is the _feedback_.
**Technical detail:** At any given moment in time (we'll call that moment t), [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") uses the value of the input signal (xt), to calculate the output yt in the following manner:yt = axt + bx(t-d) + cy(t-d)The bx(t-d) term in the equation is called the _feedforward_ and the cy(t-d) term is the _feedback_.
**Technical detail:** At any given moment in time (we'll call that moment t), [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") uses the value of the input signal (xt), to calculate the output yt in the following manner:yt = axt + bx(t-d) + cy(t-d)The bx(t-d) term in the equation is called the _feedforward_ and the cy(t-d) term is the _feedback_. ::: The fundamental frequency of the comb filter depends on the delay time, and the intensity of the filtering depends on the other three parameters. Note that the scaling factor for the feedback (the right inlet) should usually not exceed 1, since that would cause the output of the filter to increase steadily as a greater and greater signal is fed back.
## Trying out the comb filter
The tutorial patch enables you to try out the comb filter by applying it to different sounds. The patch provides you with three possible sound sources for filtering -- the audio input of your computer, a band-limited pulse wave, or white noise -- and three filtering options -- unfiltered, comb filter with parameters adjusted manually, or comb filter with parameters continuously modulated by other signals.
![](https://docs.cycling74.com/images/bc1f6d456ccf6fecf6a2b3df32175e35_267.webp) Choose a sound source and route it to the desired filtering using the pop-up menus
  * Click on the buttons of the [preset](https://docs.cycling74.com/reference/preset/ "preset") to try out some different combinations, with example parameter settings. Listen to the effect of the filter, then experiment by changing parameters yourself. You can use MIDI note messages from your synth to provide pitch and velocity (frequency and amplitude) information for the pulse wave, and you can use the mod wheel to change the delay time of the filter.


A comb filter has a characteristic harmonic resonance because of the equally spaced frequencies of its peaks and valleys of amplification. This trait is particularly effective when the comb is swept up and down in frequency, thus emphasizing different parts of the source sound. We can cause this frequency sweep simply by varying the delay time.
## Band-limited pulse
The effects of a filter are most noticeable when there are many different frequencies in the source sound, which can be altered by the filter. If we want to apply a comb filter to a pitched sound with a harmonic spectrum, it makes most sense to use a sound that has many partials such as a sawtooth wave or a square wave.
![](https://docs.cycling74.com/images/65988fe2dc0fb6c27789bac7fe079423_411.webp) These mathematically ideal waves may be too ‘perfect’ for use as computer sound waves
The problem with such mathematically derived waveforms, though, is that they may actually be too rich in high partials. They may have partials above the Nyquist rate that are sufficiently strong to cause inharmonic aliasing. (This issue is discussed in more detail in _[Filter Tutorial 3](https://docs.cycling74.com/learn/articles/08_filterchapter03/)_.)
For this tutorial we're using a waveform called a _band-limited pulse_. A band-limited pulse has a harmonic spectrum with equal energy at all harmonics, but has a limited number of harmonics in order to prevent aliasing. The waveform used in this tutorial patch has ten harmonics of equal energy, so its highest frequency component has ten times the frequency of the fundamental. That means that we can use it to play fundamental frequencies up to 2,205 Hz if our sampling rate is 44,100 Hz. (Its highest harmonic would have a frequency of 22, 050 Hz, which is equal to the Nyquist rate.) Since the highest key of a 61-key MIDI keyboard plays a frequency of 2,093 Hz, this waveform will not cause aliasing if we use that as an upper limit.
![](https://docs.cycling74.com/images/f67379df3ba531f09f6cb3afda4a5e45_428.webp) Playing a band-limited pulse wave with MIDI
**Technical detail:** In an idealized (optimally narrow) pulse wave, each cycle of the waveform would consist of a single sample with a value of 1, followed by all samples at 0. This would create a harmonic spectrum with all harmonics at equal amplitude, continuing upward infinitely. It's possible to make an MSP signal network that calculates -- based on the fundamental frequency and the sampling rate -- a band-limited pulse signal containing the maximum number of possible harmonics without foldover. In this case, though, we have chosen just to use a stored waveform containing ten partials.
## Velocity-to-amplitude conversion: [gain~](https://docs.cycling74.com/reference/gain~/ "gain~")
The subpatch [p](https://docs.cycling74.com/reference/patcher/)`Pulse_Wave` contains a simple but effective way to play a sound in MSP via MIDI. It uses a [poly](https://docs.cycling74.com/reference/poly/ "poly") object to implement voice stealing, limiting the incoming MIDI notes to one note at a time. (It turns off the previous note by sending it out with a velocity of 0 before it plays the incoming note.) It then uses [mtof](https://docs.cycling74.com/reference/mtof/ "mtof") to convert the MIDI note number to the correct frequency value for MSP, and it uses the MSP object [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") to scale the amplitude of the signal according to the MIDI velocity.
![](https://docs.cycling74.com/images/e39083c0b9c66d6b6cce016922135153_341.webp) Converting MIDI pitch and velocity data to frequency and amplitude information for MSP
The [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") object takes both a signal and a number in its left inlet. The number is used as an amplitude factor by which to scale the signal before sending it out. One special feature of [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") (aside from its utility as a user interface object for scaling a signal) is that it can convert the incoming numbers from a linear progression to a logarithmic or exponential curve. This is very appropriate in this instance, since we want to convert the linear velocity range (0 to 127) into an exponential amplitude curve (0 to 1) that corresponds roughly to the way that we hear loudness. Each change of velocity by 10 corresponds to a change of amplitude by 6 dB. The other useful feature of [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") is that, rather than changing amplitude abruptly when it receives a new number in its left inlet, it takes a few milliseconds to progress gradually to the new amplitude factor. The time it takes to make this progression can be specified by sending a time, in milliseconds, in the right inlet. In this patch, we simply use the default time of 20 ms.
  * Choose one of the preset example settings, and choose ‘Pulse Wave’ from the ‘Sound Source’ pop-up menu. Play long notes with the MIDI keyboard. You can also obtain a continuous sound at any amplitude and frequency by sending numbers from the pitch and velocity [number box](https://docs.cycling74.com/reference/number/) objects (first velocity, then pitch) into the inlets of the [p](https://docs.cycling74.com/reference/patcher/)`Pulse_Wave` subpatch.


## Varying parameters of the filter
As illustrated in this patch, it's usually best to change the parameters of a filter by using a gradually changing signal instead of making an abrupt change with single number. So parameter changes made to the ‘Adjusted By Hand’ [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") object are sent first to a [line~](https://docs.cycling74.com/reference/line~/ "line~") object for interpolation over a time of 25 ms.
The ‘Modulated’ [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") object has its delay time varied at low frequency according to the shape of the band-limited pulse wave (just because it's a more interesting shape than a simple sinusoid). The modulation could actually be done by a varying signal of any shape. You can vary the rate of this modulation using the mod wheel of your synth (or just by dragging on the [number box](https://docs.cycling74.com/reference/number/)). The gain of the _x_ and _y_ delays (the two rightmost inlets) is modulated by a sine wave ranging between 0.01 and 0.99 (for the feedback gain) and a cosine wave ranging from 0.01 to 0.49 (for the feedforward gain). As the amplitude of one increases, the other decreases.
  * Experimenting with different combinations of parameter values may give you ideas for other types of modulation you might want to design in your own patches.


## Summary
The [comb~](https://docs.cycling74.com/reference/comb~/ "comb~") object allows you to use very short feedback delay times to _comb filter_ a signal. A comb filter creates frequency-dependent increases and decreases of amplitude in the signal that passes through it, at regularly spaced (i.e., harmonically related) frequency intervals. The frequency interval is determined by the inverse of the delay time. The comb filter is particularly effective when the delay time (and thus the frequency interval) changes over time, emphasizing different frequency regions in the filtered signal.
The user interface object [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") is useful for scaling the amplitude of a signal according to a specific logarithmic or exponential curve. Changes in amplitude caused by [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") take place gradually over a certain time (20 ms by default), so that there are no unwanted sudden discontinuities in the output signal.
## See Also
  * [comb~ - Comb filter](https://docs.cycling74.com/reference/comb~/)
  * [gain~ - Exponential scaling volume slider](https://docs.cycling74.com/reference/gain~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
