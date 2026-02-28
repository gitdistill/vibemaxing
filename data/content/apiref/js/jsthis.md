---
description: The "this" object in the context of JavaScript in Max
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/jsthis/
title: class jsthis
---

# class jsthis
The "this" object in the context of JavaScript in Max
The jsthis object is the "this" within the context of any function you define that can be invoked from Max, as well as in your global code. When you define functions, they become methods of your extension of jsthis. When you use variables in your global code, they become its properties. The jsthis object has certain built-in properties and methods that facilitate interacting with and controlling the Max environment.
You can't create an Instance of this class. It is only available as a global context object in the Max JavaScript environment.
For most messages, a message received in the inlet of the Max `js` object will invoke a method with the same name defined for the JavaScript [jsthis](https://docs.cycling74.com/apiref/js/jsthis/ "jsthis") object passing anything after the beginning symbol as arguments to the function. The [jsthis.bang()](https://docs.cycling74.com/apiref/js/jsthis/#bang "jsthis.bang\(\)") and [jsthis.list()](https://docs.cycling74.com/apiref/js/jsthis/#list "jsthis.list\(\)") methods are two examples.
You can also create your own custom message handlers. For example, within Max, sending the message `foo 1 2 3` to the `js` object invokes the `foo()` method of the [jsthis](https://docs.cycling74.com/apiref/js/jsthis/ "jsthis") object. In other words, it looks for a function property of [jsthis](https://docs.cycling74.com/apiref/js/jsthis/ "jsthis") called `foo` and passes `1`, `2`, and `3` as arguments to the function.
```
function foo(a, b, c) {
    post(a, b, c);
}

```

Finally, some functions and methods specific to drawing will only be available in the context of an object with a graphics context. If you are overriding the drawing of an existing UI object using the `@jspainterfile` attribute, then you can define a [jsthis.paint()](https://docs.cycling74.com/apiref/js/jsthis/#paint "jsthis.paint\(\)") function for custom drawing. If you are creating a custom UI object with jsui or v8ui, then you can define a [jsthis.paint()](https://docs.cycling74.com/apiref/js/jsthis/#paint "jsthis.paint\(\)") function as well as event handlers like [jsthis.onclick()](https://docs.cycling74.com/apiref/js/jsthis/#onclick "jsthis.onclick\(\)"), [jsthis.onresize()](https://docs.cycling74.com/apiref/js/jsthis/#onresize "jsthis.onresize\(\)"), [jsthis.onfocus()](https://docs.cycling74.com/apiref/js/jsthis/#onfocus "jsthis.onfocus\(\)"), and [jsthis.onblur()](https://docs.cycling74.com/apiref/js/jsthis/#onblur "jsthis.onblur\(\)").
## Properties
### autowatch boolean
Whether automatic file reloading is on
This is particularly useful during development of your Javascript code if you have several js instances using the same source file and you want them all to update when the source changes. It can also be used to facilitate the use of an external text editor. When the text editor saves the file, the js object will notice and recompile it. By default, the value of autowatch is 0 (off). If you want to turn on autowatch, it is best to do so in your global code.
#### Example
```
// begin file example.js
autowatch = 1;

function loadbang() {
    // your code here
}

// end file example.js

```

### box [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") read-only
The current object's box
#### Example
```
function bang() {
    var box = this.box;
    post(box.rect);
}

```

### editfontsize number
Size of the font shown in the text editing window
Controls the size of the font shown in the text editing window where you edit a script in points. By assigning the editfontsize property in your global code, you can override the default font size setting for text editing, which is the same size as the text shown in the Max window.
*
#### Example
```
// begin file example.js
editfontsize = 10;

function loadbang() {
    // your code here
}

// end file example.js

```

### inlet number read-only
The inlet number which received the message triggering the currently executing function
During the execution of a function, the inlet property reports the inlet number that received the message that triggered the function, starting at 0 for the leftmost inlet. This property’s value is 0 within global code.
#### Example
```
inlets = 3;

function msg_int(val) {
    switch(inlet) {
        case 2:
            post("inlet 3: " + val);
            break;
        case 1:
            post("inlet 2: " + val);\
            break;
        default:
            post("left inlet: " + val);
    }
}

```

### inlets number
Number of inlets of the current object instance
The inlets property must be set in the global code to have any effect. If it isn't set, an object with one inlet will be created.
### jsarguments string[] read-only
Access arguments typed into the js object when instantiated
The filename is `jsarguments[0]`, and the first typed-in argument is `jsarguments[1]`, and so on. The `jsarguments[]` array is available in global code and any function and it doesn't change unless the `js` object receives the `jsargs` message with new typed-in arguments.
#### Example
Creating an object with a variable number of outlets based on an argument typed into the `js` object
```
oulets = 0
if (jsarguments.length >= 2) {
    outlets = jsarguments[1];
}
if (!outlets) {
    oulets = 1;
}

```

### max [Max](https://docs.cycling74.com/apiref/js/max/ "Max") read-only
Global Max instance
Gets a JavaScript representation of the "max" object (e.g. the recipient of `; max preempt 1` in a message box). This lets you send any message to the object that controls the Max application.
#### Example
```
max.preempt(1);

```

### messagename string read-only
Name of the message to the `js` object that invoked the method currently running
In global code, this is a `nil` value. This is generally useful only from within an `anything` function that will be called when no specific function name matches the message sent to the `js` object.
#### Example
Note the use of JavaScript bracket notation to specify a variable property
```
var stuff;
function anything(val) {
    if (arguments.length) {
        stuff[messagename] = val;
    }
}

```

### multitouch boolean
Whether multitouch event handling is enabled
This behavior is only available in the new v8 javascript engine objects.
Set this property to enable multitouch event handling. Multi-touch and tablet events are currently only supported on Windows. This property must be set in global code to enable multitouch support for onpointer* event handlers.
#### Example
```
// begin file example.js
multitouch = 1;

function onpointermove(pointerevent) {
    post("pointer: type=" + pointerevent.pointerType + " id=" + pointerevent.pointerId + "\n");
}
// end file example.js

```

### outlets number
Number of outlets the `js` object should have
The outlets property must be set in the global code to have any effect. If it isn’t set, and object with one outlet will be created.
#### Example
```
outlets = 2;
function anything() {
    outlet(0, "this is outlet 0");
    outlet(1, "this", "is", "outlet", "1");
}

```

## Methods
### anything
The `anything` function is called if no specific function is found to match the message symbol received by the `js` object
If you want to know the name of the message that invoked the function, use the `message` property. If you want to know what inlet received the message, use the `inlet` property.
```
anything(): void;

```

#### Example
```
function anything() {
    var val = arrayfromargs(messagename, arguments);
    post("anything() was called: " + val.toSource());
}

```

### arrayfromargs
A utility for writing functions that take a variable number of arguments and/or those that can be called using various messages (like `anything`)
The function object has an `arguments` property that can be numerically indexed like an `Array` but is not an instance of `Array`. This means that you cannot call `Array` functions such as `sort()` on the `arguments` property or send the `arguments` property out of an outlet as a list of values. The `arrayfromargs` method will convert the arguments property to an `Array`, optionally with `message` as the zeroth element of the array. This message usage is useful for processing messages as though they are lists beginning with a symbol, as would be typical in your `anything` function.
```
arrayfromargs(arguments: object): string[];

```
Name | Type | Description  
---|---|---  
arguments | object | a property of the `arrayfromargs` function which holds all arguments passed to the function in an array-like container  
Return Value | string[] |   
#### Example 1
In this example, the arguments passed to the `js` object are sorted and sent out the first outlet.
```
function anything() {
    // messagename is a property of the `jsthis` object and
    // returns the name of the message which invoked the function
    var a = arrayfromargs(messagename, arguments);
    a.sort();
    outlet(0, a);
}

```

#### Example 2
In this example, any list sent to the `js` object is printed as an array.
```
function list() {
   var a = arrayfromargs(arguments);
   post("received list " + a + "\n");
}

```

### arrayfromargs
A utility for writing functions that take a variable number of arguments and/or those that can be called using various messages (like `anything`)
The function object has an `arguments` property that can be numerically indexed like an `Array` but is not an instance of `Array`. This means that you cannot call `Array` functions such as `sort()` on the `arguments` property or send the `arguments` property out of an outlet as a list of values. The `arrayfromargs` method will convert the arguments property to an `Array`, optionally with `message` as the zeroth element of the array. This message usage is useful for processing messages as though they are lists beginning with a symbol, as would be typical in your `anything` function.
```
arrayfromargs(message: string, arguments: object): string[];

```
Name | Type | Description  
---|---|---  
message | string | the name of the message which triggered the function call; typically `messagename` is used here in the context of an `anything` method  
arguments | object | a property of the `arrayfromargs` function which holds all arguments passed to the function in an array-like container  
Return Value | string[] |   
#### Example
In this example, the arguments passed to the `js` object are sorted and sent out the first outlet.
```
function anything() {
    // messagename is a property of the `jsthis` object and
    // returns the name of the message which invoked the function
    var a = arrayfromargs(messagename, arguments);
    a.sort();
    outlet(0, a);
}

```

### assist
Set the patcher assist string for a designated inlet or outlet of a `js` object
This method is designed to be called from the assistance function, specified as an argument to [jsthis.setinletassist()](https://docs.cycling74.com/apiref/js/jsthis/#setinletassist "jsthis.setinletassist\(\)") or [jsthis.setoutletassist()](https://docs.cycling74.com/apiref/js/jsthis/#setoutletassist "jsthis.setoutletassist\(\)").
```
assist(...args: any[]): void;

```
Name | Type | Description  
---|---|---  
args | any[] | the assist string; if an array is supplied, the elements are concatenated  
#### Example
```
outlets = 2;

function describe(n) {
    assist("This is outlet number: ", n);
}

setoutletassist(-1, describe);

```

### bang
A function called when the `js` object receives a bang
```
bang(): void;

```

#### Example
```
function bang() {
    post("a bang was received\n");
}

```

### declareattribute
Declare an attribute which can be set, queried, and optionally stored in the patcher file
If no getter or setter methods are specified, default ones will be used. These attributes can also be referenced by pattr.
```
declareattribute(attributeName: string, getterName?: string, setterName?: string, embed?: boolean, options?: object): void;

```
Name | Type | Description  
---|---|---  
attributeName | string | the name of the attribute  
_optional_ getterName | string | the getter function name  
_optional_ setterName | string | the setter function name  
_optional_ embed | boolean | whether to embed on patcher save  
_optional_ options | object | a key/value dictinoary for additional options (only available in v8 engine)  
#### Example 1
A simple attribute declaration where default getters and setters are used
```
var foo = 2;
declareattribute("foo");

function bang() {
    outlet(0, foo);
}

```

#### Example 2
A default getter and setter are used and the attribute is stored in the patcher file on save
```
var foo = 2;
declareattribute("foo", null, null, 1);

function bang() {
    outlet(0, foo);
}

```

#### Example 3
An explicit getter and setter are declared
```
var foo = 2;
declareattribute("foo", "getfoo", "setfoo");

function getfoo() {
    return foo;
}

function setfoo(v) {
    foo = v;
}

function bang() {
    outlet(0, foo);
}

```

#### Example 4
More examples using options object in v8 engine
```
// for any attribute that uses default getters and/or setters,
// it is important to declare the attribute using 'var' insetad of 'let'

var fluffy = 0;
declareattribute("fluffy", { style: "onoff", embed: 1, label: "Enable Fluffiness" });

var bunny = 74;
declareattribute("bunny", { setter : "setbunny", min: -3, max: 101, default: 74, type: "long" });

var bingo = "One";
declareattribute({ name: "bingo", style: "enum", enumvals: ["One", "Two", "Three"] });

var bongo = [ 1, 0, 0, 1];
declareattribute({ name: "bongo", style: "rgba" });

var boppy = [ 74 , 75 ];
declareattribute("boppy", { min: -3, max: 101, default: [ 74, 75 ], type: "long" });

// custom setter
function setbunny(v)
{
    bunny = v;
    post("I am setting bunny to: " + v + "\n");
}

// possible properties to pass in are:
// name : string
// getter : string
// setter : string
// embed : number/bool
// type: string ("long", "float", "symbol", "atom")
// size : number (for arrays...also implicit if default is an array)
// style : string ("onoff", "enum", "rgba")
// label : string
// category : string
// min : number
// max : number
// default : number, string, array
// invisible : number/bool
// steps : number
// enumindex : array of strings
// enumvals : array of strings
// paint : number/bool

```

### embedmessage
The [jsthis.embedmessage()](https://docs.cycling74.com/apiref/js/jsthis/#embedmessage "jsthis.embedmessage\(\)") method works only inside of the [jsthis.save()](https://docs.cycling74.com/apiref/js/jsthis/#save "jsthis.save\(\)") function. It is used to specify the name of a function you want to be called when the `js` object containing the script is recreated.
```
embedmessage(functionName: string, args: number | number[] | string | string[]): void;

```
Name | Type | Description  
---|---|---  
functionName | string | the name of a function to be called when [jsthis.save()](https://docs.cycling74.com/apiref/js/jsthis/#save "jsthis.save\(\)") is recreated  
args | number | number[] | string | string[] | arguments to pass to the named function  
#### Example
In this example, when the `js` object containing this script is instantiated, the function `numchairs` will be called with an argument of 20 followed by the `numtables` function with an argument of `2`. Finally, the `roomname` function will be called with an argument of `"diningroom"`.
```
function save() {
    embedmessage("numchairs", 20);
    embedmessage("numtables", 2);
    embedmessage("roomname", "diningroom");
}

function numchairs(v) {
    // ...
}

function numtables(v) {
    // ...
}

function roomname(x) {
    // ...
}

```

### getvalueof
Permit pattr and related objects to attach to and query an object's current value.
The value of an object returned can be a number, string, or an array of numbers and/or strings.
```
getvalueof(): any | any[];

```
Name | Type | Description  
---|---|---  
Return Value | any | any[] |   
#### Example 1
```
myValue = 100;

function getvalueof() {
    return myValue;
}

```

#### Example 2
`getvalueof` works for other objects, not just `js` and `jsui`
```
var flonum = this.patcher.newobject("flonum");
flonum.setvalueof();
post("value: " + flonum.getvalueof() + "\n");

```

### hittest
Filter mouse events
Implement this function to filter mouse events like onclick and ondrag. If you return zero from [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)"), then the mouse event that called hittest will be filtered out and not passed on to other event handlers. Always return zero to make an object effectively invisible to the mouse.
```
hittest(x: number, y: number): number | boolean;

```
Name | Type | Description  
---|---|---  
x | number | x coordinate of the mouse event  
y | number | y coordinate of the mouse event  
Return Value | number | boolean |   
### list
A function called when the `js` object receives a Max list (i.e. messages that begin with a number)
If you're using the legacy js engine, you can use the `arrayfromargs` function to convert the arguments to an array instead, without the spread operator.
```
list(): void;

```

#### Example 1
```
function list(...args) {
   post("list was called: " + args + "\n");
}

```

#### Example 2
```
function list() {
    var val = arrayfromargs(messagename, arguments);
    post("list was called: " + val + "\n");
}

```

### loadbang
A function called when a patcher containing the `js` or `jsui` object is loaded
This function will not be called when you instantiate a new `js` or `jsui` object and add it to a patcher; it will only be called when a pre-existing patcher file containing a `js` object is loaded - in other words, at the same time that `loadbang` objects in a patcher are sending out bangs. You may wish to test the `loadbangdisabled` property of the [Max](https://docs.cycling74.com/apiref/js/max/ "Max") object and do nothing in your loadbang function if it is true.
```
loadbang(): void;

```

#### Example
```
function loadbang() {
    post("loadbang was called\n");
}

```

### msg_array
A function called when the `js` object receives a Max array, automatically converting the incoming Max array object to a native JS array object copy
This behavior is only available in the new v8 javascript engine objects. Alternatively, a function named "array" may defined to receive the name of the Max array object. This alternate strategy is also only available in the new v8 javascript engine.
```
msg_array(value: Array): void;

```
Name | Type | Description  
---|---|---  
value | Array |   
#### Example
```
function msg_array(a) {
    if (a) {
        for (var i = 0; i < a.length; i++) {
            a[i] = a[i] + 1; // increment each array element by 1
        }
        outlet_array(0, a); // outlet and convert to Max array object
    }
}

```

### msg_dictionary
A function called when the `js` object receives a Max dictionary, automatically converting the incoming Max dictionary object to a native JS object copy
The JS object will match the hierarchy and contents of the dictionary similar to if you serialized the dictionary to JSON and then parsed the JSON into a JS object. This behavior is only available in the new v8 javascript engine objects. Alternatively, a function named "dictionary" may defined to receive the name of the Max dictionary object. This alternate strategy may be used in the legacy js engine.
```
msg_dictionary(value: Object): void;

```
Name | Type | Description  
---|---|---  
value | Object |   
#### Example
```
function msg_dictionary(d) {
    if (d) {
        d.x = "marks the spot"; // add a new key
        outlet_dictionary(0, d); // outlet and convert to a Max dictionary object
    }
}

```

### msg_float
A function called when the `js` object receives a float
If no [jsthis.msg_int()](https://docs.cycling74.com/apiref/js/jsthis/#msg_int "jsthis.msg_int\(\)") method is defined, all numbers will be passed to the [jsthis.msg_float()](https://docs.cycling74.com/apiref/js/jsthis/#msg_float "jsthis.msg_float\(\)") method and ints will be converted to floats before being used.
```
msg_float(value: number): void;

```
Name | Type | Description  
---|---|---  
value | number |   
#### Example
```
function msg_float(v) {
    post(v);
}

```

### msg_int
A function called when the `js` object receives an integer
If no [jsthis.msg_float()](https://docs.cycling74.com/apiref/js/jsthis/#msg_float "jsthis.msg_float\(\)") method is defined, all numbers will be passed to the [jsthis.msg_int()](https://docs.cycling74.com/apiref/js/jsthis/#msg_int "jsthis.msg_int\(\)") method and ints will be truncated to ints before being used.
```
msg_int(): void;

```

#### Example
```
function msg_int(v) {
    post(v);
}

```

### msg_string
A function called when the `js` object receives a Max string, automatically converting the incoming Max dictionary object to a native JS string copy
This behavior is only available in the new v8 javascript engine objects. Alternatively, a function named "string" may defined to receive the name of the Max string object. This alternate strategy is also only available in the new v8 javascript engine.
```
msg_string(value: string): void;

```
Name | Type | Description  
---|---|---  
value | string |   
#### Example
```
function msg_string(s) {
    if (s) {
        s = s + " more text"; // append "more text"
        outlet_string(0, d); // outlet and convert to a Max string object
    }
}

```

### notifyclients
Notify any clients (such as the pattr family of objects) that the object's current value has changed
Clients can then take appropriate action (such as sending a `js` instance the message `getvalueof` to invoke the [jsthis.getvalueof()](https://docs.cycling74.com/apiref/js/jsthis/#getvalueof "jsthis.getvalueof\(\)") method if defined). The [jsthis.notifyclients()](https://docs.cycling74.com/apiref/js/jsthis/#notifyclients "jsthis.notifyclients\(\)") method is useful for othat define [jsthis.setvalueof()](https://docs.cycling74.com/apiref/js/jsthis/#setvalueof "jsthis.setvalueof\(\)") and [jsthis.getvalueof()](https://docs.cycling74.com/apiref/js/jsthis/#getvalueof "jsthis.getvalueof\(\)") for pattr compatibility.
```
notifyclients(): void;

```

### notifydeleted
A function called when the `js`/`jsui` object is freed
```
notifydeleted(): void;

```

### onblur
Receives blur events when the object loses focus.
Implement this function to receive a callback when the object loses keyboard focus. This is useful for handling cleanup when the object is no longer active or updating the visual state accordingly.
```
onblur(): void;

```

#### Example
```
function onblur() {
    post("Object lost focus\n");
    mgraphics.redraw();
}

```

### onclick
Receives initial click events.
Implement this function to receive a callback when the mouse is clicked in the object background. Note that if the [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") function is implemented, then this function will only be called if [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") returns a truthy value. The "button" argument will always be 1.
```
onclick(x: number, y: number, button: number, mod1: number, shift: number, caps: number, opt: number, mod2: number, pointerevent?: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
x | number | x coordinate in object space  
y | number | y coordinate in object space  
button | number | whether the mouse is down, which will always be 1 for onclick  
mod1 | number | nonzero if the Command (macOS) or Windows (Windows) key is held down  
shift | number | nonzero if the shift key is held down  
caps | number | nonzero if caps lock is enabled  
opt | number | nonzero if the option key is held down  
mod2 | number | nonzero if the control key is held down  
_optional_ pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | optional pointer event object containing additional event details (v8 only)  
### ondblclick
Receives double click events.
Implement this function to receive a callback when the mouse is double clicked in the object background. Note that if the [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") function is implemented, then this function will only be called if [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") returns a truthy value. The "button" argument will always be 1.
```
ondblclick(x: number, y: number, button: number, mod1: number, shift: number, caps: number, opt: number, mod2: number): void;

```
Name | Type | Description  
---|---|---  
x | number | x coordinate in object space  
y | number | y coordinate in object space  
button | number | whether the mouse is down, which will always be 1 for onclick  
mod1 | number | nonzero if the Command (macOS) or Windows (Windows) key is held down  
shift | number | nonzero if the shift key is held down  
caps | number | nonzero if caps lock is enabled  
opt | number | nonzero if the option key is held down  
mod2 | number | nonzero if the control key is held down  
### ondrag
Receives drag events.
Implement this function to receive a callback during drag events. Note that if the [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") function is implemented, then this function will only be called if [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") returns a truthy value. The "button" argument will be 1 while dragging, and 0 when dragging stops.
```
ondrag(x: number, y: number, button: number, mod1: number, shift: number, caps: number, opt: number, mod2: number, pointerevent?: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
x | number | x coordinate in object space  
y | number | y coordinate in object space  
button | number | whether the mouse is down, which will always be 1 for onclick  
mod1 | number | nonzero if the Command (macOS) or Windows (Windows) key is held down  
shift | number | nonzero if the shift key is held down  
caps | number | nonzero if caps lock is enabled  
opt | number | nonzero if the option key is held down  
mod2 | number | nonzero if the control key is held down  
_optional_ pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | optional pointer event object containing additional event details (v8 only)  
### onfocus
Receives focus events when the object gains focus.
Implement this function to receive a callback when the object receives keyboard focus. This is useful for handling keyboard input or updating the visual state of the object when it becomes active.
```
onfocus(): void;

```

#### Example
```
function onfocus() {
    post("Object gained focus\n");
    mgraphics.redraw();
}

```

### onidle
Receives mouse events over the object.
Implement this function to receive a callback if the mouse moves over the object. Equivalent to a "mouse over" event. Note that if the [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") function is implemented, then this function will only be called if [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") returns a truthy value. The "button" argument will always be 0.
```
onidle(x: number, y: number, button: number, mod1: number, shift: number, caps: number, opt: number, mod2: number, pointerevent?: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
x | number | x coordinate in object space  
y | number | y coordinate in object space  
button | number | whether the mouse is down, which will always be 1 for onclick  
mod1 | number | nonzero if the Command (macOS) or Windows (Windows) key is held down  
shift | number | nonzero if the shift key is held down  
caps | number | nonzero if caps lock is enabled  
opt | number | nonzero if the option key is held down  
mod2 | number | nonzero if the control key is held down  
_optional_ pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | optional pointer event object containing additional event details (v8 only)  
### onidleout
Mouse event as the cursor leaves the object boundaries.
Implement this function to receive a callback if the mouse out of bounds of the current object. Note that if the [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") function is implemented, then this function will only be called if [jsthis.hittest()](https://docs.cycling74.com/apiref/js/jsthis/#hittest "jsthis.hittest\(\)") returns a truthy value. Equivalent to a "mouse out" event. The "button" argument will always be 0.
```
onidleout(x: number, y: number, button: number, mod1: number, shift: number, caps: number, opt: number, mod2: number, pointerevent?: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
x | number | x coordinate in object space  
y | number | y coordinate in object space  
button | number | whether the mouse is down, which will always be 1 for onclick  
mod1 | number | nonzero if the Command (macOS) or Windows (Windows) key is held down  
shift | number | nonzero if the shift key is held down  
caps | number | nonzero if caps lock is enabled  
opt | number | nonzero if the option key is held down  
mod2 | number | nonzero if the control key is held down  
_optional_ pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | optional pointer event object containing additional event details (v8 only)  
### onkeydown
Receives keyboard key down events.
This behavior is only available in the new v8 javascript engine objects.
Implement this function to receive a callback when a keyboard key is pressed. Currently only key down events are supported. The function can return a nonzero value to indicate that the key event was consumed and should not be passed down the event chain.
```
onkeydown(keycode: number, textcharacter: number, updown: number, mod1: number, shift: number, caps: number, opt: number, mod2: number): number;

```
Name | Type | Description  
---|---|---  
keycode | number | the key code of the pressed key  
textcharacter | number | the text character associated with the key  
updown | number | whether the key is down (always 1 for keydown events currently)  
mod1 | number | nonzero if the Command (macOS) or Ctrl (Windows) key is held down  
shift | number | nonzero if the shift key is held down  
caps | number | nonzero if caps lock is enabled  
opt | number | nonzero if the option key is held down  
mod2 | number | nonzero if the control key is held down  
Return Value | number | nonzero if the key event was consumed and should not be passed down the event chain, otherwise 0  
#### Example
```
function onkeydown(keycode, textcharacter, updown, mod1, shift, caps, opt, mod2) {
    if (keycode == 27) { // Escape key
        post("Escape key pressed\n");
        return 1; // consume the event
    }
    return 0; // allow event to pass through
}

```

### onpointerdown
Receives pointer down events.
This behavior is only available in the new v8 javascript engine objects.
Implement this function to receive a callback when a pointer button is pressed.
```
onpointerdown(pointerevent: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | Pointer event object containing event details including position, pressure, tilt, rotation, and button states  
#### Example
```
function onpointerdown(pointerevent) {
    post("pointer down: type=" + pointerevent.pointerType + " id=" + pointerevent.pointerId +
         " buttons=" + pointerevent.buttons + " pressure=" + pointerevent.pressure + "\n");
}

```

### onpointerenter
Receives pointer enter events.
This behavior is only available in the new v8 javascript engine objects.
Implement this function to receive a callback when a pointer enters the object boundaries.
```
onpointerenter(pointerevent: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | Pointer event object containing event details  
#### Example
```
function onpointerenter(pointerevent) {
    post("pointer entered: type=" + pointerevent.pointerType + " id=" + pointerevent.pointerId + "\n");
}

```

### onpointerleave
Receives pointer leave events.
This behavior is only available in the new v8 javascript engine objects.
Implement this function to receive a callback when a pointer leaves the object boundaries.
```
onpointerleave(pointerevent: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | Pointer event object containing event details  
#### Example
```
function onpointerleave(pointerevent) {
    post("pointer left: type=" + pointerevent.pointerType + " id=" + pointerevent.pointerId + "\n");
}

```

### onpointermove
Receives pointer move events.
This behavior is only available in the new v8 javascript engine objects.
Implement this function to receive a callback when a pointer moves within the object boundaries.
```
onpointermove(pointerevent: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | Pointer event object containing event details including position, pressure, tilt, rotation, and button states  
#### Example
```
function onpointermove(pointerevent) {
    if (pointerevent.buttons != 0) {
        post("pointer moved while pressed: x=" + pointerevent.clientX + " y=" + pointerevent.clientY +
             " pressure=" + pointerevent.pressure + "\n");
    }
}

```

### onpointerup
Receives pointer up events.
This behavior is only available in the new v8 javascript engine objects.
Implement this function to receive a callback when a pointer button is released.
```
onpointerup(pointerevent: PointerEvent): void;

```
Name | Type | Description  
---|---|---  
pointerevent | [PointerEvent](https://docs.cycling74.com/apiref/js/pointerevent/ "PointerEvent") | Pointer event object containing event details  
#### Example
```
function onpointerup(pointerevent) {
    post("pointer up: type=" + pointerevent.pointerType + " id=" + pointerevent.pointerId +
         " buttons=" + pointerevent.buttons + "\n");
}

```

### onresize
Receives the new size of the object in width and height
```
onresize(width: number, height: number);

```
Name | Type | Description  
---|---|---  
width | number | the new width  
height | number | the new height  
### onwheel
Receives mouse wheel scroll events.
Implement this function to receive a callback when the mouse wheel is scrolled over the object.
```
onwheel(x: number, y: number, scrollx: number, scrolly: number, mod1: number, shift: number, caps: number, opt: number, mod2: number): void;

```
Name | Type | Description  
---|---|---  
x | number | x coordinate in object space  
y | number | y coordinate in object space  
scrollx | number | horizontal scroll amount  
scrolly | number | vertical scroll amount  
mod1 | number | nonzero if the Command (macOS) or Ctrl (Windows) key is held down  
shift | number | nonzero if the shift key is held down  
caps | number | nonzero if caps lock is enabled  
opt | number | nonzero if the option key is held down  
mod2 | number | nonzero if the control key (macOS) or right mouse button (Windows) is held down  
#### Example
```
function onwheel(x, y, scrollx, scrolly, mod1, shift, caps, opt, mod2) {
    post("wheel scroll at " + x + ", " + y + ": " + scrolly + "\n");
}

```

### outlet_array
Convert JS array to Max array and send through an outlet
This behavior is only available in the new v8 javascript engine objects. Alternatively, a JS array must be converted to a MaxArray instance and the message "array" followed by the MaxArray instance name may be sent out using the standard [jsthis.outlet()](https://docs.cycling74.com/apiref/js/jsthis/#outlet "jsthis.outlet\(\)") method -- e.g. outlet(0, "array", myarray.name);
```
outlet_array(n: number, array: Array): void;

```
Name | Type | Description  
---|---|---  
n | number | the outlet number, 0-indexed  
array | Array | JS array to send out of the outlet  
### outlet_dictionary
Convert JS object to Max dictionary and send through an outlet
The Max dictionary will match the hierarchy and contents of the JS object similar to if you serialized the JS object to JSON and then parsed the JSON into a Max dictionary. This behavior is only available in the new v8 javascript engine objects. Alternatively, a JS object must be converted to a Dict instance and the message "dictionary" followed by the Dict instance name may be sent out using the standard [jsthis.outlet()](https://docs.cycling74.com/apiref/js/jsthis/#outlet "jsthis.outlet\(\)") method -- e.g. outlet(0, "dictionary", mydict.name);
```
outlet_dictionary(n: number, dictionary: Object): void;

```
Name | Type | Description  
---|---|---  
n | number | the outlet number, 0-indexed  
dictionary | Object | JS Object to send out of the outlet  
### outlet_string
Convert JS string to Max string and send through an outlet
This behavior is only available in the new v8 javascript engine objects. Alternatively, a JS array must be converted to a MaxString instance and the message "string" followed by the MaxString instance name may be sent out using the standard [jsthis.outlet()](https://docs.cycling74.com/apiref/js/jsthis/#outlet "jsthis.outlet\(\)") method -- e.g. outlet(0, "string", mystring.name);
```
outlet_string(n: number, string: String): void;

```
Name | Type | Description  
---|---|---  
n | number | the outlet number, 0-indexed  
string | String | JS string to send out of the outlet  
### outlet
Send data through an outlet
If the outlet number if greater than the number of outlets, no output occurs.
If the argument to [jsthis.outlet()](https://docs.cycling74.com/apiref/js/jsthis/#outlet "jsthis.outlet\(\)") is a JavaScript object, it is passed as the Max message `jsobject` which is the address of the object. When `jsobject` followed by a number is sent to a `js` object, it is parsed and checked to see if the number specifies the address of a valid JavaScript object. If so, the word `jsobject` disappears and the function sees only the JavaScript object reference.
If the argument to [jsthis.outlet()](https://docs.cycling74.com/apiref/js/jsthis/#outlet "jsthis.outlet\(\)") is an array, it is unrolled one level and passed as a Max message or list (depending on whether the first element of the array is a number or string).
```
outlet(n: number, ...args: any[]): void;

```
Name | Type | Description  
---|---|---  
n | number | the outlet number, 0-indexed  
args | any[] | anything to send out of the outlet  
### paint
Define a custom paint function
This function is only available when using the jsui or v8ui objects. Do not call this function directly. Instead, call [MGraphics.redraw()](https://docs.cycling74.com/apiref/js/mgraphics/#redraw "MGraphics.redraw\(\)") to request that Max refresh the current drawing context on the next available frame. Within the context of this function, you can use [MGraphics](https://docs.cycling74.com/apiref/js/mgraphics/ "MGraphics") (or the older [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch")) global object to draw to the current graphics context.
```
paint(): void;

```

#### Example
Draw a red ellipse in the object background
```
function paint() {
    mgraphics.set_source_rgba(1, 0, 0, 1);
    mgraphics.ellipse(10, 10, 50, 40);
    mgraphics.fill();
}

function bang() {
    mgraphics.refresh();
}

```

### refresh
Copy the contents of this.sketch to the screen
This function is only available when using the jsui or v8ui objects. Call this function after drawing using the [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") object to move the contents of sketch to the screen. Must be called after making any changes to the drawing in order to see those changes. If you're using [MGraphics](https://docs.cycling74.com/apiref/js/mgraphics/ "MGraphics") to draw instead, use [MGraphics.redraw()](https://docs.cycling74.com/apiref/js/mgraphics/#redraw "MGraphics.redraw\(\)")
```
refresh(): void;

```

#### Example
Draw a ball at a randmo position when jsui gets a bang
```
function bang()
{
	with (Math) {
		with (sketch) {
			shapeslice(vslices);
			moveto((random()-0.5)*2,(random()-0.5)*2,(random()-0.5)*2);
			glcolor(random(),random(),random(),1);
			sphere(random()*0.4);
		}
	}
	refresh();
}

```

### save
Allow your script to embed state in a patcher file containing your `js` object and restore the state when the patcher is reloaded
Saving your state consists of storing a set of messages that your script will receive shortly after the `js` object containing it is recreated. These messages are stored using the [jsthis.embedmessage()](https://docs.cycling74.com/apiref/js/jsthis/#embedmessage "jsthis.embedmessage\(\)") which only words inside your save function.
```
save(): void;

```

#### Example
When the patch containing the `js` object is saved, preserve the current value of a variable
```
var numcowbells = 1;
function cowbells(a) {
    numcowbells = 1;
}

function save() {
    embedmessage("cowbells", numcowbells);
}

```

### setinletassist
Associates either a number, string, or function with a numbered inlet
If `-1` is passed as the inlet number, the object argument is used for all inlets. In order to produce any assistance text in the patcher window the assistance function needs to call the [jsthis.assist()](https://docs.cycling74.com/apiref/js/jsthis/#assist "jsthis.assist\(\)") method. For an example use, see [jsthis.setoutletassist()](https://docs.cycling74.com/apiref/js/jsthis/#setoutletassist "jsthis.setoutletassist\(\)"). The [jsthis.setinletassist()](https://docs.cycling74.com/apiref/js/jsthis/#setinletassist "jsthis.setinletassist\(\)") and [jsthis.setoutletassist()](https://docs.cycling74.com/apiref/js/jsthis/#setoutletassist "jsthis.setoutletassist\(\)") functions are best called in global code but can be called at any time. You can even replace the assistance function or string dynamically.
```
setinletassist(n: number, callback: Function): void;

```
Name | Type | Description  
---|---|---  
n | number | inlet number (0-indexed)  
callback | Function | function which calls the [jsthis.assist()](https://docs.cycling74.com/apiref/js/jsthis/#assist "jsthis.assist\(\)") method  
### setoutletassist
Associates either a number, string, or function with a numbered outlet
If `-1` is passed as the outlet number, the object argument is used for all inlets. In order to produce any assistance text in the patcher window the assistance function needs to call the [jsthis.assist()](https://docs.cycling74.com/apiref/js/jsthis/#assist "jsthis.assist\(\)") method. The [jsthis.setinletassist()](https://docs.cycling74.com/apiref/js/jsthis/#setinletassist "jsthis.setinletassist\(\)") and [jsthis.setoutletassist()](https://docs.cycling74.com/apiref/js/jsthis/#setoutletassist "jsthis.setoutletassist\(\)") functions are best called in global code but can be called at any time. You can even replace the assistance function or string dynamically.
```
setoutletassist(n: number, callback: Function): void;

```
Name | Type | Description  
---|---|---  
n | number | outlet number (0-indexed)  
callback | Function | function which calls the [jsthis.assist()](https://docs.cycling74.com/apiref/js/jsthis/#assist "jsthis.assist\(\)") method  
#### Example
```
outlets = 2;

function describe(n) {
    assist("This is outlet number: ", n);
}

setoutletassist(-1, describe);

```

### setvalueof
Permit pattr and related objects to attach to and set an object's current value
Values passed will be of type `number` or `string`. For a value that consists of more than one `number` or `string`, the [jsthis.setvalueof()](https://docs.cycling74.com/apiref/js/jsthis/#setvalueof "jsthis.setvalueof\(\)") method will receive multiple arguments. The `jsthis` `arrayfromargs` method is useful to handle values that can contain a variable number of elements.
```
setvalueof(...args: number[] | string[]): void;

```
Name | Type | Description  
---|---|---  
args | number[] | string[] | values to set  
#### Example
`setvalueof` works for other objects, not just `js` and `jsui`
```
var flonum = this.patcher.newobject("flonum");
flonum.setvalueof();
post("value: " + flonum.getvalueof() + "\n");

```

