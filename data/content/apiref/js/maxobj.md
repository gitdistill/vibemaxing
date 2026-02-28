---
description: A JavaScript representation of a Max object in a patcher.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/maxobj/
title: class Maxobj
---

# class Maxobj
A JavaScript representation of a Max object in a patcher.
Perhaps the most powerful thing about a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") is that you can send any message to a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") that you can send to a Max object. For example, if you had a number box [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") and you wanted to set its value to 23 without outputting the value, you could do this:
```
n.set(23);

```

Note that certain words such as `int`, `float`, and `delete` are keywords in JavaScript, and you will need to use either array notation or the message method for such reserved words. For example:
```
n.message("int", 23);
n["int"](23);

```

## Properties
### background boolean
Whether the object is in the patchers background layer
### boxtext string read-only
The text contained in the object box (if present)
This property is only available in the new v8 javascript engine objects.
### canhilite boolean read-only
Whether the object can be selected for text entry
A number box would be one example of an object which would return `true`
### colorindex number
**This API is deprecated**
If the object is set to use one of the standard 16 colors, the index of the color
### hidden boolean
Whether the object is hidden in a locked patcher
### ignoreclick boolean
Whether the object ignores clicks
### js object read-only
If the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") refers to an object that is a `js` Max class, this returns the associated `jsthis` object
### maxclass string read-only
The Max class
This is different from the JavaScript class ("Maxobj") which is accessed via the standard class property.
### nextobject [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | undefined read-only
The next object in the patcher's list of objects, otherwise nil
### patchcords object read-only
An object containing two arrays, `inputs`, and `outputs`, each of which may contain [MaxobjConnection](https://docs.cycling74.com/apiref/js/maxobjconnection/ "MaxobjConnection") objects
### patcher [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") read-only
The [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") object that contains the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj")
### rect [number, number, number, number]
The location of an object in a patcher (left, top, right, bottom)
When the object's rectangle is changed, it will move on screen if it's visible.
### selected boolean read-only
Whether the object is selected in an unlocked patcher window
### valid boolean read-only
Whether the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") refers to a valid Max object
A [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") could eventually refer to an object that no longer exists if the underlying Max object is freed. The valid property can be used to test for this condition.
### varname string
The patcher-specific name of the object as set in the inspector or via the Object Name... menu option
## Methods
### getattr
Get the value of an attribute
```
getattr(attrName: string): number | number[] | string;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
Return Value | number | number[] | string |   
### getattrattr
Get the value of an attribute's attribute
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
Get all available attributes for the object
```
getattrnames(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] |   
### getboxattr
Get the value of the object's box attribute
```
getboxattr(attrName: string): number | number[] | string;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
Return Value | number | number[] | string |   
### getboxattrattr
Get the value of the object's box attribute's attribute
This method is only available in the new v8 javascript engine objects.
```
getboxattrattr(attrName: string, attrAttrName: string): number | number[] | string;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
attrAttrName | string | the attribute name  
Return Value | number | number[] | string |   
### getboxattrnames
Get the names of all available attributes for the object's box
```
getboxattrnames(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] |   
### help
Open a help file describing an object, if it exists
```
help(): void;

```

### message
Send the object a message with any additional arguments
This is useful for sending messages to objects which dynamically dispatch messages with the `anything` message like `js`, `jsui`, `lcd`, and others.
```
message(message: string, ...args: any[]): void;

```
Name | Type | Description  
---|---|---  
message | string | the message to send  
args | any[] | any arguments for the message  
### setattr
Set the value of an attribute
```
setattr(attrName: string, value: number | number[] | string): void;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
value | number | number[] | string | the new attribute value  
### setattrdefault
Set the value of an attribute to its default value (if a default value is defined)
This method is only available in the new v8 javascript engine objects.
```
setattrdefault(attrName: string): void;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
### setboxattr
Set the value of a box attribute
```
setboxattr(attrName: string, value: number | number[] | string): void;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
value | number | number[] | string | the new attribute value  
### setboxattrdefault
Set the value of the object's box attribute to its default value (if a default value is defined)
This method is only available in the new v8 javascript engine objects.
```
setboxattrdefault(attrName: string): void;

```
Name | Type | Description  
---|---|---  
attrName | string | the attribute name  
### subpatcher
If the object contains a patcher, returns a [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher"), otherwise nil
```
subpatcher(index?: number): Patcher | undefined;

```
Name | Type | Description  
---|---|---  
_optional_ index | number | an instance number (only used with `poly~`)  
Return Value |  [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") | undefined |   
### understands
Get whether the object has an entry in its message list for a given string
If the entry is not a message that can be sent by a user within Max (i.e. it's a C-level "untyped" message), `false` is returned. This doesn't work for messages which are dynamically dispatched with the `anything` message, as is the case for instances of `js`, `jsui`, `lcd`, and others.
```
understands(message: string): boolean;

```
Name | Type | Description  
---|---|---  
message | string | an object message  
Return Value | boolean | 
