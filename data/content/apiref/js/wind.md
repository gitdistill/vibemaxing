---
description: A property of thePatcherwhich represents its window.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/wind/
title: class Wind
---

# class Wind
A property of the [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") which represents its window.
You cannot create a new [Wind](https://docs.cycling74.com/apiref/js/wind/ "Wind") or access other types of windows (such as that of a Max table object).
## Properties
### assoc [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") read-only
The [Patcher](https://docs.cycling74.com/apiref/js/patcher/ "Patcher") object associated with the window.
### assocclass string read-only
The Max class of the object associated with the window.
### dirty boolean
Whether the window's contents have been modified.
This property is read-only in the runtime version of Max.
### hasgrow boolean
Whether the window has a grow area.
### hashorizscroll boolean read-only
Whether the window has a horizontal scroll bar.
### hastitlebar boolean
Whether the window has a title bar.
### hasvertscroll boolean read-only
Whether the window has a vertical scroll bar.
### haszoom boolean
Whether the window has a zoom box.
### location [number, number, number, number]
An array of the four coordinates (left, top, right, bottom) representing the window's location in global coordinates.
### next [Wind](https://docs.cycling74.com/apiref/js/wind/ "Wind") read-only
The [Wind](https://docs.cycling74.com/apiref/js/wind/ "Wind") object of the next patcher visible in the application's list of windows. The first [Wind](https://docs.cycling74.com/apiref/js/wind/ "Wind") object can be accessed using the [Max.frontpatcher](https://docs.cycling74.com/apiref/js/max/#frontpatcher "Max.frontpatcher") `wind` property.
### size [number, number]
An array of two coordinates (width, height) representing the window's size
### title string
The window's title
### visible boolean
Whether the window is visible
## Methods
### bringtofront
Move the window in front of all other windows.
```
bringtofront(): void;

```

### scrollto
Scroll the window.
```
scrollto(x: number, y: number): void;

```
Name | Type | Description  
---|---|---  
x | number | The x-coordinate of the new top-left corner  
y | number | The y-coordinate of the new top-left corner  
### sendtoback
Move the window behind all other windows
```
sendtoback(): void;

```

### setlocation
Set the global location of the window.
```
setlocation(left: number, top: number, bottom: number, right: number): void;

```
Name | Type | Description  
---|---|---  
left | number | x-coordinate of the new top-left corner  
top | number | y-coordinate of the new top-left corner  
bottom | number | y-coordinate of the new bottom-right corner  
right | number | x-coordinate of the new bottom-right corner
