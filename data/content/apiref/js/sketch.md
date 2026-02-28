---
description: Interface to an OpenGL-backed drawing context
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/sketch/
title: class Sketch
---

# class Sketch
Interface to an OpenGL-backed drawing context
Every custom UI made with jsui or JSPainter has access to a default Sketch object bound to the global variable "sketch". Use this object to render to the OpenGL-backed drawing context available to all UI objects. Often this is the only instance of the Sketch object that you will use. If you want to render sprites, have multiple layers of images, or create alpha channels, you can construct new instances of the Sketch object.
## Constructors
```
new Sketch(width?: number, height?: number);

```

Create a new Sketch instance
Parameter | Type | Description  
---|---|---  
_optional_ width | number | width, leave undefined to use the default  
_optional_ height | number | height, leave undefined to use the default  
## Methods
### beginstroke
Begin definition of a stroked path
```
beginstroke(stroke_style: "basic2d" | "line");

```
Name | Type | Description  
---|---|---  
stroke_style | "basic2d" | "line" | the stroke style to use  
### circle
Draw a circle or an arc
Draws a filled circle with radius specified by the radius argument at the current drawing position. If theta_start and theta_end are specified, then an arc will be drawn instead of a full circle. Affected by shapeorient, shapeslice, and shapeprim values.
```
circle(radius: number, theta_start?: number, theta_end?: number);

```
Name | Type | Description  
---|---|---  
radius | number | radius of the circle  
_optional_ theta_start | number | start angle in degrees  
_optional_ theta_end | number | end angle in degrees  
### copypixels
Copy pixels from one object to the current sketch
Copies pixels from the source object to the location specified by the destination_x and destination_y arguments. The initial x and y offset into the source and size of the rectangle copied can be speified by the source_x, source_y, width and height arguments. If these are not present, an x and y offset of zero and width and height equal to the source image is assumed. No scaling of pixels is supported. If blending is enabled in the destination sketch object, alpha blending will be performed and the current alpha color will also be applied globally. he copypixels method is much faster than obtaining the equivalent result using glbindtexture() to texture a plane, and is the recommended means of drawing images when scaling and rotation are not required.
```
copypixels(source_obj: Sketch | Image, destination_x: number, destination_y: number, source_x?: number, source_y?: number, width?: number, height?: number);

```
Name | Type | Description  
---|---|---  
source_obj |  [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") | the source object to copy pixels from  
destination_x | number | x coordinate of the destination  
destination_y | number | y coordinate of the destination  
_optional_ source_x | number | x coordinate of the source  
_optional_ source_y | number | y coordinate of the source  
_optional_ width | number | width  
_optional_ height | number | height  
### cube
Draw a cube
The cube will have width = 2 * scale_x, height = 2 * scale_y, and depth = 2 * scale_z, and will be centered at the current drawing position. By default, scale_y and scale_z will be equal to scale_x. Affected by shapeorient, shapeslice, and shapeprim values.
```
cube(scale_x: number, scale_y?: number, scale_z?: number);

```
Name | Type | Description  
---|---|---  
scale_x | number | half width  
_optional_ scale_y | number | half height  
_optional_ scale_z | number | half depth  
### cylinder
Draw a cylinder or cylindrical arc
Draws a cylinder with top radius specified by the radius1 argument, bottom radius specified by the radius2 argument, length specified by the mag argument, and center point at the current drawing position. If the theta_start and theta_end arguments are specified, then a cylindrical wedge will be drawn instead of a full cylinder. Affected by shapeorient, shapeslice, and shapeprim values.
```
cylinder(radius1: number, radius2: number, mag: number, theta_start?: number, theta_end?: number);

```
Name | Type | Description  
---|---|---  
radius1 | number | radius of one end of the cylinder  
radius2 | number | radius of the other end of the cylinder  
mag | number | height of the cylinder  
_optional_ theta_start | number | start angle in degrees  
_optional_ theta_end | number | end angle in degrees  
### default2d
Set the default graphics state for 2d rendering
The default2d method is a simple way to set the graphics state to default properties useful for 2D graphics. It is called everytime your object is resized if default2d() has been called more recently than default3d(). It is essentially equivalent to the following set of calls:
```
default2d();

```

#### Example
```
with (sketch) {
	glpolygonmode("front_and_back", "fill")
	glpointsize(1)
	gllinewidth(1)
	gldisable("depth_test")
	gldisable("fog")
	glcolor(0, 0, 0, 1)
	glshademodel("smooth")
	gldisable("lighting")
	gldisable("normalize")
	gldisable("texture")
	glmatrixmode("projection")
	glloadidentity()
	glortho(-aspect, aspect, -1, 1, -1, 100)
	glmatrixmode("modelview")
	glloadidentity()
	glulookat(0, 0, 2, 0, 0, 0, 0, 0, 1)
	glclearcolor(1, 1, 1, 1)
	glclear()
	glenable("blend")
	glblendfunc("src_alpha", "one_minus_src_alpha")
}

```

### default3d
Set the default graphics state for 3d rendering
The default3d method is a simple way to set the graphics state to default properties useful for 3D graphics. It is called everytime the jsui object is resized if default3d() has been called more recently than default2d(). It is essentially equivalent to the following set of calls:
```
default3d();

```

#### Example
```
with (sketch) {
	glpolygonmode("front_and_back", "fill")
	glpointsize(1)
	gllinewidth(1)
	glenable("depth_test")
	glenable("fog")
	glcolor(0, 0, 0, 1)
	glshademodel("smooth")
	gllightmodel("two_side", "true")
	glenable("lighting")
	glenable("light0")
	glenable("normalize")
	gldisable("texture")
	glmatrixmode("projection")
	glloadidentity()
	gluperspective(default_lens_angle, aspect, 0.1, 100)
	glmatrixmode("modelview")
	glloadidentity()
	glulookat(0, 0, 2, 0, 0, 0, 0, 0, 1)
	glclearcolor(1, 1, 1, 1)
	glclear()
	glenable("blend")
	glblendfunc("src_alpha", "one_minus_src_alpha")
}

```

### depthatpixel
Get the depth at a given pixel
Returns the depth value associated with the currently rendered pixel at a given absolute screen coordinate.
```
depthatpixel(x: number, y: number): number;

```
Name | Type | Description  
---|---|---  
x | number | screen x coordinate  
y | number | screen y coordinate  
Return Value | number |   
### ellipse
Draw an ellipse or elliptical arc
Draws a filled ellipse with radii specified by the radius1 and radius2 arguments. If theta_start and theta_end are specified, then an arc will be drawn instead of a full ellipse. Affected by shapeorient, shapeslice, and shapeprim values.
```
ellipse(radius1: number, radius2: number, theta_start?: number, theta_end?: number);

```
Name | Type | Description  
---|---|---  
radius1 | number | radius of the first axis  
radius2 | number | radius of the second axis  
_optional_ theta_start | number | start angle in degrees  
_optional_ theta_end | number | end angle in degrees  
### endstroke
End definition of a path and render it
```
endstroke();

```

### font
Set the current font
```
font(font_name: string);

```
Name | Type | Description  
---|---|---  
font_name | string | name of the font  
### fontsize
Set the font size in points
```
fontsize(size: number);

```
Name | Type | Description  
---|---|---  
size | number | size of the font  
### framecircle
Draw a framed circle or arc
Draws a framed circle with radius specified by the radius argument at the current drawing position. If theta_start and theta_end are specified, then an arc will be drawn instead of a full circle. Affected by shapeorient, shapeslice, and shapeprim values.
```
framecircle(radius: number, theta_start?: number, theta_end?: number);

```
Name | Type | Description  
---|---|---  
radius | number | radius of the circle  
_optional_ theta_start | number | start angle in degrees  
_optional_ theta_end | number | end angle in degrees  
### frameellipse
Draw a framed ellipse or elliptical arc
Draws a framed ellipse with radii specified by the radius1 and radius2 arguments. If theta_start and theta_end are specified, then an arc will be drawn instead of a full ellipse. Affected by shapeorient, shapeslice, and shapeprim values.
```
frameellipse(radius1: number, radius2: number, theta_start?: number, theta_end?: number);

```
Name | Type | Description  
---|---|---  
radius1 | number | radius of the first axis  
radius2 | number | radius of the second axis  
_optional_ theta_start | number | start angle in degrees  
_optional_ theta_end | number | end angle in degrees  
### framequad
Draw a framed quadrilateral
After this method has been called, the drawing position is updated to the location specified by the x4, y4, and z4 arguments.
```
framequad(x1: number, y1: number, z1: number, x2: number, y2: number, z2: number, x3: number, y3: number, z3: number, x4: number, y4: number, z4: number);

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of the first point  
y1 | number | y coordinate of the first point  
z1 | number | z coordinate of the first point  
x2 | number | x coordinate of the second point  
y2 | number | y coordinate of the second point  
z2 | number | z coordinate of the second point  
x3 | number | x coordinate of the third point  
y3 | number | y coordinate of the third point  
z3 | number | z coordinate of the third point  
x4 | number | x coordinate of the fourth point  
y4 | number | y coordinate of the fourth point  
z4 | number | z coordinate of the fourth point  
### frametri
Draw a framed triangle
After this method has been called, the drawing position is updated to the location specified by the x3, y3, and z3 arguments.
```
frametri(x1: number, y1: number, z1: number, x2: number, y2: number, z2: number, x3: number, y3: number, z3: number);

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of the first point  
y1 | number | y coordinate of the first point  
z1 | number | z coordinate of the first point  
x2 | number | x coordinate of the second point  
y2 | number | y coordinate of the second point  
z2 | number | z coordinate of the second point  
x3 | number | x coordinate of the third point  
y3 | number | y coordinate of the third point  
z3 | number | z coordinate of the third point  
### freepeer
Free the native C peer
Frees data from the native C peer (created when making a [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") object), which is not considered by the JavaScript garbage collector, and may consume lots of memory until the garbage collector decides to run based JS allocated memory. Once called, the [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") object is not available for any other use. It's not necessary to call this function, as the memory will be freed eventually, but you can call it whenever you're done with your [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") object.
```
freepeer();

```

### getpixel
Get the pixel data at a given point
Returns an array containing the pixel value at the specified location. This array is ordered RGBA, i.e. array element 0 is red, 1, green, 2, blue, 3 alpha. Color values are floating point numbers in the range 0.-1.
```
getpixel(x: number, y: number): [number, number, number, number];

```
Name | Type | Description  
---|---|---  
x | number | x coordinate  
y | number | y coordinate  
Return Value | [number, number, number, number] |   
### gettextinfo
Get the rendered size of text
Returns an array containing the width and height of the given string in absolute screen coordinates, taking into account the current font and fontsize.
```
gettextinfo(text: string): [number, number];

```
Name | Type | Description  
---|---|---  
text | string | text to measure  
Return Value | [number, number] |   
### glbegin
Begin drawing using low level OpenGL functions
The low level OpenGL function calls (all beginning with gl) are thin wrappers around direct calls to the graphics engine. Typically, use these function calls between calls to [Sketch.glbegin()](https://docs.cycling74.com/apiref/js/sketch/#glbegin "Sketch.glbegin\(\)") and [Sketch.glend()](https://docs.cycling74.com/apiref/js/sketch/#glend "Sketch.glend\(\)"). For many of these functions, look up the documentation for the OpenGL function with the same (or very similar) name.
```
glbegin(prim_type: DrawingPrimitiveType);

```
Name | Type | Description  
---|---|---  
prim_type | [DrawingPrimitiveType](https://docs.cycling74.com/apiref/js/drawingprimitivetype/ "DrawingPrimitiveType") | the drawing primitive to use  
#### Example
```
var sx = 1.0;
var sy = 1.0;
var tx = 0.0;
var ty = 0.0;
function draw() {
	// refers to the global "sketch" object
 sketch.glclear();

	sketch.glcolor(1, 0, 0);
	sketch.glbegin("lines");

 // draw x axis
	glvertex(Math.min(tx + sx * -1, -1),  ty, 0);
	glvertex(Math.max(tx + sx * 1, 1),  ty, 0);

 // draw y axis
	glvertex(tx,  Math.min(ty + sy * -1, -1), 0);
	glvertex(tx,  Math.max(ty + sy * 1, 1), 0);
}

```

### glbindtexture
Apply the given texture to subsequent drawing calls
Note: this method also calls glenable(texture)
```
glbindtexture(image: Image);

```
Name | Type | Description  
---|---|---  
image | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") | the image to use as a texture  
### glblendfunc
```
glblendfunc(src_func: string, dst_func: string);

```
Name | Type | Description  
---|---|---  
src_func | string | source function  
dst_func | string | destination function  
### glclear
Clear the drawing context
```
glclear();

```

### glclearcolor
Set the color to fill the context with using [Sketch.glclear()](https://docs.cycling74.com/apiref/js/sketch/#glclear "Sketch.glclear\(\)")
```
glclearcolor(red: number, green: number, blue: number, alpha: number = 1);

```
Name | Type | Description  
---|---|---  
red | number | red (0-1 range)  
green | number | green (0-1 range)  
blue | number | blue (0-1 range)  
_optional_ alpha | number | alpha (0-1 range)  
### glclearcolor
```
glclearcolor(colors: number[]);

```
Name | Type | Description  
---|---|---  
colors | number[] |   
### glcleardepth
Set the depth to fill the context with using [Sketch.glclear()](https://docs.cycling74.com/apiref/js/sketch/#glclear "Sketch.glclear\(\)")
```
glcleardepth(depth: number);

```
Name | Type | Description  
---|---|---  
depth | number | depth (0-1 range)  
### glclipplane
```
glclipplane(plane: number, coeff1: number, coeff2: number, coeff3: number, coeff4: number);

```
Name | Type | Description  
---|---|---  
plane | number |   
coeff1 | number |   
coeff2 | number |   
coeff3 | number |   
coeff4 | number |   
### glclipplane
```
glclipplane(planeValues: number[]);

```
Name | Type | Description  
---|---|---  
planeValues | number[] |   
### glcolor
Set the color for subsequent drawing calls
```
glcolor(red: number, green: number, blue: number, alpha: number = 1);

```
Name | Type | Description  
---|---|---  
red | number | red (0-1 range)  
green | number | green (0-1 range)  
blue | number | blue (0-1 range)  
_optional_ alpha | number | alpha (0-1 range)  
### glcolor
```
glcolor(colors: number[]);

```
Name | Type | Description  
---|---|---  
colors | number[] |   
### glcolormask
```
glcolormask(red: number, green: number, blue: number, alpha: number = 1);

```
Name | Type | Description  
---|---|---  
red | number |   
green | number |   
blue | number |   
_optional_ alpha | number |   
### glcolormask
```
glcolormask(colors: number[]);

```
Name | Type | Description  
---|---|---  
colors | number[] |   
### glcolormaterial
```
glcolormaterial(face: number, mode: number);

```
Name | Type | Description  
---|---|---  
face | number |   
mode | number |   
### glcullface
```
glcullface(face: number);

```
Name | Type | Description  
---|---|---  
face | number |   
### gldepthmask
```
gldepthmask(onoff: number);

```
Name | Type | Description  
---|---|---  
onoff | number |   
### gldepthrange
```
gldepthrange(near: number, far: number);

```
Name | Type | Description  
---|---|---  
near | number |   
far | number |   
### gldisable
Disable a drawing capaility.
Usually "blend", "line_smooth", or "texture"
```
gldisable(capability: string);

```
Name | Type | Description  
---|---|---  
capability | string | the capability to disable  
### gldrawpixels
```
gldrawpixels(image: Image);

```
Name | Type | Description  
---|---|---  
image | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") |   
### gledgeflag
```
gledgeflag(onoff: number);

```
Name | Type | Description  
---|---|---  
onoff | number |   
### glenable
Enable a drawing capaility.
Usually "blend", "line_smooth", or "texture"
```
glenable(capability: string);

```
Name | Type | Description  
---|---|---  
capability | string | the capability to enable  
### glend
```
glend();

```

### glfinish
```
glfinish();

```

### glflush
```
glflush();

```

### glfog
```
glfog(parameter_name: string, ...values: number);

```
Name | Type | Description  
---|---|---  
parameter_name | string |   
values | number |   
### glfrustrum
```
glfrustrum(left: number, right: number, bottom: number, top: number, near: number, far: number);

```
Name | Type | Description  
---|---|---  
left | number |   
right | number |   
bottom | number |   
top | number |   
near | number |   
far | number |   
### glfrustrum
```
glfrustrum(frustrumValues: number[]);

```
Name | Type | Description  
---|---|---  
frustrumValues | number[] |   
### glhint
```
glhint(target: string, mode: number);

```
Name | Type | Description  
---|---|---  
target | string |   
mode | number |   
### gllight
```
gllight(light: string, parameter_name: string, ...values: number);

```
Name | Type | Description  
---|---|---  
light | string |   
parameter_name | string |   
values | number |   
### gllightmodel
```
gllightmodel(light: string, model: number);

```
Name | Type | Description  
---|---|---  
light | string |   
model | number |   
### gllinestipple
```
gllinestipple(factor: any, bit_pattern: any);

```
Name | Type | Description  
---|---|---  
factor | any |   
bit_pattern | any |   
### gllinewidth
```
gllinewidth(width: number);

```
Name | Type | Description  
---|---|---  
width | number |   
### glloadidentity
Load the identity matrix
```
glloadidentity();

```

### glloadmatrix
```
glloadmatrix(matrix_array: number[]);

```
Name | Type | Description  
---|---|---  
matrix_array | number[] |   
### gllogicop
```
gllogicop(op: number);

```
Name | Type | Description  
---|---|---  
op | number |   
### glmaterial
```
glmaterial();

```

### glmatrixmode
```
glmatrixmode(mode: string);

```
Name | Type | Description  
---|---|---  
mode | string |   
### glmultmatrix
```
glmultmatrix(matrix_array: number[]);

```
Name | Type | Description  
---|---|---  
matrix_array | number[] |   
### glnormal
```
glnormal(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number |   
y | number |   
z | number |   
### glortho
```
glortho(left: number, right: number, bottom: number, top: number, near: number, far: number);

```
Name | Type | Description  
---|---|---  
left | number |   
right | number |   
bottom | number |   
top | number |   
near | number |   
far | number |   
### glortho
```
glortho(orthoValues: number[]);

```
Name | Type | Description  
---|---|---  
orthoValues | number[] |   
### glpointsize
```
glpointsize(size: number);

```
Name | Type | Description  
---|---|---  
size | number |   
### glpolygonmode
```
glpolygonmode(face: number, mode: number);

```
Name | Type | Description  
---|---|---  
face | number |   
mode | number |   
### glpolygonoffset
```
glpolygonoffset(factor: number, units: number);

```
Name | Type | Description  
---|---|---  
factor | number |   
units | number |   
### glpopattrib
```
glpopattrib();

```

### glpopmatrix
```
glpopmatrix();

```

### glpushattrib
```
glpushattrib();

```

### glpushmatrix
```
glpushmatrix();

```

### glrect
```
glrect(x1: number, y1: number, x2: number, y2: number);

```
Name | Type | Description  
---|---|---  
x1 | number |   
y1 | number |   
x2 | number |   
y2 | number |   
### glrect
```
glrect(rectValues: number[]);

```
Name | Type | Description  
---|---|---  
rectValues | number[] |   
### glrotate
```
glrotate(angle: number, x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
angle | number |   
x | number |   
y | number |   
z | number |   
### glrotate
```
glrotate(rotateValues: number[]);

```
Name | Type | Description  
---|---|---  
rotateValues | number[] |   
### glscale
```
glscale(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number |   
y | number |   
z | number |   
### glscale
```
glscale(scaleValues: number[]);

```
Name | Type | Description  
---|---|---  
scaleValues | number[] |   
### glscissor
```
glscissor(x: number, y: number, width: number, height: number);

```
Name | Type | Description  
---|---|---  
x | number |   
y | number |   
width | number |   
height | number |   
### glscissor
```
glscissor(scissorValues: number[]);

```
Name | Type | Description  
---|---|---  
scissorValues | number[] |   
### glshademodel
```
glshademodel(mode: number);

```
Name | Type | Description  
---|---|---  
mode | number |   
### gltexcoord
```
gltexcoord(s: number, t: number);

```
Name | Type | Description  
---|---|---  
s | number |   
t | number |   
### gltexenv
```
gltexenv(parameter_name: string, val1: number, val2: number, val3: number, val4: number);

```
Name | Type | Description  
---|---|---  
parameter_name | string |   
val1 | number |   
val2 | number |   
val3 | number |   
val4 | number |   
### gltexgen
```
gltexgen(coord: number[], parameter_name: string, val1: number, val2: number, val3: number, val4: number);

```
Name | Type | Description  
---|---|---  
coord | number[] |   
parameter_name | string |   
val1 | number |   
val2 | number |   
val3 | number |   
val4 | number |   
### gltexparameter
```
gltexparameter(parameter_name: string, val1: number, val2: number, val3: number, val4: number);

```
Name | Type | Description  
---|---|---  
parameter_name | string |   
val1 | number |   
val2 | number |   
val3 | number |   
val4 | number |   
### gltranslate
```
gltranslate(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number |   
y | number |   
z | number |   
### gltranslate
```
gltranslate(translateValues: number[]);

```
Name | Type | Description  
---|---|---  
translateValues | number[] |   
### glulookat
```
glulookat(eye_x: number, eye_y: number, eye_z: number, center_x: number, center_y: number, center_z: number, up_x: number, up_y: number, up_z: number);

```
Name | Type | Description  
---|---|---  
eye_x | number |   
eye_y | number |   
eye_z | number |   
center_x | number |   
center_y | number |   
center_z | number |   
up_x | number |   
up_y | number |   
up_z | number |   
### glulookat
```
glulookat(lookatValues: number[]);

```
Name | Type | Description  
---|---|---  
lookatValues | number[] |   
### gluortho2d
```
gluortho2d(left: number, right: number, bottom: number, top: number);

```
Name | Type | Description  
---|---|---  
left | number |   
right | number |   
bottom | number |   
top | number |   
### gluortho2d
```
gluortho2d(orthoValues: number[]);

```
Name | Type | Description  
---|---|---  
orthoValues | number[] |   
### gluperspective
```
gluperspective(fovy: number, aspect: number, near: number, far: number);

```
Name | Type | Description  
---|---|---  
fovy | number |   
aspect | number |   
near | number |   
far | number |   
### gluperspective
```
gluperspective(perspectiveValues: number[]);

```
Name | Type | Description  
---|---|---  
perspectiveValues | number[] |   
### glvertex
```
glvertex(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number |   
y | number |   
z | number |   
### glvertex
```
glvertex(vertexValues: number[]);

```
Name | Type | Description  
---|---|---  
vertexValues | number[] |   
### glviewport
```
glviewport(x: number, y: number, width: number, height: number);

```
Name | Type | Description  
---|---|---  
x | number |   
y | number |   
width | number |   
height | number |   
### glviewport
```
glviewport(viewportValues: number[]);

```
Name | Type | Description  
---|---|---  
viewportValues | number[] |   
### line
Draw a line relative to the current position
Draws a line from the current drawing position to the location specified by adding the delta x, y, and z arguments to the current position. After this method has been called, the drawing position is updated by an offset relative to the original drawing position.
```
line(dx: number, dy: number, dz: number);

```
Name | Type | Description  
---|---|---  
dx | number | x offset  
dy | number | y offset  
dz | number | z offset  
### linesegment
Draw a line segment
Draws a line from the location specified by the x1, y1, and z1 arguments to the location specified by the x2, y2, and z2 arguments. After this method has been called, the drawing position is updated to the location specified by the x2, y2, and z2 arguments.
```
linesegment(x1: number, y1: number, z1: number, x2: number, y2: number, z2: number);

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of the start point  
y1 | number | y coordinate of the start point  
z1 | number | z coordinate of the start point  
x2 | number | x coordinate of the end point  
y2 | number | y coordinate of the end point  
z2 | number | z coordinate of the end point  
### lineto
Draw a line to the specified position
Draws a line from the current drawing position to the location specified by the x, y, and z arguments. After this method has been called, the drawing position is updated to the location specified by the x, y, and z arguments.
```
lineto(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate  
y | number | y coordinate  
z | number | z coordinate  
### move
Move the drawing position relatively
Moves the drawing position to the location specified by the sum of the current drawing position and the delta x, y, and z arguments.
```
move(dx: number, dy: number, dz: number);

```
Name | Type | Description  
---|---|---  
dx | number | x offset  
dy | number | y offset  
dz | number | z offset  
### moveto
Move the current drawing position
Moves the drawing position to the location specified by the x, y, and z arguments.
```
moveto(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate  
y | number | y coordinate  
z | number | z coordinate  
### ortho3d
Set the default graphics state for rendering with orthographic projection
The orth3d method is a simple way to set the graphics state to default properties useful for 3D graphics, using an orthographic projection (i.e. object scale is not affected by distance from the camera). It is called every time the jsui object is resized if ortho3d() has been called more recently than default2d(), or default3d(). It is essentially equivalent to the following set of calls:
```
ortho3d();

```

#### Example
```
with (sketch) {
	glpolygonmode("front_and_back", "fill")
	glpointsize(1)
	gllinewidth(1)
	glenable("depth_test")
	glenable("fog")
	glcolor(0, 0, 0, 1)
	glshademodel("smooth")
	gllightmodel("two_side", "true")
	glenable("lighting")
	glenable("light0")
	glenable("normalize")
	gldisable("texture")
	glmatrixmode("projection")
	glloadidentity()
	glortho(-aspect, aspect, -1, 1, -1, 100)
	glmatrixmode("modelview")
	glloadidentity()
	glulookat(0, 0, 2, 0, 0, 0, 0, 0, 1)
	glclearcolor(1, 1, 1, 1)
	glclear()
	glenable("blend")
	glblendfunc("src_alpha", "one_minus_src_alpha")
}

```

### plane
Draw a plane
Draws a plane with top width = 2 * scale_x1, left height = 2 * scale_y1, bottom width = 2 * scale_x2, right height = 2 * scale_y2, and center point at the current drawing position. If scale_y1 is not specified, it will assume the same value as scale_x1. If scale_x2 and scale_y2 are not specified, they will assume the same values as scale_x1 and scale_y1 respectively. Affected by shapeorient, shapeslice, and shapeprim values.
```
plane(scale_x1: number, scale_y1?: number, scale_x2?: number, scale_y2?: number);

```
Name | Type | Description  
---|---|---  
scale_x1 | number | half top width  
_optional_ scale_y1 | number | half left height  
_optional_ scale_x2 | number | half bottom width  
_optional_ scale_y2 | number | half right height  
### point
Draw a point
Draws a point at the location specified by the x, y, and z arguments. After this method has been called, the drawing position is updated to the specified location.
```
point(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate  
y | number | y coordinate  
z | number | z coordinate  
### quad
Draw a filled quadrilateral
After this method has been called, the drawing position is updated to the location specified by the x4, y4, and z4 arguments.
```
quad(x1: number, y1: number, z1: number, x2: number, y2: number, z2: number, x3: number, y3: number, z3: number, x4: number, y4: number, z4: number);

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of the first point  
y1 | number | y coordinate of the first point  
z1 | number | z coordinate of the first point  
x2 | number | x coordinate of the second point  
y2 | number | y coordinate of the second point  
z2 | number | z coordinate of the second point  
x3 | number | x coordinate of the third point  
y3 | number | y coordinate of the third point  
z3 | number | z coordinate of the third point  
x4 | number | x coordinate of the fourth point  
y4 | number | y coordinate of the fourth point  
z4 | number | z coordinate of the fourth point  
### roundedplane
Draw a plane with rounded corners
Draws a rounded plane with width = 2 * scale_x, height = 2 * scale_y, and center point at the current drawing position. The radius of the rounded portion of the plane is determined by the round_amount argument. If scale_y is not specified, it will assume the same value as scale_x. Affected by shapeorient, shapeslice, and shapeprim values.
```
roundedplane(round_amount: number, scale_x1: number, scale_y1?: number);

```
Name | Type | Description  
---|---|---  
round_amount | number | radius of the rounded corners  
scale_x1 | number | half width  
_optional_ scale_y1 | number | half height  
### screentoworld
Return the world coordinate for a point on screen
Returns an array containing the x, y, and z world coordinates associated with a given screen pixel using the same the depth from the camera as 0, 0, 0. Optionally a third depth arg may be specified, which may be useful for hit detection and other applications. The depth value is typically specified in the range 0.-1. where 0 is the near clipping plane, and 1. is the far clipping plane. The worldtoscreen method can be used to determine the depth value of a given world coordinate, and the [Sketch.depthatpixel()](https://docs.cycling74.com/apiref/js/sketch/#depthatpixel "Sketch.depthatpixel\(\)") method can be used to determine the depth value associated with the currently rendered pixel at a given absolute screen coordinate.
```
screentoworld(x: number, y: number, depth?: number): [number, number, number];

```
Name | Type | Description  
---|---|---  
x | number | screen x coordinate  
y | number | screen y coordinate  
_optional_ depth | number | range from 0 (near clipping plane) to 1 (far clipping plane)  
Return Value | [number, number, number] |   
### setpixel
Set the pixel value at a given location
Sets the pixel value at the specified location. Color values are floating point numbers in the range 0.-1.
```
setpixel(x: number, y: number, red: number, green: number, blue: number, alpha: number);

```
Name | Type | Description  
---|---|---  
x | number | x  
y | number | y  
red | number | red  
green | number | green  
blue | number | blue  
alpha | number | alpha  
### shapeorient
Set rotation for shape drawing calls
Sets the rotation in x, y, and z for future shape drawing calls.
```
shapeorient(rotation_x: number, rotation_y: number, rotation_z: number);

```
Name | Type | Description  
---|---|---  
rotation_x | number | x rotation in degrees  
rotation_y | number | y rotation in degrees  
rotation_z | number | z rotation in degrees  
### shapeprim
Set the drawing primitive shape
Sets the OpenGL drawing primitive to use within any of the "shape" drawing methods.
```
shapeprim(draw_prim: DrawingPrimitiveType);

```
Name | Type | Description  
---|---|---  
draw_prim | [DrawingPrimitiveType](https://docs.cycling74.com/apiref/js/drawingprimitivetype/ "DrawingPrimitiveType") | the drawing primitive to use  
### shapeslice
Set the number of slices to use when rendering shapes
Increasing the slice_a and slice_b arguments will increase the quality at which the shape is rendered, while decreasing these values will improve performance.
```
shapeslice(slice_a: number, slice_b: number);

```
Name | Type | Description  
---|---|---  
slice_a | number | number of slices to use  
slice_b | number | number of slices to use  
### sphere
Draw a sphere
Draws a sphere with the given radius, centered at the current drawing position. If the theta1_start, theta1_end, theta2_start, and theta2_end arguments are specified, then a section will be drawn instead of a full sphere. Affected by shapeorient, shapeslice, and shapeprim values.
```
sphere(radius: number, theta1_start?: number, theta1_end?: number, theta2_start?: number, theta2_end?: number);

```
Name | Type | Description  
---|---|---  
radius | number | radius of the sphere  
_optional_ theta1_start | number | start angle in degrees (0 - 360)  
_optional_ theta1_end | number | end angle in degrees (0 - 360)  
_optional_ theta2_start | number | start angle in degrees (0 - 360)  
_optional_ theta2_end | number | end angle in degrees (0 - 360)  
### strokeparam
Set the value for a given stroke param. Depending on the parameter, may apply to each point, or to the path as a whole. See [Basic2dStrokeStyleParameterNames](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/ "Basic2dStrokeStyleParameterNames") and [LineStrokeStyleParameterNames](https://docs.cycling74.com/apiref/js/linestrokestyleparameternames/ "LineStrokeStyleParameterNames").
```
strokeparam(parameter_name: Basic2dStrokeStyleParameterNames.alpha, value: number);

```
Name | Type | Description  
---|---|---  
parameter_name | [Basic2dStrokeStyleParameterNames.alpha](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/#alpha "Basic2dStrokeStyleParameterNames.alpha") |   
value | number |   
### strokeparam
```
strokeparam(parameter_name: LineStrokeStyleParameterNames.order, order: number = 3);

```
Name | Type | Description  
---|---|---  
parameter_name | [LineStrokeStyleParameterNames.order](https://docs.cycling74.com/apiref/js/linestrokestyleparameternames/#order "LineStrokeStyleParameterNames.order") |   
_optional_ order | number |   
### strokeparam
```
strokeparam(parameter_name: LineStrokeStyleParameterNames.slices, slice_count: number = 20);

```
Name | Type | Description  
---|---|---  
parameter_name | [LineStrokeStyleParameterNames.slices](https://docs.cycling74.com/apiref/js/linestrokestyleparameternames/#slices "LineStrokeStyleParameterNames.slices") |   
_optional_ slice_count | number |   
### strokeparam
```
strokeparam(parameter_name: Basic2dStrokeStyleParameterNames.color, red: number, green: number, blue: number, alpha: number);

```
Name | Type | Description  
---|---|---  
parameter_name | [Basic2dStrokeStyleParameterNames.color](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/#color "Basic2dStrokeStyleParameterNames.color") |   
red | number |   
green | number |   
blue | number |   
alpha | number |   
### strokeparam
```
strokeparam(parameter_name: Basic2dStrokeStyleParameterNames.order, order: number = 3);

```
Name | Type | Description  
---|---|---  
parameter_name | [Basic2dStrokeStyleParameterNames.order](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/#order "Basic2dStrokeStyleParameterNames.order") |   
_optional_ order | number |   
### strokeparam
```
strokeparam(parameter_name: Basic2dStrokeStyleParameterNames.outcolor, red: number, green: number, blue: number, alpha: number);

```
Name | Type | Description  
---|---|---  
parameter_name | [Basic2dStrokeStyleParameterNames.outcolor](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/#outcolor "Basic2dStrokeStyleParameterNames.outcolor") |   
red | number |   
green | number |   
blue | number |   
alpha | number |   
### strokeparam
```
strokeparam(parameter_name: Basic2dStrokeStyleParameterNames.outline, active: 0 | 1);

```
Name | Type | Description  
---|---|---  
parameter_name | [Basic2dStrokeStyleParameterNames.outline](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/#outline "Basic2dStrokeStyleParameterNames.outline") |   
active | 0 | 1 |   
### strokeparam
```
strokeparam(parameter_name: Basic2dStrokeStyleParameterNames.scale, width: number);

```
Name | Type | Description  
---|---|---  
parameter_name | [Basic2dStrokeStyleParameterNames.scale](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/#scale "Basic2dStrokeStyleParameterNames.scale") |   
width | number |   
### strokeparam
```
strokeparam(parameter_name: Basic2dStrokeStyleParameterNames.slices, slice_count: number = 20);

```
Name | Type | Description  
---|---|---  
parameter_name | [Basic2dStrokeStyleParameterNames.slices](https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/#slices "Basic2dStrokeStyleParameterNames.slices") |   
_optional_ slice_count | number |   
### strokeparam
```
strokeparam(parameter_name: LineStrokeStyleParameterNames.alpha, value: number);

```
Name | Type | Description  
---|---|---  
parameter_name | [LineStrokeStyleParameterNames.alpha](https://docs.cycling74.com/apiref/js/linestrokestyleparameternames/#alpha "LineStrokeStyleParameterNames.alpha") |   
value | number |   
### strokeparam
```
strokeparam(parameter_name: LineStrokeStyleParameterNames.color, red: number, green: number, blue: number, alpha: number);

```
Name | Type | Description  
---|---|---  
parameter_name | [LineStrokeStyleParameterNames.color](https://docs.cycling74.com/apiref/js/linestrokestyleparameternames/#color "LineStrokeStyleParameterNames.color") |   
red | number |   
green | number |   
blue | number |   
alpha | number |   
### strokepoint
Add an anchor point to the current path
Some stroke styles such as "basic2d" will ignore the z coordinate.
```
strokepoint(x: number, y: number, z: number);

```
Name | Type | Description  
---|---|---  
x | number | x  
y | number | y  
z | number | z  
### text
Draw the given text
Draws the text specified by the string argument at the current drawing position, taking into account the current font, fontsize, and text alignment. Text is strictly 2D, and does not take into account any world transformations. After calling the text method, if the x axis text alignment is set to "left", the current drawing position will be updated to reflect the world position associated with the end of the string. If the x axis text alignment is set to "right", the current drawing position will be updated to reflect the world position associated with the end of the string. If the x axis text alignment is set to "center", the current drawing position will remain unchanged.
```
text(text: string);

```
Name | Type | Description  
---|---|---  
text | string | text to draw  
### textalign
Set the text alignment in x and y
Sets the alignment of text to be drawn with respect to the current drawing position. Default alignment is "left" and "bottom".
```
textalign(align_x: "left" | "center" | "right", align_y: "top" | "center" | "bottom");

```
Name | Type | Description  
---|---|---  
align_x | "left" | "center" | "right" | horizontal alignment  
align_y | "top" | "center" | "bottom" | vertical alignment  
### torus
Draw a torus
Draw a torus centered at the current drawing position. If theta1_start, theta1_end, theta2_start, and theta2_end are specified, then a section will be drawn instead of a full torus. Affected by shapeorient, shapeslice, and shapeprim values.
```
torus(major_radius: number, minor_radius: number, theta1_start?: number, theta1_end?: number, theta2_start?: number, theta2_end?: number);

```
Name | Type | Description  
---|---|---  
major_radius | number | major radius  
minor_radius | number | minor radius  
_optional_ theta1_start | number | start angle in degrees (0 - 360)  
_optional_ theta1_end | number | end angle in degrees (0 - 360)  
_optional_ theta2_start | number | start angle in degrees (0 - 360)  
_optional_ theta2_end | number | end angle in degrees (0 - 360)  
### tri
Draw a filled triangle
After this method has been called, the drawing position is updated to the location specified by the x3, y3, and z3 arguments.
```
tri(x1: number, y1: number, z1: number, x2: number, y2: number, z2: number, x3: number, y3: number, z3: number);

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of the first point  
y1 | number | y coordinate of the first point  
z1 | number | z coordinate of the first point  
x2 | number | x coordinate of the second point  
y2 | number | y coordinate of the second point  
z2 | number | z coordinate of the second point  
x3 | number | x coordinate of the third point  
y3 | number | y coordinate of the third point  
z3 | number | z coordinate of the third point  
### worldtoscreen
Returns the screen coordinate for a given world coordinate
Returns an array containing the x, y, and depth screen coordinates associated with a given world coordinate. The depth value is typically specified in the range 0.-1. where 0 is the near clipping plane, and 1. is the far clipping plane.
```
worldtoscreen(x: number, y: number, z: number): [number, number, number];

```
Name | Type | Description  
---|---|---  
x | number | world x coordinate  
y | number | world y coordinate  
z | number | world z coordinate  
Return Value | [number, number, number] | 
