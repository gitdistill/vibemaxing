---
description: Managing compositing in Max, for object occlusion and transparency. Using both the depth buffer as well as explicit layering.
group: Jitter
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/jitter/depth_layer_blend/
title: Depth Testing and Layering
---

# Depth Testing and Layering
Composing refers to the various ways of drawing multiple objects in the same graphics context. One object might partially obscure another, or another object might be visible behind a transparent object. Compositing generally uses one of two techniques: **depth testing** and **layering**. To facilitate these techniques, all Jitter objects representing entities in a rendered scene share the attributes `@layer`, `@depth_enable`, `@blend_enable`, and `@blend`.
## Depth Testing
Depth testing models the way objects closer to the camera lens obscure objects further away. Every pixel that would be drawn writes its distance from the camera—its depth—into the **depth buffer**. When a new object is drawn, the renderer checks the depth (distance from the camera) of every pixel and compares that with the depth of whatever pixels may have been previously drawn in the same location. If the new pixel is closer it will be drawn, otherwise it will be discarded.
By default, every context has a depth buffer. Whether or not a context has a depth buffer can be set on [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") and [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") with the `@depthbuffer` attribute. Additionally, every `jit.gl.*` object that supports depth testing has a `@depth_enable` attribute. This is on by default, but can be used to control depth testing on a per-object basis.
![](https://docs.cycling74.com/images/5f14ec81ab9ee2e9aa571e49a17168fa_618.webp) When @depth_enable is disabled, the object will no longer write to the depth buffer, and the renderer will not use depth information when compositing the object into the scene.
## Layering
Layering gives you direct control over the order in which objects are drawn. Objects in a lower layer are rendered first, then objects in higher layers. By default, all 3D objects are added to layer 0, and therefore their drawing order is indeterminate. You can change the `@layer` attribute to move the object to a different layer, where higher values are drawn on top of lower values.
Be careful to disable depth testing with `@depth_enable 0` if you want to use layering, otherwise depth testing will override the layer value. Unlike other `jit.gl.*` objects the [jit.gl.layer](https://docs.cycling74.com/reference/jit.gl.layer "jit.gl.layer") object disables depth testing by default.
![](https://docs.cycling74.com/images/1cfabe72ee37d5a457cbd43063422602_636.webp) The red layer (3) is drawn on top of the green layer (2) which is drawn on top of the blue layer (1) 
## Blending
Enable blending to allow overlapping layers to blend together. Blending is disabled by default, but you can enable it for relevant objects by setting `@blend_enable 1`. You can change the way pixels from different layers mix together by changing the **blend mode** , controlled with the `@blend` attribute. By default, blend is set to **alpha blend** , which uses the alpha value of the higher layer to determine how much of the higher and lower pixels to blend together. An alpha value of 0 means the pixel in the top layer is completely transparent, while an alpha value of 1 means the top pixel is totally opaque. Images and movie files that contain alpha values (e.g. PNG, TIFF, Animation codec, and ProRes 4444) can be displayed with proper transparency by texturing an object (like [jit.gl.layer](https://docs.cycling74.com/reference/jit.gl.layer "jit.gl.layer") or [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape")) with alpha blend enabled. Unlike other `jit.gl.*` objects the [jit.gl.layer](https://docs.cycling74.com/reference/jit.gl.layer "jit.gl.layer") object enables blending by default.
![](https://docs.cycling74.com/images/12cec3c420f989fb48220ff40f1302be_674.webp)
An image with an alpha channel, rendered on top of a video, using alpha blending
## Combining the Techniques
### Drawing an overlay
Layering and blending can work together with depth testing to draw a transparent overlay on top of a 3D scene. If objects in the scene have `@depth_enable 1`, while elements in the transparent overlay have `@depth_enable 0`, `@blend_enable 1`, and `@layer 1`, then the overlay will always be drawn on top of elements in the 3D scene. Whether or not the overlay is transparent or opaque will be determined by the alpha values of pixels in the overlay.
### Drawing transparent objects.
Sometimes, you want to have a transparent object in your scene that still uses the depth buffer. However, even if you give this object a transparent texture, it will still block objects behind it because the it still writes to the depth buffer. The solution is to set `@depth_write 0` and `@layer 1` on the transparent object. With `@depth_write 0`, the object will not update the depth buffer with its current depth values. That way, the object will be obscured by opaque objects in the scene, but other objects will be visible through your transparent object.
![](https://docs.cycling74.com/images/266758b071099616e4d55051a201551f_721.webp) A transparent torus ensconcing a rubber duck. By disabling depth_write, other objects are still visible through the transparent object.
