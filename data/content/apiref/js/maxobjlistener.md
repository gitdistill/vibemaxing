---
description: A listener for changes in aMaxobjobject.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/maxobjlistener/
title: class MaxobjListener
---

# class MaxobjListener
A listener for changes in a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") object.
The MaxobjListener object listens for changes to a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") object's value, or changes to a specified attribute of a [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") object. When a change occurs, a user-specified function will be called. The object also provides methods for getting and setting the value of the observed value or attribute.
For convenience, the `MaxobjListener` object is a property of the [MaxobjListenerData](https://docs.cycling74.com/apiref/js/maxobjlistenerdata/ "MaxobjListenerData") argument passed to the callback function. To access the `ParameterListener` from within its function, use [MaxobjListenerData.listener](https://docs.cycling74.com/apiref/js/maxobjlistenerdata/#listener "MaxobjListenerData.listener").
#### Example
```
function valuechanged(data) {
    post("value changed!\n");
    if (data.attrname) {
        post("attrname: " + data.attrname + "\n");
    }
    post("new value: " + data.value + "\n");
}

var ob = this.patcher.getnamed("someobject");
var l = new MaxobjListener(ob, "patching_rect", valuechanged);

```

## Constructors
```
new MaxobjListener(object: Maxobj, fn: Function);

```

Constructs a new instance of the `MaxobjListener` class
Without an attribute name provided, the listener will observe the value of the object itself. Not every Max object has an observable value -- objects compatible with the pattr family of Max objects can be observed in this fashion. Practically, that means nearly every UI object as well as a handful of normal Max box objects (including js, pattr and dict). Attributes can be observed for any Maxobj which has attributes.
Parameter | Type | Description  
---|---|---  
object | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | the object to attach a listener to  
fn | Function | the callback function which takes a [MaxobjListenerData](https://docs.cycling74.com/apiref/js/maxobjlistenerdata/ "MaxobjListenerData") as an argument  
```
new MaxobjListener(object: Maxobj, attrName: string, fn: Function);

```

Create a MaxobjListener that observes a specific attribute
Parameter | Type | Description  
---|---|---  
object | [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") | the object to attach a listener to  
attrName | string | the attribute to listen to  
fn | Function | the callback function which takes a [MaxobjListenerData](https://docs.cycling74.com/apiref/js/maxobjlistenerdata/ "MaxobjListenerData") as an argument  
## Properties
### attrname string read-only
An attribute to observe for changes, if desired
### maxobj [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") read-only
The [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") to observe
### silent number
Whether to execute the callback function in response to calling [MaxobjListener.setvalue()](https://docs.cycling74.com/apiref/js/maxobjlistener/#setvalue "MaxobjListener.setvalue\(\)") from this `MaxobjListener`
## Methods
### getvalue
Get the value of the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") or its specified attribute
```
getvalue(): number | number[] | string;

```
Name | Type | Description  
---|---|---  
Return Value | number | number[] | string |   
### setvalue_silent
Set the value of a the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") or its specified attribute, but don't execute the callback function
```
setvalue_silent(value: number): void;

```
Name | Type | Description  
---|---|---  
value | number | the new value  
### setvalue
Set the value of the [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") or its specified attribute
```
setvalue(value: any): void;

```
Name | Type | Description  
---|---|---  
value | any | the new value
