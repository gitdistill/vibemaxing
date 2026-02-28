---
description: Data container for text characters
group: Data
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/strings/
title: Strings
---

# Strings
A **String** is a container for text (specifically UTF-8 text) that is independent of Max's [Symbol Table](https://docs.cycling74.com/userguide/strings/#strings-vs-symbols). You can create and manage Strings using the [string](https://docs.cycling74.com/reference/string/ "string") object. Like [Arrays](https://docs.cycling74.com/userguide/arrays/) and [Dictionaries](https://docs.cycling74.com/userguide/dictionaries/), Strings have names and can be passed between objects with `string u12345678` messages. For developers, a String wraps Max's internal `t_string` object.
## When to Use Strings
In addition to the [string](https://docs.cycling74.com/reference/string/ "string") object, Max has several objects for editing, combining, filtering, and searching through strings. The [string.at](https://docs.cycling74.com/reference/string.at "string.at") object searches a string for the position of a substring, and [string.slice](https://docs.cycling74.com/reference/string.slice "string.slice") creates a new string from a character range within an existing string. If your patchers require this sort of text manipulation, it's easier and more efficient to use these purpose-built **String** objects than it is to use **Symbols**.
## Working with Strings
Create a new **String** using the [string](https://docs.cycling74.com/reference/string/ "string") object. The first argument is the initial value for the string, and you can (optionally) provide a name for the string as well using the `@name` attribute. Strings with the same name will share the same value, so you can create a string in one place and then refer to it somewhere else. When you print a string using the [print](https://docs.cycling74.com/reference/print/ "print") object, Max will format the output to show the name and contents of the string.
![Two string objects, with the same @name attribute. The Max console showing the result of sending a String to a print object.](https://docs.cycling74.com/images/b98f4ad30b8d52253e2218b97f7a76cb_577.webp) Strings basics
If you use a [message](https://docs.cycling74.com/reference/message/ "message") object to display a string, you'll see the actual values that pass between Max objects when sending a string in a message. In a message, a string is represented by the symbol `string` followed by the unique identifier for that string. If you don't give your string an explicit name using the `@name` attribute, Max will assign one automatically.
![A string object without a @name attribute. Hovering of a patchcord to show how a string is actually passed between objects, and a message box showing how a string will be rendered when received in its right inlet.](https://docs.cycling74.com/images/888aa64d35a77ac3da162f5bf72c8687_197.webp)
The [message](https://docs.cycling74.com/reference/message/ "message") object has a `@convertobjs` attribute which will automatically convert received String objects into symbols for display.
If a string object changes the input string somehow, it will output a new string rather than modifying the original. This means that if you want to modify a string recursively, adding your changes back to the original string, you can use the name of the string to replace the original string.
![A string object with the name "greeting" connected to a string.concat object, which then connects to another string object also with the name "greeting". This demonstrates how to create a recursive operation on a string, to build up a result from multiple manipulations on a single string.](https://docs.cycling74.com/images/e9f8f4efb645062535630c75da546a34_216.webp)
### pattr and pattrstorage
The [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") and [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/ "pattrstorage") objects will store the value of a string. They do not store the string itself, so if you modify the string after storing its value in a [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object, the updated value will not appear in [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") until you send the string to [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") again.
![A pattr object bound to a string object. The string object is modified outside of the pattr object, to show that changes to the string are not reflected in pattr.](https://docs.cycling74.com/images/682001afd9b61e953ec70ddfb029f3f7_453.webp)
In this example, changing the value of the string by sending the `new_value` message to the second [string](https://docs.cycling74.com/reference/string/ "string") object will not update the value stored in [pattr](https://docs.cycling74.com/reference/pattr/ "pattr").
### Backwards compatibility
If a receiving object does not understand the new `string` type, then Max will automatically convert that string into a symbol to maintain compatibility.
![A string object connected to a sprintf object, showing how the string gets converted automatically to a symbol](https://docs.cycling74.com/images/582fd9bdf5f63c163eeb115bd7c29b1d_218.webp)
A handful of control objects will always pass strings unmodified, so that they can still be used to route strings between objects. Those objects include:
  * [append](https://docs.cycling74.com/reference/append/ "append")
  * [prepend](https://docs.cycling74.com/reference/prepend/ "prepend")
  * [route](https://docs.cycling74.com/reference/route/ "route")
  * [routepass](https://docs.cycling74.com/reference/routepass/ "routepass")
  * [trigger](https://docs.cycling74.com/reference/trigger/ "trigger")
  * [match](https://docs.cycling74.com/reference/match/ "match")
  * [router](https://docs.cycling74.com/reference/router/ "router")
  * [universal](https://docs.cycling74.com/reference/universal/ "universal")
  * [typeroute~](https://docs.cycling74.com/reference/typeroute~/ "typeroute~")
  * [gate](https://docs.cycling74.com/reference/gate/ "gate")/[switch](https://docs.cycling74.com/reference/switch/ "switch")

![A string object connected to a trigger object, which passes the string through unmodified](https://docs.cycling74.com/images/f13b3ca4a04659a9bc4c3848d9efcc15_276.webp) The trigger object passes the string message through without decomposing it into a symbol. This works even when we use the symbol formatter for trigger.
## JavaScript
Use the `MaxString` class to create a JavaScript reference to a Max String. You can give it an initial value by passing a string value to the constructor. Update the value of the string by calling `.parse` or `.set`.
```
var max_str = new MaxString("initial_value");
max_str.parse("new_value"); // update the string contents

```

By setting the name property of the `MaxString`, you can refer to a String defined in the parent patcher.
```
var max_str = new MaxString();
max_str.name = "fred"; // Now the MaxString refers to a string named "fred"
max_str.set("new_value"); // Updates the string in the containing patcher

```

If you want to manipulate the String value, call `.stringify` or `.get` to turn the Max String into a JavaScript string. From there, you can use regular JavaScript string manipulation functions.
```
var max_str = new MaxString();
max_str.set("the original string value");

var js_str = max_str.get(); // retrieve the value as a JS string
var updated_str = js_str.replace("original", "new");
max_str.parse(updated_str);
post(max_str.stringify()); // prints "the new string value"

```

To send a Max String out of an outlet defined in JavaScript, send the symbol "string" followed by the name of the string.
```
function bang() {
  var str = new MaxString();
  str.parse("I got a bang");
  outlet(0, "string", str.name);
}

```

## Strings vs Symbols
When working in Max, most of the time, objects pass around text in the form of symbols. When you include text like `bgcolor` or `set` in a list, you're using a symbol. Max doesn't pass the text of a symbol directly, but instead generates a unique identifier for each symbol, passing that identifier between objects instead. This makes certain operations on symbols very efficient, for example comparing the value of two symbols. However, it also means that every time you use a new symbol, it must be assigned to a unique identifier, and that identifier must be added to the **Symbol Table**. The identifiers added to the Symbol Table are never removed -- the table will grow forever until Max is quit, or runs out of memory.
Strings, on the other hand, do not interact with the Symbol Table. Instead, Max manages Strings in a similar way to **Buffers** or the contents of a [dict](https://docs.cycling74.com/reference/dict/ "dict") object. The text contents of a String are located somewhere in memory, and Max gives that memory a name that can be used to locate the contents of the String. The object interface to a block of audio samples is [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), and the object interface to a Dictionary is the [dict](https://docs.cycling74.com/reference/dict/ "dict") object. In a similar way, the [string](https://docs.cycling74.com/reference/string/ "string") object is the interface to a text String. When a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") or a [dict](https://docs.cycling74.com/reference/dict/ "dict") is cleared, the underlying memory is released back to the operating system to be used for new storage. The same applies to Strings, which can be, depending on your requirements, a more efficient way to store text data.
One further difference is that Max symbols are restricted to 32767 characters. Strings have no such limitation, and support the storage of huge blocks of text data.
