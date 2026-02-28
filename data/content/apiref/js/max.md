---
description: Singleton Max object, controlling the Max environment.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/max/
title: class Max
---

# class Max
Singleton Max object, controlling the Max environment.
Use the singleton instance of this object to control the Max environment. In the context of JavaScript executed in Max, the global `Max` singleton is always bound to an object named `max`.
#### Example 1
```
var arch = max.arch;
// The max object is already bound to the singleton Max object

post(arch);
// Prints the architecture of the current Max application.

```

In addition to the properties and methods described here, you can also use the global Max object to call methods as defined in [Controlling Max with Messages](https://docs.cycling74.com/userguide/controlling_max_with_messages/ "Controlling Max with Messages").
#### Example 2
```
// Message box contents:
; max preempt 1

// JavaScript equivalent:
max.preempt(1);

```

## Properties
### apppath string read-only
The pathname of the Max application
### arch "arm64" | "x86" | "x64" read-only
The architecture of the Max application
### cmdkeydown number read-only
Command key state
1 if the command (Macintosh) or control (Windows) key is currently held down.
### ctrlkeydown number read-only
Control key state
1 if the control key is currently held down.
### frontpatcher [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") read-only
The Patcher object of the frontmost patcher window
The Patcher object of the frontmost patcher window, or a nil value if no patcher window is visible. You can traverse the list of open patcher windows with the next property of a [Wind](https://docs.cycling74.com/apiref/js/wind/ "Wind") object.
### isplugin number read-only
Whether the js object is in a plugin
Will be 1 if the `js` object is in a plugin, and 0 otherwise. This will generally only be 1 if the `js` object is loaded as a Max device in a Max `vst~` object.
### isruntime number read-only
True if the current Max environment does not allow editing.
Returns 1 if the currently executing Max application environment does not allow editing, 0 if it does.
### loadbangdisabled number read-only
True if the user disabled loadbang.
1 if the user has disabled loadbang for the currently loading patch. If your object implements a loadbang method, it can test this property and choose to do nothing if it is true.
### optionkeydown number read-only
Option/alt key state
1 if the option (Macintosh) or alt (Windows) key is currently held down
### os string read-only
The name of the operating system
The name of the platform (e.g., “windows” or “macintosh”)
### osversion string read-only
The current OS version number
### shiftkeydown string read-only
Shift key state
1 if the shift key is currently held down
### time number read-only
Current scheduler time in milliseconds.
Will be a floating point value.
### version string read-only
Max application version number
Will be in string form, like "835"
## Methods
### getattr
Get the value of the named attribute
```
getattr(name: string): number | string | any[];

```
Name | Type | Description  
---|---|---  
name | string | the name of the attribute to retrieve  
Return Value | number | string | any[] | the value of the attribute, as an array if the attribute value is a list  
### getattrnames
Available attributes of the Max global object
```
getattrnames(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] | the available attributes  
### getcolor
Get the value of the named color in the current theme
```
getcolor(name: string): number[4] | Dict;

```
Name | Type | Description  
---|---|---  
name | string | the name of the color to retrieve  
Return Value | number[4] | [Dict](https://docs.cycling74.com/apiref/js/dict/ "Dict") | the value of the color, possibly as a gradient dictionary  
### setattr
Set the value of the named attribute
```
setattr(name: string, value: any): void;

```
Name | Type | Description  
---|---|---  
name | string | the name of the attribute to set  
value | any | the value of the attribute to set
