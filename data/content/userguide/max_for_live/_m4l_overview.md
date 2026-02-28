---
description: Overview of Max for Live, building devices, connecting MIDI and audio from Live to Max
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/_m4l_overview/
title: Max for Live Overview
---

# Max for Live
Max for Live allows you to harness the power and flexibility of Max inside Ableton Live. Using Max for Live, you can build your own devices and tools that enable you to completely control and shape how you work and create with Live. You can make:
  * [Audio Effects](https://docs.cycling74.com/userguide/m4l/live_audiodevices/)
  * [MIDI Effects](https://docs.cycling74.com/userguide/m4l/live_midieffects/)
  * [Instruments](https://docs.cycling74.com/userguide/m4l/live_audiodevices/)
  * [MIDI Transformations and Generators](https://docs.cycling74.com/userguide/m4l/live_miditools/)


You'll be able to connect custom hardware controllers, design sequencers, process audio in novel and exciting ways, and much more.
## Example Devices
Live Suite users have access to a wealth of packs on the [packs store](https://www.ableton.com/en/packs/#?item_type=max_for_live). From here you might get an idea of what Max for Live lets you build, including [sequencers](https://www.ableton.com/en/packs/sequencers/), [custom note transformations](https://www.ableton.com/en/packs/midi-tools/), [tools for controlling modular synthesisers](https://www.ableton.com/en/packs/cv-tools/), [bespoke instruments](https://www.ableton.com/en/packs/chiral/) and more.
There are also some parts of Ableton Live's software that are built using Max and it is a fully capable tool for making high-quality, professional devices. For example, [Convolution Reverb](https://www.ableton.com/en/packs/convolution-reverb/), [Granulator II](https://www.ableton.com/en/packs/granulator-ii/) and [Granulator III](https://www.ableton.com/en/packs/granulator-iii/) are all devices made with a combination of Max and sometimes [RNBO](https://rnbo.cycling74.com/).
Lastly, one of the major strengths of Max and Max for Live is its community and the spirit of sharing that comes with it. There are lots of great devices that can help you feel inspired by other people, often found at <https://maxforlive.com>.
## Learning Resources
Max for Live extends how you can use Ableton Live through a combination of [objects](https://docs.cycling74.com/userguide/objects/), [abstractions](https://docs.cycling74.com/userguide/abstractions/) and [APIs](https://docs.cycling74.com/userguide/m4l/live_api_overview/). All of these different tools and capabilities are embedded in "devices". A device is file ending in the `.amxd` extension which can be loaded and used in Ableton Live, much like the existing library of devices that are shipped with Live. A Max for Live device can contain patchers, abstractions, media and anything that can be added to a [Max collective](https://docs.cycling74.com/userguide/standalones_and_collectives/). To begin putting all these building blocks together, we recommend the [Building Max Devices](https://www.ableton.com/en/packs/building-max-devices/) pack. This pack guides you through building your own devices, while also offering over 90 devices that you can use as the basis of your own experimentation. You might also want to investigate both the [MSP](https://docs.cycling74.com/learn/series/msp-tutorials/) and [Max](https://docs.cycling74.com/learn/series/max-tutorials/) tutorials to get a better handle on the mechanics of patching just in Max.
Another option to supplement this is to take a look at the [Max sidebar](https://docs.cycling74.com/userguide/sidebar_search/) and the Max for Live clippings and snippets. These include lots of helpful shortcuts for putting together your own work.
## Jitter and Max for Live
You may find these tips useful if you want to create a Max for Live device using Jitter.
  * If you are using Vizzie in a Max for Live device, you will need to use a PROJECTR module or a vs.projectr Vizzie abstraction in your device.
  * If you are using [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") in a Max for Live device, you will need an implicitly named context or a --- (triple-dash) named context.
  * When you export a Max for Live project which includes a named context, a new instance of that context will be created during the export to the .amxd device. If the patch that includes that named context is open when you export the Project, you will see an error in the console that ob3d does not allow multiple bindings. The patch you're working on will no longer work as expected until you close it and then relaunch it after your export.
  * Jitter operates in Ableton Live’s interface update thread. This has two major effects: 
    * Jitter frame updates will be interrupted by the Live application’s interface redraws.
    * The maximum frame rate is dependent on the Ableton application’s audio buffer size.


## Max for Live Documentation
### Creating Devices
  * [Creating Devices Overview](https://docs.cycling74.com/userguide/m4l/live_creatingdevices/)
  * [Creating Audio Devices](https://docs.cycling74.com/userguide/m4l/live_audiodevices/)
  * [Creating MIDI Effects](https://docs.cycling74.com/userguide/m4l/live_midieffects/)
  * [Creating MIDI Tools](https://docs.cycling74.com/userguide/m4l/live_miditools/)
  * [User Interfaces](https://docs.cycling74.com/userguide/m4l/live_userinterfaces/)
  * [Symbols](https://docs.cycling74.com/userguide/m4l/live_symbols/)
  * [Timing](https://docs.cycling74.com/userguide/m4l/live_timing/)
  * [Limitations](https://docs.cycling74.com/userguide/m4l/live_limitations/)


### Live API
  * [Live API Overview](https://docs.cycling74.com/userguide/m4l/live_api_overview/)
  * [Creating Live API Devices](https://docs.cycling74.com/userguide/m4l/live_api/)


### Parameters
  * [Automation](https://docs.cycling74.com/userguide/m4l/live_automation/)
  * [Parameters](https://docs.cycling74.com/userguide/m4l/live_parameters/)
  * [Parameters Window](https://docs.cycling74.com/userguide/m4l/live_parameterswindow/)
  * [Pattr](https://docs.cycling74.com/userguide/m4l/live_pattr/)


### Sharing Devices
  * [Sharing](https://docs.cycling74.com/userguide/m4l/live_sharing/)
  * [Freezing](https://docs.cycling74.com/userguide/m4l/live_freezing/)
  * [Unfreezing](https://docs.cycling74.com/userguide/m4l/live_unfreezing/)
  * [Resolving Conflicts](https://docs.cycling74.com/userguide/m4l/live_resolveconflicts/)


