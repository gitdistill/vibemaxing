---
description: Understanding preview mode while editing Max for Live devices
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_preview/
title: Preview Mode
---

# Preview Mode
After opening a Live device in Max for editing, there are two copies of the device -- the one you are editing and the one inserted into a track in Live. _Preview Mode_ permits you to listen to the device you are editing while Live runs in the background. The copy of the device inserted in the Live track is disabled. Audio, MIDI, timing, and messages (including [Live API](https://docs.cycling74.com/userguide/m4l/live_api/) commands) are sent between Max and Live in order to make this happen. Preview Mode is always enabled when you begin to edit a device in Max.
## Enabling and Disabling Preview Mode
  * To toggle preview mode, click the preview icon. When preview mode is disabled, the icon in the toolbar is gray.
  * You can also turn preview mode off by clicking the edit button in the Live device's title bar. However, this also has the effect of closing the device in the editor.


## Uses of Preview Mode
  * You can turn preview mode off as you are editing a device to compare the edited version of a device with the original version.
  * You can turn preview mode off after saving a device to see how its user interface appears in the Live device view.
  * Preview mode will increase the latency of a Live device slightly. Turn preview mode off to hear the device with its original defined latency.


## Preview Mode Caveats
  * The memory state of Max objects is not made consistent between devices as you enable and disable preview mode. For instance, if you change a number box to 74 in a device in Live and then edit the device, the number box will be set to zero when the edited version is opened.
  * However, [parameter state](https://docs.cycling74.com/userguide/m4l/live_parameters/) will be updated when toggling preview mode. If you set a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") to 47 in Max, then disable preview mode, the dial will be updated to 47 in Live. If you then set the dial to 61 in Live, then enable preview mode again, the dial will be updated to 61 in Max.
  * Changes to parameter values in Max while in preview mode are undoable in Live.
  * Preview mode implements communicating between a [send](https://docs.cycling74.com/reference/send/ "send") object in Live and a [receive](https://docs.cycling74.com/reference/receive/ "receive") object in Max (or vice versa), but the performance of the communication will be reduced compared to the performance of [send](https://docs.cycling74.com/reference/send/ "send") and [receive](https://docs.cycling74.com/reference/receive/ "receive") within a single application.
  * The [grab](https://docs.cycling74.com/reference/grab/ "grab") object cannot communicate with a [receive](https://docs.cycling74.com/reference/receive/ "receive") object unless both objects are in the same device, so you cannot use [grab](https://docs.cycling74.com/reference/grab/ "grab") to communicate between devices in preview mode.
  * Some Max objects monopolize a resource on your computer. The [udpreceive](https://docs.cycling74.com/reference/udpreceive/ "udpreceive") object, for example, reserves a UDP port for itself so that no one else can access the port. This has the potential to create problems when you have two [udpreceive](https://docs.cycling74.com/reference/udpreceive/ "udpreceive") objects in two copies of the same device. In this specific case, we have made the UDP objects release the port when they are disabled as a result of a preview mode switch. However, other third-party objects with similar resource-monopolizing issues may not work properly with preview mode.
  * Max objects that share data via symbolic names, such as [table](https://docs.cycling74.com/reference/table/ "table"), [coll](https://docs.cycling74.com/reference/coll/ "coll"), and [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), do not share data across the boundary between Max and Live. For instance, if you have sample data loaded into a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object named `toto` in Live, and you edit another device with a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object named `toto`, the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object in the device in Max will not share data with the object in Live.


