---
description: List of Gen operators exclusive to Jitter Gen
group: Gen
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/gen/gen_jitter_operators/
title: Jitter Operators
---

# Jitter Operators
The following Gen operators are unique to the [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") objects - unlike the Common Gen Operators , they are only used in the matrix/texture domain.
## Color
  * [hsl2rgb](https://docs.cycling74.com/reference/gen_jit_hsl2rgb/) : Convert HSL to RGB, preserving alpha
  * [rgb2hsl](https://docs.cycling74.com/reference/gen_jit_rgb2hsl/) : Convert RGB to HSL, preserving alpha


## Coordinate
  * [cell](https://docs.cycling74.com/reference/gen_jit_cell/) : Cell coordinates of input matrix [0, dim-1]
  * [dim](https://docs.cycling74.com/reference/gen_jit_dim/) : Dimensions of input matrix
  * [norm](https://docs.cycling74.com/reference/gen_jit_norm/) : Normalized coordinates of input matrix [0, 1]
  * [snorm](https://docs.cycling74.com/reference/gen_jit_snorm/) : Signed normalized coordinates of input matrix [-1, 1]


## Quaternion
  * [qconj](https://docs.cycling74.com/reference/gen_jit_qconj/) : Get the conjugate of a quaternion.
  * [qmul](https://docs.cycling74.com/reference/gen_jit_qmul/) : Multiply quaternion inputs
  * [qrot](https://docs.cycling74.com/reference/gen_jit_qrot/) : Rotate a vector by a quaternion. The equation of the rotation is q∗v∗q−1q*v*q^{-1}q∗v∗q−1.


## Sampling
  * [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/) : Nearest neighbor sample a matrix at a given coordinate (normalized). Nearest has a boundmode attribute that can be set to wrap, mirror or clamp.
  * [nearestpix](https://docs.cycling74.com/reference/gen_jit_nearestpix/) : Nearest neighbor sample a matrix at a given coordinate (in pixels). Nearest has a boundmode attribute that can be set to wrap, mirror or clamp.
  * [sample](https://docs.cycling74.com/reference/gen_jit_sample/) : Sample a matrix at a given coordinate (normalized) with linear interpolation. Sample has a boundmode attribute that can be set to wrap, mirror or clamp.
  * [samplepix](https://docs.cycling74.com/reference/gen_jit_samplepix/) : Sample a matrix at a given coordinate (in pixels) with linear interpolation. Pixel centers are located at PIXEL+0.5. For example, the center of the upper-left pixel is (0.5, 0.5). Samplepix has a boundmode attribute that can be set to wrap, mirror or clamp.


## Surface
  * [circle](https://docs.cycling74.com/reference/gen_jit_circle/) : Equation of a circle taking input coordinates ranging from [0, 1]
  * [cone](https://docs.cycling74.com/reference/gen_jit_cone/) : Equation of a cone taking input coordinates ranging from [0, 1]
  * [cylinder](https://docs.cycling74.com/reference/gen_jit_cylinder/) : Equation of a cylinder taking input coordinates ranging from [0, 1]
  * [plane](https://docs.cycling74.com/reference/gen_jit_plane/) : Equation of a plane taking input coordinates ranging from [0, 1]
  * [sphere](https://docs.cycling74.com/reference/gen_jit_sphere/) : Equation of a sphere taking input coordinates ranging from [0, 1]
  * [torus](https://docs.cycling74.com/reference/gen_jit_torus/) : Equation of a torus taking input coordinates ranging from [0, 1]


## Vector
  * [concat](https://docs.cycling74.com/reference/gen_jit_concat/) : Concatenate vector values into a larger vector
  * [cross](https://docs.cycling74.com/reference/gen_jit_cross/) : Take the cross product of two vectors
  * [dot](https://docs.cycling74.com/reference/gen_jit_dot/) : Take the dot product of two vectors
  * [faceforward](https://docs.cycling74.com/reference/gen_jit_faceforward/) : Return a vector pointing in the same direction as another
  * [length](https://docs.cycling74.com/reference/gen_jit_length/) : Returns the length of a vector
  * [normalize](https://docs.cycling74.com/reference/gen_jit_normalize/) : Normalize a vector to unit length
  * [reflect](https://docs.cycling74.com/reference/gen_jit_reflect/) : Reflect a vector off a surface defined by a normal
  * [refract](https://docs.cycling74.com/reference/gen_jit_refract/) : Refract a vector through a surface defined by a normal and a refraction index
  * [rotor](https://docs.cycling74.com/reference/gen_jit_rotor/) : Return a quaternion that can rotate the first input into the second.
  * [swiz](https://docs.cycling74.com/reference/gen_jit_swiz/) : Unpack and remap vector components
  * [vec](https://docs.cycling74.com/reference/gen_jit_vec/) : Pack scalar values into a vector


