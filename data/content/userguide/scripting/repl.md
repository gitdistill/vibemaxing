---
description: The Read Evaluate Print Loop feature lets you send messages to Max objects using text
group: Scripting
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/repl/
title: REPL
---

# REPL
## Introduction
The Max REPL (an acronym for _Read-Evaluate-Print Loop_) is a text entry area at the bottom of the [Max Console](https://docs.cycling74.com/userguide/max_console/) that lets you interact with patchers via text commands.
Using the REPL, you can:
  * Send messages to Max objects in your patcher
  * Evaluate JavaScript expressions
  * Control the Max environment with text-based commands
  * Access the documentation


## Accessing the REPL
To show the REPL, open either the sidebar [Max Console](https://docs.cycling74.com/userguide/max_console/) or the standalone [Max Console](https://docs.cycling74.com/userguide/max_console/).
![](https://docs.cycling74.com/images/51650484acc176adce8eeea52da6c518_38.webp)
If the command prompt at the bottom of the [Max console](https://docs.cycling74.com/userguide/max_console/) is not showing, click the REPL icon in the bottom [Max console](https://docs.cycling74.com/userguide/max_console/) toolbar to show it.
![](https://docs.cycling74.com/images/657de0e8785fe77e29e9102b8c9f4d18_98.webp)
## Using the REPL
Let's see a simple example of the REPL in action. Click once in the text entry box at the bottom of the [Max Console](https://docs.cycling74.com/userguide/max_console/) to highlight the REPL for text input. The caret will begin blinking.
![](https://docs.cycling74.com/images/100b61de185bc76395fbfc28f3360017_212.webp)
Enter `max printversion` and press Return.
![](https://docs.cycling74.com/images/4305b728ddfd3dcfe18c945fe05b6b74_231.webp)
After pressing Return, you'll see `max printversion` posted to the [Max console](https://docs.cycling74.com/userguide/max_console/) followed by the current version number. For example:
![](https://docs.cycling74.com/images/edf7318fa8472ee29b77bd695c4bd0c9_141.webp)
What's going on in this example? The REPL is sending a **message** to a **named object**. The "read" in this case is reading what you type. It's then "evaluating" the text you typed by sending the message. Finally, the result of the message is (often) "printed" back to the [Max console](https://docs.cycling74.com/userguide/max_console/). And after reading, evaluating, and printing, the REPL is ready for another command (the "loop").
In the above example `max` is the named object and `printversion` is the message. This simple form -- receiver followed by message -- is the same as a [message](https://docs.cycling74.com/reference/message/ "message") box that begins with a semicolon.
![](https://docs.cycling74.com/images/771de65e36663352eba2f4ba6f58d13e_111.webp)
The REPL is a faster and simpler way to send messages to `max` and other named objects because you don't need to create and then click on a message box, and you don't need a semicolon.
Finally, notice that after you press return, the text entry field clears, but the cursor is still blinking, waiting for another command. This permits you to send REPL commands in quick succession.
### Quick Documentation Access
Ever forget what a Max object does? The REPL can help. Enter `man funnel` and press Return. (If `man` is too much typing, you can also use `?`.) The Max window posts the following:
> funnel: Identifies the inlet of incoming data. It can be used to store values into a table or coll based on their source, or used to set a destination with an object such as spray.
## REPL History
To repeat a previous command, you can use the **up arrow** key to scroll through the history of what you've previously typed into the REPL. Pressing the up arrow once will enter the most recently typed command into the REPL's text entry box, ready for you to send it again by pressing the Return key. The **down arrow** scrolls the opposite direction back to the most recently typed command. Once you pass the most recent command, pressing the down arrow will clear the text entry box.
## Shortcuts
Above the text entry field of the REPL you'll see the **shortcuts bar** :
![](https://docs.cycling74.com/images/db2eaa93f1a6480e10a0008c4eb87724_247.webp)
These **shortcuts** are named objects (_targets_) where you can send messages. Clicking on a shortcut makes it persistent, so you can send it repeated messages without having to type the object name. For example, click on the **max** shortcut. It will appear at the beginning of the text entry box:
![](https://docs.cycling74.com/images/f1235d3150b66ffb5ac173c46fb8059e_165.webp)
Type `printversion` after the word `max` and press return. Now, after the version number is posted to the [Max console](https://docs.cycling74.com/userguide/max_console/), `max` remains at the beginning of the text entry box, ready for you to send it another command.
There are several other standard shortcuts that appear in the REPL area of the [Max console](https://docs.cycling74.com/userguide/max_console/):
  * **?** is the same as **man** , for documentation queries (currently limited to object descriptions)
  * **_** is a way to send messages to the REPL itself
  * **man** (short for _manual_) is for documentation queries (currently limited to object descriptions)
  * **js** is the global JavaScript evaluator
  * **max** is the `max` object; messages are documented in [Controlling Max with Messages](https://docs.cycling74.com/userguide/controlling_max_with_messages/)
  * **< p>** is the patcher for which this console is the sidebar (**< p>** does nothing in the standalone [Max console](https://docs.cycling74.com/userguide/max_console/) window)
  * **+** opens a menu showing other available named object targets; if none are currently available, the menu will not appear when you click **+**


### Managing Shortcuts
To set the current shortcut, click on the desired name (or choose it from the **+** menu). It will highlight and the text will appear at the beginning of the text entry box.
To clear the current shortcut, click its name in the shortcuts bar again. The text at the begining of the text entry box will be removed.
To make the current named object the persistent REPL target so it doesn't go away when you pretty Return, press Shift-Return instead.
To clear the current shortcut after sending it a message, press Option- or Alt-Return
To remove non-default shortcuts (ones you added by the **+** menu) from the shortcuts bar, hold down the control key and click on the shortcut name until you see a menu that says _Delete Shortcut_.
![](https://docs.cycling74.com/images/9d21f901a2198da31b255d79ad7f5f42_147.webp)
## Patcher-Specific and Global Targets
Two named object REPL targets already introduced are `max` and `man`. These are **global** targets that work in any [Max console](https://docs.cycling74.com/userguide/max_console/) window, whether it's the sidebar or the standalone. In fact, all the standard shortcuts listed above are global except for **< p>**.
##  [receive](https://docs.cycling74.com/reference/receive/ "receive") Objects Are Global
The name argument to a [receive](https://docs.cycling74.com/reference/receive/ "receive") object is its global name. While you can have many [receive](https://docs.cycling74.com/reference/receive/ "receive") objects that share the same name in different patchers, using a [send](https://docs.cycling74.com/reference/send/ "send") object with the same name will send to all [receive](https://docs.cycling74.com/reference/receive/ "receive") objects. The same is true for the REPL.
Make the following simple patcher:
![](https://docs.cycling74.com/images/f88e76f1914d56fcc1426ae5e4c20b4a_192.webp)
You can use `xyz` as a named object target in the REPL in any [Max console](https://docs.cycling74.com/userguide/max_console/) window, not just the one connected to the patcher where the [receive](https://docs.cycling74.com/reference/receive/ "receive") object lives.
Enter `xyz 74` and press Return. The [message](https://docs.cycling74.com/reference/message/ "message") box text will be set to 74. This does the same thing as entering `; xyz 74` into a message box and clicking it.
Once a receive object exists in the Max environment, it will be available as a shortcut in the menu you see by clicking **+**.
![](https://docs.cycling74.com/images/eb2ae454e42677bb47e91202ea00e545_238.webp)
You can send any message to a [receive](https://docs.cycling74.com/reference/receive/ "receive") object via the REPL, not just numbers. Given the above example, `xyz cat + dog` will set the [message](https://docs.cycling74.com/reference/message/ "message") box contents to `cat + dog`.
Note that unlike a [message](https://docs.cycling74.com/reference/message/ "message") box, the REPL does not currently support sending multiple messages in sequence to the same named object using commas.
## Scripting Name Targets Are Patcher-Specific
In addition to [receive](https://docs.cycling74.com/reference/receive/ "receive") objects, you can use the REPL to send messages to any object with a scripting name. Here's a simple example. In a new patcher window, open the sidebar [Max console](https://docs.cycling74.com/userguide/max_console/). Then return to the patcher and create new a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") object.
![](https://docs.cycling74.com/images/c5774027dcecb9b1bc304c3e6518e224_91.webp)
The default scripting name for a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") is `live.dial`. But we don't even have to look in the inspector to see what it's called because having created the [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") it will show up in the shortcut menu under **Named Objects** when we click the **+** above the text entry area in the REPL.
![](https://docs.cycling74.com/images/a955838a459cf3729f00e6b32de433f3_224.webp)
Choosing **::live.dial** from the **+** menu will make it the current shortcut (and add it to the shortcuts bar).
![](https://docs.cycling74.com/images/903b52835cf0e502d35acd9906912605_331.webp)
Objects with scripting names are preceded with two colons (**::**) to distinguish them from [receive](https://docs.cycling74.com/reference/receive/ "receive") objects.
With `::live.dial` are the REPL target, type `74` and press return. The dial is now set to 74.
![](https://docs.cycling74.com/images/e6295b1088659e56cea6579124a35fdc_67.webp)
Using a scripting name gives you direct access to an object, so you can also set its attributes and send the object any message it understands. Let's set the dial to a deep blue color -- enter `activedialcolor 0 0 1 1` after `::live.dial` and press Return.
![](https://docs.cycling74.com/images/7169d734d628b2a3bcecb1e8e411ab47_65.webp)
## Evaluating JavaScript
### The Global js Environment
Using the special `js` global target, the REPL has its own JavaScript environment that can be used for evaluating math expressions and defining variables.
When working with the JavaScript evaluator, it's helpful to click on **js** in the shortcut bar to make it the current shortcut.
![](https://docs.cycling74.com/images/bf84a53cb37603f399857d28a2a0f258_142.webp)
Here are a couple of examples of using the evaluator:
  * Enter `js 3 + 4` and press Return. The [Max console](https://docs.cycling74.com/userguide/max_console/) should print `7`.
  * Need a random number? Enter `js Math.random()` and press Return. You'll get a number between 0 and 1.
  * You can declare a variable for later use. Enter `let b = 20` and press Return. The [Max console](https://docs.cycling74.com/userguide/max_console/) will print `undefined` because there was no result for this variable assignment operation.
  * Now you can retreive the variable `b` and use it in other expressions. For example, try `b * 100` and you should see `2000`.


In the [Redirection](https://docs.cycling74.com/userguide/repl/#js-redirection) discussion below, we'll see how you can send the result of a Javascript expression to a named object target.
### Javascript with Named [v8](https://docs.cycling74.com/reference/v8/ "v8") Objects
If you give a [v8](https://docs.cycling74.com/reference/v8/ "v8"), [v8ui](https://docs.cycling74.com/reference/v8ui/ "v8ui"), or [v8.codebox](https://docs.cycling74.com/reference/v8.codebox "v8.codebox") JavaScript object a scripting name, you can use the REPL to interact with the environment in that object using JavaScript. You can call functions defined in the object's script or get and set the values of variables or properties.
A [v8](https://docs.cycling74.com/reference/v8/ "v8") object with a scripting name, like any other object, can be a target for Max messages. For example, if you define a function bang inside a script in [v8](https://docs.cycling74.com/reference/v8/ "v8") object named `calum` you can call that function with `::calum bang`.
By using the special `.js` "sub-target" you can interact with the [v8](https://docs.cycling74.com/reference/v8/ "v8") object in JavaScript itself. For example, to call the defined function `bang` using the `.js` sub-target: `::calum.js bang()`.
Note the parentheses are necessary because you are not sending `calum` a Max message, you are using Javascript to call a function inside the object's script itself. Similarly if you have declared a variable at global scope in your script named `bob` you can print out its value with `::calum.js bob`. Or you can change the value of `bob` with `::calum.js bob = 74`.
Everything else you can do in the global JavaScript evaluator is possible with a named [v8](https://docs.cycling74.com/reference/v8/ "v8") object and the `.js` sub-target.
## JS Redirection
Using the **redirect operator** (**<**) you can send the result of evaluating a JavaScript expression to a named object. For example, we can generate a random value between 0 and 127 with `js Math.random() * 127`. Now we want to send the random value we generated using JavaScript to a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial").
To set a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") object with scripting name `::live.dial` to a random value between 0 and 127, enter `::live.dial < js Math.random() * 127`.
The **<** _redirects_ the result of the Javascript expression to become the _message_ sent to the dial.
The result of expressions evaluated by named [v8](https://docs.cycling74.com/reference/v8/ "v8") objects can also be redirected as Max messages. The same example as above using a [v8](https://docs.cycling74.com/reference/v8/ "v8") object with scripting name `calum`: `::live.dial < ::calum.js Math.random() * 127`
The REPL currently supports only one redirection per line. One way to circumvent this limitation would be to write a function in a script in a [v8](https://docs.cycling74.com/reference/v8/ "v8") object that sends its arguments out an outlet as a Max message. This would allow you to call that function with more than one argument. For example, to generate a random color sent to a function called `sendit()`, you could do something like this: `::calum.js sendit(Math.random(), Math.random(), Math.random(), 1.0)`
## Patcher Scripting with the <p> Target
The REPL target **< p>** represents the patcher next to the sidebar [Max console](https://docs.cycling74.com/userguide/max_console/) where you are typing commands. It is an undefined name in the standalone [Max console](https://docs.cycling74.com/userguide/max_console/) window.
Using the same messages you can send to the [thispatcher](https://docs.cycling74.com/reference/thispatcher/ "thispatcher") object or the `patcher` object in the JavaScript API, the REPL allows you control and script your patcher. Here are a couple of simple examples:
  * To change the unlocked background color of the patcher to a dull medium gray, enter `<p> editing_bgcolor 0.5 0.5 0.5 1.0`.
  * To create a new button object with a scripting name, enter `<p> script newobject button @varname ddd`. Now you can send the newly created button messages such as `::ddd bang` or `::ddd bgcolor 0.7 0.2 0.3 1.0`


## Object Values and Attributes
To change the value of an object's attribute, type the attribute name and value after the object name. For example, to set the `ignoreclick` attribute of a [slider](https://docs.cycling74.com/reference/slider/ "slider") with scripting name `biffy`: `::biffy ignoreclick 1`
As a reminder, you can also change the value of the slider with `::biffy 25`.
You can use redirection to _access_ the value of an object or one of its attributes and send that value to another object. In this example, we have a [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") with scripting name `togo` that we will set with the current value of the `ignoreclick` attribute of the [slider](https://docs.cycling74.com/reference/slider/ "slider") named `biffy`. To access an attribute of an object, use the `::` notation to separate the attribute name from the scripting name.
`::togo < ::biffy::ignoreclick`
If have set `ignoreclick` in the [slider](https://docs.cycling74.com/reference/slider/ "slider") to 1, after entering this command, the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") should have a value of 1.
To access the value of an object such as a [slider](https://docs.cycling74.com/reference/slider/ "slider"), the name itself is sufficient after the redirect. In this example, we have another [slider](https://docs.cycling74.com/reference/slider/ "slider") named `coppy` that we want to set to the current value of `biffy`:
`::coppy < ::biffy`
## The [repl](https://docs.cycling74.com/reference/repl/ "repl") Object
The [repl](https://docs.cycling74.com/reference/repl/ "repl") object is an alternative to the [receive](https://docs.cycling74.com/reference/receive/ "receive") object with some REPL-specific features, including the ability to set either global or patcher-specific scope and the ability to use sub-targets.
Create a [repl](https://docs.cycling74.com/reference/repl/ "repl") with a name:
![](https://docs.cycling74.com/images/938a29848d0046a0395f28c8828557d0_109.webp)
Once created, the object is available as a target `foo` in the REPL. However, you can also append additional names (_sub-targets_) to `foo` using dot notation. For example, `foo.a 50 100` will still be sent to the `repl @name foo` object.
The right outlet of [repl](https://docs.cycling74.com/reference/repl/ "repl") precedes the message you send from the REPL with the target name. You can use the target name with the [route](https://docs.cycling74.com/reference/route/ "route") to direct messages aimed at different sub-targets to different outlets.
![](https://docs.cycling74.com/images/e5affd8161ce7cb923c1ca53e750fac1_320.webp)
