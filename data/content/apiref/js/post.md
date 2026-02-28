---
description: Prints a representation of the arguments in the Max window.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/post/
title: function post
---

# function post
Prints a representation of the arguments in the Max window.
If post() has no arguments, it prints starting on the next line. Otherwise it prints the input on the current line separated by spaces. Arrays are unrolled to one level as with [jsthis.outlet()](https://docs.cycling74.com/apiref/js/jsthis/#outlet "jsthis.outlet\(\)").
```
export declare function post(...args: any): void;

```
Name | Type | Description  
---|---|---  
args | any | one or more arguments to print  
#### Example
```
var a = new Array(900, 1000, 1100);
post(1, 2, 3, "violet", a);
post();
post(4, 5, 6);

// prints the following to the Max console:
// 1 2 3 violet 900 1000 1100
// 4 5 6

```

If you want a line break in the middle of a call to post() you can use "\n" within a string. Also, post() begins a new line if the last person to write to the Max window was not the js object.
If you try to print a JavaScript class instance, you will see jsobject printed to the console.
