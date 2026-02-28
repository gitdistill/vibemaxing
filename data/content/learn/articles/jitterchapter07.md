---
description: Image Level Adjustment
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter07/
title: Jitter Tutorial 7
---

Download Series Content and Patchers
# Tutorial 7: Image Level Adjustment
This tutorial shows how to adjust levels of brightness, contrast, and saturation in Jitter matrices that contain image data. We will also look at the concept of hue and hue rotation.
The tutorial patch has two new objects in it: [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa"), which allows you to control brightness, contrast, and saturation of an image stored in a Jitter matrix, and [jit.hue](https://docs.cycling74.com/reference/jit.hue "jit.hue"), which lets you rotate the hue of an image:
## Brightness, Contrast, and Saturation
![Open and view the image.](https://docs.cycling74.com/images/a6fb773258d1434a85f7793738a6046c_206.webp) Open and view the image.
  * Open the file _colorwheel.pct_ by clicking the [message](https://docs.cycling74.com/reference/message/ "message") box that says `read colorwheel.pct`. View the movie by clicking the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box to start the [metro](https://docs.cycling74.com/reference/metro/ "metro").


You should see a color wheel appear in the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") at the bottom of the patch:
![The Color Wheel of Fortune](https://docs.cycling74.com/images/ef4b058aaf78319105e3fa1cf897297f_177.webp) The Color Wheel of Fortune
The [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object shows us the image after it has passed through our two new objects. We'll talk about [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") first, and then get to [jit.hue](https://docs.cycling74.com/reference/jit.hue "jit.hue"). The [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object takes a 4-plane _char_ Jitter matrix and, treating it as ARGB image data, allows you to alter the brightness, contrast, and saturation of the processed matrix. The three attributes are called, not surprisingly, `brightness`, `contrast`, and `saturation`. The default values of `1.0` for the three attributes result in the matrix passing out of the object unchanged:
![Using the  jit.brcosa  object](https://docs.cycling74.com/images/38b3ff38948f60a4eadce9494ba27086_365.webp) Using the jit.brcosa object
  * Change the attributes of the [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object and observe how the output matrix changes.


The brightness of an image refers to its overall lightness or darkness when compared to a reference color (usually black). Changing the `brightness` attribute is equivalent to multiplying the values in the matrix by that value. A `brightness` value of `0` will turn the image to black; values above `1.0` will gradually increase all non-0 cell values until they clip at white (255). A value of `0.5` will significantly darken the image, reducing its natural range of 0-255 to 0-127. Some brightness values are shown below on the color wheel:
![The color wheel with  brightness  values of  0.5 ,  1.5 , and  10 , respectively](https://docs.cycling74.com/images/aaaee8cf949098b7a5ff27a45b737588_521.webp) The color wheel with brightness values of 0.5 , 1.5 , and 10 , respectively
Note that cell values clip at 0 and 255 when altered in this way. This is why the rightmost image, with a `brightness` of `10`, is mostly white, with color showing only in areas where one or more of the visible color planes (RGB, or planes 1, 2, and 3) are 0 in the original matrix.
Image contrast can be expressed as the amount the colors in an image deviate from the average luminosity of the entire original image (see below). As the `contrast` attribute of [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") is increased above `1.0`, cell values above the average luminosity of the entire matrix are lightened (increased), and values below the average are darkened (decreased). The result is a dynamic expansion of the matrix image so that light values get lighter and dark values get darker. Settings for `contrast` below `1.0` reverse the process, with darker tones getting lighter and lighter tones getting darker until, at a `contrast` value of `0.0`, you only retain the average grey luminosity of the entire image. Negative values invert the color of the image with the same amount of overall contrast.
_Technical Detail:_ The average luminosity of a matrix can be computed by averaging the values of all the cells in the matrix, keeping the planes separate (so you get individual averages for Alpha, Red, Green, and Blue). The three visible planes are then multiplied by the formula: L = .299*Red + .587*Green + .114*BlueThe value L will give you the average luminance of the entire matrix, and is used by [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") to determine the threshold value to expand from when adjusting contrast.
_Technical Detail:_ The average luminosity of a matrix can be computed by averaging the values of all the cells in the matrix, keeping the planes separate (so you get individual averages for Alpha, Red, Green, and Blue). The three visible planes are then multiplied by the formula: L = .299*Red + .587*Green + .114*BlueThe value L will give you the average luminance of the entire matrix, and is used by [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") to determine the threshold value to expand from when adjusting contrast.
_Technical Detail:_ The average luminosity of a matrix can be computed by averaging the values of all the cells in the matrix, keeping the planes separate (so you get individual averages for Alpha, Red, Green, and Blue). The three visible planes are then multiplied by the formula: L = .299*Red + .587*Green + .114*BlueThe value L will give you the average luminance of the entire matrix, and is used by [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") to determine the threshold value to expand from when adjusting contrast.
Here are some example `contrast` settings:
![The color wheel with  contrast  settings of  0.3 ,  2 ,  -1 , and  100](https://docs.cycling74.com/images/bc252e10b47bc6708527902c7abcb3e9_706.webp) The color wheel with contrast settings of 0.3 , 2 , -1 , and 100
The first example shows the color wheel with its `contrast` drastically reduced (the cell values are all close to the average luminosity of the matrix). The second example shows an increased `contrast`. Note how the lighter shades in the middle of the color wheel begin to approach white. The third example shows a negative `contrast` setting. The colors are inverted from the original, but the average luminosity of the matrix is the same as in the original. The last example shows the result of a massive `contrast` boost. Cell values in this example are polarized to 0 or 255.
Image saturation reflects the ratio of the dominant color in a cell to the less dominant colors in that cell. As `saturation` values decrease below `1.0`, all color values in a cell will become more similar and thus _de-saturate_ towards grayscale. Values above `1.0` will push the colors farther away from one another, exaggerating the dominant color of the cell. As with contrast, a negative value for the `saturation` attribute will invert the colors but retain the same luminosity relationship to the original.
![The color wheel with saturation values of 0.2, 2 and -1](https://docs.cycling74.com/images/9f10e00bf4e3d1461c691b5d2f32fc61_527.webp) The color wheel with saturation values of 0.2, 2 and -1
The first image is de-saturated, so each cell value in the matrix is being drawn toward the value of the luminosity of that cell. The second image is over-saturated, so the individual colors are much brighter (or darker) than their originals. The third image maintains the original luminosity of the color wheel but inverts the colors.
## Hue and Cry
The [jit.hue](https://docs.cycling74.com/reference/jit.hue "jit.hue") object allows you to _rotate_ the hue of the input matrix. Setting the `hue_angle` attribute rotates the hue of the input matrix a specified amount in degrees:
![The  hue_angle  attribute rotates the hue of the input matrix.](https://docs.cycling74.com/images/4482be551c3c3dbd530746d4802854b7_146.webp) The hue_angle attribute rotates the hue of the input matrix.
The hue of a matrix cell can be thought of as its basic color (e.g. magenta). Image hue is visualized on a color wheel (like the one we've been using) which goes from red to green to blue to red again. The hue value, specified in degrees from 0-360, along with the saturation and lightness of the image, can be used to describe a unique color, much in the same way that a specific series of RGB values describe a unique color. By rotating the hue of an image forward, we shift the red part of the color spectrum so that it appears green, the green part of the spectrum to blue, and the blue part to red. The saturation and lightness do not change. A negative hue rotation shifts red into blue, etc. Hue rotations in increments of 120 degrees will transpose an image exactly one (or more) color planes off from the original hue of the image.
_**Technical Detail:**_ Our eyes perceive color through specialized receptors in our retina called _cones_ (another type of receptor exists that responds to low levels of light but doesn't distinguish color—these receptors are called _rods_). Cones in our eyes are differentiated by the wavelength of light they respond to, and fall into three categories: L-sensitive receptors which respond to long wavelength light (red), M-sensitive receptors which respond to medium wavelength light (green), and S-sensitive receptors which respond to short wavelength light (blue). Just as our auditory system is weighted to be more perceptive to frequencies that are within the range of human speech, the distribution of cones in our eyes is weighted towards the middle wavelengths which are most crucial to perceiving our environment. As a result, we have roughly twice as many green receptors in our eyes as the other two colors. This explains why the luminance formula (above) allocates almost 60% of perceived luminosity to the amount of green in an image. Camera technology has been developed to emulate the physiology of our eyes, so cameras (and film) are also more sensitive to green light than other colors.
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box to automate the `hue_angle` of the color wheel. Note that when the `hue_angle` reaches `360` degrees, the original matrix image is restored.

![Our color wheel at various hue rotations \(0-360 degrees\)](https://docs.cycling74.com/images/8d6168fb794cd3c7e1ddb06a89c7bb78_638.webp) Our color wheel at various hue rotations (0-360 degrees)
## Summary
The [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") and [jit.hue](https://docs.cycling74.com/reference/jit.hue "jit.hue") objects allow you to modify the brightness, contrast, saturation, and hue of an input matrix. You use the two objects to perform tasks such as dynamic level adjustment (e.g. autoexposure), color correction, or idiosyncratic hue displacement.
## See Also
  * [Video and Graphics Tutorial 9: Building live video effects](https://docs.cycling74.com/learn/articles/jitterchapter00k_building-live-video-effects/)
  * [jit.brcosa - Adjust image brightness/contrast/saturation](https://docs.cycling74.com/reference/jit.brcosa)
  * [jit.hue - Rotate hue](https://docs.cycling74.com/reference/jit.hue)
  * [jit.pwindow - In-Patcher Window](https://docs.cycling74.com/reference/jit.pwindow)
  * [jit.movie - Play or edit a movie](https://docs.cycling74.com/reference/jit.movie)
  * [metro - send bangs at regular intervals](https://docs.cycling74.com/reference/metro/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
