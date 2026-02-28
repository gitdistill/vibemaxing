---
description: Basic filter objects in MSP
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/08_filterchapter01/
title: Simple Filters
---

Download Series Content and Patchers
# Filter Tutorial 1: Simple Filters
This group of tutorials look at different ways to use _filters_ in MSP. This includes the basic uses of filters for the equalization and shaping of a sound and using filters to create timbres in subtractive synthesis. Along the way, we'll look at some of the theory behind filters and how they work.
## So what is a filter, anyway?
A filter is a circuit or software routine that can change the _spectral shape_ of a signal; that is, it will change the amplitude of some frequency regions and leave others alone. The simplest example is the bass control found on most audio systems—it will increase the low end of the music, or if that's not your style, turn it down. Similarly, the treble control will afect the high end. Both leave the middle as it is. There are many kinds of filter available; some are named by what they do, others are named by the technique used to implement them. When we talk about filters, we will make use of the following terms:
  * Any audio system can be described by its `frequency response`, which is a graph of the amplitude change across the audio spectrum (20-20,000 Hz). in an ideal system, the graph is a straight line, indicating a `flat` frequency response. To talk about filters, we look at the frequency response.
  * The frequency region that is _unaffected_ by a filter is the `passband`.
  * A `highpass` filter affects signals _lower_ than a specified frequency.
  * A `lowpass` filter affects signals _higher_ than a specified frequency.
  * Most filters have a gradual transition from the passband to the rejected region. The shape of this transition is called the `slope`, which is specified in dB per octave.
  * The frequency at which a filter becomes effective is called the `cutoff frequency`. It is actually the frequency at which the signal is reduced by 3dB. (A just noticeable difference in level.)
  * A `bandpass` filter affects signals _above and below_ a specified `center frequency`.
  * Obviously, a bandpass filter has two cutoff frequencies. The difference between these is the `bandwidth`.
  * The ratio of center frequency to bandwidth of a bandpass filter is known as the `quality factor` or `Q` of the filter. A filter with high Q will have a narrow passband. A filter with a high Q will also, depending on design, tend to resonate. This has led to an association of Q and a feature called `resonance`, at least in synthesis circles. Strictly speaking, resonance is a feature of some low and high pass designs, but some authors (and manufacturers) use the terms interchangeably.
  * The opposite of a bandpass filter is a `notch` filter, which rejects a band in the middle of the spectrum.
  * In addition to modifying amplitude of each frequency, filters also modify phase. A plot of phase change vs. frequency is the `phase response`. An ideal phase response would also be a flat line.


