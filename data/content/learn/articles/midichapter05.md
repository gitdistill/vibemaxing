---
description: Recording and manipulating MIDI sequences
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/midichapter05/
title: Advanced Sequencing
---

Download Series Content and Patchers
# MIDI Tutorial 5: MIDI Advanced Sequencing
## Introduction
In this tutorial, we will expand on our use of the [seq](https://docs.cycling74.com/reference/seq/ "seq") object by recording new MIDI data, loading existing files and writing sequences to disk. We will also use the second outlet of the [seq](https://docs.cycling74.com/reference/seq/ "seq") object to provide looped playback of the current sequence.
Working with existing sequences is useful, but being able to record new sequences within Max allows us to create and store sequences and phrases for later use. This sequencing tutorial is focused on recording, the use of the file input/output functions, and the ability to use the [seq](https://docs.cycling74.com/reference/seq/ "seq") object output to loop playback.
## Recording a sequence
Our tutorial has a number of regions with different patcher logic in each. The leftmost region (labeled **Recording**) shows the basic setup for selecting MIDI input that we saw in earlier MIDI tutorials. The [seq](https://docs.cycling74.com/reference/seq/ "seq") object expects a raw MIDI stream, so our recording input comes directly from a [midiin](https://docs.cycling74.com/reference/midiin/ "midiin") object.
Select a valid MIDI input device from the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") so we can record MIDI data into our own sequence. In addition, double-click the [midiout](https://docs.cycling74.com/reference/midiout/ "midiout") object and select a valid MIDI output device. In addition to feeding the [seq](https://docs.cycling74.com/reference/seq/ "seq") object, the [midiin](https://docs.cycling74.com/reference/midiin/ "midiin") object is also sending data to the [midiout](https://docs.cycling74.com/reference/midiout/ "midiout") (via [midiflush](https://docs.cycling74.com/reference/midiflush/ "midiflush")), so you should be able to test your connections by playing on your MIDI controller.
Clicking on the red `record` message will start the recording of MIDI data. Click on this [message](https://docs.cycling74.com/reference/message/ "message") box, then play some MIDI data in from a connected controller. Clicking the `stop` message will stop recording; we can then hit `start` to hear the playback of the MIDI we just recorded. Since the [seq](https://docs.cycling74.com/reference/seq/ "seq") object is recording the complete MIDI stream, we can also send continuous controllers, pitchbend messages, program changes or any other MIDI data – it will be recorded and played back just like note messages. As in the last tutorial, we use the [midiflush](https://docs.cycling74.com/reference/midiflush/ "midiflush") object in between [seq](https://docs.cycling74.com/reference/seq/ "seq") and [midiout](https://docs.cycling74.com/reference/midiout/ "midiout") to silence any remaining note-on messages when we `stop` our sequence.
## Loading and saving a sequence
Once we’ve recorded a sequence, we may want to save the results. This is where the file-handling messages come into play. The top-right area (labeled **File Handling**) shows three messages that [seq](https://docs.cycling74.com/reference/seq/ "seq") understands for saving and loading files; in this case, the `write` message is our friend. Clicking on the `write` message will open a **Save** dialog that allows us to store the sequence to disk. Click on the `write` message, and save your newly recorded sequence to disk.
Reading the file from disk can take two forms: we can explicitly choose a file to read, or open a dialog to select from any MIDI file stored on disk. Explicit selection is done using a file name argument to the `read` message. Sending the `read` message without an argument will provide an **Open** dialog for selecting any available MIDI file. Click on the `read seq_sc.midi` message to load our test sequence file; to prove that we have changed the current sequence, play it using the `start` message. Click on the no-argument `read` message and select your saved sequence. Clicking the `start` message should play back our sequence as we performed it earlier.
## Looping playback
In the previous tutorial, we saw that the right outlet of [seq](https://docs.cycling74.com/reference/seq/ "seq") produces a `bang` message when a sequence is done with playback. Using this information, we can perform a common sequencing task: looping playback of our sequence. The bottom-right area (labeled **Loop Playback**) shows a [gswitch2](https://docs.cycling74.com/reference/gswitch2/ "gswitch2") (Graphical Gate) that will route the `bang` message back to the `start` message whenever the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object is checked. This is a simple use of the right-hand output for sequencer control; it could also be used for loading another sequence, starting a second [seq](https://docs.cycling74.com/reference/seq/ "seq") object or even starting another process in Max entirely.
## Summary
Recording a raw MIDI stream is one of the strengths of the [seq](https://docs.cycling74.com/reference/seq/ "seq") object; it can grab and store almost any type of MIDI message. Using the read and write commands, we can save and then restore any recorded MIDI data, whether received from a MIDI controller or generated from Max. We can also use the right outlet of [seq](https://docs.cycling74.com/reference/seq/ "seq") to control playback parameters or even start completely new Max processes. The [seq](https://docs.cycling74.com/reference/seq/ "seq") object should be seen as a robust, useful tool for many sequencing tasks.
## See Also
  * [seq - MIDI sequencer](https://docs.cycling74.com/reference/seq/)
  * [midiflush - Send note-offs for hanging note-ons in raw MIDI data](https://docs.cycling74.com/reference/midiflush/)



Kind
    Tutorial 

Category
    MIDI 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
