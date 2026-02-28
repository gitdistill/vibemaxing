---
description: Sends a message to the named Max object.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/messnamed/
title: function messnamed
---

# function messnamed
Sends a message to the named Max object.
A named Max object is an object associated with a global symbol (not an object with a patcher-specific name). For example, Max receive objects are bound to global symbols. The code in the first example sends the message bang to the named object flower.
The arguments passed to the object can be individual arguments or an array.
```
export declare function messnamed(objectName: string, selector: string, args: any): void;

```
Name | Type | Description  
---|---|---  
objectName | string | the name of the object to send the message to  
selector | string | the name of the object method to call  
args | any | the arguments to pass to the object method  
#### Example 1
```
messnamed("flower", "bang");

```

#### Example 2
```
messnamed("flower", "count", 1, 2, 3);
messnamed("flower", "count", [1, 2, 3]);

```

