---
description: Examples of how to create fractal geometries using jit.geom + JavaScript
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-fractals/
title: Fractals
---

Download Series Content and Patchers
# Fractal Geometry
I thought it might be fun to make a patch that can process a Jitter geometry in self-similar fashon.
## Self-similarity?
Open the patch _fractals.maxpat_.
![](https://docs.cycling74.com/images/a9d30e612ad85077e2f0e69e3c6d30ff_1024.webp)
Self-similarity means lots of things, but this is what I'm thinking about:
  * I'd like to implement a process that can take any triangulated geometry, and add new vertices to it following certain criteria.
  * I want this process to be repeatable, and the pattern that iIm expecting to see should be similar to itself at smaller and smaller scales.
  * I'd like this process, although potentially endless, to proceed in stepped fashon, like launching a new iteration at the press of a button.


## Feedback Connections
Since I'd like our emergent pattern to repeat itself, we need the possibility to provide as input to the next iteration the result of the previous one. It smells like feedback to me!
But how can we connect jit.geom objects in such a way? We know that matrices containing vertices data can be transofmed into Jitter geometries using [jit.geom.togeom](https://docs.cycling74.com/reference/jit.geom.togeom "jit.geom.togeom"), and that Jitter geometries can be transformed back into matrices with [jit.geom.tomatrix](https://docs.cycling74.com/reference/jit.geom.tomatrix "jit.geom.tomatrix") or via script. So, that's it! We just need to convert our Jitter geometry to matrix and back, and use traditional Jitter objects to create the feedback loop.
![](https://docs.cycling74.com/images/d5020b0bcb21cc13c1d90585f9300217_311.webp)
## The Process
My idea is quite simple:
  * for each triangle of the mesh, compute its area, normal vector, and centroid.
  * for each triangle, add a new vertex in correspondance of the centroid, but shifted along the normal vector by a user-defined amount scaled by the triangle's area.
  * for each edge of the triangle, compute the middle point.
  * connect the 3 original vertices and the new 4 ones like this:

![](https://docs.cycling74.com/images/0065a1a001a87cd42df663422f4297fa_1024.webp)
then, take this geometry as the input for the next generation, and keep subdividing it.
![](https://docs.cycling74.com/images/513eeb75f2d514d3ab5affc6650b69b2_1024.webp)
That's not the only way to create fractal geometries, of course, but you can start experimenting from here! 

Kind
    Example 

Author
    Cycling '74 

Contributors
    Matteo Marson
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
