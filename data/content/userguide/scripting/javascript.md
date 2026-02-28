---
description: Extend the functionality of Max by writing JavaScript code
group: Scripting
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/javascript/
title: JavaScript
---

# JavaScript
Using **JavaScript** , you can script the behavior of Max by writing text code. Most of the things that you could do with a [Max external](https://docs.cycling74.com/userguide/externals/), you can also do with a JavaScript object.
  * Receive messages from inlets
  * Manage internal state
  * Send messages to outlets
  * Perform custom drawing and handle mouse events
  * Schedule events
  * Query the state of the patcher
  * Other functions exposed through the [JavaScript API](https://docs.cycling74.com/apiref/js/)

![](https://docs.cycling74.com/images/b4d56c53771fcb463af95b13dc75118a_547.webp)
## JavaScript Objects
The JavaScript family of objects [v8](https://docs.cycling74.com/reference/v8/ "v8") and [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") ([js](https://docs.cycling74.com/reference/js/ "js") and [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") using the older JavaScript engine) let you define a custom Max object using JavaScript. The JavaScript code that you write to define the behavior of your object can be loaded as a separate `.js` file, or embedded in your patcher.
Max is in the process of updating its JavaScript engine, and so there are currently two engines available in Max. There is an older JavaScript engine, running version 1.8.5, as well as a newer v8 engine. The older version is only maintained for backwards compatibility, and in the near future the v8 engine will be a drop-in replacement for the older engine. Developers using the old engine through the [js](https://docs.cycling74.com/reference/js/ "js") object don't need to take any action—when the old engine is replaced the [js](https://docs.cycling74.com/reference/js/ "js") object will also use the v8 engine. If you're writing new JavaScript code, use the [v8](https://docs.cycling74.com/reference/v8/ "v8") and [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") objects to take advantage of the new engine.
There are two JavaScript objects: [v8](https://docs.cycling74.com/reference/v8/ "v8") and [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui"). The main difference between the two is that [v8](https://docs.cycling74.com/reference/v8/ "v8") is a simple Max object, while [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") provides a drawing and interaction context. Use [v8](https://docs.cycling74.com/reference/v8/ "v8") to implement a generic Max object using JavaScript, and use [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") to implement a user interface object. You can also replace the default drawing behavior of any UI object using the `@jspainter` attribute. See [**Custom UI Objects**](https://docs.cycling74.com/userguide/custom_ui_objects/) for a full description of working with `@jspainter` and [jsui](https://docs.cycling74.com/reference/jsui/ "jsui").
Max also provides an object called [node.script](https://docs.cycling74.com/reference/node.script "node.script"), which lets you start and interact with [Node](https://nodejs.org) processes from Max. Node uses JavaScript, but code running in [node.script](https://docs.cycling74.com/reference/node.script "node.script") runs in a separate process.
## jsthis
Before calling into your JavaScript code, Max binds an instance of [jsthis](https://docs.cycling74.com/apiref/js/jsthis/) to `this`. Doing so puts a number of Max-specific functions into scope. Using `this` is optional when referring to these functions.
```
function bang() {
    // The `post` function is a method of jsthis
    post("hi\n");

    // Using "this" is optional, but makes explicit the reference
    // to the bound instance of jsthis
    this.post("nice to see you\n");
}

```

See the [JS API Docs](https://docs.cycling74.com/apiref/js/jsthis/) for a full list.
### Number of Inlets and Outlets
Set the number of inlets and outlets on your JavaScript object by setting the value of `inlets` and `outlets` on `jsthis`.
```
inlets = 3; // object will have three intles
outlets = 2; // object will have two outlets

function bang() {
    outlet(1, "hi"); // send "hi" out the second outlet.
}

```

## Arguments
Arguments supplied to the [js](https://docs.cycling74.com/reference/js/ "js") or [v8](https://docs.cycling74.com/reference/v8/ "v8") object after the filename will be passed to the JavaScript code as arguments. These will be available in a `jsthis` property called `jsarguments`.
```
// The first argument will always be the name of the file
const filename = jsarguments[0];

const argumentsLength = jsarguments.length;

// Get an array of arguments supplied by the user
const userArguments = jsarguments.slice(1, argumentsLength);

// Fancy way to do the same thing with array destructuring
const [filename1, ...userArguments1] = jsarguments;

```

With [jsui](https://docs.cycling74.com/reference/jsui/ "jsui") and [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui"), use the `@arguments` attribute to specify the argumetns to your JavaScript code.
## Input
A message received in the inlet of a [v8](https://docs.cycling74.com/reference/v8/ "v8") or [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") object will invoke a function with the same name. Arguments following the message name will be passed to the JavaScript function. This method would print "1, 2, 3" in response to the message `foo 1 2 3`.
```
function foo(a, b, c) {
    post(a, b, c);
}

```

With `v8` you can use destructuring assignment to get the arguments to the function as an array.
```
function foo(...args) {
    post(args.length);
}

```

You can even get the first argument as a single value and the rest as an array.
```
function foo(first, ...rest) {
    post(first, ...rest);
};

```

## Special Functions
You can define a number of functions with special names to respond to specific hooks from Max.
### bang
Invoked in response to a bang message.
### msg_int, msg_float
Invoked in response to an integer or a float, respectively.
```
function msg_int(a) {
    post(`received an int: ${a}\n`);
}

function msg_float(a) {
    post(`received a float: ${a}\n`);
}

```

If you define only `msg_int`, any float received will be truncated and passed to `msg_int`. Similarly, if only `msg_float` exists, an int received will be passed to the `msg_float` function.
### list
Invoked in response to a list (a message with more than one element that starts with a number).
```
function list(...elements) {
    post(`elements length: ${elements.length}\n`);
    post(`first element: ${elements[0]}\n`);
}

```

### anything
You can define an `anything` function that will run if no specific function is found to match the message symbol received by the [v8](https://docs.cycling74.com/reference/v8/ "v8") or [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") object. If you want to know the name of the message that invoked the function, use the `messagename` property. If you want to know what inlet received the message, use the `inlet` property.
```
function anything(...args) {
    post(`message: ${this.messagename}\n`);
    post(`inlet: ${this.inlet}\n`);
    post(`arguments: ${args}\n`);
}

```

### loadbang
Invoked when the patcher file containing the [v8](https://docs.cycling74.com/reference/v8/ "v8") or [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") object is loaded. This function will not be called when you instantiate a new [v8](https://docs.cycling74.com/reference/v8/ "v8") or [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") object and add it to a patcher; it will only be called when a pre-existing patcher file containing a JavaScript object is loaded.
```
function loadbang() {
    post("loadbang\n");
}

```

### getvalueof
Defining a `getvalueof` function lets your JavaScript object participate in the [**pattr**](https://docs.cycling74.com/userguide/pattr/) system, enabling Max to save the state of your JavaScript object using [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") and [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/ "pattrstorage"). The return value of `getvalueof` can be a `number`, a `string`, an `Array` of `number` and `string`, or a Max [Dict](https://docs.cycling74.com/apiref/js/Dict/).
```
let myvalue = 0.25
function getvalueof() {
    return myvalue;
}

```

### setvalueof
If you've defined a `getvalueof` function, you can define a `setvalueof` function to enable [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") and related object to restore the state of your JavaScript object from a preset. Like the return value of `getvalueof`, the arguments to `setvalueof` can be a `number`, a `string`, an `Array` of `number` and `string`, or a Max [Dict](https://docs.cycling74.com/apiref/js/Dict/).
```
let myvalue;
function setvalueof(v) {
    myvalue = v;
}

```

### save
Defining a function called `save` allows your script to embed state in a patcher file containing your JavaScript object. Max will automatically restore your saved state when the patcher is loaded.
Saving your state consists of storing a set of messages that your script will receive shortly after the JavaScript object is recreated. These messages are stored using a special global function called `embedmessage` that only works inside the `save` function.
Suppose you have a function `cowbells` that sets the number of cowbells your object currently has:
```
let numcowbells = 1
function cowbells(a) {
    numcowbells = a
}

```

When the patcher containing the JavaScript object is saved, you would like to preserve the current number of cowbells, so you define a `save` function as follows:
```
function save() {
    embedmessage("cowbells", numcowbells)
}

```

The first argument to embedmessage is the name of the function you want to call as a string. Additional arguments to embedmessage supply the arguments to this function. These additional arguments will typically be the values of the state you want to save. For each call to `embedmessage`, Max will call that function with the provided arguments as it restores the state of your JavaScript object.
### notifydeleted
The `notifydeleted` method is called when the JavaScript object is freed.
### Reserved names
The [v8](https://docs.cycling74.com/reference/v8/ "v8") and [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui") objects already do something in response to the `compile` message. So, if you define a function named "compile" in your JavaScript code, there will be no way to call that function from Max. However, you can still call the function locally, from your own JavaScript code.
## Output
Call the `jsthis` method `outlet` to send messages out of a given outlet.
```
function bang() {
    outlet(0, "bang");
}

```

## Global Code and Initialization
When the JavaScript object is loaded, Max will execute the script once from beginning to end. Variables defined in the global scope will persist through the life of the object, and you can use these to hold on to internal state.
```
let counter = 0;

function count() {
    post(`count: ${++counter}`);
}

```

In fact, Max will attach global variables to the `this` context when executing functions from an inlet. The above code is equivalent to the following.
```
this.counter = 0;

function count() {
    this.counter++;
    post(`count: ${this.counter}`);
}

```

During the execution of global code, the JavaScript object is still being initialized. The object does not have any outlets, nor is it yet part of any patcher. If you want to send messages to an outlet immediately after your JavaScript object is created, define a `loadbang` function.
## require
Use `require` to include code from other JavaScript files.
```
const lib = require("my-lib.js");

function call(a) {
    const computedValue = lib.compute(a);
    outlet(0, computedValue);
}

```

The included file should be a CommonJS module. To export functions and variables, it should set the properties of `exports` or else replace `module.exports` with an object containing exported properties.
```
// An example implementation of my-lib
function compute(a) {
    return a + 10;
}

module.exports = {
    compute: compute
};

```

## Private (Local) Functions
If you want to use a function locally, but you don't want it to be called from Max, you can set its `local` property to `1`. For example, suppose the function `foo` is not something we wish to expose to the outside world.
```
foo.local = 1
function foo() {
    post("what does Pd *really* stand for?");
}

```

Now, when we send the message `foo` to the JavaScript object, we see the following error in the Max window:
```
error: js: function foo is private

```

## Available APIs
Since the Max JavaScript engine is not running inside of a web browser, certain APIs may not be available.
  * JSON serialization with `JSON.stringify` and `JSON.parse` are available.
  * Timing functions like `setImmediate` and `setTimeout` are not available. Use [**Task**](https://docs.cycling74.com/apiref/js/task/) instead.
  * There is no DOM, so document methods like `document.getElementById` are not available.


## JavaScript, Threading, and Priority
Max schedules events using a high priority thread for events that require high timing accuracy, like MIDI, and a low priority thread for long-running operations like decompressing video. The JavaScript engine in Max always executes code in the [low priority thread](https://docs.cycling74.com/userguide/scheduler/#high-priority-and-low-priority). That means that if a JavaScript object receives a message from a MIDI object, or from any other object that schedules events on the high priority queue, that event will be deferred to the low priority queue.
