---
description: Thebangmessage
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/basicchapter02/
title: Bang!
---

Download Series Content and Patchers
# Tutorial 2: Bang!
## The `bang` message
In this tutorial, we will work with the `bang` message as a way to follow messages through the connections in a Max patcher.
This simple patcher will let us look at how to generate messages in Max, and how these messages execute through a patcher in a pre-defined order.
## Looking around
Take a look at the patcher `02mBang`. Click on the Max console icon in the right patcher window toolbar to open the sidebar. The left side of the patcher window has a very simple patch, with a [button](https://docs.cycling74.com/reference/button/ "button") UI object connected to a [print](https://docs.cycling74.com/reference/print/ "print") object. If you click on the button marked by the [comment](https://docs.cycling74.com/reference/comment/ "comment"), "Click me!", you will see that the Max Console displays a "bang" message – the output from the button.
The `bang` message has a specific use within Max – it's the message that tells many objects to _do that thing you do_. As a result, sending the bang message to other objects will normally cause them to send messages from their outlets. In the second part of the patcher (to the right), there is a [button](https://docs.cycling74.com/reference/button/ "button") (labeled "Now click me!") connected to a [message](https://docs.cycling74.com/reference/message/ "message") box (with the message `Gotcha!`), which is subsequently connected to a [print](https://docs.cycling74.com/reference/print/ "print") object. If we click on the message box, we can see the "Gotcha!" message sent to the Max Console – just like in the previous Tutorial. Now, click on the attached button object. We see the same "Gotcha!" message appear in the Max Console. How did that happen?
Let’s follow the messages. First, clicking on the [button](https://docs.cycling74.com/reference/button/ "button") object sends a `bang` message from its outlet. This message follows the patch cord to the inlet of the [message](https://docs.cycling74.com/reference/message/ "message") box. When the message box receives the bang message, it performs its task – it sends out its message. Hence, the "Gotcha!" message is sent from the message box outlet to the print object, where it is printed to the Max Console.
Most Max objects (including the [message](https://docs.cycling74.com/reference/message/ "message") box and [button](https://docs.cycling74.com/reference/button/ "button") ) will interpret a `bang` as an instruction to perform their main task using whatever information they have available. We'll see in subsequent tutorials how this plays out with objects that manipulate numbers and other items of data in the Max universe, but for now it's worth observing that since the primary function of the message box is to construct and pass messages, sending a bang to _any_ message box will cause that object to output whatever message is stored in it.
## Following messages through connections
The `bang` message is not only useful for triggering [message](https://docs.cycling74.com/reference/message/ "message") boxes – as we mentioned above, it can act as a trigger for many other objects as well. Click on the [button](https://docs.cycling74.com/reference/button/ "button") labeled "Click for one." It is connected to a second button that is triggered by a bang message, which then sends its message (again bang) to the [print](https://docs.cycling74.com/reference/print/ "print") object. Note that this print object has an _argument_ after it ("one"). If you look at the Max Console, you will see that instead of the word "print" appearing in the _object_ column, the argument to the print object appears - "one". This is useful for debugging Max patchers, as it allows you to create multiple print objects with custom labels to differentiate them from one another in the Max Console.
Now unlock the patcher and connect the outlet of the "click for one" [button](https://docs.cycling74.com/reference/button/ "button") to the pink button below and to its left. Notice that this doesn’t break the connection that already exists; outlets can be connected to more than one object, and the same message will be sent down each of the patch cords. Lock the patcher and click on the top-most button. The `bang` gets sent to both button objects, and each of them produces a bang message of their own. By a similar token, multiple patch cords can be connected to a single inlet of an object. In this case, both pink buttons are connected to the same [print](https://docs.cycling74.com/reference/print/ "print") object. When you click on the top button, the output of both buttons that receive bang messages are routed to the print object, and _two_ "bang" messages are displayed in the Max Console.
The next patch over demonstrates both of these principles. Clicking the [button](https://docs.cycling74.com/reference/button/ "button") labeled "Click for several!" sends _three_`bang` messages to the Max Console through a [print](https://docs.cycling74.com/reference/print/ "print") object labeled "several". The print object receives a bang from both of the second tier button objects (triggered by our topmost button) as well as a single bang from the top button itself, connected directly to the print object.
We can take this idea further with the right-most patch. It has a number of [message](https://docs.cycling74.com/reference/message/ "message") boxes, all connected to a single [print](https://docs.cycling74.com/reference/print/ "print") object named “many”. Each message box has a [button](https://docs.cycling74.com/reference/button/ "button") attached to it, and a higher-level button controlling them all. You can make individual message objects print their message by either clicking on the message box itself, or by clicking on their attached button objects. If you want to trigger all of the messages at once, you can click on the top-most button.
When you hit the top [button](https://docs.cycling74.com/reference/button/ "button"), notice the order in which the messages are displayed in the Max Console. The messages are not in an arbitrary order – they are generated based on the _spatial_ organization of the objects in the patcher, executing from _right-to-left_. We will explore the details of message ordering in a future tutorial, but it is vital to understand that messages are sent in right-to-left order when a single object is connected to more than one destination.
Unlock the patch, and add several more [button](https://docs.cycling74.com/reference/button/ "button") objects. You can do this by simply hitting the 'b' (for button) key on the keyboard in an unlocked patcher. Connect them to other button objects on that right-hand patch. Try different combinations of multiple outlet connections and multiple inlet connections. As you connect each button, try to guess which messages will display and in what order they will appear in the Max Console.
## Summary
The `bang` message is among the most powerful messages in the Max environment; it causes other objects to trigger their output, and can be used to create matrices of connections that produce complex output. We’ve seen that outlets can have multiple connections, and that these connections pass their messages in a right to left order. Inlets may also have multiple connections, and messages are processed in the order they arrive. We’ve also seen that some objects, such as the [print](https://docs.cycling74.com/reference/print/ "print") object, can be assigned an argument which causes the object to change its behavior. An argument to the print object allows you to identify the source of messages printed to the Max Console.
## See Also
  * [button - Output a bang](https://docs.cycling74.com/reference/button/)
  * [print - Print any message in the Max Console](https://docs.cycling74.com/reference/print/)
  * [message - Display and send any message](https://docs.cycling74.com/reference/message/)



Kind
    Tutorial 

Category
    Max 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
