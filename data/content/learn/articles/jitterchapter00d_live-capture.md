---
description: Grab live video
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter00d_live-capture/
title: Live Capture
---

Download Series Content and Patchers
# Video and Graphics Tutorial 2: Live Capture
## Intro
Now that we have video playback working, we’ll turn to using live video input as source material for image processing. To do that, we’ll use your computer’s built-in camera.
## Setup
As in the previous lesson, we’ll be using [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") to display the output of our Jitter patch, so add [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") and [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") objects to your patch. Next, create a [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab") object and connect the left outlet to the inlet of your [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") object. To start up the camera, add a [message](https://docs.cycling74.com/reference/message/ "message") box containing the message `open`, connect it to your [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab"), then lock the patch and click on the [message](https://docs.cycling74.com/reference/message/ "message") box. Finally, turn on the toggle connected to jit.world to see the camera image in the window.
![](https://docs.cycling74.com/images/032b8ab800d7dfdbbf0e692fe8fa3bab_139.webp)
## Image Control
Now that the live image is being captured, let’s introduce some image processing into the signal flow. Create a new [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object , an all-in-one brightness, contrast and saturation effect.
![](https://docs.cycling74.com/images/fdf3e7501d1f3dc6a61859b9d31a558b_158.webp)
Connect this between the outlet of the [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab") and the inlet of the [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") objects. To adjust the image, we need to send messages to change the brightness, contrast and saturation. For now, we’ll do this using a special object called [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") (attribute user-interface) that exposes the attributes of any object it is connected to.
To attach an [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") control, click the left-hand side of the [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object box to display the object menu.
![](https://docs.cycling74.com/images/82de096d01dbc4b61bc0510d8feb378d_88.webp)
From there, navigate to the Attributes section and select **Brightness**. This will automatically create an attrui connected to [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") with the desired attribute.
![](https://docs.cycling74.com/images/d1576f93329aa0ed7886d5c4c9e4d81e_253.webp)
Notice that a floating point number appears on the right side of the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui"). 
![](https://docs.cycling74.com/images/88e65b84997321a84b7c7513e52ce39f_219.webp)
Follow the same steps to add [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") controls for the Contrast and Saturation attributes, lock the patch, then play around with these values to see how they affect the image.
![](https://docs.cycling74.com/images/8d6038fa467c1906ca25666a878363f3_292.webp)
## Explore Further
Now that you have successfully added an effect, you can use the same technique (insert an object, connect [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") objects to the object, change parameters) to explore a variety of other video processing possibilities within Jitter. Try out [jit.fluoride](https://docs.cycling74.com/reference/jit.fluoride "jit.fluoride") for selective neon tinting, [jit.hue](https://docs.cycling74.com/reference/jit.hue "jit.hue") for some dramatic color shifting, [jit.slide](https://docs.cycling74.com/reference/jit.slide "jit.slide") for quick and fun frame blending and [jit.wake](https://docs.cycling74.com/reference/jit.wake "jit.wake") for classic video feedback.
Some objects (such as [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") and [jit.slide](https://docs.cycling74.com/reference/jit.slide "jit.slide")) will have only a few attributes while others ([jit.wake](https://docs.cycling74.com/reference/jit.wake "jit.wake") and [jit.plur](https://docs.cycling74.com/reference/jit.plur "jit.plur")) will have a lot more. You’ll find you can get to know a lot about Jitter objects by just connecting them and using [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") to try out their attributes. 

Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
