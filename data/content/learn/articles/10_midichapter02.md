---
description: Mapping standard MIDI parameters for synthesizer control
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/10_midichapter02/
title: MIDI Synthesizer
---

Download Series Content and Patchers
# MIDI Tutorial 2: MIDI Synthesizer
In this tutorial we show how to create and work with a simple 4-voice MIDI-controllable synthesizer. Along the way, we discuss simple methods of polyphonic routing as well as using a variety of common MIDI messages to control synthesis parameters.
  * To use the tutorial patchers in this section of the tutorial, make sure you have a correctly configured MIDI controller connected to your computer. The tutorials in this section use a variety of MIDI messages as example input; if your controller lacks any of these features, you can simulate their input with user interface objects in the tutorial.


## Playing our synthesizer
  * Take a look at the tutorial patcher. Notice that it contains a fair bit of patcher logic involving four different categories of MIDI input objects sending messages and signals to four copies of an abstraction called `synthvoice~`. Turn on audio by clicking the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~"), turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider, and play some notes on your MIDI keyboard. The [kslider](https://docs.cycling74.com/reference/kslider/ "kslider") object should animate in response to your actions. While holding a note, adjust the pitch bend wheel on your keyboard. Adjust the modulation wheel or another controller that can send CC#1. Listen to the different changes to the sound.


