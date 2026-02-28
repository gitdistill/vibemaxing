---
description: Scissors and Glue
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter13/
title: Jitter Tutorial 13
---

Download Series Content and Patchers
# Tutorial 13: Scissors and Glue
In this tutorial we'll learn how to use two simple objects to slice and combine rectangular regions of two-dimensional Jitter matrices. The tutorial patch shows two Jitter objects that neatly complement each other: [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors"), which cuts a matrix into equally sized smaller matrices, and [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue"), which pastes multiple matrices into one matrix. We'll also take a brief look at a Max object called [router](https://docs.cycling74.com/reference/router/ "router"), which lets you easily route Max messages from multiple sources to multiple destinations.
![Read the movie](https://docs.cycling74.com/images/d86b7bcacf86c65c0bbe5ecbf4f3927a_210.webp) Read the movie
The top left of the patch is straightforward enough. The [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") object automatically sends the `read traffic.mov` message to the [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") object, which then loads our movie of traffic footage.
  * Start the [metro](https://docs.cycling74.com/reference/metro/ "metro") by clicking the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box at the top of the patch. You will see the traffic appear in the large [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") at the bottom of the patch. More interestingly, you will see the traffic image cut into quadrants, each of which appears in a separate [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object off to the right side.


## Cut it Up
The [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") object is responsible for splitting the Jitter matrix containing the traffic footage into four smaller matrices: 
![The  jit.scissors  object](https://docs.cycling74.com/images/b11d429a4a759e31514876cd62534233_462.webp) The jit.scissors object
The [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") object cuts a Jitter matrix of any size, type, or planecount into smaller Jitter matrices that are then sent out independent outlets of the object. The `rows` and `columns` attributes specify how many smaller matrices are created each time the object receives a new matrix in its inlet. In our tutorial patch, the [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") object is splitting the image into four smaller matrices (2 `columns` and 2 `rows`). These separate matrices come out individual outlets of the object in _column-major_ order (i.e. the object assigns outlets to the smaller matrices from left-to-right and then from top-to-bottom). 
Two very important things you should know about [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") :
1) The number of outlets that [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") has is determined at object creation. Therefore the `rows` and `columns` attributes will only create outlets when they are specified in the object box. For example, typing [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors")`@rows 10 @columns 2` will create an instance of [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") with 20 matrix outlets (plus the usual right outet for attribute queries), but simply making a [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") object with no arguments will only give you one matrix outlet. You can change the `rows` and `columns` attributes with Max messages to the object, but you won't be able to add outlets beyond what those initially created by the object.
2) The size (`dim`) of the matrices put out by [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") is equal to the size of the slices of the matrix, not the entire original matrix. For example, the four smaller matrices in our tutorial patch are each 160x120 cells, not 320x240.
## Routing the Matrices
The four smaller matrices output by [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") in our patch are each sent to two different places: to [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") objects so we can see what's going on, and to a Max object in the middle of the patch called [router](https://docs.cycling74.com/reference/router/ "router"). The colored patchcords illustrate where each smaller matrix is sent.
![The Max  router  object](https://docs.cycling74.com/images/c1a9ba4c157f709784b8b2ab52e15fde_119.webp) The Max router object
The [router](https://docs.cycling74.com/reference/router/ "router") object is a combination of the Max [gate](https://docs.cycling74.com/reference/gate/ "gate") and [switch](https://docs.cycling74.com/reference/switch/ "switch") objects. It takes two arguments (the number of routeable inlets and the number of routable outlets) and is controlled by messages sent to the leftmost inlet. Most of the messages that [router](https://docs.cycling74.com/reference/router/ "router") understands are identical to the MSP object [matrix~](https://docs.cycling74.com/reference/matrix~/ "matrix~"). As a result you can use [router](https://docs.cycling74.com/reference/router/ "router") with the [matrixctrl](https://docs.cycling74.com/reference/matrixctrl/ "matrixctrl") object with ease.
The four inlets to the right of the [router](https://docs.cycling74.com/reference/router/ "router") object take their input from the four matrix outlets of our [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") object. A [receive](https://docs.cycling74.com/reference/receive/ "receive") object assigned to the symbol `routeit` gets messages from the lower-right of the tutorial patch, which controls our [router](https://docs.cycling74.com/reference/router/ "router") object. The four leftmost outlets of the router object are connected to a [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") object, which we'll talk about in a moment.
![Controlling the  router](https://docs.cycling74.com/images/4af2e206022ccbe8381034f6a477b857_312.webp) Controlling the router
Sending the message `patch` followed by an inlet number and an outlet number to a [router](https://docs.cycling74.com/reference/router/ "router") object will make a virtual connection between that inlet and that outlet in the object. Any message arriving at that inlet will be instantly forwarded to the relevant outlet. If an inlet was previously connected to that outlet, a `patch` message will sever that connection in favor of the new one.
The [radiogroup](https://docs.cycling74.com/reference/radiogroup/ "radiogroup") objects in this patch control which outlets of the [router](https://docs.cycling74.com/reference/router/ "router") our four small Jitter matrices (arriving at the inlets) are sent to. The inlets and outlets number up from `0`, so the message `patch 2 1` makes a connection between the third routeable inlet and the second outlet of the [router](https://docs.cycling74.com/reference/router/ "router") object.
  * Click on some of the [radiogroup](https://docs.cycling74.com/reference/radiogroup/ "radiogroup") controls, and watch how the output image in the lower jit.pwindow changes. Notice how with the [router](https://docs.cycling74.com/reference/router/ "router") object you can make the matrices cut from the traffic image appear in any of the four quadrants of the composite image at the bottom.


## The Glue That Keeps It Together
The [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") object at the bottom of the patch does the effective opposite of [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors"). The `rows` and `columns` attributes specify inlets, not outlets, and a composite matrix is output which is made up of the incoming matrices laid out in a grid. 
![Sending the same matrix to all four inlets of  jit.glue](https://docs.cycling74.com/images/140b076d63e8d2b89b7be0eb5452b14f_579.webp) Sending the same matrix to all four inlets of jit.glue
Important Note: As with [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors"), [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") can only create new inlets and outlets when the object is created, so the `rows` and `columns` attributes present in the object box will determine how many inlets the object has. Also, the size (`dim`) of the output matrix generated by [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") will be equal to the size of all the smaller matrices put together (e.g. our four 160x120 matrices in this patch will yield one 320x240 matrix).
One final point worth making about [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") is that its default behavior is to only output a composite matrix when a new matrix arrives it its _leftmost_ inlet. If we were to disconnect the leftmost inlet of our [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") object, we would no longer get any new output matrices from the object. The `syncinlet` attribute lets you make [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") sent its output in response to a different inlet. A `syncinlet` value of `-1` will cause [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") to output new composite matrices when it gets new matrices at _any_ inlet. While this sounds like a good idea in theory, it can quickly bog down the frame rate of your Jitter processes with lots of redundant work.
## Summary
The [jit.scissors](https://docs.cycling74.com/reference/jit.scissors "jit.scissors") object cuts a matrix into smaller, equal-sized rectangular matrices. The [jit.glue](https://docs.cycling74.com/reference/jit.glue "jit.glue") object takes equal-sized rectangular matrices and pastes them back together into a composite matrix. The `rows` and `columns` attributes of both objects determine their number of outlets or inlets, respectively, when given at object creation, as well as the way in which the matrix is sliced up or composited. The [router](https://docs.cycling74.com/reference/router/ "router") object lets you arbitrarily connect Max messages from multiple inlets to multiple outlets in a similar fashion to the MSP [matrix~](https://docs.cycling74.com/reference/matrix~/ "matrix~") object.
## See Also
  * [jit.glue - Glue many matrices into one](https://docs.cycling74.com/reference/jit.glue)
  * [jit.pwindow - In-Patcher Window](https://docs.cycling74.com/reference/jit.pwindow)
  * [jit.movie - Play or edit a movie](https://docs.cycling74.com/reference/jit.movie)
  * [jit.scissors - Cut up a matrix into evenly spaced sub matrices](https://docs.cycling74.com/reference/jit.scissors)
  * [metro - send bangs at regular intervals](https://docs.cycling74.com/reference/metro/)
  * [radiogroup - Radio button/check box user interface object](https://docs.cycling74.com/reference/radiogroup/)
  * [router - Matrix-compatible Max message router](https://docs.cycling74.com/reference/router/)
  * [toggle - Switch between on and off (1 and 0)](https://docs.cycling74.com/reference/toggle/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
