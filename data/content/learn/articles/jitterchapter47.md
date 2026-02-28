---
description: Using Jitter Object Callbacks in JavaScript
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter47/
title: Jitter Tutorial 47
---

Download Series Content and Patchers
# Tutorial 47: Using Jitter Object Callbacks in JavaScript
In the last two tutorials, we've looked at some of the possibilities and advantages of using Jitter objects and matrices within JavaScript code. In this tutorial we'll encapsulate an entire Jitter OpenGL patch inside of JavaScript, using many of the techniques we've already seen. Most importantly, however, we'll learn how to "listen" to the _output_ of Jitter objects that have been encapsulated in JavaScript in order to design functions that respond interactively to these objects. A number of Jitter objects (such as [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie"), [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"), and [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window")) output messages from their status (right-hand) outlets in response to processes initiated by the user in a Max patcher. For example, when you read a movie file into [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie"), the object outputs the message `read` followed by the movie's filename and a status number out its status outlet. Similarly, the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") and [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") objects can respond to mouse events in their windows by sending messages out their status outlet. Because Jitter objects instantiated within JavaScript have no inlets and outlets _per se_ , we need to explicitly create an object (called a JitterListener) to catch those messages and call a function (called a _callback function_) in response to them.
This Tutorial assumes you've looked at the earlier JavaScript tutorials, as well as the first OpenGL tutorial _[Tutorial 30:](https://docs.cycling74.com/learn/articles/jitterchapter30/) Drawing 3D Text_.
  * Open the tutorial patch.


The first thing we notice about this tutorial patch is that there is very little in it, in terms of Max objects. Virtually all the work done in the patcher is accomplished inside the [js](https://docs.cycling74.com/reference/js/ "js") object in the patch.
![Our Tutorial patcher: not much to look at.](https://docs.cycling74.com/images/ded69bc586cc9993b660f8be429bf6dd_308.webp) Our Tutorial patcher: not much to look at.
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box labeled _Display_. The [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") object will begin to send `bang` messages into the [js](https://docs.cycling74.com/reference/js/ "js") object, and the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object should fill with a number of shapes (one large sphere and a few dozen small spheres) on a black background.


Our [js](https://docs.cycling74.com/reference/js/ "js") object contains a complete set of Jitter objects performing an OpenGL rendering (including a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object).
  * Move your mouse over the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"). The large sphere will "glue" to your mouse, following you along in the window. As the large sphere touches the smaller spheres, it will "push" them along as if they were solid objects colliding. Try to get a feel for moving the smaller spheres around with the larger one.


Our [js](https://docs.cycling74.com/reference/js/ "js") file not only draws our OpenGL scene, but also handles interactive events from the mouse. This is done through a listening and callback mechanism (called a JitterListener) that we'll learn about in the JavaScript code.
![Pushing the spheres around.](https://docs.cycling74.com/images/55dd36a0e45a978f188ede2df55da7da_320.webp) Pushing the spheres around.
## Creating OpenGL objects in JavaScript
  * Double-click the [js](https://docs.cycling74.com/reference/js/ "js") object in our Tutorial patch. A text editor will appear that contains the source code for the [js](https://docs.cycling74.com/reference/js/ "js") object in the patch. The code is saved as a file called "47jMarbles.js" in the same folder as the Tutorial patch. Look at the global code block at the top of the file.


Our JavaScript code creates all the JitterObject objects we need to render our scene: a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object to display the drawing context, a [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object to perform the rendering, and a number of [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") objects to draw and animate the spheres in the scene. These objects are instantiated in the global block of code at the beginning of the JavaScript file. var OBJECT_COUNT = 32; // number of little spheres 
This line declares a variable (_OBJECT_COUNT_) that determines the number of smaller spheres in our scene.
```
// create a [jit.window] object for our display
// (this is the object we'll listen to):
var mywindow = new JitterObject("jit.window","ListenWindow");
// turn off depth testing... we're using blending instead:
mywindow.depthbuffer = 0;
// turn ON idlemousing... we want to listen for it:
mywindow.idlemouse = 1;

```

Next, we create a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object to display everything. We'll refer to it in our JavaScript code by the variable _mywindow_. Just as in a Max patch, the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") needs a name ("ListenWindow") that must match the OpenGL drawing context we're using. We've turned off the `depthbuffer` and turned on the `idlemouse` attribute, which allows the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object to track mouse events in the window regardless of whether we've clicked our mouse down or not.
```
// create a [jit.gl.render] object for drawing into our window:
var myrender = new JitterObject("jit.gl.render","ListenWindow");
// use a 2-dimensional projection:
myrender.ortho = 2;
// set background to black with full erase opacity (no trails):
myrender.erase_color = [0,0,0,1];

```

Our [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object (assigned to the variable _myrender_) defines a drawing context called "ListenWindow". The [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object (above) and the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") objects (below) share this name. We've decided to use an _orthographic_ projection (by setting the `ortho` attribute to `2`). This means that the _z_ axis of our drawing context is ignored in terms of sizing objects based on their distance from the virtual camera. This essentially creates a 2-dimensional rendering of our scene. We've set the background to black (with a full erase between successive drawing) by setting our `erase_color` to `0 0 0 1`.
```
// create a [jit.gl.gridshape] object for use to control with the mouse
var mywidget = new JitterObject("jit.gl.gridshape","ListenWindow");
mywidget.shape = "sphere";
mywidget.lighting_enable = 1;
mywidget.smooth_shading = 1;
mywidget.scale = [0.1,0.1,0.1];
mywidget.color = [1,1,1,0.5] ;
mywidget.blend_enable = 1;
mywidget.position = [0,0]; // no z necessary in orthographic projection

```

The first [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object we create (assigned to the variable _mywidget_) corresponds to the large sphere moved by our mouse in the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"). After creating it, we set all the relevant attributes we want the sphere to have, just as we would in a Max patcher. Note that in setting the `position` attribute we only use two arguments (_x_ and _y_). In an orthographic projection the _z_ axis is irrelevant to how the shapes are drawn.
```
// create an array of [jit.gl.gridshape] objects
// randomly arrayed across the window
var mysphere = new Array(OBJECT_COUNT);

```

Rather than naming our smaller spheres individually, we're treating them as an Array (called _mysphere_). Each element in this array will then be a separate [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object that we can access by array notation (e.g. _mysphere[5]_ will be the _sixth_ sphere, counting up from 0).
```
// initialize our little spheres with random colors and positions (x,y)
for(var i=0;i<OBJECT_COUNT;i++) {
  mysphere[i] = new JitterObject("jit.gl.gridshape","ListenWindow");
  mysphere[i].shape = "sphere";
  mysphere[i].lighting_enable = 1;
  mysphere[i].smooth_shading = 1;
  mysphere[i].scale = [0.05,0.05,0.05];
  mysphere[i].color = [Math.random(),Math.random(),Math.random(),0.5] ;
  mysphere[i].position = [Math.random()*2.-1, Math.random()*2.-1];
  mysphere[i].blend_enable = 1;
}

```

This code actually creates the individual [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") objects as individual JitterObjects that are members of the Array _mysphere_. We use a JavaScript for() loop to set the initial attributes of all these objects in one block of code. We give them random initial `color` and `position` attributes, scattering them over the screen and coloring them all differently.
```
// create a JitterListener for our [jit.window] object
var mylistener = new JitterListener(mywindow.getregisteredname(), thecallback);

```

Finally, we create a variable called _mylistener_ that we assign to be a JitterListener object. JitterListener objects take two arguments: the _object_ that they listen to, and the _function_ that will be called when the object triggers an event. Our JitterListener object is set to listen to our [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object (_mywindow_). The getregisteredname() property of a JitterObject object returns the `name` by which that object can be accessed by the JitterListener (in the case of [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") objects, this will be the same as name of the drawing context). Whenever our [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object generates an event, a function called thecallback() will be triggered in our JavaScript code. Now that we've instantiated a JitterListener, we can (in most cases) leave it alone and simply deal with the mechanics of the callback function it triggers in response to an event from the object it listens to.
  * Back in the Tutorial patcher, click the [message](https://docs.cycling74.com/reference/message/ "message") box labeled `randomize` or hit the _spacebar_ on your computer keyboard. The small spheres should scatter and change colors. Look at the code for the randomize() function in our [js](https://docs.cycling74.com/reference/js/ "js") file.

```
function randomize() // reorient the little spheres
{
  for(var i=0;i<32;i++) {
   mysphere[i].color = [Math.random(),Math.random(),Math.random(),0.5];
   mysphere[i].position = [Math.random()*2.-1, Math.random()*2.-1];
  }
}

```

Our randomize() function takes our little spheres and scatters them randomly, changing their colors. This allows us to basically restart our simulation whenever we like.
## The callback function
The [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object responds to a variety of mouse events. When the `idlemouse` attribute is set to `1` (as it is in our code) the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object outputs mouse information (the `mouseidle` message) when you drag the pointer over the window. It also tells us when the pointer has left the window area (the `mouseidleout` message). Regardless of the setting of the `idlemouse` attribute, the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object also responds to mouse clicks inside the window (the `mouse` message).
  * In the Tutorial patcher, move the pointer into the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") and click the mouse. The white sphere will turn into a green torus. Release the mouse and the torus will turn into a red sphere. Moving the pointer will turn the sphere white again.

![How our sphere responds to mouse click events \(mouse down and mouse up\).](https://docs.cycling74.com/images/a59059205a6370159e69446eb25e683a_640.webp) How our sphere responds to mouse click events (mouse down and mouse up).
  * Look at the code for the function called thecallback() in our JavaScript code. This code executes whenever our JitterListener object receives an event from our [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object.

```
function thecallback(event)
// callback function to handle events triggered by mousing
// in our [jit.window]
{
	var x,y,button; // some local variables for the callback function

```

The _event_ constructor stores the message sent by the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object to the JitterListener object in our patch. We also declare a few local variables (_x_ , _y_ , and _button_) to store information about the pointer derived from the _event_ message's arguments.
We then use JavaScript if() statements based on the `eventname` property of the _event_ that triggered the callback function. The `eventname` property will contain the name of the message (`mouse`, `mouseidle`, etc.) that triggered the function.
```
if (event.eventname="="mouse")" {
// we're entering, dragging within, or leaving a "mouse click" event

```

This part of the code handles a mouse click event (a click down, dragging of the mouse, and the release of a click).
```
// arguments are (x,y,button,cmd,shift,capslock,option,ctrl)...
// we only care about the first three
x = event.args[0];
y = event.args[1];
button = event.args[2];

```

The first three arguments to the `mouse` event contain the position of the mouse (x and y) and a flag telling us whether the mouse button is down (`1`) or up (`0`). We store these settings into variables (_x_ , _y_ , and _button_) for use later on.
```
if (button) // we're clicked down
   {
      mywidget.color = [0,1,0,1]; // color our control object green
      mywidget.shape = "torus"; // change it to a donut shape
   }
   else // we've just unclicked
   {
      mywidget.color = [1,0,0,1]; // color our object red
      mywidget.shape = "sphere"; // change back to a sphere
   }
   // move our control object to the drawing context's
   // equivalent of where our mouse event occurred:
   mywidget.position = myrender.screentoworld(x,y);
}

```

If our button is down, we turn our [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object _mywidget_ from a white sphere into a green torus. When we release the mouse, we turn it into a red sphere.
Finally, we update the position of the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object controlled by our mouse by updating the `position` attribute of the JitterObject object _mywidget_. Because our drawing context works in OpenGL world coordinates (where the default center of the space is (0, 0) and positions are expressed in decimal values), we need to convert our _x_ and _y_ values into numbers that make sense for our drawing context. The screentoworld() method to a [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object will convert those values from pixel coordinates on the display to world coordinates for the rendering.
```
else if (event.eventname="="mouseidle")" {
   // we're mousing over the window with the mouse up
   x = event.args[0];
   y = event.args[1];
   mywidget.color = [1,1,1,1] ; // color our object white
   mywidget.position = myrender.screentoworld(x,y);
}

```

This code executes whenever we drag our pointer across the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object without clicking the pointer. First we store the variables _x_ and _y_ based on the pointer position, we turn our [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object (_mywidget_) white, in case the previous callback had turned it a different color, and again we reposition mywidget.
```
else if (event.eventname="="mouseidleout")" {
   // we're no longer mousing over the window
   mywidget.color = [1,1,1,0.5] ; // make our object translucent
}

```

When our pointer leaves the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"), the `eventname` property of our callback will be "mouseidleout". All we do is change the alpha to 0.5, leaving the sphere where it was.
```
}
// don't allow this function to be called from Max
thecallback.local = 1;

```

Because our thecallback() function is intended to be executed by our JitterListener object, we set its `local` property to `1` to prevent it from being executed directly by a Max message sent to the [js](https://docs.cycling74.com/reference/js/ "js") object.
## Drawing the scene
Now that we've seen how to respond to mouse events and update our _mywidget_ object's position, color, and shape accordingly, we need to look at how we perform the actual rendering of our scene in response to a `bang` message from the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") object in our Max patcher. The bang() function in our JavaScript code handles the drawing as well as the animation of the little spheres in response to the new position of our large sphere.
  * Look at the code for the bang() function.


The majority of our bang() function iterates through the positions of all the little spheres and compares them to the position of the large one. If the distance between them is small enough that the spheres would overlap when drawn, we move the little sphere away the minimum amount necessary to have the spheres touch. This type of processing is known as _collision detection_ and is a ubiquitous technique in the field of computer animation.
```
function bang()
// main drawing loop... figure out which little spheres to move
// and drive the renderer
{
  // collision detection block. we need to iterate through
  // the little spheres and check their distance from the control
  // object. if we're touching we move the little sphere away
  // along the correct angle of contact.
  for(var i = 0;i<OBJECT_COUNT;i++) {

```

We enter a JavaScript for() loop to check the position of our large sphere against every small sphere, one at a time.
```
// cartesian distance along the x and y axis
var distx = mywidget.position[0]-mysphere[i].position[0];
var disty = mywidget.position[1]-mysphere[i].position[1];

// polar distance between the two objects
var r = Math.sqrt(distx*distx+disty*disty);
// angle of little sphere around control object
var theta = Math.atan2(disty,distx);

```

By subtracting the _x_ and _y_ positions of the two spheres (large and small) from one another, we get their Cartesian distance. We can convert this to polar (absolute) distance by applying the Pythagorean theorem to derive the hypotenuse (stored in the variable _r_). We then derive the angle of the small sphere around the large one by taking the arctangent of the rise (_x_) over the run (_y_).
```
// check for collision...
if(r<0.15)
// control object is size 0.1, little spheres are 0.05,
// so less than 0.15 and it's a hit...
{

```

Because our large sphere has a `scale` attribute of `0.1 0.1 0.1` and our small spheres have `scale` attributes of `0.05 0.05 0.05`, we can infer that the objects are overlapping if the distance between them is less than 0.15. This triggers a block of code that deals with the collision.
```
// convert polar->cartesian to figure out x and y displacement
   var movex = (0.15-r)*Math.cos(theta);
   var movey = (0.15-r)*Math.sin(theta);

   // offset the little sphere to the new position,
   // which should be just beyond touching at the
   // angle of contact we had before. the result
   // should look like we've "pushed" it along...
   mysphere[i].position = [mysphere[i].position[0]-movex, mysphere[i].position[1]-movey];
}

```

We use the polar distance and angle, combined with the minimum allowable distance between the objects (0.15), to derive how far we need to nudge the little sphere along the _x_ and _y_ axes to stop it from overlapping the large sphere. We figure out these values by converting the polar coordinates back into Cartesian values stored in the variables _movex_ and _movey_. We then subtract these two variables' values from the current position of the small sphere, pushing it out of the way.
```
// rendering block...
  myrender.erase(); // erase the drawing context
  myrender.drawclients(); // draw the client objects
  myrender.swap(); // swap in the new drawing
}

```

This last block of code does the actual rendering. Just as you would when working with Jitter OpenGL objects in a Max patcher, you send an `erase` message to the [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object (_myrender_). The drawclients() method to [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") collects all the relevant information from the OpenGL objects attached to our drawing context and draws them; any OpenGL objects with an `automatic` attribute set to `0` will have to be drawn manually here. The swap() method then replaces the old rendering with the new one in the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object, showing us the updated scene. The drawclients() and swap() method are combined into one operation when you send a `bang` message to a [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") object in a Max patcher.
  * Back in the Tutorial patcher, click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box attached to the [message](https://docs.cycling74.com/reference/message/ "message") box labeled `fullscreen $1` (or hit the _escape_ key on your computer keyboard). The [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object will fill the screen. Notice that the coordinate conversion that allows you to move the large sphere around the screen with the mouse still works fine. You can take the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object out of fullscreen mode by pressing the _escape_ key on your keyboard. In the JavaScript code, look at the fullscreen() function:

```
function fullscreen(v)
// function to send the [jit.window] into fullscreen mode
{
  mywindow.fullscreen = v;
}

```

The fullscreen() attribute of a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") JitterObject object behaves just as the `fullscreen` message sent to a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object in a Max patcher.
## Summary
An entire OpenGL Jitter patch can be encapsulated in JavaScript by instantiating [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render"), [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"), and other OpenGL objects within procedural code written for the [js](https://docs.cycling74.com/reference/js/ "js") object. These objects have all their messages and attributes exposed as corresponding methods and properties. You can use a JitterListener object to respond to events triggered by a Jitter object within JavaScript. The JitterListener then executes a callback function, passing the calling message to it as its argument. This allows you to write JavaScript functions to respond to mouse interactivity in a [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object, file reading in a [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") object, and other situations where you would want to respond to an event triggered by a message sent by a Jitter object out its status outlet in a Max patcher.
## Code Listing
```
// 47jMarbles.js
//
// Demonstrates how to set up a JitterListener object to listen
// to the output of a Jitter object instantiated within [js].
//
// rld, 7.05
//

var OBJECT_COUNT = 32; // number of little spheres

// create a [jit.window] object for our display
// (this is the object we'll "listen" to):
var mywindow = new JitterObject("jit.window","ListenWindow");
// turn off depth testing... we're using blending instead:
mywindow.depthbuffer = 0;
// turn ON idlemousing... we want to listen for it:
mywindow.idlemouse = 1;

// create a [jit.gl.render] object for drawing into our window:
var myrender = new JitterObject("jit.gl.render","ListenWindow");
// use a 2-dimensional projection:
myrender.ortho = 2;
// set background to black with full erase opacity (no trails):
myrender.erase_color = [0,0,0,1];

// create a [jit.gl.gridshape] object for use to control with the mouse
var mywidget = new JitterObject("jit.gl.gridshape","ListenWindow");
mywidget.shape = "sphere";
mywidget.lighting_enable = 1;
mywidget.smooth_shading = 1;
mywidget.scale = [0.1,0.1,0.1];
mywidget.color = [1,1,1,0.5] ;
mywidget.blend_enable = 1;
mywidget.position = [0,0]; // no z necessary in orthographic projection

// create an array of [jit.gl.gridshape] objects randomly arrayed across the window
var mysphere = new Array(OBJECT_COUNT);

// initialize our little spheres with random colors and positions (x,y)
for(var i=0;i<OBJECT_COUNT;i++) {
  mysphere[i] = new JitterObject("jit.gl.gridshape","ListenWindow");
  mysphere[i].shape = "sphere";
  mysphere[i].lighting_enable = 1;
  mysphere[i].smooth_shading = 1;
  mysphere[i].scale = [0.05,0.05,0.05];
  mysphere[i].color = [Math.random(),Math.random(),Math.random(),0.5] ;
  mysphere[i].position = [Math.random()*2.-1, Math.random()*2.-1];
  mysphere[i].blend_enable = 1;
}

// create a JitterListener for our [jit.window] object
var mylistener = new JitterListener(mywindow.getregisteredname(), thecallback);

function randomize() // reorient the little spheres
{
  for(var i=0;i<32;i++) {
   mysphere[i].color = [Math.random(),Math.random(),Math.random(),0.5] ;
   mysphere[i].position = [Math.random()*2.-1, Math.random()*2.-1];
  }
}


function thecallback(event)
// callback function to handle events triggered by mousing
// in our [jit.window]
{

  var x,y,button; // some local variables for thecallback
  if (event.eventname="="mouse")" {
  // we're entering, dragging within, or leaving a "mouse click" event

   // arguments are (x,y,button,cmd,shift,capslock,option,ctrl)...
   // we only care about the first three
   x = event.args[0];
   y = event.args[1];
   button = event.args[2];
   if (button) // we're clicked down
   {
      mywidget.color = [0,1,0,1]; // color our control object green
      mywidget.shape = "torus"; // change it to a donut shape
   }
   else // we've just unclicked
   {
      mywidget.color = [1,0,0,1]; // color our object red
      mywidget.shape = "sphere"; // change back to a sphere
   }
   // move our control object to the drawing context's
   // equivalent of where our mouse event occurred:
   mywidget.position = myrender.screentoworld(x,y);
  }
  else if (event.eventname="="mouseidle")" {
  // we're mousing over the window with the mouse up
   x = event.args[0];
   y = event.args[1];
   mywidget.color = [1,1,1,1] ; // color our object white
   // move our control object to the drawing context's
   // equivalent of where our mouse event occurred:
   mywidget.position = myrender.screentoworld(x,y);
  }
  else if (event.eventname="="mouseidleout")" {
  // we're no longer mousing over the window
   mywidget.color = [1,1,1,0.5] ; // make our object translucent
  }


}
// don't allow this function to be called from Max
thecallback.local = 1;

function bang()
// main drawing loop... figure out which little spheres to move
// and drive the renderer
{
  // collision detection block. we need to iterate through
  // the little spheres and check their distance from the control
  // object. if we're touching we move the little sphere away
  // along the correct angle of contact.
  for(var i = 0;i<OBJECT_COUNT;i++) {
   // cartesian distance along the x and y axis
   var distx = mywidget.position[0]-mysphere[i].position[0];
   var disty = mywidget.position[1]-mysphere[i].position[1];

   // polar distance between the two objects
   var r = Math.sqrt(distx*distx+disty*disty);
   // angle of little sphere around control object
   var theta = Math.atan2(disty,distx);

   // check for collision...
   if(r<0.15)
   // control object is size 0.1, little spheres are 0.05,
   // so less than 0.15 and it's a hit...
   {
      // convert polar->cartesian to figure out x and y displacement
      var movex = (0.15-r)*Math.cos(theta);
      var movey = (0.15-r)*Math.sin(theta);

      // offset the little sphere to the new position,
      // which should be just beyond touching at the
      // angle of contact we had before. the result
      // should look like we've "pushed" it along...
      mysphere[i].position = [mysphere[i].position[0]-movex, mysphere[i].position[1]-movey];
   }
  }

  // rendering block...
  myrender.erase(); // erase the drawing context
  myrender.drawclients(); // draw the client objects
  myrender.swap(); // swap in the new drawing
}

function fullscreen(v)
// function to send the [jit.window] into fullscreen mode
{
  mywindow.fullscreen = v;
}

```

## See Also
  * [jit.gl.gridshape - Generate simple geometric shapes as a connected grid](https://docs.cycling74.com/reference/jit.gl.gridshape)
  * [jit.gl.render - Render Open GL](https://docs.cycling74.com/reference/jit.gl.render)
  * [jit.window - Display data in a Window](https://docs.cycling74.com/reference/jit.window)
  * [js - Javascript in Max](https://docs.cycling74.com/reference/js/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
