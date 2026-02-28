---
description: Bind a Maxstringobject
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/maxstring/
title: class MaxString
---

# class MaxString
Bind a Max `string` object
Create a MaxString object when you want to bind to a Max `string` object, either because you want to fetch its value or when you want to modify its contents. To manipulate the contents of the string, get the value of the string using .stringify and then use regular JavaScript string functions.
#### Example 1
```
function string(str_name) {
	var max_str = new MaxString();
	max_str.name = str_name; // binds to the Max `string` by name
	var contents = max_str.stringify(); // read the value of the string
}

```

#### Example 2
```
function lower(str_name) {
	var max_str = new MaxString();
	max_str.name = str_name; // binds to the Max `string` by name
	var js_str = max_str.stringify(); // get the value of the string
	js_str = js_str.toLowerCase(); // regular JavaScript string functions
	max_str.parse(js_str); // set the string's new value
}

```

## Constructors
```
new MaxString(initial_value: string?, ...attr_pairs: string?);

```

Create a new MaxString
You can set the name of the string either by passing the name after the argument "name", or you can set the .name property after creating the MaxString objects.
Parameter | Type | Description  
---|---|---  
initial_value | string? | initial value  
attr_pairs | string? | usually the string "name" followed by the name of the string  
#### Example
```
// These both create a string that binds to the same named string.
var my_str = new MaxString("initial_value", "@name", "fred");

var my_str2 = new MaxString("initial_value");
my_str2.name = "fred";

```

## Properties
### name string
Get and set the name of the MaxString
Will bind to an existing Max string with the same name
## Methods
### parse
Update the value of the MaxString
```
parse(value: any);

```
Name | Type | Description  
---|---|---  
value | any | value to parse into a string  
### stringify
Get the current value of the MaxString as a string
```
stringify(): string;

```
Name | Type | Description  
---|---|---  
Return Value | string | The current value of the MaxString
