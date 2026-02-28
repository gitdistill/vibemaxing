---
description: Working with MIDI in Max, including MIDI objects and configuration options for MIDI input and output
group: MIDI
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/midi/
title: MIDI
---

# MIDI
MIDI stands for Musical Instrument Digital Interface. It's a method for exchanging information among compatible devices and programs. Originally created on top of a serial protocol, MIDI messages are often sent entirely within a computer, either between applications or from an application to a plug-in.
## MIDI Setup
Choose _MIDI Setup..._ from the _Options_ menu to open the **MIDI Setup Window**.
![](https://docs.cycling74.com/images/bfbb8103ac55303159ad238e405a5061_498.webp)
The MIDI Setup window provides information on the availability and status of all available MIDI inputs and outputs, and lets you perform mapping between MIDI devices and names or numbers.
Max can receive MIDI on any MIDI _Input Port_ , and can send MIDI to any MIDI _Output Port_. These ports have the following properties:
  * _Name_ - The unique identifier for the port
  * _Abbrev_ - An optional, single-letter abbreviation that acts as a shorthand for the port name.
  * _Offset_ - An optional channel offset, in multiples of 16.
  * _On_ - Whether or not the port is enabled
  * _Map_ - Whether the port is available for [mapping](https://docs.cycling74.com/userguide/mapping/#midi-mapping)


### Enabling/disabling MIDI ports
Toggle the checkbox in the _On_ column to enable and disable MIDI port. All ports are enabled by default.
### Mapping mode
The checkbox in the _Map_ column determines whether or not the given port is available for [**MIDI Mapping**](https://docs.cycling74.com/userguide/mapping/#midi-mapping). Mapping output is disabled by default, see [MIDI Output and Mapping](https://docs.cycling74.com/userguide/mapping/#midi-output-and-mapping) for more details.
### Abbreviation and channel offset
Use the _Abbrev_ and _Offset_ columns to configure the abbrevation and channel offset for each MIDI port. To create a letter mapping for a MIDI input or output, click in the Abbrev column for the row corresponding to a MIDI input or output and choose a letter from the pop-up menu that appears. The MIDI input or output device can now be identified using the letter abbreviation you have selected.
Additionally, you can set a channel offset for each MIDI port. To create a channel offset for a MIDI input or output, click in the Offset column for the row corresponding to a MIDI input or output and choose a channel offset value from the pop-up menu that appears. The MIDI input or output device can now be identified by sending or receiving a message whose MIDI channel number falls in the range _Offset Value_ + 15. For example, if you configure a MIDI port to have an offset of 32, then setting the channel offset of 35 on a MIDI object will address that MIDI port on channel 3.
## Objects for MIDI
The simplest objects for working with MIDI are [midiin](https://docs.cycling74.com/reference/midiin/ "midiin") and [midiout](https://docs.cycling74.com/reference/midiout/ "midiout"), which connect to a MIDI port and route MIDI byte streams to or from those ports. The MIDI objects [midiparse](https://docs.cycling74.com/reference/midiparse/ "midiparse") and [midiformat](https://docs.cycling74.com/reference/midiformat/ "midiformat") convert MIDI streams to and from Max messages. MIDI objects like [notein](https://docs.cycling74.com/reference/notein/ "notein")/[noteout](https://docs.cycling74.com/reference/noteout/ "noteout"), [bendin](https://docs.cycling74.com/reference/bendin/ "bendin")/[bendout](https://docs.cycling74.com/reference/bendout/ "bendout"), [ctlin](https://docs.cycling74.com/reference/ctlin/ "ctlin")/[ctlout](https://docs.cycling74.com/reference/ctlout/ "ctlout"), [polyin](https://docs.cycling74.com/reference/polyin/ "polyin")/[polyout](https://docs.cycling74.com/reference/polyout/ "polyout"), and [pgmin](https://docs.cycling74.com/reference/pgmin/ "pgmin")/[pgmout](https://docs.cycling74.com/reference/pgmout/ "pgmout") combine the functionality of [midiin](https://docs.cycling74.com/reference/midiin/ "midiin")/[midiout](https://docs.cycling74.com/reference/midiout/ "midiout") and [midiparse](https://docs.cycling74.com/reference/midiparse/ "midiparse")/[midiformat](https://docs.cycling74.com/reference/midiformat/ "midiformat").
![](https://docs.cycling74.com/images/f409b04c9ae5a9bfdc57335816b1b6a8_510.webp) Basic objects for working with MIDI streams
Receive MIDI real-time messages with [rtin](https://docs.cycling74.com/reference/rtin/ "rtin"). This includes MIDI `start`, `stop`, and `tick` messages.
To work with MIDI system-exclusive messages, use [sysexin](https://docs.cycling74.com/reference/sysexin/ "sysexin") to receive sysex messages and [sysexformat](https://docs.cycling74.com/reference/sysexformat/ "sysexformat") to format them.
## MIDI Ports and Devices
A MIDI **Port** is a named MIDI source or destination. Often, a MIDI **Device** , or a physical or virtual system that can send or receive MIDI, will open a single MIDI port, whose identifier is simply the name of the device. Because of this, you'll sometimes see _port_ and _device_ used interchangeably in MIDI object help files.
MIDI sending and receiving objects all respond to the `port` message, which configures them to bind to a particular MIDI port. The name of a MIDI port can also be an abbreviation, which can be configured in the [_MIDI Setup Window](https://docs.cycling74.com/userguide/midi/#midi-setup), or using the [`portabbrev`](https://docs.cycling74.com/userguide/controlling_max_with_messages/#portabbrev) message to Max. The [midiinfo](https://docs.cycling74.com/reference/midiinfo/ "midiinfo") object can list MIDI devices.
![](https://docs.cycling74.com/images/0cf11d3308b7e7a1557a3402719ed0e8_396.webp) From left to right: a midiin object, bound to the port named 'to Max 1'; a midiin object bound to the port with the abbreviation 'a'; a midiin object that will listen on all ports, with messages to select between ports.
## MPE
MPE stands for MIDI Polyphonic Expression. The MPE specification assigns each voice its own MIDI Channel, so that expression messages like pitch bend and aftertouch can be applied to indivicual notes.
The [mpeparse](https://docs.cycling74.com/reference/mpeparse/ "mpeparse") object will format an incoming MIDI stream into MPE message events, and the corresponding [mpeformat](https://docs.cycling74.com/reference/mpeformat/ "mpeformat") object will convert message events into an MPE-compatible midi stream. The [mpeconfig](https://docs.cycling74.com/reference/mpeconfig/ "mpeconfig") object will let you configure a MPE device, for example by defining zones. Finally, the [polymidiin](https://docs.cycling74.com/reference/polymidiin/ "polymidiin") object works in conjunction with the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object, facilitating working with MPE in the context of a [polyphonic subpatch](https://docs.cycling74.com/userguide/polyphony/).
![](https://docs.cycling74.com/images/56585ebc7bf56a8e8c48026e5c32fd86_412.webp) The last outlet of mpeparse formats the MIDI stream into 'mpeevent' messages, which are understood by a poly~ containing a polymidiin object.
## Default Devices for MIDI Objects
If you create a MIDI output object without specifying a device name, the object transmits MIDI to the first device (the default) in the list of output devices in the MIDI Setup window.
On the Macintosh, the default MIDI output is an AudioUnit DLS synthesizer. The AU DLS synth supports its own set of internal sounds as a General MIDI bank, and also provides support for Level 2 SoundFont files.
On Windows systems, the default MIDI output is the Microsoft GS Wavetable Synthesizer. (Note: the Microsoft GS Wavetable Synthesizer does not support SoundFont files)
If you don’t assign MIDI input or output to a specific destination or port (i.e., one that does not have a MIDI device name or abbreviation as an argument) , Max will automatically merge all input devices. This is useful if you want to treat all MIDI input identically regardless of its source, But this also means that the only way for a Max patcher to determine which device is actually the source of input to these objects is to compare the incoming MIDI channel number to the MIDI channel offset specified for each device.
Note: The [midiin](https://docs.cycling74.com/reference/midiin/ "midiin") object is an exception to this behavior — if you don’t use an argument to specify a device, it receives data only from the first device in the input device list. When multiple devices share the same letter abbreviation, Max will use the first one in the list at the time a MIDI input or output object is created with that abbreviation as an argument. Changing the abbreviations of devices has no effect on pre-existing objects, although it will have an effect on the meaning of subsequent port messages sent to MIDI output objects with abbreviations as argument.
## Configuring the Built-in MIDI Synthesizers
Max uses your machine's built-in MIDI synthesizer as its default MIDI output destination. With the OS-provided, built-in synthesizer, you can make sound without any external MIDI gear.
On Macintosh, the default MIDI output is the AudioUnit DLS (Down-Loadable-Sounds) synthesizer. The AU DLS synth supports its own set of internal sounds as a General MIDI bank, and also provides support for Level 2 SoundFont files.
On Windows systems, the default MIDI output is the Microsoft GS Wavetable Synthesizer.
On both systems, you can configure the built-in synthesizer by [sending messages to Max directly](https://docs.cycling74.com/userguide/controlling_max_with_messages/).
### Creating a new port for a DLS synth (Mac only)
Only one port for the built-in synth is created by default. ([augraph](https://docs.cycling74.com/reference/augraph/ "augraph") on Mac OS X or [midi_mme](https://docs.cycling74.com/reference/midi_mme/ "midi_mme") on Windows). However, on Mac, you can work with more than one DLS synth by creating additional MIDI synthesizer ports and assigning new DLS sound bank files to each one. This feature is not available on Windows machines.
  * Use the [`createoutport`](https://docs.cycling74.com/userguide/controlling_max_with_messages/#createoutport) message.
  * The name of the driver will be `augraph` on macOS. For the port name, you can use the name you want to give to your virtual output port.
  * For example, the message `;#SM createoutport synth2 augraph` create a second DLS synth called “synth2”.


### Deleting a DLS synth port (Mac only)
  * Use the [`deleteoutport`](https://docs.cycling74.com/userguide/controlling_max_with_messages/#deleteoutport) message.
  * Again, on macOS the name of the driver will be `augraph`. The port name will be the name of the virtual port (created with `createoutport`) that you want to delete.


### Loading a bank of sounds on a DLS Synth (type 1 or 2) (macOS only)
  * Use the [`driver loadbank`](https://docs.cycling74.com/userguide/controlling_max_with_messages/#driver-loadbank) message.
  * The filename should be the name of an existing DLS bank file, and the port name will be the name of the port that will use this bank. If you omit the port name, the bank you specify will be loaded by all DLS ports. On macOS, the folder `/Library/Audio/Sounds/Banks` is added to the search path when looking for a DLS bank file (i.e. it is the default location for searching for sound bank files).
  * If you specify a zero (0) for the filename, the default GM (General MDI) sound bank will be loaded (e.g., ;#SM driver loadbank 0 <portname>).


### Turning the DLS synth reverb on and off (Mac only)
  * Use the [`driver reverb`](https://docs.cycling74.com/userguide/controlling_max_with_messages/#driver-reverb) message.


### Setting MIDI output latency (Windows only)
  * The Windows _midi_mme_ will let you configure the output latency.
  * Use the message [`driver latency`](https://docs.cycling74.com/userguide/controlling_max_with_messages/#driver-latency).
  * For example, the message `;#SM driver latency 10 midi_mme` will set the driver latency to 10 milliseconds.


