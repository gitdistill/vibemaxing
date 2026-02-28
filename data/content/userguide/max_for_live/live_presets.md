---
description: Handling preset storage in Max for Live devices
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_presets/
title: Presets
---

# Presets
Presets are a feature of Live that permit you to store the current state of a device. Since it is Live, not Max, that does the saving, the state must be known to Live, which means a preset captures the state of all the [parameters](https://docs.cycling74.com/userguide/m4l/live_parameters/) you have defined. This means that the value of a number box not connected to a parameter will not be saved -- Live presets are different from the Max [preset](https://docs.cycling74.com/reference/preset/ "preset") object in this way.
## Storing a Preset
  * Click the Save Preset icon in the title bar of the Max device. (The Save Preset icon is the one at the far right that resembles a _floppy disk_ , for those of you who know what a floppy disk looks like.)

![](https://docs.cycling74.com/images/1ccec0c0d5a940febe9df016a32477f2_60.webp)
  * In the File Browser, a new preset will be created and its name will be selected, ready for you to edit. Type in a name for the preset.


## Presets for a Devices in the Library
When you store a preset for a Max device in the Library, it appears beneath the device hierarchically. In the example shown below, _NicePreset_ is a preset that has been saved for the Max device _MyEffect_.
![](https://docs.cycling74.com/images/a9dac9b3a1cdaa38304c7281b14dcbe7_237.webp)
## Presets for a Devices Outside the Library
When you store a preset for a Max device that is _not_ located in the Library, the preset will have a special _preset-plus-device_ icon and also show the device name in square brackets before the preset name. In the example below, we stored a preset called _GiantPreset_ for an effect originally outside the Library called _MyGiantEffect_. 
![](https://docs.cycling74.com/images/302a1f73bde9d180c6f74ab052935f0b_237.webp)
## Saving a Max Device in the Library
If you want to save a device into the Live library, it's better to use the Save As... command within Max instead of moving the device file using your operating system. Using Save As... permits Live to keep track of your device and manage its presets.
  * Insert the device you want to move. Click the edit button to launch Max to edit the device.
  * In Max, choose **Save As...** from the File menu. Navigate the standard save file dialog to show the current Live Library folder. Save the device inside the Presets folder inside the Library folder, or a subfolder of the Presets folder.
  * Return to Live and you will see the newly saved device. In the example below, we saved our device as _MyEffect_.

![](https://docs.cycling74.com/images/1e262abe2e148961517d0c1afe368936_242.webp)
