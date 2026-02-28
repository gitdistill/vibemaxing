---
description: Examples of how to generate a point cloud using jit.geom.
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-point-cloud/
title: Point Cloud
---

Download Series Content and Patchers
# Rainbow Point Cloud
This example shows how to create intricate point clouds using `jit.geom` that can then be used in a `jit.gl.mesh` based rendering setup.
## The Patch
Open the patch _geom-to-pointcloud.maxpat_.
![](https://docs.cycling74.com/images/ef64ff589ee3e4810bbef7a2917d0416_1024.webp)
The patcher to achieve this does the following steps.
  * Generates a base shape using `jit.geom.shape`.
  * Distributes a random number of points on it using `jit.geom.distribute`.
  * Places many small shapes one the base shape using the points from the previous step with `jit.geom.multiple`.
  * It then deforms the resulting geometry using a couple of chained `jit.geom.twist`.
  * Finally, it uses another `jit.geom.distribute` to generate the visible point cloud.
  * Lastly, `jit.geom.tomatrix` is used so that the point cloud can be turned into a `jit.gl.mesh`.

![](https://docs.cycling74.com/images/eead50e02e1fa94c158f8d9b544584a2_932.webp) The patch looks like this.
You will notice that there is one subpatcher called `[p GenerateRotationAndScale]`. It is a simple helper to generate random rotation and scale values for the small shapes we want to place using `jit.geom.multiple`.
![](https://docs.cycling74.com/images/4223243d83ed5f525b5f2bc5e0431fb7_453.webp) The subpatcher to generate the random rotation and scale values.
## Results
When playing around with the different settings that are exposed in the patch you can achieve a satisfying variety of point arrangements conveying different motion and texture.
![](https://docs.cycling74.com/images/60155166c9672243a4ac20444e17e758_1024.webp) Using a uv sphere as the base shape. ![](https://docs.cycling74.com/images/f54a5e4b8af1564ee22485ef27d55ab2_1024.webp) Using a torus as the base shape and a plane as the multiplied one.
To add animation you could use a custom vertex shader on the resulting `jit.gl.mesh` to modulate the point cloud. I will leave this as an excercise for the reader. 

Kind
    Example 

Author
    Cycling '74 

Contributors
    Matthias Dorfelt
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
