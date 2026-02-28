---
description: Bind to a Maxpolybuffer~object.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/polybuffer/
title: class PolyBuffer
---

# class PolyBuffer
Bind to a Max `polybuffer~` object.
The PolyBuffer object in JavaScript is a companion to the polybuffer~ object in Max. Through it, you can to access samples and metadata for the polybuffer~ object with the given name.
## Constructors
```
new PolyBuffer(name: string);

```

Constructs a new instance of the `PolyBuffer` class
Parameter | Type | Description  
---|---|---  
name | string | name of the Max `polybuffer~` to bind to.  
## Properties
### count string read-only
Number of `buffer~` objects in the `polybuffer~`
### name string read-only
Name of the Max `polybuffer~`
### size number read-only
Memory size used by the `polybuffer~` in bytes
## Methods
### append
Add a sound file to the `polybuffer~`
```
append(soundfilePath?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ soundfilePath | string | sound file path to load; if none provided, a dialog will appear  
### appendempty
Add an empty buffer~ with specified length and channel count
```
appendempty(duration: number, channels: number): void;

```
Name | Type | Description  
---|---|---  
duration | number | the duration in milliseconds  
channels | number | the number of channels  
### clear
Delete every buffer~
```
clear(): void;

```

### dump
Get info about a `polybuffer~`
```
dump(): [number, string, string, number, number, number];

```
Name | Type | Description  
---|---|---  
Return Value | [number, string, string, number, number, number] | - an array containing the index, name, path, duration, channel, and sample rate of `buffer~`s in the `polybuffer~`  
### getbufferlist
Get the names of `buffer~`s in the `polybuffer~`
```
getbufferlist(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] |   
### getshortname
Get every `buffer~` name followed by the sound file name (without extensions)
```
getshortname(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] |   
### open
Open the `polybuffer~` object's window to see information about the buffers
```
open(): void;

```

### print
Post the `polybuffer~`s contents to the Max window
The content printed are the number of items in the `polybuffer~` and the shortname and filenames of each buffer in the `polybuffer~`.
```
print(): void;

```

### readfolder
Load multiple sound files from the specified folder
```
readfolder(folderPath?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ folderPath | string | folder to read; if none provided, a dialog will appear  
### send
Send messages to `buffer~` objects in the `polybuffer~`
```
send(index: number, message: any): void;

```
Name | Type | Description  
---|---|---  
index | number | the `buffer~` index (1-indexed); an index of 0 sends the message to every `buffer~`  
message | any | the message to send  
#### Example
The following example binds to a `polybuffer~` named `"mypolybuffer"` and clears the second `buffer~` if there is one.
```
var pb = new PolyBuffer("mypolybuffer");
pb.send(2, "clear");

```

### wclose
Close the window editor
```
wclose(): void;

```

### writefolder
Write every buffer~ to a fild in a folder
```
writefolder(folderPath?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ folderPath | string | folder to read; if none provided, a dialog will appear
