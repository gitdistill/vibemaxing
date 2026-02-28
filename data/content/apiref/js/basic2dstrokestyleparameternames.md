---
description: Stroke parameters for use withSketch.beginstroke()in the "basic2d" drawing style
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/basic2dstrokestyleparameternames/
title: enum Basic2dStrokeStyleParameterNames
---

# enum Basic2dStrokeStyleParameterNames
Stroke parameters for use with [Sketch.beginstroke()](https://docs.cycling74.com/apiref/js/sketch/#beginstroke "Sketch.beginstroke\(\)") in the "basic2d" drawing style
**Members**
Member | Value | Description  
---|---|---  
alpha | `"alpha"` | May vary point to point. Value is specified as an alpha value. Useful if alpha is the only color channel which will vary throughout the path.  
color | `"color"` | May vary point to point. Values are specified as red, green, blue, alpha.  
order | `"order"` | Global for a given path. Value must be interpolation order. Default is 3, or bi-cubic interpolation.  
outcolor | `"outcolor"` | May vary point to point. Outline color. Values are specified as red, green, blue, and alpha values. If no color is specified, then the outline color will be the same as the interior color.  
outline | `"outline"` | Global for a given path. Value is 0 (off) or 1 (on). Default is 1.  
scale | `"scale"` | May vary point to point. Value is specified as an width value. Width of the stroked path.  
slices | `"slices"` | Global for a given path. Number of slices for a curved section. Default is 20.
