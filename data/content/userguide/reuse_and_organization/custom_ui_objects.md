---
description: How to customize the appearance of Max UI objects, using jspainter to define drawing with JavaScript
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/custom_ui_objects/
title: Custom UI Objects
---

# Custom UI Objects
In addition to creating a completely new object by writing your own [Max External](https://docs.cycling74.com/userguide/externals/), you can also customize the appearance of Max objects using JavaScript. If you want to change the look of an existing user interface object, you can set its `@jspainter` attribute to a JavaScript file with your custom drawing code. If you want to create a UI object with custom behavior, you can use the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object, which combines the [js](https://docs.cycling74.com/reference/js/ "js") object with a context you can draw to. Most custom drawing uses the **MGraphics** API for "painter's canvas" style drawing, and in fact this in the only drawing API available with `@jspainter`. With [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") you can use either **MGraphics** or the older **Sketch** API, which wraps a lower-level OpenGL 2.1 drawing context.
## Customzing Existing UI Objects
To customize the appearance of an existing Max object, set the `@jspainterfile` attribute of that object to a JavaScript file containing JavaScript drawing code.
![](https://docs.cycling74.com/images/0a729d5c386ffea864d329a47a13722b_373.webp)
In that JavaScript file, you must implement the `paint` function to define the appearance of the object, where you can use the **MGraphics** API for drawing. A very simple implementation that replaces the existing paint function with a solid color would look like this:
```
function paint() {
  var viewsize = mgraphics.size;
  var width = viewsize[0];
  var height = viewsize[1];
  mgraphics.set_source_rgba(
    box.getattr("bgcolor")
  );
  mgraphics.rectangle(0, 0, width, height);
  mgraphics.fill();
}

```

### Attributes and Value
When using `@jspainterfile`, call `box.getvalueof()` to return the **value** of the parent object. This lets you change your drawing based on the current value of the object, for example changing the length of a slider or the angle of a dial. This will always be an array value, so if the object has a single number as its value, it will be stored in an array of size 1.
```
// Custom drawing for a 'toggle' object
function paint() {
  var val = box.getvalueof(); // this is an array of size 1
  var isToggleOn = val[0] > 0;
  var viewsize = mgraphics.size;
  var width = viewsize[0];
  var height = viewsize[1];

  if (isToggleOn) {
    mgraphics.set_source_rgba(box.getattr("checkedcolor"));
  } else {
    mgraphics.set_source_rgba(box.getattr("uncheckedcolor"));
  }
  mgraphics.rectangle(0, 0, width, height);
  mgraphics.fill();
}

```

### Mapping styles to attributes
Using the `box.attrname_forstylemap()` function, you can retrieve the name of the attribute for a given **Style** element. For a list of valid **Style** element names, check your [**Theme**](https://docs.cycling74.com/userguide/color_themes/). For example, the style element names for the standard Max theme are
```
"bgcolor", "color", "elementcolor", "accentcolor", "selectioncolor", "textcolor", "textcolor_inverse", "patchlinecolor", "clearcolor", "locked_bgcolor", "editing_bgcolor", "stripecolor", "darkcolor", "lightcolor", "bgfillcolor_type", "bgfillcolor_color1", "bgfillcolor_color2", "bgfillcolor_color"

```

This can be useful if you want to look up an object's attribute name based on its function, rather than its internal name. For example, here's generic code for a custom, solid-color toggle, using colors from Max's current theme.
```
// Solid-color toggle, using theme colors
function paint() {
    var val = box.getvalueof(); // this is an array of size 1
    var isToggleOn = val[0] > 0;
    var viewsize = mgraphics.size;
    var width = viewsize[0];
    var height = viewsize[1];

    var onColorName = box.attrname_forstylemap("color");
    var offColorName = box.attrname_forstylemap("elementcolor");
    var oncolor = box.getattr(onColorName);
    var offcolor = box.getattr(offColorName);

    if (isToggleOn) {
      mgraphics.set_source_rgba(oncolor);
    } else {
      mgraphics.set_source_rgba(offcolor);
    }
    mgraphics.rectangle(0, 0, width, height);
    mgraphics.fill();
  }

```

### Calling the original `paint` function
The **mgraphics** API includes a method `parentpaint` that will call the original object's paint method. This lets you draw on top of (or under) the standard interface for the object. For example, here's a way to render a border on top of the standard native object UI using the underlying object's "elementcolor" style color:
```
function paint() {
  var viewsize = mgraphics.size;
  var width = viewsize[0];
  var height = viewsize[1];

  // call original object paint method
  mgraphics.parentpaint();

  // the actual underlying attribute name may be different
  // so we use the attrname_forstylemap() method to map
  // the style color to object attribute name
  var colorname = box.attrname_forstylemap("elementcolor");
  var bordercolor = box.getattr(colorname);

  // draw border rectangle over it
  mgraphics.set_source_rgba(bordercolor);
  mgraphics.rectangle(0.5, 0.5, width - 1, height - 1);
  mgraphics.stroke();
}

```

## The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") Object
Like the [js](https://docs.cycling74.com/reference/js/ "js") object, [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") refers to a separate JavaScript file to define its behavior. In most ways, [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") is the same as a [js](https://docs.cycling74.com/reference/js/ "js") object, except [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") also has a drawing surface that you can use to implement your own custom appearance.
The easiest way to implement custom drawing with [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") is using **mgraphics**. Call `mgraphics.init` somewhere in the global scope of your JavaScript file (typically near or at the top) and then make a `paint` function where you define your custom drawing. Max will call this function when the object needs redrawing, or after you call `mgraphics.redraw()`.
When using [jsui](https://docs.cycling74.com/reference/jsui/ "jsui"), you also have access to the older **Sketch** API. This is really a completely separate drawing model, and while it's possible to use **sketch** at the same time as **mgraphics** , it's not intended. The **Sketch** API currently uses a legacy OpenGL 2.1 context, and so it supports low-level graphics functions, but not a very modern implementation. Unlike MGraphics, with **sketch** you redraw your object manually by calling `refresh()`.
### Event handlers with [jsui](https://docs.cycling74.com/reference/jsui/ "jsui")
The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object can also handle simple UI events, including mouse and resize events. To respond to these events, implement a function with a name like `on<eventname>` where `<eventname>` is the name of the event you want [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") to respond to. For example, to handle a mouse click event:
```
function onclick(x, y) {
  someOtherFunction(x, y);
  mgraphics.redraw();
}

```

The full arguments to any of the mouse events include `x, y, button, mod1, shift, caps, opt, mod2`, which will be the x, y position of the mouse click in the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object, the `phase` of the event, the state of the left modifier key, the state of the shift key, the state of caps lock, the state of the option key, and the state of the right modifier key. You can see full documentation for these functions in the [jsthis JavasScript documentation](https://docs.cycling74.com/apiref/js/jsthis/#onclick) The supported functions are:
```
/**
 * Receives initial click events.
 * @remarks
 * The "button" argument will always be 1.
 */
function onclick(x, y, button, mod1, shift, caps, opt, mod2) { }

```
```
/**
 * Receives double click events.
 * @remarks
 * The "button" argument will always be 1.
 */
function ondblclick(x, y, button, mod1, shift, caps, opt, mod2) { }

```
```
/**
 * Receives drag events.
 * @remarks
 * The "button" argument will be 1 while dragging, and 0 when dragging stops.
 */
function ondrag(x, y, button, mod1, shift, caps, opt, mod2) { }

```
```
/**
 * Receives mouse events over the object.
 * @remarks
 * Equivalent to a "mouse over" event. The "button" argument will always be 0.
 */
function onidle(x, y, button, mod1, shift, caps, opt, mod2) { }

```
```
/**
 * Mouse event as the cursor leaves the object boundaries.
 * @remarks
 * Equivalent to a "mouse out" event. The "button" argument will always be 0.
 */
function onidleout(x, y, button, mod1, shift, caps, opt, mod2) { }

```

There is one more event that will be received when the object resizes.
```
/**
 * Receives the new size of the object in width and height
 */
function onresize(width, height) { }

```

## MGraphics
MGraphics uses a "painter's canvas" drawing model. You call functions that create shapes, paths, text, or other things to draw, and then fill or stroke them to add to the current canvas. Whether you're using MGraphics with [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") or the `@jspainter` attribute, you don't ever draw to the canvas directly. Rather, you implement a `paint` function, which Max will call whenever the object needs to be redrawn. You can also call `mgraphics.redraw()`, which will tell Max to redraw the object as soon as it can. A simple paint function might look like this:
```
// Implement this somewhere in your custom drawing code
function paint() {
  mgraphics.rectangle(-0.2, 0.2, 0.2, -0.2)
  mgraphics.fill()
}

```

### Initialization
In the global scope of your JavaScript file, usually near the top, call `mgraphics.init()` to initialize your object for MGraphics drawing. This is also a good time to configure the MGraphics context globally—you could configure `mgraphics` for [relative coordinates](https://docs.cycling74.com/userguide/custom_ui_objects/#coordinate-system), or tell `mgraphics` not to fill shapes automatically when you use the `stroke()` functions by disabling `autofill`.
```
// Set up the object for mgraphics drawing
mgraphics.init();

// Optionally, configure the global mgraphics instance
mgraphics.relative_coords = 1;
mgraphics.autofill = 0;

```

### Shape Drawing
Whether you're drawing a path, shape, or text, the formula for drawing with MGraphics is more or less the same:
  * Set the colors and properties of the thing you want to draw.
  * Create the path, shape, text, or other thing to draw.
  * Call a function to execute the drawing.


So a drawing routine might look like:
```
function paint() {
  mgraphics.set_source_rgba(0.2, 0.2, 0.2, 1);
  mgraphics.set_line_width(0.03);
  mgraphics.move_to(-1.0, -1.0);
  mgraphics.line_to(1.0, 1.0);
  mgraphics.stroke();
}

```

This drawing function is using the relative coordinate system: the `move_to` call moves to the top-left of the drawing context, and `line_to` draws a line ending in the bottom-right.
### Coordinate System
MGraphics supports two coordinate systems: relative and absolute. With absolute coordinates, the origin `(0, 0)` is the top-left of the canvas, and `(width, height)` would be the bottom-right of the canvas. If your display was `400` by `200`, you could draw an 'X' filling this area with code like this:
```
/**
 * Draw a cross using absolute coordinates. This shape will always be the
 * same size, no matter how the mgraphics context is resized.
 */
function paint() {
  mgraphics.move_to(0, 0) // the top-left
  mgraphics.line_to(400, 200) // the bottom-right
  mgraphics.stroke() // draw it

  mgraphics.move_to(400, 0) // the top-right
  mgraphics.line_to(0, 200) // the bottom-left
  mgraphics.stroke()
}

```

Switch to the relative coordinate system by setting `relative_coords` to `1` on your MGraphics object. After enabling relative coordinates, the origin `(0, 0)` will be at the center of the canvas, the point `(-1, -1)` will be at the top-left, and `(1, 1)` will be at the bottom-right.
```
/**
 * Draw a cross using relative coordinates. This drawing will stretch to
 * fill the full width and height of the drawing context
 */
mgraphics.relative_coords = 1;

function paint() {
  mgraphics.move_to(-1, -1) // the top-left
  mgraphics.line_to(1, 1) // the bottom-right
  mgraphics.stroke() // draw it

  mgraphics.move_to(1, -1) // the top-right
  mgraphics.line_to(-1, 1) // the bottom-left
  mgraphics.stroke()
}

```

## Sketch
JavaScript files loaded by the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object have access to an instance of `Sketch` through the global `sketch` object, which can be used for drawing using the Sketch API. Sketch is an older API than MGraphics, wrapping a legacy OpenGL 2.1 drawing context. It is not the most modern way to implement custom interfaces with [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") or `@jspainterfile`, though it's still available if you need to use the low-level OpenGL functions that the API exposes.
The Sketch API provides high-level functions like `sphere` and `torus`, as well as low-level functions like `glclearcolor`. These lower level functions, all prefixed with `gl`, are thin wrappers around OpenGL functions. You can find the most complete, accurate documentation for these functions by checking the OpenGL documentation.
### Colors and coordinates
Color values are floating point numbers in the range 0. to 1. Color support an alpha channel, with all colors in RGBA format. If an alpha value is not provided, it is assumed to be 1—totally opaque. To disable alpha blending, use `sketch.gldisable("blend")`. If you want to disable depth buffering, which can interfere with alpha blending, use `sketch.gldisable("depth_test")`.
Unlike some graphics APIs, the OpenGL API does not distinguish between 2D and 3D drawing. Conventional 2D drawing is simply a subset of 3D drawing calls with specific graphics state--e.g. no lighting, no depth testing, orthorgraphic projection, et cetera. High level utility methods are provided as a convenience to setup up the OpenGL graphics state to something typically used for 2D or 3D graphics. If assuming 2D drawing conventions, one can ordinarily use z coordinates of zero for all methods that require them.
Coordinates in OpenGL are also given in terms of floating point relative world coordinates, rather than absolute pixel coordinates. The scale of these world coordinates will change depending on the current graphics transformation--i.e. translation, rotation, scaling, projection mode, viewport, etc. However, our default mapping is that Y coordinates are in the range `-1`. to `1` from bottom to top, and X coordinates are in the range `-aspect` to `aspect` from left to right, where `aspect` is equal to the ratio of `width/height`. In the default case, `(0,0)` will be center of your object, `(-aspect,1.)` will be the upper left corner, and `(aspect,-1.)` will be the lower right corner.
User events like mouse clicks will be in absolute screen coordinates. Use `sketch.screentoworld()` and `sketch.worldtoscreen()` to convert between OpenGL world coordinates and screeen coordinates.
### OpenGL conventions and differences
  * Sketch methods are all lowercase, so the OpenGL function `glBegin` is wrapped by the Sketch function `glbegin`.
  * Instead of using symbolic constants like `GL_LIGHTING`, Sketch simply uses lowercase JavaScript strings without the `GL_` prefix. So instead of `GL_LINE_STRIP`, use `"line_strip"` with Sketch.
  * Sketch doesn't have special vector versions of its functions, and only floating point numbers are supported. So `glColorv4fv()` is simply `sketch.glcolor()`.
  * Sketch functions can take arrays as well as individual arguments, so `sketch.glcolor(0.5, 0.5 0.5)` and `sketch.glcolor([0.5, 0.5, 0.5])` are both supported.


## JSPainter vs [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") in Depth
When using `@jspainterfile`, all of the underlying logic of the object is still handled in native Max C code. Your JavaScript drawing function changes how the object appears, but nothing else. Like a standard Max object, message scheduling happens in the high priority scheduler thread, and painting happens in the low priority application thread. The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object has the same limitation as the [js](https://docs.cycling74.com/reference/js/ "js") object: all object logic is executed in the low priority application thread. However, with [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") you're also free to change the object's behavior, just like with the [js](https://docs.cycling74.com/reference/js/ "js") object.
### JSPainter limitations
JSPainter is powerful but has some limitations. While drawing with JSPainter, any use of the **Task** object to support timing information in the UI is not supported. Also, objects with text fields will have some issues. Text may be rendered with standard mgraphics API calls, but as is the case with JSUI, there is no automatic linewrapping, and if the underlying object has a textfield (as do number boxes, message objects, comment objects and the standard text object), there will be conflicts or missing text. For this reason the jspainterfile attribute is hidden for such objects. And finally, there is no support for `@autowatch` or double clicking to open the `jspainterfile` in a text editor.
