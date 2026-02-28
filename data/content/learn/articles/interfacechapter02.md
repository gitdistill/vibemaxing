---
description: Designing user interfaces with custom image elements
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/interfacechapter02/
title: Picture UI Elements
---

Download Series Content and Patchers
# Interface Tutorial 2: Picture UI Elements
## Introduction
This tutorial covers the creation of custom controls using your own pictures. This function is provided by the [pictctrl](https://docs.cycling74.com/reference/pictctrl/ "pictctrl") and [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") objects, which use specially formatted pictures to give you customizable user interfaces.
Changing the colors and sizes of user interface elements can only get you so far when creating custom interfaces. The [pictctrl](https://docs.cycling74.com/reference/pictctrl/ "pictctrl") and [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") objects take it to the next level: virtually any graphic can be used to create switches, sliders and state indicators. However, in order to get the best possible result, you will have to format the images to make them conform to the objects’ requirements.
## Overview of the tutorial patcher
If you take a look at the tutorial patcher, you will see four rather silly pictures. In order to see the patch at work, click on the cellphone – it starts the [metro](https://docs.cycling74.com/reference/metro/ "metro"), which animates all of the other graphics. The cellphone is obviously acting like a momentary _switch_ , the ring is a _slider_ (following the output of a [drunk](https://docs.cycling74.com/reference/drunk/ "drunk") object), the thumb is a yea/nay indicator (another type of _switch_), and the eyes are a multi-state indicator (jumping to the value of the [random](https://docs.cycling74.com/reference/random/ "random") object's output). Click on the cellphone again, and the whole operation will cease. Let’s look at each of these controls to see what is causing it to work.
The cellphone image, our momentary button, is made of two images – the plain cellphone and one with the backlight turned on. If you watch the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object connected to its output, you see that the output is `1` when you click the control, and `0` when you release the mouse. Using the [select](https://docs.cycling74.com/reference/select/ "select") object at the output allows us to trigger the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") controlling the [metro](https://docs.cycling74.com/reference/metro/ "metro").
While the [metro](https://docs.cycling74.com/reference/metro/ "metro") is off, let’s look at some of the other controls. They are all being driven by [random](https://docs.cycling74.com/reference/random/ "random") -like objects, but they can be manually changed as well. Click and drag on the ring, and you will see that it acts like a horizontal slider – the output connected to the [number](https://docs.cycling74.com/reference/number/ "number") box provides a current value output when manually changed. In this case, there are `128` steps tracked by the object.
The thumb image can also be controlled manually: When you click on it, it becomes neutral. When you release the mouse button, it reverses state. The eyes are similar, but change when you drag and click on the image. There are only a few frames, so it might be convenient to use the [number](https://docs.cycling74.com/reference/number/ "number") box above it to change the value in a more controllable way.
## Swapping images and settings
Let’s play with some of the setting of the cellphone switch. Unlock the patch, select the cellphone and open the object inspector. You will see a large number of attributes available for this object; let’s start by playing with the object sizing. As provided in the patch, there is no way to change the object size: you can mouse around the bottom-right of the object, but the grow box will never be displayed.
In the inspector, you will see that an attribute named `Snap Size to Picture Size` is turned on. This attribute defeats user-based sizing; rather, it forces the object to be the size of the source image. If you turn off this attribute, the object can be resized, and the image will scale to match the sizing of the image.
Sometimes you will want to try certain images for buttons, but you may have to try several images for it to be right. You can change the image file by looking in the _image_ section and clicking on the **Choose…** button for the `Image File` attribute. As an example, click on **Choose** , navigate to the Max folder on your disk, then go to the _patches/picts_ folder and select the `boring button.pct` image. This is more of a stock button image, and it replaces the cellphone button completely.
Click on the ring finger slider object, and look at the changes in the inspector. This is a different object (the [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") object), and it has a different set of attributes; most notably, two different images are used for the display. The background image (in this case, the finger) can be used to set the size of the object, while the ring image can be scaled or replaced separately. Click on the **Choose** button for the `Knob Image File` of the [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider"), move to the _patches/picts_ folder, and select the "smiley2.pct" file. It will immediately show both smiley faces; one of these is the _clicked_ image, so you need to click on the `Has Clicked Image` attribute to make it look right. Now, instead of moving a ring around the finger, you are sliding a face. You may want to try changing the `Bottom Margin` attribute to center the face correctly for this image.
## Resizing and reformatting
There are a variety of object attributes that require specific image formatting. For example, attributes such as `Has Image Mask` and `Has Clicked Image` require that the source file be specially formatted to support those options. If you have an image editor available, you might want to open the _thumbtoggle.pct_ and _eyedial.pct_ files to see how the complexity of a file increases when certain options are selected. The “eyes” [pictctrl](https://docs.cycling74.com/reference/pictctrl/ "pictctrl"), which supports _dial_ mode, also provides an example of attributes that are only able in dial mode.
To get more information about the image formats for the [pictctrl](https://docs.cycling74.com/reference/pictctrl/ "pictctrl") and [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") object, open the help file for each and select the `picture_format` tab to see how an image has to be created for it to be a valid controller. If most of the special features are not used, the image can often be fairly simple, but more robust controls require more complex images – especially if a mask is used to provide transparency.
## Summary
Covering all of the custom UI options made available by [pictctrl](https://docs.cycling74.com/reference/pictctrl/ "pictctrl") and [pictslider](https://docs.cycling74.com/reference/pictslider/ "pictslider") is beyond the scope of this tutorial. However, you should be able to see how the user interface of a patch can be completely altered by using custom image-based elements. While proper creation of the images can be difficult, the effort allows for complete control of the visual control environment.
## See Also
  * [pictctrl - Picture-based control](https://docs.cycling74.com/reference/pictctrl/)
  * [pictslider - Picture-based slider control](https://docs.cycling74.com/reference/pictslider/)
  * [decide - Choose randomly between on and off (1 and 0)](https://docs.cycling74.com/reference/decide/)



Kind
    Tutorial 

Category
    User Interface 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
