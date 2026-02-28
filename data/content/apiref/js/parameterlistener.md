---
description: A listener for changes in named parameters.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/parameterlistener/
title: class ParameterListener
---

# class ParameterListener
A listener for changes in named parameters.
The `ParameterListener` listens for changes to the value of a named Max parameter. When a change occurs, a user-specified callback function will be called. The object also provides methods for getting and setting the value of the observed parameter.
For convenience, the `ParameterListener` object is a property of the [ParameterListenerData](https://docs.cycling74.com/apiref/js/parameterlistenerdata/ "ParameterListenerData") argument passed to the callback function. To access the `ParameterListener` from within its function, use [ParameterListenerData.listener](https://docs.cycling74.com/apiref/js/parameterlistenerdata/#listener "ParameterListenerData.listener").
#### Example
```
function valuechanged(data) {
    post("parameter value changed: " + data.name + "\n");
    post("new value: " + data.value + "\n");
}

var l = new ParameterListener("myParameter", valuechanged);

```

## Constructors
```
new ParameterListener(paramName: string, fn: Function);

```

Constructs a new instance of the `ParameterListener` class
Parameter | Type | Description  
---|---|---  
paramName | string | the parameter name  
fn | Function | the callback function which takes a [ParameterListenerData](https://docs.cycling74.com/apiref/js/parameterlistenerdata/ "ParameterListenerData") as an argument  
## Properties
### name string read-only
The name of the parameter to observe
### silent number
Whether to execute the callback function in response to calling [ParameterListener.setvalue()](https://docs.cycling74.com/apiref/js/parameterlistener/#setvalue "ParameterListener.setvalue\(\)") from this `ParameterListener`
## Methods
### getvalue
Get the value of a parameter
```
getvalue(): number | number[] | string;

```
Name | Type | Description  
---|---|---  
Return Value | number | number[] | string |   
### setvalue_silent
Set the value of a parameter, but don't execute the callback function
```
setvalue_silent(value: number): void;

```
Name | Type | Description  
---|---|---  
value | number | the new parameter value  
### setvalue
Set the value of a parameter
```
setvalue(value: any): void;

```
Name | Type | Description  
---|---|---  
value | any | the new parameter value
