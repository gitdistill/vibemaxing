---
description: Designing graphical user interfaces with JavaScript
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/javascriptchapter04/
title: Designing User Interfaces
---

Download Series Content and Patchers
# JavaScript Tutorial 4: Designing User Interfaces in JavaScript
## Introduction
The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object allows you use JavaScript to design graphical user interface objects for use in the Max environment. The JavaScript implementation for the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object is similar to that used in the [js](https://docs.cycling74.com/reference/js/ "js") object, with an added API that supports two- and three-dimensional vector graphics drawn with OpenGL commands. It also includes methods for handling mouse interaction in the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object window.
In addition to the advantages provided by JavaScript, [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") provides a number of built-in features that make UI development flexible:- [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") objects draw their geometries relative to the size of the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object box; resizing a [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object will correctly resize all of the drawn elements inside of it.
  * [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") objects work with a vector graphics language (OpenGL) that supports a wide variety of simple shape and drawing primitives. In addition, a number of higher-level graphics functions are available. The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object can also perform anti-aliasing on the image to give you as smooth an object as possible, though this comes with a decrease in performance.
  * The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object allows you to draw a scene that exceeds the boundaries of the object box. By adjusting the camera orientation in the OpenGL space, you can create and manage different ‘views’ of the same UI object. In addition to using the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object for user-interface design, one could use the object simply as an OpenGL graphics engine built into the Max patcher for algorithmic drawing operations.


This Tutorial assumes that you’ve already looked at the other JavaScript Tutorials. The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object bases most of its graphics language on OpenGL functions, the specifics of which are beyond the scope of this Tutorial. The OpenGL ‘Redbook’ is the standard reference for these functions. An online version is available at: <http://www.opengl.org/documentation/red_book/>
The OpenGL API supported by [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") is contained in an object called [jsui](https://docs.cycling74.com/reference/jsui/ "jsui")**sketch**. This object understands most OpenGL commands and symbolic constants. Converting between OpenGL code (e.g. as given in C in the ‘Redbook’ code examples) and **sketch** methods and properties for [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") JavaScript code is quite straightforward if you observe the following guidelines:- All OpenGL commands are lowercase in the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") sketch object, e.g. `glColor()` becomes `sketch.glcolor()`.
  * OpenGL symbolic constants, in addition to being lowercase, lose their ‘GL_’ prefix, so that `GL_CLIP_PLANE1` becomes `clip_plane1()`, for example.


A number of higher-level drawing and shape commands are available which may speed up user interface development. The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") sketch reference found in the [Javascript in Max](https://docs.cycling74.com/userguide/javascript/) guide (and the help patch for the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object) contain lists of these commands.
##  [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") in Action
Take a look at our tutorial patcher. You will see a [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object containing a grid of light red circles against a green background. Clicking on a circle inside the object will change the circle’s color to a darker red. Clicking on the same circle again will change the color back to light red.
Click on some circles so that they are highlighted (in dark red). At the right of the patch, manipulate some of the [slider](https://docs.cycling74.com/reference/slider/ "slider") objects above the [router](https://docs.cycling74.com/reference/router/ "router") object. Note the correspondence between which circles are clicked and which [slider](https://docs.cycling74.com/reference/slider/ "slider") objects below the [router](https://docs.cycling74.com/reference/router/ "router") echo the values from above. Click on the [message](https://docs.cycling74.com/reference/message/ "message") box labeled clear attached to the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object. The circles should all go to light red and the [router](https://docs.cycling74.com/reference/router/ "router") object will no longer pass messages from the [slider](https://docs.cycling74.com/reference/slider/ "slider") objects above. Click on the [message](https://docs.cycling74.com/reference/message/ "message") box containing the list `0 0 1, 1 1 1`, etc. The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object should update to show a diagonal row. The [router](https://docs.cycling74.com/reference/router/ "router") object will now pass messages from the first [slider](https://docs.cycling74.com/reference/slider/ "slider") above to the first [slider](https://docs.cycling74.com/reference/slider/ "slider") below, and so on.
Our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object uses JavaScript code to emulate some of the functionality of the Max [matrixctrl](https://docs.cycling74.com/reference/matrixctrl/ "matrixctrl") object. The columns represent the input to the [router](https://docs.cycling74.com/reference/router/ "router") object; the rows specify the output. Our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") communicates with the [router](https://docs.cycling74.com/reference/router/ "router") object by sending lists (in the format input output state) that tell the [router](https://docs.cycling74.com/reference/router/ "router") object to pass messages received at an inlet to all the appropriate outlets given the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object’s current configuration.
Like the [js](https://docs.cycling74.com/reference/js/ "js") object, the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object gets its program from a file written in JavaScript saved somewhere in the search path. Because it is a graphical object, there is no object box to type in the name of the file. Instead, we set the JavaScript source file using the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object’s **Inspector**.
Unlock the tutorial patch and highlight the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object. Under the **Object** menu, select **Get Info…**. An Inspector should appear with the name of our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") source file (‘mymatrix.js’) in the text field labeled ‘JavaScript File.’ 
You can also set the size of the object in the Inspector, as well as turn on or off a border around the object. Disabling the object border, combined with setting the background color of your Max patch to match that of your [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object, can help you design a seamless user interface.
## The Drawing Code
The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object is graphical, so double-clicking the object will not open the text editor as it does with the [js](https://docs.cycling74.com/reference/js/ "js") object. Instead, click the [message](https://docs.cycling74.com/reference/message/ "message") box labeled `open`. The text editor containing our JavaScript file (‘mymatrix. [js](https://docs.cycling74.com/reference/js/ "js") ’) will appear. Our JavaScript file is saved on disk in the same folder as the tutorial patch.
As with a [js](https://docs.cycling74.com/reference/js/ "js") script, our code for the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object starts with a global block that allows us to define inlets and outlets for the object and global variables for our code. It is also where we type commands that we want to occur when the object is initialized:
```
// inlets and outlets
inlets = 1;
outlets = 1;
// global variables
var ncols=4; // default columns
var nrows=4; // default rows
var vbrgb = [0.8,1.,0.8,0.5];
var vmrgb = [0.9,0.5,0.5,0.75];
var vfrgb = [1.,0.,0.2,1.];
// initialize state array
var state = new Array(8);
for(var i=0;i < 8;i++)
{
   state[i] = new Array(8);
   for(var j=0;j < 8;j++)
   {
      state[i][j] = 0;
   }
}
// set up  jsui  defaults to 2d
sketch.default2d();
// initialize graphics
draw();
refresh();

```

Our JavaScript code defines two global variables (`ncols` and `nrows`) which can be accessed by all functions, as well as a number of global **Array** objects that define colors for the drawing and a state array that we will use to hold information about which circles are ‘on’ and which are ‘off’ in our user interface.
Multi-dimensional arrays in JavaScript are allocated by an **Array** object in which each element of the Array is itself an Array object (and so on, if more than two dimensions are needed). This may seem somewhat unusual if you’ve worked in other programming languages where multi-dimensional arrays can be declared directly (e.g. C). The `for()` loops in our global block accomplish this allocation and initialize all the elements of the state array to `0`. Once a multi-dimensional array is created, it can be referenced using common bracket notation, e.g. `state[4][2]`.
Following our variable and array declarations, we find three commands that refer to the graphical behavior of the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object. The first, `sketch.default2d()`, tells our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object to initialize a number of default behaviors with the assumption that we will be giving it graphics commands for a two-dimensional scene. It sets a default view upon the OpenGL rendering context and performs a number of utility routines to make it easy for us to simply start placing graphical elements in the window. The `draw()` command (which could be named anything) refers to our main graphics function which we write to contain all the commands needed to draw the user interface of the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object. The `refresh()` command copies the OpenGL backbuffer (where the drawing is done initially to prevent flicker) to the actual screen display. Commenting out the `refresh()` command will prevent our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object from ever showing us anything.
Below the global block, examine the `draw()` function. This is the function that provides [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") with all the commands it needs to draw our screen interface:
```
// draw -- main graphics function
function draw()
{
   with (sketch)
   {
      // set how the polygons are rendered
      glclearcolor(vbrgb[0],vbrgb[1],vbrgb[2],vbrgb[3]); // set the clear color
      glclear(); // erase the background
      var colstep=2./ncols; // how much to move over per column
      var rowstep=2./nrows; // how much to move over per row
      for(var i=0;i < ncols;i++) // iterate through the columns
      {
         for(var j=0;j < nrows;j++) // iterate through the rows
         {
            moveto((i*colstep + colstep/2)-1.0, 1.0 - (j*rowstep + rowstep/2), 0.); // move the drawing point
            if(state[i][j]) // set 'on' color
            {
               glcolor(vfrgb[0],vfrgb[1],vfrgb[2],vfrgb[3]);
            }
            else // set 'off' color (midway between vbrgb and vfrgb)
            {
               glcolor(vmrgb[0],vmrgb[1],vmrgb[2],vmrgb[3]);
            }
            circle(0.7/Math.max(nrows,ncols)); // draw the circle
         }
      }
   }
}

```

The graphics commands (everything beginning with ‘gl’, as well as the `circle()` command) are all methods and properties of the **sketch** object, which encapsulates most of the OpenGL API, much as the **Math** object encapsulates most common math functions.
The JavaScript `with()` statement allows us to use properties and methods belonging to an object (in this case the **sketch** object that provides us with our OpenGL functionality) without having to reference ‘sketch’ in every command. Without the `with()`, we would have to write `sketch.glcolor()` instead of `glcolor()`, `sketch.circle()` instead of `circle()`, etc. This useful trick could also be implemented in functions that rely heavily on other objects (e.g. **Task** or **Patcher**).
Our `draw()` function sets some default drawing behaviors and clears the window with the color defined by the `vbrgb` array. It then iterates through our state array based on how many columns (`ncols`) and rows (`nrows`) we’ve defined for our object. If a particular state element is `0` (off), it draws a circle in the color defined by `vmrgb`. If an element is `1` (on), the circle is drawn in the `vfrgb` color. The position of the circles is determined by the number of rows and columns, and is based on boundaries of our OpenGL world, which are set to be between `–1.0` and `1.0` on both axes (i.e. the middle of our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") window in OpenGL coordinates is `0`, `0`).
The size of the world is not limited to coordinates in the range of `–1.0` to `1.0`; our default viewport merely sets us at the center of the scene whose y range is `–1.0` to `1.0` and whose x range is scaled based on the aspect ration of the object. Because our object box happens to be square, our ranges are the same on both axes. Changing the viewport (by manipulating the position of our virtual “camera”, for example) will change what coordinates are visible in the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object’s box.
## Setting Parameters
In the Tutorial patch, change the [number](https://docs.cycling74.com/reference/number/ "number") box objects that set the rows and columns. Note that the object will dynamically add up to eight rows and columns of circles based on those values. Look at the `rows()` and `cols()` functions in the JavaScript code. Note that they call a `bang()` function after setting their variables.
```
// rows -- change number of rows in  jsui 
function rows(val)
{
   if(arguments.length)
   {
      nrows=arguments[0];
       bang (); // draw and refresh display
   }
}
// cols -- change number of columns is  jsui 
function cols(val)
{
   if(arguments.length)
   {
      ncols=arguments[0];
       bang (); // draw and refresh display
   }
}

```

The `bang()` function, which we call after nearly every change made to the object from Max (including mouse events), simply calls `draw()` and `refresh()` as we did in our global block, causing the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object to update its window to reflect any graphical changes.
```
// bang -- draw and refresh display
function bang()
{
   draw();
   refresh();
}

```

By only doing the drawing when necessary, we are able to reduce the amount of processor time the object uses.
In the tutorial patcher, change the [swatch](https://docs.cycling74.com/reference/swatch/ "swatch") objects that set the `frgb` and `brgb` messages to our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object. Look at the corresponding functions (`frgb()` and `brgb()`) in the JavaScript code. Note that the array for the ‘off’ circle’s color (`vmrgb`) is midway between the colors set by frgb and brgb messages:
```
// frgb -- change foreground (clicked) circle color
function frgb(r,g,b)
{
   vfrgb[0] = r/255.;
   vfrgb[1] = g/255.;
   vfrgb[2] = b/255.;
   vmrgb[0] = 0.5*(vfrgb[0]+vbrgb[0]);
   vmrgb[1] = 0.5*(vfrgb[1]+vbrgb[1]);
   vmrgb[2] = 0.5*(vfrgb[2]+vbrgb[2]);
    bang (); // draw and refresh display
}
// brgb -- change background color
function brgb(r,g,b)
{
   vbrgb[0] = r/255.;
   vbrgb[1] = g/255.;
   vbrgb[2] = b/255.;
   vmrgb[0] = 0.5*(vfrgb[0]+vbrgb[0]);
   vmrgb[1] = 0.5*(vfrgb[1]+vbrgb[1]);
   vmrgb[2] = 0.5*(vfrgb[2]+vbrgb[2]);
    bang (); // draw and refresh display
}

```

Color in OpenGL is represented as four floating-point values in the range `0.0` - `1.0`, corresponding to the red, green, blue, and alpha (transparency) amounts, respectively. This is in contrast to many video systems that commonly refer to color in the integer `0` - `255` (with no alpha value). Most of the work in our `frgb()` and `brgb()` functions is to convert from the latter (used by the [swatch](https://docs.cycling74.com/reference/swatch/ "swatch") object) into the former (understood by the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object).
## Mouse Interaction
Unlock the tutorial patcher and resize the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object (the circles should resize dynamically). Lock the patcher and notice that the mouse clicks still change the states of the correct circles. Lock the patch again and look at the `onclick()` function in the JavaScript code.
The `onclick()`, `ondblclick()`, and `ondrag()` functions, when defined, tell our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object what to do when a user clicks, double-clicks, or drags the mouse across the object. The function is called with arguments for where in the object’s window the action occurred, as well as a number of flags (such as whether the mouse was depressed, the state of the shift key, etc.). In our onclick() function, we only use first two arguments, corresponding to the x and the y of the mouse click.
```
// onclick -- deal with mouse click event
function onclick(x,y)
{
   var worldx = sketch.screentoworld(x,y)[0];
   var worldy = sketch.screentoworld(x,y)[1];
   var colwidth = 2./ncols; // width of a column, in world coordinates
   var rowheight = 2./nrows; // width of a row, in world coordinates
   var x_click = Math.floor((worldx+1.)/colwidth); // which column we clicked
   var y_click = Math.floor((1.-worldy)/rowheight); // which row we clicked
   state[x_click][y_click] = !state[x_click][y_click]; // flip the state of the clicked point
   outlet(0, x_click, y_click, state[x_click][y_click]); // output the coordinates and state of the clicked point
    bang (); // draw and refresh display
}

```

Our OpenGL graphics world is defined in terms of floating-point coordinates (in our case, between `–1.0` and `1.0`). The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") mouse functions return coordinates based on which _pixel_ (counting away from the upper left-hand corner of the object box) the mouse event occurred. We need to convert between these two systems (of world coordinates and screen coordinates, respectively) in order to properly evaluate the mouse events for our grid of circles. The sketch methods `worldtoscreen()` and `screentoworld()` perform these conversions for us: 
```
worldx = sketch.screentoworld(x,y)[0];
worldy = sketch.screentoworld(x,y)[1];

```

Once we know the width and height where we clicked, we can subdivide it based on how many circles we have on each axis: 
```
colwidth = 2./ncols; // width of a column, in world coordinates
rowheight = 2./nrows; // width of a row, in world coordinates

```

We can then plug in the coordinates of the mouse click to figure out which circle we clicked nearest to: 
```
x_click = Math.floor((worldx+1.)/colwidth); // which column we clicked
y_click = Math.floor((1.-worldy)/rowheight); // which row we clicked

```

We then reverse the element of the state array corresponding to the circle we clicked: 
```
state[x_click][y_click] = !state[x_click][y_click];

```

After we’ve set the state array correctly, we send out a list corresponding to the change out our [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object’s outlet into Max. We then `bang` our own [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object, updating the graphics to reflect the change: 
```
outlet(0, x_click, y_click, state[x_click][y_click]);
bang();

```

Note that we have set our `onclick()` function to be local, so that it can’t be triggered from an `onclick` message sent from our Max patch.
Familiarize yourself with the JavaScript code and how it relates to the behavior of the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object in the patcher. Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object to activate the [metro](https://docs.cycling74.com/reference/metro/ "metro") object at the right of the patch. This will simulate some input from the [slider](https://docs.cycling74.com/reference/slider/ "slider") objects. Place `post()` statements in the JavaScript code to help navigate the values as they are passed from mouse click to list output.
## Summary
The [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object is a powerful tool to allow you to design and implement customizable user interfaces using JavaScript as a programming language. The key points in the program involve the main drawing function (which defines a sequence of commands to describe the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") object’s graphical display) and the mouse interaction functions `onclick()`, `ondblclick()`, and `ondrag()`. Important things to note are the differences in color representation (floating point vs. integer) and spatial coordinates (floating-point world coordinates vs. Cartesian pixel coordinates) between the OpenGL API used in the [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") sketch object and the Max environment, respectively.
## Code Listing
```
// mymatrix. js 
//
// simulates a simple grid of clickable widgets (a la matrixctrl)
//
// rld, 5.04
//
// inlets and outlets
inlets = 1;
outlets = 1;
// global variables
var ncols=4; // default columns
var nrows=4; // default rows
var vbrgb = [0.8,1.,0.8,0.5];
var vmrgb = [0.9,0.5,0.5,0.75];
var vfrgb = [1.,0.,0.2,1.];
// initialize state array
var state = new Array(8);
for(var i=0;i < 8;i++)
{
   state[i] = new Array(8);
   for(var j=0;j < 8;j++)
   {
      state[i][j] = 0;
   }
}
// set up  jsui  defaults to 2d
sketch.default2d();
// initialize graphics
draw();
refresh();
// draw -- main graphics function
function draw()
{
   with (sketch)
   {
      // set how the polygons are rendered
      glclearcolor(vbrgb[0],vbrgb[1],vbrgb[2],vbrgb[3]); // set the clear color
      glclear(); // erase the background
      var colstep=2./ncols; // how much to move over per column
      var rowstep=2./nrows; // how much to move over per row

      for(var i=0;i < ncols;i++) // iterate through the columns
      {
         for(var j=0;j < nrows;j++) // iterate through the rows
         {
            moveto((i*colstep + colstep/2)-1.0, 1.0 - (j*rowstep + rowstep/2), 0.); // move the drawing point
            if(state[i][j]) // set 'on' color
            {
               glcolor(vfrgb[0],vfrgb[1],vfrgb[2],vfrgb[3]);
            }
            else // set 'off' color (midway between vbrgb and vfrgb)
            {
               glcolor(vmrgb[0],vmrgb[1],vmrgb[2],vmrgb[3]);
            }
            circle(0.7/Math.max(nrows,ncols)); // draw the circle
         }
      }
   }
}
// bang -- draw and refresh display
function bang()
{
   draw();
   refresh();
}
// rows -- change number of rows in  jsui 
function rows(val)
{
   if(arguments.length)
   {
      nrows=arguments[0];
      bang(); // draw and refresh display
   }
}
// cols -- change number of columns is  jsui 
function cols(val)
{
   if(arguments.length)
   {
      ncols=arguments[0];
      bang(); // draw and refresh display
   }
}

// list -- update our state to respond to a change from Max
function list(v)
{
   if(arguments.length==3) // bail if incorrect number of arguments
   {
      state[arguments[0]][arguments[1]]=arguments[2]; // update our internal state based on the list
      outlet(0, arguments[0], arguments[1], arguments[2]); // echo the list out the outlet
   }
   bang(); // draw and refresh display
}
// clear -- wipe the state clean
function clear()
{
   for(var i=0;i < ncols;i++)
   {
      for(var j=0;j < nrows;j++)
      {
         state[i][j]=0; // wipe the state
      }
   }
   outlet(0, “clear”); // clear the  router  or matrix~ downstream
   bang(); // draw and refresh display
}
// frgb -- change foreground (clicked) sphere color
function frgb(r,g,b)
{
   vfrgb[0] = r/255.;
   vfrgb[1] = g/255.;
   vfrgb[2] = b/255.;
   vmrgb[0] = 0.5*(vfrgb[0]+vbrgb[0]);
   vmrgb[1] = 0.5*(vfrgb[1]+vbrgb[1]);
   vmrgb[2] = 0.5*(vfrgb[2]+vbrgb[2]);
   bang(); // draw and refresh display
}
// brgb -- change background color
function brgb(r,g,b)
{
   vbrgb[0] = r/255.;
   vbrgb[1] = g/255.;
   vbrgb[2] = b/255.;
   vmrgb[0] = 0.5*(vfrgb[0]+vbrgb[0]);
   vmrgb[1] = 0.5*(vfrgb[1]+vbrgb[1]);
   vmrgb[2] = 0.5*(vfrgb[2]+vbrgb[2]);
   bang(); // draw and refresh display
}
// onresize -- deal with a resized  jsui  box
function onresize(w,h)
{
   bang(); // draw and refresh display
}
onresize.local = 1; // make function private to prevent triggering from Max

// onclick -- deal with mouse click event
function onclick(x,y)
{
   var worldx = sketch.screentoworld(x,y)[0];
   var worldy = sketch.screentoworld(x,y)[1];
   var colwidth = 2./ncols; // width of a column, in world coordinates
   var rowheight = 2./nrows; // width of a row, in world coordinates
   var x_click = Math.floor((worldx+1.)/colwidth); // which column we clicked
   var y_click = Math.floor((1.-worldy)/rowheight); // which row we clicked
   state[x_click][y_click] = !state[x_click][y_click]; // flip the state of the clicked point
   outlet(0, x_click, y_click, state[x_click][y_click]); // output the coordinates and state of the clicked point
   bang(); // draw and refresh display
}
onclick.local = 1; // make function private to prevent triggering from Max
// ondblclick -- pass buck to onclick()
function ondblclick(x,y)
{
   onclick(x,y);
}
ondblclick.local = 1; // make function private to prevent triggering from Max

```

## See Also
  * [jsui - JavaScript UI object](https://docs.cycling74.com/reference/jsui/)
  * [swatch - Color ](https://docs.cycling74.com/reference/swatch/)[swatch](https://docs.cycling74.com/reference/swatch/ "swatch") for RGB color selection and display



Kind
    Tutorial 

Category
    JavaScript 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
