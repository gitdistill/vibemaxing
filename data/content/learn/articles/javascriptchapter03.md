---
description: Scheduling events and sharing data in JavaScript
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/javascriptchapter03/
title: Tasks, Arguments, and Globals
---

Download Series Content and Patchers
# JavaScript Tutorial 3: JavaScript Tasks, Arguments, and Globals
## Introduction
The [js](https://docs.cycling74.com/reference/js/ "js") object allows you create JavaScript functions that use the Max scheduler. These functions can be triggered by Max messages to the [js](https://docs.cycling74.com/reference/js/ "js") object. The timing interval at which the function is called, how many times it repeats (including whether it repeats indefinitely), and whether it begins executing immediately or at some point in the future can all be determined by your code.
In this Tutorial, we’ll look at how scheduling works in JavaScript. Along the way, we’ll look at two other important features of the JavaScript implementation in Max: [js](https://docs.cycling74.com/reference/js/ "js") object _arguments_ (which allow you to pass arguments directly to your JavaScript from the object box) and _Global_ objects (which allow you to share data between internal [js](https://docs.cycling74.com/reference/js/ "js") data structures and Max).
## Scheduling in JavaScript
Take a look at the tutorial patcher. You’ll see four [js](https://docs.cycling74.com/reference/js/ "js") objects, all of which use the same JavaScript source file (called ‘globaltask.js’), which is saved on disk in the same folder as the Tutorial patch.
Click the [button](https://docs.cycling74.com/reference/button/ "button") object at the top of the patch labeled ‘send a bounce.’ The four [js](https://docs.cycling74.com/reference/js/ "js") objects should begin to generate numbers that are then sent downstream to your MIDI synthesizer output (via the [makenote](https://docs.cycling74.com/reference/makenote/ "makenote") and [noteout](https://docs.cycling74.com/reference/noteout/ "noteout") objects). Double-click the [noteout](https://docs.cycling74.com/reference/noteout/ "noteout") object and select a valid output synthesizer, and you should begin hearing notes. Additional [button](https://docs.cycling74.com/reference/button/ "button") objects are connected to the left outlets of the [js](https://docs.cycling74.com/reference/js/ "js") objects to provide visual feedback on when a number is being sent. In addition, a [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") object called `view` receives the `bang` messages from the [button](https://docs.cycling74.com/reference/button/ "button") object and creates a scrolling visual feedback of the generated rhythm with a [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") object.
Note that the specific timing of the four objects, as well as what pitches they generate, are different; these are determined by the arguments to the [js](https://docs.cycling74.com/reference/js/ "js") objects (more on this later).
The JavaScript code used in the [js](https://docs.cycling74.com/reference/js/ "js") objects is a simple mock-up of an exponentially decaying timing function (analogous to a rubber ball being dropped onto a hard floor). Notes are sent at an exponentially increasing rate, until the speed at which they are sending exceeds a threshold value (five milliseconds, in the case of our script). Upon exceeding that threshold, the function stops and a `bang` is sent out of the right outlet of our [js](https://docs.cycling74.com/reference/js/ "js") objects to notify that the timing function has ceased. The use of a ‘done’ `bang` is a common convention among Max objects to signify the completion of a task (c.f. [line](https://docs.cycling74.com/reference/line/ "line"), [uzi](https://docs.cycling74.com/reference/uzi/ "uzi"), [coll](https://docs.cycling74.com/reference/coll/ "coll"), etc.).
Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") labeled ‘repeat’ and click the top [button](https://docs.cycling74.com/reference/button/ "button") again. Notice that the cycle of bouncing notes repeats, as the `bang` from the [js](https://docs.cycling74.com/reference/js/ "js") objects cause them to retrigger themselves. The difference in the timing acceleration of the four [js](https://docs.cycling74.com/reference/js/ "js") objects will cause them to phase over multiple iterations of the cycle (note how this is displayed in the [multislider](https://docs.cycling74.com/reference/multislider/ "multislider")). If you click the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") again, the current cycle of bounces will complete in each object and then stop. Double-click any of the [js](https://docs.cycling74.com/reference/js/ "js") objects in the patch; let’s examine their code.
## Right on Schedule
Examine the global code for our script:
```
// inlets and outlets
inlets = 1;
outlets = 2;
// define global variables and set defaults
var tsk = new Task(mytask, this); // our main task
var count = 0;
var decay = 1.0;
// defaults for arguments
var dcoeff = -0.0002; // decay coefficient
var note = 60; // note to trigger upon bounce
// process arguments (decay coefficient, note to trigger)
if(jsarguments.length>1) // argument 0 is the name of the  js  file
{
   dcoeff = jsarguments[1];
}
if(jsarguments.length>2)
{
   note = jsarguments[2];
}
// Global (Max namespace) variables
glob = new Global(“bounce”);
glob.starttime = 500;

```

The global code section of our JavaScript file, which defines the familiar inlets, outlets (we have two this time), and variables, has a number of things that we haven’t encountered before. The first is a variable assigned to a special object called **Task** :
```
var tsk = new Task(mytask, this); // our main task

```

This creates a new Task object in JavaScript referred to by the name `tsk`. When we call methods for `tsk`, they will relate to the scheduling of a function called `mytask()`. The controlling object for the Task will be our [js](https://docs.cycling74.com/reference/js/ "js") object (which we refer to as `this`). If we would like to execute our task once, we would write: 
```
tsk .execute(); // run our task function once

```

If we would like to make our task repeat every 250 milliseconds for 20 repetitions, we would write:
```
tsk .interval = 250;
 tsk .repeat(20);

```

If no arguments are given to the `repeat()` method, the Task will be scheduled indefinitely, until we cancel it as follows:
```
tsk .cancel(); // cancel our task

```

The `execute()`, `repeat()`, and `cancel()` methods give us all of the flexibility we need to schedule repeating events in JavaScript. In addition to the `interval` property of the Task object, we can also find out whether a task is running or not (`running`) and how many times it has been called (`iterations`), for example.
One important thing to keep in mind is that all methods in the [js](https://docs.cycling74.com/reference/js/ "js") object (whether triggered by Max messages or scheduled internally through tasks) are executed at low priority in the Max scheduler. This means that, while they will always execute and send data to Max in the correct order, they cannot be relied on for critically accurate timing if the scheduler is overloaded with other actions.
Once we’ve defined our Task `tsk`, we trigger it through the `bang()` method to our [js](https://docs.cycling74.com/reference/js/ "js") object:
```
function bang()
{
    tsk .cancel(); // cancel the bounce, if it's going already
   count = 0; // reset the number of bounces
   decay = 1.0; // reset the initial decay
    tsk .interval = glob.starttime; // set the initial task interval
    tsk .repeat(); // start the bouncing
}

```

When any of our [js](https://docs.cycling74.com/reference/js/ "js") objects receive a `bang`, they cancel any previously scheduled `tsk` tasks, reset some variables that are relevant to the task function, set an initial timing interval for the task, and then start it going again.
Start a ‘bounce’ in the Tutorial patch by clicking the button at the top. Click the [message](https://docs.cycling74.com/reference/message/ "message") box labeled `stop`. The notes should cease. Our `stop()` function will cancel our previously scheduled task simply by calling the `cancel()` method to `tsk` :
```
function stop()
{
    tsk .cancel(); // cancel our task
}

```

## The Task at Hand
Our Task object, once set in motion by our `bang()` method, calls the function defined in its initial declaration.
Peruse the code for the mytask() function:
```
// mytask -- the scheduled task - output number and reschedule next task
function mytask()
{
   if(arguments.callee.task.interval>5) // keep bouncing
   {
      outlet(0, note); // send a note value
      decay = decay*Math.exp(++count*dcoeff); // increment the decay variable
      arguments.callee.task.interval=arguments.callee.task.interval*decay; // update the task interval
   }
   else // bounce interval is too small, so consider it 'floored'
   {
      arguments.callee.task.cancel(); // cancel the task
      outlet(1,  bang ); // send a  bang  out the right outlet to signify that we're done bouncing
   }
}

```

Unlike the other functions we’ve used in our JavaScript tutorials, we don’t intend our `mytask()` function to be triggered by a Max message from outside the [js](https://docs.cycling74.com/reference/js/ "js") object. By default, any declared function in a [js](https://docs.cycling74.com/reference/js/ "js") object will respond to an appropriately named message from the Max environment. Since we don’t want `mytask()` triggerable by a `mytask` message from our patcher, we place the following line of code after the function ends: mytask.local = 1;
This statement makes `mytask()`_local_ to the [js](https://docs.cycling74.com/reference/js/ "js") environment, and inaccessible from outside.
Our Task function accomplishes two things: it sends out an integer to Max (triggering a MIDI note), and increments its own timing interval so that the next run of `mytask()` will happen a little bit sooner. Outside of the task function, we can change our timing interval by setting the `interval` property to the task (e.g. `tsk`.interval = 250). Properties and methods of a Task object can be modified within the task function by referring to the Task as the callee, e.g.:
```
arguments.callee.task.interval=250; // adjust timing of task to 250
arguments.callee.task.cancel(); // have the task cancel itself

```

We use this reflexive capability to change our Task object’s timing interval from within the Task function. When the timing interval decreases to a suitably low value (5 milliseconds in our case), we also use this feature to have our Task function cancel the Task that called it in the first place.
## Using a Math Object
Look at the code for `mytask()` again, paying attention to the line that changes the decay value with every bounce:
```
decay = decay*Math.exp(++count*dcoeff); // increment decay variable

```

In addition to the objects that allow for interaction between JavaScript and Max (**Maxobj** , **Task**), JavaScript has a number of core objects that can be useful when writing programs for [js](https://docs.cycling74.com/reference/js/ "js"). The **Math** object has a large library of built-in properties and methods that allow you to perform commonly needed mathematical functions. In our code, we use the `exp()` method to the Math object, which returns the value of _**e**_ (the base of the natural logarithm: roughly `2.71828`) to the power of its argument (in this case, our decay coefficient multiplied by the next ball count). This is crucial to the modeling of the exponentially increasing rate of the bounce event.
The Math object in JavaScript is roughly analogous in features to the math library in C or the [expr](https://docs.cycling74.com/reference/expr/ "expr") object in Max (which is itself based on the C math library). A number of other predefined core objects (e.g. **Date** , **String**) provide similar extensions to the language that more-or-less match their C equivalents (e.g. time, string).
## Arguments to the [js](https://docs.cycling74.com/reference/js/ "js") Object
Two of our script’s variables (`dcoeff` and `note`) are determined by the arguments given to the [js](https://docs.cycling74.com/reference/js/ "js") object. These arguments are parsed in our global code block by checking the `jsarguments` property of our [js](https://docs.cycling74.com/reference/js/ "js") object:
```
if(jsarguments.length>1) // argument 0 is the name of the  js  file
{
   dcoeff = jsarguments[1];
}
if(jsarguments.length>2)
{
   note = jsarguments[2];
}

```

Note that argument `0` is the name of the JavaScript file (e.g. ‘globaltask.js’), so, realistically, we will usually start looking at the arguments starting at `1`. The above code checks to make sure that the arguments exist before we attempt to assign their values to variables.
## The **Global** Object
Close the [js](https://docs.cycling74.com/reference/js/ "js") object’s editor and return to the tutorial patch for a moment. In the lower-left hand corner, look at the [number](https://docs.cycling74.com/reference/number/ "number") box connected to the [message](https://docs.cycling74.com/reference/message/ "message") box containing the text `; bounce starttime $1`. Type `2000` into the [number](https://docs.cycling74.com/reference/number/ "number") box and enter the value. Send a bounce by clicking on the [button](https://docs.cycling74.com/reference/button/ "button") at the top. Notice that the timing between bounces in all the objects is wider than before. Try changing the [number](https://docs.cycling74.com/reference/number/ "number") box to a small value. The timing interval should start out quicker.
We would expect our [message](https://docs.cycling74.com/reference/message/ "message") box to have sent the message `starttime 2000` to a [receive](https://docs.cycling74.com/reference/receive/ "receive") object somewhere in our Max patch called `bounce`. In fact, it sets the `starttime` property of a Global object (assigned to respond to the name `bounce`) to `2000` within our [js](https://docs.cycling74.com/reference/js/ "js") objects. We accomplish this be declaring a Global object in our global code:
```
// Global (Max namespace) variables
glob = new Global(“bounce”);
glob.starttime = 500;

```

In our code, we’ve created a variable (`glob`) and assigned it to a new Global object. The argument to the global object (`"bounce"`) is the name in the Max namespace that will be tied to the object. Any message sent to `bounce` within Max will attempt to set properties of the Global object using that name. Note that internally, we refer to the Global object by a variable name of our choosing (`glob`), not by the symbol with which Max and our [js](https://docs.cycling74.com/reference/js/ "js") object communicate.
We’ve added a property (`starttime`) to our object simply by assigning it in our global block. Now, any message beginning with `starttime` sent to `bounce` in our Max patch will set that property to its arguments.
Furthermore, this object is truly global, in the sense that not only can Max set it from outside of a [js](https://docs.cycling74.com/reference/js/ "js") object, multiple [js](https://docs.cycling74.com/reference/js/ "js") objects share the specific instance of this object and its properties. You could use this feature to have multiple [js](https://docs.cycling74.com/reference/js/ "js") objects share information, as well as have Max broadcast information to multiple [js](https://docs.cycling74.com/reference/js/ "js") objects.
## Summary
JavaScript allows you to schedule events dynamically using the **Task** object. You create a Task and bind it to a function that gets called by the Task. You can activate and cancel the task and set the Task’s timing interval and how often it repeats. Furthermore, by using the `callee` property of the function called by the Task, you can set these things from within the scheduled event itself. All methods in [js](https://docs.cycling74.com/reference/js/ "js") objects (whether called internally or by Max messages) are executed at low priority in the scheduler.
JavaScript has a number of core objects that provide functionality for common programming routines that you may find necessary. The **Math** object, for example, gives you access to a variety of mathematical functions that you would find in the C math library or in the Max [expr](https://docs.cycling74.com/reference/expr/ "expr") object.
Arguments to the [js](https://docs.cycling74.com/reference/js/ "js") object are handled by the `jsarguments` property to the object. The object starts numbering its arguments at `0`, but the first argument to [js](https://docs.cycling74.com/reference/js/ "js") is the name of the source file it had loaded.
Global objects in JavaScript allow communication between [js](https://docs.cycling74.com/reference/js/ "js") objects, and allow for object properties to be set directly from the Max environment.
## Code Listing
```
// globaltask. js 
//
// generate a stream of numbers timed to an exponentially
// decaying time curve. arguments set the curve and the
// value to output.
//
// rld, 5.04
//
// inlets and outlets
inlets = 1;
outlets = 2;

// define global variables and set defaults
var  tsk  = new Task(mytask, this); // our main task
var count = 0;
var decay = 1.0;
// defaults for arguments
var dcoeff = -0.0002; // decay coefficient
var note = 60; // note to trigger upon bounce
// process arguments (decay coefficient, note to trigger)
if(jsarguments.length>1) // argument 0 is the name of the  js  file
{
   dcoeff = jsarguments[1];
}
if(jsarguments.length>2)
{
   note = jsarguments[2];
}
// Global (Max namespace) variables
glob = new Global(“bounce”);
glob.starttime = 500;

//  bang  -- start the task
function  bang ()
{
    tsk .cancel(); // cancel the bounce, if it's going already
   count = 0; // reset the number of bounces
   decay = 1.0; // reset the initial decay
    tsk .interval = glob.starttime; // set the initial task interval
    tsk .repeat(); // start the bouncing
}

// stop -- allow the user to stop the bouncing
function stop()
{
    tsk .cancel(); // cancel our task
}
// mytask -- the scheduled task - output number and reschedule next task
function mytask()
{
   if(arguments.callee.task.interval>5) // keep bouncing
   {
      outlet(0, note); // send a note value
      decay = decay*Math.exp(++count*dcoeff); // increment the decay variable
      arguments.callee.task.interval=arguments.callee.task.interval*decay; // update the task interval
   }
   else // bounce interval is too small, so consider it 'floored'
   {
      arguments.callee.task.cancel(); // cancel the task
      outlet(1,  bang ); // send a  bang  out the right outlet to signify that we're done bouncing
   }
}
mytask.local = 1; // prevent triggering the task directly from Max

```

## See Also
  * [js - Max JavaScript object](https://docs.cycling74.com/reference/js/)



Kind
    Tutorial 

Category
    JavaScript 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
