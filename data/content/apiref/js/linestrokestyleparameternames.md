---
description: Stroke parameters for use withSketch.beginstroke()in the "line" drawing style
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/linestrokestyleparameternames/
title: enum LineStrokeStyleParameterNames
---

# enum LineStrokeStyleParameterNames
Stroke parameters for use with [Sketch.beginstroke()](https://docs.cycling74.com/apiref/js/sketch/#beginstroke "Sketch.beginstroke\(\)") in the "line" drawing style
**Members**
Member | Value | Description  
---|---|---  
alpha | `"alpha"` | May vary point to point. Value is specified as an alpha value. Useful if alpha is the only color channel which will vary throughout the path.  
color | `"color"` | May vary point to point. Values are specified as red, green, blue, alpha.  
order | `"order"` | Global for a given path. Value must be interpolation order. Default is 3, or bi-cubic interpolation.  
slices | `"slices"` | Global for a given path. Number of slices for a curved section. Default is 20.
