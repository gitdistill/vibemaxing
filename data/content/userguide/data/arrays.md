---
description: The array data type in Max, for storing ordered data. Generally a more powerful version of lists.
group: Data
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/arrays/
title: Arrays
---

# Arrays
Arrays are a data type in Max. Similar to [lists](https://docs.cycling74.com/userguide/message_types/#lists), arrays store multiple items in order. Unlike lists, which are limited to storing [numbers](https://docs.cycling74.com/userguide/message_types/) and [symbols](https://docs.cycling74.com/userguide/message_types/#symbols), arrays can store other Max data structures including [strings](https://docs.cycling74.com/userguide/strings/), [dictionaries](https://docs.cycling74.com/userguide/dictionaries/), and other arrays. Similar to [dictionaries](https://docs.cycling74.com/userguide/dictionaries/) and [strings](https://docs.cycling74.com/userguide/strings/), arrays are stored in memory by name. Generally, arrays are a more powerful version of lists.
## When to Use Arrays
## Creating an Array
Create an array with the [array](https://docs.cycling74.com/reference/array/ "array") object. Initialize the contents of the array by including the initial values as [object arguments](https://docs.cycling74.com/userguide/objects/#arguments).
![An Max patcher containing two object boxes. The first has the contents "array" and the second has the contents "array 1 2 3". A comment describes the first object as an empty array, and the second object as an array with initial contents](https://docs.cycling74.com/images/68daafe0250c00fe47f197e3e7f66dd5_267.webp)
## Editing Arrays
Edit an array in place by using the [append](https://docs.cycling74.com/reference/array/#method_append), [clear](https://docs.cycling74.com/reference/array/#method_clear), [delete](https://docs.cycling74.com/reference/array/#method_delete), [insert](https://docs.cycling74.com/reference/array/#method_insert), [prepend](https://docs.cycling74.com/reference/array/#method_prepend), and [replace](https://docs.cycling74.com/reference/array/#method_replace) messages.
![An Max patcher containing an array object. Message boxes containing example messages like append, clear, delete, insert, prepend, and replace are connected to it.](https://docs.cycling74.com/images/53d37ca56dd1bde5ab4061740de958c5_431.webp)
Objects that modify arrays as they pass through them, like `array.rotate`, don't change the original array, but create a new array with the result of their computation. In this example, the objects on the left always output the same result, but the objects on the right will update the original array with every rotation.
![On the left, objects connected in series that rotate an array to the right by one. On the right, the same set of objects, with an additional connection that updates the original array after rotation.](https://docs.cycling74.com/images/d1efef19483bfc6d1820e834aacfb843_306.webp)
## Named Arrays
Like [dictionaries](https://docs.cycling74.com/userguide/dictionaries/) and [strings](https://docs.cycling74.com/userguide/strings/), arrays always have a unique name. By default, the name will simply be a randomly generated unique identifier. You can also assign a name to an array using the @name attribute.
![On the left, an array object connected to a chooser object, demonstrating the unique name assigned to array objects by default. On the right, an array with the name Peter.](https://docs.cycling74.com/images/2f73738058bd5183a3038dd6867bb7d3_316.webp)
An array is identified by its unique name, so you can access the same array from any array object with the same name.
![Two array objects, both with the name "tom". A message box with the contents "1 2 3" is connected to the right inlet of one of the array objects. A button is connected to the left inlet of the other array object, and that array object is also connected to the right inlet of a message box with the contents "1 2 3".](https://docs.cycling74.com/images/066c4118397af060f32fb13c3f40d606_276.webp)
## Converting to and from a List
Any list sent to an [array](https://docs.cycling74.com/reference/array/ "array") object will automatically be converted to an array. When it comes to working with arrays and lists, many objects will use arrays and lists interchangeably. However, in some circumstances, you might need to use a list and not an array. In these cases, you can use the [array.tolist](https://docs.cycling74.com/reference/array.tolist "array.tolist") object to convert an array into a list.
![](https://docs.cycling74.com/images/7dc4bba112cc48ab13c8a7f2cfcd4482_514.webp)
If the array contains structured data, like dictionaries or other arrays, converting to a list will not unpack the contents of any structured data object. Instead, the list will simply contain a symbol representation of the object.
![](https://docs.cycling74.com/images/731a1ab4fc166b29b6d6c8b245138bfa_236.webp)
If your array contains only numbers, symbols/strings, and other arrays, you can use the object [array.flatten](https://docs.cycling74.com/reference/array.flatten "array.flatten") to collect all sub-arrays and their contents into one long array. This can then pass through the [array.tolist](https://docs.cycling74.com/reference/array.tolist "array.tolist") object to return a simple representation of your array's contents.
![](https://docs.cycling74.com/images/07a4f087784437bd4d2b2f260d501995_520.webp)
## Arrays and Dictionaries
Dictionaries can contain arrays, and arrays can contain dictionaries. Printing an array containing a dictionary will output a JSON representation of the dictionary.
![](https://docs.cycling74.com/images/81666967cb69c8c3172c85be3ac9a4b1_527.webp)
## JavaScript
Use the `MaxArray` class to create a JavaScript reference to a Max Array. You can give it an initial value by passing a list or Array value to the constructor. Update the value of the array by calling `.set`.
```
var max_arr = new MaxArray(1, 2, "three", 4.0);
max_arr.set(10, 9, "eight", 7.0); // update the array contents

```

By setting the name property of the `MaxArray`, you can refer to a Array defined in the parent patcher.
```
var max_arr = new MaxArray();
max_arr.name = "frith"; // Now the MaxArray refers to an array named "frith"
max_arr.set(2, 4, "six", 8); // Updates the array in the containing patcher

```

If you want to manipulate the Array value, call `.stringify` and `JSON.parse` to turn the Max Array into a JavaScript Array. From there, you can use regular JavaScript array manipulation functions. To convert back, use `JSON.stringify` and `.parse`.
```
var max_arr = new MaxArray();
max_arr.set(2, "3", "four", 6);
var js_arr = JSON.parse(max_arr.stringify()); // retrieve the value as a JS string, convert to Array
post(JSON.stringify(js_arr) + '\n'); // prints "[2, '3', 'four', 6]"
js_arr[1] = 3;
max_arr.parse(JSON.stringify(js_arr));
post(max_arr.stringify() + '\n'); // prints "[2, 3, 'four', 6]"

```

To send a Max Array out of an outlet defined in JavaScript, send the string "array" followed by the name of the array.
```
function bang() {
  var arr = new MaxArray();
  arr.parse("[I, got, a, bang]");
  outlet(0, "array", arr.name);
}

```

