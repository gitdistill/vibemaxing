---
description: Shaders
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter41/
title: Jitter Tutorial 41
---

Download Series Content and Patchers
# Tutorial 41: Shaders
One of the primary purposes of graphics cards is to render 3D objects to a 2D frame buffer to display. How the object is rendered is determined by what is called the "shading model", which is typically fed information such as the object's color and position, lighting color and positions, texture coordinates, and material characteristics like how shiny or matte the object should appear. The program that executes in hardware or software to perform this calculation is called the _shader_. Traditionally graphics cards have used a fixed shading pipeline for applying a shading model to an object, but in recent years, graphics cards have acquired programmable pipelines so that custom shaders can be executed in place of the fixed pipeline. For a summary off many of the ways to control the fixed OpenGL pipeline, see _[Tutorial 35:](https://docs.cycling74.com/learn/articles/jitterchapter35/) Lighting and Fog_. 
**Hardware Requirement:** To fully experience this Tutorial, you will need a graphics card that supports programmable shaders, e.g. ATI Radeon 9200, NVIDIA GeForce 5000 series or later graphics cards. It is also recommended that you update your OpenGL driver with the latest available for your graphics card. On Macintosh, this is provided with the latest OS update. On PC, you can acquire the latest driver from either your graphics card manufacturer or your computer manufacturer.
## Flat Shading
One of the simplest shading models which takes lighting into account is called _Flat Shading_ or _Facet Shading_ , where each polygon has a single color across the entire polygon based on surface normal and lighting properties. As we saw demonstrated in _Tutorial 35_ , this can be accomplished in Jitter by setting the `lighting_enable` attribute of a Jitter OpenGL object (e.g. [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape")) to `1`.
## Getting Started
  * Open the Tutorial patch 41jShaders in the Jitter Tutorial folder. Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box labeled _Start Rendering_.
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box object above the [message](https://docs.cycling74.com/reference/message/ "message") box object reading `lighting_enable $1` to turn on lighting for the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object drawing the torus. The `smooth_shading` attribute is `0` by default.
  * Now you should see a change in the lighting of the torus. Instead of the dull gray appearance it started with, you will see a shiny gray appearance like this:

![A rendered torus showing Flat shading.](https://docs.cycling74.com/images/93ebedc7d347305dc26f2a810b14ce93_344.webp) A rendered torus showing Flat shading.
## Smooth Shading
While this might be a desirable look, the color of most objects in the real world changes smoothly across the surface. "Gouraud Shading" (1971) was one of the first shading models to efficiently address this problem by calculating a per vertex color based on surface normal and lighting properties. It then linearly interpolates color across the polygon for a smooth shading look. While the artifacts of this simple approach might look odd when using a small number of polygons to represent a surface, when using a large number of polygons, the visible artifacts of this approach are minimal. Due to the computational efficiency of this shading model, Gouraud Shading has been quite popular and remains the primary shading model used today by computer graphics cards in their standard fixed shading pipeline. In Jitter, this can be accomplished by setting the `smooth_shading` attribute to `1` (on). Let's do this in our patch, increasing and decreasing the polygon count by changing the `dim` attribute of the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object.
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box attached to the [message](https://docs.cycling74.com/reference/message/ "message") box reading `smooth_shading $1`. Try increasing and decreasing the polygon count by changing the [number](https://docs.cycling74.com/reference/number/ "number") box attached to the message box reading `dim $1 $1` in the lower right of the patch.

![A torus rendered with smooth shading.](https://docs.cycling74.com/images/471049033606578206c7f76105c5b4eb_344.webp) A torus rendered with smooth shading.
## Per-Pixel Lighting
As mentioned, smooth shading with a low number of polygons has visible artifacts that result from just performing the lighting calculation on a per vertex basis, interpolating the color across the polygon. Phong Shading (1975) smooths not only vertex color across a polygon, but also smooths the surface normals for each vertex across the polygon, calculating a per fragment (or pixel) color based on the smoothed normal and lighting parameters. The calculation of lighing values on a per pixel basis is called "Per Pixel lighting". This is computationally more expensive than Gouraud shading but yields better results with fewer polygons. Per pixel shading isn't in the OpenGL fixed pipeline; however we can load a custom _shader_ into the programmable pipeline to apply this shading model to our object. 
  * Load the per-pixel lighting shader by clicking the [message](https://docs.cycling74.com/reference/message/ "message") box that says `read mat.dirperpixel.jxs` connected to the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object.
  * Apply the shader to our object by clicking the [message](https://docs.cycling74.com/reference/message/ "message") box `shader shademe` connected to the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object. This sets object’s `shader` attribute to reference the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object by its `name` (`shademe`).

![Per-pixel shading applied to the torus.](https://docs.cycling74.com/images/440f10220fac64bb8eddb5c0308e0c0f_344.webp) Per-pixel shading applied to the torus.
## Programmable Shaders
In 1984, Robert Cook proposed the concept of a shade tree, where one could build arbitrary shading models out of some fundamental primitives using a "shading language". This shading language made it so that a rendering pipeline could be extended to support an infinite number of shaders rather than a handful of predefined ones. Cook's shading language was extended by Ken Perlin to contain control structures and became the model used by Pixar's popular _RenderMan_ shading language. More recently the GPU-focused _Cg_ and _GLSL_ shading languages were established based on similar principles. The custom shaders used in this tutorial, including the per-pixel lighting calculation, were written in GLSL. 
A brief introduction to how to write your own shaders will be covered in a subsequent Tutorial. For now, lets continue to use pre-existing shaders and show how we can dynamically change shader parameters. Gooch shading is a non-photorealistic shading model developed primarily for technical illustration. It outlines the object and uses warm and cool colors to give the sense of depth desired for technical illustrations. We have a custom shader that implements a simplified version of Gooch Shading which ignores the application of outlines. 
  * Load the simplified Gooch shader by clicking the [message](https://docs.cycling74.com/reference/message/ "message") box `read mat.gooch.jxs` connected to the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object.

![The simplified Gooch shading model applied to our torus.](https://docs.cycling74.com/images/960b1bedac94e25ec1d20c4ce7caffa8_344.webp) The simplified Gooch shading model applied to our torus.
You should notice that the warm tone is a yellow color and the cool tone is a blue color. These values have been defined as defaults in our shader file, but are exposed as parameters that can be overridden by messages to the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object. 
  * Using the [number](https://docs.cycling74.com/reference/number/ "number") boxes in the patch, send the messages `param warmcolor <red> <blue> <green> <alpha>` and `param coolcolor <red> <green> <blue> <alpha>` to the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object to change the tones used for the warm and cool colors.


We can determine parameters available to the shader by sending the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object the message `dump params` to print the parameters in the Max Console, or by sending the message `getparamlist`, which will output a parameter list out the object’s rightmost (dump) outlet. An individual parameter's current value can be queried with the message `getparamval <parameter-name>`. A parameter’s default value can be queried with the message `getparamdefault <parameter-name>`, and the parameter’s type can be queried with `getparamtype <parameter-name>`. 
## Vertex Programs
Shaders can be used not only to determine the surface color of objects, but also the position and attributes of our object's vertices, and as we'll see in our next Tutorials. For now, let's look at vertex processing. In the previous shaders we just discussed how the different shaders would render to pixels. In fact, for each of these examples we were running two programs: one to process the vertices (the vertex program) and one to render the pixels (the fragment program). The vertex program is necessary to transform the object in 3D space (rotation, translation, scaling), as well as calculate per-vertex lighting, color, and other attributes. Since we see the object move and rotate as we make use of the [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object in our patch, obviously some vertex program must be running. Logically, the vertex program runs on the programmable vertex processor and the fragment program runs on the programmable fragment processor. This model fits with the fixed function pipeline that also separates vertex and fragment processing tasks.
The custom vertex program in the previous examples, however, didn’t visibly perform any operation that is noticeably different than the fixed pipeline vertex program. So let’s load a vertex shader that has a more dramatic effect. The _vd.gravity.jxs_ shader can push and pull geometry based on the vertex distance from a point in 3D space. 
  * Load the simplified gravity vertex displacement shader by clicking the [message](https://docs.cycling74.com/reference/message/ "message") box `read vd.gravity.jxs` connected to the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object.
  * Control the position and amount of the gravity vertex displacement shader by changing the [number](https://docs.cycling74.com/reference/number/ "number") boxes connected to the [pak](https://docs.cycling74.com/reference/pak/ "pak") object and [message](https://docs.cycling74.com/reference/message/ "message") box outputting the messages `param gravpos <x> <y> <z>` and `param amount <n>`, respectively.

![Vertex Distortion.](https://docs.cycling74.com/images/650125feadfbaacaa2cf76590101b65e_344.webp) Vertex Distortion.
## Summary
In this tutorial we discussed the fixed and programmable pipelines available on the graphics card and demonstrated how we can use the programmable pipeline by loading custom shaders with the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object. Shaders can then be applied them 3D objects to obtain different effects. We can also set and query shader parameters through messages to the [jit.gl.shader](https://docs.cycling74.com/reference/jit.gl.shader "jit.gl.shader") object. 
## See Also
  * [jit.gl.gridshape - Generate simple geometric shapes as a connected grid](https://docs.cycling74.com/reference/jit.gl.gridshape)
  * [jit.gl.handle - Use mouse movement to control position/rotation](https://docs.cycling74.com/reference/jit.gl.handle)
  * [jit.gl.shader - Manages a GL shader](https://docs.cycling74.com/reference/jit.gl.shader)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
