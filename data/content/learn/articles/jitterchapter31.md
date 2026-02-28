---
description: Rendering Destinations
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter31/
title: Jitter Tutorial 31
---

Download Series Content and Patchers
# Tutorial 31: Rendering Destinations
In the previous tutorial, we saw how to draw OpenGL graphics into a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") using the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object. Now we will look at the other kinds of destinations into which a [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object can draw, what to use them for, and how to switch between destinations. 
Open the tutorial and double-click the `Render_Destinations` subpatch to open it.
In the upper left of the patch is a [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object with an argument of `inky`, along with other objects.
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") in the upper left of the patch labeled _Start Rendering_.


You should see a red ball appear in the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object. The [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object is drawing the ball. Its first argument, `inky`, specifies the drawing context currently being drawn by the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object to the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"). The other arguments set the `color` and `scale` attributes of the ball. 
![Draw a red ball in the window named  inky](https://docs.cycling74.com/images/761f0d5fd28ff04572a26584899ff2fd_481.webp) Draw a red ball in the window named inky
## Drawing and Swapping Buffers 
Clicking the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") starts the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") object, which sends `bang` messages to the object [t](https://docs.cycling74.com/reference/trigger/)`b b erase`. This object first sends an `erase` message followed by a `bang` message to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object, and then a `bang` message that is used elsewhere in the patch. 
When the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object receives the `bang` message, it draws all of the GL group objects which share its destination, then copies its offscreen buffer, if any, to the screen. An _offscreen buffer_ is an area of memory not visible on the screen, the same size as the drawing destination. By default, all drawing contexts have an offscreen buffer. Drawing is done into the buffer, which must then be copied to the screen in order to be seen. 
The offscreen buffer makes flicker-free drawing and animation possible, as we see here. Even though the buffer is being erased before the red ball is drawn each time, we never see the buffer in its erased state. To see what drawing looks like without the offscreen buffer, click on the [message](https://docs.cycling74.com/reference/message/ "message") box `doublebuffer 0` in the upper right of the patch . You will probably see the image start to flicker. This happens because the `erase` message now causes the window itself to be erased, not the offscreen buffer. The window remains blank for a short but indeterminate period of time before the red ball is drawn, so you can see the area under the ball flickering between red and the dark gray of the erased window. Click the [message](https://docs.cycling74.com/reference/message/ "message") box `doublebuffer 1` to remake the offscreen buffer and stop the flickering. 
## Setting Fullscreen Mode
The [p](https://docs.cycling74.com/reference/patcher/)`fullscreen` subpatch contains a [key](https://docs.cycling74.com/reference/key/ "key") object, a [select](https://docs.cycling74.com/reference/select/ "select") object, a [toggle](https://docs.cycling74.com/reference/toggle/ "toggle"), a [message](https://docs.cycling74.com/reference/message/ "message") box and an [outlet](https://docs.cycling74.com/reference/outlet/ "outlet") object that sends the results of the subpatch to the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object. This is standard Max stuff, so we won’t go over it in too much detail— the result is that the escape key toggles between sending the messages `fullscreen 0` and `fullscreen 1` to the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object. (See the "Full Screen Display" section of [Tutorial 14](https://docs.cycling74.com/learn/articles/jitterchapter14/).)
  * Press the 'esc' key to change the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object to fullscreen mode and back. 


The escape key seems to be a common way to toggle fullscreen mode, so we’ve used this setup in many of the example patches. It’s important to note, however, that this is just a convention—there’s nothing built into Jitter that forces you to use one key or another for this purpose. 
You can use the `fsmenubar` attribute in conjunction with the `fullscreen` message to hide the menubar in addition to covering the screen. If the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object has the `fsmenubar` attribute set to 0, the menubar will be hidden
## Setting a jit.pwindow Destination
The [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object can draw to two different kinds of destinations. This patch contains an object example of the two: a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") and a [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"). Right now we are rendering to the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object. To change the destination to the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object, we need to first `name` the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object and then set the destinations of the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object and the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object.
  * Click on the [message](https://docs.cycling74.com/reference/message/ "message") box name blinky above the lefthand [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") objects.


This names the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object, which allows it to be used as a rendering destination. To switch the drawing to this destination, we need to send messages to both the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object and the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object, telling them about the new destination.
  * Click on the [message](https://docs.cycling74.com/reference/message/ "message") box `blinky` in the _Switch Destinations_ section of the patch. 


The symbol `drawto` is prepended to the message `blinky`, and the result is sent to the [s](https://docs.cycling74.com/reference/send/)`dest` object. Two objects receive this message — [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") and [t](https://docs.cycling74.com/reference/trigger/)`l b erase`. The [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object sends a sequence of messages to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object, which tell it to:
  1. Erase its current destination’s draw buffer
  2. Swap that buffer to the screen, visibly clearing the old destination, and
  3. Switch future drawing to the new destination.


The result is that the red ball is displayed on the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object at the right of the patch.
![Viewing our rendered output in a  jit.pwindow  object](https://docs.cycling74.com/images/900a0a8140c7932aeca999d9711b6b46_187.webp) Viewing our rendered output in a jit.pwindow object
## Rendering to a Jitter Matrix
  * Open the `Matrix_Rendering` subpatch.


You may want to create a rasterized image of your OpenGL scene so that any of Jitter's video-processing effects can be applied to the image. You can do this by using the `@output_matrix` attribute of the [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") object. Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") labeled _Start Rendering_.
You should see a cyan ball on a light gray background. This is because the red ball image generated by OpenGL is processed through the [jit.op](https://docs.cycling74.com/reference/jit.op "jit.op") object, which subtracts each color component from 255, inverting the image.
![Utilizing the matrix output of  jit.world](https://docs.cycling74.com/images/61865c42b313f5b6c35d5a9e6b4b9874_614.webp) Utilizing the matrix output of jit.world
Hardware vs. Software Rendering: One of the great advantages about using OpenGL for rendering graphics is that most of the work can be done by the graphics accelerator hardware in your computer, freeing the CPU up for other work such as generating audio. When drawing into jit.window objects or jit.pwindow objects, the hardware renderer can be used. Unfortunately, due to limitations of the current system software the hardware renderer cannot draw directly into jit.matrix objects. Note that drawing into Jitter matrices is significantly slower than drawing to jit.window or jit.pwindow objects, especially for complex scenes or those involving textures.
## Multiple Renderers and Drawing Order
  * Open the `More_Render_Destinations` subpatch.


Note that the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") objects have their z scaling set to 0. This essentially makes them 2D objects.
To move an OpenGL scene to a different destination, the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object as well as any GL group objects involved in drawing the scene must receive the `drawto` message. Why not just send a message to the renderer, telling it to move the entire scene? The reason is that each GL group object can have an independent destination, as well as each renderer. Objects in the GL group can be moved between multiple renderers. To see an example of why this might be useful, please look at the right-hand portion of the patch for this tutorial.
_At the right are three_[jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") objects named `A`, `B` and `C`. The [message](https://docs.cycling74.com/reference/message/ "message") box objects above them are not strictly necessary, because once a [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object has been named, its name is stored with it in the patch. But they are useful here as labels and as a reminder of what messages to send to name the objects.
There are also three [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") objects in the patch. Each of them is pointed at a different destination.
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle")`labeled` _Start Rendering_`.`


This repeatedly sends the `erase` message followed by a `bang` message to each of the three renderers. You should see a yellow circle within a blue circle in the topmost drawing destination. This simple OpenGL scene is created by the two [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") objects in the bottom left of the patch. We can move each of these objects to any of the three drawing destinations present.
![Rendering to  jit.pwindow  A](https://docs.cycling74.com/images/bb41fe6b3615a4af7a242be45402464e_182.webp) Rendering to jit.pwindow A
  * Click the topmost [message](https://docs.cycling74.com/reference/message/ "message") box `reading``B``in the`_Switch Destinations_ section of the tutorial patch. This changes the destination of the blue circle to the draw context named "B"—it now appears on the center [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow").
  * Click the lower [message](https://docs.cycling74.com/reference/message/ "message") box `reading``B``in the`_Switch Destinations_ section of the tutorial patch. This changes the destination of the yellow circle to the draw context named "B". The two objects are reunited.


Each time a [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object receives a `bang` message, it draws all of the GL group objects that have been added to its context. It draws the objects in the order in which they were added to the context. In this case, the yellow circle was added to the draw context named "B" after the blue circle, so it appears on top. To change this order, we can send the message `drawto B` to the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object drawing the blue circle again. This will remove it from its present place in the list of objects for the context named `B`, and add it again at the end of the list.
  * Click the upper [message](https://docs.cycling74.com/reference/message/ "message") box `reading``B``in the`_Switch Destinations_ section of the tutorial patch again. The blue circle should now obscure the yellow circle.

![The blue circle obscures the yellow one](https://docs.cycling74.com/images/d9d8299567e087e44913e5e4f7800025_178.webp) The blue circle obscures the yellow one
## Summary
We have introduced a flexible system for creating multiple OpenGL _renderers and drawing destinations_ , and for moving objects in the GL group between them using `drawto` messages. 
Two Jitter objects can function as drawing destinations: [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") and [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"). Each kind of destination has different uses. A [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object can be moved to different monitors and quickly enlarged to cover the screen. A [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object keeps its location in the patch. Futhermore, we can use the matrix output of the [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") object to create a rasterized image of the 3D scene, to which further video processing may be applied. 
## See Also
  * [Video and Graphics Tutorial 4: Adding 3D Objects](https://docs.cycling74.com/learn/articles/jitterchapter00f_adding-3d-objects/)
  * [jit.gl.gridshape - Generate simple geometric shapes as a connected grid](https://docs.cycling74.com/reference/jit.gl.gridshape)
  * [jit.gl.render - Render Open GL](https://docs.cycling74.com/reference/jit.gl.render)
  * [jit.matrix - The Jitter Matrix!](https://docs.cycling74.com/reference/jit.matrix)
  * [jit.pwindow - In-Patcher Window](https://docs.cycling74.com/reference/jit.pwindow)
  * [jit.window - Display data in a Window](https://docs.cycling74.com/reference/jit.window)
  * [qmetro - Queue-based metronome](https://docs.cycling74.com/reference/qmetro/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
