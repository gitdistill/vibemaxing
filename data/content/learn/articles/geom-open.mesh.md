---
description: How to find the edges at the borders of an open mesh
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-open.mesh/
title: Open Mesh
---

Download Series Content and Patchers
# Open meshes
Meshes can be classified into two categories:
  * _**Open**_ - a surface or 3D shape where some edges are not connected to other faces, leaving gaps or holes in the structure.
  * _**Closed**_ - a 3D shape where all edges are fully connected to adjacent faces, forming a continuous surface with no gaps or holes.


For example, a sphere is a closed mesh, and a disk is an open mesh.
Sometimes, knowing which edges sit on the borders of an open mesh is required to implement geometry processing algorithms. The following is an example of how to identify open borders in a Jitter geometry using custom scripts.
## Open or closed?
Let's fill a Jitter matrix with the vertex coordinates of a triangle, let's turn it into a Jitter geometry with [jit.geom.togeom](https://docs.cycling74.com/reference/jit.geom.togeom "jit.geom.togeom"), and finally, let's convert it to a dictionary with [jit.geom.todict](https://docs.cycling74.com/reference/jit.geom.todict "jit.geom.todict").
![](https://docs.cycling74.com/images/b5a2a04793f8c60ea21a7571a7ee0487_975.webp)
A single triangle is, by definition, an open mesh. If you take a look at the content of the dictionary, there's an entry called "_**closed**_ ", which reports if the Jitter geometry is open or closed.
![](https://docs.cycling74.com/images/4d54fc535723bca69419c9df68d7cc05_846.webp)
As expected, this Jitter geometry is open as _**closed**_ , which is a boolean value [0; 1], says the shape isn't closed. We could imagine such a simple geometry structure as follows:
![](https://docs.cycling74.com/images/d0897756147bfef690db24323fc29e8c_879.webp)
3 vertices (v0v0v0, v1v1v1, v2v2v2) connected by 3 edges (e0e0e0, e1e1e1, e2e2e2), with 3 halfedges pointing from one vertex to the next (h0h0h0, h2h2h2, h4h4h4), and 1 face (f0f0f0). But if you take a closer look at the dictionary, something is not lining up as expected:
![](https://docs.cycling74.com/images/4c7b81bf5b6e9e71e658f2599ae8d97c_844.webp)
The _**halfedges_size**_ reports not 3, but 6 halfedges. That is because of how Jitter geometry deals with open meshes:
In Jitter geometry structures, EVERY halfedge points to an opposite halfedge, even if there's no adjacent face. Let's try to follow the halfedges' pointers in the dictionary:
![](https://docs.cycling74.com/images/0c0076ae7bca26db36dba321567f2d25_270.webp)
The halfedge of index 000 points to an opposite halfedge of index 111. If you look at the face to which halfedge 111 belongs, it reports a face of index −1-1−1. This indicates that halfedge 111, and thus halfedge 000, are at an open end of the mesh.
Note: The dictionary lists the geometry elements as counting from 1, but the geometry structure's pointers count from 0.
The geometry structure of our triangle looks, in fact, like this:
![](https://docs.cycling74.com/images/579cbf0f46a8b9369d2ae93d2ba1b2d1_1024.webp)
All halfedges at the open end of the mesh belong to a face of index −1-1−1. While this may sound complicated at first, it's actually a very effective way of knowing where the mesh's open border is.
## Drawing the open edges of the mesh
Open the patch _geom.draw.borders.maxpat_
![](https://docs.cycling74.com/images/20730b243522456839d90933157a1036_881.webp)
This patch takes a Jitter geometry and draws a line corresponding to the outer edge of an open mesh.
Double-click on `v8 geom.draw.contours.js` to look at the script.
```
function dictionary(dict){

  // Create a reference to the Max dictionary using the dictionary name
  let d = new Dict(dict);

  // Turn this into a JavaScript object
  let fullGeometryDesc = JSON.parse(d.stringify());

  // Get the first geometry
  geom = fullGeometryDesc.geomlist[0];  

  // Quit if the geometry isn't open
  if(geom.closed == 1){
    post("this is not an open geometry!!", "\n");
    return;
  }

  // Initialize an empty array to store the position of the border's vertices
  let outline = [];

  // Iterate through the halfedges
  for(let h = geom.halfedges_size-1; h >= 0; h--){

    // If this halfedge points to an unexisting face
    if(geom.halfedges[h].face == -1){

      // Get its endpoints
      let v0 = geom.halfedges[h].from;
      let v1 = geom.halfedges[h].to;

      // And push them into the array
      outline.push(geom.vertices[v0].point);
      outline.push(geom.vertices[v1].point);
    }
  }

  // Create an empty Jitter matrix 
  let mLines = new JitterMatrix(3, "float32", outline.length);

  // Copy the vertex positions into the matrix
  for(let i = outline.length-1; i >= 0; i--) mLines.setcell(i, "val", outline[i]);

  // Output the Jitter matrix
  outlet(0, "jit_matrix", mLines.name);
}

```

The script receives a dictionary containing the Jitter geometry and turns it into a JavaScript object. It then iterates through the halfedges, and if they point to a face of index −1-1−1, it pushes the endpoints of such a halfedge into an array. Finally, it copies the array with the position of the vertices into a Jitter matrix and outputs it. 

Kind
    Example 

Author
    Cycling '74 

Contributors
    Matteo Marson
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
