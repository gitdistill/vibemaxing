---
description: Utilities for Jitter 3D manipulations
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/jitter3dutilsinterface/
title: class Jitter3dUtilsInterface
---

# class Jitter3dUtilsInterface
Utilities for Jitter 3D manipulations
It is not necessary to instantiate this interface directly; it is available globally as a `Jitter3DUtils` object and methods can be called like `Jitter3DUtils.vadd()`.
## Methods
### add_quats
Add three 4D vectors (quaternions)
```
add_quats(q1: Jitter3dUtilsTypes.vec4, q2: Jitter3dUtilsTypes.vec4, q3: Jitter3dUtilsTypes.vec4): void;

```
Name | Type | Description  
---|---|---  
q1 | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | first quaternion  
q2 | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | second quaternion  
q3 | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | third quaternion  
### axis_to_quat
Convert an angle/axis rotation to a quaternion
```
axis_to_quat(axis: Jitter3dUtilsTypes.vec3, quat: Jitter3dUtilsTypes.vec4): void;

```
Name | Type | Description  
---|---|---  
axis | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | axis rotation  
quat | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | output quaternion  
### build_rotmatrix
Build a rotation matrix for a given quaternion
```
build_rotmatrix(m: Jitter3dUtilsTypes.vec4, q: Jitter3dUtilsTypes.vec4): void;

```
Name | Type | Description  
---|---|---  
m | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | rotation matrix  
q | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | quaternion  
### closest_line_sphere
Set `p1` to the point on a sphere closest to a line segment
```
(x3 - x1)(x2 - x1) + (y3 - y1)(y2 - y1) + (z3 - z1)(z2 - z1)
-----------------------------------------------------------
(x2 - x1)(x2 - x1) + (y2 - y1)(y2 - y1) + (z2 - z1)(z2 - z1)

```
```
closest_line_sphere(lineA: Jitter3dUtilsTypes.vec3, lineB: Jitter3dUtilsTypes.vec3, center: Jitter3dUtilsTypes.vec3, r: number, p1: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
lineA | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first line point  
lineB | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second line point  
center | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | center point  
r | number | sphere radius  
p1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | point to set  
### intersect_line_quad
Returns whether the ray defined by the line's two points intersect the quad defined by a position, rotation, and scale. Sets `p2` to the point of intersection with the quad plane in unit coordinates and sets `p1` to the same point in world coordinates.
```
intersect_line_quad(lineA: Jitter3dUtilsTypes.vec3, lineB: Jitter3dUtilsTypes.vec3, pos: Jitter3dUtilsTypes.vec3, rot: Jitter3dUtilsTypes.vec3, scale: Jitter3dUtilsTypes.vec3, p1: Jitter3dUtilsTypes.vec3, p2: Jitter3dUtilsTypes.vec3): boolean;

```
Name | Type | Description  
---|---|---  
lineA | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first line point  
lineB | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second line point  
pos | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | quad position  
rot | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | quad rotation  
scale | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | quad scale  
p1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | world coordinate intersection point  
p2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | unit coordinate intersection point  
Return Value | boolean |   
### intersect_line_sphere
Returns whether the ray defined by the line's two points intersect with the sphere of given center and radius. Sets `p1` to the closest point of intersection.
```
intersect_line_sphere(lineA: Jitter3dUtilsTypes.vec3, lineB: Jitter3dUtilsTypes.vec3, center: Jitter3dUtilsTypes.vec3, r: number, p1: Jitter3dUtilsTypes.vec3): boolean;

```
Name | Type | Description  
---|---|---  
lineA | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first line point  
lineB | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second line point  
center | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | sphere center  
r | number | sphere radius  
p1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | closest point of intersection  
Return Value | boolean |   
### normalize_quat
Normalize a quaternion
```
normalize_quat(quat: Jitter3dUtilsTypes.vec4): void;

