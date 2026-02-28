---
description: Drawing context for rendering shapes and images.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/mgraphics/
title: class MGraphics
---

# class MGraphics
Drawing context for rendering shapes and images.
The MGraphics object combines a virtual drawing canvas with functions to manage drawing to that canvas. In enables you to draw simple shapes, complex paths, text, and images.
Most of the time, you'll work with the global MGraphics object, always stored in a global variable called mgraphics, in order to perform custom drawing of a jsui object, or in a jspainter file. In that case, make sure to call the [MGraphics.init()](https://docs.cycling74.com/apiref/js/mgraphics/#init "MGraphics.init\(\)") method somewhere in global scope:
```
// Initialize mgraphics
mgraphics.init();

// Now you can use mgraphics in your custom drawing code
function paint() {
    mgraphics.rectangle(50, 0, 200, 100);
    mgraphics.fill();
}

```

It's also possible to create your own MGraphics object in order to draw to an offsceen . In this case, there is no need to call [MGraphics.init()](https://docs.cycling74.com/apiref/js/mgraphics/#init "MGraphics.init\(\)").
## Constructors
```
new MGraphics(width: number, height: number);

```

Creates a new MGraphics instance
Create a MGraphics context, including a buffer of offscreen memory to to render to, which can be used as a drawing context for creating saved or persistent images. An MGraphics instance can also be copied into an object by passing the MGraphics instance to the Image constructor.
Parameter | Type | Description  
---|---|---  
width | number | Width of the offscreen drawing area  
height | number | Height of the offscreen drawing area  
## Properties
### autofill 1 | 0
Enable or disable automatic fill after stroke.
With autofill enabled, any call to [MGraphics.stroke()](https://docs.cycling74.com/apiref/js/mgraphics/#stroke "MGraphics.stroke\(\)") will also fill the current path automatically.
### autopaint 1 | 0
Turns on/off painting of the global [MGraphics](https://docs.cycling74.com/apiref/js/mgraphics/ "MGraphics") object.
See [MGraphics.autosketch](https://docs.cycling74.com/apiref/js/mgraphics/#autosketch "MGraphics.autosketch") for technical details about managing autosketch and autopaint. In most cases, use the [MGraphics.init()](https://docs.cycling74.com/apiref/js/mgraphics/#init "MGraphics.init\(\)") method to enable custom drawing with mgraphics.
### autosketch 1 | 0
Turns on/off painting with the global sketch object.
In the context of a jsui or jspainter object, the object draws itself using two layers: sketch and mgraphics. By default, only the sketch layer renders, and the mgraphics layer is unused. If the mgraphics layer is enabled, then the object will call into the user-defined paint() function to draw the mgraphics layer on top of the sketch layer. Calling [MGraphics.init()](https://docs.cycling74.com/apiref/js/mgraphics/#init "MGraphics.init\(\)") will set autosketch to 0 and autopaint to 1, disabling the sketch layer and displaying only custom drawing in the mgraphics layer. In most cases, this is the easiest way to implement custom drawing.
### relative_coords 1 | 0
Enable or disable the use of relative coordinates.
When disabled, the origin [0, 0] will be the top-left, and [width, height] will be the bottom-right, where width and height are the dimensions of [MGraphics.size](https://docs.cycling74.com/apiref/js/mgraphics/#size "MGraphics.size"). When relative_coords is enabled, the origin [0, 0] will be in the center of the drawing area. The y-coordinate -1 will always be the top, and 1 will always be the bottom. The x-coordinate of the left edge will depend on the aspect ratio of the drawing area. If the width of the drawing area is x times the height, then the left edge will be -x and the right edge will be x.
### size [number, number] read-only
Get the current size of the MGraphics canvas
If you're using the global mgraphics instance as part of custom drawing code for jsui or with jspainter, then this will be the size of the object being redrawn.
## Methods
### append_path
Appends a stored path to the current path at the current end point.
```
append_path(path: MGraphicsPathHandle);

```
Name | Type | Description  
---|---|---  
path | [MGraphicsPathHandle](https://docs.cycling74.com/apiref/js/mgraphicspathhandle/ "MGraphicsPathHandle") | A path handle as returned from [MGraphics.copy_path()](https://docs.cycling74.com/apiref/js/mgraphics/#copy_path "MGraphics.copy_path\(\)").  
### arc_negative
Add a circular, counter-clockwise arc to the current path.
```
arc_negative(xc: number, yc: number, radius: number, angle1: number, angle2: number);

```
Name | Type | Description  
---|---|---  
xc | number | x coordinate of the center of the arc  
yc | number | y coordinate of the center of the arc  
radius | number | radius of the arc  
angle1 | number | start angle for the arc segment in radians  
angle2 | number | end angle for the arc segment in radians  
### arc
Add a circular, clockwise arc to the current path.
```
arc(xc: number, yc: number, radius: number, angle1: number, angle2: number);

```
Name | Type | Description  
---|---|---  
xc | number | x coordinate of the center of the arc  
yc | number | y coordinate of the center of the arc  
radius | number | radius of the arc  
angle1 | number | start angle for the arc segment in radians  
angle2 | number | end angle for the arc segment in radians  
### close_path
Close the current path.
Adds a line from the current point to the starting point of the path, which closes it.
```
close_path();

```

### copy_path
Returns a copy of the current path.
Returns a copy of the current path to be stored and reused later.
```
copy_path(): MGraphicsPathHandle;

```
Name | Type | Description  
---|---|---  
Return Value | [MGraphicsPathHandle](https://docs.cycling74.com/apiref/js/mgraphicspathhandle/ "MGraphicsPathHandle") |   
### curve_to
Add a cubic Bezier spline to the current path.
```
curve_to(x1: number, y1: number, x2: number, y2: number, x3: number, y3: number);

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of the first control point  
y1 | number | y coordinate of the first control point  
x2 | number | x coordinate of the second control point  
y2 | number | y coordinate of the second control point  
x3 | number | x coordinate of the destination point  
y3 | number | y coordinate of the destination point  
### device_to_user
Convert a point in device space to user space.
The inverse of [MGraphics.user_to_device()](https://docs.cycling74.com/apiref/js/mgraphics/#user_to_device "MGraphics.user_to_device\(\)").
```
device_to_user(position: [number, number]): [number, number];

```
Name | Type | Description  
---|---|---  
position | [number, number] | A two-element array containing the x, y coordinate of a point in device space.  
Return Value | [number, number] | The equivalent point in user space.  
### ellipse
Add a closed ellipse to the current path.
```
ellipse(x: number, y: number, width: number, height: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the top-left of the rectangle containing the ellipse  
y | number | y coordinate of the top-left of the rectangle containing the ellipse  
width | number | width of the ellipse  
height | number | height of the ellipse  
### fill_extent
Get the enclosing rectangle of the current path.
```
fill_extent(): [number, number, number, number];

```
Name | Type | Description  
---|---|---  
Return Value | [number, number, number, number] | An array containing the top, left, bottom, and right extremes of the rectangle.  
### fill_preserve_with_alpha
Fill and preserve the current path with alpha override.
Fill the current path, but override the alpha value of the current color with a new alpha channel value. This lets you change transparency without resetting the color values. Do not discard the path afterwards.
```
fill_preserve_with_alpha(alpha: number);

```
Name | Type | Description  
---|---|---  
alpha | number | the opacity between 0 and 1  
### fill_preserve
Draw and preserve the current path.
Fill the current path, using the current MGraphics context settings including color. Do not discard the path afterwards, which can be useful, for example, when you want to draw the stroke and fill with different colors.
```
fill_preserve();

```

### fill_with_alpha
Fill the current path with alpha override.
Fill the current path, but override the alpha value of the current color with a new alpha channel value. This lets you change transparency without resetting the color values. The path is discarded afterwards.
```
fill_with_alpha(alpha: number);

```
Name | Type | Description  
---|---|---  
alpha | number | the opacity between 0 and 1  
### fill
Fill the current path.
Fill the current path, using the current MGraphics context settings including color. The path is discarded afterwards.
```
fill();

```

### font_extents
Get ascent, descent, and height for font.
Returns the ascent, descent, and height for the current font. Ascent measures the distance from the text baseline to the tallest glyph. Descent measures the distance from the text baseline to the lowest point on any glyph under the baseline. Height is simply ascent plut descent.
```
font_extents(): [number, number, number];

```
Name | Type | Description  
---|---|---  
Return Value | [number, number, number] | An array containing font ascent, descent, and height.  
### get_current_point
The current drawing position.
This is the point at which any new additions to the current path would begin. It is also the end point of the current path, and if you close the current path, this point will be connected back to the start of the the path. Most functions that add to the path will move this point.
```
get_current_point(): [number, number];

```
Name | Type | Description  
---|---|---  
Return Value | [number, number] |   
### get_line_cap
Get the current line cap.
```
get_line_cap(): "butt" | "round" | "square";

```
Name | Type | Description  
---|---|---  
Return Value | "butt" | "round" | "square" |   
### get_line_join
Get the current line join.
```
get_line_join(): "miter" | "round" | "bevel";

```
Name | Type | Description  
---|---|---  
Return Value | "miter" | "round" | "bevel" |   
### get_line_width
Get the current line width.
```
get_line_width(): number;

```
Name | Type | Description  
---|---|---  
Return Value | number |   
### get_matrix
Retrieve the current transformation matrix.
```
get_matrix(): MGraphicsMatrixHandle;

```
Name | Type | Description  
---|---|---  
Return Value | [MGraphicsMatrixHandle](https://docs.cycling74.com/apiref/js/mgraphicsmatrixhandle/ "MGraphicsMatrixHandle") |   
### getfontlist
Get a list of installed fonts.
Get a list of all fonts installed on your system.
```
getfontlist(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] |   
### identity_matrix
Reset the transform matrix to identity (no transformation).
```
identity_matrix();

```

### image_surface_draw
Draw an image into the current surface.
Place an image (typically stored as an Image object) into the current surface. The drawing is placed at the top-left of the drawing context, changeable using a transform matrix or translate function. You can also choose the section of the image to draw using four optional arguments that describe a rectangle taken from the image.
```
image_surface_draw(image: Image, source_rect?: [number, number, number, number]);

```
Name | Type | Description  
---|---|---  
image | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") | to draw  
_optional_ source_rect | [number, number, number, number] | (optional) section of the image to draw  
### in_fill
Determine if a point is within the current path.
Assuming the current path is fillable, tests if the given position is contained in the current path.
```
in_fill(position: [number, number]): 1 | 0;

```
Name | Type | Description  
---|---|---  
position | [number, number] | The position to test  
Return Value | 1 | 0 | 1 if the point is in the path, and 0 otherwise.  
### init
Initialize the mgraphics system.
Initialize the mgraphics system. Call this somewhere in global scope (usually near the top of your JavaScript file) in order to use mgraphics in your custom drawing code.
```
init(): void;

```

### line_to
Add a line segment to the current path.
```
line_to(x: number, y: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the destination point  
y | number | y coordinate of the destination point  
### move_to
Move the current point to a new location.
Move the current point to a new location, and begin a new subpath.
```
move_to(x: number, y: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the new location  
y | number | y coordinate of the new location  
### new_path
Create a new, empty path.
```
new_path();

```

### ovalarc
Add an ellipical arc to the current path.
```
ovalarc(xc: number, yc: number, radiusx: number, radiusy: number, angle1: number, angle2: number);

```
Name | Type | Description  
---|---|---  
xc | number | x coordinate of the center of the arc  
yc | number | y coordinate of the center of the arc  
radiusx | number | horizontal radius of the arc.  
radiusy | number | vertical radius of the arc.  
angle1 | number | start angle for the arc segment in radians  
angle2 | number | end angle for the arc segment in radians  
### path_roundcorners
Round the corners of the current path.
Modify the current path by rounding the corners to the radius provided, or as close as possible depending on the path's angle.
```
path_roundcorners(radius: number);

```
Name | Type | Description  
---|---|---  
radius | number | the radius of the rounded corners  
### pattern_create_for_surface
Create a pattern using an image.
Create a pattern using an image for the background. Repeating patterns depends on the extend value set using the [Pattern.set_extend()](https://docs.cycling74.com/apiref/js/pattern/#set_extend "Pattern.set_extend\(\)") function
```
pattern_create_for_surface(image: Image): Pattern;

```
Name | Type | Description  
---|---|---  
image | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") |   
Return Value | [Pattern](https://docs.cycling74.com/apiref/js/pattern/ "Pattern") |   
### pattern_create_linear
Create a linear gradient.
```
pattern_create_linear(x1: number, y1: number, x2: number, y2: number): Pattern;

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of first color stop  
y1 | number | y coordinate of first color stop  
x2 | number | x coordinate of second color stop  
y2 | number | y coordinate of second color stop  
Return Value | [Pattern](https://docs.cycling74.com/apiref/js/pattern/ "Pattern") |   
### pattern_create_radial
Create a radial gradient.
```
pattern_create_radial(x1: number, y1: number, rad1: number, x2: number, y2: number, rad2: number): Pattern;

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of first color stop  
y1 | number | y coordinate of first color stop  
rad1 | number | radius of first color stop  
x2 | number | x coordinate of second color stop  
y2 | number | y coordinate of second color stop  
rad2 | number | radius of second color stop  
Return Value | [Pattern](https://docs.cycling74.com/apiref/js/pattern/ "Pattern") |   
### pattern_create_rgba
Create a solid color pattern.
```
pattern_create_rgba(red: number, green: number, blue: number, alpha: number): Pattern;

```
Name | Type | Description  
---|---|---  
red | number |   
green | number |   
blue | number |   
alpha | number |   
Return Value | [Pattern](https://docs.cycling74.com/apiref/js/pattern/ "Pattern") |   
### pop_group
Completes a path execution group and returns the result.
Complete a path execution group, returning the results as a [Pattern](https://docs.cycling74.com/apiref/js/pattern/ "Pattern").
```
pop_group(): Pattern;

```
Name | Type | Description  
---|---|---  
Return Value | [Pattern](https://docs.cycling74.com/apiref/js/pattern/ "Pattern") |   
### push_group
Define a starting point for a path execution group.
Define a starting point for a path execution group. This group can be used for creating an image from a set of path functions without actually drawing the results to the screen.
```
push_group();

```

### rectangle_rounded
Add a closed rounded-rectangle to the current path.
```
rectangle_rounded(x: number, y: number, width: number, height: number, ovalwidth: number, ovalheight: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the top-left of the rectangle  
y | number | y coordinate of the top-left of the rectangle  
width | number | width of the rectangle  
height | number | height of the rectangle  
ovalwidth | number | width of the oval used for the rounded corners  
ovalheight | number | height of the oval used for the rounded corners  
### rectangle
Add a closed rectangle to the current path
```
rectangle(x: number, y: number, width: number, height: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the top-left of the rectangle  
y | number | y coordinate of the top-left of the rectangle  
width | number | width of the rectangle  
height | number | height of the rectangle  
### redraw
Request that the current display area be redrawn.
Request that the current display area be redrawn. Max will then call your custom paint() function as part of the next available drawing loop. You should never call your custom paint() function directly.
```
redraw(): void;

```

### rel_curve_to
Add a cubic Bezier spline relative to the current point.
Add a cubic Bezier spline to the current path. The arguments to this function are coordinates relative to the current point.
```
rel_curve_to(x1: number, y1: number, x2: number, y2: number, x3: number, y3: number);

```
Name | Type | Description  
---|---|---  
x1 | number | x coordinate of the first control point  
y1 | number | y coordinate of the first control point  
x2 | number | x coordinate of the second control point  
y2 | number | y coordinate of the second control point  
x3 | number | x coordinate of the destination point  
y3 | number | y coordinate of the destination point  
### rel_line_to
Add a line segment relative to the current point.
Add a line segment to the current path. The arguments to this function are coordinates relative to the current point.
```
rel_line_to(x: number, y: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the destination point  
y | number | y coordinate of the destination point  
### rel_move_to
Move the current point relative to the current point.
Move the current point to a new location, and begin a new subpath. The arguments to this function are relative to the current point.
```
rel_move_to(x: number, y: number);

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the new location  
y | number | y coordinate of the new location  
### restore
Pop the current MGraphics state.
Pop the most recent saved MGraphics state off the stack and apply it. See [MGraphics.save()](https://docs.cycling74.com/apiref/js/mgraphics/#save "MGraphics.save\(\)").
```
restore(): void;

```

### rotate
Adds a rotation to the current transform matrix.
```
rotate(angle: number);

```
Name | Type | Description  
---|---|---  
angle | number | the rotation angle in radians (counter-clockwise)  
### save
Push the current MGraphics state.
Push the current MGraphics state, including stroke and fill color, the current matrix transform, line style, and font style, onto the state stack. After making changes, call [MGraphics.restore()](https://docs.cycling74.com/apiref/js/mgraphics/#restore "MGraphics.restore\(\)") to return to the saved state.
```
save(): void;

```

### scale_source_rgba
Modifies the color transform by adding a scale.
Modifies the color transform by adding a scale. When drawing, MGraphics will multiple the current source color by this scale before drawing. This can be useful if you want to modify the source color in some way without losing the source color. Calling this function again will scale the color further. There is no way to reset the color transform without using [MGraphics.save()](https://docs.cycling74.com/apiref/js/mgraphics/#save "MGraphics.save\(\)") and [MGraphics.restore()](https://docs.cycling74.com/apiref/js/mgraphics/#restore "MGraphics.restore\(\)").
```
scale_source_rgba(sc_red: number, sc_green: number, sc_blue: number, sc_alpha: number);

```
Name | Type | Description  
---|---|---  
sc_red | number | red channel color scaling  
sc_green | number | green channel color scaling  
sc_blue | number | blue channel color scaling  
sc_alpha | number | alpha channel color scaling  
### scale_source_rgba
Modifies the color transform by adding a scale, using an array
```
scale_source_rgba(colors: [number, number, number, number]);

```
Name | Type | Description  
---|---|---  
colors | [number, number, number, number] | Array of [red, green, blue, alpha] scaling values  
### scale
Add a scale to the current transform matrix.
Add a scale to the current transform matrix. This will stretch or squish the drawing horizontally or vertially. Affects line widths.
```
scale(scale_x: number, scale_y: number);

```
Name | Type | Description  
---|---|---  
scale_x | number |   
scale_y | number |   
### select_font_face
Sets the current font face by name
```
select_font_face(fontname: string);

```
Name | Type | Description  
---|---|---  
fontname | string |   
### set_font_size
Set the current font size
Set the current font size. Floating point and integers are both accepted.
```
set_font_size(fontsize: number);

```
Name | Type | Description  
---|---|---  
fontsize | number |   
### set_line_cap
Set the drawing style for the end point of a line.
```
set_line_cap(cap: "butt" | "round" | "square");

```
Name | Type | Description  
---|---|---  
cap | "butt" | "round" | "square" | The desired drawing style  
### set_line_join
Set the appearance of the connection point between lines.
```
set_line_join(join: "miter" | "round" | "bevel");

```
Name | Type | Description  
---|---|---  
join | "miter" | "round" | "bevel" | The desired connection style.  
### set_line_width
Set the current line width.
Set the width of path lines drawn using the [MGraphics.stroke()](https://docs.cycling74.com/apiref/js/mgraphics/#stroke "MGraphics.stroke\(\)") function. The interpretation of this value is dependent on the coordinate system in use, set with [MGraphics.relative_coords](https://docs.cycling74.com/apiref/js/mgraphics/#relative_coords "MGraphics.relative_coords")
```
set_line_width(width: number);

```
Name | Type | Description  
---|---|---  
width | number | Line width  
### set_matrix
Set the current transform matrix directly.
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
### set_matrix
Set the current transform matrix directly, using an array
```
set_matrix(matrix: [number, number, number, number, number, number]);

```
Name | Type | Description  
---|---|---  
matrix | [number, number, number, number, number, number] | Array of [xx, xy, yx, yy, x0, y0] values  
### set_source_rgb
Set the color used for drawing.
Set the color used for drawing, and set the opacity to 1 (fully opaque).
```
set_source_rgb( red: number, green: number, blue: number): void;

```
Name | Type | Description  
---|---|---  
red | number | Red component (0-1)  
green | number | Green component (0-1)  
blue | number | Blue component (0-1)  
### set_source_rgb
Set drawing color using an array
Set the color used for drawing, and set the opacity to 1 (fully opaque).
```
set_source_rgb( colors: [number, number, number]): void;

```
Name | Type | Description  
---|---|---  
colors | [number, number, number] | Array of [red, green, blue] values (0-1)  
### set_source_rgba
Set the color and alpha used for drawing.
Set the color and alpha used for drawing. Values are between 0 and 1.
```
set_source_rgba( red: number, green: number, blue: number, alpha: number): void;

```
Name | Type | Description  
---|---|---  
red | number | Red component (0-1)  
green | number | Green component (0-1)  
blue | number | Blue component (0-1)  
alpha | number | Alpha component (0-1)  
### set_source_rgba
Set drawing color and alpha using an array
Set the color and alpha used for drawing. Values are between 0 and 1.
```
set_source_rgba( colors: [number, number, number, number]): void;

```
Name | Type | Description  
---|---|---  
colors | [number, number, number, number] | Array of [red, green, blue, alpha] values (0-1)  
### set_source_surface
Sets an image to use as a drawing source
```
set_source_surface(image: Image, dx?: number, dy?: number);

```
Name | Type | Description  
---|---|---  
image | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") | to draw  
_optional_ dx | number | translation in x  
_optional_ dy | number | translation in y  
### set_source
Set the source pattern.
Sets the pattern to be used for the next [MGraphics.fill()](https://docs.cycling74.com/apiref/js/mgraphics/#fill "MGraphics.fill\(\)") call.
```
set_source(pattern: Pattern);

```
Name | Type | Description  
---|---|---  
pattern | [Pattern](https://docs.cycling74.com/apiref/js/pattern/ "Pattern") |   
### show_text
Draw text without a path.
Draws the text at the current location, using the current font face and font size. This does not create a path or modify the current path. Matrix transforms will not affect this drawing.
```
show_text(text_to_display: string);

```
Name | Type | Description  
---|---|---  
text_to_display | string | text to draw  
### stroke_preserve_with_alpha
Draw and preserve the outline of the current path with alpha override.
Draw the outline of the current path, but override the alpha value of the current color with a new alpha channel value. This lets you change transparency without resetting the color values. Do not discard the path afterwards.
```
stroke_preserve_with_alpha(alpha: number);

```
Name | Type | Description  
---|---|---  
alpha | number | the opacity between 0 and 1  
### stroke_preserve
Draw and preserve the outline of the current path.
Draw the outline of the current path, using the current settings for color, line width, etc. Do not discard the path afterwards, which can be useful, for example, when you want to draw the stroke and fill with different colors.
```
stroke_preserve();

```

### stroke_with_alpha
Draw the outline of the current path with alpha override.
Draw the outline of the current path, but override the alpha value of the current color with a new alpha channel value. This lets you change transparency without resetting the color values. The path is discarded afterwards.
```
stroke_with_alpha(alpha: number);

```
Name | Type | Description  
---|---|---  
alpha | number | the opacity between 0 and 1  
### stroke
Draw the outline of the current path.
Draw the outline of the current path, using the current settings for color, line width, etc. The path is discarded afterwards.
```
stroke();

```

### svg_render
Render an SVG image.
Draw an SVG image in the current graphics context. The SVG source can be either a filename, or a raw SVG string, or an [MGraphicsSVG](https://docs.cycling74.com/apiref/js/mgraphicssvg/ "MGraphicsSVG") object. Optional x, y, width, and height arguments determine the destination rect into which the SVG will be rendered.
```
svg_render(source: MGraphicsSVG | string, x?: number, y?: number, width?: number, height?: number, opacity?: number);

```
Name | Type | Description  
---|---|---  
source |  [MGraphicsSVG](https://docs.cycling74.com/apiref/js/mgraphicssvg/ "MGraphicsSVG") | string | SVG object, filename, or raw SVG string  
_optional_ x | number | destination origin x coordinate  
_optional_ y | number | destination origin y coordinate  
_optional_ width | number | destination width  
_optional_ height | number | destination height  
_optional_ opacity | number | opacity (0-1)  
### text_measure
Measure the bounds of text
Returns an array contaning the width and height of the given text, as it would appear if rendered in the current font face and font size.
```
text_measure(text: string): [number, number];

```
Name | Type | Description  
---|---|---  
text | string | Text to measure  
Return Value | [number, number] | Text width and height  
### text_path
Create a path from text
Creates a path from the given text, using the current font face and font size. Once the text is in the path, it can be transformed just like an ordinary path.
```
text_path(text_to_display: string);

```
Name | Type | Description  
---|---|---  
text_to_display | string | build a path for this text  
### transform
Modify the current transform matrix by multiplying.
Modify the current transform matrix by multiplying. Useful if you already have a transform matrix that you want to include in the current matrix transform.
```
transform(xx: number, xy: number, yx: number, yy: number, x0: number, y0: number);

```
Name | Type | Description  
---|---|---  
xx | number | x scaling support  
xy | number | rotational warping  
yx | number | rotational warping  
yy | number | y scaling support  
x0 | number | x translation  
y0 | number | y translation  
### transform
Modify the current transform matrix by multiplying, using an array
```
transform(matrix: [number, number, number, number, number, number]);

```
Name | Type | Description  
---|---|---  
matrix | [number, number, number, number, number, number] | Array of [xx, xy, yx, yy, x0, y0] values  
### translate_source_rgba
Modifies the color transform by adding an offset.
Modifies the color transform by adding an offset. When drawing, MGraphics will add this offset to the current source color before drawing. This can be useful if you want to modify the source color in some way without losing the source color. Calling this function again will increase or decrease the color offset. There is no way to reset the color transform without using [MGraphics.save()](https://docs.cycling74.com/apiref/js/mgraphics/#save "MGraphics.save\(\)") and [MGraphics.restore()](https://docs.cycling74.com/apiref/js/mgraphics/#restore "MGraphics.restore\(\)").
```
translate_source_rgba(t_red: number, t_green: number, t_blue: number, t_alpha: number);

```
Name | Type | Description  
---|---|---  
t_red | number | red channel color offset  
t_green | number | green channel color offset  
t_blue | number | blue channel color offset  
t_alpha | number | alpha channel color offset  
### translate_source_rgba
Modifies the color transform by adding an offset, using an array
```
translate_source_rgba(colors: [number, number, number, number]);

```
Name | Type | Description  
---|---|---  
colors | [number, number, number, number] | Array of [red, green, blue, alpha] offset values  
### translate
Adds a translation to the current transform matrix.
```
translate(t_x: number, t_y: number);

```
Name | Type | Description  
---|---|---  
t_x | number | horizontal translation  
t_y | number | vertical translation  
### user_to_device
Convert a user space point to device space.
Convert a point in user space, in which drawing occurs, to device space, the coordinate system after matrix transforms have been applied. If MGraphics were an oil painting, user space would be the position of a point on the canvas, and device space would be where that same point appears in a photograph taken of the painting.
```
user_to_device(position: [number, number]): [number, number];

```
Name | Type | Description  
---|---|---  
position | [number, number] | A two-element array containing the x, y coordinate of a point in user space. *  
Return Value | [number, number] | The equivalent point in device space.
