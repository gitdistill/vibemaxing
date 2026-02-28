---
description: Creating simple MIDI-compatible samplers in MSP
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/10_midichapter03/
title: MIDI Sampler
---

Download Series Content and Patchers
# MIDI Tutorial 3: MIDI Sampler
In this tutorial we talk about how to create a MIDI-controllable sampler in MSP. Along the way, we'll look at different features of many samplers, including looping, keymaps, and multi-timbral operation.
  * To use the tutorial patchers in this section of the tutorial, make sure you have a correctly configured MIDI controller connected to your computer. The tutorials in this section use a variety of MIDI messages as example input; if your controller lacks any of these features, you can simulate their input with user interface objects in the tutorial.


## Our fun sampler
  * Take a look at the patcher for this tutorial. The two sets of patcher logic (labeled `1` and `2` both deal with playing back samples stored in [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") objects by using [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") objects under MIDI control. Look at patcher area `1`. Turn on the audio by clicking the [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") and turn up the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider. From the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object at the top of the patch, select option `1` ('bd+hh.aiff'). Play some notes on your MIDI keyboard. You should hear a the bass drum sample at different pitches depending on which key you press. Select option `2` and take a listen; you should hear the snare drum.
  * Select option `3` ('cym.aiff') from the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu"). Play a note on the keyboard and hold it down, or select a note from the [kslider](https://docs.cycling74.com/reference/kslider/ "kslider") object. Notice that the sample loops. Select option `4`; notice that the bass guitar sound loops a swell. Play the sounds triggered by options `5` and `6`. Double-click the [coll](https://docs.cycling74.com/reference/coll/ "coll") file named `sampler`.


The [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object in our tutorial patcher causes the [coll](https://docs.cycling74.com/reference/coll/ "coll") object to dump out different data depending on which sample we select. Looking at its contents by double-clicking it reveals the entire database:
1, 24 sample1 0 0 0; _(bd+hh.aiff)_ 2, 33 sample2 0 0 0; _(snare.aiff)_ 3, 50 sample3 0.136054 373.106537 1; _(cym.aiff)_ 4, 67 sample4 60.204079 70.476189 1; _(bass.aiff)_ 5, 84 sample5 0 0 0; _(epno.aiff)_ 6, 108 sample6 0 0 0; _(ahkey.aiff)_
Each entry in the file sets up the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object in the patcher to play a sample. The format of each line in the [coll](https://docs.cycling74.com/reference/coll/ "coll") file is:
_base_key buffer~_name loop_start loop_end looping_
The _base key_ refers to which MIDI note the sample will play at _normal_ speed. The second item in the [coll](https://docs.cycling74.com/reference/coll/ "coll") refers to which [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object will play the sample. The next three values determine the start and end points of an internal loop which the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object will play, and whether or not to use it at all (the last value).
The point of a sampler is to play back recordings (audio samples), often from an acoustic instrument. If an acoustic instrumental source is used, it's inefficient to create a unique sample for every possible note on that instrument. Instead, every few notes are sampled, and in-between pitches are achieved by playing these sampled notes slightly fast or slow based on their base key. Similarly, a sampler is capable of playing notes that sustain for far longer than it's practical to record an instrumental sample. Instead, a sample of modest length is used, as an area is found _within_ the sustaining part of the sample that can be safely looped. When you play a note and hold it, the sample starts playback at the beginning; once it moves into the loop zone, it repeats that area over and over again; when you pick up the note, it plays from the loop zone through to the end of the sample.
  * Click through the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") again and notice how the different parameters coming from the [coll](https://docs.cycling74.com/reference/coll/ "coll") object set up the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object.


The _base key_ is converted from MIDI to frequency by the [mtof](https://docs.cycling74.com/reference/mtof/ "mtof") object and used as a divisor for the frequency we want to play. In this way, we get a _ratio_ of the desired frequency and the base frequency which we can use to set the speed of a [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object. If we want the sound to come out an octave higher, we want the ratio to be `2.0`; an octave lower, it should be `0.5`. The second value out of the [coll](https://docs.cycling74.com/reference/coll/ "coll") file is formatted with a `set` prefix by the [prepend](https://docs.cycling74.com/reference/prepend/ "prepend") object and send to the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") to select the appropriate [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") to play. The loop values come out as numeric data, setting the loop start and end points and sending a loop value into an [int](https://docs.cycling74.com/reference/int/ "int") box which is triggered each time a note plays. Note-on values (i.e. values with velocities greater than `0`) passed from the [stripnote](https://docs.cycling74.com/reference/stripnote/ "stripnote") object trigger the `loop` message, set the value of the [sig~](https://docs.cycling74.com/reference/sig~/ "sig~") object, and restart the sample by sending a `0` into the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object. Note-off objects set the `loop` state to `0`, allowing the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") to play out the sample to the end and then stop.
## Multi-timbral samplers and keymaps
  * Look at the patcher logic labeled `2` on the right of the tutorial patcher. As in the last tutorial, a [poly](https://docs.cycling74.com/reference/poly/ "poly") object is used to route MIDI data to a number of instances of a single abstraction, this time called `samplervoice~`. However, the values out of the [poly](https://docs.cycling74.com/reference/poly/ "poly") object do more than set the voice allocation.
  * Turn down the [gain~](https://docs.cycling74.com/reference/gain~/ "gain~") slider in patcher area `1` and turn up the one in patcher area `2`. Using an attached MIDI keyboard, play some notes all over the range of the keyboard. Notice that, depending on which notes you play, different samples are heard. Play some chords. Notice that you can have as many as four notes playing simultaneously. Look at the [message](https://docs.cycling74.com/reference/message/ "message") box attached to the [funbuff](https://docs.cycling74.com/reference/funbuff/ "funbuff") object:


0 1, 41 2, 48 3, 53 4, 68 5, 96 6
The [funbuff](https://docs.cycling74.com/reference/funbuff/ "funbuff") object is loaded with these values to use them as a _key map_ for a multi-timbral sampler. Any MIDI notes whose pitch values are between `0` and `40` will trigger sample `1` (as defined in the [coll](https://docs.cycling74.com/reference/coll/ "coll") file); pitches between `41` and `47` will trigger sample `2`; and so on.
  * Double-click any of the abstractions named `samplervoice~` and look at the patcher logic inside. Notice how it resembles the patcher logic in area `1` of the main patcher, with the addition of some objects to handle MIDI velocity to scale the amplitude output of the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object.


The MIDI velocity of incoming notes is divided by `127.` to scale it between `0.` and `1.` It is then multiplied _by itself_ , creating an exponential scaling wherein higher values on the MIDI velocity continuum yield far greater increases in volume than lower numbers. This simulates the behavior of logarithmic volume circuits (such as mixer faders) in analog audio equipment.
  * Return to the main patcher, and click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box labeled 'Play a sequence'. Double-click the [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") object named `sequence` as you rock out to the sequence playing out of our sampler.


The `sequence` subpatch contains a [seq](https://docs.cycling74.com/reference/seq/ "seq") object, a [midiflush](https://docs.cycling74.com/reference/midiflush/ "midiflush"), and a [midiparse](https://docs.cycling74.com/reference/midiparse/ "midiparse"). These objects load a MIDI file and output the raw bytes in response to `start` and `stop` messages ([seq](https://docs.cycling74.com/reference/seq/ "seq")), shut off all sounding notes in a MIDI byte stream in response to a `bang` ([midiflush](https://docs.cycling74.com/reference/midiflush/ "midiflush")), and parse and extract the pitch/velocity pairs from a MIDI stream so that they can be used elsewhere ([midiparse](https://docs.cycling74.com/reference/midiparse/ "midiparse")). This allows our awesome MIDI sequence to be played by the sampler logic in the main patch.
## Summary
MIDI-controllable samplers can be created using MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") and [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") objects. Different parameters of sampler data (loop points, sample name, base key) can be stored in [coll](https://docs.cycling74.com/reference/coll/ "coll") files for easy access so that you can easily switch samples depending on MIDI events within the same MSP patcher logic. 

Kind
    Tutorial 

Category
    MIDI 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
