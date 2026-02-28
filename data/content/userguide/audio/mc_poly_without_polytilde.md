---
description: Busy maps and using mc.noteallocator and mc.voiceallocator instead of poly~ for polyphony
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_poly_without_polytilde/
title: MC Managed Polyphony
---

# MC Managed Polyphony
The MC Wrapper can manage polyphony without the use of the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object. You can assign Max messages or MIDI events to specific MC channels and turn off processing for unused channels.
## The Basis for Polyphony
Using the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object, a polyphonic synth has a defined voice count. [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") will load a separate patcher for each voice, which generates or processes sound independently from the other patchers. By contrast, with MC-based polyphony, there is a single patcher with MC wrapper objects set to a number of channels equal to the total voice count. For example, in this simple example, the [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~"), [mc.*~](https://docs.cycling74.com/reference/mc.*~ "mc.*~"), and [mc.gain~](https://docs.cycling74.com/reference/mc.gain~ "mc.gain~") objects have 12 channels. If you could control these objects independently, you could hear 12 independent voices.
![](https://docs.cycling74.com/images/1aaa5ddaf36f17119f12204c94611247_214.webp)
A good polyphony management system has three main benefits:
  1. To the maximum extent possible given the fixed resources allocated to your synth, new notes will not cut off already-playing notes.
  2. Voices allocated are spready cyclically to all channels, permitting pleasing panning or mixing effects based on channel number. For example you could spread channels across a stereo space knowing that on average, notes played will tend to fill the space.
  3. A polyphony management system can help keep track of which voices are actually playing and manage DSP resources by shutting off process for voices not producing sound.


As with the Max [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object, the MC polyphony system provides all three benefits. DSP resource management is more involved with MC polyphony than with [poly~](https://docs.cycling74.com/reference/poly~/ "poly~"); we'll cover that in the final section below.
## MC Polyphony using MIDI Notes
The [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") object accepts MIDI messages and directs messages to a specific target voice based on its internal voice allocation mechanism. Voices can be allocated either on the basis of MIDI note-on and note-off messages, or, more typically, by connecting a multichannel audio signal to the left inlet of [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~"). In that case, when a note-off for an allocated voice has been received _and_ the corresponding audio signal in the multichannel input goes to zero, [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") marks that channel as available to be allocated when future MIDI note-on messages are received.
![](https://docs.cycling74.com/images/6594d9626dab6bbd642f69e03ef4bc84_210.webp)
To specify a maximum number of voice numbers for allocation, supply a value for the `@voices` attribute. By default the `@voices` attribute has a value of zero, which means that if a multichannel audio signal is connected to the left inlet of [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~"), it will use the number of channels in the incoming audio signal. If no audio signal is connected, [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") will use a default of 15 voices ([mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~") works similarly but defaults to 16 voices).
## MC Polyphony using Max Messages
If you prefer to allocate and control MC channels using Max messages instead of MIDI notes, you can use the more general [mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~") object. Here is an example driven by a [metro](https://docs.cycling74.com/reference/metro/ "metro") object that allocates and releases voices using [mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~").
![](https://docs.cycling74.com/images/f1e52b9e679e98a7ffd7545357c8776b_496.webp)
The [mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~") object accepts the `endevent` and `release` messages to free an allocated voice, so if you want to write your own audio analysis algorithm to detect when a "note" has finished playing, that algorithm could trigger these messages.
## Managing DSP Resources
MC polyphony manages DSP resources by turning off channels of processing within each object using the MC wrapper. To enable/disable this behavior you need to use the `@usebusymap` attribute for each MC object.
A _busy map_ is maintained by [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") and [mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~") to keep track of which voices are currently defined to be playing ("busy"). These objects use the map to decide which MC channels are available for use; effectively implementing the first benefit of polyphony management mentioned above (new notes don't cut off playing notes).
Keep in mind that an object such as [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~") in the MC Wrapper consists of a set of MSP [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") objects. When you use the busy map, wrapper-based objects will turn off processing in individual [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") objects within an [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~"). If fewer than the maximum number of voices are playing, this can save CPU resources.
MC objects not based on the [MC Wrapper](https://docs.cycling74.com/userguide/mc/mc_wrapper/) do not implement busy maps because they have no way of turning off processing for individual channels.
## Enabling the Busy Map
To enable the use of the busy map for any wrapper-based object:
  * For all wrapper-based objects whose DSP resources you want to control, set the `@usebusymap` attribute to 1. For brevity the name `@bz` can also be used.


Here is the [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") example above where all wrapper-based objects have `@bz 1` included.
![](https://docs.cycling74.com/images/7c639a1de0233b80cbda7cfded19b23a_280.webp)
The `@usebusymap` attribute uses a patcher-global busy map. If you want to control wrapper-based objects in several patchers, or you have more than one [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") or [mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~") in the same patcher, you can use _named busy maps_ described in the next section.
## Using Named Busy Maps
The [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") and [mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~") objects include a `@name` attribute that specifies a symbolic name to associate with their internal busy map.
To control DSP resources of a wrapper-based object using a named busy map:
  * Create an [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") or [mc.voiceallocator~](https://docs.cycling74.com/reference/mc.voiceallocator~ "mc.voiceallocator~") object with a `@name` attribute
  * Add the `busymapname` (`bzname` for short) attribute to each wrapper object you want to control


Here is the [mc.noteallocator~](https://docs.cycling74.com/reference/mc.noteallocator~ "mc.noteallocator~") example above using named busy maps:
![](https://docs.cycling74.com/images/56216cd490cb9bbcef0e4bc3a751f103_358.webp)
