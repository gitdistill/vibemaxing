---
description: Global object for sharing data between Max JavaScript instances.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/global/
title: class Global
---

# class Global
Global object for sharing data between Max JavaScript instances.
Each Global object is a reference to a shared storage object. Creating two Global objects with the same namespace will share stored properties. Properties stored in a Global object can be accessed in Max, from outside of JavaScript.
#### Example 1
```
var g = new Global("name");
g.bob = 12;
var h = new Global("name");
post(h.bob); // 12

```

You can send messages to a named Global object from Max, using a message object.
#### Example 2
```
; xyz height 42
// Put this in a message box to set the property `height` of the Global object
// named `xyz` to the value 42.

; xyz frank x y z
// Set the value of `frank` of the Global object `xyz` to the string array ["x", "y", "z"].

; xyz sendnamed height dest
// Send the value of `height` of the Global object `xyz` to all receive objects named `dest`.

```

## Constructors
```
new Global(namespace: string);

```

Constructs a new instance of the `Global` class
Parameter | Type | Description  
---|---|---  
namespace | string | Namespace identifier  
## Methods
### sendnamed
Forward a property to receive objects
Forward the value of a property to named `receive` objects. The `target` of `sendnamed` is the name of a `receive` object, in which case every `receive` object with that name will receive the value of the named property.
```
sendnamed(target: string, propertyName: string): void;

```
Name | Type | Description  
---|---|---  
target | string | Name of a `receive` object  
propertyName | string | Identifier for a property stored in the Global object  
#### Example
```
var g = new Global("xyz");
g.ethyl = 1000;
g.sendnamed("fred", "ethyl");
// every [receive fred] will output 1000

```

