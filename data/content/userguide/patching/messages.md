---
description: Details of how messages are structured, and how they pass between objects
group: Patching
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/messages/
title: Messages
---

# Messages
## Messages Overview
Max objects communicate with each other by sending each other _Messages_. A message consists of one or more _Atoms_ , where each atom can be a _bang_ , a _symbol_ , an _int_ , or a _float_.
  * bang: empty atom, a bang means "do it"
  * symbol: one or more alphanumeric characters
  * int: a whole number
  * float: a number with a decimal part


If a message contains multiple atoms, it's referred to as a list. The atoms in a list are separated by spaces. If a symbol atom must contain spaces, the whole symbol should be [escaped](https://docs.cycling74.com/userguide/messages/#escaping-characters) with double-quotes. When an object receives a message, what the object does depends on the first element of the message. For example, the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") oscillator object can respond to messages by changing its frequency or phase.
This first element of a Max message, which determines how an object will interpret the message, doesn't have a special name in Max, but you may sometimes hear it called a _selector_ , since it functions in a similar way to a _selector_ in programming languages like Smalltalk or Objective-C.
![](https://docs.cycling74.com/images/da1e499bd6b9a22459109498c675a248_251.webp) When a cycle~ object gets a message starting with 'frequency', it responds by changing its internal frequency. When it gets a message starting with 'phase', it responds by changing its phase instead.
## Interpreting Messages
The way an object responds to a message depends on two things: the contents of the message, and the inlet that receives the message. Generally, every inlet is bound to a specific function, but you can override that function depending on how you format your message. For example, the second inlet of the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object sets the phase of the oscillator, and when [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") receives a _float_ or _int_ value in its second inlet, it will interpret that number as changing the phase of the oscillator. However, if you really want to, you can send the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") a message like `phase 0.5` to any inlet, and the [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object will always update its phase. This might be a confusing way to design your patcher, but it's allowed.
Because of this flexibility, an object could respond to multiple messages in the same way. When a [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object gets a float in its first inlet, it will change its frequency. The same is true if it gets an _int_ message, or the message `float 440`. Also, you could send the message `frequency 440` to any inlet, and the result would be the same.
![](https://docs.cycling74.com/images/681487cf8a6c50f35c1eae4260842a06_274.webp) These messages, when sent to cycle~, all have the same effect. The `frequency 4` message will set the frequency, even though it's being sent to the right inlet.
## Message Box
A _Message Box_ is a special kind of [UI object](https://docs.cycling74.com/userguide/objects/#creating-ui-objects) that contains a single message. When you click on a message box or send it a _bang_ , the message box will respond by sending out its contents as a message. Message boxes are extremely flexible and fulfill all kinds of functions in a Max patcher. You can use a group of message boxes to store values, to format other messages, or to view the messages that are passing between other objects.
![](https://docs.cycling74.com/images/b777948eb41df621efb6c4672a353ace_353.webp) Clicking on any of these messages would send a different list to line~, triggering an enveelope with a different shape
### Viewing Messages
The easiest way to view a message is to connect a patch cord to the right inlet of a message box. Lists of any kind can easily be viewed this way.
![](https://docs.cycling74.com/images/6a1e3572653e7e497172eb3e762ad6dd_365.webp) Using the right inlet of a message box, it's possible to view even very long and complex messages
One thing to keep in mind when using a message box this way is that the message box will only display the last message that it received. Sometimes it's not clear that a message box has actually received multiple messages, since only the last message received will be displayed. When you want to view all of the messages that have been sent along a given patch cord, you can use the [print](https://docs.cycling74.com/reference/print/ "print") object to log messages to the Max console.
![](https://docs.cycling74.com/images/0d33f8ecd79631687f89259694520c89_574.webp) The print object will log all received messages to the console, where the message object itself will only show the most recent message.
Finally, you can set **breakpoints** and **watchpoints** on your patch cords, for even more precise control over how messages move through your patcher. See [Debugging and Probing](https://docs.cycling74.com/userguide/debugging_and_probing/#debugging) for more details.
### Dollar sign replacement
If a message box contains the special `$` character, followed immediately by one of the digits `1-9`, that message box will re-format any messages that come through it. The characters `$1` will be replaced by the first element of the incoming message, the characters `$2` will be replaced by the second element, and so on. Characters like `$1` and `$2` do not need to appear in order, and they can appear any number of times. So the message `$2 $1` will reverse the first two element of an incoming message, and the message `$1 $1 $1` will repeat the first element three times. If you want a symbol to begin with `$1` and for those characters not to be replaced, add the backslash `\` character before the `$` to escape it.
![](https://docs.cycling74.com/images/91923909ef151a379653ba23525e2768_486.webp) The special $1 characters are replaced by the first element of the incoming message
Dollar-sign replacement will only work if the characters like `$1` appear at the beginning of a word. So sending a message like `34` to `$1-bis` would result in `34-bis`, but sending the same message to `bis-$1` won't cause any replacement to happen.
### Commas
Commas in a message box will cause a single message box to send multiple messages. If you click on a message box containing the text `1, 2, 3`, that message box will send the message `1`, followed by the message `2`, followed by the message `3`. If you're new to Max, probably the first place you'll see this is in conjunction with the [line~](https://docs.cycling74.com/reference/line~/ "line~") object, where a single-element message sets the value of [line~](https://docs.cycling74.com/reference/line~/ "line~") immediately, and the following list message gives [line~](https://docs.cycling74.com/reference/line~/ "line~") an envelope to follow.
![](https://docs.cycling74.com/images/b8c6592d63eb031d0cbb80f653718a36_550.webp) Commas in a message box cause a single message box to send multiple messages.
### Semicolon prefix
Finally, the semicolon character `;` has a special meaning whenever it appears at the beginning of a message. When you trigger a message box beginning with a semicolon, instead of sending that message to its first outlet, the message box will send a message to the named destination in the global namespace.
For example, a message like `; max clearmaxwindow` will send the message `clearmaxwindow` to the global object named `max`. In this case, this message will tell Max to clear the Max console. Messages like this are commonly used to script and control the Max application itself. This is useful for [controlling Max with messages](https://docs.cycling74.com/userguide/controlling_max_with_messages/), for [controlling Jitter with messages](https://docs.cycling74.com/userguide/controlling_jitter_with_messages/), and for [controlling DSP with messages](https://docs.cycling74.com/userguide/controlling_dsp_with_messages/).
Because `send` and `receive` objects are also in the global namespace, you can send messages to these objects as well using messages with the semicolon character. This is not a common pattern, but you're welcome to do it anyway.
![](https://docs.cycling74.com/images/822866aee3bdb94dd079cc7fe4353fc9_201.webp) You can send messages to a receive object using a semicolon message, even though it's not very common
### Escaping characters
You can use the backslash character to escape a single character anywhere in a message box. For example, you can use a backslash before the `$` character if you want to make sure that the `$` is not interpreted as a placeholder for [dollar-sign replacement](https://docs.cycling74.com/userguide/messages/#dollar-sign-replacement).
![](https://docs.cycling74.com/images/0b2de5e48f10ecbdea9d91c702535b3e_404.webp) Use the backslash to escape a $ if you want to avoid dollar-sign replacement
To escape multiple characters, or a whole sequence of characters, you can enclose everything you want to escape in double quotes. Note that single quotes will not work, so the message box containing `'hi there'` contains two symbols: `'hi` and `there'`. Double quotes are often useful if you want a block of text containing spaces to be interpreted as a single symbol.
![](https://docs.cycling74.com/images/74c5de9a0602ef8117dfbceff776927a_310.webp) Use double quotes to escape multiple characters, especially multiple spaces.
