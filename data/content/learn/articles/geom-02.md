---
description: Transforming half-edge geometries with Jitter geometry objects. Generating normals and texture coordinates.
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-02/
title: Manipulating Jitter Geometries
---

Download Series Content and Patchers
# Manipulating Jitter Geometries
In the last tutorial, we looked at how to create simple shapes using the `jit.geom` family of objects for **Half-edge Geometry Structures**. We briefly talked about how what makes these structures special is that they include information about **vertex adjacency** , which makes certain kinds of transformations and calculations much more efficient. Let's look at some of those transformations now.
## Converting a Model to a Geometry
Open the patch `geom-02.maxpat`.
![](https://docs.cycling74.com/images/e563bdf12bf7bdf27de27f0781c0df20_1024.webp)
At the top of the patch you'll see how to use a model file with Jitter geometry, by taking the output of [jit.gl.model](https://docs.cycling74.com/reference/jit.gl.model "jit.gl.model") and passing it into [jit.geom.togeom](https://docs.cycling74.com/reference/jit.geom.togeom "jit.geom.togeom").
![](https://docs.cycling74.com/images/52a0f0f980618fb7248d2e21692352f9_377.webp)
The [jit.geom.togeom](https://docs.cycling74.com/reference/jit.geom.togeom "jit.geom.togeom") object converts a Jitter matrix of triangles into a geometry. Like you see here, it can work with the output of [jit.gl.model](https://docs.cycling74.com/reference/jit.gl.model "jit.gl.model"), but it works just as well with shapes from [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape"), or with any kind of triangular mesh.
If you're not working with the output of [jit.gl.model](https://docs.cycling74.com/reference/jit.gl.model "jit.gl.model") or [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape"), then you'll need to make sure that the input to [jit.geom.togeom](https://docs.cycling74.com/reference/jit.geom.togeom "jit.geom.togeom") follows the [standard for 3D surfaces](https://docs.cycling74.com/userguide/jitter/graphics_processing/#usingmatrixoutputwithjit_gl_gridshape) as represented by a Jitter matrix.
You'll notice that we've disabled the `@automatic` attribute of [jit.gl.model](https://docs.cycling74.com/reference/jit.gl.model "jit.gl.model"). That's because we only want to send the model through once, rather than sending it automatically with every render frame. Once the matrix output of [jit.gl.model](https://docs.cycling74.com/reference/jit.gl.model "jit.gl.model") is converted to a geometry and stored in [jit.geom.togeom](https://docs.cycling74.com/reference/jit.geom.togeom "jit.geom.togeom"), we don't need to send it again. In fact, it woud be inefficient to do so, since we'd be converting the same geometry over and over again.
## Transforming a Geometry
Once we've converted the model to a half-edge geometry, we're ready to start transforming it. Under [jit.geom.togeom](https://docs.cycling74.com/reference/jit.geom.togeom "jit.geom.togeom"), we've stacked two effects: a [jit.geom.twist](https://docs.cycling74.com/reference/jit.geom.twist "jit.geom.twist") and a [jit.geom.waves](https://docs.cycling74.com/reference/jit.geom.waves "jit.geom.waves").
![](https://docs.cycling74.com/images/b371a2f57a27dd968bbaf2143ffbf0dd_602.webp)
We used the `@bypass` attribute to bypass these effects, but try disabling the `@bypass` attribute to enable the effect and see how it affects the geometry.
![](https://docs.cycling74.com/images/a6c6705e19e5b68cffdcde3e9db55fa2_1024.webp) From left to right, the original duck model, the duck with a twist applied, and the duck with waves applied.
If you want to include multiple effects, it's best to put them in a chain like this, and to turn them on and off using `@bypass`. You might, for example, think about using a `gate` object to route a single geometry through different effects.
![](https://docs.cycling74.com/images/369e68f83414cfefa2c6c272601a1826_355.webp) The wrong way to bypass a Jitter geometry effect
You could bypass a video effect this way, but it's not the right way to work with geometry effects. The problem is that `jit.geom` objects are smart. Unlike video effects, where every new frame passes through the whole render chain, `jit.geom` objects only trigger new computation when their internal state changes. When you change the state of the [gate](https://docs.cycling74.com/reference/gate/ "gate") object in this example, you're not changing the state of any `jit.geom` object. This won't trigger any new computation, and you won't actually see any change to the geometry.
Of course, you could bang the first object in the `jit.geom` chain to re-trigger computation manually.
## Texture Coordinates
After we manipulate the geometry, we generate new **texture coordinates** for the geometry with [jit.geom.texgen](https://docs.cycling74.com/reference/jit.geom.texgen "jit.geom.texgen"). This object uses the half-edge geometry to compute texture coordinates for each vertex. If you're not familiar with texture coordinates, they're basically a map from an image—the texture—to each point on the geometry.
![](https://docs.cycling74.com/images/5d6390e5eb68ecfff2f417c87de36f12_888.webp) The duck model, with the original texture applied. The texture, on the right, is a sort of palette that's used to apply color to the surface of the duck. The texture coordinates describe how to color the surface using the texture image.
If we try to apply our custom, checkerboard texture to the duck without updating the texture coordinates, it will use the same coordinates as the original model. You can see what this looks like by enabling the `@bypass` attribute on [jit.geom.texgen](https://docs.cycling74.com/reference/jit.geom.texgen "jit.geom.texgen").
![](https://docs.cycling74.com/images/fd5447ae75cea0e9cfd3c63065da192d_482.webp) Disabling @bypass will use the texture coordinates from the original model.
The [jit.geom.texgen](https://docs.cycling74.com/reference/jit.geom.texgen "jit.geom.texgen") objects has a few different algorithms that it can use to compute new texture coordinates, based on the shape of the geometry. Try disabling the `@bypass` attribute on [jit.geom.texgen](https://docs.cycling74.com/reference/jit.geom.texgen "jit.geom.texgen") and seeing what the different texture coordinate generation algorithms look like.
![](https://docs.cycling74.com/images/1a02d3be37ff75a3fb30f2d0414b0ffc_1024.webp) From left to right, mapping a checkerboard image to the duck model using planar, triplanar, and spherical coordinates.
## Animation and Reactivity
Finally, try enabling animation and audio reactivity for the twist and waves effects.
If you don't see any changes when you enable these animations, you'll need to make sure the `@bypass` attribute is disabled.
In the last tutorial, we mentioned that Jitter geometry objects worked asynchronously. In fact, Jitter geometry processing takes place on a dedicated geometry thread, separate from the other processing that goes on in Max. Sometimes this means that it's not possible to modulate certain attributes in real time. For example, if you try to change the number of subdivisions of a [jit.geom.shape](https://docs.cycling74.com/reference/jit.geom.shape "jit.geom.shape") object, you'll see that the object doesn't always update right away.
However, it's important to point out that most of the time the fact that Jitter geometry objects are asynchronous isn't something you need to think about. Like in this patch, much of the time you can treat them just like any other object, and modulate their attributes for real-time effects. 

Kind
    Tutorial 

Author
    Cycling '74 

Contributors
    Sam Tarakajian
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
