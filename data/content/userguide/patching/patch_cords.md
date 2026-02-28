---
description: Different kinds of patch cords, and the data they carry
group: Patching
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/patch_cords/
title: Patch Cords
---

# Patch Cords
The inlets and outlets Max objects are connected together using patch cords.
## Types of patch cords
There are six kinds of patch cords:
  1. Event - Messages sent between Max objects, handled by the [scheduler](https://docs.cycling74.com/userguide/scheduler/)
  2. Signal - Audio processed in blocks
  3. [MC](https://docs.cycling74.com/userguide/mc/) - Multichannel signals
  4. [Jitter matrix](https://docs.cycling74.com/userguide/jitter/matrix/) - Video and other multidimensional data, processed on the CPU
  5. [GL texture](https://docs.cycling74.com/userguide/jitter/textures/) - Multidimensional data residing on the GPU, part of [graphics processing](https://docs.cycling74.com/userguide/jitter/graphics_processing/)
  6. [Jitter geometry](https://docs.cycling74.com/userguide/jitter/geometry/) - Half-edge geometry structures


Patcher cords can be distinguished by their stripe patterns and colors.
![Patcher cord types](https://docs.cycling74.com/images/7d40852d470b3b60502817170975b5e9_562.webp)
## Creating Patcher Cords
You can connect objects with patch cords in a few ways:
  * Clicking on an inlet/outlet and dragging the mouse to another inlet/outlet
  * Clicking on an inlet/outlet and then clicking on another inlet/outlet
  * Hovering or selecting a patch cord, and then using the green or red circles by clicking or dragging to new inlets/outlets


To disconnect patch cords, you can:
  * Select a patch cord and use the backspace or delete key on your keyboard
  * Hovering or selecting a patch cord, and then dragging the green or red circle to an empty spot on the patcher window


When creating patch cords, if you hold shift as you finalize a connection, Max will automatically start a new connection from the same inlet or outlet. This can be _extremely_ useful when creating many patch cords from the same inlet/outlet.
## Editing Patcher Cords
### Selecting patch cords
Click on a single patch cord to select it. To select multiple patch cords, hold down `Option` (macOS) or `alt` (Windows) while drawing a selection rectangle. This will select objects as well as patch cords.
### Re-connecting patch cords
When a patch cord is selected, a green and red circle will appear next to the inlet and outlet. Click and drag on either of these to move the patch cord, leaving either the inlet or outlet connected.
![](https://docs.cycling74.com/images/dba468d1cdf0402d781b7a2024536aed_612.webp)
With this same technique, you can move multiple connections from one object to another.
![](https://docs.cycling74.com/images/477a1495d2df890091ee986e6e8637c2_912.webp)
You can also shift patch cords along the inlets or outlets of an object.
![](https://docs.cycling74.com/images/20fb5c0cffdcb9795278792190400cca_927.webp)
### Inserting/removing objects from a patch cord
Insert an object into the middle of a patch cord by holding `Shift` while dragging the object.
![](https://docs.cycling74.com/images/56e26ed429caab2ddea32f55031e36f4_497.webp)
You can also drag an object out of a patch cord by holding shift while dragging the object. This will only work if the object has a single connection to the first inlet, and a single connection to the first outlet.
### Patching mechanics
For mouse-free patching, Max supports [**Patching Mechanics**](https://docs.cycling74.com/userguide/patching_mechanics/). With this feature activated, you can do things like create and delete patch cords without using the mouse.
## Disabling patch cords
Right-click on any patch cord and select _Disable Patcher Cord_ in the contextual menu to disable it. Select _Enable Patcher Cord_ from the contextual menu to re-enable the patch cord.
![](https://docs.cycling74.com/images/645df4ff8c65148952044a5b4bed4880_217.webp)
## Viewing Patcher Cord Contents
### Enabling probing
With [**Probing**](https://docs.cycling74.com/userguide/debugging_and_probing/) enabled, you can view the contents of a patch cord by hovering over it. Max supports [**Event Probing**](https://docs.cycling74.com/userguide/debugging_and_probing/#event-probing), [**Signal Probing**](https://docs.cycling74.com/userguide/debugging_and_probing/#signal-probe), and [**Matrix Probing**](https://docs.cycling74.com/userguide/debugging_and_probing/#matrix-probe).
### Debugging patch cords
With **Debugging** enabled, you can attach [**Break Points and Watch Points**](https://docs.cycling74.com/userguide/debugging_and_probing/#enablingdisabling-debug-mode) to a patch cord. These will show the contents of a patch cord in a separate window, and pause execution when a message flows through a patch cord.
[**Illustration Mode**](https://docs.cycling74.com/userguide/debugging_and_probing/#illustration-mode) is another helpful way to visualize the flow of messages along patch cords.
### Extracting a [message](https://docs.cycling74.com/reference/message/ "message") from a patch cord
With the [**Event Probe**](https://docs.cycling74.com/userguide/debugging_and_probing/#event-probing) enabled, right-click on an event patch cord and select _Convert Last Message to Object_. This will create a message box containing the contents of the last message to pass through that patch cord.
![](https://docs.cycling74.com/images/9fe3780f41d02cd9eae7b951b593f0d2_904.webp)
## Styling Patcher Cords
### Segmented Patcher Cords
By default, patch cords are drawn in a curved style, but it is also possible to use a "segmented" style which has joints and corners. You can change the default style in the Max Preferences with the _Segmented Patcher Cords_ option. To create a segmented patch cord when the _Segmented Patcher Cords_ option is not checked in the Max Preferences menu (or to create a curved patch cord when Segmented Patcher Cord is enabled), hold the Shift key down when clicking on an outlet.
When creating segmented patch cords, click at each point where you want the patch cord to bend, and then click on the inlet/outlet of the other object.
To correct a segmented patch cord while you draw, Option-click (macOS) or Alt-click (Windows) to erase the most recent patch cord line segment. To remove a patch cord completely, command-click (macOS) or control-click (Windows) anywhere in the Patcher window.
To automatically create a segmented patch cord from a curved patch cord, right click on the patch cord and select _Align_. To automatically create route a segmented patch cord around objects, instead, select _Route Patch Cord_. To change a segmented patch cord to a curved one, right click on the patch cord and select _Remove All Segments_.
If you are making a segmented patch cord and want to make a corner over an object, hold down the control key to disable the normal auto-connection feature.
### Coloring patch cords
Patch cords can be individually colored, or styled as a whole using the [**Format Palette**](https://docs.cycling74.com/userguide/format_palette/).
To color an individual patch cord, or a selection of patch cords, select all of the patch cords that you want to color and right-click on one to open the contextual menu. Select _Color..._ to open the color picker.
To style all of the patch cords in a patcher at once, open the Format Palette and edit the _Patchline Color_.
### Aligning and routing patch cords
With one or more patch cords selected, open the _Arrange_ menu and select _Auto Align_ to create aligned, segmented patch cords.
![](https://docs.cycling74.com/images/55d88d012a83ba92a3ce382f128c4648_485.webp)
You can also route patch cords automatically, creating segmented patch cords that move between objects. With one or more patch cords selected, open the _Arrange_ menu and select _Route Patcher Cords_.
![](https://docs.cycling74.com/images/3b2535ef990dd0b4260188ab8b8c3908_352.webp)
### Hiding patch cords
To hide patch cords in locked patcher mode, right click on a patch cord and select _Hide on Lock_. To make hidden patch cords visible again, right click on the patch cord and select _Show on Lock_.
