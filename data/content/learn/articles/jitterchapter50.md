---
description: Procedural Texturing & Modeling
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter50/
title: Jitter Tutorial 50
---

Download Series Content and Patchers
# Tutorial 50: Procedural Texturing & Modeling
In this Tutorial we will be examining different operations that can be used to construct a procedural model of a texture or some form of geometric data.
Procedural techniques are a powerful way of defining some aspect of a computer-generated model through algorithms and/or mathematical functions. In contrast to using pre-existing data such as a static images or photographs, procedural models can generate visual complexity of arbitrary resolution and infinite variation. In conjunction with parametric controls, such models can be used to build a flexible interface for controlling complex behaviors and capturing a special effect.
Jitter provides a comprehensive set of basis functions and generators that are exposed through the [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") object. Each function performs a point-wise operation in _n_ -dimensional space whose evaluation is independent of neighboring results. This means that these operations can be performed on any number of dimensions, across any coordinate, without any need of referencing existing calculations. In addition, since they all share a common interface, these objects can be combined together and evaluated in a function graph by cross-referencing several [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") objects.
There are several categories of functions, each of which are characterized by a different intended use. These categories include _fractal_ , _noise_ , _filter_ , _transfer_ , and _distance_ operations. Functions contained in these folders can be passed by name to [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") either fully qualified (category.classname) or relaxed (classname).
Before looking at these categories in detail, we'll first explore the general interface of [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") and show how to create different types of procedural functions and fill a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") with our results.
## jit.bfg
Once the patch loads, take a look at the different objects being used. Notice that we have a [metro](https://docs.cycling74.com/reference/metro/ "metro") object attached to the [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") object. Once activated, a `bang` message will notify [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") to evaluate and output a Jitter matrix just like most other Jitter objects. In this example, [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") has been set up to generate a single plane matrix of type `float32` and size `128x128`.
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box connected to the [metro](https://docs.cycling74.com/reference/metro/ "metro") object to begin sending `bang` messages to [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg").


Notice that the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object remains solid black in color! Since [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") has not been told what basis function evaluate, [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") is not outputting a matrix and [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") remains unchanged. 
  * Select the `noise.cell` basis function from the list in the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object.

![An evaluated basis function.](https://docs.cycling74.com/images/dbde15d354ce84fbde82b89a11d4de09_287.webp) An evaluated basis function.
Now that [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") has been given a function to evaluate, we can see the results of its calculation in [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"). Internally, [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") is generating a series of Cartesian coordinates that it passes to the indicated `basis` function during its evaluation.
If we wanted to, we could adjust these coordinates and have [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") perform the evaluation over a different domain. 
  * Change the value of the [number](https://docs.cycling74.com/reference/number/ "number") box connected to the `scale`[message](https://docs.cycling74.com/reference/message/ "message") box.


Notice that the results of [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") change as we adjust the domain.
  * Select the `distance.euclidean` basis function from the list in the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object.
  * Again change the value of the [number](https://docs.cycling74.com/reference/number/ "number") box connected to the `scale`[message](https://docs.cycling74.com/reference/message/ "message") box.


Notice that positive values in the `scale`[number](https://docs.cycling74.com/reference/number/ "number") box have little effect on the results being shown in [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"), whereas negative values flip the image components from white to black. What is going on? Distance should always be positive and increase outward from the origin, right?
## jit.normalize
The output of [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") goes into a [jit.normalize](https://docs.cycling74.com/reference/jit.normalize "jit.normalize") object connected to the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"). This object will examine an incoming matrix and scale the minimum and maximum values into a normalized range of `0` - `1`.
When we changed the `scale` values being sent to [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") for evaluating the `distance.euclidean` function from positive to negative, the highest and lowest values that were being outputted from [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") switched as we crossed over the origin. Since [jit.normalize](https://docs.cycling74.com/reference/jit.normalize "jit.normalize") always scales the input matrix maximum to `1` and the minimum to `0`, our colors flipped. 
Since the output range of [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") may yield extremely large results, especially when evaluating unbounded functions such as fractals, we need to normalize our output in order to map the results for display.
## Basis Categories
Now that we are familiar with the basic interface for setting up [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") and specifying a basis function to evaluate, let's examine the contents of each function category.
## Distance Functions
The functions in the `distance` category each define a unique metric for determining the positional difference from a given point to the global origin.
Descriptions of each of these functions are provided in the following list.
  * `chebychev` : Absolute maximum difference between two points.

![](https://docs.cycling74.com/images/31f5549ab727212f153052ae26f05a01_483.webp)
  * `euclidean` : True straight line distance in Euclidean space.

![](https://docs.cycling74.com/images/147900c3d05111c9cccb0f813b62ac58_483.webp)
  * `euclidean.squared` : Squared Euclidean distance.

![](https://docs.cycling74.com/images/d89a88f5308aed8e537509a8d4c7a59e_483.webp)
  * `manhattan` : Rectilinear distance measured along axes at right angles.

![](https://docs.cycling74.com/images/7c051b7fee3a40d83118866aa58cb33d_487.webp)
  * `manhattan.radial` : Manhattan distance with radius fall-off control.

![](https://docs.cycling74.com/images/3f7afd4db5f70aea6c562ef81a9b6d78_487.webp)
  * `minkovsky` : Exponentially controlled distance.

![](https://docs.cycling74.com/images/7f59f4ed22cb894831cee5c93a0af794_487.webp)
The `noise.voronoi` object requires one of these `distance` objects to be specified as part of its evaluation.
## Filter Functions
The `filter` category contains signal processing filters which can be used to perform image sampling and reconstruction or to create pre-computed kernels for a general convolution.
Descriptions of each of these functions are provided in the following list.
  * `box` : Sums all samples in the filter area with equal weight.

![](https://docs.cycling74.com/images/b206c2a8657abfd7738882ca1d2ef64f_487.webp)
  * `gaussian` : Weights samples in the filter area using a bell curve.

![](https://docs.cycling74.com/images/229eef9ca06d8b31b08699302609f732_487.webp)
  * `lanczossinc` : Weights samples using a steep windowed sinc curve.

![](https://docs.cycling74.com/images/edd2c15d7d56423f2a0a2e48597e45b5_487.webp)
  * `mitchell` : Weights samples using a controllable cubic polynomial.

![](https://docs.cycling74.com/images/365163a1b62e5cb6379537dd7eddf1d2_487.webp)
  * `disk` : Sums all samples inside the filter's radius with equal weight.

![](https://docs.cycling74.com/images/0aad9f35d511e010d4091cae9c838491_487.webp)
  * `sinc` : Weights samples using an un-windowed sinc curve.

![](https://docs.cycling74.com/images/b0233637784f1501257e777f4a7d324f_487.webp)
  * `catmullrom` : Weights samples using a Catmull-Rom cubic polynomial.

![](https://docs.cycling74.com/images/8e9e6be45739e4075328164dad0d1fcb_487.webp)
  * `bessel` : Weights samples with a linear phase response.

![](https://docs.cycling74.com/images/3e548ce6f31925855f70da8ac78e8c9d_487.webp)
  * `triangle` : Weights samples in the filter area using a pyramid.

![](https://docs.cycling74.com/images/a1563267dc1dea5c2d9cf2e27f74fadc_487.webp)
These objects are used as parameters to both the `noise.value.convolution` and the `noise.sparse.convolution` objects, which expect to be given a `filter` object as part of their evaluation.
## Transfer Functions
Functions that map input to a different output are contained in the `transfer` category. Most of these functions operate only on a single dimension within the unit interval `0` - `1`.
A brief description of these functions is contained in the list below.
  * `step` : Always `1` if given value is less than threshold.

![](https://docs.cycling74.com/images/5c9883c97a477ac93ee86de1c03d2203_487.webp)
  * `smoothstep` : Step function with cubic smoothing at boundaries.

![](https://docs.cycling74.com/images/4ef1eff4473f38257929e827aded9a05_442.webp)
  * `bias` : Polynomial similar to gamma but remapped to unit interval.

![](https://docs.cycling74.com/images/b7f8f30f12f00f3fdb00f908df4ad4ae_448.webp)
  * `cubic` : Generic 3rd order polynomial with controllable coefficients.

![](https://docs.cycling74.com/images/6caa20e8dbb303b1a5e80b0bf2ba743f_479.webp)
  * `saw` : Periodic triangle pulse train.

![](https://docs.cycling74.com/images/b6542ae404311fe640bbd038a6de966a_479.webp)
  * `quintic` : Generic 5th order polynomial with controllable coefficients.

![](https://docs.cycling74.com/images/91885bb08912e74ed11ea2f0fdc12b55_479.webp)
  * `gain` : S-Shaped polynomial evaluated inside unit interval. Note: the default settings will result in a linear curve instead of the descriptive S-curve shape.

![](https://docs.cycling74.com/images/48d09fcad3dd4c51fc836f1b384b08e6_479.webp)
  * `pulse` : Periodic step function.

![](https://docs.cycling74.com/images/42f57e36d139e8233dc2d9b610bbe098_479.webp)
  * `smoothpulse` : Periodic step function with cubic smoothing at boundaries.

![](https://docs.cycling74.com/images/489aa9002b93dca29090c75689af18a2_479.webp)
  * `sine` : Periodic sinusoidal curve.

![](https://docs.cycling74.com/images/30b917b00173477ff3496384084f0523_479.webp)
  * `linear` : Linear function across unit interval.
  * `solarize` : Scales given value if threshold is exceeded.


These `transfer` functions can be used inside of several of the `noise` objects to change their smoothing function and/or alter their output.
## Noise Functions
Deterministic stochastic patterns (aka pseudo-random coherent noise functions) are the cornerstone of nearly every procedural model. They allow a controllable amount of complexity to be created by adding visual detail. 
A brief description of these functions is contained in the list below.
  * `cellnoise` : Coherent blocky noise.

![](https://docs.cycling74.com/images/e9415dbc2562f88342cd2e97841f2c92_479.webp)
  * `checker` : Periodic checker squares.

![](https://docs.cycling74.com/images/11e6b366ba9f46730f1571a1eb23ee5f_479.webp)
  * `value.cubicspline` : Polynomial smoothed pseudo-random values.

![](https://docs.cycling74.com/images/d80dca6904ca6ba5c0869eac60672f24_479.webp)
  * `value.convolution` : Convolution filtered pseudo-random values.

![](https://docs.cycling74.com/images/5b09eb1e5c4963aa70f95e419147cad5_479.webp)
  * `sparse.convolution` : Convolution filtered pseudo-random feature points.

![](https://docs.cycling74.com/images/15fb908a0f6d7e880ad0f4f60b4ca162_479.webp)
  * `gradient` : Directionally weighted polynomially interpolated values.

![](https://docs.cycling74.com/images/48bfdf1d610001e7f08587f4df3388fb_479.webp)
  * `simplex` : Simplex weighted pseudo-random values.

![](https://docs.cycling74.com/images/8bfbea3cda4b6d69901c83692fe6d057_479.webp)
  * `voronoi` : Distance weighted pseudo-random feature points.

![](https://docs.cycling74.com/images/6c6fa91fa064dc4ba1625fb4bf8455e0_479.webp)
  * `distorted` : Domain distorted combinational noise.

![](https://docs.cycling74.com/images/b8affc7bf73fb66eb6c4a587a14bf883_479.webp)
All of these functions are generators with the exception of the `noise.distorted` object, which is a binary operator and uses two existing functions for its evaluation.
## Fractal Functions
Fractals provide a specialized form of generation by combining multiple scales or octaves of another basis function. This process forms the characteristic self-similarity exhibited by all fractals.
A brief description of these functions is contained in the list below.
  * `mono` : Additive fractal with global simularity across scales.

![](https://docs.cycling74.com/images/74b86a4492cafd1257fad80771f75ada_479.webp)
  * `multi` : Multiplicative fractal with varying simularity across scales.

![](https://docs.cycling74.com/images/9afe4fd661ff5bd27cded6c7410fb159_479.webp)
  * `multi.hybrid` : A hybrid additive and multiplicative fractal.

![](https://docs.cycling74.com/images/7a0a7ccb91a9fe9a48974b0eee946268_479.webp)
  * `multi.hetero` : Heterogenous multiplicative fractal.

![](https://docs.cycling74.com/images/4907f2f55864b585eda45955800da7d2_487.webp)
  * `multi.ridged` : Multiplicative fractal with sharp ridges.

![](https://docs.cycling74.com/images/a962a9fc9bcae990ce421c973901e340_487.webp)
  * `turbulence` : Additive mono-fractal with sharp ridges.

![](https://docs.cycling74.com/images/14910589144a2f96dd1329d6c316b0fe_487.webp)
## Other Attributes & Messages
  * Select the `noise.checker` basis function from the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object.


Notice that in addition to the `scale` message that we used previously, we can also transform the evaluation coordinates through `rotation`, translation (via `offset`) and by adjusting their `origin`.
  * Change the 1st and 2nd[number](https://docs.cycling74.com/reference/number/ "number") boxes connected to `origin` to change the _x_ and _y_ origin.
  * Change the 1st and 2nd[number](https://docs.cycling74.com/reference/number/ "number") boxes connected to `offset` to change the _x_ and _y_ offset position.
  * Change the 1st[number](https://docs.cycling74.com/reference/number/ "number") box connected to `rotation` to change our rotation angle about the _x_ axis.


Notice the effect of the transform. Also notice the drop in performance when a `rotation` is performed – we will always get better frame rates if the `rotation` attribute is left at `0` for each matrix dimension.
_Technical Detail:_ In addition to the internal coordinate generation already described, [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") also accepts an input matrix of coordinates to evaluate (XYZ map to planes `0-2`, and the input matrix must be the same `dim` as the [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") output matrix).
  * Change the 1st[number](https://docs.cycling74.com/reference/number/ "number") box connected to `rotation` to `0` to disable rotation.
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box connected to `autocenter` to enable automatic centering.


If the `autocenter` attribute is set to `1`, the current matrix `dim` sizes will be used to place the origin in the center of the output matrix, overriding any values already set for the origin.
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box connected to `autocenter` again to disable automatic centering.
  * Select the `noise.gradient` basis function from the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object.
  * Click the `dim 128 128 1`[message](https://docs.cycling74.com/reference/message/ "message") box.


As mentioned previously, all of the basis functions that Jitter provides can be evaluated over any number of dimensions. This message has changed our output matrix to be a 3D matrix, and has correspondingly set the evaluation to be performed in 3-dimensional space. Since our display is still a 2D screen, we only need to evaluate a single slice in 3D, and thus our 3rd dim is set to 1.
  * Change the 3rd[number](https://docs.cycling74.com/reference/number/ "number") box connected to `offset` to change the _z_ evaluation position.


Notice how our results change. We are now traversing along the _z_ -axis as if we were moving forward/backwards through a volume aligned with the screen.
  * Select `float64` from the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") connected to the `precision` message.


The `precision` message can be used to change the [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") object’s internal evaluation precision. This may be desirable if we need more or less accurate results without changing the output matrix type.
  * Change the 3rd[number](https://docs.cycling74.com/reference/number/ "number") box connected to `offset` to change the _z_ evaluation position.


Notice how the higher precision affects the frame rate reported by the [jit.fpsgui](https://docs.cycling74.com/reference/jit.fpsgui "jit.fpsgui") object. We should be careful to only use `float64` precision when needed. 
  * Select `float32` from the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") connected to the `precision` message.
  * Change the `planecount` for [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") from `1` to `3` to enable RGB output.


In addition to _n_ -dimensional evaluation, [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") can generate up to 32 planes per dimension. Each plane is offset by a pseudo-random fractional amount controlled by the `align` attribute. 
  * Change the [number](https://docs.cycling74.com/reference/number/ "number") box connected to `align` for [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg").


Notice how the planes separate and become more visible as the `align` amount gets larger.
  * To see more specific examples for different combinations of _basis_ functions, open the help patch for the [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") object and look in the subpatchers for each category of function..


_Technical Detail:_ The output of [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") can actually be used as an input to another [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") to perform domain distortion, similar to the way `noise.distorted` operates. Check out the example patch in _jit-examples/other/jit.bfg.distorter.pat._
## Summary
The [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") object gives us access to a library of procedural basis functions and generators that we can use to define a procedural model for creating textures and modifying geometry. Internally [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") generates Cartesian coordinates along a grid. These coordinates can be transformed using the corresponding `origin`, `offset`, and `rotation` attributes, or overridden altogether via an input matrix containing evaluation coordinates.
## See Also
  * [jit.bfg - Evaluates a procedural basis function graph](https://docs.cycling74.com/reference/jit.bfg)
  * [jit.matrix - The Jitter Matrix!](https://docs.cycling74.com/reference/jit.matrix)
  * [jit.normalize - Normalize a matrix](https://docs.cycling74.com/reference/jit.normalize)
  * [jit.pwindow - In-Patcher Window](https://docs.cycling74.com/reference/jit.pwindow)
  * [umenu - Pop-up menu, to display and send commands](https://docs.cycling74.com/reference/umenu/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
