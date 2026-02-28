---
description: Using JavaScript in a patcher
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/javascriptchapter01/
title: Basic JavaScripting
---

Download Series Content and Patchers
# JavaScript Tutorial 1: Basic JavaScript
## Introduction
This tutorial introduces the use of **JavaScript** within a Max patcher. JavaScript is an object-oriented scripting language originally developed to facilitate the use of embedded software in websites. The Max [js](https://docs.cycling74.com/reference/js/ "js") object allows you to use JavaScript as a language _within_ the Max environment, writing program code for your own object without the need for external developer tools (compilers, debuggers, etc.). In this tutorial, we’ll show a simple example of how you would use the [js](https://docs.cycling74.com/reference/js/ "js") object to create an object in JavaScript to respond to simple numerical input from Max and return a number to the patcher.
The [js](https://docs.cycling74.com/reference/js/ "js") object gives Max users the powerful ability to write an object using an embedded programming language directly within Max. In a nutshell, it allows us to: • Design and program procedural operations that may be difficult or impossible to implement using Max objects by themselves. These may include operations that require recursion or respond to messages with an unknown number of arguments, to give two examples. • Create objects that respond to customizable messages and rely on their own internal data structures. • Schedule timed events in response to messages. • Manage global variables for use among multiple [js](https://docs.cycling74.com/reference/js/ "js") objects or between [js](https://docs.cycling74.com/reference/js/ "js") objects and the Max patcher. • Interface to Max’s powerful scripting architecture. • Access the file system of your computer to look for files by name and types.
In order to develop a Max object using a programming language other than Max itself (i.e. subpatchers) you have several options. You can develop your own external object in C using the Max Software Development Kit. You can also develop objects in Java using the mxj object. Both of these solutions require that the code you write be compiled into a format that Max can execute (either directly by loading a shared library or by executing Java code through the Java Virtual Machine). With the [js](https://docs.cycling74.com/reference/js/ "js") object (and its graphical cousin, [jsui](https://docs.cycling74.com/reference/jsui/ "jsui")), code is evaluated as a script directly by the computer as you run your patch, allowing for more immediate feedback on how the mini-program written for your [js](https://docs.cycling74.com/reference/js/ "js") object will behave. That isn’t to say that [js](https://docs.cycling74.com/reference/js/ "js") doesn’t check for mistakes first; it does, and we’ll look at some of the ways in which the [js](https://docs.cycling74.com/reference/js/ "js") object can help you catch mistakes in your program.
The Max [js](https://docs.cycling74.com/reference/js/ "js") object uses version 1.8.5 of the JavaScript language, a Mozilla specific superset of ECMAScript 5. While we don’t presume specific knowledge of JavaScript in these tutorials, the better you understand the language, the easier it will be for you to develop code. An online JavaScript reference can be found here:
<https://developer.mozilla.org/en/JavaScript/Reference>
It's worth noting that there are many variations on the JavaScript language, as well as a number of extensions to the language specifically designed for its use with web browsers. The Max [js](https://docs.cycling74.com/reference/js/ "js") object supports only the core JavaScript language (as outlined at the URL above) as well as some extensions added to the language to support interfacing with Max.
## JavaScript in Action
Take a look at the tutorial patcher. If you want to hear the MIDI playback from the patch, select a valid MIDI output device by double-clicking on [noteout](https://docs.cycling74.com/reference/noteout/ "noteout") object on the lower-left of the patcher.
Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") at the top of the patch to start the [metro](https://docs.cycling74.com/reference/metro/ "metro") object. The [float](https://docs.cycling74.com/reference/float/ "float") object sends a value into the [js](https://docs.cycling74.com/reference/js/ "js") object at every tick of the [metro](https://docs.cycling74.com/reference/metro/ "metro"). Slowly increment the floating-point [number](https://docs.cycling74.com/reference/number/ "number") box attached to the right inlet of the [float](https://docs.cycling74.com/reference/float/ "float") object. The output of the [js](https://docs.cycling74.com/reference/js/ "js") object will change in response. The output number is displayed using the [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") object in the patch and generates MIDI notes.
As you increase the value going into the [js](https://docs.cycling74.com/reference/js/ "js") object above `3.0`, the value generated by our [js](https://docs.cycling74.com/reference/js/ "js") object will begin to _oscillate_ between a high and a low value. At higher values (e.g. above `3.5`), the output of will become chaotic.
The [js](https://docs.cycling74.com/reference/js/ "js") object in this patch simulates a simple chaotic function called the _logistic population equation_. The basic formula for the function is: 
```
f(x) = rx(1-x)

```

where `r` is the current input value, and `x` is the previous output value.
Double-click the [js](https://docs.cycling74.com/reference/js/ "js") object in the tutorial patch. A text editor will appear, containing the source code for the [js](https://docs.cycling74.com/reference/js/ "js") object in the patcher. This code is saved as a file called ‘popu.js’ located in the same folder as the tutorial patch.
The Max [js](https://docs.cycling74.com/reference/js/ "js") object allows you to edit JavaScript code directly within Max through a basic text editor (the same text editor, in fact, that you use when editing the contents of a [coll](https://docs.cycling74.com/reference/coll/ "coll") or [text](https://docs.cycling74.com/reference/text/ "text") object). The source code that the [js](https://docs.cycling74.com/reference/js/ "js") object loads is determined by the first argument to the object, which specifies a text file in the Max search path. If you don’t give [js](https://docs.cycling74.com/reference/js/ "js") an argument, you can still write a JavaScript program from scratch in the editor, but you’ll have to save the file in order to use it.
## The Global Code
When you open the [js](https://docs.cycling74.com/reference/js/ "js") object’s editor you’ll see some JavaScript code. The code begins with a comment block that tells us the name of the file, what it does, and who wrote it. The [js](https://docs.cycling74.com/reference/js/ "js") object ignores these lines because they are prefaced with a double slash (‘//’), commonly used in C++ (and other programming languages) to define a comment. C-style comments (‘/*’ to start, and ‘*/’ to end) are also allowed in JavaScript.
The programming after the initial comment block defines some global code for the [js](https://docs.cycling74.com/reference/js/ "js") object. This is code that will let us define variables and run any part of the program we need to execute before anything happens to the object within the Max environment. In our example, we use the global code to tell Max how many inlets and outlets we need for our [js](https://docs.cycling74.com/reference/js/ "js") object and to define and initialize a variable (called `x`):
```
// inlets and outlets
inlets = 1;
outlets = 1;
// global variables
var x = 0.66;

```

The keywords _inlets_ and _outlets_ tell Max how many of each we’ll need our [js](https://docs.cycling74.com/reference/js/ "js") object to have. The object box will update when these variables are changed.
The _var_ keyword tells JavaScript that the label following it is to be declared as a _variable_ , which we then assign to any value either in the declaration itself (as we do here, by saying that `x` equals `0.66`) or later on in the code. Our new variable, `x`, is _global_ in scope; we’ll investigate exactly what that means later on.
In order to make any changes in our JavaScript code permanent, we need to save the code in the text editor. When you save changes (by selecting **Save** from the **File** menu with the text editor in the front), Max will tell you that it has updated the [js](https://docs.cycling74.com/reference/js/ "js") object, and will report any problems it may have had with your code.
Type the following line underneath the ‘outlets = 1;’ statement in the code:
```
post("Hi There!!!");

```

Save the code in the text editor. The Max Console should have printed the following:
```
js • Hi There!!!

```

The message posted in the Max Consle shows the output from the `post()` statement we put in. The `post()` statement prints its arguments into the Max Console, letting you do exactly what the [print](https://docs.cycling74.com/reference/print/ "print") object does from within [js](https://docs.cycling74.com/reference/js/ "js").
Add the following line right underneath where we initialize x to equal `0.66` :
```
post(x);

```

When we save the code, our Max Console now tells us:
```
js • Hi There!!! 0.66

```

If you give `post()` a text string (enclosed in double-quotes) it will print it. Other letters are interpreted as variable names. In this case, we asked [js](https://docs.cycling74.com/reference/js/ "js") to tell us the value of the variable `x`, which we had initialized on the previous line to `0.66`. Note that `post()` does not put a carriage return at the end of the line; to do this, we can place a `post()` statement with no arguments.
Add this line somewhere in between the two `post()` statements we’ve added:
```
post();

```

Our Max Console now tells us this when we save the code:
```
js • Hi There!!!
0.66

```

## Handling Mistakes
Remove the closing parenthesis (‘)’) from any of the `post()` statements we’ve added so far. Save the JavaScript code. The Max Console should print an error:
```
js • [popu.js] Javascript SyntaxError: syntax error, line 15
  source line: post(;

```

This tells us that we’ve made a type of mistake called a _syntax error_. This means that we wrote something illegal from the point of view of JavaScript syntax; in this case, we broke the rule that says that parentheses must be balanced. Mismatched parentheses, brackets, and braces are common causes of syntax errors. Helpfully, [js](https://docs.cycling74.com/reference/js/ "js") attempts to isolate which line the error occurred on (the line cited to you may be slightly different, depending on where you placed your `post()` statements).
Go to the offending line in your JavaScript code and close the parentheses correctly. When you save the code, all should be well again.
Misspellings are another common cause of mistakes in JavaScript. Rewrite your `post()` statement so that the word ‘post’ is spelled wrong (feel free to be creative here). Save your script. Something like this will appear:
```
js • Hi There!!!
js • [popu.js] Javascript ReferenceError: pst is not defined, line 15
js • error axlling function bang [popu.js]

```

A reference error means that we told JavaScript to execute a command that it simply didn’t understand. While `post()` is in its vocabulary of legitimate commands, `pst()` is not.
Note that JavaScript stopped executing our global code _at the point where the error occurred_. In the case just cited, the words ‘Hi There!!!’ were printed in the Max Console, but the value of `x` (`0.66`) was not. This gives us an important clue as to where the error lies (i.e. somewhere between the two). Using `post()` statements liberally in the development phase of your [js](https://docs.cycling74.com/reference/js/ "js") code is just as important as using [print](https://docs.cycling74.com/reference/print/ "print") objects and watchpoints for debugging in Max. You can always take them out later.
Correct your spelling and save your code. Let’s move on to the rest of the script.
## Defining Functions
Max objects interface with one another through the use of _methods_ , which are routines of code that are executed in response to messages received at the inlets of the object. In JavaScript, these methods are defined as _functions_ within our code, each of which responds to a different type of incoming Max message. In our example [js](https://docs.cycling74.com/reference/js/ "js") object, we have two functions defined. These functions (`msg_float()` and `bang()`) contain the code that [js](https://docs.cycling74.com/reference/js/ "js") executes when our object receives in its inlet a floating-point number and a `bang`, respectively.
Take a look at the `bang()` function first. The code looks like this:
```
function bang()
{
   post(“the current population is”);
   post(x);
   post();
}

```

This function tells [js](https://docs.cycling74.com/reference/js/ "js") what to do if we send it a `bang` from our Max patch. It will print out the current value of `x` in the Max Console with an explanatory preface. The `post()` statement at the end of the function tells Max to put a carriage return in the Max Console so that the next message printed there will begin on a new line. Note that our function is enclosed in curly braces. Removing one of these braces will result in a syntax error.
In the tutorial patch, click on the [button](https://docs.cycling74.com/reference/button/ "button") object connected to the [js](https://docs.cycling74.com/reference/js/ "js") object. Our `bang()` function should be working correctly. Look at the msg_float() function. Here is the code:
```
function msg_float(r)
{
   x = r*x*(1.-x);
   outlet(0, x);
}

```

Our `msg_float()` function executes the most important part of our JavaScript code, which is to run a single iteration of our cool formula. Note that, unlike our `bang()` function, our `msg_float()` function has an argument (stated within the parentheses as `r`). This argument tells the [js](https://docs.cycling74.com/reference/js/ "js") object to assign the floating-point value coming into our object’s inlet to the variable `r`. We can then use this value in the rest of the function.
Generally speaking, the name of the function in JavaScript will correspond directly to the name of the _message_ that you want to call it. For example, we respond to a `bang` message with the `bang()` function in our [js](https://docs.cycling74.com/reference/js/ "js") object. A function called `beep()` would respond to a Max message that began with the word `beep`. Since _float_ and _int_ are reserved words in JavaScript, however, we use `msg_float()` and `msg_int()`, respectively, to define the functions which respond to floats and ints.
The main body of our `msg_float()` function sets `x` to the result of the multiplication of `r` (the value coming in the inlet), the old value of `x`, and the old value of `x` subtracted from `1.0`. This statement:
```
x = r*x*(1.-x);

```

is an example of a powerful feature of using an embedded programming language within Max. To accomplish this with the [expr](https://docs.cycling74.com/reference/expr/ "expr") object, for example, we would have to take the output of the object and feed it back around to an inlet in such a way as to prevent a feedback loop in Max, probably through the use of a [number](https://docs.cycling74.com/reference/number/ "number") box.
Double-click the [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") called `done_with_expr` to see how you would do this using normal Max objects. Note that because the [expr](https://docs.cycling74.com/reference/expr/ "expr") object has no knowledge of its previous output value, we have to store it manually and enter it again using a second inlet to the object.
The second line of code in our `msg_float()` function takes our new value of `x` and sends it out the [js](https://docs.cycling74.com/reference/js/ "js") object’s outlet to Max. The `outlet()` function takes as its arguments the number of the outlet to use and the information to send out. The outlet numbering starts at `0` for the leftmost (and, in our case, only) outlet.
Try running the patch again, knowing how the code works. See if you can work out at what point the equation becomes chaotic, and why.
## Variable Scope
The key to the success of our JavaScript code resides in the use of `x` as a _global_ variable. JavaScript, like many scripting languages, will dynamically allocate variables as you use them, allowing you to use new variable names as you go without having to predefine them all ahead of time. These dynamic variables, however, are _local_ to the functions within which they are used. For example, if we had a variable `i` in our `msg_float()` function, our `bang()` function would not be able to use it. Consequently, we could use `i` as a variable in both functions independently of one another. Because we explicitly defined `x` as a variable in our global code, both `msg_float()` (which evaluates `x`, sets it to a new value, and sends it out to our patch) and `bang()` (which prints the current value of `x` in the Max Console) are talking about the same thing when they refer to `x`.
Comment out the line:
```
var x = 0.66;

```

by placing two slashes (‘//’) at the beginning of it. Save your script, and either recreate the [js](https://docs.cycling74.com/reference/js/ "js") object or reopen the tutorial patch. Try to run the patch.
With `x` undefined, our [js](https://docs.cycling74.com/reference/js/ "js") object reports reference errors when you send it a float or a `bang`. This is because it is trying to access a variable that has never been initialized. We could remove these errors by setting `x` to some value within each of our functions, but we would then be using `x` locally. Not only would this prevent us from sharing the value of `x` between our two functions, it would also reinitialize `x` every time we sent a float into [js](https://docs.cycling74.com/reference/js/ "js"), preventing our object from maintaining `x` over multiple iterations of the function.
Uncomment the variable declaration for x. All should be well again when you save your script.
## Summary
The [js](https://docs.cycling74.com/reference/js/ "js") object is a powerful tool that lets you write code using a standard programming language within Max. You define inlets, outlets, and global variables in the global code section of the script (which resides outside of any specific function). Methods that respond to particular messages (floats, `bang` messages, etc.) are written as functions below the global code, and are executed in response to the relevant messages from the Max environment. You can use the `post()` function to print information in the Max Console (much as you’d use the print object in a patch), and you can use the `outlet()` function to send messages out of your [js](https://docs.cycling74.com/reference/js/ "js") object back to the Max patcher containing it. You can write JavaScript code directly into the text editor for the [js](https://docs.cycling74.com/reference/js/ "js") object; when you save a modified script, the [js](https://docs.cycling74.com/reference/js/ "js") object will scan your code for programming mistakes such as syntax and reference errors, allowing you to program and debug your code from within Max.
## Code Listing
```
// popu.js
//
// simulates the logistic population equation:
// f(x) = rx(1-x)
//
// input is r. output is current x.
//
// rld, 5.04
//
// inlets and outlets
inlets = 1;
outlets = 1;
// global variables
var x = 0.66;
// float -- run the equation once
function msg_float(r)
{
   x = r*x*(1.-x);
   outlet(0, x);
}
// bang -- post the current population to the max window
function bang()
{
   post(“the current population is”);
   post(x);
   post();
}

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
