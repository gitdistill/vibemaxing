---
description: Max's Extras menu provides quick access to frequently used patchers
group: Max Interface
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/extras_menu/
title: Extras Menu
---

# Extras Menu
The _Extras_ menu provides quick access to frequently used patchers. Max comes with a set of utility patchers for everyday functions like testing [MIDI](https://docs.cycling74.com/userguide/midi/) input and opening the [Global Transport](https://docs.cycling74.com/userguide/transport/), and you can also add your own patchers to the Extras menu.
![](https://docs.cycling74.com/images/86b70de1d38a6510fb72c7114d098e7f_392.webp)
## Included Extras
Extra | Description  
---|---  
Audiotester | Measures input and output levels for your audio setup, and can be used to test your audio hardware and sound system.  
DSP CPU Monitor | Shows the current approximate audio CPU utilization.  
ExamplesOverview | Browse and launch examples included with Max.  
GlobalTransport | Start, stop, and display the passage of time for objects that use [Max Time formats](https://docs.cycling74.com/userguide/time_value_syntax/).  
Human Interface Driver Tester | Set up and test any object that support the [hi](https://docs.cycling74.com/reference/hi/ "hi") object.  
JitterTester | Tests video input devices.  
KeyMidi | Use your computer keyboard as a MIDI keyboard.  
Meterin and Meterout | Provide 24 channels of meters for audio input and output.  
MIDI Tester | Display all MIDI input and output devices and lets you test your connections.  
Mousemeter | Tracks the mouse.  
ObjectHelpLauncher | Fast way to open a help file.  
Quickrecord | Quickly record the audio output, up to 8 channels.  
UDP Tester | lets you test the sending of Max messages over a network using UDP.  
You can add your own patchers to the Extras menu by creating a [_Package_](https://docs.cycling74.com/userguide/packages/) with an `extras` folder.
## Package Extras
[_Packages_](https://docs.cycling74.com/userguide/packages/) that you add to Max (from the [_Package Manager_](https://docs.cycling74.com/userguide/package_manager/) or by adding folders to the `Packages` directory) will add patchers to the _Extras_ menu as well. Most packages include a "launcher" patcher that acts as an overview for the package, and some packages will have an _extras_ folder that adds even more patchers.
### Adding extras
If you want to add your own patchers to the _Extras_ menu, you can create a custom package and add your patchers to the `extras` subfolder. See [Packages](https://docs.cycling74.com/userguide/packages/) for more information.
