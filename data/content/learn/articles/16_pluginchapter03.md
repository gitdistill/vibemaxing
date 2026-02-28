---
description: Using Max for live patches within MSP
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/16_pluginchapter03/
title: AMXD devices
---

Download Series Content and Patchers
# MSP Plugin Tutorial 3: AMXD Plug-ins
## Max for Live in Max
Max for Live allows Maxers to create patches that can be used in Ableton Live projects. Many folks have created clever and interesting patches and are sharing them in as .amxd flies. The [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object allows us to add these files to Max patchers, using them as plug-ins.
## The [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object
![](https://docs.cycling74.com/images/b37c3f47d2efd0b8a4e9d450e789dcfd_88.webp) An empty {amxd~} object
The bare [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object is not very impressive, as it consists of nothing but inlets and outlets. Before it can be used, it must be loaded with an .amxd file. These can be found in the _plug-ins_ toolbox on the left toolbar—select Live Device as the type, find the one you want and drag it onto the [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object. Note that unlike VST plug-ins, Live Devices can only be loaded when the patcher is unlocked. When you load one, the object will expand to contain the device's user interface:
![](https://docs.cycling74.com/images/98c884d0b3883c0a57a1461730363bc0_261.webp) A loaded Live Device
A live device only needs a few connections to work. For an effects device, all that is required is audio in and audio out.
![](https://docs.cycling74.com/images/7922b674344f3bf67dd58c879e367295_339.webp) A Live Device in a patch
As you can see, the device presents a complete interface. The little plus sign even saves a snapshot for you. This will be kept if the patch is saved and closed. (Click the bullseye to return to the saved settings.) Parameter access is very much like the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object:- Double click on the `Parameters` subpatch in the blue region of the main patch.
![](https://docs.cycling74.com/images/8a86aaca27802fd8169ad1fe5946b720_697.webp) Accessing paramters in a Live Device
The `getparams` message returns a list of all parameters from the right outlet. The parameter names are all preceeded by "info param", so those two words need to be stripped off by a pair of [route](https://docs.cycling74.com/reference/route/ "route") objects. In the subpatch, the names are used to stuff a [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object as described in [Plugin Tutorial 1](https://docs.cycling74.com/learn/articles/16_pluginchapter01/). You can then use the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") to choose a particular parameter to examine and set. Unlike parameters in [vst~](https://docs.cycling74.com/reference/vst~/ "vst~"), [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") parameters vary in range, so we need to be aware of the minimum and maximum allowable values when making adjustments. The `getinfo` message accompanied by a parameter name will retrieve the min and max values and possibly some other information. These also require some routing to place the numbers where they belong, over on the green side of the patch. `Getvalue` fetches the current setting of the named parameter. All of this happens when the parameter name is chosen. Adjusting the number box labeled "set parameter value" will do just that. Note it also repeats the most recent `getvalue` request to keep that display up to date.
## Live Device softsynths
The right half of the tutorial patch has an example of a synthesizer Device. As you can see, it responds to `midievent` messages as described in [Plugin Tutorial 2](https://docs.cycling74.com/learn/articles/16_pluginchapter02/). Most Live Devices are fairly simple, so they won't necessarily respond to a wide range of messages. It's really up the author of the patch. Getting exterrnal MIDI into an [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") is simpler than with [vst~](https://docs.cycling74.com/reference/vst~/ "vst~"). All we need to do is connect a [midiin](https://docs.cycling74.com/reference/midiin/ "midiin") object directly to the right inlet. All of the parsing chores are handled internally.
## Deconstructing Live Devices
Since amxd devices were originally Max patches, why can't we open them up and see what makes them tick? Well, in fact we can.
  * Right click on the loaded device and choose `Open Original` from the `Objects` submenu.

![](https://docs.cycling74.com/images/b645de1b0b498c674047d592e5472298_540.webp) Live Device source patch
The first thing you will see is a patcher in presentation mode. Switch to patching mode, and the internal logic will be revealed. This is actually a rather complex patch, with a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") based FM synthesizer and several subpatches full of logic to handle MIDI and midievent parsing. The only special objects are the [plugout~](https://docs.cycling74.com/reference/plugout~/ "plugout~") and various M4L user controls.
## Summary
The [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object completes the circle of Max to Live, allowing us to bring patches created in Max for Live back to Max. Live Devices function as simple plug-ins.
## See Also
  * [amxd~ - Load Live Devices into a Max patch](https://docs.cycling74.com/reference/amxd~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