Filters have many uses from clearifying the vocals in a thrash mix to creating the sound of a Hungarian horntail. Often, filters are combined into complex devices like equalizers and vocoders. MSP has filters of all types, and new ones are added with each release (not to mention hundreds of third party externals).
## Our first filter: [lores~](https://docs.cycling74.com/reference/lores~/ "lores~")
Take a look at the tutorial patcher. Patcher area `1` contains a simple sampler, playing the _sacre.aiff_ sound (loaded into a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") named `chords`) using the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object. The circuit shown in this patch allows us to "play" the sample at any pitch with the [kslider](https://docs.cycling74.com/reference/kslider/ "kslider").
  * Turn on the audio in the patcher with the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box. Adjust the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Dry volume' and play some of the notes on the [kslider](https://docs.cycling74.com/reference/kslider/ "kslider"). You should hear the sample play at different notes.
  * Turn down the 'Dry volume' and turn up the next [number](https://docs.cycling74.com/reference/number/ "number") box, labeled 'Lowpass volume'. Notice the change in sound. Turn the [dial](https://docs.cycling74.com/reference/dial/ "dial") object at the top of patcher region `2`. As you move the [dial](https://docs.cycling74.com/reference/dial/ "dial") to a higher value, more of the high frequencies from the sample are audible.


The [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") object implements a _lowpass_ filter on an incoming audio signal (in our case, the output of the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object. A lowpass filter, as we saw in the tutorial introduction, passes the low frequencies and attenuates the high frequencies of the incoming signal. The two parameters that the filter takes are the _cutoff frequency_ (specified in the middle inlet or as the first argument to the object) and the _resonance_ (specified in the right inlet or as the second argument).
The cutoff frequency of a lowpass filter determines the frequency at which the audio is attenuated 3 dB. The resonance amount, when greater than `0.`, controls a peak of resonation (boosted frequencies) immediately below the cutoff. If we plot the response of the filter on a graph with the _X_ axis representing frequency and the _Y_ axis representing gain, it would look like this:
![](https://docs.cycling74.com/images/43928009093c97f8e184b9ca29c7eaaa_492.webp) A lowpass filter with and without resonance: **A** and **B**are the cutoff frequencies;**C** shows the resonance peak
  * With the sound going, adjust the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Resonance' in patcher area `2`. Notice how as the resonation approaches `1` the ringing at the resonance frequency becomes very loud. Adjust the cutoff frequency with the resonance set to a high number. Notice how you can now audibly "sweep" the filter based on hearing the resonation.


## Bandpass filters: the [reson~](https://docs.cycling74.com/reference/reson~/ "reson~") object
  * Turn down the volume of the lowpass filter, and look at section `3` in the tutorial. Turn up the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Bandpass volume'. Sweep the [dial](https://docs.cycling74.com/reference/dial/ "dial") labeled 'Center frequency' and listen to the result.


Just as a lowpass filter passes low frequency, a _bandpass_ filter passes a **band** of frequencies, attenuating anything lower or higher than a center frequency. The MSP [reson~](https://docs.cycling74.com/reference/reson~/ "reson~") object implements a bandpass filter with three parameters (controllable as inlets or arguments): the filter's gain, the center frequency, and _Q_.
  * With the [dial](https://docs.cycling74.com/reference/dial/ "dial") controlling the center frequency at 12 o'clock, click in the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Q' in patcher area `3`. Type the number `3` and hit return. Listen to the results. Try other positive numbers, such as `6`, `10`, or `0.5`. Notice that the higher the number is, the less frequencies make it through the filter. If necessary, adjust the 'Gain' with the [number](https://docs.cycling74.com/reference/number/ "number") box to the left.  ![](https://docs.cycling74.com/images/d346734e487254de59967f75b10587cf_640.webp)


A bandpass filter with Q values of `0.5`, `1.0`, `3.0`, and `30.0`, respectively.
## The state-variable filter: [svf~](https://docs.cycling74.com/reference/svf~/ "svf~")
  * Turn down the 'Bandpass volume' and look at patcher area `4`. Turn up the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Lowpass', adjust the 'Cutoff/Center Freq.' [dial](https://docs.cycling74.com/reference/dial/ "dial"), and set the 'Resonance' [number](https://docs.cycling74.com/reference/number/ "number") box to something that sounds good to you. Now, turn down the 'Lowpass' control and raise the 'Highpass'. Notice the difference. Do the same with the[number box](https://docs.cycling74.com/reference/number/)objects labeled 'Bandpass' and 'Notch'. Play with different combinations of volumes and settings.


The MSP [svf~](https://docs.cycling74.com/reference/svf~/ "svf~") object simulates an analogue _state-variable_ filter. Because of the way in which filters are wired using electronic components, the difference between one type of filter and another is often simply a matter of how you wire (or where you 'tap') the circuit. A state-variable filter is a filter that allows you to tap energy from several places in the filter, getting four simultaneous filters for the price of one. The [svf~](https://docs.cycling74.com/reference/svf~/ "svf~") object gives you four filtered sounds: a lowpass output , a _highpass_ output , a bandpass output , and a _notch_ output. The notch output should mirror the response of the equivalent bandpass filter. Notch filters are often called _bandstop_ or _bandreject_ filters. A plot of these possibilities shows their frequency responses:
![](https://docs.cycling74.com/images/10fe6d412cedadb8986f217f037b20a9_640.webp)
The outputs of a state-variable filter: lowpass, highpass, bandpass, notch.
  * Play with different combinations of the filters in the tutorial, mixing them in different ways with different settings. In the next tutorial, we'll look at building more complex filter arrangements.


##  How is all of this done digitally?
Filters, put simply, are algorithms that alter the frequency spectrum of a sound. When working with digital audio in the time domain (i.e. as a stream of samples representing the amplitude of a wave), filters are implemented as equations that use short _delays_ to shape an incoming waveform.
As an example, let's say we wanted to roll off the treble on an audio signal. If we plot a waveform, we can intuit the visual difference between low frequency and high frequency content:
![](https://docs.cycling74.com/images/11804fce92c166f631be04d184b3f24e_540.webp) Two waveforms, one with a low frequency, one with lots of high frequencies
As we can see, the top waveform (stored in the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") named `lowfrequency`, contains a sine wave at 50 Hz. The bottom waveform (in the `highfrequency`[buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~")) contains a complex FM tone with lots of high frequencies. If we wanted to roll off the treble on the bottom waveform, we could think of how it looks: high frequencies look like sharper angles when plotted in time. In order to cut high frequencies, we could _smooth_ this waveform. One way to smooth a signal is to _average_ it over time.
Let's say that we take a much simpler signal, that of a single sample of `1` in a sea of `0` 's. This is called an _impulse_ :
![](https://docs.cycling74.com/images/9a6d3135a925e8ab62cf970378b08206_252.webp) An impulse in an audio signal
An impulse has a frequency response equivalent to pure noise... hypothetically, all frequencies are present at equal volume (think of a 'click' in a digital audio signal or any other short burst of sound). So it contains plenty of high frequencies. If we wanted to smooth this signal, we could average each sample with the previous sample in this signal:
![](https://docs.cycling74.com/images/26ff3ed5e081e17e84089d2959deaa2c_254.webp) Our impulse, smoothed over one sample
This has the result of smearing the energy of the impulse across two samples. As a result, its frequency response will contain much less high-frequency energy; in fact, it's almost as if we've lowered the sampling rate: a click that lasts one sample at 44,100 Hz contains energy all the way up to 22,050 Hz; by derivation, a click that lasts _two_ samples at that sampling rate is the same as a one-sample click at half that rate, i.e. it only has energy up to 11,025 Hz.
## Some filter definitions
If we were to generalize what we just did to our impusle when we smoothed it, we could say this:
yn = 0.5xn + 0.5xn-1
where **x** represents _incoming_ samples, **y** represents outgoing samples, and **n** represents the current _time_ on the sample clock (i.e. _now_). This equation defines the filter: we're averaging (multiplying by 0.5) the current and previous incoming samples to generate the outgoing samples.
To put a name on this filter, we could call it a first-order non-recursive lowpass filter. The _order_ of a filter refers to how many samples of delay it contains: because we're only looking at one previous input, it's a first-order filter. Because the filter only uses incoming samples in its equation, it's non-recursive. As for what it does, it _passes_ low frequencies (and cuts high ones): hence the term _lowpass_.
Now consider this equation:
yn = 0.5xn + 0.5yn-1
This filter uses the previous _outgoing_ sample from the filter as part of the filter itself; by implementing feedback in the filter, we get a much stronger effect:
![](https://docs.cycling74.com/images/44207814397b8eb261a7bead0ac8ea9d_257.webp) Our impulse, averaged with the previous output sample
This equation defines a _recursive_ filter; as a result, the effect of the filter is dissipated beyond the order of the filter. While our first equation spread the energy of our one-sample click over two samples, this new equation spreads the energy over many, because of the averaging. Consider how the click interacts with the equation:
(xn + yn-1) / 2 =yn (1.0 + 0.0) / 2 = 0.5 (0.0 + 0.5) / 2 = 0.25 (0.0 + 0.25) / 2 = 0.125 (0.0 + 0.125) / 2 = 0.075 and so on...
In the filter described above, the energy of the click, hypothetically, will _never_ fully dissipate. Another term for this kind of filter is an _IIR_ , or infinite impulse response, filter; our first filter, which only uses incoming samples in its terms, has a finite impulse response (an _FIR_ filter).
In a later tutorial, we'll revisit some more filter theory. For now, it's simply important to understand that filters are made by manipulating very short (often single sample) delays (either with or without feedback) and mixing them with the current sample.
## Summary
Filters are devices or software that modify the frequency response of systems. Common filter types include lowpass, highpass, bandpass, and notch. Lowpass filters can be created with the [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") object, bandpass filters with the [reson~](https://docs.cycling74.com/reference/reson~/ "reson~") object, and all four with the [svf~](https://docs.cycling74.com/reference/svf~/ "svf~") object. Filters commonly have controls for their center or cutoff frequency and their Q or resonance.
In digital signal processing, _filters_ refer to equations which modify the frequency response of a signal. Filters are constructed by mixing small amounts of delayed signal with the original, smoothing or sharpening the waveform to accentuate or attenuate different frequencies.
## See Also
  * [lores~ - Resonant lowpass filter](https://docs.cycling74.com/reference/lores~/)
  * [reson~ - Resonant bandpass filter](https://docs.cycling74.com/reference/reson~/)
  * [svf~ - State-variable filter with simultaneous outputs](https://docs.cycling74.com/reference/svf~/)



Kind
    Tutorial 

Categories
    Audio     Synthesis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
