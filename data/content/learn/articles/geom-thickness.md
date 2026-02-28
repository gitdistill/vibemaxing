---
description: Example of how to extrude triangles to create volumes
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-thickness/
title: Thickness
---

Download Series Content and Patchers
# Extrusion
A very desirable operation to perform on a mesh is diplacing the triangles of which it is composed. Althoug not evident on closed meshes, when displaced, triangles look flat and volumeless. This patch uses a custom geometry script to account for that.
## Let's thicken them up
Open the patch _thickness.maxpat_
![](https://docs.cycling74.com/images/e6d70f4766601373f575ad3441ee807d_320.webp)
This patch takes a Jitter geometry and extrudes the triangles along their vertex normals, forming truncated pyramids of user-defined height. It then performs a random displacement of such extruded triangles to show them in all their glorious thickness.
Let's take a look at the patch:
![](https://docs.cycling74.com/images/93b7fce82e50de5eccdb039fc9353768_589.webp)
The first step consists in grabbing a mesh, turning it into a Jitter geometry, and computing vertex normals using [jit.geom.normgen](https://docs.cycling74.com/reference/jit.geom.normgen "jit.geom.normgen"). Each vertex in the Jitter geometry structure now retains vertex normals.
![](https://docs.cycling74.com/images/31e0afe15ece31a1577d4ccc5783f17b_291.webp)
Then, [jit.geom.todict](https://docs.cycling74.com/reference/jit.geom.todict "jit.geom.todict") converts the Jitter geometry into a dictionary accessible by JavaScript.
Double-click on `v8 geom.thickness.js` to take a look at what the custom geometry script does.
```
// Go through all the faces
faces.forEach(face => {

  // get two halfedges on this face
  let he0 = face.halfedge;
  let he1 = geom.halfedges[he0].next;

  // get the index of the vertices of this face
  let v0 = geom.halfedges[he0].from;
  let v1 = geom.halfedges[he1].from;
  let v2 = geom.halfedges[he1].to;

  // get the vertex normals
  let n0 = geom.vertices[v0].normal;
  let n1 = geom.vertices[v1].normal;
  let n2 = geom.vertices[v2].normal;

  // get the position of the vertices
  let p0 = geom.vertices[v0].point;
  let p1 = geom.vertices[v1].point;
  let p2 = geom.vertices[v2].point;

  // create 3 new positions based on p0, p1, and p2, 
  // shifted by "thickness" along their normal vector
  let pt0 = translate(p0, n0);
  let pt1 = translate(p1, n0);
  let pt2 = translate(p2, n0);

```

The script iterates over the triangles reading the positions and the normal vectors of the 3 vertices. It then computes 3 new positions, shifting each vertex inwards along the direction of their vertex normals.
```
// Push the points into the list
// top face
triangleVertices.push(p0);
triangleVertices.push(p1);
triangleVertices.push(p2);

// bottom face
triangleVertices.push(pt0);
triangleVertices.push(pt1);
triangleVertices.push(pt2);


// side faces
triangleVertices.push(p0);
triangleVertices.push(pt0);
triangleVertices.push(p1);

triangleVertices.push(p1);
triangleVertices.push(pt0);
triangleVertices.push(pt1);

triangleVertices.push(p1);
triangleVertices.push(pt1);
triangleVertices.push(p2);

triangleVertices.push(p2);
triangleVertices.push(pt1);
triangleVertices.push(pt2);

triangleVertices.push(p2);
triangleVertices.push(pt2);
triangleVertices.push(p0);

triangleVertices.push(p0);
triangleVertices.push(pt2);
triangleVertices.push(pt0);

```

It then triangulates the old and the new positions forming a volume.
Now, open the [p animate] subpatch if you want to take a look at how is the mesh dancing.
![](https://docs.cycling74.com/images/98d16101634bc14b68fdd47345785081_489.webp)
The animation is achieved by offsetting the volumes' positions along their face normals using procedural noise provided by [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg"). 

Kind
    Example 

Author
    Cycling '74 

Contributors
    Matteo Marson
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
