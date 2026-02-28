---
description: Checking for intersections with paths
group: Custom Drawing with JavaScript
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/03-hit-testing/
title: Hit Testing
---

Download Series Content and Patchers
# Hit Testing
Now that we know how to position paths within our graphics context, it can be useful to figure out how to interact with our custom drawing. For example, we might want the drawing to react in some way when the mouse enters a certain region of our drawing. In general, determining whether a point of interest lies within a given area is called hit testing.
## The hittest Function
Any [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") or [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") can define a function `hittest()` to determine whether or not mouse events should be passed to the object. This can be useful if you know that all of your interaction will happen within a particular region, even if your drawing canvas is always a square. For example, you could use code like this to implement an elliptical button:
```

mgraphics.init();
mgraphics.relative_coords = 0;

let size = [0, 0];
let state = 0;

function hittest(x, y)
{
	// Check if the point is contained in the ellipse
	let radx = size[0] / 2;
	let rady = size[1] / 2;
	let dx = x - (size[0] / 2);
	let dy = y - (size[0] / 2);
	
	let dist_x = dx * dx / (radx * radx);
	let dist_y = dy * dy / (rady * rady);
	
	return (dist_x + dist_y) <= 1 ? 1: 0;
}

function paint()
{	
	size = mgraphics.size;
	let [width, height] = size;
	
	mgraphics.ellipse(0, 0, width, height);
	
	if (state === 0) {
		mgraphics.set_source_rgba(0.1, 0.1, 0.1, 0.5);
	} else if (state === 1) {
		mgraphics.set_source_rgba(0.1, 0.1, 0.1, 0.9);
	} else {
		mgraphics.set_source_rgba(0.9, 0.1, 0.1, 0.9);
	}
	
	mgraphics.fill();
}

function onclick()
{
	state = 2;
	mgraphics.redraw();
}

function ondrag()
{
	state = 2;
	mgraphics.redraw();
}

function onidle()
{
	state = 1;
	mgraphics.redraw();
}

function onidleout()
{
	state = 0;
	mgraphics.redraw();
}

function onresize(w, h)
{
	size = [w, h];
}

```
![](https://docs.cycling74.com/images/5a26a219a9ad17cf6b8eff6abcf30773_873.webp) The hittest function checks if the mouse pointer is inside the ellipse
The `hittest` function is called whenever the mouse pointer is over our custom object. If the function returns a true value, like `1`, then Max will interpret the mouse pointer as having "passed" the hit test, and will forward the mouse event to other event handling functions. Otherwise, the mouse is ignored. This can help simplify a lot of our drawing code. For example, the `onidle` function will only be called if the mouse passes the hit test, meaning that it's within the ellipse. Because of this, we know that we can update the state to `1`, meaning the mouse is over the ellipse, without needing to check again whether the mouse intersects the ellipse. The same logic applies to the `ondrag`, `onclick`, and `onidleout` functions.
## The `in_fill` Function
The MGraphics API also provides a function [in_fill()](https://docs.cycling74.com/apiref/js/mgraphics/#in_fill), which will return `true` if the given point lies within the current path. In this way, we could draw an arbitrarily complex path, and then call `in_fill()` to determine if the mouse pointer were within that path.
```

mgraphics.init();
mgraphics.relative_coords = 0;

let mouse_pos = undefined;

function paint()
{	
	let [width, height] = mgraphics.size;
	
	mgraphics.move_to(0.5 * width, 0);
	mgraphics.line_to(0.85 * width, 1.0 * height);
	mgraphics.line_to(0, 0.35 * height);
	mgraphics.line_to(width, 0.35 * height);
	mgraphics.line_to(0.15 * width, 1.0 * height);
	mgraphics.close_path();
	
	if (!!mouse_pos && mgraphics.in_fill(mouse_pos)) {
		mgraphics.set_source_rgba(0.9, 0.6, 0.2, 1.0);
	} else {
		mgraphics.set_source_rgba(0.9, 0.9, 0.4, 1.0);
	}
	
	mgraphics.fill();
}

function onidle(x, y)
{
	mouse_pos = [x, y];
	mgraphics.redraw();
}

function onidleout()
{
	mouse_pos = undefined;
	mgraphics.redraw();
}

```
![](https://docs.cycling74.com/images/d4239b662f80eefa5c1380066effe7a9_827.webp) The in_fill function compares the mouse pointer with the current path.
Notice that we can't actually call `in_fill` inside the `onidle` function. Instead, we store the last known mouse position in `mouse_pos`, and we call `redraw` to trigger another call to the paint function. The `in_fill` function belongs to the graphics context, which only exists during the call to `paint`.
## The copy_path and append_path Functions
Not only can we hit test with a complex path, we can also hit test against a collection of paths, performing some kind of special function for just those paths that intersect the mouse pointer. The key to this kind of behavior is to use the MGraphics function [copy_path()](https://docs.cycling74.com/apiref/js/mgraphics/#copy_path) to copy and store a given path, and the function [append_path()](https://docs.cycling74.com/apiref/js/mgraphics/#append_path) to add a stored path to the current drawing context.
```
mgraphics.init();
mgraphics.relative_coords = 0;

let paths = [];
let idle_pos = undefined;

function paint()
{	
	if (paths.length === 0) {
		initialize_paths(mgraphics);
	}
	
	paths.forEach((path, idx) => {
		mgraphics.append_path(path);
		mgraphics.set_source_rgba(0.1, 0.1, 0.1, 0.6);
		if (idle_pos !== undefined) {
			if (mgraphics.in_fill(idle_pos)) {
				mgraphics.set_source_rgba(0.9, 0.1, 0.1, 0.9);
			}
		}
		
		mgraphics.fill();
	});
}

function initialize_paths(mgraphics)
{
	let [width, height] = mgraphics.size;
	
	for (let i = 0; i < 250; i++) {
		mgraphics.ellipse(
			width * Math.random(),
			height * Math.random(),
			10 + Math.random() * 40,
			10 + Math.random() * 40
		);
		paths.push(mgraphics.copy_path());
		mgraphics.new_path(); // start from a fresh path next time we call mgraphics.ellipse
	}
}

function onidle(x, y)
{
	idle_pos = [x, y];
	mgraphics.redraw();
}

function onidleout()
{
	idle_pos = undefined;
	mgraphics.redraw();
}

```
![](https://docs.cycling74.com/images/bbb03f44a6ad273ef863dd73fb20def8_469.webp) By storing paths, we can hit test against a list of paths later. 

Kind
    Tutorial 

Author
    Cycling '74 

Contributors
    Sam Tarakajian
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
