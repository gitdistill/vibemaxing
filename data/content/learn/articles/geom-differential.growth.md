---
description: Using Jitter geometry and JavaScript to implement a differential growth algorithm
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-differential.growth/
title: Differential Growth
---

Download Series Content and Patchers
# Differential growth
![](https://docs.cycling74.com/images/1d498c04bdbe38d05243075d78156fdf_600.webp)
Today i'd like to explore how we can implement a differential growth algorithm in Max 9 using Jitter geometry and JavaScript. Before jumping into the code, let's talk for a second about growth algorithms.
In the context of computer graphics, growth algorithms refer to techniques that simulate the natural growth processes of plants, trees, and other organic structures. These algorithms generate realistic models of biological forms by mimicking the patterns and rules that govern their growth in nature.
Differential growth refers to a process in which different parts of a structure grow at different rates, resulting in complex shapes and patterns. This phenomenon is commonly observed in nature, such as in the growth of leaves, shells, coral reefs, and biological tissues. In computer graphics, differential growth algorithms simulate these natural growth processes to create intricate, organic forms.
So, let's see how differential growth algorithms work:
## Algorithm overview
To understand the mechanics of _**differential growth**_ algorithms, let's start considering a 2D example: Let's drop some points on a plane, somewhat arranged in a circle, and let's connect adjacent points through edges:
![](https://docs.cycling74.com/images/ef9088cbbbe6b274be250f043d84da0f_1016.webp)
Growth is about expansion, so if we want to expand this figure we need to apply some forces to the points to make them move. The first force that we must apply is a _**repulsive force**_ : within a certain radius, each point repels the others. Let's make an example.
![](https://docs.cycling74.com/images/15fd7a51132d2f14f072563b924fac26_900.webp)
Let's draw a circle of radius _**r**_ from the center of each point to find the neighboring points (in yellow) that apply a repulsive force on the red one. The yellow arrows are the individual force vectors, and the green one is the sum of the forces. Let's now skip one step ahead and let's apply these forces. Under the repulsive force, the points shift an amount and direction proportional to the force vectors.
![](https://docs.cycling74.com/images/934d342d611a17378119155247fb13bc_900.webp)
You can notice that, due to the repulsive force, some points moved outwards while others moved inwards. So far, so good, but if you think about it, the repulsive force alone can't make the figure grow: if the force is bound within a radius, once the points are far apart from each other of a distance greater than that radius, the figure stops expanding. Here comes into play the next step, that is _**edge splitting**_.
![](https://docs.cycling74.com/images/eedb7d55b22c77631a88a1c703e73adb_900.webp)
If an edge connecting two points is longer than a fixed _**"split length"**_ (the purple segment), a new point is introduced at the middle of the edge, splitting it in half. This new point is like fuel for the growing mechanism, as now points have a new neighbor to push away. Repeating repulsion and point insertion, the figure starts growing:
![](https://docs.cycling74.com/images/3c464ef4c4f4556b124c35a2831c7923_280.webp) image from https://inconvergent.net/generative/differential-line/
In the beginning, we said that points are subjected to some forceS, and, in fact, the _**repulsive force**_ is not the only one. There's another force that tends to keep the points at the same distance from each other. We could define this force with the somewhat inaccurate term of _**spring force**_. Such force can be repulsive or attractive and involves two points connected by an edge.
![](https://docs.cycling74.com/images/ece0dac2ae9490c567771a2d1c26b1df_796.webp)
If the edge length is shorter than half the _**split length**_ , then the force is repulsive and pushes the two points away in opposite directions along the edge; if the edge length is greater than half the _**split length**_ , then the force is attractive and pushes the points towards each other.
The _**repulsive force**_ and the _**spring force**_ combined make the figure grow while maintaining a "rounded" shape. Without the _**spring force**_ , the mesh is likely to degenerate under the pressure of the _**repulsive force**_ alone.
I didn't yet give any formula to chew on, but they'll come later. For now, i'd like to add an extra dimension to our example, and consider the implications of the growth algorithm described above in 3D. In reality, it doesn't change much...if not at all! Every point is now a vertex of a triangle, but the same principles apply to the 3D case as well: each vertex is subjected to a _**repulsive force**_ and a _**spring force**_ that develops along the triangle's edges.
Some things become a bit more complicated, but not more complex, for example, the insertion of a new vertex into the mesh. Consider adding one point to a 2-dimensional geometry structure; you only have to add a new point to the list of points, a new edge to the list of edges, and update the points' and edges' pointers to the corresponding edges and points. In 3D, we have more things to care about; inserting a new point means updating the whole geometry structure for the edges, halfedges, and faces connected to the new vertex.
Another thing that becomes trickier is maintaining a well-structured mesh: if, in the 2D example, splitting the edges and introducing new points doesn't affect the structure of the mesh overall, in 3D, we'll have to take care of keeping a good arrangement of the mesh triangles.
That said, let's see how to turn our beloved duck into a Cronenberg-esque nightmare!
## Implementation
In this section i'll go through the implementation details. Let's start with the initial setup:
Open the patch _differential.growth.maxpat_.
![](https://docs.cycling74.com/images/cbb961f029ae16dae30b7f57b6c04633_1024.webp)
This patch can perform a stepped _**differential growth**_ on a closed mesh.
As you can see, the patch is straightforward, and all the action takes place inside the custom script. So, let's take a look at it -> Double-click on `v8 geom.differential.growth.js`
The script has two input functions:
```
function dictionary(dict){

  // Create a reference to the Max dictionary using the dictionary name
  let d = new Dict(dict);

  // Turn this into a JavaScript object
  let fullGeometryDesc = JSON.parse(d.stringify());

  // Get the first geometry
  geom = fullGeometryDesc.geomlist[0];  

  //initialize forces to [0,0,0]
  initForces();

  //output the mesh
  draw();
}

```

**dictionary()** takes a Max dictionary containing a Jitter geometry and turns it into a JavaScript object; then, the function _**initForce()**_ initializes at [0,0,0] an array of size geom.vertices_size that will contain the forces to apply to the vertices.
```
function initForces(){

  forces = [];
  for(let i = geom.vertices_size - 1; i >= 0; i--) forces.push([0,0,0]);
}

```

When [v8](https://docs.cycling74.com/reference/v8/ "v8") receives a _**bang**_ message, the script performs a growth iteration and outputs the vertex position matrix.
```
function bang(){

  //make it grow!
  grow();

  //output the mesh
  draw();
}

```

Now let's dive into _**grow()**_ , the core function of the script:
```
function grow(){

  findMinMax();
  initGrid(); 
  fillGrid();   

  calcRepulsiveForces();  
  calcSpringForces();
  
  applyForces();

  insertNewVertices();

  remesh();
  smooth();
}

```

Judging by the functions' names, you can identify parts of the algorithm described in the introductory section with a few extra things. The remaining part of the current section has been subdivided into paragraphs to give you an exhaustive and organized explanation of how these functions work.
### _**1) The parameters**_
The growth algorithm is controlled by a few attributes:
![](https://docs.cycling74.com/images/9de7a3af3edae08c040ec2caa631e627_546.webp)
  * _**growth_speed**_ is a factor used to reduce or increase the applied forces easily
  * _**split_len**_ determines the edge length over which a new vertex is inserted into the mesh; it also affects the _**spring force**_ and the search radius for the _**repulsive force**_
  * _**radius_ratio**_ determines the extent of the force radius as a function of _**split_len**_ (radius=radiusratio∗splitlenradius = radiusratio*splitlenradius=radiusratio∗splitlen)
  * _**remesh_enable**_ activates/deactivates re-meshing (see paragraph 7)
  * _**smooth_iterations**_ sets the number of smoothing iterations (see paragraph 7)
  * _**smooth_amt**_ controls the amount of smoothing (see paragraph 7)
  * _**inertia**_ controls the amount of inertia (see paragraph 5)


### _**2) The acceleration structure**_
Let's think about the forces that we have to apply to the mesh, and in particular, let's focus on the _**repulsive force**_. We said that each vertex exerts a repulsive force over the other vertices if the distance separating them is less than a fixed radius; in other words, we should evaluate each vertex against each other vertex to know, at least, if they're close enough to interact. Such an operation is veeeeery slow because for NNN vertices, we have to perform (N2)/2(N^2)/2(N2)/2 distance checks. Is there anything we can do to reduce the problem's complexity?
![](https://docs.cycling74.com/images/1c8d09f2b7ce31970102ae96e1693208_983.webp)
We know that two vertices repel each other only if their relative distance is less than a radius; knowing this, we could create a grid of cellsize=radiuscellsize=radiuscellsize=radius and insert in each cell of the grid the indexes of the vertices living inside it. If we do so, we then have to compute the repulsive force only between the vertices living in neighboring grid cells.
Open the JavaScript file `geom.differential.growth.include.gridfunctions.js`
```
function findMinMax(){

  //initialize meshMin and meshMax
  meshMin = [100000, 100000, 100000];
  meshMax = [-100000, -100000, -100000];

  let p;
  //iterate over the vertices to find the minimum and maximum
  for(let i = geom.vertices_size - 1; i >= 0; i--){

    p = geom.vertices[i].point;

    meshMin[0] = Math.min(meshMin[0], p[0]);
    meshMin[1] = Math.min(meshMin[1], p[1]);
    meshMin[2] = Math.min(meshMin[2], p[2]);
    meshMax[0] = Math.max(meshMax[0], p[0]);
    meshMax[1] = Math.max(meshMax[1], p[1]);
    meshMax[2] = Math.max(meshMax[2], p[2]);
  }

  //compute the extend of the mesh
  shape_size = [  meshMax[0] - meshMin[0], 
                  meshMax[1] - meshMin[1], 
                  meshMax[2] - meshMin[2]];
}

```

The function _**findMinMax()**_ computes the extent of the mesh by iterating through vertices and computing the minimum and maximum vertex positions. The mesh's extent is used to determine the acceleration grid's size.
```
function initGrid(){

  //compute the number of cells in each dimension of the grid
  grid_size = new Array(3);
  grid_size[0] = Math.floor(shape_size[0] / radius);
  grid_size[1] = Math.floor(shape_size[1] / radius);
  grid_size[2] = Math.floor(shape_size[2] / radius);

  //fill the grid with an empty array
  grid = new Array(grid_size[0]);
  for(let x = grid_size[0]-1; x >= 0; x--){
    grid[x] = new Array(grid_size[1]);
    for(let y = grid_size[1]-1; y >= 0; y--){
      grid[x][y] = new Array(grid_size[2]);
      for(let z = grid_size[2]-1; z >= 0; z--){
        grid[x][y][z] = {vertices: []};
      }
    }
  }
}

```

The function _**initGrid()**_ creates and initializes the grid. In theory, one could allocate a grid of arbitrary size, but to save memory and computing power, we make it fit the mesh tightly by computing the number of cells in each dimension as gridsize[n]=floor(shapesize[n]/radius)gridsize[n] = floor(shapesize[n] / radius)gridsize[n]=floor(shapesize[n]/radius). Each cell of the grid is initialized with an empty array.
```
function pos2grid(p){

  //convert the vertex position into a grid position
  p = sub(p, meshMin);
  p = div(p, shape_size);
  p = floor(mul(p, [grid_size[0]-1, grid_size[1]-1, grid_size[2]-1] ));
  return p;
}

function fillGrid(){

  let g;

  //iterate over the vertices
  for(let i = geom.vertices_size - 1; i >= 0; i--){

    //calc grid position
    g = pos2grid(geom.vertices[i].point);

    //push vertex i in this grid cell
    grid[g[0]][g[1]][g[2]].vertices.push(i);
  }
}

```

The function _**fillGrid()**_ iterates over the mesh's vertices and pushes their indexes into the corresponding grid cell.
### _**3) Repulsive force**_
Let's get to the juicy part. As said before, vertices exert a repulsive force on the other vertices closer than _**radius**_. We already prepared an acceleration structure to speed up the process, so let's see how the _**repulsive force**_ computation is implemented:
```
function calcRepulsiveForces(){

  let gx,gy,gz,gtx,gty,gtz,x,y,z;

  //for each cell of the grid
  for(gx = grid_size[0]-1; gx >= 0; gx--){
    for(gy = grid_size[1]-1; gy >= 0; gy--){
      for(gz = grid_size[2]-1; gz >= 0; gz--){


        //explore the neighborood of the grid cell of coordinates [gx][gy][gz]
        for(x = 0; x <= 1; x++){
          gtx = gx + x;
          if(gtx >= grid_size[0]) continue; //skip if outside the grid
          for(y = 0; y <= 1; y++){
            gty = gy + y;
            if(gty >= grid_size[1]) continue; //skip if outside the grid
            for(z = 0; z <= 1; z++){
              gtz = gz + z;
              if(gtz >= grid_size[2]) continue; //skip if outside the grid

              if(gx == gtx && gy == gty && gz == gtz){
                calcRepulsionSameCell(gx,gy,gz);
              } else {
                calcRepulsionDifferentCell(gx,gy,gz,gtx,gty,gtz);
              }
            } 
          }
        }
      }
    }
  }
}

```

First of all, we set up a nester _**for**_ loop to iterate over the grid cells.
```
  //for each cell of the grid
  for(gx = grid_size[0]-1; gx >= 0; gx--){
    for(gy = grid_size[1]-1; gy >= 0; gy--){
      for(gz = grid_size[2]-1; gz >= 0; gz--){

        [...]
      }
    }
  }

```

For each grid cell, we run a new nested cycle to access one of these grid cell neighbors and the cell itself.
```
        //explore the neighborood of the grid cell of coordinates [gx][gy][gz]
        for(x = 0; x <= 1; x++){
          gtx = gx + x;
          if(gtx >= grid_size[0]) continue; //skip if outside the grid
          for(y = 0; y <= 1; y++){
            gty = gy + y;
            if(gty >= grid_size[1]) continue; //skip if outside the grid
            for(z = 0; z <= 1; z++){
              gtz = gz + z;
              if(gtz >= grid_size[2]) continue; //skip if outside the grid

            [...]
            }
          } 
        }

```

This image shows the first few iterations:
![](https://docs.cycling74.com/images/12cc547b2417d3ce8c0b9a367d1c3d5a_597.webp)
  * the red grid cell is the current cell in the iteration (of coordinates gxgxgx, gygygy, gzgzgz), and it's the cell to process.
  * the yellow cells are 7 neighboring cells (of coordinates gtxgtxgtx, gtygtygty, gtzgtzgtz).
  * in green, the cells that have been processed already.
  * the blue cells are the ones still to be processed.


The vertices in the red cell must be tested against the vertices contained in the yellow cells and in itself.
```
              if(gx == 0 gtx && gy == gty && gz == gtz){
                calcRepulsionSameCell(gx,gy,gz);
              } else {
                calcRepulsionDifferentCell(gx,gy,gz,gtx,gty,gtz);
              }

```

The first step is to compute the repulsive interactions between the vertices in the red cell. To do so, we run the function _**calcRepulsionSameCell()**_
```
function calcRepulsionSameCell(gx, gy, gz){

  //declare the variables
  let v0,v1,p0,p1,diff,dist,dist2,dir,force,k,j;

  //for each vertex of the grid cell of coordinates [gx][gy][gz]
  for(k = grid[gx][gy][gz].vertices.length-1; k >= 0; k--){

    //get the vertex index
    v0 = grid[gx][gy][gz].vertices[k];

    //get the vertex position
    p0 = geom.vertices[v0].point;

    //for each other vertex of the grid cell of coordinates [gx][gy][gz]
    for(let j = grid[gx][gy][gz].vertices.length-1; j >= k+1; j--){

      //get the vertex index
      v1 = grid[gx][gy][gz].vertices[j];

      //get the vertex position
      p1 = geom.vertices[v1].point;

      calcDistanceAndSetForces(v0,v1,p0,p1);
    }
  }
}

```

The function iterates over the vertices living in the red cell, and for each possible couple of vertices, it runs the function _**calcDistanceAndSetForces()**_
```
function calcDistanceAndSetForces(v0,v1,p0,p1){

      //compute the squared distance between the two vertices
      diff = sub(p0, p1);
      dist2 = dot(diff, diff);

      //if the squared distance is greater than the squared radius, 
      //skip this vertex
      if(dist2 > radius2) return; 

      //compute the distance
      dist = Math.sqrt(dist2);

      //compute the force direction
      dir = div1(diff, dist);

      //compute the force: force_dir / (p0p1_dist^2)
      force = div1(dir, dist2+0.001);

      //add this force to the forces pushing v0
      forces[v0] = sum(forces[v0], force);

      //add an equal and opposite force to v1
      forces[v1] = sum(forces[v1], mul1(force, -1));

}

```

The function _**calcDistanceAndSetForces()**_ , as the name suggests, computes the distance between the vertices v0v0v0 and v1v1v1. If such distance is less than _**radius**_ , it computes the amount of _**repulsive force**_ to apply on v0v0v0 and v1v1v1.
The force is obtained by normalizing the difference between the position of the two vertices and dividing it by the squared distance separating them. This makes the force stronger when the vertices are close and weaker when they're far apart. In the code, a small offset of 0.0010.0010.001 is added to the squared distance to avoid numerical issues, as we could potentially divide by a value very close to 000.
Remember that every action has an equal and opposite reaction; in other words, if v0v0v0 pushes v1v1v1, v1v1v1 pushes v0v0v0 in the opposite direction. For this reason, the force is applied both on v0v0v0 and v1v1v1 equally, but with flipped signs.
One may ask why we still have to test the distance between two vertices if we managed to put them in a grid of cellsize=radiuscellsize = radiuscellsize=radius; the distance test is still relevant because the grid cells are cubes of side _**radius**_ , so potentially two vertices in the same cell could be separated by a distance greater than radius, as the diagonal of a cell has length=radius∗3length = radius*\sqrt{3}length=radius∗3​.
Note: the distance check is performed on the squared distance against the squared radius; dist>radiusdist > radiusdist>radius is mathematically equivalent to dist2>radius2dist^2 > radius^2dist2>radius2, but in case the two vertices are too far apart to interact, the costly _**sqrt()**_ function is skipped. That's a minor optimization.
Then, we perform a similar computation between the vertices populating the red cell and the neighboring cells (the ones colored yellow).
```
function calcRepulsionDifferentCell(gx, gy, gz, gtx, gty, gtz){

  //declare the variables
  let v0,v1,p0,p1,diff,dist,dist2,dir,force,k,j;

  //for each vertex of the grid cell of coordinates [gx][gy][gz]
  for(k = grid[gx][gy][gz].vertices.length-1; k >= 0; k--){

    //get the vertex index
    v0 = grid[gx][gy][gz].vertices[k];

    //get the vertex position
    p0 = geom.vertices[v0].point;

    //for each vertex of the neighboring cell of coordinates [gtx][gty][gtz]
    for(let j = grid[gtx][gty][gtz].vertices.length-1; j >= 0; j--){

      //get the vertex index
      v1 = grid[gtx][gty][gtz].vertices[j];

      //get the vertex position
      p1 = geom.vertices[v1].point;

      calcDistanceAndSetForces(v0,v1,p0,p1);
    }
  }
}

```

The function _**calcRepulsionDifferentCell()**_ iterates over the vertices in the red cell and couples them with all the vertices in a yellow cell. It then performs the distance check and the _**repulsive force**_ computation just as above.
Once we managed to successfully compute all the _**repulsive forces**_ , we can move on to the next force to compute.
### _**4) Spring force**_
```
function calcSpringForces(){

  //compute the length of half split distance
  let halfSplit_len = split_len*0.5;

  //for each edge in the geometry
  for(let i = geom.edges_size - 1; i >= 0; i--){

    //get the first halfedge of this edge
    let he0 = geom.edges[i].halfedges[0];

    //get the endpoints of the edge
    let v0 = geom.halfedges[he0].from;
    let v1 = geom.halfedges[he0].to;
    let p0 = geom.vertices[v0].point;
    let p1 = geom.vertices[v1].point;

    //compute their distance
    let diff = sub(p0, p1);
    let dist2 = dot(diff, diff);
    let edge_len = Math.sqrt(dist2);

    //compute the direction of this edge
    let edge_dir = div1(diff, edge_len);

    //compute the force: edge_dir / (dist^2)
    let force = div1(edge_dir, dist2+0.001);

    //if the length of the edge is greater than half the split length, make the force attractive
    if(edge_len > halfSplit_len) force = mul1(force, -1);
    
    //apply the force to v0
    forces[v0] = sum( forces[v0], force );

    //and an equal and opposite force to v1
    forces[v1] = sum( forces[v1], mul1(force, -1) );
  }
}

```

The _**spring force**_ is way easier to manage than the _**repulsive force**_ , as there's no acceleration structure involved in the computation. The _**calcSpingForces()**_ function iterates over the edges of the Jitter geometry and computes the _**spring force**_ between the endpoints of the edge.
The computation of the force is exactly like the _**repulsive force**_ with the only difference that when edgelen>splitlen/2edgelen > splitlen/2edgelen>splitlen/2, the sign of the force vector is flipped, turning the force from repulsive to attractive.
```
    //if the length of the edge is greater than half the split length, make the force attractive
    if(edge_len > halfSplit_len) force = mul1(force, -1);

```

### _**5) Applying forces**_
Finally, we computed all the forces to which each vertex is subjected. It's now time to use them to move the vertices. The way forces are applied to the vertices is effortless:
```
function applyForces(){

  //for each vertex
  for(let i = geom.vertices_size - 1; i >= 0; i--){

    //sum to the current vertex position the force, dampened by a fixed 
    //scaling factor (0.00003) and the param growth_speed
    geom.vertices[i].point = sum(geom.vertices[i].point, mul1(forces[i], 0.00003*growth_speed));

    //multiply this force by the inertia factor
    forces[i] = mul1(forces[i], inertia);
  }
}

```

The function _**applyForces()**_ iterates over the vertices and sums to their positions the corresponding force, scaled by a small arbitrary value and the _**growth_speed**_ attribute.
Since our final goal is to simulate a natural behavior, we should consider that bodies with mass tend to conserve their state of motion. For this reason, the forces we just computed aren't discarded at the next growth iteration, but they're used as the initial forces[] state for the next iteration. This creates an inertia of the growing movement. The last line of the function scales the forces by _**inertia**_ , preparing the forces[] array for the next growth iteration.
Once the forces are all applied and the vertices have moved, we can pass to the next step of the algorithm: edge splitting.
### _**6) Edge splitting**_
When the length of an edge is greater than a user-defined _**split length**_ , such edge is split in half, and a new vertex is inserted into the mesh at the midpoint of the edge.
```
function insertNewVertices(){

  //For each edge of the mesh
  for(let i = geom.edges_size - 1; i >= 0; i--){

    //het the first halfedge of this edge
    let he0 = geom.edges[i].halfedges[0];

    //get the edges endpoints
    let v0 = geom.halfedges[he0].from;
    let v1 = geom.halfedges[he0].to;
    let p0 = geom.vertices[v0].point;
    let p1 = geom.vertices[v1].point;

    //calc the edge length
    let diff = sub(p0, p1);
    let edge_len2 = dot(diff, diff);

    //if the edge's length is greater than split length, insert a new vertex on this edge
    if(edge_len2 > split_len2) pushVertex(i);

  }
}

```

The function _**insertNewVertices()**_ iterates over the edges and computes the edge's length. When it's greater than _**split length**_ , the function _**pushVertex()**_ is called:
```
function pushVertex(e0){

  //current state
  let h0 = geom.edges[e0].halfedges[0]
  let h1 = geom.halfedges[h0].next;
  let h2 = geom.halfedges[h1].next;
  let h3 = geom.edges[e0].halfedges[1];
  let h4 = geom.halfedges[h3].next;
  let h5 = geom.halfedges[h4].next;

  let f0 = geom.halfedges[h0].face;
  let f1 = geom.halfedges[h3].face;

  let v0 = geom.halfedges[h0].from;
  let v1 = geom.halfedges[h3].from;
  let v2 = geom.halfedges[h2].from;
  let v3 = geom.halfedges[h5].from;

  //compute the position of the new vertex
  let p0 = geom.vertices[v0].point;
  let p1 = geom.vertices[v1].point;
  let pm = mul1(sum(p0, p1), 0.5);

  //push the new vertex
  let vm = geom.vertices_size++;
  geom.vertices.push({  point: pm,
              halfedges: []
            });

  //add a new element to the force array that's the sum 
  //of the forces of the surrounding vertices
  forces.push([0,0,0]);
  forces[vm] = sum(forces[vm], forces[v0]);
  forces[vm] = sum(forces[vm], forces[v1]);
  forces[vm] = mul1(forces[vm], 0.5);

  
  //push new faces
  let f2 = geom.faces_size++;
  geom.faces.push({halfedge: h5});

  let f3 = geom.faces_size++;
  geom.faces.push({halfedge: h1});

  //update existing faces
  geom.faces[f0].halfedge = h2;
  geom.faces[f1].halfedge = h4;

  //add new halfedges
  let h6 = geom.halfedges_size++;
  geom.halfedges.push({   from: vm,
              to: v2,
              next: h2,
              prev: h0,
              face: f0,
              opposite: h6+1 /*h7*/
            });

  let h7 = geom.halfedges_size++;
  geom.halfedges.push({   from: v2,
              to: vm,
              next: h7+1 /*h8*/,
              prev: h1,
              face: f3,
              opposite: h6
            });

  let h8 = geom.halfedges_size++;
  geom.halfedges.push({   from: vm,
              to: v1,
              next: h1,
              prev: h7,
              face: f3,
              opposite: h3
            });

  let h9 = geom.halfedges_size++;
  geom.halfedges.push({   from: vm,
              to: v3,
              next: h5,
              prev: h4,
              face: f2,
              opposite: h9+1 /*h10*/
            });

  let h10 = geom.halfedges_size++;
  geom.halfedges.push({   from: v3,
              to: vm,
              next: h10+1 /*h11*/,
              prev: h4,
              face: f1,
              opposite: h9
            });

  let h11 = geom.halfedges_size++;
  geom.halfedges.push({   from: vm,
              to: v0,
              next: h4,
              prev: h10,
              face: f1,
              opposite: h0
            });

  //update existing halfedges
  geom.halfedges[h0].from = v0;
  geom.halfedges[h0].to = vm;
  geom.halfedges[h0].next = h6;
  geom.halfedges[h0].prev = h2;
  geom.halfedges[h0].face = f0;
  geom.halfedges[h0].opposite = h11;

  geom.halfedges[h1].from = v1;
  geom.halfedges[h1].to = v2;
  geom.halfedges[h1].next = h7;
  geom.halfedges[h1].prev = h8;
  geom.halfedges[h1].face = f3;

  geom.halfedges[h2].from = v2;
  geom.halfedges[h2].to = v0;
  geom.halfedges[h2].next = h0;
  geom.halfedges[h2].prev = h6;
  geom.halfedges[h2].face = f0;

  geom.halfedges[h3].from = v1;
  geom.halfedges[h3].to = vm;
  geom.halfedges[h3].next = h9;
  geom.halfedges[h3].prev = h5;
  geom.halfedges[h3].face = f2;
  geom.halfedges[h3].opposite = h8;

  geom.halfedges[h4].from = v0;
  geom.halfedges[h4].to = v3;
  geom.halfedges[h4].next = h10;
  geom.halfedges[h4].prev = h11;
  geom.halfedges[h4].face = f1;

  geom.halfedges[h5].from = v3;
  geom.halfedges[h5].to = v1;
  geom.halfedges[h5].next = h3;
  geom.halfedges[h5].prev = h9;
  geom.halfedges[h5].face = f2;

  //add the new edges
  let e1 = geom.edges_size++;
  geom.edges.push({ halfedges: [h8, h3] });

  let e2 = geom.edges_size++;
  geom.edges.push({ halfedges: [h6, h7] });

  let e3 = geom.edges_size++;
  geom.edges.push({ halfedges: [h9, h10] });

  //update edges
  geom.edges[e0].halfedges = [h0, h11];

  //update valences
  geom.vertices[v2].halfedges.push(h7);
  geom.vertices[v3].halfedges.push(h10);
  geom.vertices[vm].halfedges.push(h6);
  geom.vertices[vm].halfedges.push(h11);
  geom.vertices[vm].halfedges.push(h9);
  geom.vertices[vm].halfedges.push(h8);
  
}

```

Now, the function _**pushVertex()**_ may seem pretty long and scary, but in reality, its job is relatively simple: if we want to add a new vertex to the mesh, we must reconstruct a coherent Jitter geometry around the new vertex. This means updating all the parts of the Jitter geometry structure that are connected or somehow related to the new vertex. Take a look at the following image:
![](https://docs.cycling74.com/images/e8e33a129580d1d0df2c2f8093ba3571_1024.webp)
The image shows what is happening: starting from the two triangles on the left, we introduce a new vertex vmvmvm at the middle of edge e0e0e0. To do so, we have to add new elements to the Jitter geometry (vertex: vmvmvm, faces: f2f2f2, f3f3f3, edges: e1e1e1, e2e2e2, e3e3e3, halfedges: h6h6h6, h7h7h7, h8h8h8, h9h9h9, h10h10h10, h11h11h11) and update the rest of the structure (vertex: v0v0v0, v1v1v1, v2v2v2, v3v3v3, faces: f0f0f0, f1f1f1, edge e0e0e0, halfedges: h0h0h0, h1h1h1, h2h2h2, h3h3h3, h4h4h4, h5h5h5).
Moreover, we must add a new element to the forces[] array for the newborn vertex vmvmvm. To do it, we compute the average force of the neighboring vertices v0v0v0 and v1v1v1, which are the endpoints of the original edge e0e0e0:
```
  //add a new element to the force array that's the sum 
  //of the forces of the surrounding vertices
  forces.push([0,0,0]);
  forces[vm] = sum(forces[vm], forces[v0]);
  forces[vm] = sum(forces[vm], forces[v1]);
  forces[vm] = mul1(forces[vm], 0.5);

```

### _**7) Remeshing**_
The mesh can finally grow, and we can add new vertices where needed. The problem is that such new vertices can potentially pop up anywhere in the mesh and ruin the mesh quality. What, mesh quality? By "quality" i don't mean any aesthetic consideration, nor i'm referring to the amount of details that a mesh can have; The mesh quality is something that can be measured and responds to precise criteria. A mesh is considered "good" when it exhibits the following features:
  * equal-length edges
  * equilateral triangles
  * valence close to 6


Since our growth algorithm uses a sort of _**spring force**_ to keep the vertices at the same distance from each other, we know for sure that the first criterion is met; the same applies to the second criterion as equal-length edges form equilateral triangles. Regarding the last, we don't have any assurance.
But first of all, what is the _**valence**_? It is simply the number of edges connected to a vertex. A "sane" mesh has a valence of 6 for the internal vertices and 4 for vertices at the edge. The image below shows a "bad" and a "good" mesh, reporting the _**valence**_ of each vertex:
![](https://docs.cycling74.com/images/9e80fd514a96b32fa4ad628d18c4cdb0_1024.webp)
What can we do then to improve the mesh quality? We can perform an edge flip where needed.
Edge flipping consists of taking two adjacent triangles and flipping the internal edge by swapping the vertices it connects. This can improve or worsen the mesh mean valence, so we don't perform it on every edge but only where it's worth it.
```
function remesh(){

  //if remesh is disabled, return
  if(remesh_enable == 0) return; 

  //declare the variables
  let flipValence, noFlipValence, tv, h0,h3,h1,h4,v0,v1,v2,v3;

  //for each edge of the mesh
  for(let e0 = geom.edges_size - 1; e0 >= 0; e0--){

    //get the halfedges of this edge
    h0 = geom.edges[e0].halfedges[0];
    h3 = geom.edges[e0].halfedges[1];
    h1 = geom.halfedges[h0].next;
    h4 = geom.halfedges[h3].next;

    //get the endpoints of this edge and the opposite vertices
    v0 = geom.halfedges[h0].from;
    v1 = geom.halfedges[h4].to;
    v2 = geom.halfedges[h3].from;
    v3 = geom.halfedges[h1].to;

    //calc if it's worth to flip this edge
    tv = geom.vertices[v0].halfedges.length - 6; 
    noFlipValence = tv*tv;
    tv = geom.vertices[v1].halfedges.length - 6; 
    noFlipValence += tv*tv;
    tv = geom.vertices[v2].halfedges.length - 6;
    noFlipValence += tv*tv;
    tv = geom.vertices[v3].halfedges.length - 6;
    noFlipValence += tv*tv;

    tv = geom.vertices[v0].halfedges.length - 7;
    flipValence = tv*tv;
    tv = geom.vertices[v1].halfedges.length - 5;
    flipValence += tv*tv;
    tv = geom.vertices[v2].halfedges.length - 7;
    flipValence += tv*tv;
    tv = geom.vertices[v3].halfedges.length - 5;
    flipValence += tv*tv;

    //if the valence improves (gets closer to 6)
    if(flipValence < noFlipValence){

      //get the rest of the geometry
      let h2 = geom.halfedges[h1].next;
      let h5 = geom.halfedges[h4].next;
      let f0 = geom.halfedges[h0].face;
      let f1 = geom.halfedges[h3].face;

      //and flip this edge
      flipEdge(e0, h0, h1, h2, h3, h4, h5, v0, v1, v2, v3, f0, f1);
    } 
  }
}

```

The function _**remesh()**_ iterates over the edges of the mesh and calculates if it's worth to flip this edge or not. The benefit of flipping this edge is computed comparing the squared mean valence of the no-flip scenario against the flip route.
```
    //calc if it's worth to flip this edge
    tv = geom.vertices[v0].halfedges.length - 6; 
    noFlipValence = tv*tv;
    tv = geom.vertices[v1].halfedges.length - 6; 
    noFlipValence += tv*tv;
    tv = geom.vertices[v2].halfedges.length - 6;
    noFlipValence += tv*tv;
    tv = geom.vertices[v3].halfedges.length - 6;
    noFlipValence += tv*tv;

    tv = geom.vertices[v0].halfedges.length - 7;
    flipValence = tv*tv;
    tv = geom.vertices[v1].halfedges.length - 5;
    flipValence += tv*tv;
    tv = geom.vertices[v2].halfedges.length - 7;
    flipValence += tv*tv;
    tv = geom.vertices[v3].halfedges.length - 5;
    flipValence += tv*tv;

```

if the mean valence improves, then flip this edge:
```
    //if the valence improves (gets closer to 6)
    if(flipValence < noFlipValence){

      //get the rest of the geometry
      let h2 = geom.halfedges[h1].next;
      let h5 = geom.halfedges[h4].next;
      let f0 = geom.halfedges[h0].face;
      let f1 = geom.halfedges[h3].face;

      //and flip this edge
      flipEdge(e0, h0, h1, h2, h3, h4, h5, v0, v1, v2, v3, f0, f1);
    } 

```

Like we did for pushing a new vertex into the mesh, we can flip an edge by changing the elements of the Jitter geometry structure connected to that edge:
```
function flipEdge(e0, h0, h1, h2, h3, h4, h5, v0, v1, v2, v3, f0, f1){

  //flip the edge by updating the halfedge structure
  geom.halfedges[h0].from = v1; 
  geom.halfedges[h0].to = v3; 
  geom.halfedges[h0].next = h2; 
  geom.halfedges[h0].prev = h4; 
  geom.halfedges[h0].face = f0;

  geom.halfedges[h1].from = v2; 
  geom.halfedges[h1].to = v3; 
  geom.halfedges[h1].next = h3; 
  geom.halfedges[h1].prev = h5; 
  geom.halfedges[h1].face = f1;

  geom.halfedges[h2].from = v3; 
  geom.halfedges[h2].to = v0; 
  geom.halfedges[h2].next = h4; 
  geom.halfedges[h2].prev = h0; 
  geom.halfedges[h2].face = f0;

  geom.halfedges[h3].from = v3; 
  geom.halfedges[h3].to = v1; 
  geom.halfedges[h3].next = h5; 
  geom.halfedges[h3].prev = h1; 
  geom.halfedges[h3].face = f1;

  geom.halfedges[h4].from = v0; 
  geom.halfedges[h4].to = v1; 
  geom.halfedges[h4].next = h0; 
  geom.halfedges[h4].prev = h2; 
  geom.halfedges[h4].face = f0;

  geom.halfedges[h5].from = v1; 
  geom.halfedges[h5].to = v2; 
  geom.halfedges[h5].next = h1; 
  geom.halfedges[h5].prev = h3; 
  geom.halfedges[h5].face = f1;

  geom.faces[f0].halfedge = h0;
  geom.faces[f1].halfedge = h3; 

  //increase the valence of v1 and v3
  geom.vertices[v1].halfedges.push(h0);
  geom.vertices[v3].halfedges.push(h3);

  //decrease the valence of v0 and v2
  geom.vertices[v0].halfedges.splice(geom.vertices[v0].halfedges.indexOf(h0), 1);
  geom.vertices[v2].halfedges.splice(geom.vertices[v2].halfedges.indexOf(h3), 1);

}

```

The function _**flipEdge()**_ re-assigns the elements of the Jitter geometry of the two triangles divided by the edge to flip:
![](https://docs.cycling74.com/images/0bb4beee54a10cbe28a5d9df339322a6_1024.webp)
this is the difference with and without remeshing:
  * without remeshing

![](https://docs.cycling74.com/images/a702362097f63bf7f2422d361a2fe88a_193.webp)
  * with remeshing

![](https://docs.cycling74.com/images/cd9e9bd76343ae4a8c09d4eb448335f1_193.webp)
The growth pattern looks completely different. I decided to leave the possibility to enable and disable remeshing because, although not ideal for the quality of the mesh, the shapes that the mesh could assume without remeshing may be interesting and desirable.
There's still something we can do to improve the structural quality of the mesh; under the pressure of the forces, the vertices are pushed here and there, creating an uneven mesh surface. While this may be desirable, i thought to include a controllable smoothing function to create a sort of "surface tension":
```
function smooth(){

  //if smoothing is disabled, quit
  if(smooth_iterations <= 0) return;
  let newPos;

  //compute mixing factors
  let filterA = smooth_amt;
  let filterB = 1 - filterA;

  //compute "smooth_iterations" of smoothing
  for(let s = 0; s < smooth_iterations; s++){
    
    //prepare an array for the smoothed positions
    newPos = new Array(geom.vertices_size);
    
    //for each vertex
    for(let i = geom.vertices_size - 1; i >= 0; i--){

      //initialize the mean position to [0,0,0]
      let meanPos = [0,0,0];

      //for each halfedge starting from this edge
      for(let n = geom.vertices[i].halfedges.length - 1; n >= 0; n--){

        //get the position of this neighboring vertex
        let h = geom.vertices[i].halfedges[n];
        let v = geom.halfedges[h].to;
        let p = geom.vertices[v].point;

        //add its position to the running mean of the positions
        meanPos = sum(meanPos, p);
      }

      //compute the mean position dividing by the number of neighboring vertices
      newPos[i] = div1(meanPos, geom.vertices[i].halfedges.length);
    }

    //for each vertex
    for(let i = geom.vertices_size - 1; i >= 0; i--){

      //update the position of this vertex blending the smoothed and non-smoothed position
      geom.vertices[i].point = mul1(geom.vertices[i].point, filterB);
      geom.vertices[i].point = sum(geom.vertices[i].point, mul1(newPos[i], filterA));
    }   
  }
}

```

The function _**smooth()**_ iterates over the vertices of the mesh, and, for each vertex, it accesses the neighboring vertices, which are the ones connected to this vertex by an edge. The function then computes the mean position of the neighboring vertices and updates the vertex positions by blending the current vertex position with the mean position of the neighboring vertices. The smoothing is controlled by the _**smooth_iterations**_ attribute, which decides how many iterations of the smoothing algorithm to perform, and by the attribute _**smooth_amt**_ , which determines the blending factor between the current vertex position and the mean position of the surrounding vertices.
The smoothing operation seems to improve the cohesion of the mesh surface.
Next, we just need to triangulate the vertices and output the mesh.
### _**8) Output the mesh**_
The last stage of our algorithm consists of triangulating the vertices and outputting the geometry as a Jitter matrix.
```
function draw(){

  //set the dimension of the output matrix
  mOut.dim = geom.faces_size*3;

  //declare the variables
  let he, v, p;
  let points = new Float32Array(geom.faces_size*9);
  let count = 0;

  //for each face, get the vertices of this face, and push them into the array
  for(let i = geom.faces_size - 1; i >= 0; i--){

    he = geom.faces[i].halfedge;
    v = geom.halfedges[he].from;
    p = geom.vertices[v].point;
    points[count++] = p[0];
    points[count++] = p[1];
    points[count++] = p[2];

    he = geom.halfedges[he].next;
    v = geom.halfedges[he].from;
    p = geom.vertices[v].point;
    points[count++] = p[0];
    points[count++] = p[1];
    points[count++] = p[2];

    v = geom.halfedges[he].to;
    p = geom.vertices[v].point;
    points[count++] = p[0];
    points[count++] = p[1];
    points[count++] = p[2];
  }

  //cooy the array into the matrix
  mOut.copyarraytomatrix(points);

  //output the matrix
  outlet(0, "jit_matrix", mOut.name);
}

```

The function _**draw()**_ iterates over the faces of the mesh and triangulates their vertices by pushing their positions into an array in the right order. The array gets then copied into a Jitter matrix at the end of the _**for**_ loop, and the matrix is then sent out from the script.
## Final thoughts
This concludes the tutorial about implementing a differential growth algorithm using Jitter geometry and JavaScript. Remember that you could take the result of this growth process and turn it into a Jitter geometry again for further manipulation, like subdivision, normals generation, and to create texture coordinates. This is not the only growth algorithm that can be implemented using these tools, and that's not the only way to implement this specific one.
I give you some quick inputs to hopefully tickle your curiosity:
  * what about generating new random vertices instead of waiting for an edge to overcome the _**split_length**_?
  * what if _**radius**_ , _**split_len**_ , and _**halfsplit_len**_ were independent from each other?
  * what if the _**growth_speed**_ wasn't constant but more prominent for the vertices pointing up?
  * what about introducing a flow field made with jit.bfg to affect the growth speed and direction?
  * What about adding a surrounding mesh as a container and computing its repulsive force? Will the grown mesh take the shape of the container?
  * what about introducing an _**age**_ parameter? At each growth iteration, vertices get older and less reactive, but the newborn vertices start at age 0


I hope you can use this patch and this script to explore the fascinating world of growth algorithms. Check out also other growth strategies, such as Lindenmayer Systems, Fractal-Based Growth, Space Colonization Algorithms, Diffusion-Limited Aggregation, and Reaction-Diffusion Systems.
Thanks much for following me to this point, and have a tremendous patching day!
MM 

Kind
    Example 

Author
    Cycling '74 

Contributors
    Matteo Marson
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
