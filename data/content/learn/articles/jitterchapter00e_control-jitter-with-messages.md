---
description: Controlling Jitter Objects
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter00e_control-jitter-with-messages/
title: Control Jitter with Messages
---

Download Series Content and Patchers
# Video and Graphics Tutorial 3: Control Jitter with Messages
## Intro
Messages are essential for controlling Jitter objects. We saw a little of that with [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") and [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab"). In this tutorial, we’ll look at how to take control of Jitter effects with simple messages.
## Setup
We'll start where we left off in the last tutorial - a patch containing [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab"), [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") and [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") objects.
![](https://docs.cycling74.com/images/bf9f46a77ad80ea829efbdf5716b45e2_287.webp)
## Adding Objects
Now let’s add a few additional effects. Create a [jit.fluoride](https://docs.cycling74.com/reference/jit.fluoride "jit.fluoride") and a [jit.slide](https://docs.cycling74.com/reference/jit.slide "jit.slide") object below the [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa"), and connect the new objects to the outlet of [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") and the inlet of [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world"). 
![](https://docs.cycling74.com/images/aea42d1b72215313816df9d9d2a4966a_214.webp)
Next, create some [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") objects for each effect. The [jit.slide](https://docs.cycling74.com/reference/jit.slide "jit.slide") only needs two (_slide_up_ and _slide_down_), while [jit.fluoride](https://docs.cycling74.com/reference/jit.fluoride "jit.fluoride") will require 4 object-specific attributes (_glow_ , _lum_ , _mode_ and _tol_). 
## Messages
While [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") objects are great for quick exploration, they have some limitations when it comes to sharing data with other objects and - more importantly - state saving using snapshots and the pattr system (which we'll want to do later on). For more robust control, we’ll look at how to construct _messages_ to control objects.
We'll start by creating standard messages that duplicate the way that [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") objects let us control the [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object. Most messages to Jitter objects consist of a list starting with the attribute name followed by the value(s) you want to set the attribute _to_. Create a new [message](https://docs.cycling74.com/reference/message/ "message") box that contains the message `brightness $1`. Next add a floating point number box ([flonum](https://docs.cycling74.com/reference/flonum/ "flonum")) and connect its outlet to the left inlet of the [message](https://docs.cycling74.com/reference/message/ "message") box. In turn, connect the outlet of the [message](https://docs.cycling74.com/reference/message/ "message") box to the inlet of [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa"). 
![](https://docs.cycling74.com/images/874b49feeb424d316a537073f0e2af1f_117.webp) The `$1` part of the message acts as a variable and tells the [message](https://docs.cycling74.com/reference/message/ "message") box to accept an incoming value in its place.
Repeat the process for the contrast and saturation attributes. 
Next we’ll add some control messages for [jit.fluoride](https://docs.cycling74.com/reference/jit.fluoride "jit.fluoride"). However, note that the _glow_ attribute has **three** values (red, green, and blue). For this attribute, we need to put together a list of those red, green and blue values using a [pak](https://docs.cycling74.com/reference/pak/ "pak") object. Make a new [pak](https://docs.cycling74.com/reference/pak/ "pak") object with three floating point arguments. These can be any value, but the values we give will also act as defaults - so a **pak 0. 0. 0.** would default to black. Add and connect three [flonum](https://docs.cycling74.com/reference/flonum/ "flonum") objects - one for each input of the [pak](https://docs.cycling74.com/reference/pak/ "pak") object - and connect your [pak](https://docs.cycling74.com/reference/pak/ "pak") object to a [message](https://docs.cycling74.com/reference/message/ "message") box containing the message `glow $1 $2 $3`. Connect the [message](https://docs.cycling74.com/reference/message/ "message") box outlet to the inlet of [jit.fluoride](https://docs.cycling74.com/reference/jit.fluoride "jit.fluoride"). 
![](https://docs.cycling74.com/images/489ca9f7cb800e6bf6e26ac2423a11c1_166.webp) If you don’t like making color decisions based on number values, you can use the [swatch](https://docs.cycling74.com/reference/swatch/ "swatch") object instead. Make a [swatch](https://docs.cycling74.com/reference/swatch/ "swatch") object and connect it to an [unpack](https://docs.cycling74.com/reference/unpack/ "unpack") object with the arguments **0. 0. 0.** Connect the three outlets of the [unpack](https://docs.cycling74.com/reference/unpack/ "unpack") object to the three [flonum](https://docs.cycling74.com/reference/flonum/ "flonum") objects. Now, you can easily select the color you want by moving the swatch cursor and also see the numerical values associated with the color you choose.  ![](https://docs.cycling74.com/images/0a64a1d5a250f6f68eaa585620af9886_244.webp)
Continue to convert the remaining [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") objects into messages, then adjust the values to see your messages in action.
## Explore Further
You may want to go back and review some of the basic Max message and list tutorials as you go to get more ideas of how to control Jitter objects. Try driving object parameters with random number generators, counters, and other data sources (you’ll probably need to do some number scaling to get things into the right range). 

Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
