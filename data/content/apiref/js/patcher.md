---
description: A JavaScript representation of a Max patcher.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/patcher/
title: class Patcher
---

# class Patcher
A JavaScript representation of a Max patcher.
You can find, create, modify, and iterate through objects within a patcher, send messages to a patcher that you would use with the thispatcher object, and more.
There are currently three ways to get a [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher"):
1. Use the constructor method
2. Access the patcher property of `jsthis` (e.g. `this.patcher`)
3. Use the [Maxobj.subpatcher()](https://docs.cycling74.com/apiref/js/maxobj/#subpatcher "Maxobj.subpatcher\(\)") method
Any message to a patcher that you can send in Max (via the thispatcher object), you can send in JavaScript.
#### Example
```
p = this.patcher;
p.fullscreen(1) // make the patcher take up the whole screen
p.dirty() // make an editable patcher dirty

```

## Constructors
```
new Patcher();

```

Constructs a new instance of the `Patcher` class with default window coordinates (100, 100, 400, 400)
```
new Patcher(left: number, top: number, bottom: number, right: number);

```

Constructs a new instance of the `Patcher` class
Parameter | Type | Description  
---|---|---  
left | number | x-coordinate of the new top-left corner  
top | number | y-coordinate of the new top-left corner  
bottom | number | y-coordinate of the new bottom-right corner  
right | number | x-coordinate of the new bottom-right corner  
## Properties
### accentcolor number[4] read-only
The accent color in the current style
### bgcolor number[4] read-only
The background color in the current style
### bgfillcolor [Dict](https://docs.cycling74.com/apiref/js/dict/ "Dict") read-only
The object background color in the current style
### box [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") read-only
If the patcher is a subpatcher, the `box` property returns the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") that contains it.
#### Example
To traverse up to the top-level patcher:
```
var prev = 0;
var owner = this.patcher.box;
while (owner) {
    prev = owner;
    owner = owner.patcher.box;
}
if (prev) post("top patcher is", prev.patcher.name)

```

### bubble_bgcolor number[4] read-only
Bubble background color in the current style
### bubble_outlinecolor number[4] read-only
Bubble outline color in the current style
### clearcolor number[4] read-only
Clear color in the current style
### color number[4] read-only
The object color in the current style
### count number read-only
Number of objects in the patcher
### darkcolor number[4] read-only
Dark color in the current style
### editing_bgcolor number[4] read-only
Unlocked patcher background color in the current style
### elementcolor number[4] read-only
The element color in the current style
### filepath string read-only
The patcher's file path on disk
### firstobject [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") read-only
If the patcher contains objects, this is the first one in its list. You can iterate through all objects in a patcher using the [Maxobj.nextobject](https://docs.cycling74.com/apiref/js/maxobj/#nextobject "Maxobj.nextobject") property.
### lightcolor number[4] read-only
Light color in the current style
### locked_bgcolor number[4] read-only
Locked patcher background color in the current style
### locked boolean
Whether the patcher is locked
This property is read-only in the runtime version of Max.
### maxclass string read-only
Returns "patcher"
### name string
The patcher's name which is its window title (without any brackets that appear for subpatchers)
### parentclass string read-only
Get the Max class name of the parent object if `this.patcher` is a subpatcher, or a nil value if this is a top-level patcher
#### Example
```
function bang() {
    var pclass = this.patcher.parentclass;
    if (pclass) {
        post("The parent patcher class is " + pclass);
    } else {
        post("This is a top-level patcher");
    }
}

```

### parentpatcher [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") | undefined read-only
Get the parent patcher if `this.patcher` is a subpatcher, otherwise a nil value
### patchlinecolor number[4] read-only
Patch cord color in the current style
### scrolloffset [number, number]
The x-y coordinate array for the scroll offset of a patcher window
### scrollorigin [number, number]
The x-y coordinate array of the patcher's fixed origin
### selectioncolor number[4] read-only
The selection color in the current style
### stripecolor number[4] read-only
Stripe color in the current style
### syntax_attrargcolor number[4] read-only
Syntax color for attribute arguments in the current style
### syntax_attributecolor number[4] read-only
Syntax color for object attributes in the current style
### syntax_objargcolor number[4] read-only
Syntax color for object arguments in the current style
### syntax_objectcolor number[4] read-only
Syntax color for object names in the current style
### textcolor_inverse number[4] read-only
The inverse text color in the current style
### textcolor number[4] read-only
The text color in the current style
### wind [Wind](https://docs.cycling74.com/apiref/js/wind/ "Wind") read-only
Get the [Wind](https://docs.cycling74.com/apiref/js/wind/ "Wind") associated with the patcher
## Methods
### apply
For all objects in a patcher, call a given function with each object's [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") as an argument
Does not recurse into subpatchers.
```
apply(fn: Function): void;

```
Name | Type | Description  
---|---|---  
fn | Function | A callback function  
#### Example
The following prints the name of each object's class:
```
function printobj(obj) {
    post(obj.maxclass);
}
this.patcher.apply(printobj);

```

### applydeep
For all objects in a patcher, recursing into subpatchers, call a given function with each object's [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") as an argument
```
applydeep(fn: Function): void;

```
Name | Type | Description  
---|---|---  
fn | Function | A callback function  
### applydeepif
For all objects in a patcher, recursing into subpatchers, call a given function with each object's [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") as an argument if a test function returns `true`
```
applydeepif(apply_fn: Function, test_fn: Function): void;

```
Name | Type | Description  
---|---|---  
apply_fn | Function |   
test_fn | Function |   
### applyif
For all objects in a patcher, call a given function with each object's [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") as an argument if a test function returns `true`
Does not recurse into subpatchers.
```
applyif(applyFn: Function, testFn: Function): void;

```
Name | Type | Description  
---|---|---  
applyFn | Function | A callback function which takes a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") and runs if `testFn` returns `true`  
testFn | Function | A function which takes a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") as an argument and returns a boolean  
#### Example
The following prints the name of each object's class if the object is hidden
```
function printhidden(obj) {
    post(obj.maxclass);
}
function ishidden(obj) {
    return obj.hidden;
}
this.patcher.applyif(printhidden, ishidden);

```

### bringtofront
Move an object to the front of the current layer (background or foreground)
You can change the layer by setting the [Maxobj.background](https://docs.cycling74.com/apiref/js/maxobj/#background "Maxobj.background") property.
```
bringtofront(object: Maxobj): void;

```
Name | Type | Description  
---|---|---  
object | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | the object to move  
### connect
Connect two `Maxobj` objects in a patcher
Indices for the outlet and inlet arguments start at 0 for the leftmost inlet or outlet.
```
connect(fromObj: Maxobj, outlet: number, toObj: Maxobj, inlet: number): void;

```
Name | Type | Description  
---|---|---  
fromObj | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | Source object  
outlet | number | Index of outlet from source object  
toObj | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | Destination object  
inlet | number | Index of inlet of destination object  
#### Example
```
var p = this.patcher;
var a = p.newobject("toggle", 122, 90, 15, 0);
var b = p.newobject("toggle", 122, 140, 15, 0);
p.connect(a, 0, b, 0);

```

### disconnect
Disconnect two connected `Maxobj` objects in a patcher
Indices for the outlet and inlet arguments start at 0 for the leftmost inlet or outlet.
```
disconnect(fromObj: Maxobj, outlet: number, toObj: Maxobj, inlet: number): void;

```
Name | Type | Description  
---|---|---  
fromObj | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | Source object  
outlet | number | Index of outlet from source object  
toObj | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | Destination object  
inlet | number | Index of inlet of destination object  
#### Example
```
var p = this.patcher;
var a = p.newobject("toggle", 122, 90, 15, 0);
var b = p.newobject("toggle", 122, 140, 15, 0);
p.connect(a, 0, b, 0);
p.disconnect(a, 0, b, 0);

```

### getattr
Get the value of a specified patcher attribute
```
getattr(attrname: string): string[];

```
Name | Type | Description  
---|---|---  
attrname | string | the attribute name  
Return Value | string[] |   
### getattrattr
Get the value of a specified patcher attribute's attribute
This method is only available in the new v8 javascript engine objects.
```
getattrattr(attrName: string, attrAttrName: string): number | number[] | string;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
attrAttrName | string | the attribute name  
Return Value | number | number[] | string |   
### getattrnames
Get an array of all available attributes for the patcher
```
getattrnames(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] |   
### getlogical
Collect all objects in a patcher which, when passed to a test function, cause that function to return true
```
getlogical(testFn: Function): Maxobj[] | undefined;

```
Name | Type | Description  
---|---|---  
testFn | Function | A function which takes a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") as an argument and returns a boolean  
Return Value |  [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj")[] | undefined |   
#### Example
```
function logical(a) {
    if (a) {
        return true;
    } else {
        return false;
    }
}

function loadbang() {
    // uses the return value as an array
    var found = patcher.getlogical(logical);
    if (found && found.length) {
        for (var i = 0; i < found.length; i++) {
            post(found[i].maxclass + ": " + found[i].rect + "\n");
        }
    }
}

function bang() {
    loadbang();
}

```

### getnamed
Get the first object found in a patcher with a given name
The name is the local varname specified via the Object Name... menu or the `varname` property in the Inspector.
```
getnamed(name: string): Maxobj;

```
Name | Type | Description  
---|---|---  
name | string | The name of the object to retrieve  
Return Value | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") |   
### hiddenconnect
Connect two `Maxobj` objects in a patcher with a hidden patch cord
Indices for the outlet and inlet arguments start at 0 for the leftmost inlet or outlet.
```
hiddenconnect(fromObj: Maxobj, outlet: number, toObj: Maxobj, inlet: number): void;

```
Name | Type | Description  
---|---|---  
fromObj | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | Source object  
outlet | number | Index of outlet from source object  
toObj | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | Destination object  
inlet | number | Index of inlet of destination object  
#### Example
```
var p = this.patcher;
var a = p.newobject("toggle", 122, 90, 15, 0);
var b = p.newobject("toggle", 122, 140, 15, 0);
p.hiddenconnect(a, 0, b, 0);

```

### newdefault
Create a new object at a specified location
```
newdefault(left: number, top: number, classname: string, ...args: any[]): Maxobj;

```
Name | Type | Description  
---|---|---  
left | number | the x-coordinate of the new object's top-left corner  
top | number | the y-coordinate of the new object's top-left corner  
classname | string | the classname of the Max object to create  
args | any[] | arguments to pass to the Max object  
Return Value | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") |   
#### Example 1
```
var obj = patcher.newdefault(122, 90, "toggle");

```

#### Example 2
The `newdefault` method also accepts additional arguments for non UI objects that represent the created object's typed-in arguments.
```
var obj = patcher.newdefault(122, 90, "pack", "rgb", 255, 128, 64);

```

### newobject
Create a new Max object
```
newobject(classname: string, ...args: any[]): Maxobj;

```
Name | Type | Description  
---|---|---  
classname | string | the classname of the Maxobj to create  
args | any[] | any arguments to pass to the Maxobj  
Return Value | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") |   
#### Example
```
a = patcher.newobject("toggle", 122, 90, 15, 0);

```

### remove
Remove a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") from the patcher
```
remove(object: Maxobj): void;

```
Name | Type | Description  
---|---|---  
object | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | The [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") to remove  
### sendtoback
Send an object to the back of the current layer (background or foreground)
You can change the layer by setting the [Maxobj.background](https://docs.cycling74.com/apiref/js/maxobj/#background "Maxobj.background") property.
```
sendtoback(object: Maxobj): void;

```
Name | Type | Description  
---|---|---  
object | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | the object to move  
### setattr
Set the value of a specified patcher attribute
```
setattr(attrname: string, value: any): void;

```
Name | Type | Description  
---|---|---  
attrname | string | the attribute name  
value | any | the value of the attribute  
### setattrdefault
Set the value of a specified patcher attribute to its default value (if a default value is defined)
This method is only available in the new v8 javascript engine objects.
```
setattrdefault(attrName: string): void;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name
