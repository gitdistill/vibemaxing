---
description: Using jit.geom.topoints in conjunction with jit.gl.multiple to instance multiple shapes.
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-03/
title: Meshing and Multiplying
---

Download Series Content and Patchers
# Meshing and Multiplying with Jitter Geometries
Since the **Half-edge Geometry Structure** maintains information about which points are adjacent to which other points, certain operations are much faster and more efficient. In particular, the `jit.geom` family includes objects that can add, remove, and smooth the position of vertices, all while maintaining the overall shape.
## Remeshing, Subdividing, Decimating
Open the patch `geom-03.maxpat`.
![](https://docs.cycling74.com/images/1efad8c714281c289c8f01e65df2eea2_1024.webp)
When you first open the patch, you'll see the familiar duck model, in its original form. That's because at first, the four main operations that we're performing on the geometry—decimate, remesh, smooth, and texgen—are all disabled.
First, disable the `@bypass` attribute on the first [jit.geom.decimate](https://docs.cycling74.com/reference/jit.geom.decimate "jit.geom.decimate") object. Right away, you'll notice that the object drastically reduces the number of points in the model. However, you'll also see that it maintains the overall shape of the model as well.
![](https://docs.cycling74.com/images/b6ecc8865edf32af4aea8f20684451f9_833.webp) On the left, the original duck model, with vertices highlighted. On the right, the same duck model with several vertices removed. Points are not removed at random, and the jit.geom.decimate object tries to maintain the overall shape.
Now, try disabling the `@bypass` attribute on the [jit.geom.remesh](https://docs.cycling74.com/reference/jit.geom.remesh "jit.geom.remesh") object. You'll see that the vertices move to new coordinates that are more evenly spaced on the surface of the mesh. You can try disabling the [jit.gl.mesh](https://docs.cycling74.com/reference/jit.gl.mesh "jit.gl.mesh") in the bottom-center of the patch as well, which will show you just the vertex points and not the model. This may make it easier to the effect of [jit.geom.remesh](https://docs.cycling74.com/reference/jit.geom.remesh "jit.geom.remesh").
![](https://docs.cycling74.com/images/9859450709ffb939491303ce061824cf_833.webp) From top-left, going clockwise: the duck model after decimate, the duck after decimate and remesh, decimate and remesh but without the model, and just the vertices after decimate.
It's important to highlight that all of these vertex-adjustment algorithms are iterative. You can try experimenting with the `@iterations` attribute to see how this affects the output of each step. Try re-enabling the model and changing the number of iterations on the [jit.geom.remesh](https://docs.cycling74.com/reference/jit.geom.remesh "jit.geom.remesh") object.
![](https://docs.cycling74.com/images/83d728a20115da5afe5b4130fe313533_1024.webp) The remesh algorithm works by moving vertices from their current position to points that are more evenly distributed on the surface of the mesh. Adding more interations gradually converges on a final result, but is more computationally expensive.
## Texture Coordinates
As you experiment with the [jit.geom.decimate](https://docs.cycling74.com/reference/jit.geom.decimate "jit.geom.decimate"), [jit.geom.remesh](https://docs.cycling74.com/reference/jit.geom.remesh "jit.geom.remesh"), and [jit.geom.smooth](https://docs.cycling74.com/reference/jit.geom.smooth "jit.geom.smooth") objects, you'll notice that the color of the surface of the model starts to lose its smoothness.
![](https://docs.cycling74.com/images/89301f7040a609a2c3817c4f1cbbb1d4_833.webp) Moving the vertices of a model affects the texture coordinates as well.
These artifacts appear because the [jit.geom.remesh](https://docs.cycling74.com/reference/jit.geom.remesh "jit.geom.remesh") algorithm cannot generate texture coordinates. Once a geometry passes through this object, there's no guarantee that the texture coordinates will contain anything useful. You can try to use [jit.geom.texgen](https://docs.cycling74.com/reference/jit.geom.texgen "jit.geom.texgen") to generate new texture coordinates, although these won't necessarily correspond to the originals. However, the results can still be very interesting. Try disabling the `@bypass` attribute on [jit.geom.texgen](https://docs.cycling74.com/reference/jit.geom.texgen "jit.geom.texgen") and seeing how it affects the surface of the model.
![](https://docs.cycling74.com/images/6fd2a0198f0a4081ed7e8c02a9ccd28f_1024.webp) The texture coordinates that come from jit.geom.texgen might not always make sense, but they can still be fun.
## Points and jit.gl.multiple
Now, disable the `@enable` attribute on the [jit.gl.mesh](https://docs.cycling74.com/reference/jit.gl.mesh "jit.gl.mesh") that draws the points, as well as the `@enable` attribute on the [jit.gl.mesh](https://docs.cycling74.com/reference/jit.gl.mesh "jit.gl.mesh") that displays the original duck model. Enable the [jit.gl.multiple](https://docs.cycling74.com/reference/jit.gl.multiple "jit.gl.multiple") object in the bottom-right of the patcher. You should see a "cloud" of duck models, each drawn at one of the vertices of the original model.
![](https://docs.cycling74.com/images/57b2c73c9dbbee21fdb32242e1455fbc_833.webp) Using jit.geom.topoints with jit.gl.multiple, we can instance a shape using the vertices of a geometry.
It's important to point out that we're using [jit.geom.topoints](https://docs.cycling74.com/reference/jit.geom.topoints "jit.geom.topoints") rather than [jit.geom.tomatrix](https://docs.cycling74.com/reference/jit.geom.tomatrix "jit.geom.tomatrix") to get the vertices out of our geometry. This is because [jit.geom.tomatrix](https://docs.cycling74.com/reference/jit.geom.tomatrix "jit.geom.tomatrix") will actually create an 8-plane matrix, including the triangluar mesh, the surface normals, and the texture coordinates. To instance a bunch of ducks on the surface of our model, all we need is the points, so [jit.geom.topoints](https://docs.cycling74.com/reference/jit.geom.topoints "jit.geom.topoints") is a much more efficient choice here.
### Animation
Try enabling the animation on the points mesh in the bottom-right.
![](https://docs.cycling74.com/images/447bcedf18a71fec6d2f9af56eaf3cfd_351.webp)
You should see the ducks in the "duck cloud" start to animate. This brings together a couple of different techniques, namely the new Jitter geometry objects along with more "traditional" techniques for working with Jitter matrices.
![](https://docs.cycling74.com/images/7b0e0dc64a9fe79c3cd49415d0d01b48_1024.webp) Some of the results you can achieve by experimenting with different settings for the geometry objects, along with adding animation.
In general, once you've used `jit.geom` objects to generate a matrix, you can treat that matrix just like any other matrix in Jitter. Even though they have slightly different behaviors, Jitter matrix and geometry objects can each generate data that the other can use. 

Kind
    Tutorial 

Author
    Cycling '74 

Contributors
    Sam Tarakajian
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
