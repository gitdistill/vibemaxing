---
description: Working with game controllers
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/communicationschapter01/
title: Human-Interface Devices
---

Download Series Content and Patchers
# Communications Tutorial 1: Human-Interface Devices
## Introduction
This tutorial covers the use of the Max [hi](https://docs.cycling74.com/reference/hi/ "hi") object, an interface with HID devices connected to your computer. We will see how to discover, select and process data from these common devices.
The HID (Human Interface Device) protocol allows a physical controller to connect to a computer without device-specific drivers. The computer is able to query the device for information about itself, and can present this information to the user. HID-compliant controllers include joysticks, gamepads, some mice and graphics tablets, touchscreens, and a wide variety of other interfaces designed to communicate with the computer for real-time control.
While HID devices are typically designed for use by the gaming community, they are often used by Max performers, since they tend to be inexpensive and flexible; the most common HID device is a game-style joystick, which can provide an extraordinary number of interface tools in a small, portable package.
## Understanding the [hi](https://docs.cycling74.com/reference/hi/ "hi") interface
Take a look at the tutorial. This entire patch is based around the [hi](https://docs.cycling74.com/reference/hi/ "hi") object – Max’s interface with HID devices. This object provides all of the information we need to interface with joysticks, drawing pads and other controllers. In order to see the devices that are available to the [hi](https://docs.cycling74.com/reference/hi/ "hi") object, click on the `info`[message](https://docs.cycling74.com/reference/message/ "message") box. The [hi](https://docs.cycling74.com/reference/hi/ "hi") object will respond by listing all of your available HID devices (as well as some information on them) in the Max Console.
The list begins with version information and a count of all the available HID devices. You will probably be surprised to see that your computer already has a number of devices available. Each of these devices is listed by name, followed by a notation of the number of _elements_ for that device. Elements are the individual control parameters available from the device; for example, a simple game controller might include four joystick elements (two joysticks with two axes each), six or more button elements and other assorted controls. There are often more elements than physical controls – these might be for device feedback, or for communication with the connected computer.
We will want to have the [hi](https://docs.cycling74.com/reference/hi/ "hi") object focus on a single device (in our tests, we used a _Logitech Dual Action_ game controller). You can send a message to the object with the name of the HID device, but it is easier to let the [hi](https://docs.cycling74.com/reference/hi/ "hi") object propagate a [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") with the available devices, and use that to select a controller. This is what the `menu` message does – when you click on that [message](https://docs.cycling74.com/reference/message/ "message") box, the right outlet of the [hi](https://docs.cycling74.com/reference/hi/ "hi") object outputs the messages necessary to load a [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") with the names of the devices. Taking the second output of the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") and sending it back to the [hi](https://docs.cycling74.com/reference/hi/ "hi") object will allow you to select a device. When you select a menu option, you will notice that the Max Consoles says “ [hi](https://docs.cycling74.com/reference/hi/ "hi") : focusing on your device name”.
## Polling and data
The [hi](https://docs.cycling74.com/reference/hi/ "hi") object is unlike MIDI interfaces – rather than producing a stream of messages, it waits to be _polled_ (by sending it a `bang` message), then outputs any changed values. In the second section of the tutorial patch, you can see that we’ve set up a [metro](https://docs.cycling74.com/reference/metro/ "metro") with a `20` ms interval to poll the [hi](https://docs.cycling74.com/reference/hi/ "hi") object. If you’ve selected a device, you should now be able to move your controller and see the results displayed in the [number](https://docs.cycling74.com/reference/number/ "number") boxes below the [hi](https://docs.cycling74.com/reference/hi/ "hi") object. The output is a pair of numbers: the first number is the `element` index, while the second number contains the last `value` received from that element.
Another option for polling the [hi](https://docs.cycling74.com/reference/hi/ "hi") object is to use its built-in timer; to do this, you send it a `poll` message with an argument for the polling interval. This is a convenient way to set up the [hi](https://docs.cycling74.com/reference/hi/ "hi") object with as few additional objects as necessary. Turn off the [metro](https://docs.cycling74.com/reference/metro/ "metro"), then click on the `poll 20` message – you will see that the values are still output, based on the object’s ability to self-poll.
While the [hi](https://docs.cycling74.com/reference/hi/ "hi") object is running, let’s use the output to determine the elements that are available with the device you are using. The patch has a [comment](https://docs.cycling74.com/reference/comment/ "comment") box that lists some common elements available with a game controller: in this case, a two-stick control with a four-button game pad. Identifying the available elements is the first step to making a useful Max program for your HID device. Operate the controls on your HID controller, and watch the element/value pair. Each move you make, whether a continuous control or a button push, should produce output. If you are having problems seeing all of the element/value pairs, you could connect a [print](https://docs.cycling74.com/reference/print/ "print") object to the out of the [hi](https://docs.cycling74.com/reference/hi/ "hi") object to view all of the output. If your HID device does not match the parameters listed in the tutorial patch, you will need to determine which controls are available and useful to you.
## Routing data for the applications
Once you have a list of controls that work for your HID device, you can use them to control the rest of your application. In our tutorial patcher, the [route](https://docs.cycling74.com/reference/route/ "route") object is the perfect tool: it routes messages by the first item in a list (in this case, the element index), and conveniently strips it off for us as well.
In this case, we use two elements (`20` and `21`, the joystick X and Y) to conduct the drawing, two elements (`6` and `8`, the top and bottom gamepad buttons) for sizing the drawn circle, and two more elements (`5` and `7`, the left and right gamepad buttons) for clearing and randomizing the color. If you look at the contents of the subpatchers, you will find that the programming is very similar to what we’ve used in previous drawing patches. Since the [hi](https://docs.cycling74.com/reference/hi/ "hi") object has turned complex game controller movements into a simple stream of numbers, we can use it for any processing that Max can perform.
## Summary
The HID protocol allows a standardized interface between a computer and relatively inexpensive hardware. The [hi](https://docs.cycling74.com/reference/hi/ "hi") object give a Max programmer the ability to use these devices for controlling and manipulating their performance patches. Since there are useful HID devices for almost any task, [hi](https://docs.cycling74.com/reference/hi/ "hi") provides an easy interface into physical control of your system.
## See Also
  * [hi - Human Interface (gaming) device input](https://docs.cycling74.com/reference/hi/)



Kind
    Tutorial 

Category
    Communication 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
