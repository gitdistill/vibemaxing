---
description: Using VST, Audio Unit, and Max for Live device plugins in Max
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/plugins/
title: Plugins
---

# Audio Plugins
Most DAWs (Digital Audio Workstations) support plug-ins, which let third parties extend the audio processing capabilities of the main software. Max supports Audio Unit, VST, and VST3 plug-ins, and can load Max for Live devices (AMXDs) as plug-ins as well.
The Max object wrapping VST and Audio Unit support is called [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") or [mc.vst~](https://docs.cycling74.com/reference/mc.vst~ "mc.vst~"), and the object wrapping Max for Live devices is called [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") or [mc.amxd~](https://docs.cycling74.com/reference/mc.amxd~ "mc.amxd~"). The object [plugin~](https://docs.cycling74.com/reference/plugin~/ "plugin~") is for authoring Max for Live devices, and does not load plug-ins itself.
![](https://docs.cycling74.com/images/f86c7cc317dcfe4e4773408a3b004761_351.webp) macOS includes an Audio Unit called AUHighShelfFilter, which Max can load as a plugin to implement that audio effect.
## Loading a Plugin
If you have a `.component` or `.vst` file, you should be able to drop that file onto an unlocked patcher to load the plug-in. This will automatically create a [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object that points to that file.
The left toolbar also provides access to the **Plug-in Browser**. Clicking on the _Plug-ins_ icon will open the browser, letting you filter for plug-ins and AMXDs by name and kind.
![](https://docs.cycling74.com/images/ff23d5d411144f9a3b41ab0bc7cdb53e_428.webp)
Max builds the list of plug-ins by scanning for them at launch. In the _Plug-ins_ section, you can use the _Full Scan_ button to initiate a scan manually, which can be useful if you're adding new plug-ins with Max open.
![](https://docs.cycling74.com/images/5ab28ea263755e0f115777bd67553613_597.webp)
## User Interface
When you drop a plug-in into your patcher, the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") or [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object will enable the `@viewvisibility` attribute and show you a user interface for the plug-in. For an Audio Unit or VST plug-in, you'll see the generic interface. This lists all of the parameters in the plug-in, and lets you set their values.
![](https://docs.cycling74.com/images/4d42864c39a4081733a5ade8152546ea_423.webp) The generic plug-in interface
With Max for Live devices, you'll see the customized user interface for that device.
![](https://docs.cycling74.com/images/4d42864c39a4081733a5ade8152546ea_423.webp) The custom user interface for the 'Additive Heaven' Max for Live device
### Configuring parameter visibility
In the generic interface, click the pencil icon in the top toolbar to edit parameter visibility. Disable the _Visibility_ checkbox to hide the parameter from view.
![](https://docs.cycling74.com/images/a79cca7cd966404668609545a069d7b7_478.webp)
### Viewing the native editor
Most VST and Audio Unit plug-ins provide their own user interface. Click on the wrench icon in the top toolbar to open the native editor.
![](https://docs.cycling74.com/images/b799264dd2f38eb314549708dae7079c_630.webp) The native editor for the AUFilter Audio Unit
### Saving and restoring snapshots
You can save the current state of a plug-in as a [**Snapshot**](https://docs.cycling74.com/userguide/snapshots/), which will include the current value of all of the plug-in parameters. Click on the camera icon in the top toolbar to save the current parameter set to a snapshot. Click on the snapshot selection button in the top-right to list all saved snapshots.
![](https://docs.cycling74.com/images/c828abdf3716e418e1743c9c6620dfaa_515.webp) Viewing saved snapshots for the plug-in
The plug-in object UI does not provide any way to edit or delete snaphots. Select the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object and open the **Snapshot Sidebar** to edit the names of snapshots, or to delete a snapshot.
![](https://docs.cycling74.com/images/e292a3c0946106eca6203d6b7725154d_741.webp) With the vst~ object selected, open the snapshot sidebar to edit snapshots.
### Hiding the controls
The `@viewvisibility` attribute on a [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") or [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object determines whether or not the object will show an editable interface in the patcher. By disabling this attribute, you can get a much more compact representation of the wrapping object.
![](https://docs.cycling74.com/images/6e96330459f854ab43310b2b1c4985e5_369.webp) With @viewvisibility disabled, the object looks like a typical Max signal processing object.
