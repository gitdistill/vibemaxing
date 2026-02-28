---
description: SVG object handle
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/mgraphicssvg/
title: class MGraphicsSVG
---

# class MGraphicsSVG
SVG object handle
The function [MGraphics.svg_render()](https://docs.cycling74.com/apiref/js/mgraphics/#svg_render "MGraphics.svg_render\(\)") can draw an SVG file directly from a filename. However, drawing from an instance of MGraphicsSVG can be more efficient, since the SVG file does not need to be reloaded. You can also use the functions [MGraphicsSVG.mapcolor()](https://docs.cycling74.com/apiref/js/mgraphicssvg/#mapcolor "MGraphicsSVG.mapcolor\(\)") and [MGraphicsSVG.mapreset()](https://docs.cycling74.com/apiref/js/mgraphicssvg/#mapreset "MGraphicsSVG.mapreset\(\)") to map the colors in the SVG source to a new color, which can be useful to render the same image multiple times with different states.
#### Example
```
// Using an SVG file in Max's search path
var my_svg = new MGraphicsSVG("icon.svg");
var disabled = false;

function paint() {

		my_svg.mapreset();
		if (disabled) {
			my_svg.mapcolor(
				[0, 0, 0, 1.0],
				[0.5, 0.5, 0.5, 1.0]
			)
		}

		mgraphics.svg_render(my_svg);
}

```

## Constructors
```
new MGraphicsSVG(source?: string);

```

Create an SVG object whose colors can be remapped
You can optionally provide a filename or SVG XML string to load an SVG immediately, or create an empty instance and use [MGraphicsSVG.setsvg()](https://docs.cycling74.com/apiref/js/mgraphicssvg/#setsvg "MGraphicsSVG.setsvg\(\)") to load an SVG later. If the argument contains "<svg", "<SVG", or "</", it will be treated as an XML string. Otherwise, it will be treated as a filename.
Parameter | Type | Description  
---|---|---  
_optional_ source | string | (optional) Filename (in Max's search path) or raw SVG XML string  
#### Example 1
```
// Create and load from file
var my_svg = new MGraphicsSVG("icon.svg");

```

#### Example 2
```
// Create and load from XML string
var svg_xml = "<svg><rect width='100' height='100'/></svg>";
var my_svg = new MGraphicsSVG(svg_xml);

```

#### Example 3
```
// Create empty, load later
var my_svg = new MGraphicsSVG();
my_svg.setsvg("icon.svg");

```

## Properties
### loaded number read-only
Whether the SVG has been successfully loaded
This attribute is set to 1 (true) when an SVG is successfully loaded via the constructor or the [MGraphicsSVG.setsvg()](https://docs.cycling74.com/apiref/js/mgraphicssvg/#setsvg "MGraphicsSVG.setsvg\(\)") method, and 0 (false) otherwise.
### size [number, number] read-only
The size of the SVG
The width and height of the SVG as a two-element array. If no SVG is loaded, returns [0, 0].
### viewbox [number, number, number, number] read-only
The viewbox of the SVG
The viewbox of the SVG as a four-element array containing [x, y, width, height]. If no SVG is loaded, returns [0, 0, 0, 0].
## Methods
### mapcolor
Remap source SVG color
Maps a source color in the SVG to a destination color. This allows you to change colors in the SVG without modifying the source file. Multiple color mappings can be added, and they will all be applied when the SVG is rendered. Use [MGraphicsSVG.mapreset()](https://docs.cycling74.com/apiref/js/mgraphicssvg/#mapreset "MGraphicsSVG.mapreset\(\)") to clear all mappings.
```
mapcolor(source_color: [number, number, number, number], map_color: [number, number, number, number]): void;

```
Name | Type | Description  
---|---|---  
source_color | [number, number, number, number] | Origin color in RGBA format [red, green, blue, alpha]  
map_color | [number, number, number, number] | Destination color in RGBA format [red, green, blue, alpha]  
#### Example
```
var my_svg = new MGraphicsSVG("icon.svg");
// Map black to gray
my_svg.mapcolor([0, 0, 0, 1.0], [0.5, 0.5, 0.5, 1.0]);

```

### mapreset
Clear all color remappings
Removes all color mappings that were added via [MGraphicsSVG.mapcolor()](https://docs.cycling74.com/apiref/js/mgraphicssvg/#mapcolor "MGraphicsSVG.mapcolor\(\)"). After calling this method, the SVG will render with its original colors.
```
mapreset(): void;

```

### setsvg
Load an SVG from a file or XML string
Loads an SVG from either a filename (in Max's search path) or from a raw XML string. If the argument contains "<svg", "<SVG", or "</", it will be treated as an XML string. Otherwise, it will be treated as a filename. The [MGraphicsSVG.loaded](https://docs.cycling74.com/apiref/js/mgraphicssvg/#loaded "MGraphicsSVG.loaded") attribute will be updated based on whether the SVG was successfully loaded.
```
setsvg(source: string): number;

```
Name | Type | Description  
---|---|---  
source | string | Filename or raw SVG XML string  
Return Value | number | 1 if the SVG was successfully loaded, 0 otherwise  
#### Example 1
```
var my_svg = new MGraphicsSVG();
var success = my_svg.setsvg("icon.svg");
if (!success) {
    post("Failed to load SVG\n");
}

```

#### Example 2
```
var my_svg = new MGraphicsSVG();
var svg_xml = "<svg><rect width='100' height='100'/></svg>";
my_svg.setsvg(svg_xml);

```

