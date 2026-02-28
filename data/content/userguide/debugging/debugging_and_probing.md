---
description: How to debug a Max patcher, and how to activate probe to inspect the data flowing on message, signal, and matrix patch cords
group: Debugging
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/debugging_and_probing/
title: Debugging and Probing
---

# Debugging and Probing
## Debugging
With **Debugging** , you can monitor any messages passing along a patchcord, or pause execution and walk through processing in the patcher step by step. Debugging starts with **Watchpoints** , which you can configure to _monitor_ , _print_ , or _pause_. To add a watchpoint, right-click on any patchcord and select _Add Watchpoint_ , or select a patchcord and select _Add Watchpoint_ from the _Debug_ menu.
  * **Print Watchpoint** : A Watchpoint that will print a message to the Max Console whenever a message passes through the patch cord. This message indicates the source and destination of the message, along with its contents.  ![A print watchpoint printing its message](https://docs.cycling74.com/images/9e9e3a2021a9abb71081776a70dded80_285.webp) A print watchpoint printing its message
  * **Monitor Watchpoint** : Display a popup in the Max patcher when a message passes through the patchcord.
  * **Break Watchpoint** : Pause execution and open the Debug Window whenever a message passes through the patchcord.  ![A break watchpoint pausing execution](https://docs.cycling74.com/images/5d6514dfe448c02fdb02d6804a63cd60_484.webp) A break watchpoint pausing execution. You can see that the value 13 has not yet reached the live.dial, which still displays the value 2.


## Enabling/disabling Debug Mode
Choose _Debugging_ from the _Debug_ menu to enable debugging. You can also use the _Debug_ icon in the bottom toolbar to toggle debugging, as well as enabling [**Illustration Mode**](https://docs.cycling74.com/userguide/illustration_mode/).
![](https://docs.cycling74.com/images/c4bb89b8a36f8483f4cc6ee054fc2c73_373.webp)
## Stepping Through
When a Break Watchpoint is triggered, execution pauses and Max will focus on the **Debug Window**. From here you can see the sender, receiver, and contents of the message that triggered the watchpoint.
After triggering a breakpoint, The _Continue_ button will let you resume execution, and the _Abort_ button will effectively remove the message from Max's scheduler and exit debugging. This can be really useful, especially if the message is about to do something that you don't want.
![The Continue and Abort buttons](https://docs.cycling74.com/images/35f54f935d06e368fc02ea277cbfa4dc_443.webp) The Continue and Abort buttons
The _Step_ button is a very powerful tool in the Debug Window, allowing you to walk through the flow of messages in a Max patcher one step at a time.
![The debug window showing the call stack during stepping](https://docs.cycling74.com/images/6480066df19b1e4be7317a404d67cbc0_517.webp) Pressing the step button moves through the patcher and adds layers to the call stack.
When stepping, whenever sending a message to an object triggers a new message, the new message will appear at the bottom of the execution stack. In this way, you can see the whole processing chain in response to a message.
If you are in the middle of debugging, you cannot operate your patcher. In addition, you cannot close the patcher window being debugged, and you cannot quit Max. To exit debugging and enable these functions again, choose _Abort_ from the _Debug_ menu, and you will be able to operate Max normally.
## Illustration Mode
  * Introduction
  * Activating illustration mode
  * Clearing pending messages


## Probing
Probing lets you see the last message that passed through a patch cord by hovering over the patch cord you want to inspect. With probing you can see messages, matrices and textures, as well as audio vectors passing between objects. _Event Probing_ , _Signal Probing_ , and _Matrix Probing_ must all be enabled from the _Debug_ menu before you can use them.
![Probing in the Debug menu](https://docs.cycling74.com/images/41057c4091c0766ad67f74c2fcba7be2_363.webp) Probing in the Debug menu
### Event Probing
With Event Probe enabled, hovering over any patchcord will display the last message that passed through, or else `no data` if no message has passed through.
### Signal Probe
The Signal Probe lets you see the audio data passing between two objects. With Signal Probe enabled, hover over any audio patch cord to get a visualization of the data. While the signal probe popup is visible, you can press the up or down arrow keys to cycle between **Meter** , **Scope** , and **History** views.
![The Signal Probe popup](https://docs.cycling74.com/images/4b988ad32e6fc5541df977fadf53c18c_519.webp) The Signal Probe popup (all three views).
Signal Processing must be enabled in order to use the Signal Probe.
The Signal Probe also works with **mc.** * objects.
![The Signal Probe with an mc object](https://docs.cycling74.com/images/4ac7d8f85b6b5132c8715caa49b5160e_519.webp) The Signal Probe with an mc object (all three views).
### Matrix Probe
Unlike the Signal Probe and Event Probe, the Matrix Probe displays in a separate window. Enabling _Matrix Probe_ from the _Debug_ menu will display the Matrix Probe window.
![Viewing a matrix with the Matrix Probe](https://docs.cycling74.com/images/659c176e58aedbf4e0601deaea17077e_520.webp) Viewing a matrix with the Matrix Probe.
From the _Window_ tab, the _Mode_ chooser will let you choose which plane of the matrix to inspect—alpha, red, green, blue, or a composite of all four.
![Choosing the plane to display](https://docs.cycling74.com/images/7bdea1caafc94f256dee48df992cfcb9_263.webp) Choosing the plane to display
The dropdown menus at the bottom of the window will let you view additional information about the matrix, including the number of planes, the type of data contained in the matrix, and the dimensions of the matrix.
![Get more information about the matrix](https://docs.cycling74.com/images/5010bb87aa0ecce708cc5821dec7fc8d_263.webp) Get more information about the matrix
The _Scope_ tab shows useful statistics about the matrix. For example, the _vectorscope_ view shows the distribution of color intensities, which can help you visualize which colors are most common in the matrix.
![The scope tab](https://docs.cycling74.com/images/936656b56c249d93000c64dba1937a32_720.webp) The *vectorscope* shows that red and orange are strong colors in the matrix.