Our tutorial patcher deals with MIDI through a number of methods. Let's look through these one at a time.
  * Play notes on your keyboard one at a time and look at the area of the tutorial patcher labeled `1`. Notice what the [poly](https://docs.cycling74.com/reference/poly/ "poly") object does to the values. Try playing a note and holding it, then adding another while the first key is still down.


Our tutorial patcher is capable of playing four sounds at the same time, due to there being four different copies of the `synthvoice~` abstraction in our patch. In order to take advantage of the polyphony however, we need to figure out how to _route_ our MIDI values to the different voices so that the appropriate copy of the `synthvoice~` abstraction receives each message. The [poly](https://docs.cycling74.com/reference/poly/ "poly") object takes MIDI pitch and velocity and performs _voice assignment_ on the values based on the arguments to the object. The first note the object receives will be given voice number `1`, the second note voice `2`, and so on. Once we exceed the polyphony the object is programmed for (in our case, `4` voices), the object will roll around and start again at voice `1`. Note-off events will map to the _same voice_ as their corresponding note-on events, guaranteeing that the message to stop a MIDI event goes to the same destination as the one that started it.
  * Using your MIDI keyboard, play a four-note chord. Now, without releasing any of the keys, press a fifth note. Notice what happens.


The second argument to [poly](https://docs.cycling74.com/reference/poly/ "poly") (`1`) tells it to _steal_ voices if the polyphony is exceeded. If we attempt to sound more notes than the [poly](https://docs.cycling74.com/reference/poly/ "poly") object allows for, the _oldest_ note will be dropped and its voice will be recycled.
The output for our [poly](https://docs.cycling74.com/reference/poly/ "poly") object is sent into a [pack](https://docs.cycling74.com/reference/pack/ "pack") object and then through a [route](https://docs.cycling74.com/reference/route/ "route") object to send the remaining lists of pitches and velocities to the appropriate copy of our `synthvoice~` abstraction.
  * Take a look at tutorial area `2`. Move the pitch bend wheel on your keyboard controller. Notice that, unlike most controllers, its resting point is at the middle of the range at `63`. See what the patcher logic below does to scale the values between `-2.` and `2.`


To create our pitch bend value, we take the MIDI pitch bend wheel and [split](https://docs.cycling74.com/reference/split/ "split") its range to two different [scale](https://docs.cycling74.com/reference/scale/ "scale") objects. The left-hand [scale](https://docs.cycling74.com/reference/scale/ "scale") object takes the lower half of the MIDI range and scales it from `-2.` to `0.`; the right-hand object scales the upper range between `0.` and `2.` This guarantees that the center value in the range (`63`) maps to a value of `0.` in all cases.
  * Take a look at the tutorial area labeled `3`. Move the continuous controller and look how it's scaled. Look at the tutorial area labeled `4`. If you have a MIDI controller with real-time transport capabilities (i.e. it can send MIDI beat clock), set it up to transmit at any tempo you like and start the transport on the controller. If you like, you could also use an inter-application MIDI routing utility and a software sequencer on your computer to do this. If not, click in the [number](https://docs.cycling74.com/reference/number/ "number") box labeled `tick speed` and enter the value `20.` Change the continuous controller and play some notes. Listen to the result. Change the `tick speed` to something faster (like `10.`). Notice what happens.


The MIDI CC# and the real-time messages are sent in by the [ctlin](https://docs.cycling74.com/reference/ctlin/ "ctlin") and [rtin](https://docs.cycling74.com/reference/rtin/ "rtin") objects, respectively, to work together controlling a low-frequency oscillator (LFO). The real-time messages that define the _beat clock_ control the _rate_ of the LFO; the controller messages change the _depth_. MIDI beat clock typically runs at 96 PPQ; the [timer](https://docs.cycling74.com/reference/timer/ "timer") object measures the intervals between ticks, which are then scaled to derive the rate of the LFO so that it lasts one measure. MIDI real-time message `250` (the 'start' message on a sequencer) resets the phase of the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object so that the LFO will re-synch with a sequence if it starts on a barline.
Note how the output of the LFO is scaled so that even with the depth sending a signal of `0.`, the signal sent into the `synthvoice~` abstraction is guaranteed to be centered around `1.` Let's take a look at what's in that patch.
## The `synthvoice~` abstraction
  * Double-click any of the abstractions named `synthvoice~` and look at the patcher logic inside.


Our `synthvoice~` abstraction has three inLets. The first inlet takes lists of pitch and velocity values from our MIDI keyboard input. The _pitch_ value is sent to drive a constant signal ([sig~](https://docs.cycling74.com/reference/sig~/ "sig~")) which has the signal from inlet #2 added to it ([+~](https://docs.cycling74.com/reference/%2B~/ "+~")). This value is then interpreted as a MIDI number and converted to a frequency in the signal domain by an object called [mtof~](https://docs.cycling74.com/reference/mtof~/ "mtof~"), which behaves just like the [mtof](https://docs.cycling74.com/reference/mtof/ "mtof") object but operates on continuous MSP signals instead of Max numbers. This frequency value then feeds two band-limited oscillators: a square wave ([rect~](https://docs.cycling74.com/reference/rect~/ "rect~")) and a sawtooth wave ([saw~](https://docs.cycling74.com/reference/saw~/ "saw~")) which are mixed together. The _frequency_ of the [rect~](https://docs.cycling74.com/reference/rect~/ "rect~") object is multiplied by the LFO signal coming in inlet #3 so that a rich, chorused tone can be acheived when the depth of the LFO is increased.
## Standard synthesizer envelopes: [adsr~](https://docs.cycling74.com/reference/adsr~/ "adsr~")
Meanwhile, the _velocity_ output of the MIDI notes is scaled between `0.` and `1.` and sent to an object called [adsr~](https://docs.cycling74.com/reference/adsr~/ "adsr~"). The object stands for _Attack, Decay, Sustain, Release,_ and generates signal ramps in a standard configuration borrowed from analog synthesizer design:
![](https://docs.cycling74.com/images/0ba78f0947a976632d35a106e9ea88cf_156.webp)
_A standard ADSR curve._
The arguments to [adsr~](https://docs.cycling74.com/reference/adsr~/ "adsr~") are interpreted as an attack time, a decay time, a sustain _level_ , and a release time. The sustain level is a multiplier of the overall amplitude which the object outputs during a sustaining note.
The [adsr~](https://docs.cycling74.com/reference/adsr~/ "adsr~") object takes a value and interprets it as an envelope trigger of a certain amplitude. Any number higher than `0.` triggers the attack, decay, and sustain phases, scaled to match the amplitude of the trigger (e.g. an input value of `0.5` will trigger a softer envelope than a trigger of `0.8`). The object then stays at the sustain phase, putting out a constant value until it receives a `0.` It then continues to the release phase of the envelope and ramps to `0`.
  * Now that we understand how the synthesizer elements work, return to the main patcher and see if the controllable parameters make sense. Try exploring the full range of the MIDI control to see how expressive it is.


## Summary
Within a patcher, MIDI note events can be routed polyphonically to different copies of the same abstraction using a [poly](https://docs.cycling74.com/reference/poly/ "poly") object. Objects such as [bendin](https://docs.cycling74.com/reference/bendin/ "bendin") and [ctlin](https://docs.cycling74.com/reference/ctlin/ "ctlin") can be scaled to match different synthesizer parameter ranges, and real-time MIDI commands can be used to derive tempo data for LFOs and sequencers within Max. The [adsr~](https://docs.cycling74.com/reference/adsr~/ "adsr~") object generates envelope ramps based on triggers for a note-on and a note-off, making it ideal for use with MIDI note-based systems.
## See Also
  * [poly - Allocate notes to different voices](https://docs.cycling74.com/reference/poly/)
  * [mtof~ - Convert a MIDI note number to frequency at signal rate](https://docs.cycling74.com/reference/mtof~/)
  * [adsr~ - ADSR envelope generator](https://docs.cycling74.com/reference/adsr~/)



Kind
    Tutorial 

Category
    MIDI 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
