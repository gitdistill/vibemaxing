---
description: Camera View
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter32/
title: Jitter Tutorial 32
---

Download Series Content and Patchers
# Tutorial 32: Camera View
_Note:_ Some techniques described in this tutorial are outdated. Users are recommended to use the [jit.gl.camera](https://docs.cycling74.com/reference/jit.gl.camera "jit.gl.camera") object instead of the jit.gl.render _camera_ and _lookat_ messages described below.
This tutorial shows you how to set up the camera view and how to position and rotate GL objects using [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle"). It will cover the group of components which together make up the _camera view_ : the camera's position, the point at which the camera is looking, the "up" vector, the type of projection, the lens angle, and the clipping planes.
In the lower left of the patch, there is a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object named `mister`. This window will be the destination for our OpenGL drawing. You will notice that the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object has an attribute argument `@depthbuffer 1` to specify the creation of a depth buffer. A depth buffer allows the OpenGL renderer to determine which drawing command is visible at a given pixel based on the proximity of the geometry to the camera. Without depth buffering, OpenGL uses what is often referred to as the "Painter's Algorithm"--i.e. the visible results of drawing commands correspond to sequence in which they are performed. 
## The GL Context
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object labeled _Start Rendering_.


We now see large gray circle and some yellow lines. These are being drawn by two instances of the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object. The [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object can draw a variety of 3D shapes, including spheres, tori, cylinders, cubes, planes, and circles. The grey circle we see drawn in the window is actually a sphere and is being drawn by the section of the patch labeled _Grey Shape_. The yellow lines are actually a plane and are being drawn by the section of the patch labeled _Yellow Plane_. The yellow plane is being rendered with `poly_mode 1 1,` which means that the shape is being drawn with outlined polygons rather than filled polygons for both the front and back faces of the plane. If you switch off the toggle object connected to the [message](https://docs.cycling74.com/reference/message/ "message") box `poly_mode $1 $1`, you can see the plane rendered with filled polygons. 
![The  mister  drawing context](https://docs.cycling74.com/images/30a6d5b1f685fc2beebbedabd76ae44c_455.webp) The mister drawing context
  * In the _Grey Shape_ section of the patch, click on the [message](https://docs.cycling74.com/reference/message/ "message") box `scale 0.3 0.3 0.3` and then click on the message box containing `shape torus`. You should now see what looks like a grey doughnut.
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object connected to the [message](https://docs.cycling74.com/reference/message/ "message") box `lighting_enable $1` and then click on the toggle object connected to the [message](https://docs.cycling74.com/reference/message/ "message") box `smooth_shading $1`. We are now staring at a lit, smoothly shaded, 3D gray torus.


By default, Jitter's GL objects have lighting and smooth shading disabled, so it is necessary to turn these on. Lighting will be covered in detail in [Tutorial 35](https://docs.cycling74.com/learn/articles/jitterchapter35/).
![Rendered shapes with smooth shading and lighting enabled](https://docs.cycling74.com/images/93bf3b7ae8adb945ca1ac3be6833f2cf_320.webp) Rendered shapes with smooth shading and lighting enabled
## Camera Position
  * Open the _Camera View_ subpatch of the patch, and click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object labeled _jit.gl.render axes_.


You should see a red line from the center of the window to the right of the window, a green line from the center of the window to the top of the window. These are the _x_ and _y_ axes, respectively. They help us to determine the origin of our scene. Since the default camera position is at [0.,0.,2.], and the default `lookat` position is [0.,0.,0.], the camera is looking directly at the origin of our scene along the _z_ axis. Hence, we do not see the blue line which represents the _z_ axis along which the camera is looking.
![View the axes](https://docs.cycling74.com/images/0b79200ee59afefb108b1e1e68ad3f69_320.webp) View the axes
  * Under the _camera position_ label, set the _x_ value to be `1`. Now the camera is at the position [1.,0.,2.], it is still looking at the position [0.,0.,0.], and the blue line of the _z_ axis has become visible.

![The axes with a different viewing position](https://docs.cycling74.com/images/7f7b1d0007d085a0538c283314458743_320.webp) The axes with a different viewing position
  * Now let's set the `camera position`_x_ value to `6.,`_y_ value to - `6.,` and _z_ value to `6`. so that the camera position is [6,–6,6]. You can see that the yellow plane and the axes are, in fact, finite.

![Viewing the edge of the plane](https://docs.cycling74.com/images/a946f37cfe0e3b86ea4ce3123cd377d2_320.webp) Viewing the edge of the plane
So far, the _y_ axis has always been pointing upwards with respect to the camera view. This is because the default "up" vector is [0.,1.,0.]—i.e. the unit _y_ vector.
  * Under the _up vector_ label, let's set the _y_ value to 0. and the _z_ value to 1. We see that the view has rotated, and the blue line of the _z_ axis is now pointing upwards.

![Using a different “up” vector](https://docs.cycling74.com/images/111bb2092544cc38cd8b2b5940fd81fc_320.webp) Using a different “up” vector
You may have noticed, as we've moved the camera further away from the origin, that the torus, plane, and axes have become smaller. This is because the default viewing mode uses a perspective projection, which is similar to the way we see things in the 3-dimensional world we inhabit. If you are familiar with camera lenses, you may also know that depending upon the angle of the lens, objects will be smaller as the lens angle increases to accommodate a larger field of view. Similarly, we can change the lens angle of our perspective transformation to increase the field of view, and in doing so the objects will become yet smaller.
  * The default lens angle is 45 degrees, so let's change it to something like 60 degrees by changing the [number](https://docs.cycling74.com/reference/number/ "number") box connected to the [message](https://docs.cycling74.com/reference/message/ "message") box `lens_angle $1`.

![Using a 60-degree lens angle](https://docs.cycling74.com/images/10b286adfa53046be8f5bce8863ccdc3_320.webp) Using a 60-degree lens angle
## Orthographic Projection
Another type of projection supported by OpenGL is the _orthographic projection_. This type of projection does not diminish the size of objects based on camera position. The orthographic projection is common to 3D CAD software used for tasks such as mechanical engineering. Many early video games like Q-Bert also used an orthographic projection. You can switch between the perspective projection and the orthographic projection by clicking on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box labeled _orthographic projection_. The message `ortho 1` will turn on orthographic projection. If you try moving the camera with orthographic projection turned on, you should not see the objects become any smaller. However, changing the lens angle will still change the field of view, and the size of objects relative to the view.
![Viewing our scene using orthographic projection](https://docs.cycling74.com/images/6d4965aa43440d05243ebc864029529b_320.webp) Viewing our scene using orthographic projection
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") again to turn off the orthographic projection with an `ortho 0` message.


## Clipping Planes
Let's examine the _clipping planes_ that determine the extent along the camera's view that will be rendered. OpenGL has a _near_ clipping plane and a _far_ clipping plane, and only geometry which lies in between these two planes will be rendered. These clipping planes are specified in units of distance from the camera along the viewing vector using the `clip_near` and `clip_far` messages. By default, the near clipping plane is set to 0.1 and the far clipping plane is set to 100.
  * Try increasing the near clipping plane to `10` and decreasing the far clipping plane to `12.` You should see the near and far edges of the yellow plane that fall outside the clipping planes disappear.

![Using a more constrained clipping plane](https://docs.cycling74.com/images/f077620eced95392e2b32dac8b5a0869_320.webp) Using a more constrained clipping plane
  * Set the near clipping plane back to the default of `0.1` and the far clipping plane back to the default of `100`.


So far, the camera has always been looking at the origin [0.,0.,0.]. If we change the `lookat` position's x value to `3.`, the camera is now looking at [3.,0.,0.].
## Handles
  * Let's move the torus to the position [3.,0.,0.], by clicking on the [message](https://docs.cycling74.com/reference/message/ "message") box containing `position 3. 0. 0`. in the subpatch labeled _UI Rotation and Position Control_. The torus is now again located at the center point of the view, [3.,0.,0.].

![Changing the viewing position and the position of the shape](https://docs.cycling74.com/images/be02a7c535c0d466388ee55fe31926f1_320.webp) Changing the viewing position and the position of the shape
Not only did this send the `position 3. 0. 0.` message to the torus, but also to the jit.gl.handle object. The jit.gl.handle object is a GL group object that uses mouse information to move and rotate objects in the 3D scene. Like the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object, the [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object requires a named draw context into which to draw. Unlike the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object, it's also a user interface object that translates mouse activity in the draw context's destination to Max messages.
In this patch, messages from the [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object are sent to the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object. They are also sent to the [route](https://docs.cycling74.com/reference/route/ "route")`rotate position` object and formatted so you can see exactly what is being sent. These messages are the only communication from the [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object—there is nothing going on behind the scenes.
If you click on the torus and drag the mouse, you will see the torus being rotated by the [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object as though it were a virtual trackball. If you hold down the command key while dragging, you can move the torus left, right, up, and down. If you hold the option key as you drag, you can move the torus towards you or away from you. Using the shift key as you perform any of the above mouse actions will constrain the action to a single axis.
  * Try manipulating the orientation of the torus by clicking on it in the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object. Get a feel for how the [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object translates the 2-dimensional mouse information into 3-dimensional rotation information.

![Using the  jit.gl.handle  object to manipulate the object’s position](https://docs.cycling74.com/images/a1087580ea079a5728d8797c2f7454c3_320.webp) Using the jit.gl.handle object to manipulate the object’s position
As with the displayable axes of the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object, the [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object shows colored lines that correspond to the _x_ (red), _y_ (green), and _z_ (blue) planes of the object being rotated. The lines appear as circles around the relevant object being "handled." The mouse controls the axes whose circles are nearest to the front of your current field of view. By manipulating the image so that those circles move to the back of the object, you can control a different pair of axes with the next mouse click. The modifier keys let you reposition the object by relocating it on the three axes. The [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object outputs the relevant messages to set the `rotate` and `position` attributes of the GL group object attached to it. Note that if you are displaying a GL context in a [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"), the Help in Locked Patchers option of Max (which you can change under the Options menu) needs to be disabled in order for zooming to work using [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle"). Otherwise, the option key will cause the help patch for [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") to appear(!).
## Summary
We have examined the several components which make up an OpenGL scene's camera view, and the necessary attributes of the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object which control them. The `camera` attribute specifies the camera position; `up` specifies the upwards vector; `lookat` specifies the position at which the camera is looking; `ortho` specifies whether to use an orthographic or perspective projection; and `near_clip` and `far_clip` specify the clipping planes. Lighting and smooth shading attributes can be enabled by setting the `lighting_enable` and `smooth_shading` attributes of the GL group object handling the geometry (in this case the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object).
The [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object lets us rotate and reposition OpenGL objects using the mouse and the modifier keys on the keyboard. The [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object takes the name of a valid draw context to attach itself to, and sends messages to any connected object that is also using that context, setting the `rotation` and `position` attributes of that object.
## See Also
  * [Video and Graphics Tutorial 4: Adding 3D Objects](https://docs.cycling74.com/learn/articles/jitterchapter00f_adding-3d-objects/)
  * [jit.gl.gridshape - Generate simple geometric shapes as a connected grid](https://docs.cycling74.com/reference/jit.gl.gridshape)
  * [jit.gl.handle - Use mouse movement to control position/rotation](https://docs.cycling74.com/reference/jit.gl.handle)
  * [jit.gl.render - Render Open GL](https://docs.cycling74.com/reference/jit.gl.render)
  * [jit.window - Display data in a Window](https://docs.cycling74.com/reference/jit.window)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
