---
description: Mapping audio channesl in and out of Max
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/audio_channels/
title: Multi-Channel Audio I/O
---

# Multi-Channel Audio I/O
The first part of this guide describes how audio input and output works in Max, specifically how channels map to hardware. The [second part](https://docs.cycling74.com/userguide/audio_channels/#mc-hardware-interfacing) describes how [MC](https://docs.cycling74.com/userguide/mc/) works with audio hardware. Work with patch cords and objects that deal with multiple channels simplifies working with audio hardware, but is not absoltely necessary.
## Logical and Physical Audio Channels
Max provides up to 1024 logical audio channels that you can dynamically assign to the physical channels of your audio hardware.
When you create an [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") or [adc~](https://docs.cycling74.com/reference/adc~/ "adc~") object with different channel numbers as arguments, these numbers refer to logical channels. These channels are internal to Max, and they can be dynamically reassigned to physical device channels of a particular driver using either the Audio Status window, its I/O Mappings subwindow, or an [adstatus](https://docs.cycling74.com/reference/adstatus/ "adstatus") object with an input or output keyword argument.
The purpose of having both logical channels and physical device channels is to allow you to create patches that use as many channels as you need without regard to the particular hardware configuration you're using. For instance, some audio interfaces use physical device channels 3 and 4 for _S/PDIF_ input and output, others use channels 9 and 10 instead. Without logical mapping you would have to change the arguments on all of your [adc~](https://docs.cycling74.com/reference/adc~/ "adc~") and [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") objects when you changed interfaces.
Note that logical channels can map to a single physical channel.
## Assigning Logical to Physical Channels
To configure the assignment of logical to physical audio channels, open the **Audio I/O Mappings** window from the Preferences window toolbar.
![](https://docs.cycling74.com/images/3e6e9f0ed80bc59b9a87704b54ec6584_106.webp)
The window displays assignment menus for logical input and output channels in groups of 16. This is the default assignment for a single-channel audio input device and a two-channel audio output device.
![](https://docs.cycling74.com/images/19a09208dbf813d8193c49a77e08580f_294.webp)
The assignment menu contains the physical channels of the selected hardware input or output devices. For example, here is the output assignment menu when using a Focusrite interface that has eight output channels.
![](https://docs.cycling74.com/images/107148c4387f891de897a9d72e11d678_106.webp)
Use the menu to set the desired physical channel for each logical channel you want to use.
To move to another bank of 16 channels, use the menus for input and output at the top of the Audio I/O Mappings window.
## MC Hardware Interfacing
MC provides flexible managment of multichannel signals, but interfacing with your hardware requires system-specific setup and routing. The [adc~](https://docs.cycling74.com/reference/adc~/ "adc~") object for audio input has a multichannel counterpart ([mc.adc~](https://docs.cycling74.com/reference/mc.adc~ "mc.adc~")) with a single multichannel output, and the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") object for audio output has a multichannel counterpart ([mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~")) with a single multichannel input.
## Working with Multichannel Input
Use [mc.adc~](https://docs.cycling74.com/reference/mc.adc~ "mc.adc~") object to obtain a multi-channel input signal from your audio interface.
  * Create an instance of the [mc.adc~](https://docs.cycling74.com/reference/mc.adc~ "mc.adc~") with the input channels that you want to access. The channels are numbered starting with 1.
  * Connect the multichannel signal output to any processing or monitoring objects to work with the MC content.

![](https://docs.cycling74.com/images/544119d8c56bdf92ad2c5bec1dc60d5f_163.webp)
A multi-channel version of [ezadc~](https://docs.cycling74.com/reference/ezadc~/ "ezadc~") with two signals in one patch cord is availble with [mc.ezadc~](https://docs.cycling74.com/reference/mc.ezadc~ "mc.ezadc~").
![](https://docs.cycling74.com/images/5adc046abe66e4f9389a410938934732_112.webp)
## Working with Multichannel Output
Use [mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~") to send a multi-channel audio output signal to your audio interface.
  * Create an instance of [mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~") with the output channels that you want to access. The channels are numbered starting at 1.
  * Connect a multichannel signal to the input of the object to send the audio stream to your interface.

![](https://docs.cycling74.com/images/71d6076a9614de42a23bce9ab5c71d87_318.webp)
A multi-channel version of [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") that outputs all channels of its input multi-channel signal is availble with [mc.ezdac~](https://docs.cycling74.com/reference/mc.ezdac~ "mc.ezdac~").
![](https://docs.cycling74.com/images/6581a48a51ce914ead3e5eb3e328a5fa_311.webp)
## Audio Hardware Routing
In addition to setting up the inputs and outputs of your patch, you will also need to verify the hardware input and output routings are correct. This is done using the [Audio I/O Mappings](https://docs.cycling74.com/userguide/audio_channels/#assigning-logical-to-physical-channels) window available in the [Preferences](https://docs.cycling74.com/userguide/preferences_and_settings/) window toolbar.
The Audio I/O Mappings window establishes mappings between channels on your audio interface hardware and Max's 1024 _virtual_ channels.
![](https://docs.cycling74.com/images/e93e827c33724092aed02d7da030296a_147.webp)
For each input channel you wish to use for multichannel input (via [mc.adc~](https://docs.cycling74.com/reference/mc.adc~ "mc.adc~")), choose a hardware input from the pop-up menu. For each output channel you wish to use for multichannel output (via [mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~")), choose a hardware output from the pop-up menu. You can assign the same hardware input or output to any number of virtual channels.
## See Also
  * [Spatialization with MC](https://docs.cycling74.com/userguide/mc/mc_spatialization/)
  * [MC in Max for Live](https://docs.cycling74.com/userguide/mc/mc_maxforlive_interface/)


