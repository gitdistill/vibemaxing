---
description: All of the different types of messages that pass between objects
group: Patching
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/message_types/
title: Message Types
---

# Message Types
All Max messages are built up of atoms, which can be a **bang** , a **float** , an **int** , or a **symbol**. These are simple types which hold a small, fixed amount of data. An ordered group of atoms is called a **list**. These are the fundamental Max data types. For larger, more complex data types, Max messages use atoms to refer to the place where that more complex data is stored.
## Atoms
There are no more fundamental types in Max than _bang_ , _float_ , _int_ , and _symbol_. An ordered group of these types is called a _list_ , which also acts a lot like a fundamental Max data type. In a [**message box**](https://docs.cycling74.com/userguide/messages/#message-box), Max treats each space-separated element as an atom. You can use the [typeroute~](https://docs.cycling74.com/reference/typeroute~/ "typeroute~") object to separate messagse traveling on a single patch cord by their data type.
![](https://docs.cycling74.com/images/0cfde8a1449915c70bfc8656bd7c8c0d_406.webp) Name | Description  
---|---  
bang |  _bang_ means "do it"—most objects respond to a bang by performing their primary function.  
int | A whole number without a decimal component  
float | A number with a decimal component  
symbol | Any combination of characters, including numeric characters  
### Floats and Ints
In Max, the difference between an int and a float can be significant. Some objects will have different behavior depending on whether they receive a float or an int, and some might refuse to accept one type of number when they expect the other. For a more in-depth discussion, see [Integers and Floats](https://docs.cycling74.com/userguide/integers_vs_floats/).
### Symbols
Symbols can contain any combination of characters. Max will automatically treat any non-numeric group of characters as a symbol (the one exception is the characters `bang`, which Max will recognize as a _bang_). If you want to treat a group of numbers as a symbol, or you want your symbol to contain spaces, use quotation marks.
![](https://docs.cycling74.com/images/7626abba0c79607592cf78b42308b0a0_306.webp)
A symbol is a fixed-length, immutable entity. Adding or removing characters from a symbol will create a new symbol and add that to the **Symbol Table**. Often this is a technical detail that you can safely ignore. If you want to know more, you can read about [symbols and strings](https://docs.cycling74.com/userguide/strings/#strings-vs-symbols).
## Lists
A list is just an ordered group of atoms. Often, if the first element of a list is a symbol, the object receiving the list will interpret the leading symbol as a _selector_ , and the following list elements as _arguments_.
Building, manipulating, and routing lists is fundamental to working in Max. You can route a list to one part of your patcher or another, based on the first element of the list, using the [route](https://docs.cycling74.com/reference/route/ "route") object. It's also very common to build lists using [dollar-sign replacement](https://docs.cycling74.com/userguide/messages/#dollar-sign-replacement) in a [message](https://docs.cycling74.com/reference/message/ "message") box. The `list.*` family of objects, like [list.append](https://docs.cycling74.com/reference/list.append "list.append"), [list.iter](https://docs.cycling74.com/reference/list.iter "list.iter"), and [list.rot](https://docs.cycling74.com/reference/list.rot "list.rot"), provide even more ways to work with lists.
Technically, a list must always start with either a float or an integer. If a list starts with a symbol, then the symbol is the selector, and what follows are the arguments for that selector. Usually you can ignore this technicality, but the distinction can be important to remember when working with Max's C or JavaScript APIs. There are also some sneaky situations that expose what's really going on "under the hood". For example, any object that accepts a message like ::message[list 1 2 3] will respond the same way to the message ::message[1 2 3]. So, the "length" of the message ::message[list 1 2 3] is actually 3.
![](https://docs.cycling74.com/images/ec8cdc68640fb04bcea66185387913c4_276.webp) The list selector instructs the object to treat the arguments that follow as a list.
## Named Storage Types
Atoms and lists are primitive in the sense that the name of the data is the same as the data. The number 12 and the atom `12` are the same. However, for larger and more complex data, it's not feasible to put the entire block of data into a message box. When one Max object wants to tell another Max object to process an image that's stored in a **matrix** , it doesn't send a message containing the data, but rather the name of the matrix that stores the data.
## Matrices
Matrices store multidimensional data, where every _cell_ has the same data type. Matrices are often used to store images, 3D models, and 3D transformations. The object that manages a reference to a matrix is called [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix").
When you view a matrix in a [message](https://docs.cycling74.com/reference/message/ "message") box, you'll see that matrices are identified by a list with two parts: the symbol `jit_matrix`, followed by the unique name of the matrix. For more info on matrices, see [matrix](https://docs.cycling74.com/userguide/matrix/).
![](https://docs.cycling74.com/images/5472ec2dcccc2748a2ecea92c459e545_172.webp)
Patcher cords that carry matrices also get a special, striped-green style. This is just cosmetic—as you can see it's simply carrying a normal message.
## Textures
Textures are similar to matrices, in that they store multidimensional data of all the same type. However, the big difference between Max matrices and textures is that textures reside on the Graphics Processing Unit, or GPU. Max itself manages the data and the life cycle of matrices, but it asks the graphics API to manage textures on its behalf.
The object that manages a reference to a texture is called [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture"). When you view a texture in a [message](https://docs.cycling74.com/reference/message/ "message") box, you'll see that a texture is identified by the symbol `jit_gl_texture` followed by the unique name of the texture. For more info on textures, see [textures](https://docs.cycling74.com/userguide/textures/).
![](https://docs.cycling74.com/images/b0edc636302b266c488d200adbb8257f_160.webp)
Like matrices, texture patch cords get their own styling.
## Dictionaries
Dictionaries store structured data. That data is organized into _keys_ and _values_ , and you can use the key to look up the value. A value can be a number, a list, a symbol, a string, an array, or even another dictionary.
Dictionaries are managed by the [dict](https://docs.cycling74.com/reference/dict/ "dict") object, and you can work with dictionaries using the `dict.*` family of objects. In a message box, you'll see that dictionaries are identified by the symbol `dict` followed by the name of the dictionary. For more info on dictionaries, see [dictionaries](https://docs.cycling74.com/userguide/dictionaries/).
## Strings
Strings store an ordered collection of characters. Unlike a symbol, strings are mutable, which means that a string can be changed without creating a new string.
Strings are managed by the [string](https://docs.cycling74.com/reference/string/ "string") object and manipulated with the `string.*` family of objects. In a message box, you'll see strings represented as by the symbol `string` followed by the name of the string. For more info on strings, see [strings](https://docs.cycling74.com/userguide/strings/).
## Arrays
Arrays are an ordered collection of arbitrary data. Unlike lists, arrays can store complex data types like dictionaries, strings, and other arrays. Max provides the handy [array.map](https://docs.cycling74.com/reference/array.map "array.map") and [array.reduce](https://docs.cycling74.com/reference/array.reduce "array.reduce") for functional-style programming on arrays.
Arrays are managed by the [array](https://docs.cycling74.com/reference/array/ "array") object and manipulated with the `array.*` family of objects. In a message box, you'll see arrays represented as by the symbol `array` followed by the name of the array. For more info on arrays, see [arrays](https://docs.cycling74.com/userguide/arrays/).
