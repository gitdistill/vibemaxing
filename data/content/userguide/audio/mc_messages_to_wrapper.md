---
description: The wrapper holds one or more instances of an object. Using features specific to the wrapper, you can address all instances at once or target specific instances.
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_messages_to_wrapper/
title: Messages to the MC Wrapper
---

# Messages to the MC Wrapper
Most MC objects exist inside the [MC Wrapper](https://docs.cycling74.com/userguide/mc/mc_wrapper/). The wrapper holds one or more instances of an object. Using features specific to the wrapper, you can address all instances at once or target specific instances.
Finally, a powerful set of wrapper messages permit simultaneous high-level control of all object instances.
## Setting a Number of Object Instances Within the Wrapper
The `@chans` attribute sets the count of instances of an object `xxx~` within a wrapper object `mc.xxx~`. If the `chans` attribute has a value other than 0, the instance count is fixed and does not _auto-adapt_ to the maximum number of channels in any multichannel signal connected to its inlets. Typically `@chans` is a typed-in argument to a wrapper object.
## Changing the @chans Attribute
While the `@chans` attribute can be changed during the lifetime of an object, the actual multichannel outputs of the object will not update to reflect the new channel count until the audio is restarted.
In this example, if the `chans 4` message is sent to the [mc.*~](https://docs.cycling74.com/reference/mc.*~ "mc.*~") object while the audio is running, the output will not change. But if you turn the audio off and on again after having sent the `@chans 4` message, it will send a four-channel signal to the [mc.unpack~](https://docs.cycling74.com/reference/mc.unpack~ "mc.unpack~") meaning the four right outputs of [mc.unpack~](https://docs.cycling74.com/reference/mc.unpack~ "mc.unpack~") will change to 0.
![](https://docs.cycling74.com/images/dd055363d7f9d6e4bce41240fbe37c1c_637.webp)
## Setting Initial Values of Instances Within the Wrapper
If you simply type `mc.cycle~ 440` all [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") objects within the wrapper will have the initial frequency value of 440. To assign different initial values to wrapper instances, use the `@values` typed-in attribute. For example, `mc.cycle~ @chans 3 @values 440 660 880` would assign a frequency of 440 to the first [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object, a frequency of 660 to the second [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object, and a frequency of 880 to the third object.
You can combine both arguments if you want the first few objects to be set to different values but the rest set to a default value. For example, `mc.cycle~ 200 @chans 8 @values 440 660 880` would set the first three [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") objects to 440, 660, and 880 and the rest of the objects to 200.
## Sending Messages to All Instances Within the Wrapper
To send a message to all instances of an object within the wrapper, simply send the message. It will be sent to each instance. In this example, after clicking the message `660` connected to the [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~"), all 16 instances will have the frequency 660.
![](https://docs.cycling74.com/images/6649fb7e99daeee0681768a9933eade0_188.webp)
## Sending Messages to a Specific Instance Within the Wrapper
To send a message to a specific instance of an object within the wrapper, precede the message by the word `setvalue` followed by the instance number starting at 1. For example, after clicking the message `setvalue 1 660` connected to the [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~") shown below, the first instance will have a frequency of 660 while the remaining 15 instances will retain their initial frequency of 440.
![](https://docs.cycling74.com/images/55a1cd8c4c147cc0091655aa1a138a2f_187.webp)
You can also target specific instances with the [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target") object. Sending any message into the left inlet of [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target") outputs that message preceded by `setvalue` and the current channel (voice) number. Here is the same example as above. First the message `1` is sent to the right inlet of [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target"), then the `660` is sent. The [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target") object produces the message `setvalue 1 660`.
![](https://docs.cycling74.com/images/cdf30aa7f058a371ea8782873c52a461_289.webp)
Many event-based objects in MC follow a convention of sending a voice number out a rightmost outlet immediately before a message out a different outlet, making it possible to use [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target") to control specific object instances with these events.
## Applying a List of Values to Successive Instances Within the Wrapper
Use the `applyvalues` message a send single value within a list to successive instances within the wrapper. In this example, after clicking the `applyvalues 440 660 880` message box, the first instance of [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") within the [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~") object will have a value of 440, the second will have a value of 660 and the third will have a value of 880.
![](https://docs.cycling74.com/images/dab5e2e5568a272d4cf69e2c889541e2_188.webp)
In addition to applying numerical values, `applyvalues` can set single-valued message arguments and attribute values. In this example, the `@cutoff` attribute of each [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") instance is set to a different value based on the arguments to the `applyvalues` message sent to [mc.lores~](https://docs.cycling74.com/reference/mc.lores~ "mc.lores~").
![](https://docs.cycling74.com/images/bcb75b4d5729a6ad82a62369d98b4b33_265.webp)
When showing the inspector an MC Wrapper object, the values shown for an object's attributes are for the first instance only along with wrapper-specific attributes such as `chans`.
## Applying a Sequence of Values to Successive Instances Within the Wrapper
To apply a repeating sequence of values to all wrapper instances, use the `replicatevalues` message. With one argument, `replicatevalues` is the same as simply sending that value to all instances. With two or more arguments, `replicatevalues` cycles through the arguments applying them to each instance in succession. For example, clicking the `replicatevalues 1 2 3` message in this example will set all values of [mc.sig~](https://docs.cycling74.com/reference/mc.sig~ "mc.sig~") to a repeating cycle of 1, 2, and 3.
![](https://docs.cycling74.com/images/4492811890b59d90166506bf3f60af92_225.webp)
