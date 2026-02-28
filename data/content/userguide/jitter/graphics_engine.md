---
description: The different graphics engines available in Max, how to change them, and the differences between the two
group: Jitter
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/jitter/graphics_engine/
title: Graphics Engine
---

# Graphics Engine
The **Graphics Engine** manages the interface between Max and the real time graphics API that interacts with your computer's GPU. It's an abstraction layer that translates your instructions about rendering a 3D or 2D scene into hardware instructions that your computer can understand. Operations like positioning virtual objects, calculating light and shadow, running postprocessing effects, and simulating physics interactions are all handled by the graphics engine.
## Changing the Graphics Engine
Under most circumstances, it's not necessary to change the graphics engine. Currently Jitter ships with two engine variants, [legacy OpenGL](https://www.khronos.org/opengl/wiki/Legacy_OpenGL) (`gl2`) and core profile OpenGL (`glcore`). As of Max 8.5 the default graphics engine used by Jitter is `glcore`, which was formerly termed `gl3`. Users needing legacy behavior can set the Graphics Engine preference to `gl2`.
![](https://docs.cycling74.com/images/72e07c9927bc7fa5893c2a157c8652a6_471.webp)
## Engine Comparison
For a full engine comparison, see the [legacy OpenGL](https://www.khronos.org/opengl/wiki/Legacy_OpenGL) discussion. Summarized briefly, the following have been deprecated:
  * Fixed-function vertex and fragment processing, as the rendering pipeline is now fully programmable.
  * Immediate-mode vertex attribute specification and client-side vertex arrays.
  * The GL_QUAD and GL_POLYGON primitive types.
  * Fixed-function lighting, materials and color materials, fixed-function shadow mapping and bump mapping.


