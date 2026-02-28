---
description: The OpenGL Matrix Format
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter99_appendixb/
title: Appendix B
---

Download Series Content and Patchers
# Appendix B: The OpenGL Matrix Format
## Matrices, Video and OpenGL
OpenGL is a standard which specifies a virtual machine for turning lists of numbers into 2D images. The lists may contain the 3D locations of vertices to connect with lines or polygons. They can also contain other data such as coordinates for texture mapping, normals for lighting, colors and edge flags.
Jitter treats video as a type of data which can be processed in its general matrix system. When manipulating video data in Jitter, each cell of a matrix represents one pixel. The four planes of the matrix store the `A, R, G` and `B` components of that pixel. This is Jitter's convention for storing video.
Jitter also has a convention, used by all the objects in the GL group, for storing OpenGL-compatible image descriptions in a matrix. Like video data, these descriptions can be read, processed, and output by various objects. This document specifies Jitter's convention for storing OpenGL data in matrices and the syntax of messages to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object containing these matrices.**When You Need This Reference** Objects in the GL group send out matrices in the format described here when they have their `matrixoutput` attributes set to 1. In order to process these geometries through your own patches, you will need to know this format. If you want to make geometries directly using the [jit.op](https://docs.cycling74.com/reference/jit.op "jit.op") object and other matrix operators, you will also need to know the format. But if Jitter's GL objects are flexible enough for your drawing needs, you can continue to let these objects draw behind the scenes without any knowledge of the OpenGL matrix format.
## GL Matrix Reference
### Message Format
OpenGL data can be passed to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object in Max messages of the forms
### Draw Primitive
The draw primitive specifies how to draw the connections between vertices in the geometry matrix. When a draw primitive is not passed to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object along with the geometry matrix, the current primitive of the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object is used. The current primitive can be changed by sending a message containing just the primitive. When a draw primitive accompanies the geometry matrix, it is used only to draw the given geometry and the current primitive is unchanged. 
The draw primitive can be one of the following symbols:
  * `points` Draws each vertex as a single point. 
  * `lines` Connects eavery other pair of vertices with a line. Given a geometry matrix with vertices A, B, C and D, it draws line segments AB and CD. 
  * `line_strip` Connects each pair of vertices with a line. Given a geometry matrix with vertices A, B, C and D, it draws line segments AB, BC and CD. 
  * `line_loop` Like line_strip but a line segment is drawn connecting the last vertex in the matrix back to the first one. 
  * `triangles` Draws unconnected triangles. Given vertices A B C D E F, draws triangles ABC and DEF. 
  * `tri_strip` Draws a strip of connected triangles. Given vertices A B C D E F, draws triangles ABC, CBD, CDE and EDF. Note the order of the vertices, which is swapped so that all the triangles face the same way (see Tutorial 33: Polygon Modes, Colors and Blending).
  * `tri_fan` Draws a fan of triangles. Given vertices A B C D E F, draws triangles ABC, ACD, ADE and AEF. 
  * `quads` Draws unconnected quadrilaterals. Given vertices A B C D E F G H, draws quadrilaterals ABCD and EFGH. 
  * `quad_strip` Draws connected quadrilaterals. Given vertices A B C D E F, draws quadrilateral ABCD and CDFE. 
  * `polygon` Draws a single polygon using all the vertices in the matrix. If the polygon is not simple and convex, the results are undefined. 
  * `tri_grid` If the geometry matrix has two dimensions, triangles are drawn which link each vertex to its neighbors in the matrix to form a surface. 
  * `quad_grid` If the geometry matrix has two dimensions, quadrilaterals are drawn which link each vertex to its neighbors in the matrix to form a surface. 


### The Connections Matrix
A connections matrix must be one-dimensional and contain either _long_ or _char_ data. If present, it specifies the order in which to connect the vertices in the geometry matrix. By leaving the geometry matrix constant and changing the connections matrix which indexes into it, a changing set of connections between the same vertices can be drawn. 
### The Geometry Matrix
Geometry matrices must contain data in _long_ , _float32_ , or _float64_ format, _float32_ being the most common choice. _Float64_ has more precision than is normally needed for rendering to the screen. The long data type restricts values to integers, which is generally not desired when specifying coordinates. 
Each cell of the matrix represents one vertex. The image is rendered by drawing connections between vertices, either along the rows or the columns of the matrix. A one cell wide matrix will be connected along columns (its only column). A one cell high matrix will be connected along rows. If the matrix is more than one cell in both width and height, the `geom_rows` attribute of the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object determines whether rows or columns will be followed. If the `tri_grid` or `quad_grid` primitives are specified, both the rows and the columns of the matrix are always connected.
Matrices with anywhere from two to 13 planes can be used. Planes 13 and up are reserved for later use and will currently be ignored. Each plane represents a different value in one of five groups: vertices, texture coordinates, normals, vertex color and edges. If enough planes are present to specify a given group, that group is used in rendering the matrix. To be used, each group must be totally present, with the exception of vertices. If only _x_ and _y_ values for vertices are present, the _z_ coordinate of all vertices is set to 0, and an 2D image on the _xy_ plane results.
  * plane 0: _x_ coordinate of vertex
  * plane 1: _y_ coordinate of vertex
  * plane 2: _z_ coordinate of vertex
  * plane 3: _s_ coordinate of texture at vertex, if textured
  * plane 4: _t_ coordinate of texture at vertex, if textured
  * plane 5: _x_ component of lighting normal at vertex
  * plane 6: _y_ component of lighting normal at vertex
  * plane 7: _z_ component of lighting normal at vertex
  * plane 8: red component of vertex color
  * plane 9: green component of vertex color
  * plane 10: blue component of vertex color
  * plane 11: alpha component of vertex color
  * plane 12: edge flag for connection to next vertex: if = 0, no line is drawn.



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
