---
description: Chromakeying
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter10/
title: Jitter Tutorial 10
---

Download Series Content and Patchers
# Tutorial 10: Chromakeying
This tutorial explains how to perform chromakeying with two source movies using the [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") object. We will also learn how to find out the color of any pixel on the screen with the [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") object.
When you open the tutorial patch, Max will automatically read two movies (_oh.mov_ and _traffic.mov_) into two [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") objects by sending appropriate `read` messages to those objects with a [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") :
![Initializing the patch via  loadbang .](https://docs.cycling74.com/images/c06c369e6c28996a0ea9de6aca96a261_523.webp) Initializing the patch via loadbang .
Additional parameters we need for this patch are also initialized by the [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang"), which is connected to the [message](https://docs.cycling74.com/reference/message/ "message") box on the right of the patch. The [message](https://docs.cycling74.com/reference/message/ "message") box initializes the rest of the patch by sending messages to named [receive](https://docs.cycling74.com/reference/receive/ "receive") objects elsewhere in the patch. (See Tutorial 16: [Remote Messaging](https://docs.cycling74.com/learn/articles/basicchapter16/) — Sending messages without patchcords).
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box to start the [metro](https://docs.cycling74.com/reference/metro/ "metro"). You should see images appear in the three [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") objects in the patch. Note that the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box not only starts and stops the [metro](https://docs.cycling74.com/reference/metro/ "metro"), but also starts and stops the movie transport of the two [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") objects.


The lower half of the tutorial patch (with two of the three [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") objects) looks something like this:
![The  jit.chromakey  object](https://docs.cycling74.com/images/dce988be849850406ffff8aecc8b6529_362.webp) The jit.chromakey object
  * Click with the mouse on the blue region of the left-hand [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object (i.e. the area behind the man's head in the movie). 


The third [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object (in the lower-right hand of the patch) will look like this:
![How the heck did he get in front of that fence?](https://docs.cycling74.com/images/10e289fcce88a8ea23fb30eb8f13c902_321.webp) How the heck did he get in front of that fence?
_**Historical note:**_ ** Bluescreen compositing, or the process of shooting live footage against a blue matte background only to replace the blue with a separate image later, has been around since the late 1930s. Originally a very expensive film process involving lithographic color separation, bluescreen (and its now more common sibling, greenscreen) has evolved into the most commonplace special effect in film, television, and video. The ability to perform chromakeying (the technical term for the process) using digital superimposition has only made it more ubiquitous. Video chromakeying is often referred to in the television industry as CSO (Colour Separation Overlay), the name given to the process by the BBC team that developed it in the 1960s. Petro Vlahos, a bluescreen innovator in the 1960s, was awarded a Lifetime Achievement Award by the Academy of Motion Picture Arts and Sciences in 1994, an acknowledgment of how indispensible the technology had become. 
## The jit.chromakey object
_Chromakeying_ —the process of superimposing one image on top of another by selective replacement of color—is accomplished in Jitter by the [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") object. By specifying a color and a few other parameters, [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") detects cells containing that color in the first (left-hand) matrix and replaces them with the equivalent cells in the second (right-hand) matrix when it constructs the output matrix. The result is that cells from the first matrix are superimposed onto the second. 
  * Since any color is fair game for the chromakey, try clicking elsewhere in the lefthand [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"). Different colors will be knocked out of the man's face to reveal the traffic.

![The disappearing face trick \(part one\)](https://docs.cycling74.com/images/093df1308f04050c5b446efce4861af8_318.webp) The disappearing face trick (part one)
The [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") object uses the `color` attribute to define the center color to in the chromakey (called the reference color). This attribute is set as a list of values for as many planes as exist in the matrices that are being keyed. The `tol` attribute specifies a range of values around the key color. Colors within this range will be keyed as well. When using [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") with _char_ matrices (e.g. video), the attributes are specified in a floating point range `0` to `1`, which is then mapped to the 0-255 range necessary for _char_ data. To set the `color` attribute for a solid green chromakey, therefore, you would set the attribute as `color 0 0 1.0 0`, not `0 0 255 0`. A `tol` range of `0.5` will key all values within half of the chromatic distance from the reference color (computed as the sum of the absolute differences between the reference color and the actual cell value in each plane). A `tol` range of `0` will treat only the exact reference color as part of the chromakey. 
  * Try clicking on the blue region in the lefthand movie again, and play with the `tol` attribute to see how the chromakey output changes. At low tolerance, some of the bluescreen in the left image will remain in the keyed output. At a very high tolerance, parts of the man's face may disappear.


In the tutorial patch, the `color` attribute to [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") is set by clicking on an invisible object. If you unlock the patch, you will see a region of concentric red squares that sit on top of the left-hand [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object:
![The  suckah  object](https://docs.cycling74.com/images/026abe36056908dfa2f01eb5950c0fb1_249.webp) The suckah object
The region is a Max user interface object called [suckah](https://docs.cycling74.com/reference/suckah/ "suckah"), which appears on the add object:interface palette like this:
![The  suckah  object in the object palette](https://docs.cycling74.com/images/dadf18e1f33e34d5245e2c5ceaec1b13_414.webp) The suckah object in the object palette
The [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") object will report the RGB values of any pixel on the screen that the [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") object overlays. It reports these values as a list of floats in the range `0.0` to `1.0` when you click in the object in a locked patch. For example, clicking on a region of solid blue that has a [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") on top of it will cause the [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") to send out the list `0 0 1.0`. (The first version of [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") used the range 0 to 255 for output. There is a checkbox in the inspector if this behavior is desired.)
To set the `color` attribute for our [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") object, we take the RGB list that comes out of the [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") object and send it through a [prepend](https://docs.cycling74.com/reference/prepend/ "prepend")`0`, which adds an alpha value of `0` to the front of the list. The message is then completed by the [prepend](https://docs.cycling74.com/reference/prepend/ "prepend")`color` and sent to [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey").
## Keying options
The [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") object has additional attributes: `minkey`, `maxkey`, and `fade`. When a matrix arrives in the left inlet, [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") creates a greyscale (1-plane) mask internally, based on that matrix. Cells in the incoming matrix that have color values within the tolerance (`tol`) range are set to the `maxkey` attribute's value (the default is `1`) in the mask. Regions outside the tolerance range are multiplied by the `minkey` attribute (default is `0`). If the `minkey` and `maxkey` are set to `0` and `1`, the resulting image should look white where the keying should take place, and black where the original image is to be retained.
The resulting mask and its inverse are then multiplied by the right and left matrices, respectively. The results of the multiplication are then added to form the composite image. The following diagram shows you a pictorial overview of the process:
![The two sources, their masks \(with  minkey  at  0  and  maxkey  at  1 \) and the composite chromakey.](https://docs.cycling74.com/images/1c6a27c4bbc79f6d849250d02c1fa6f7_528.webp) The two sources, their masks (with minkey at 0 and maxkey at 1 ) and the composite chromakey.
As you can see, the `maxkey` attribute sets the strength of the righthand matrix in the output, while the `minkey` attribute sets the strength of the lefthand matrix. If we were to reverse the `minkey` and `maxkey` attributes, the chromakey would be reversed, and the following would happen:
![The composite effect with the  minkey  at  1  and the  maxkey  at  0  \(reverse chromakey\).](https://docs.cycling74.com/images/ede2016a2849e0aa7e4934c35b770e66_528.webp) The composite effect with the minkey at 1 and the maxkey at 0 (reverse chromakey).
The `fade` attribute allows for an amount of interpolation between the area being keyed and the area not being keyed. This lets you create a soft edge to the chromakey effect. Colors in the left matrix that are slightly out of bounds of the key tolerance range, yet that are within the range of `tol` + `fade` from the reference color, are interpolated between their original (unkeyed) color and the color in the same cell of the right matrix. The amount of interpolation is based on how great the `fade` value is, and how far the color in question lies outside the tolerance range.
  * Try experimenting with different `tol`, `fade`, `minkey`, `maxkey` and `color` values. Watch how the five attributes interact for different keying effects, and how the `minkey` and `maxkey` values complement one another.


Accurate chromakeying can be a challenging process. Correct values for the `tol` and `fade` attributes are essential to make sure that the correct regions in the first image are keyed to the second image. In general, very detailed key images will show slight speckling in spots where the colors rapidly move between keyed and non-keyed regions. In addition, a single key color (e.g. blue) almost never suffices for a complete key, so a range of values must always be used. You will often find, however, that the color you want keyed out of part of the image is somewhat present in the region you want to retain! Balancing all of these factors to get the most convincing effect is the hardest part of using the [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") object.
## Summary
The [jit.chromakey](https://docs.cycling74.com/reference/jit.chromakey "jit.chromakey") object lets you do two-source chromakeying in Jitter. You can set a color range for the key using the `color` and `tol` attributes, and use the `fade`, `minkey`, and `maxkey` values to define how the two matrices work in a composite. The [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") user interface object allows you to easily select colors as they appear on the screen by setting the object over a [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"). Clicking the [suckah](https://docs.cycling74.com/reference/suckah/ "suckah") object will give you the color of the pixel just clicked on the screen.
## See Also
  * [Video and Graphics Tutorial 10: Composing the Screen](https://docs.cycling74.com/learn/articles/jitterchapter00l_composing-the-screen/)
  * [jit.chromakey - Keying based on chromatic distance](https://docs.cycling74.com/reference/jit.chromakey)
  * [jit.pwindow - In-Patcher Window](https://docs.cycling74.com/reference/jit.pwindow)
  * [jit.movie - Play or edit a movie](https://docs.cycling74.com/reference/jit.movie)
  * [loadbang - Send a bang automatically when patcher is loaded](https://docs.cycling74.com/reference/loadbang/)
  * [metro - send bangs at regular intervals](https://docs.cycling74.com/reference/metro/)
  * [prepend - Place one message at the beginning of another](https://docs.cycling74.com/reference/prepend/)
  * [suckah - Get pixel color at display coordinates](https://docs.cycling74.com/reference/suckah/)
  * [vexpr - Evaluate a mathematical expression on lists](https://docs.cycling74.com/reference/vexpr/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
