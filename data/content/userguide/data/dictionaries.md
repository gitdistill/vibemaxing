---
description: The dictionary data type in Max, a named container for JSON-style key-value pair data
group: Data
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/dictionaries/
title: Dictionaries
---

# Dictionaries
A **Dictionary** is a container for data organized into key-value pairs. A key is always a symbol, but the value can be anything, including a number, symbol, list, or even another dictionary. You can create and manage dictionaries using the [dict](https://docs.cycling74.com/reference/dict/ "dict") object, and the associated family of dictionary manipulation objects. Like [arrays](https://docs.cycling74.com/userguide/arrays/) and [strings](https://docs.cycling74.com/userguide/strings/), dictionaries have names and can be passed between objects with messages like `dictionary u12345678`.
For developers, a dictionary is most similar to a JSON object, and there are convenience functions in the API for converting a dictionary to a JSON string, as well as updating the contents of a dictionary with JSON.
## When to Use Dictionaries
Dictionaries are useful for working with structured data, especially when that data has a hierarchical or labeled format. Imagine you were trying to simulate a large number of agents, each one modeling a simple creature with some kind of behavior. The state of each creature might look something like the following.
```
{
  "position": {
    "x": 2,
    "y": 5
  },
  "mood": "nostalgic"
}

```

With a dictionary, the values of your object not only have a place in a hierarchy, they also have labels.
## Working with Dictionaries
Create a new dictionary using the [dict](https://docs.cycling74.com/reference/dict/ "dict") object. The argument for the [dict](https://docs.cycling74.com/reference/dict/ "dict") object is the unique name for the dictionary. If you do not give the dictionary a name, Max will generate a unique name automatically. Two [dict](https://docs.cycling74.com/reference/dict/ "dict") objects with the same name will reference the same dictionary.
![Two dictionary objects with the same name. The left dictionary has a key-value pair set, but printing the right dictionary shows that the two have the same contents.](https://docs.cycling74.com/images/4b705619e1df95c1c886edc7acd4d980_396.webp) Dictionary basics
If you use a [message](https://docs.cycling74.com/reference/message/ "message") object to display a string, you'll see the actual values that pass between Max objects when sending a dictionary in a message. In a message, a dictionary is represented by the symbol `dictionary`, followed by the unique name of the dictionary.
## Editing a Dictionary
Edit the contents of a dictionary by double-clicking on a [dict](https://docs.cycling74.com/reference/dict/ "dict") object, or by sending the [dict](https://docs.cycling74.com/reference/dict/ "dict") object the `edit` message. This will open a text editor for modifying the contents of a dictionary.
![A dictionary object with its editor window open](https://docs.cycling74.com/images/1d3e4d477e81b07dd68bae620e317501_474.webp) Dictionary editing
Dictionaries can be edited using JSON syntax (except that dictionaries don't support boolean (`true`/`false`) values). Keys must be strings, enclosed in quotation marks. Values can be numbers, strings, arrays (denoted with square brackets) or dictionaries (denoted by curly braces). Since the entire structure is itself a dictionary, curly braces must enclose the whole dictionary expression.
By sending the `export` message to the [dict](https://docs.cycling74.com/reference/dict/ "dict") object, you can write the contents of a dictionary to a file, in either JSON or YAML format. Using the `import` message, you can then read such a file into a [dict](https://docs.cycling74.com/reference/dict/ "dict") object.
### pattr and pattrstorage
The [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") and [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/ "pattrstorage") objects will store the contents of a dictionary. Because a dictionary is not a simple numeric value, you can't interpolate between dictionary values using floating-point values for `recall`. However, in other respects, dictionaries are fully compatible with [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") and [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/ "pattrstorage").
![A dictionary connected to the pattr system](https://docs.cycling74.com/images/b1b20c3e6e611750c6f02c563531e676_384.webp) Dictionaries and pattr
### Getting and setting values
Dictionaries can have nested dictionaries as values, and can contain array values an well. To simplify accessing nested elements within a dictionary, Max dictionary objects use a double-colon syntax.
```
{
  "farm" : 	{
    "age": 101,
    "animals" : [ "sheep", "chicken", "cow" ],
    "crops" : [ "corn", "peas" ]
  }
}

```

Given a dictionary with the above contents, you can use the `get` or `set` messages to access values in the dictionary. Use a double-colon `::` to access a nested dictionary by its key, and use brackets `[]` to access elements in an array.
![](https://docs.cycling74.com/images/c5637b5e8a0b65701a3f6fef2990236d_611.webp)
Convert a message to a signal without any smoothing
## Abbreviated Dictionary Syntax
Dictionaries can be serialized to JSON, or initialized from a JSON string. However, dictionaries can also be parsed from a special abbreviated dictionary syntax, consisting of keys and values separated by a single colon. The following JavaScript code demonstrates initializing the same dictionary in two different ways.
```
let serial1 = `cow : 1 sheep : 2`;
let serial2 = `{ "cow": 1, "sheep": 2 }`;

let d1 = new Dict();
d1.parse(serial1);

let d2 = new Dict();
d2.parse(serial2);

// Dictionaries are the same

```
![](https://docs.cycling74.com/images/50ca477d483fe122f0e78626ab53be09_310.webp) Initializing a dictionary with abbreviated dictionary syntax
## JavaScript
Use the `Dict` class to create a JavaScript reference to a Max Dictionary. The name of the dictionary will be the first argument to the constructor, or an automatically generated unique name if none is provided. If the `js` object is in a patcher that contains a dictionary with the same name, then the `js` `Dict` object and the Max [dict](https://docs.cycling74.com/reference/dict/ "dict") object refer to the same dictionary. Modifying the contents of one will change the contents of the other.
```
var max_dict = new Dict("mydict");

```

To manipulate the contents of the dictionary, use the `get` and `set` methods.
```
max_dict.set("color", "red");
console.log(max_dict.get("color")); // prints "red"

```

The `parse` method can initialize the contents of a dictionary using a JavaScript JSON serialization. This is a useful way to convert a JavaScript object to a Max dictionary.
```
let obj = {x: 1, y: 2};
let serial = JSON.stringify(obj);
max_dict.parse(serial); // dictionary now has the keys x and y with values 1 and 2

```

To receive a dictionary in a JavaScript function, define a function named `dictionary`. The first argument to this function will be the name of the dictionary.
```
function dictionary(dict_name) {
  var myDict = new Dict(dict_name); // now "myDict" links to the passed-in string.
}

```

To send a Max dictionary out of an outlet defined in JavaScript, send the symbol "dictionary" followed by the name of the dictionary.
```
function bang() {
  var myDict = new Dict();
  myDict.set("wood", "balsa");
  outlet(0, "dictionary", myDict.name);
}

```

