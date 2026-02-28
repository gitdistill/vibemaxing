---
description: Using Plugin Processors within MSP
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/16_pluginchapter01/
title: Plugin Effects
---

Download Series Content and Patchers
# MSP plug-in Tutorial 1: Effects
## The Wonderful World of plug-ins
Even though we can build just about any audio effect we want to in Max, sometimes what we are looking for is too complex, would take too much time, or isn't really in our area of expertise. For those situations, there is the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object, which lets us install the same plug-ins we use in our DAWs in Max. Despite its name, the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object can host either VST or AudioUnit plug-ins. This gives us access to litereally thousands of of audio processors and instruments. Some of these are startlingly expensive, but many are free. An internet search will hunt them down—there are several sites such as [KVR audio](http://www.kvraudio.com) that list them and let you search by criteria such as platform and function. Most music producers quickly acquire a library of dozens of plugs.
The [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object defaults to two inputs and two outputs. You can accomodate more with arguments. First is number of inputs, second is number of outputs.
## Loading a plug-in
There are no plug-ins shipped with Max, so you will need to acquire your own in order to explore the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object. For demonstration purposes, a reverb plug called Freeverb3_Hibiki_Reverb will be loaded. That is a nice open source reverb that will complement the Max objects.
  * Open the tutorial patcher
  * Note the yellow tinted [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object in the right corner of the patch. Before you do anything, you must load a vst plug-in to this object. The easy way to find a plug-in is to click on the plug icon on the left toolbar. This will open a list of all plug-ins installed on your computer. Select a processing plug-in and drag it to the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object. This list is also shown under the files catergory of the object action menu at the left end of the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object. If the plug you want is not shown, click the `plug` message. This will open a file dialog to let you find the plug-in. (You can also type the plug-in file name as an argument to the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object.) If you save a patch with a plug-in loaded, that plug (but not necessarily its settings) will be installed when you reopen it.
  * Click the `open` message. The plug-in's interface window should appear.


Now you can apply audio to the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object and see how the plug-in sounds. Change the controls to see how the sound is affected. As you work the controls, messages will appear in the patcher with the number of the parameter that is changing and its value.
There are two basic commands that are useful when you are tweaking the parameters in a plug-in:
  * `bypass` 1 will as the name implies, bypass the processor entirely. Input signal will simply be passed to the output. This is essential to hearing exactly what the plug is doing to your sound.
  * `disable` 1 shuts down DSP within the plug, and the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object wil output 0s. Some plug-ins have significant processor load, so this is a good way to switch between alternate plug-ins.


Sometimes the interface supplied with a plug-in is a bit convoluted, perhaps with awkward controls or with the controls spread over several pages. The message `genericeditor 1` will cause the `open` message to use a very plain but highly informative interface. (Not available on all AudioUnits.)
![](https://docs.cycling74.com/images/7fd06a68b4f04ac7aaea74277597027f_310.webp) A plug-in interface window ![](https://docs.cycling74.com/images/1f36acb9fd5e177489af99a8a197e3e5_532.webp) A generic plug-in interface window
## Changing parameters from Max
  * Open the `Working_with_parameters` subpatch by double-clicking on it. 
  * Click the `params` message. 


There will now be a list of parameters for the plug-in in the Max console. Furthermore, the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") labeled "Choose parameter" will be populated with parameter names. If you pick one, changing the number box labeled "Set parameter" will change the setting. (You should see controls move in the interface window when you do this.)
The `params` message to the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object produces a series of names from the 3rd outlet. Each parameter has a number, and they appear in this order (starting with 1). (Note how the [prepend](https://docs.cycling74.com/reference/prepend/ "prepend")`append` object funnels these into the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu"). Also note the clear message that is sent to [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") first.) A list with the name or number of a parameter followed by a value will change the setting. The values sent are always between 0 and 1—you will have to discover how these translate to the values shown in the plug interface on your own. Another thing you will have to discover is what the parameters actually do. The names we get may not match the labels in the interface. Hopefully, there will be some kind of documentation.
![](https://docs.cycling74.com/images/a2af3ce08568b20f641f074b78b7a863_490.webp) Fetching parameter names from a plug-in
The current value of a parameter can be obtained by a `get` command with the parameter number for an argument. The result appears at outlet 4. There are various aspects of a plug-in besides parameters that can be queried, such as whether a plug will work in mono. These use negative parameter numbers and are listed in the reference.
Some plug-ins have parameters like delay time that can link to the tempo of the host DAW. In Max, these will be linked to the `global transport`. A few plug-ins have parameters that will respond to MIDI controls—passing MIDI to plug-ins is covered in the [next tutorial](https://docs.cycling74.com/learn/articles/16_pluginchapter02/)
## Programs
  * Open the `Working with programs` subpatch


Most plug-in come with built in settings called programs or presets. These can be called up simply by sending an integer to the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object. The message `pgmnames`, or possibly `presetnames` will produce the names from the sixth outlet. These can be captured into a [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") in the same manner as before. They come in order, starting with number 1. Since the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") numbers items from 0, 1 has to be added to the left ouput to call up the preset that matches a name.
![](https://docs.cycling74.com/images/c34db5f832b0e77275db464fc942cd7c_584.webp) Fetching plug-in program names
If you make changes to any of the programs, you can save your version and reload it later:
  * The message `write` will open a file dialog. You can choose to save the active program, or the entire bank.
  * The message `read` will open a dialog to retreive what you have saved. If you load a single program, it will overwrite the currently active program, so you may want to choose an empty slot before reading.
  * The message `set` with a name will rename the active program. You should do this when you have read a progam back in for the first time, then save it again. Otherwise it will have the name of the program you began with.


The programs will be restored to the shipping versions when the plug-in is removed from [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") and reloaded.
There is no standard usage of the words "preset" and "program". The Steinberg VST specification refers to a collection of parameter settings as a program, but the Apple Audiounit specification uses the word preset. So some plug-ins will respond to `pgmnames` and some (particularly AU plugs) will respond to `presetnames`. Other plug-ins make a distinction between factory programs and user defined presets. Some plugs which have their own file management system will not respond to either.
## Latency
Every software process takes time. In the case of audio processers, computation time creates a delay in the signal, called _latency_. Latency can be unimportant, or it can be critical depending on how the signal is used. The worst case is where a processed signal is mixed back with the original—that will often cause echos or comb filtering. The command get -10 will return the latency of the plug-in in samples. You can use this value to delay the original signal input to a mix. It's too bad there is no time travel object in Max to remove latency instead.
## Summary
Standard VST and AudioUnit plug-ins can be loaded into the [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") object for use with MSP objects. In addition to features offered by the plug-in's own interface, parameters may be modified by Max operations and edited programs may be saved and reloaded.
## See Also
  * [vst~ - Load VST and AU plug-ins](https://docs.cycling74.com/reference/vst~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