```
Name | Type | Description  
---|---|---  
quat | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | a quaternion to normalize  
### quat_to_axis
Convert a quaternion to an angle/axis rotation
```
quat_to_axis(quat: Jitter3dUtilsTypes.vec4, axis: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
quat | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | quaternion to convert  
axis | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | output angle/axis rotation  
### transform_point
```
transform_point(point: Jitter3dUtilsTypes.vec4, matrix: Jitter3dUtilsTypes.mat16): void;

```
Name | Type | Description  
---|---|---  
point | [Jitter3dUtilsTypes.vec4](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec4 "Jitter3dUtilsTypes.vec4") | a point to transform  
matrix | [Jitter3dUtilsTypes.mat16](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-mat16 "Jitter3dUtilsTypes.mat16") | a 4x4 matrix  
### vadd
Add two 3D vectors
```
vadd(src1: Jitter3dUtilsTypes.vec3, src2: Jitter3dUtilsTypes.vec3, dst: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
src1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first vector  
src2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second vector  
dst | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | output vector to store sum of `src1 + src2`  
### vcopy
Copy one vector to another
```
vcopy(v1: Jitter3dUtilsTypes.vec3, v2: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
v1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | source  
v2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | destination  
### vcross
Calculate the cross product of two 3D vectors
```
vcross(v1: Jitter3dUtilsTypes.vec3, v2: Jitter3dUtilsTypes.vec3, cross: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
v1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first vector  
v2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second vector  
cross | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | cross product  
### vdiv
Divide `src1` and `src2` (element-wise) and store the result in `dst`
```
vdiv(src1: Jitter3dUtilsTypes.vec3, src2: Jitter3dUtilsTypes.vec3, dst: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
src1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first vector  
src2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second vector  
dst | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | destination vector  
### vdot
Calculate the dot product of two 3D vectors
```
vdot(v1: Jitter3dUtilsTypes.vec3, v2: Jitter3dUtilsTypes.vec3): number;

```
Name | Type | Description  
---|---|---  
v1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first vector  
v2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second vector  
Return Value | number |   
### vlength
Compute the squared distance of a 3D vector
```
vlength(v: Jitter3dUtilsTypes.vec3): number;

```
Name | Type | Description  
---|---|---  
v | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | vector  
Return Value | number |   
### vlength2
A cheaper distance-squared calculation
```
vlength2(v: Jitter3dUtilsTypes.vec3): number;

```
Name | Type | Description  
---|---|---  
v | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | vector  
Return Value | number |   
### vmul
Multiply `src1` and `src2` (element-wise) and store the result in `dst`
```
vmul(src1: Jitter3dUtilsTypes.vec3, src2: Jitter3dUtilsTypes.vec3, dst: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
src1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first vector  
src2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second vector  
dst | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | destination vector  
### vnormal
Normalize a 3D vector
```
vnormal(v: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
v | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | vector  
### vscale
Scale a vector
```
vscale(v: Jitter3dUtilsTypes.vec3, scale: number): void;

```
Name | Type | Description  
---|---|---  
v | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | vector  
scale | number | scale factor  
### vset
Set the values of a vector
```
vset(v: Jitter3dUtilsTypes.vec3, x: number, y: number, z: number): void;

```
Name | Type | Description  
---|---|---  
v | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | vector  
x | number | new x value  
y | number | new y value  
z | number | new z value  
### vsub
Subtract `src2` from `src1` and store the result in `dst`
```
vsub(src1: Jitter3dUtilsTypes.vec3, src2: Jitter3dUtilsTypes.vec3, dst: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
src1 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | first vector  
src2 | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | second vector  
dst | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | destination vector  
### vzero
Set all elements of a vector to zero
```
vzero(v: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
v | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | vector  
### xyz_to_axis
Convert rotation in Euler angles (xyz) to angle/axis rotation
```
xyz_to_axis(v: Jitter3dUtilsTypes.vec3, axis: Jitter3dUtilsTypes.vec3): void;

```
Name | Type | Description  
---|---|---  
v | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | rotation in Euler angles  
axis | [Jitter3dUtilsTypes.vec3](https://docs.cycling74.com/apiref/js/jitter3dutilstypes/#type-vec3 "Jitter3dUtilsTypes.vec3") | output angle/axis rotation
