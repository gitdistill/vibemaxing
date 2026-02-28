---
description: Pattern object for drawing gradients and patterns.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/pattern/
title: class Pattern
---

# class Pattern
Pattern object for drawing gradients and patterns.
The [MGraphics](https://docs.cycling74.com/apiref/js/mgraphics/ "MGraphics") object can create Pattern objects with functions like [MGraphics.pattern_create_linear()](https://docs.cycling74.com/apiref/js/mgraphics/#pattern_create_linear "MGraphics.pattern_create_linear\(\)"), [MGraphics.pattern_create_radial()](https://docs.cycling74.com/apiref/js/mgraphics/#pattern_create_radial "MGraphics.pattern_create_radial\(\)"), and [MGraphics.pattern_create_rgba()](https://docs.cycling74.com/apiref/js/mgraphics/#pattern_create_rgba "MGraphics.pattern_create_rgba\(\)"). Generally, you use this Pattern object to add color stops and transformations to customize the pattern, then set that pattern as a source before filling a path.
#### Example
```
function paint() {
		// create a path
		mgraphics.rectangle(50, 0, 200, 100);

		// create a gradient pattern to fill the shape
		var tmp = mgraphics.pattern_create_radial(20.,20.,20.,100.,100.,30.);
		tmp.add_color_stop_rgba(0.,1.,0.,0.,1.);
		tmp.add_color_stop_rgba(1.,0.,1.,0.,1.);

		// set the gradient as a source
		mgraphics.set_source(tmp);

		// fill the shape
		mgraphics.fill();
}

```

## Methods
### add_color_stop_rgba
Add a color stop to a pattern.
Sets a color stop for the pattern. Linear and radial gradients will fade continuously between these color values.
```
add_color_stop_rgba(index: number, red: number, green: number, blue: number, alpha: number);

```
Name | Type | Description  
---|---|---  
index | number | The index of the color stop  
red | number | The red component of the color stop  
green | number | The green component of the color stop  
blue | number | The blue component of the color stop  
alpha | number | The alpha component of the color stop  
### get_extend
Get the extend value of the pattern
The extend value determines how the pattern will be drawn to fill extra space. "none" will draw nothing, "reflect" will invert the pattern and continue to draw it as if reflected, "repeat" will start the pattern over and continue to draw, and "pad" will take the last color of the pattern and extend it outward.
```
get_extend(): "none" | "reflect" | "repeat" | "pad";

```
Name | Type | Description  
---|---|---  
Return Value | "none" | "reflect" | "repeat" | "pad" |   
**This API is deprecated**
This functionality is not implemented and probably never will be
### get_type
Get the pattern type
Get the type of the pattern. Values are 0-solid, 1-surface, 2-linear, 3-gradient.
```
get_type(): 0 | 1 | 2 | 3;

```
Name | Type | Description  
---|---|---  
Return Value | 0 | 1 | 2 | 3 |   
### identity_matrix
Reset the transform matrix to identity (no transformation).
```
identity_matrix();

```

### rotate
Adds a rotation to the pattern
```
rotate(angle: number);

```
Name | Type | Description  
---|---|---  
angle | number | the rotation angle in radians (counter-clockwise)  
### scale
Scale the pattern horizontally and vertically
```
scale(scale_x: number, scale_y: number);

```
Name | Type | Description  
---|---|---  
scale_x | number | horizontal scaling  
scale_y | number | vertical scaling  
### set_extend
Set the extend value of the pattern
```
set_extend(extend_value: "none" | "reflect" | "repeat" | "pad");

```
Name | Type | Description  
---|---|---  
extend_value | "none" | "reflect" | "repeat" | "pad" | The extend value to set  
**This API is deprecated**
This functionality is not implemented and probably never will be
### set_matrix
Set the transform matrix for the pattern directly.
```
set_matrix(xx: number, xy: number, yx: number, yy: number, x0: number, y0: number);

```
Name | Type | Description  
---|---|---  
xx | number | x scaling support  
xy | number | rotational warping  
yx | number | rotational warping  
yy | number | y scaling support  
x0 | number | x translation  
y0 | number | y translation  
### translate
Translate the current pattern
```
translate(t_x: number, t_y: number);

```
Name | Type | Description  
---|---|---  
t_x | number | horizontal translation  
t_y | number | vertical translation
