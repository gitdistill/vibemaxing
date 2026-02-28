---
description: Manipulating Matrix Data using JavaScript
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter46/
title: Jitter Tutorial 46
---

Download Series Content and Patchers
# Tutorial 46: Manipulating Matrix Data using JavaScript
As we saw in the last tutorial, we can use the Max [js](https://docs.cycling74.com/reference/js/ "js") object to design a pipeline of Jitter objects within procedural JavaScript code. The JitterObject and JitterMatrix objects within JavaScript allow us to create new Jitter objects and matrices and work with them more or less as we would within a Max patcher. In many situations, we need to manipulate data stored in a Jitter matrix in a manner that would be awkward or difficult to do using a Max patcher. This tutorial looks at a variety of solutions for how to manipulate matrix data within [js](https://docs.cycling74.com/reference/js/ "js") using methods and properties of the JitterMatrix object, as well as using the [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") object within JavaScript. This tutorial assumes you've read through the previous _[Tutorial 45:](https://docs.cycling74.com/learn/articles/jitterchapter45/) Introduction to using Jitter within JavaScript_. In addition, this tutorial works with Jitter OpenGL objects as well as [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr"), so you may want to review _[Tutorial 30:](https://docs.cycling74.com/learn/articles/jitterchapter30/) Drawing 3D Text_, _[Tutorial 31:](https://docs.cycling74.com/learn/articles/jitterchapter31/) Rendering Destinations_, and _[Tutorial 39:](https://docs.cycling74.com/learn/articles/jitterchapter39/) Spatial Mapping_ before we begin.
  * Open the tutorial patch.


This tutorial patch uses a [js](https://docs.cycling74.com/reference/js/ "js") object loading a file called _46jParticles.js_. The JavaScript code generates a Jitter matrix in response to a `bang` that we then send to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object in the patcher. The file contains a number of functions to respond to various settings we can send as messages from our patch. 
![Our patcher containing the JavaScript file.](https://docs.cycling74.com/images/fba978f3511305a038012a3f32880509_745.webp) Our patcher containing the JavaScript file.
  * Click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box above the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") object on the left hand side of the patch. Observe the results in the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") named `parts`.


Our JavaScript code generates a set of points that represent a simple _particle system_. A particle system is essentially an algorithm that operates on a (often very large) number of spatial points called _particles_. These particles have rules that determine how they move over time in relation to each other or in relation to other actors within the space. At their basic level, particles contain only their spatial coordinates. Particle systems may also contain other information and can be used to simulate a wide variety of natural processes such as running water or smoke. Particle systems are widely used in computer simulations of our environment, and as such are a staple technology in many computer-generated imagery (CGI) applications. 
![A particle system generated as a Jitter matrix.](https://docs.cycling74.com/images/afa2a11253ea97f1dec438910c44c931_318.webp) A particle system generated as a Jitter matrix.
## The Wide World of Particles
The particle system used in our JavaScript simulation works by generating two sets of random points representing the positions and velocities of the particles and a number of spatial positions in the 3D space that contain gravity. These gravity points, called _attractors_ , act upon the particles in each frame to gradually pull particles towards them. As we can see in the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"), the points in our particle system gradually collapse towards one or more points of singularity. Alternately, the attractor points may be such that the particles oscillate between them, caught in a conflicting gravity field that gradually stabilizes.
  * With the patcher as the frontmost window, press the _spacebar_ on your computer keyboard or click on the [message](https://docs.cycling74.com/reference/message/ "message") box labeled `init` attached to the [js](https://docs.cycling74.com/reference/js/ "js") object. Try this a few times to observe the different behaviors of our particle system.


The `init` message to our [js](https://docs.cycling74.com/reference/js/ "js") object reboots the particle system. It randomly scatters the particles and generates new attractor points. 
![A variety of behaviors from a simple set of rules.](https://docs.cycling74.com/images/63a8b23d08931aee68a1ff800b818bcc_636.webp) A variety of behaviors from a simple set of rules.
  * Click in the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"). A set of colored red, green, and blue axes will appear around the world. Rotate the world with your mouse. Try zooming out (by holding down the ALT/Option key and dragging in the window). Restart the particle system from different vantage points.


A [jit.gl.handle](https://docs.cycling74.com/reference/jit.gl.handle "jit.gl.handle") object controls our [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object, allowing us to see that our particle system inhabits a three-dimensional world. By rotating the space around to different perspectives we can see how the attractors pull in particles from all around them.
## Under the Hood
Now that we've seen a good part of the functionality of the patch (we'll return to it later), let's look at the JavaScript code to see how the algorithm is constructed.
  * Double-click the [js](https://docs.cycling74.com/reference/js/ "js") object in our Tutorial patch. A text editor will appear, containing the source code for the [js](https://docs.cycling74.com/reference/js/ "js") object in the patch. The code is saved as a file called "46jParticles.js" in the same folder as the Tutorial patch.


Our JavaScript code works by manipulating our particles and attractors as Jitter matrices. The particle system is updated by a generation every time our [js](https://docs.cycling74.com/reference/js/ "js") object receives a `bang`. This is accomplished by performing a series of operations on the data in the Jitter matrices. We can take advantage of the Jitter architecture to perform mathematical operations on _entire_ matrices at once since we've encoded our system as matrices. This provides a significant advantage in speed, clarity, and efficiency over working with our data as individual values that must be adjusted one at a time, in many cases (as we would were we to encode our particles as an Array, for example).
Our JavaScript code actually contains three ways of updating our particle system from generation to generation, each of which uses different techniques for manipulating the matrix data representing the particles. We can process the particle system as a single entity using a series of op() methods to the JitterMatrix object, by using a [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") object, or by iterating through the particle system point-by-point (or cell-by-cell). We'll look at each in turn once we investigate the code common to them all. 
  * Look at the global block of code that begins the JavaScript file. 


After the initial comment block and inlet/outlet declarations, we can see a number of variables declared and initialized, including a few JitterObject and JitterMatrix objects. If we examine this code in detail, we can see the outline of how we'll perform our particle system.
```
var PARTICLE_COUNT = 1000; // initial number of particle vertices
var ATTRACTOR_COUNT = 3; // initial number of points of gravity

```

These two global variables (_PARTICLE_COUNT_ and _ATTRACTOR_COUNT_) are used to decide how many particles and how many points of attraction we'd like to work with in our simulation. These will determine the `dim` of the Jitter matrices containing the particle and attractor information.
```
// create a [jit.noise] object for particle and velocity generation
var noisegen = new JitterObject("jit.noise");
noisegen.dim = PARTICLE_COUNT;
noisegen.planecount = 3;
noisegen.type = "float32";

// create a [jit.noise] object for attractor generation
var attgen = new JitterObject("jit.noise");
attgen.dim = ATTRACTOR_COUNT;
attgen.planecount = 3;
attgen.type = "float32";

```

Our particle systems are generated randomly by the init() function, which we will investigate presently. The [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") objects created here as JitterObject objects will perform that function for us, by generating one-dimensional matrices of `float32` values of a size (`dim`) corresponding to the number of particles and attractors specified for our system. The matrices generated by our [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") objects have a `planecount` of `3`, corresponding to x, y, and z spatial data.
```
// create two [jit.expr] objects for the bang_expr() function
// first expression: sum all the planes in the input matrix
var myexpr = new JitterObject("jit.expr");
myexpr.expr = "in[0].p[0]+in[0].p[1]+in[0].p[2]";
// second expression: evaluate a+((b-c)*d/e)
var myexpr2 = new JitterObject("jit.expr");
myexpr2.expr = "in[0]+((in[1]-in[2])*in[3]/in[4])";

```

One of the ways we will update our particle system is to use two [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") objects within our JavaScript code. This part of the code creates the JitterObject objects and defines the mathematical expression to be used by them (the `expr` attribute). We'll step through this when we investigate the code that uses them later on.
```
// create the Jitter matrices we need to store our data
// matrix of x,y,z particle vertices
var particlemat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// matrix of x,y,z particle velocities
var velomat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// matrix of x,y,z points of attraction (gravity centers)
var attmat = new JitterMatrix(3, "float32", ATTRACTOR_COUNT);
// matrix for aggregate distances
var distmat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// temporary matrix for the bang_op() function
var tempmat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// temporary summing matrix for the bang_op() function
var summat = new JitterMatrix(1, "float32", PARTICLE_COUNT);
// another temporary summing matrix for the bang_op() function
var summat2 = new JitterMatrix(1, "float32", PARTICLE_COUNT);
// a scalar matrix to store the current gravity point
var scalarmat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// a scalar matrix to store acceleration (expr_op() function only)
var amat = new JitterMatrix(1, "float32", PARTICLE_COUNT);

```

Our algorithm calls for a number of JitterMatrix objects to store information about our particle system and to be used as intermediate storage during the processing of each generation of the system. The first three matrices (bound to the variables _particlemat_ , _velomat_ , and _attmat_) store the x,y,z positions of our particles, the x,y,z velocities of our particles, and the x,y,z positions of our attractors, respectively. The other six matrices are used in computing each generation of the system.
```
var a = 0.001; // acceleration factor
var d = 0.01; // decay factor

```

These two variables control two important aspects of the behavior of our particle system: the variable _a_ controls how rapidly the particles accelerate toward an attractor, while the variable _d_ controls how much the particles' current velocity decays with each generation. This second variable influences how easy it is for a particle to change direction and be drawn to other attractors.
```
var perform_mode="op"; // default perform function

```

This variable defines which of the three techniques we'll use to process our particle system (the _perform_mode_).
## The Initialization Phase
The first step in creating a particle system is to generate an _initial state_ for the particles and any factors that will act upon them (in our case, the attractor points). For example, were we to attempt to simulate a waterfall, we would start all our particles at the top of the space, with a fixed gravity field at the bottom of the space acting upon the particles with each generation. Our system is slightly less ambitious in terms of real-world accuracy—the particles and attractors will simply be in random positions throughout the 3D scene.
  * Look at the code for the loadbang() and init() functions in the JavaScript code.

```
function loadbang() // execute this code when our Max patch opens
{
  init(); // initialize our matrices
  post("particles initialized.\n");
}

function init()
// initialization routine... call at load, as well as
// when we change the number of particles or attractors
{
  // generate a matrix of random particles spread between -1 and 1
  noisegen.matrixcalc(particlemat, particlemat);
  particlemat.op("*", 2.0);
  particlemat.op("-", 1.0);
  // generate a matrix of random velocities spread between -1 and 1
  noisegen.matrixcalc(velomat, velomat);
  velomat.op("*", 2.0);
  velomat.op("-", 1.0);
  // generate a matrix of random attractors spread between -1 and 1
  attgen.matrixcalc(attmat, attmat);
  attmat.op("*", 2.0);
  attmat.op("-", 1.0);
}

```

The loadbang() function in a [js](https://docs.cycling74.com/reference/js/ "js") object runs whenever the Max patcher containing the [js](https://docs.cycling74.com/reference/js/ "js") file is loaded. This happens _after_ the object is instantiated with the rest of the patch, and is triggered at the same time as messages triggered by [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") and [loadmess](https://docs.cycling74.com/reference/loadmess/ "loadmess") objects in a Max patch would be. Our loadbang() function simply calls the init() function and then prints a friendly message to the Max Console telling us that all is well.
The loadbang() function of JavaScript code only executes when the patcher containing the [js](https://docs.cycling74.com/reference/js/ "js") object is opened. This function does _not_ execute when you change and recompile the JavaScript code. 
Our init() function runs when we open our patch as well as whenever we call it from our Max patcher (through the [message](https://docs.cycling74.com/reference/message/ "message") box triggered by the _spacebar_). The init() function also gets called whenever we change the number of attractors and particles in our simulation. The matrixcalc() method of [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") fills the output matrix (the second argument to the method) with random values between `0` and `1`. This is the same as sending a `bang` to a [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") object in a patcher. In our init() function we fill three matrices with random values in 3 planes. These matrices represent the initial position of our particles (_particlemat,_) the initial velocity of our particles (_velomat,_) and the position of our attractors (_attmat_). Using the op() method to our JitterMatrix objects, we then scale these random values to be between `–1` and `1`. We do this by multiplying the matrix values by `2` and then subtracting `1`.
Now that we have our initial state set up for our particle system, we need to look at how we process the particles with each generation. This is accomplished through one of three different methods in our JavaScript code determined by the _perform_mode_ variable.
  * In the Tutorial patcher, restart the particle system and switch the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object labeled _Perform routine_ from “op” to “expr”. The particle system should continue to behave exactly as before. Switch the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") again to “iter”. The particle system will still run, but very slowly (note the frame rate in the [jit.fpsgui](https://docs.cycling74.com/reference/jit.fpsgui "jit.fpsgui") object attached to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object in the lower left part of the patch). Switch the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") back to “op”.


The [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") changes the value of the _perform_mode_ variable via the mode() function in our JavaScript code. We will look at later in this Tutorial, but it's important to note that one of the methods used (“iter”) runs much more slowly than the other two. This is largely due to the technique used to update the particle system. We"ll look at why this is when we investigate the function that performs that task.
  * Look at the bang() function in the JavaScript code.

```
function bang() // perform one iteration of our particle system
{
  switch(perform_mode) { // choose from the following...
   case "op": // use Jitter matrix operators
      bang_op();
      break;
   case "expr": // use [jit.expr] for the bulk of the algorithm
      bang_expr();
      break;
   case "iter": // iterate cell-by-cell through the matrices
      bang_iter();
      break;
   default: // use bang_op() as our default
      bang_op();
      break;
  }
  // output our new matrix of particle vertices
  outlet(0, "jit_matrix", particlemat.name);
}

```

Our bang() function uses a JavaScript switch() statement to decide what function to call from within it to do the actual processing of our particle system. Depending on the _perform_mode_ we choose in the Max patcher, we select from one of three different functions (bang_op(), bang_expr(), or bang_iter()). Assuming all goes well, we then output the message `jit_matrix`, followed by the `name` of our _particlemat_ matrix (which contains the current coordinates of the simulation"s particles) back into Max.
In the grand tradition of _Choose Your Own Adventure_ and _Let's Make a Deal_ , we'll now investigate the three different perform routines represented by the different functions mentioned above.
## Door #1: The op() route
  * Look at the JavaScript source for the bang_op() function.


Our bang_op() function updates our particle system by using, whenever possible, the op() method to the JitterMatrix object to mathematically alter the contents of matrices _all at once_. Whenever possible, we do this processing _in place_ to limit the number of separate Jitter matrices we need to get through the algorithm. We perform the bulk of the processing multiple times within a for() loop, once for each attractor in our particle system. Once this loop completes, we get an updated version of the velocity matrix (_velomat_), which we then add to the particle matrix (_particlemat_) to define the new positions of the particles.
In a nutshell, we do the following:
```
function bang_op() // create our particle matrix using Matrix operators
{
  for(var i = 0; i < ATTRACTOR_COUNT; i++)
  // do one iteration per gravity point
  {

```

We perform the code until the closing brace (}) once for every attractor, setting the attractor we're currently working on to the variable _i_.
```
// create a scalar matrix out of the current attractor:
scalarmat.setall(attmat.getcell(i));

```

The getcell() method of a JitterMatrix object returns the values of the numbers in the cell specified as its argument. The setall() method sets _all_ the cells of a matrix to a value (or array of values). These methods work the same as the corresponding messages to the [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object in a Max patcher. This line tells our [js](https://docs.cycling74.com/reference/js/ "js") object to copy the current attractors coordinates out of the attractor matrix (_attmat_) and set every single cell in the JitterMatrix _scalarmat_ to those values. The _scalarmat_ matrix has the same `dim` as the _particlemat_ matrix (equal to the number of particles in our system). This allows us to use it as a scalar operand in our op() methods.
```
// subtract our particle positions from the current attractor
// and store in a temporary matrix (x,y,z):
tempmat.op("-", scalarmat, particlemat);

```

This code subtracts our particle positions (_particlemat_) from the position of the attractor we"re currently working with (_scalarmat_). The result is then stored in a temporary matrix with the same `dim` as two used in the op() function. This matrix represents the distances from each particle to the current attractor.
```
// square to create a cartesian distance matrix (x*x, y*y, z*z):
distmat.op("*", tempmat, tempmat);

```

This code multiplies the _tempmat_ matrix _by itself_ , as a simple way of squaring it. The result is then stored in the _distmat_ matrix.
```
// sum the planes of the distance matrix (x*x+y*y+z*z)
summat.planemap = 0;
summat.frommatrix(distmat);
summat2.planemap = 1;
summat2.frommatrix(distmat);
summat.op("+", summat, summat2);
summat2.planemap = 2;
summat2.frommatrix(distmat);
summat.op("+", summat, summat2);

```

In this block of code, we take the separate _planes_ of the _distmat_ matrix and add them together into a single-plane matrix called _summat_. In order to do this, we use the `planemap` property of JitterMatrix to specify which plane of the source matrix to use when copying from using the frommatrix() method. To sum everything we need a second temporary matrix (_summat2_) to help with the operation. First we copy plane `0` of _distmat_ (the squared _x_ distances) into _z_ distances) into _summat2_. We then add _summat_ and _summat2_ again, keeping in mind that _summat_ at this point _already_ contains the sum of the first two planes of _distmat_. The result of this second sum is stored back into _summat_ , which now contains the sum of all three planes of _distmat_.
```
// scale our distances by the acceleration value:
tempmat.op("*", a);
// divide our distances by the sum of the distances
// to derive gravity for this frame:
tempmat.op("/", summat);
// add to the current velocity bearings to get the
// amount of motion for this frame:
velomat.op("+", tempmat);
}

```

This is the last block of code in our per-attractor loop. We multiply the _tempmat_ matrix (which contains the distances of our particles from the current attractor) by the value stored in the variable a, representing acceleration. We then divide that result by the _summat_ matrix (the sum of the squared distances), and add those results to the current velocities of each particle as stored in the _velomat_ matrix. The result of the addition is stored in _velomat_.
This _entire_ process is repeated again for each attractor. As a result, the _velomat_ matrix is added to each time based on how far our particles are from each attractor. By the time the loop finishes (when _i_ reaches the last attractor index), _velomat_ contains a matrix of velocities corresponding to the aggregate pull of all our attractors on all our particles.
```
// offset our current positions by the amount of motion:
   particlemat.op("+", velomat);
   // reduce our velocities by the decay factor for the next frame:
   velomat.op("*", d);
}

```

Finally, we add these velocities to our matrix of particles (_particlemat_ + _velomat_). Our particle matrix is now updated to a new set of particle positions. We then decay the velocity matrix by the amount stored in the variable _d_ , so that the simulation retains a remnant of this generation"s velocity for the next generation of the particle system.
The use of a cascading series of op() methods to perform our algorithm on entire matrices gives us a big advantage in terms for speed, as Jitter can perform a simple mathematical operation on a large set of data very quickly. However, there are a few points (particularly in the generation of the summing matrix _summat_) where the code may have seemed more awkward than necessary. We can use [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") to define a more complex mathematical expression to perform much of this work in a single operation.
## Door #2: The expr() route
  * Back in the global block of our JavaScript file, revisit the code that instantiates the [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") objects.

```
// create two [jit.expr] objects for the bang_expr() function

// first expression: sum all the planes in the input matrix
var myexpr = new JitterObject("jit.expr");
myexpr.expr = "in[0].p[0]+in[0].p[1]+in[0].p[2]";
// second expression: evaluate a+((b-c)*d/e)
var myexpr2 = new JitterObject("jit.expr");
myexpr2.expr = "in[0]+((in[1]-in[2])*in[3]/in[4])";

```

At the beginning of our JavaScript code we created two JitterObject objects (_myexpr_ and _myexpr2_) that instantiated [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") objects. The expression for the first object takes a single matrix (_in[0]_) and sums its planes (the _.p[n]_ notation refers to the data stored in plane _n_ of that matrix). The second expression takes five matrices (_in[0]_ – _in[4]_) and adds the first matrix (_A_) to the result of the second subtracted from the third (_B-C_) multiplied by a fourth (_D_) and divided by a fifth (_E_). Our _myexpr2_ JitterObject therefore evaluates the expression:
A+((B-C)*D/E) 
  * Look at the code for the bang_expr() function. Compare it to what we"ve used in the bang_op() function.


The basic outline of our bang_expr() function is equivalent to the bang_op() function, i.e. we iterate through a loop based on the number of attractors in our simulation, eventually ending up with an aggregate velocity matrix (_velomat_) that we than use to offset our particle matrix (_particlemat_). The key difference lies in where we insert the calls to [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") :
```
function bang_expr() // create our particle matrix using [jit.expr]
{
  // create a scalar matrix out of our acceleration value:
  amat.setall(a);

```

The above line fills every cell in the _amat_ matrix with the value of the variable _a_ (the acceleration factor). This allows us to use it as an operand in one of the [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") expressions later on.
```
for(var i = 0; i < ATTRACTOR_COUNT; i++)
// do one iteration per gravity point
{
   // create a scalar matrix out of the current attractor:
   scalarmat.setall(attmat.getcell(i));
   // subtract our particle positions from the current attractor
   // and store in a temporary matrix (x,y,z):
   tempmat.op("-", scalarmat, particlemat);
   // square to create a cartesian distance matrix (x*x, y*y, z*z):
   distmat.op("*", tempmat, tempmat);

```

This is all the same as in bang_op(). We derive a squared distance matrix based on the difference between the current attractor and our particle positions.
```
// sum the planes of the distance matrix (x*x+y*y+z*z) :
// "in[0].p[0]+in[0].p[1]+in[0].p[2]" :
myexpr.matrixcalc(distmat, summat);

```

Instead of summing the _distmat_ matrix plane-by-plane using op() and frommatrix() methods, we simply evaluate our first mathematical expression using _distmat_ as a 3-plane input matrix and _summat_ as a 1-plane output matrix.
```
// derive amount of motion for this frame :
// "in[0]+((in[1]-in[2])*in[3]/in[4])" :
myexpr2.matrixcalc([velomat,scalarmat,particlemat,amat,summat],velomat);

```

Similarly, at the end of our attractor loop we can derive the velocity matrix _velomat_ in one compound expression based on the previous velocity matrix (_velomat_), the scalar matrix containing the current attractor point (_scalarmat_), the current particle positions (_particlemat_), the scalar matrix containing the acceleration (_amat_), and the matrix containing the distance sums (_summat_). This is much simpler (and a cleaner read) than using a whole sequence of op() functions working with intermediary matrices. Note that we use brackets ([ and ]) to establish an array of input matrices in the matrixcalc() method to the _myexpr2_ object.
```
// offset our current positions by the amount of motion:
   particlemat.op("+", velomat);
   // reduce our velocities by the decay factor for the next frame:
   velomat.op("*", d);
}

```

This is the same as in bang_op(). We generate the new particle positions and decay the new velocities for use as initial velocities in the next generation of the system. 
## Door #3: Cell-by-cell 
  * Look at the code for the bang_iter() function.


The bang_iter() function works in a different way from the other two perform routines we're using in our JavaScript code. Rather than working on the matrices as single entities, we work on everything on a cell-by-cell basis, iterating through not only the matrix of attractor positions (_attmat_), but also through the matrices of particles and velocities. We do this through a pair of nested for() loops, temporarily storing each cell value in different Array objects. We use the getcell() and setcell1d() methods to the JitterMatrix object to retrieve and store values from these Arrays.
```
function bang_iter() // create our particle matrix cell-by-cell
{
  var p_array = new Array(3); // array for a single particle
  var v_array = new Array(3); // array for a single velocity
  var a_array = new Array(3); // array for a single attractor

  for(var j = 0; j < PARTICLE_COUNT; j++)
  // do one iteration per particle
  {
   // fill an array with the current particle:
   p_array = particlemat.getcell(j);
   // fill an array with the current particle's velocity:
   v_array = velomat.getcell(j);

   for(var i = 0; i < ATTRACTOR_COUNT; i++)
   // do one iteration per gravity point
   {
      // fill an array with the current attractor:
      a_array = attmat.getcell(i);

      // find the distance from this particle to the
      // current attractor:
      var distsum = (a_array[0]-p_array[0])*(a_array[0]-p_array[0]);
      distsum+= (a_array[1]-p_array[1])*(a_array[1]-p_array[1]);
      distsum+= (a_array[2]-p_array[2])*(a_array[2]-p_array[2]);

      // derive the amount of motion for this frame:
      v_array[0]+= (a_array[0]-p_array[0])*a/distsum; // x
      v_array[1]+= (a_array[1]-p_array[1])*a/distsum; // y
      v_array[2]+= (a_array[2]-p_array[2])*a/distsum; // z
   }

   // offset our current positions by the amount of motion
   p_array[0]+=v_array[0]; // x
   p_array[1]+=v_array[1]; // y
   p_array[2]+=v_array[2]; // z

   // reduce our velocities by the decay factor for the next frame:
   v_array[0]*=d; // x
   v_array[1]*=d; // y
   v_array[2]*=d; // z

   // set the position for this particle in the Jitter matrix:
   particlemat.setcell1d(j, p_array[0],p_array[1],p_array[2]);
   // set the velocity for this particle in the Jitter matrix:
   velomat.setcell1d(j, v_array[0],v_array[1],v_array[2]);
  }
}

```

Note that by updating our particle system bit-by-bit (and using intermediary Array objects to store data for each cell) we're essentially replicating the same operation, as many times as there are particles in our system! While this may not be noticeably inefficient with a small number of particles, once you begin to work with thousands of points it will become noticeably slower.
## Other functions 
  * Back in the Max patcher, change the [number](https://docs.cycling74.com/reference/number/ "number") box objects attached to the [message](https://docs.cycling74.com/reference/message/ "message") boxes labeled `particles $1`, `attractors $1`, `accel $1`, and `decay $1`. Try setting the number of particles to very large and very small numbers. Try to work out how the `accel` and `decay` attributes alter the responsiveness of the system. Look at the code for these functions in the JavaScript file.


The bulk of these functions simply change variables, sometimes scaling them first (e.g. accel() and decay() simply change the values of _a_ and _d_ , respectively). Similarly, the mode() function changes the value of the _perform_mode_ variable to a string that we use to decide the perform routine:
```
function mode(v) // change perform mode
{
  perform_mode = v;
}

```

The particles() and attractors() functions, however, need to not only change the value of a variable (_PARTICLE_COUNT_ and _ATTRACTOR_COUNT_ , respectively), but they need to change the `dim` of the matrices that depend on those values as well as reboot the particle simulation (by calling the init() function).
```
function particles(v) // change the number of particles we're working with
{
  PARTICLE_COUNT = v;

  // resize matrices
  noisegen.dim = PARTICLE_COUNT;
  particlemat.dim = PARTICLE_COUNT;
  velomat.dim = PARTICLE_COUNT;
  distmat.dim = PARTICLE_COUNT;
  attmat.dim = PARTICLE_COUNT;
  tempmat.dim = PARTICLE_COUNT;
  summat.dim = PARTICLE_COUNT;
  summat2.dim = PARTICLE_COUNT;
  scalarmat.dim = PARTICLE_COUNT;
  amat.dim = PARTICLE_COUNT;

  init(); // re-initialize particle system
}

function attractors(v)
// change the number of gravity points we're working with
{
  ATTRACTOR_COUNT = v;

  // resize attractor matrix
  attgen.dim = ATTRACTOR_COUNT;

  init(); // re-initialize particle system
}

```

  * In the Max patcher, change the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object labeled _Drawing primitive_. Try different settings and notice how it changes the way the particle system is drawn. The primitive() function in our JavaScript code changes the value of the variable _draw_primitive_.


Our particle system is visualized by sending the matrix of particle positions (referred to as _particlemat_ in our JavaScript code) to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object. The matrix contains _3_ planes of _float32_ data, which [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") interprets as x,y,z vertices in a geometry. The _drawing primitive_ , which is set using the `@draw_mode` attribute of the [jit.gl.mesh](https://docs.cycling74.com/reference/jit.gl.mesh "jit.gl.mesh") object, defines the way in which our OpenGL drawing context visualizes the data. 
For more information on the specifics of these drawing primitives and the OpenGL matrix format, consult _[Appendix B:](https://docs.cycling74.com/learn/articles/jitterchapter99_appendixb/) The OpenGL Matrix Format_ or the OpenGL "Redbook". 
![Different ways of visualizing our particles using different drawing primitives.](https://docs.cycling74.com/images/a973b0b22bf964296608f4722e1aae31_1024.webp) Different ways of visualizing our particles using different drawing primitives.
  * Play around with the patch some more, looking at the different ways we can generate and visualize our particles. A wide variety of interesting systems can be created simply by passing unadorned x,y,z values to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object as 3-plane matrices.


## Conclusion 
JavaScript can be a powerful language to use when designing algorithms that manipulate matrix data in Jitter. The ability to perform mathematical operations directly on matrices using a variety of techniques (op() methods, [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") objects, and cell-by-cell iteration) within procedural code lets you take advantage of Jitter as a tool to process large sets of data at once.
In the next tutorial, we"ll look at ways to trigger callback functions in JavaScript based on the actions of JitterObject objects themselves. 
## Code Listing
```
// 46jParticles.js
//
// a 3-D particle generator with simple gravity simulation
// demonstrating different techniques for mathematical
// matrix manipulation using Jitter objects in [js].
//
// rld, 7.05
//

inlets = 1;
outlets = 1;

var PARTICLE_COUNT = 1000; // initial number of particle vertices
var ATTRACTOR_COUNT = 3; // initial number of points of gravity

// create a [jit.noise] object for particle and velocity generation
var noisegen = new JitterObject("jit.noise");
noisegen.dim = PARTICLE_COUNT;
noisegen.planecount = 3;
noisegen.type = "float32";

// create a [jit.noise] object for attractor generation
var attgen = new JitterObject("jit.noise");
attgen.dim = ATTRACTOR_COUNT;
attgen.planecount = 3;
attgen.type = "float32";

// create two [jit.expr] objects for the bang_expr() function

// first expression: sum all the planes in the input matrix
var myexpr = new JitterObject("jit.expr");
myexpr.expr = "in[0].p[0]+in[0].p[1]+in[0].p[2]";
// second expression: evaluate a+((b-c)*d/e)
var myexpr2 = new JitterObject("jit.expr");
myexpr2.expr = "in[0]+((in[1]-in[2])*in[3]/in[4])";

// create the Jitter matrices we need to store our data

// matrix of x,y,z particle vertices
var particlemat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// matrix of x,y,z particle velocities
var velomat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// matrix of x,y,z points of attraction (gravity centers)
var attmat = new JitterMatrix(3, "float32", ATTRACTOR_COUNT);
// matrix for aggregate distances
var distmat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// temporary matrix for the bang_op() function
var tempmat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// temporary summing matrix for the bang_op() function
var summat = new JitterMatrix(1, "float32", PARTICLE_COUNT);
// another temporary summing matrix for the bang_op() function
var summat2 = new JitterMatrix(1, "float32", PARTICLE_COUNT);
// a scalar matrix to store the current gravity point
var scalarmat = new JitterMatrix(3, "float32", PARTICLE_COUNT);
// a scalar matrix to store acceleration (expr_op() function only)
var amat = new JitterMatrix(1, "float32", PARTICLE_COUNT);

var a = 0.001; // acceleration factor
var d = 0.01; // decay factor

var perform_mode=""op";" // default perform function

function loadbang() // execute this code when our Max patch opens
{
  init(); // initialize our matrices
  post("particles initialized.\n");
}

function init()
// initialization routine... call at load, as well as
// when we change the number of particles or attractors
{
  // generate a matrix of random particles spread between -1 and 1
  noisegen.matrixcalc(particlemat, particlemat);
  particlemat.op("*", 2.0);
  particlemat.op("-", 1.0);
  // generate a matrix of random velocities spread between -1 and 1
  noisegen.matrixcalc(velomat, velomat);
  velomat.op("*", 2.0);
  velomat.op("-", 1.0);
  // generate a matrix of random attractors spread between -1 and 1
  attgen.matrixcalc(attmat, attmat);
  attmat.op("*", 2.0);
  attmat.op("-", 1.0);
}

function bang() // perform one iteration of our particle system
{
  switch(perform_mode) { // choose from the following...
   case "op": // use Jitter matrix operators
      bang_op();
      break;
   case "expr": // use [jit.expr] for the bulk of the algorithm
      bang_expr();
      break;
   case "iter": // iterate cell-by-cell through the matrices
      bang_iter();
      break;
   default: // use bang_op() as our default
      bang_op();
      break;
  }

  // output our new matrix of particle vertices
  outlet(0, "jit_matrix", particlemat.name);

}

function bang_op() // create our particle matrix using Matrix operators
{
  for(var i = 0; i < ATTRACTOR_COUNT; i++)
  // do one iteration per gravity point
  {
   // create a scalar matrix out of the current attractor:
   scalarmat.setall(attmat.getcell(i));

   // subtract our particle positions from the current attractor
   // and store in a temporary matrix (x,y,z):
   tempmat.op("-", scalarmat, particlemat);

   // square to create a cartesian distance matrix (x*x, y*y, z*z):
   distmat.op("*", tempmat, tempmat);

   // sum the planes of the distance matrix (x*x+y*y+z*z)
   summat.planemap = 0;
   summat.frommatrix(distmat);
   summat2.planemap = 1;
   summat.frommatrix(distmat);
   summat.op("+", summat, summat2);
   summat2.planemap = 2;
   summat2.frommatrix(distmat);
   summat.op("+", summat, summat2);

   // scale our distances by the acceleration value:
   tempmat.op("*", a);
   // divide our distances by the sum of the distances
   // to derive gravity for this frame:
   tempmat.op("/", summat);
   // add to the current velocity bearings to get the
   // amount of motion for this frame:
   velomat.op("+", tempmat);
  }

   // offset our current positions by the amount of motion:
   particlemat.op("+", velomat);
   // reduce our velocities by the decay factor for the next frame:
   velomat.op("*", d);
}

function bang_expr() // create our particle matrix using [jit.expr]
{
  // create a scalar matrix out of our acceleration value:
  amat.setall(a);

  for(var i = 0; i < ATTRACTOR_COUNT; i++)
  // do one iteration per gravity point
  {
   // create a scalar matrix out of the current attractor:
   scalarmat.setall(attmat.getcell(i));
   // subtract our particle positions from the current attractor
   // and store in a temporary matrix (x,y,z):
   tempmat.op("-", scalarmat, particlemat);
   // square to create a cartesian distance matrix (x*x, y*y, z*z):
   distmat.op("*", tempmat, tempmat);

// sum the planes of the distance matrix (x*x+y*y+z*z) :
// "in[0].p[0]+in[0].p[1]+in[0].p[2]" :
   myexpr.matrixcalc(distmat, summat);

   // derive amount of motion for this frame :
   // "in[0]+((in[1]-in[2])*in[3]/in[4])" :
   myexpr2.matrixcalc([velomat,scalarmat,particlemat,amat,summat],
   velomat);

   // offset our current positions by the amount of motion:
   particlemat.op("+", velomat);
   // reduce our velocities by the decay factor for the next frame:
   velomat.op("*", d);
}

function bang_iter() // create our particle matrix cell-by-cell
{
  var p_array = new Array(3); // array for a single particle
  var v_array = new Array(3); // array for a single velocity
  var a_array = new Array(3); // array for a single attractor

  for(var j = 0; j < PARTICLE_COUNT; j++)
  // do one iteration per particle
  {
   // fill an array with the current particle:
   p_array = particlemat.getcell(j);
   // fill an array with the current particle's velocity:
   v_array = velomat.getcell(j);

   for(var i = 0; i < ATTRACTOR_COUNT; i++)
   // do one iteration per gravity point
   {
      // fill an array with the current attractor:
      a_array = attmat.getcell(i);

      // find the distance from this particle to the
      // current attractor:
      var distsum = (a_array[0]-p_array[0])*(a_array[0]-p_array[0]);
      distsum+= (a_array[1]-p_array[1])*(a_array[1]-p_array[1]);
      distsum+= (a_array[2]-p_array[2])*(a_array[2]-p_array[2]);

      // derive the amount of motion for this frame:
      v_array[0]+= (a_array[0]-p_array[0])*a/distsum; // x
      v_array[1]+= (a_array[1]-p_array[1])*a/distsum; // y
      v_array[2]+= (a_array[2]-p_array[2])*a/distsum; // z
   }

   // offset our current positions by the amount of motion
   p_array[0]+=v_array[0]; // x
   p_array[1]+=v_array[1]; // y
   p_array[2]+=v_array[2]; // z

   // reduce our velocities by the decay factor for the next frame:
   v_array[0]*=d; // x
   v_array[1]*=d; // y
   v_array[2]*=d; // z

   // set the position for this particle in the Jitter matrix:
   particlemat.setcell1d(j, p_array[0],p_array[1],p_array[2]);
   // set the velocity for this particle in the Jitter matrix:
   velomat.setcell1d(j, v_array[0],v_array[1],v_array[2]);
  }
}


function particles(v) // change the number of particles we're working with
{
  PARTICLE_COUNT = v;

  // resize matrices
  noisegen.dim = PARTICLE_COUNT;
  particlemat.dim = PARTICLE_COUNT;
  velomat.dim = PARTICLE_COUNT;
  distmat.dim = PARTICLE_COUNT;
  attmat.dim = PARTICLE_COUNT;
  tempmat.dim = PARTICLE_COUNT;
  summat.dim = PARTICLE_COUNT;
  summat2.dim = PARTICLE_COUNT;
  scalarmat.dim = PARTICLE_COUNT;
  amat.dim = PARTICLE_COUNT;

  init(); // re-initialize particle system
}

function attractors(v)
// change the number of gravity points we're working with
{
  ATTRACTOR_COUNT = v;

  // resize attractor matrix
  attgen.dim = ATTRACTOR_COUNT;

  init(); // re-initialize particle system
}

function accel(v) // set acceleration
{
  a = v*0.001;
}

function decay(v) // set decay
{
  d = v*0.001;
}

function mode(v) // change perform mode
{
  perform_mode = v;
}

function bang() // perform one iteration of our particle system
{
  switch(perform_mode) { // choose from the following...
   case "op": // use Jitter matrix operators
      bang_op();
      break;
   case "expr": // use [jit.expr] for the bulk of the algorithm
      bang_expr();
      break;
   case "iter": // iterate cell-by-cell through the matrices
      bang_iter();
      break;
   default: // use bang_op() as our default
      bang_op();
      break;
  }

  // output our new matrix of particle vertices
  outlet(0, "jit_matrix", particlemat.name);

}

function bang_op() // create our particle matrix using Matrix operators
{
  for(var i = 0; i < ATTRACTOR_COUNT; i++) // do one iteration per gravity point
  {
   scalarmat.setall(attmat.getcell(i)); // create a scalar matrix out of the current attractor

   tempmat.op("-", scalarmat, particlemat); // subtract our particle positions from the current attractor and store in a temporary matrix (x,y,z)

   distmat.op("*", tempmat, tempmat); // square to create our cartesian distance matrix (x*x, y*y, z*z)

   // sum the planes of the distance matrix (x*x+y*y+z*z)
   summat.planemap = 0;
   summat.frommatrix(distmat);
   summat2.planemap = 1;
   summat.frommatrix(distmat);
   summat.op("+", summat, summat2);
   summat2.planemap = 2;
   summat2.frommatrix(distmat);
   summat.op("+", summat, summat2);

   tempmat.op("*", a); // scale our distances by the acceleration value
   tempmat.op("/", summat); // divide our distances by the sum of the distances to derive gravity for this frame
   velomat.op("+", tempmat); // add to the current velocity bearings to get the amount of motion for this frame
  }

   particlemat.op("+", velomat); // offset our current positions by the amount of motion
   velomat.op("*", d); // reduce our velocities by the decay factor for the next frame
}

function bang_expr() // create our particle matrix using [jit.expr]
{
  amat.setall(a); // create a scalar matrix out of our acceleration value

  for(var i = 0; i < ATTRACTOR_COUNT; i++) // do one iteration per gravity point
  {
   scalarmat.setall(attmat.getcell(i)); // create a scalar matrix out of the current attractor

   tempmat.op("-", scalarmat, particlemat); // subtract our particle positions from the current attractor and store in a temporary matrix (x,y,z)

   distmat.op("*", tempmat, tempmat); // square to create our cartesian distance matrix (x*x, y*y, z*z)

   myexpr.matrixcalc(distmat, summat); // sum the planes of the distance matrix (x*x+y*y+z*z) : "in[0].p[0]+in[0].p[1]+in[0].p[2]"

   myexpr2.matrixcalc([velomat,scalarmat,particlemat,amat,summat], velomat); // derive amount of motion for this frame : "in[0]+((in[1]-in[2])*in[3]/in[4])"
  }

   particlemat.op("+", velomat); // offset our current positions by the amount of motion
   velomat.op("*", d); // reduce our velocities by the decay factor for the next frame
}

function bang_iter() // create our particle matrix cell-by-cell
{
  var p_array = new Array(3); // create an array for a single particle (x,y,z)
  var v_array = new Array(3); // create an array for a single velocity (x,y,z)
  var a_array = new Array(3); // create an array for a single attractor (x,y,z)


  for(var j = 0; j < PARTICLE_COUNT; j++) // do one iteration per particle
  {
   p_array = particlemat.getcell(j); // fill an array with the current particle
   v_array = velomat.getcell(j); // fill an array with the current particle's velocity

   for(var i = 0; i < ATTRACTOR_COUNT; i++) // do one iteration per gravity point
   {
      a_array = attmat.getcell(i); // fill an array with the current attractor

      // find the distance from this particle to the current attractor
      var distsum = (a_array[0]-p_array[0])*(a_array[0]-p_array[0]);
      distsum+= (a_array[1]-p_array[1])*(a_array[1]-p_array[1]);
      distsum+= (a_array[2]-p_array[2])*(a_array[2]-p_array[2]);

      v_array[0]+= (a_array[0]-p_array[0])*a/distsum; // derive the amount of motion for this frame (x)
      v_array[1]+= (a_array[1]-p_array[1])*a/distsum; // derive the amount of motion for this frame (y)
      v_array[2]+= (a_array[2]-p_array[2])*a/distsum; // derive the amount of motion for this frame (z)
   }

   p_array[0]+=v_array[0]; // offset our current positions by the amount of motion (x)
   p_array[1]+=v_array[1]; // offset our current positions by the amount of motion (y)
   p_array[2]+=v_array[2]; // offset our current positions by the amount of motion (z)

   v_array[0]*=d; // reduce our velocities by the decay factor for the next frame (x)
   v_array[1]*=d; // reduce our velocities by the decay factor for the next frame (y)
   v_array[2]*=d; // reduce our velocities by the decay factor for the next frame (z)

   particlemat.setcell1d(j, p_array[0],p_array[1],p_array[2]); // set the position for this particle in the Jitter matrix
   velomat.setcell1d(j, v_array[0],v_array[1],v_array[2]); // set the velocity for this particle in the Jitter matrix
  }
}

function particles(v) // change the number of particles we're working with
{
  PARTICLE_COUNT = v;

  // resize matrices
  noisegen.dim = PARTICLE_COUNT;
  particlemat.dim = PARTICLE_COUNT;
  velomat.dim = PARTICLE_COUNT;
  distmat.dim = PARTICLE_COUNT;
  attmat.dim = PARTICLE_COUNT;
  tempmat.dim = PARTICLE_COUNT;
  summat.dim = PARTICLE_COUNT;
  summat2.dim = PARTICLE_COUNT;
  scalarmat.dim = PARTICLE_COUNT;
  amat.dim = PARTICLE_COUNT;

  init(); // re-initialize particle system
}

function attractors(v) // change the number of gravity points we're working with
{
  ATTRACTOR_COUNT = v;

  // resize attractor matrix
  attgen.dim = ATTRACTOR_COUNT;

  init(); // re-initialize particle system
}

function accel(v) // set acceleration
{
  a = v*0.001;
}

function decay(v) // set decay
{
  d = v*0.001;
}

function mode(v) // change perform mode
{
  perform_mode = v;
}

```

## See Also
  * [jit.expr - Evaluate expressions](https://docs.cycling74.com/reference/jit.expr)
  * [jit.gl.handle - Use mouse movement to control position/rotation](https://docs.cycling74.com/reference/jit.gl.handle)
  * [jit.gl.render - Render Open GL](https://docs.cycling74.com/reference/jit.gl.render)
  * [jit.window - Display data in a Window](https://docs.cycling74.com/reference/jit.window)
  * [js - Javascript in Max](https://docs.cycling74.com/reference/js/)
  * [qmetro - Queue-based metronome](https://docs.cycling74.com/reference/qmetro/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
