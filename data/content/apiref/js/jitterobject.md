---
description: A JavaScript representation of a Jitter object in a patcher.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/jitterobject/
title: class JitterObject
---

# class JitterObject
A JavaScript representation of a Jitter object in a patcher.
#### Example
```
var win = new JitterObject("jit.window", "my_window");
var rend = new JitterObject("jit.gl.render", win.getregisteredname());

```

## Constructors
```
new JitterObject(objectName: string, ...params: any);

```

Constructs a new instance of the `JitterObject` class
Parameter | Type | Description  
---|---|---  
objectName | string | name of Jitter object  
params | any | parameter and attributes  
## Methods
### freepeer
Delete the JitterObject
```
freepeer(): void;

```

### getregisteredname
Get the registered name of the JitterObject
```
getregisteredname(): string;

```
Name | Type | Description  
---|---|---  
Return Value | string | 
