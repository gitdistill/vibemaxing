---
description: Adding sine waves to make a complex tone
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/06_synthesischapter01/
title: Additive Synthesis
---

Download Series Content and Patchers
# Synthesis Tutorial 1: Additive Synthesis
In the tutorial examples up to this point we have synthesized sound using basic waveforms. In the next few chapters we'll explore a few other well known synthesis techniques using sinusoidal waves. Most of these techniques are derived from pre-computer analog synthesis methods, but they are nevertheless instructive and useful.
## Combining tones
A sine wave contains energy at a single frequency. Since complex tones, by definition, are composed of energy at several (or many) different frequencies, one obvious way to synthesize complex tones is to use multiple sine wave oscillators and add them together.
![](https://docs.cycling74.com/images/86d597065df86e11d47aa9faed0e211d_380.webp) Four sinusoids added together to make a complex tone
Of course, you can add any waveforms together to produce a composite tone, but we'll stick with sine waves in this tutorial example. Synthesizing complex tones by adding sine waves is a somewhat tedious method, but it does give complete control over the amplitude and frequency of each component (_partial_) of the complex tone.
In the tutorial patch, we add together six cosine oscillators ([cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") objects), with independent control over the frequency, amplitude, and phase of each one. In order to simplify the patch, we designed an [Abstraction](https://docs.cycling74.com/userguide/abstractions/) called `partial~` which allows us to specify the frequency of each partial as a ratio relative to a fundamental frequency.
![](https://docs.cycling74.com/images/cb7fed2bf6d4f5d29ec43ebb209ec35c_483.webp) The contents of the partial~ abstraction
For example, if we want a partial to have a frequency twice that of the fundamental we just type in `2.0` as an argument (or send it in the second inlet). This way, if several `partial~` abstractions are receiving their fundamental frequency value (in the left inlet) from the same source, their relative frequencies will stay the same even when the value of the fundamental frequency changes.
Of course, for the sound to be very interesting, the amplitudes of the partials must evolve with relative independence. Therefore, in the main patch, we control the amplitude of each partial with its own _envelope generator_.
## Envelope generator: [function](https://docs.cycling74.com/reference/function/ "function")
In[Basics Tutorial 3](https://docs.cycling74.com/learn/articles/basicchapter03/)you saw how to create an amplitude envelope by sending a list of number pairs to a [line~](https://docs.cycling74.com/reference/line~/ "line~") object, thus giving it a succession of target values and transition times. This idea of creating a control function from a series of line segments is useful in many contexts - generating amplitude envelopes happens to be one particularly common usage - and it is demonstrated in the review in[Basics Tutorial 5](https://docs.cycling74.com/learn/articles/basicchapter05/), as well.
The [function](https://docs.cycling74.com/reference/function/ "function") object is a great help in generating such line segments, because it allows you to draw in the shape that you want, as well as define the function's domain and range (the numerical value of its dimensions on the _x_ and _y_ axes). You can draw a function simply by clicking with the mouse where you want each breakpoint to appear. When [function](https://docs.cycling74.com/reference/function/ "function") receives a `bang`, it sends a list of value-time pairs out its 2nd outlet. That list, when used as input to the [line~](https://docs.cycling74.com/reference/line~/ "line~") object, produces a changing signal that corresponds to the shape drawn.
By the way, [function](https://docs.cycling74.com/reference/function/ "function") is also useful for non-signal purposes in Max. It can be used as an interpolating lookup table. When it receives a number in its inlet, it considers that number to be an _x_ value and it looks up the corresponding _y_ value in the drawn function (interpolating between breakpoints as necessary) and sends it out the left outlet.
## A variety of complex tones
Even with only six partials, one can make a variety of timbres ranging from ‘realistic’ instrument-like tones to clearly artificial combinations of frequencies. The settings for a few different tones have been stored in a [preset](https://docs.cycling74.com/reference/preset/ "preset") object in the tutorial patcher for you to try. A brief explanation of each tone is provided below.
  * Click on the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") speaker icon to turn audio on. Click on the [button](https://docs.cycling74.com/reference/button/ "button") to play a tone. Click on one of the stored presets in the [preset](https://docs.cycling74.com/reference/preset/ "preset") object to change the settings, then click the button again to hear the new tone.


**Preset 1.** This tone is not really meant to emulate a real instrument. It's just a set of harmonically related partials, each one of which has a different amplitude envelope. Notice how the timbre of the tone changes slightly over the course of its duration as different partials come to the foreground. If you can't really notice that change of timbre, try changing the note's duration to something longer using the [number](https://docs.cycling74.com/reference/number/ "number") box at the top of the patcher. Changing its value to `8000` milliseconds, for example, will let you hear the note evolve more slowly.
**Preset 2.** This tone sounds rather like a church organ. The partials are all octaves of the fundamental, the attack is moderately fast but not percussive, and the amplitude of the tone does not diminish much over the course of the note. You can see and hear that the upper partials die away more quickly than the lower ones.
**Preset 3.** This tone consists of slightly mistuned harmonic partials. The attack is immediate and the amplitude decays rather rapidly after the initial attack, giving the note a percussive or plucked effect.
**Preset 4.** The amplitude envelopes for the partials in this tone are derived from an analysis of a trumpet note in the lower register. Of course, these are only six of the many partials present in a real trumpet sound.
**Preset 5.** The amplitude envelopes for the partials of this tone are derived from the same trumpet analysis. However, in this case, only the odd-numbered harmonics are used. This creates a tone more like a clarinet, because the cylindrical bore of a clarinet resonates the odd harmonics. Also, the longer duration of this note slows down the entire envelope, giving it a more characteristically clarinet-like attack.
**Preset 6.** This is a completely artificial tone. The lowest partial enters first, followed by the sixth partial a semitone higher. Eventually the remaining partials enter, with frequencies that lie between the first and sixth partial, creating a microtonal cluster. The beating effect is due to the interference between these waves of slightly different frequency.
**Preset 7.** In this case the partials are spaced a major second apart, and the amplitude of each partial rises and falls in such a way as to create a composite effect of an arpeggiated whole-tone cluster. Although this is clearly a whole-tone chord rather than a single tone, the gradual and overlapping attacks and decays cause the tones to fuse together fairly successfully.
**Preset 8.** In this tone the partials suggest a harmonic spectrum strongly enough that we still get a sense of a fundamental pitch, but they are sufficiently mistuned that they resemble the inharmonic spectrum of a bell. The percussive attack, rapid decay, and independently varying partials during the sustain portion of the note are also all characteristic of a struck metal bell.
Notice that when you are adding several signals together like this, their sum will often exceed the amplitude limits of the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") object, so the over-all amplitude must be scaled appropriately with a [*~](https://docs.cycling74.com/reference/*~/ "*~") object.
## Experiment with complex tones
  * Using these tones as starting points, try designing your own sounds with this additive synthesis patch. Vary the tones by changing the fundamental frequency, partials, and duration of the preset tones. You can also change the envelopes by clicking and dragging on the breakpoints in the [function](https://docs.cycling74.com/reference/function/ "function") objects:
  * Click in the [function](https://docs.cycling74.com/reference/function/ "function") object to create a new breakpoint. If you click and drag, the x and y coordinates of the point are shown in the upper portion of the object, and you can immediately move the breakpoint to the position you want.
  * Similarly, you can click and drag on any existing breakpoint to move it.
  * Shift-click on an existing point to delete it.


Although not demonstrated in this tutorial, it is also possible to create, move, and delete breakpoints in a [function](https://docs.cycling74.com/reference/function/ "function") just by using Max messages. See the reference page of [function](https://docs.cycling74.com/reference/function/ "function") object for details.
The message `setdomain`, followed by a number, changes the scale of the x axis in the [function](https://docs.cycling74.com/reference/function/ "function") without changing the shape of the envelope. When you change the number in the ‘Duration’ [number](https://docs.cycling74.com/reference/number/ "number") box, it sends a `setdomain` message to the [function](https://docs.cycling74.com/reference/function/ "function").
## Summary
_Additive synthesis_ is the process of synthesizing new complex tones by adding simple tones (typically sine waves) together. Since pure sine tones have energy at only one frequency, they are the fundamental building blocks of additive synthesis, but of course any signals can be added together. The sum signal may need to by scaled by some constant signal value less than 1 in order to keep it from being clipped by the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~").
In order for the timbre of a complex tone to remain the same when its pitch changes, each partial must maintain its relationship to the fundamental frequency. Stating the frequency of each partial in terms of a ratio to (i.e., a multiplier of) the fundamental frequency maintains the tone's spectrum even when the fundamental frequency changes.
In order for a complex tone to have an interesting timbre, the amplitude of the partials must change with a certain degree of independence. The [function](https://docs.cycling74.com/reference/function/ "function") object allows you to draw control shapes such as amplitude envelopes, and when [function](https://docs.cycling74.com/reference/function/ "function") receives a `bang` it describes that shape to a [line~](https://docs.cycling74.com/reference/line~/ "line~") object to generate a corresponding control signal.
## See Also
  * [function - Graphical function breakpoint editor](https://docs.cycling74.com/reference/function/)



Kind
    Tutorial 

Categories
    Audio     Synthesis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
