---
description: Creating dynamic compressors, limiters, and gates in MSP
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/09_dynamicschapter02/
title: Dynamics Processing
---

Download Series Content and Patchers
# Dynamics Tutorial 2: Dynamics Processing
This tutorial looks at using envelope following techniques to create _dynamics processors_ in MSP. Once we've derived the amplitude envelope of a waveform as a control signal, we can add patcher logic to make decisions on the overall gain of a signal. This allows us to make compressors, limiters, and gates based on the time-varying amplitude of our audio.
  * In the tutorial patcher, look at the area labeled `1`. This is a simple playback patcher that takes a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") and loops it using a [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object. Turn on the audio by clicking the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") and turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider to hear the sound. Note that the audio from the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object goes into a [send~](https://docs.cycling74.com/reference/send~/ "send~") object named `audio`. We'll pick up this audio in the subpatchers within the tutorial patcher. Turn down the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider and doubleclick the [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") object labeled 'Compressor/Limiter'.


## Audio compression and limiting
If we have an audio signal containing a wide range of amplitudes (such as a drum loop or expressive vocals) it's often necessary to reduce, or _compress_ , this range. A _compressor_ algorithm reduces the dynamic range of an audio signal by tracking its envelope and checking that value against a _threshold_ number. When the audio signal exceeds the threshold, its gain is reduced by a scaling factor called a compression _ratio_. We can change the behavior of a compressor by adjusting its _threshold_ and _ratio_ , as well as by making intelligent decisions regarding the way in which the envelope signal is derived.
  * In the tutorial [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") labeled 'Compressor/Limiter', turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider. Note the difference between the sound and the sound of the uncompressed drum loop in the main patcher. Click in the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Threshold' and lower its value to `0.2`. Raise the [number](https://docs.cycling74.com/reference/number/ "number") box labeled 'Ratio' to `30.`. Listen to the results. Change the 'Decay' value to `200`. Bring the ratio back down to `4.`, and the threshold to `0.5`. Try raising the 'Attack' value. Listen to the results as you play with the controls, and look at the [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") objects at the bottom of the patcher.


Our compression patcher contains the standard controls that we would find on a hardware compressor box or a dynamics plug-in for a DAW program. The 'Attack' and 'Decay' controls set parameters for the envelope following of the audio signal. These values (converted from milliseconds to samples by the [*](https://docs.cycling74.com/reference/*/ "*") objects) set how fast the [rampsmooth~](https://docs.cycling74.com/reference/rampsmooth~/ "rampsmooth~") object allows the envelope to rise and fall based on the incoming signal. A long attack and decay will make the compressor circuit less responsive, but will also limit some of the artifacts associated with a highly responsive compressor, such as audible 'pumping' of the gain. The 'Threshold' and 'Ratio' controls alter how the compressor deals with scaling the gain. Our circuit implements the following equation to set the gain, where `g` is the gain, `e` is the envelope signal, and `t` and `r` are the threshold and ratio, respectively:
g = ( (e-t)*(1/r) + t ) / e; 0<=g<=1.
This gain value `g` is clipped in the range of `0.` to `1.` and then multiplied by our original audio to control its volume. The envelope value `e` and output gain `g` are shown in the patcher in the [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") objects labeled 'Enveloped' and 'Reduction'. The colors in the 'Reduction' [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") are flipped so that the colored area is greater as the gain is lower, visually cueing us into the fact that the audio volume is being _attenuated_ by our compressor.
  * Set the 'Attack', 'Decay', and 'Threshold' to `10.`, `100.`, and `0.5`, respectively. Click on the `message` box containing the value `0.` and labeled 'Limiter?'. Listen to the results.


A _limiter_ is a compression circuit with an infinite compression ratio, i.e. sound above the threshold is attenuated to never exceed that threshold. For a limiter, the `r` term is infinite, zeroing out part of the equation:
g = t / e; 0<=g<=1.
  * Experiment more with different compression settings to see how the circuit responds. Note that the circuit always attenuates the signal, so at very low thresholds it may be necessary to raise the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider to hear the results. When you've finished, turn down the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider, return to the main tutorial patcher, and open the [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") named 'Gate'.


## Audio gating
  * Look at the contents of the subpatcher named 'Gate': the settings are similar to the compression example, but the results are quite different. Turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider and listen to the results of the circuit. Look at the [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") objects and see how they respond to the drum loop.


The MSP circuit in this patcher starts on the same premise of a compressor: that of an envelope follower and a threshold. Rather than reducing the gain of audio energy that exceeds the threshold, however, this circuit attenuates signals that fall _below_ it. This type of dynamics compression is called a _gate_ (it is also sometimes referred to as a _noise gate_). Unlike a compressor, however, the gate has a _knee_ setting instead of a compression ratio. This setting is a proportion of the threshold within which the audio is attenuated rather than cut altogether. So with the default settings in the tutorial patch, we can expect the following results:
Sound above `0.5` are left alone (`g` = 1). Sound below `0.5` and above `0.375` (the threshold * the knee) are scaled between 0 and 1. Sound below `0.375` are gated out (`g` = 0)
In equation form, our gate looks something like this, where `g` is the gain, `e` is the envelope signal, and `t` and `k` are the threshold and knee:
g = (e-(t*k)) / (t-(t*k); 0<=g<=1.
As with our compressor, `g` is clipped between `0` and `1`.
  * Familiarize yourself with the gate settings. Set the knee as high as it will go, and notice at the gate effect now simply cuts in and out. Set the knee to a low value, and the gate will fade in and out smoothly. See how the 'Attack' and 'Decay' controls on the envelope follower effect the ability of our gate to track the beat of the drum loop and gate out the silences.


## Summary
Dynamics processors in MSP can be constructed using signal processing algorithms that take an envelope follower output as their control signal. Compressors and limiters attenuate audio signals that exceed a certain amplitude threshold according to their envelopes; gates attenuate audio that falls below a threshold. The parameters of the envelope follower itself control the responsiveness of the dynamics circuit, while parameters such as the threshold and ratio / kne. control the 'sound' of the processing. 

Kind
    Tutorial 

Categories
    Audio     Synthesis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
