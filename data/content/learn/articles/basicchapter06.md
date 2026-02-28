---
description: Performing calculations
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/basicchapter06/
title: Simple Math
---

Download Series Content and Patchers
# Tutorial 6: Simple Math in Max
## Performing calculations
This tutorial covers the basic mathematical operations that are available with Max objects, and the process of connecting up several objects into a calculation chain. We will also cover the common operations of objects with multiple inlets, and some issues with numeric conversion.
Common math operations, such as addition and multiplication, are important for manipulating incoming data into a range and form that is useful for our patches. Additionally, dealing with the difference between integer and floating-point numbers is critical when working with many types of data such as MIDI, audio and serial information.
## Everybody loves Math
Look at the tutorial file 06mSimpleMath.maxpat. The top row of patches shows examples of the various simple mathematical operations that are available in Max. The left-most patch performs addition using the [+](https://docs.cycling74.com/reference/%2B/ "+") (_plus_) object. The [+](https://docs.cycling74.com/reference/%2B/ "+") object, like most math objects in Max, has two inlets – one for each operand. Numbers coming into the right inlet are stored, and added to numbers coming into the left inlet. If no number has yet come into the right inlet, the right operand is set to the object's _argument_ ; if no argument is supplied, the right operand defaults to `0`.
When we click on the [message](https://docs.cycling74.com/reference/message/ "message") box containing the number `2` (on the left), the result (which is displayed in the connected [number](https://docs.cycling74.com/reference/number/ "number") box) is revealed to be `2` as well; since no number has come into the right inlet, the current stored operand remains `0`. Clicking on the message box with the number `3` produces no output, but _stores_ the number `3` as the new right-hand operand. When we click on the `2` again, we see the additive result – `5` – displayed in the [number](https://docs.cycling74.com/reference/number/ "number") box.
The next patch uses an _argument_ to the [+](https://docs.cycling74.com/reference/%2B/ "+") object that sets an initial default value for the right-hand operand. Now, when we put a number into the [+](https://docs.cycling74.com/reference/%2B/ "+") object (using the top [number](https://docs.cycling74.com/reference/number/ "number") box), we see a result without having to send any number into the right inlet. Using default arguments for math operations is a common setup in many situations where you need to perform a constant mathematical operation (e.g. offsetting or scaling a number) on a stream of input values.
Next are the [-](https://docs.cycling74.com/reference/-/) (_minus_) and [*](https://docs.cycling74.com/reference/*/ "*") (_multiply_) objects, which perform subtraction and multiplication, respectively. Like the [+](https://docs.cycling74.com/reference/%2B/ "+") object, they have default operands of `0`, and accept stored values in their right inlet and produce results based on values coming in the left inlet. The _divide_ ([/](https://docs.cycling74.com/reference/%2F/ "/")) and _modulo_ ([%](https://docs.cycling74.com/reference/%25/ "%")) operations are also similar, but with one difference – in order to prevent unwanted "divide by zero" errors, their default right-hand operands are one (`1`) rather than zero.
## Inlets, Hot and Cold
As we’ve seen in the first set of math objects, some inlets cause an object to output a message, while others cause the object to simply store values. In fact, messages sent to _any_ of the inlets cause these objects to store values; the difference is that values coming in the left-most inlet have an implicit `bang` message attached to them - this forces the math object to output the result of the calculation once the value is received and stored. We can see this in action by attaching a `bang` object to a math object, and using it to explicitly force output.
The first patch in the second row is a simple addition patch, but with a [button](https://docs.cycling74.com/reference/button/ "button") connected to the left inlet. Sending numbers into the [+](https://docs.cycling74.com/reference/%2B/ "+") object performs the expected result: numbers in the right inlet are stored and used as a right-hand operand, while numbers in the left inlet are used as left-hand operands _and_ cause the object to output results. Clicking on the [button](https://docs.cycling74.com/reference/button/ "button") also produces a result: the addition is performed with the current set of operands, and the result is sent out of the outlet. _This is useful when you want to change the right-hand operand, but want output without having to resend the left-hand operand_. It is also a good example of the `bang` message performing its "do it!" function.
Inlets that cause an object to output messages are often called _hot_ inlets while inlets that only store information are called _cold_ inlets. It is a common practice, when a cold inlet needs to produce output, to apply a `bang` message (via a [button](https://docs.cycling74.com/reference/button/ "button") or [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object) into the left-most inlet to force output.
## Type conversions through arguments
The next two parts of the patcher show what appear to be equivalent operations using the [+](https://docs.cycling74.com/reference/%2B/ "+") object. Both of them purport to add together the numbers `2.5` (in the right inlet) and `12.75` (in the left). Try them both out (remember we need to click the right-hand message first to set the right operand).
The result of adding `12.75` and `2.5` should be `15.25`. But between the two [+](https://docs.cycling74.com/reference/%2B/ "+") objects, only the right-hand one produces the correct result. The left-hand [+](https://docs.cycling74.com/reference/%2B/ "+") outputs `14`. Why?
Like many programming languages, Max has different _types_ of numeric data, and operations on that data can be done using integer or floating-point mathematics. By default, all of the objects that perform math operations in Max use integer-based arithmetic. When floating-point numbers are received by a math object in "integer" mode, they are _truncated_ to integers before being used. Thus, `12.75` becomes `12`, and `2.5` is converted to `2` – which adds up to `14`. In order to set a math object to use to floating-point arithmetic, _we need to provide an argument that is floating-point_. The right-hand patch does just that – it uses a `0.` argument to inform the [+](https://docs.cycling74.com/reference/%2B/ "+") object that we want to perform floating-point arithmetic, and the addition results in the `15.25` value that we were expecting.
## Forcing a calculation
The final two patches in the second row show a simple mechanism for triggering output from the [+](https://docs.cycling74.com/reference/%2B/ "+") object, regardless of which inlet receives messages. The left inlet is fed directly by a [number](https://docs.cycling74.com/reference/number/ "number") box; since left inlets are already hot, they need no further attention. However, in order for the right inlet to produce output, we have to send a `bang` into the left inlet _after_ the right inlet has received input. This is a perfect application for the [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object, which is used to manage this function.
In both cases, the [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object (abbreviated to [t](https://docs.cycling74.com/reference/trigger/)) has two outlets (defined by its arguments): the right outlet is type-specific (`i` for integer, `f` for float), while the left (`b`) sends out a `bang`. When a number is entered into the object, [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") processes the arguments in a _right-to-left_ order, first sending the numeric value (integer or floating-point) into the right inlet of the [+](https://docs.cycling74.com/reference/%2B/ "+") object. Then, a `bang` is sent to the left inlet of [+](https://docs.cycling74.com/reference/%2B/ "+"), forcing calculation and output to the [number](https://docs.cycling74.com/reference/number/ "number") box below. In this way, we can force both inlets of the [+](https://docs.cycling74.com/reference/%2B/ "+") object to behave as though they are "hot", and receive output regardless of which inlet is sent messages.
## Using cold inlets for recursion
At the bottom of the tutorial file is a curious little patch that has the result of a [+](https://docs.cycling74.com/reference/%2B/ "+") object _feeding back into itself_. You can see what is happening by clicking on the top [number](https://docs.cycling74.com/reference/number/ "number") box, entering a number, and then entering more numbers after that (you can also drag the number box to scroll values). As you enter numbers, the result keeps accumulating.
This is a case where we are taking advantage of the "cold" (right-hand) inlet of the [+](https://docs.cycling74.com/reference/%2B/ "+") to change its right operand _based on the previous operation's output_. In this case, the result of the addition is fed back into the right-hand inlet, where it is stored as the right operand for the next addition operation. This results in an accumulation of the output, which can be handy for tracking a running total of incoming values. These types of recursive operations are useful for making counters, smoothing algorithms, and pieces of code where the system's behavior is dependent on previous outputs of the system.
## Cascading math objects
All of the above examples have been pretty simple – they’ve been simple math operations with a simple result. However, you can chain several of these operations together to create more complex equation.
For example, let's say we wanted to make a Max patcher for converting temperatures: specifically, converting Fahrenheit to Celsius. The formula for this conversion is:
```
°C = (°F – 32) * (5/9)

```

From an object standpoint, it might be easier to simplify this to:
```
°C = (((°F – 32) * 5) / 9)

```

We can produce this output by using the [-](https://docs.cycling74.com/reference/-/), [*](https://docs.cycling74.com/reference/*/ "*"), and [/](https://docs.cycling74.com/reference/%2F/ "/") objects chained together. Unlock the patch, and begin by using a [number](https://docs.cycling74.com/reference/number/ "number") box for the Fahrenheit (°F) input. Connect this to a [-](https://docs.cycling74.com/reference/-/) object with an argument of `32` as the default right-hand operand. Connect the output of the [-](https://docs.cycling74.com/reference/-/) object to a [*](https://docs.cycling74.com/reference/*/ "*") object with `5` as an argument, and connect it to a [/](https://docs.cycling74.com/reference/%2F/ "/") object with `9.` as the argument (note the decimal point). Finally, connect the output of the [/](https://docs.cycling74.com/reference/%2F/ "/") object to float [number](https://docs.cycling74.com/reference/number/ "number") box to see the result of the Fahrenheit to Celsius conversion.
## Summary
The mathematical objects, used either singly or in a sequence, provide the tools necessary for manipulating numeric input in many ways. The math objects provide both hot and cold inlets, but simple patching operations can be used to force output on cold inlets. Math objects, by default, perform their computations using integer arithmetic; an argument with a decimal point can be provided to tell the object to perform arithmetic using floating-point numbers.
## See Also
  * [+ - Arithmetic operator (plus)](https://docs.cycling74.com/reference/+/)
  * [- - Arithmetic operator (minus)](https://docs.cycling74.com/reference/-/)
  * [* - Arithmetic operator (times)](https://docs.cycling74.com/reference/*/)
  * [/ - Arithmetic operator (divided by)](https://docs.cycling74.com/reference/)
  * [% - Arithmetic operator (modulo)](https://docs.cycling74.com/reference/%/)
  * [trigger - Sends its input to many places, in right-to-left order](https://docs.cycling74.com/reference/trigger/)



Kind
    Tutorial 

Category
    Max 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
