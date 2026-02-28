---
description: Using looping sample memory
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/07_samplingchapter03/
title: Sample Playback with Loops
---

Download Series Content and Patchers
# Sampling Tutorial 3: Playback with Loops
As we've seen in the last two sampling tutorials, there are a variety of objects for accessing data from an MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object. This tutorial looks at another one which is specialized for working with looping sounds: [groove~](https://docs.cycling74.com/reference/groove~/ "groove~").
## Playing samples with [groove~](https://docs.cycling74.com/reference/groove~/ "groove~")
The [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object is one of the most versatile objects for playing sound from a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"). You can specify the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") to read, the starting point, the playback speed (either forward or backward), and start and end points for a repeating loop within the sample. As with other objects that read from a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") accesses the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") remotely, without patch cords, by sharing its name.
Take a look at [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object in the tutorial patcher. The [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object has three inlets which take both signals and standard Max messages. The left-hand inlet interprets a signal as its playback _speed_ , and a Max floating-point numeric message as its playback _position_. This allows for event-level control of the playback point (to jump to an area of the sample) as well as a time-varying signal controlling the playback rate of the sound. The second and third inlets allow you to specify start and end points in the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") to be used as loops.
The [sig~](https://docs.cycling74.com/reference/sig~/ "sig~") object is an MSP object that outputs a constant signal based on a floating-point numeric input. This signal drives the playback speed of the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~"). A signal of `1` causes normal-speed forward playback; a signal of `0.5` halves the speed (and drops the pitch of the sample by an octave); a signal of `-2` plays the sample at double-speed in reverse, and so on. While our tutorial uses constant-value signals for playback speed (supplied by the [sig~](https://docs.cycling74.com/reference/sig~/ "sig~") object), there is no reason why we couldn't use a [line~](https://docs.cycling74.com/reference/line~/ "line~"), [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") or other MSP object as a control signal for the speed of the playback.
The [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object also understands a number of messages in its left inlet to control its behavior. The message `loop 1` turns looping on, which is to say that when the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object reaches the end of the sample (or the time specified in the third inlet) it will return instantly to the beginning of the sample (or the point specified in the second inlet). In addition, you can change which [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object accesses as its sample memory at any time by sending the message `set` followed by the name of a valid [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object --- in fact, you can do this with any [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") -accessing MSP object, including [index~](https://docs.cycling74.com/reference/index~/ "index~") and [play~](https://docs.cycling74.com/reference/play~/ "play~"). In the tutorial patcher, a [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object is loaded with the names of the three [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") objects we've got in our patcher.
## Play some loops
  * Turn on the audio with the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object and adjust the output volume of the patch using the floating-point [number](https://docs.cycling74.com/reference/number/ "number") box on the right of the tutorial (labeled `Amplitude`). Click on the different circles in the [preset](https://docs.cycling74.com/reference/preset/ "preset") object to play the samples in different ways.


The first preset just functions as an ‘Off’ button. The next three presets play the three [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") objects at normal speed without looping. The rest of the presets demonstrate a variety of sound possibilities using different playback speeds on different excerpts of the buffered files, with or without looping.
  * You may want to experiment with your own settings by changing the user interface objects directly.


**Technical detail:** In traditional sampler design, the system that plays back the samples is very similar in operation to a [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object. Typically (for instrumental samples that are meant to loop) the sampler contains a handful of recorded samples of a few seconds duration, each of which is bound to a specific _root key_ , a note value at which it plays normally. Note values without samples play the nearest note that has a sample assigned to it either slightly fast or slightly slow by adjusting its playback rate. For notes that are meant to sustain (e.g. violins or synthesizer pads), the sample has metadata stored with it setting loop points within the sample which the synthesizer loops inside during sustained notes. Upon releasing the note, the sample plays out to the end.
If you want to create smooth undetectable loops with [groove~](https://docs.cycling74.com/reference/groove~/ "groove~"), you can use the `loopinterp` message to enable crossfades between the end of a loop and the beginning of the next pass through the loop to smooth out the transition back to the start point (see the [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") [Object reference page](https://docs.cycling74.com/userguide/object_reference/) for more information on this message). If the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") contains an AIFF file that has its own loop points - points established in a separate audio editing program - there is a way to use those loop points to set the loop points of [groove~](https://docs.cycling74.com/reference/groove~/ "groove~").
The [info~](https://docs.cycling74.com/reference/info~/ "info~") object can report the loop points of an AIFF file contained in a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), and you can send those loop start and end times directly into [groove~](https://docs.cycling74.com/reference/groove~/ "groove~"). You can also use the the [info~](https://docs.cycling74.com/reference/info~/ "info~") object to find out the length (in milliseconds) of any file you load into a buffer.
![](https://docs.cycling74.com/images/d0b2d1c8c2eb2e804a20ae28a2e82d54_542.webp)
_Using info~ to get loop point information from an AIFF file_
## Summary
The [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") object is the most versatile way to play sound from a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"). You can specify the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") to read, the starting point, the playback speed (either forward or backward), and starting and ending points for a repeating loop within the sample. If the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") contains an AIFF file that has its own pre-established loop points, you can use the [info~](https://docs.cycling74.com/reference/info~/ "info~") object to get those loop times and send them to [groove~](https://docs.cycling74.com/reference/groove~/ "groove~"). The playback speed of [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") is determined by the value of the signal coming in its left inlet. You can set the current buffer position of [groove~](https://docs.cycling74.com/reference/groove~/ "groove~") by sending a `float` time value in the left inlet.
## See Also
  * [buffer~ - Store audio samples](https://docs.cycling74.com/reference/buffer~/)
  * [groove~ - Variable-rate looping sample playback](https://docs.cycling74.com/reference/groove~/)
  * [info~ - Information about a buffer~](https://docs.cycling74.com/reference/info~/)
  * [sig~ - Constant signal of a number](https://docs.cycling74.com/reference/sig~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
