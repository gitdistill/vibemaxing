---
description: Provides a list of named parameter objects within a patcher hierarchy as well as information about specific parameter objects. It can also notify when parameter objects are added or removed from a patcher hierarchy.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/parameterinfoprovider/
title: class ParameterInfoProvider
---

# class ParameterInfoProvider
Provides a list of named parameter objects within a patcher hierarchy as well as information about specific parameter objects. It can also notify when parameter objects are added or removed from a patcher hierarchy.
#### Example
```
function paramschanged(data) {
    post("something was added or removed - getting a new list\n");
    if (data.added.length) {
        post(data.added.join(", ") + "added\n");
    }
    if (data.removed.length) {
        post(data.removed.join(", "), + "removed\n");
    }
}
pip = new ParameterInfoProvider(paramschanged);

```

## Constructors
```
new ParameterInfoProvider(fn?: Function);

```

Constructs a new instance of the `ParameterInfoProvider` class
Parameter | Type | Description  
---|---|---  
_optional_ fn | Function | a callback function to execute when receiving parameter change notifications which takes a [ParameterInfoProviderData](https://docs.cycling74.com/apiref/js/parameterinfoproviderdata/ "ParameterInfoProviderData") as an argument  
## Methods
### getinfo
Get parameter info like its type and range
The exact contents of the object will vary depending on the type of the parameter and will need to be enumerated. The object always contains a property `maxobj` which is the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") for the Max object hosting the parameter.
```
getinfo(paramName: string): any[];

```
Name | Type | Description  
---|---|---  
paramName | string | the parameter to find info for  
Return Value | any[] |   
#### Example
```
var pip = new ParameterInfoProvider();
var info = pip.getinfo("live.dial");
for (var i in info) {
    post(i + ": " + info[i] + "\n");
}

```

for a default `live.dial` object, this will print
```
js: longname: live.dial
js: shortname: live.dial
js: scriptname: live.dial
js: type: float
js: visibility: automated
js: min: 0
js: max: 127
js: exponent: 1
js: maxobject: [object Maxobj]

```

### getnames
Get a list of parameter objects' names from the patcher hierarchy
```
getnames(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] | 
