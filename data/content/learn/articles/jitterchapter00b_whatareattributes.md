---
description: Editing Jitter object parameters
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter00b_whatareattributes/
title: Attributes
---

Download Series Content and Patchers
# What are attributes?
_Attributes_ are a new way to specify the behavior of Max objects. Most Jitter objects use attributes for the different variables that make up their current internal state.
![The good old Max counter object](https://docs.cycling74.com/images/f0ad274f972c6bafcb9846c837ac14dc_335.webp) The good old Max counter object
Many Max objects, such as the [counter](https://docs.cycling74.com/reference/counter/ "counter") object shown above, take a number of _arguments_ to determine how they behave. The order of these arguments after the object's name determines how the object interprets them. In the example above, the first argument to [counter](https://docs.cycling74.com/reference/counter/ "counter") sets the direction in which the object counts; the second and third arguments determine the minimum and maximum values that the object counts between. Since these values are simply given to the object as numbers, their ordering is important. With some Max objects ([counter](https://docs.cycling74.com/reference/counter/ "counter") is one of them) the number of arguments you give has some effect on the way in which they are interpreted. If you supply [counter](https://docs.cycling74.com/reference/counter/ "counter") with only two arguments, they will be understood by the object as the minimum and maximum count, _not_ the direction and minimum count. Because the position and number of arguments are crucial, there is no way, for example, to create a [counter](https://docs.cycling74.com/reference/counter/ "counter") object with a predefined direction and maximum count using only two arguments.
The arguments to an object are often seen as _initial_ values, and Max objects typically have ways to modify those values through additional inlets to the object or special messages you send the object. You can change the direction and maximum count of a [counter](https://docs.cycling74.com/reference/counter/ "counter") object by sending integers into its second and fifth inlets, respectively. These will override the default values supplied by the arguments. Similarly, you can change the minimum count of the object by sending the message min followed by an integer into the left inlet.
While this system works well when a Max object only has two or three variables that define its behavior, Jitter objects often have many, many more variables (sometimes dozens). If all of these variables depended on the order of inlets and object arguments, you would spend all day searching the reference manual and never have time to do any work with Jitter!
## Setting Attributes
Jitter objects can be told how to behave by using _attributes_. You can type attributes into an object box along with the Jitter object's name, or you can set (and retrieve) attributes through Max messages after the object is created.
![A Jitter object with attributes after the object name](https://docs.cycling74.com/images/b73ae5a6d2423619e2162e1aee792b04_324.webp) A Jitter object with attributes after the object name
The Jitter object shown above, called [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa"), has three typed-in attributes. Typed-in attributes are set in object boxes by using the `@` symbol followed by the name of the attribute and one or more arguments (which could be any kind of Max data: ints, floats, symbols, or lists). You can enter as many attributes as the object recognizes, _in any order_ , after the object's name. While you may not know what the [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object does yet, you can infer a little bit about the object based on the names of the attributes and what type of data they have assigned to them.
_Important:_ There is no space between the `@` sign and the name of the typed-in attribute you want to set. The `@` character tells the Jitter object to interpret the word attached to it as an attribute name instead of an argument value for a previous attribute.
_Also Important:_ Jitter objects can have both typed-in attributes _and_ typed-in arguments. See the **Jitter Object Arguments** section below for details.
As with Max objects, the information you give a Jitter object to set its initial behavior is generally something you can change after the object is created. Attributes can be changed at any time by sending messages to the object as shown below.
![Attributes can be changed with Max messages](https://docs.cycling74.com/images/8f59a00281c81ef150ec14df81e25a82_316.webp) Attributes can be changed with Max messages
This [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object has its `brightness` attribute set to `0.5`. `1` initially (typed into the object box as '@brightness 0.5'), but we can change it to something else by sending the message `brightness [float]` into the object's left inlet. You can change virtually any attribute by sending a message with the attribute's name, followed by the relevant arguments, into a Jitter object's left inlet. 
As with Max objects, Jitter objects have default values for their parameters. The [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object above only has typed-in attributes initializing its `brightness` value, but other attributes are set to their default values. We’ll show you how to find out what attributes an object uses below. In the example above, we can change the values of the object's `contrast` and `saturation` attributes using messages, overriding whatever default values the object has supplied.
## Jitter Object Arguments
There are four pieces of information that most Jitter objects use that can be entered either as typed-in attributes or typed-in arguments. In fact, they are always attributes, but Jitter objects automatically handle them correctly when they are used as arguments. 
![Jitter objects can have arguments, too!](https://docs.cycling74.com/images/f102166d6539ba3319fc52f98561c652_316.webp) Jitter objects can have arguments, too!
The [jit.rota](https://docs.cycling74.com/reference/jit.rota "jit.rota") object, shown above, clearly has two attribute initialized: `anchor_x` and `anchor_y`. But what does the other stuff mean? If you supply arguments for a Jitter object that processes Jitter matrix data (and most Jitter objects do), the arguments are interpreted as:
  1. The `planecount` of the output matrix.
  2. The `type` of the output matrix.
  3. The size, or 'dimension list' (`dim`), of the output matrix.


Now that we know this, we can determine that the [jit.rota](https://docs.cycling74.com/reference/jit.rota "jit.rota") object above will output a matrix that is made up of `4` planes of `char` (8-bit integer) data with two dimensions of `320` by `240` cells.
_Important:_ Jitter object arguments, if used, must appear _before_ any attributes are set. Otherwise the Jitter object will misinterpret the arguments as values for the attribute, not arguments to the object.
These arguments can also be set by attributes that are consistent for all Jitter objects that output matrix data: `planecount`, `type`, and `dim`. They can be set as unordered typed-in attributes or changed with messages. The three objects below, for example, are identical.
![Arguments or attributes? You decide.](https://docs.cycling74.com/images/25ca98c344d5e96a03fb610a34ba4b3d_328.webp) Arguments or attributes? You decide.
The first object has its output matrix attributes set using typed-in arguments. The second object has the `planecount` and `type` set using typed-in arguments, but uses a typed-in attribute for the dimension list. The third object uses a typed-in attributes to set everything.
If you prefer, you can initialize an object-s attributes using messages triggered from a loadbang object as shown below.
![Yet another way to initialize your attributes](https://docs.cycling74.com/images/4c04324107c8288aa9317e7a72c911f2_350.webp) Yet another way to initialize your attributes
## Querying Attributes and Object State
The quickest way to find out an object's attribute settings is by consulting the _inspector_ window. This is available by selecting the object and keying command/alt i or by clicking the _i_ icon on the right toolbar. You will find current attribute settings near the bottom of the window.
An additional (and very useful) feature of attributes is that you can ask a Jitter object to tell you what value it currently has stored for any given attribute. You do this by _querying_ the attribute with the Max message `get` followed (_with no space_) by the name of the attribute you want to know about. The resulting value is output by the Jitter object as a message (beginning with the attribute's name), sent out the object's right outlet.
![Querying an attribute for a Jitter object](https://docs.cycling74.com/images/32cd0a26b6a2883ab8c129718d0911b7_245.webp) Querying an attribute for a Jitter object
Using `get` to find the values of attributes lets you discover the current value of an attribute, even if you never set the attribute in the first place. For example, the patch below discovers some of the default values of the [jit.plur](https://docs.cycling74.com/reference/jit.plur "jit.plur") object. The Max [route](https://docs.cycling74.com/reference/route/ "route") object lets you easily separate the values for each of the attributes.
![Finding out the default values of object attributes](https://docs.cycling74.com/images/5b014ed69e6449f77faa14ae8638e736_357.webp) Finding out the default values of object attributes
Two messages you can send to any Jitter object, `getattributes` and `getstate`, output all the attributes used by the object.
![Finding out your options…](https://docs.cycling74.com/images/a6ff21c9d8270d827487a1c55a26a9c5_276.webp) Finding out your options…
The `getattributes` message causes the Jitter object to output the message `attributes` followed by a list of all the attribute symbols that Jitter object understands. Experimenting with a few Jitter objects will quickly show you that many of these, such as `outputmode`, `type` and `dim`, are fairly standard. Others (such as mask in the [jit.brass](https://docs.cycling74.com/reference/jit.brass "jit.brass") object) will have special meaning for the object that uses them.
The `getstate` message dumps out all the attributes for the Jitter object as if every conceivable attribute query had been performed all at once.
![Finding an object's state](https://docs.cycling74.com/images/791614410392c314ec9a8666e380c16b_556.webp) Finding an object's state
You can then use [route](https://docs.cycling74.com/reference/route/ "route"), [unpack](https://docs.cycling74.com/reference/unpack/ "unpack"), and other Max objects to extract the attributes as you need them. Later in the tutorials, you will encounter several Jitter objects where the attributes change based on calculations performed on the input matrix (or a file that has just been opened by the object). Querying the relevant attributes is how you can find out the result of the object's calculation.
## Attrui
You can also read attribute values with the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object. This is a user Interface widget that seems to be connected to the inlet of an object but actually has two-way communication. The [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object has two sections—the left section is a pull-down menu with all of the connected object's attributes available. Once an attribute has been chosen, the right hand side shows the current value of the attribute and allows you to edit it.
![Finding an object's state](https://docs.cycling74.com/images/3fc11040ef0f2188713cf2cade8a32f1_301.webp) Finding an object's state
## Summary
Jitter attributes are a powerful tool for managing the parameters of complex objects. You can use attributes to initialize, change, and find out the current values stored in Jitter objects, and the attachment of each value to a fixed attribute name eliminates the need to remember typed-in argument ordering or the role of each inlet in a complex object. 

Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
