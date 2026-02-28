---
description: Playing and recording audio files from disk
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/07_samplingchapter06/
title: Recording and Playing Soundfiles
---

Download Series Content and Patchers
# Sampling Tutorial 6: Record and Play Audio Files
## Playing from memory vs. playing from disk
You have already seen how to store sound in memory - in a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") - by recording into it directly or by reading in a pre-recorded audio file. Once the sound is in memory, it can be accessed in a variety of ways with [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~"), [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~"), [index~](https://docs.cycling74.com/reference/index~/ "index~"), [play~](https://docs.cycling74.com/reference/play~/ "play~"), [groove~](https://docs.cycling74.com/reference/groove~/ "groove~"), [wave~](https://docs.cycling74.com/reference/wave~/ "wave~"), etc.
The main limitation of [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") for storing samples, of course, is the amount of unused RAM available on your computer. You can only store as much sound in memory as you have memory to hold it. For playing and recording very large amounts of audio data, it is more reasonable to use the hard disk for storage. But it takes more time to access the hard disk than to access RAM; therefore, even when playing from the hard disk, MSP still needs to create a small buffer to preload some of the sound into memory. That way, MSP can play the preloaded sound _while_ it is getting more sound from the hard disk, without undue delay or discontinuities due to the time needed to access the disk.
## Record audio files: [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~")
MSP has objects for recording directly into, and playing directly from, an audio file: [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") and [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~"). Recording an audio file is particularly easy, you just open a file, begin recording, and stop recording. (You don't even need to close the file; the [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") object takes care of that for you.) In the upper right corner of the Patcher window there is a patch for recording files.
The [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") object records to disk whatever signal data it receives in its inlets. The signal data can come directly from an [adc~](https://docs.cycling74.com/reference/adc~/ "adc~") or [ezadc~](https://docs.cycling74.com/reference/ezadc~/ "ezadc~") object, or from any other MSP object.
  * Click on the `open`[message](https://docs.cycling74.com/reference/message/ "message") box marked ‘Create an AIFF file’. You will be shown a Save As dialog box for naming your file. Navigate to the folder where you want to store the sound, name the file, and click Save. Turn audio on. Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") to begin recording; click on it again when you have finished.


## Play audio files: [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~")
In the left part of the tutorial patcher there is a patch for playing audio files. The basic usage of [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") requires only a few objects, as shown in the following example. To play a file, you just have to open it and start [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~"). The audio output of [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") can be sent directly to [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") or [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~"), and/or anywhere else in MSP.
  * Click on the `open`[message](https://docs.cycling74.com/reference/message/ "message") box marked ‘Set the current file’, and open the audio file you have just recorded. Then (with audio on) click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") marked ‘Play/Stop’ to hear your file.


[Sfplay~](https://docs.cycling74.com/reference/Sfplay~/ "Sfplay~") can play .aif, .wav, and mp3 files.
## Play excerpts on cue
Because [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") does not need to load an entire audio file into memory, you can actually have many files open in the same [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") object, and play any of them (or any portion of them) on cue. The most recently opened file is considered by [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") to be the ‘current’ file, and that is the file it will play when it receives the message `1`.
  * Click on the remaining `open`[message](https://docs.cycling74.com/reference/message/ "message") boxes to open some other audio files, and then click on the [message](https://docs.cycling74.com/reference/message/ "message") box marked ‘Define cues, 2 to 9’.


The `preload` message to [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") specifies an entire file or a portion of a file, and assigns it a _cue number_. From then on, every time [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") receives that number, it will play that cue. In the example patch, cues `2`, `3`, and `4` play entire files, cue `5` plays the first 270 milliseconds of _sacre.aiff,_ and so on. Cue `1` is always reserved for playing the current (most recently opened) file, and cue `0` is reserved for stopping [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~").
Whenever [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") receives a cue, it stops whatever it is playing and immediately plays the new cue. (You can also send [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") a _queue of cues_ , by sending it a `list` of numbers, and it will play each cue in succession.) Each `preload` message actually creates a small buffer containing the audio data for the beginning of the cue, so playback can start immediately upon receipt of the cue number.
Now that cues 0 through 9 are defined, you can play different audio excerpts by sending [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") those numbers. The upper-left portion of the patch permits you to type those numbers directly from the computer keyboard.
  * Click on the toggle marked ‘Keyplay On/Off’. Type number keys to play the different pre- defined cues. Turn ‘Keyplay’ off when you are done.


## Try different file excerpts
Before you define a cue, you will probably need to listen to segments of the file to determine the precise start and end times you want. You can use the `seek` message to hear any segment of the current file.
  * Open your own audio file again (or any other audio file) to make it the current file. In the right portion of this patch, enter an end time for the `seek` message. The excerpt you have specified will begin playing. Try different start and end times.


Once you find start and end times you like, you could use them in a `preload` message to establish a cue. Because [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") can't know in advance what excerpt it will be required to play in response to a `seek` message, it can't preload the excerpt. There will be a slight delay while it accesses the hard disk before it begins playing. For that reason, `seek` is best used as an auditioning tool; preloaded cues are better for performance situations where immediate playback is more critical.
## Trigger an event at the end of a file
The patch in the lower right portion of the Patcher window demonstrates the use of the right outlet of [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~"). When a cue is done playing (or when it is stopped with a `0` message), [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") sends a `bang` out the right outlet. In this example patch, the `bang` is used to trigger the next (randomly chosen) cue, so [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") effectively restarts itself when each cue is done.
Note the importance of the [gate](https://docs.cycling74.com/reference/gate/ "gate") object in this patch. If it were not present, there would be no way to stop [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") because each `0` cue would trigger another non-zero cue. The [gate](https://docs.cycling74.com/reference/gate/ "gate") must be closed before the `0` cue is sent to [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~").
  * In the patch marked ‘Play random excerpts’, click on the [message](https://docs.cycling74.com/reference/message/ "message") box to preload the cues, then click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") to start the process. To stop it, click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") again. Turn audio off.


## Summary
For large and/or numerous audio samples, it is often better to read the samples from the hard disk than to try to load them all into RAM. The objects [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") and [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") provide a simple way to record and play audio files to and from the hard disk. The [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") object can have many audio files open at once. Using the `preload` message, you can pre-define ready cues for playing specific files or sections of files. The `seek` message to [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") lets you try different start and end points for a cue. When a cue is done playing (or is stopped) [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") sends a `bang` out its right outlet. This `bang` can be used to trigger other processes, including sending [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") its next cue.
## See Also
  * [sfplay~ - Play audio file from disk](https://docs.cycling74.com/reference/sfplay~/)
  * [sfrecord~ - Record to audio file on disk](https://docs.cycling74.com/reference/sfrecord~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
