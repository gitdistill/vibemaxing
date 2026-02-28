---
description: Bind to a Maxbuffer~object.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/buffer/
title: class Buffer
---

# class Buffer
Bind to a Max `buffer~` object.
The Buffer object in JavaScript is a companion to the buffer~ object in Max. Through it, you can to access samples and metadata for the buffer~ object with the given name.
## Constructors
```
new Buffer(name: string);

```

Constructs a new instance of the `Buffer` class
Parameter | Type | Description  
---|---|---  
name | string | name of the Max `buffer~` to bind to.  
## Methods
### channelcount
Buffer channel count
Return the channels the buffer~ object. This is a method, not a property, and so must be called to get the number of channels.
```
channelcount(): number;

```
Name | Type | Description  
---|---|---  
Return Value | number | The number of channels in the buffer~ object.  
### create
Create a new Max `buffer~` object.
This method is only available in the new v8 javascript engine objects.
```
create(name?: string, filename?: string, duration?: number, channelcount?: number): void;

```
Name | Type | Description  
---|---|---  
_optional_ name | string | name of the Max `buffer~` to create. If no name is provided the current name is used.  
_optional_ filename | string | filename of the audio file to load. If no filename is provided the buffer is created empty.  
_optional_ duration | number | duration of the buffer in milliseconds. If no duration is provided the buffer is created empty.  
_optional_ channelcount | number | number of channels in the buffer. If no channelcount is provided the buffer is created with 1 channel.  
### framecount
Buffer frame count
Return the number of frames (samples in a single channel) in the buffer~ object. This is a method, not a property, and so must be called to get the number of frames.
```
framecount(): number;

```
Name | Type | Description  
---|---|---  
Return Value | number | The number of frames in the buffer~ object.  
### freepeer
Free the native C peer
Frees the buffer~ data from the native C peer (created when making a object), which is not considered by the JavaScript garbage collector, and may consume lots of memory until the garbage collector decides to run based JS allocated memory. Once called, the object is not available for any other use. It's not necessary to call this function, as the memory will be freed eventually, but you can call it whenever you're done with your object.
```
freepeer(): void;

```

### getattr
Get the value of the named attribute
This method is only available in the new v8 javascript engine objects.
```
getattr(name: string): number | string | (number | string)[];

```
Name | Type | Description  
---|---|---  
name | string | the name of the attribute to retrieve  
Return Value | number | string | (number | string)[] | the value of the attribute, as an array if the attribute value is a list  
### getname
Get the name of the buffer
This method is only available in the new v8 javascript engine objects.
```
getname(): string;

```
Name | Type | Description  
---|---|---  
Return Value | string | The name of the buffer~ object.  
### length
Length of the buffer in milliseconds
Return the length of the buffer~ object in milliseconds. This is a method, not a property, and so must be called to get the length of the buffer.
```
length(): number;

```
Name | Type | Description  
---|---|---  
Return Value | number | The length of the buffer in milliseconds.  
### peek
Fetch an array of samples from the buffer
```
peek(channel: number, frame: number, count: number): number[];

```
Name | Type | Description  
---|---|---  
channel | number | channel to fetch samples from (indexed from 1)  
frame | number | frame at which to start fetching samples (indexed from 0)  
count | number | number of samples to fetch  
Return Value | number[] |   
### poke
Write samples into the buffer
It is more efficient to call this function once with an array, than to call it mulpitle times, each time with a single sample.
```
poke(channel: number, frame: number, samples: number | number[]): void;

```
Name | Type | Description  
---|---|---  
channel | number | channel to write samples to (indexed from 1)  
frame | number | frame at which to start writing samples (indexed from 0)  
samples | number | number[] | samples to write (or a single sample to write)  
### send
Send a message to the buffer.
Can send any message that buffer~ understands. See [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") reference.
```
send(message: string, ...args: any[]): void;

```
Name | Type | Description  
---|---|---  
message | string | the name of message  
args | any[] | arguments that follow the name of the message  
### setattr
Set the value of the named attribute
This method is only available in the new v8 javascript engine objects.
```
setattr(name: string, value: number | string | (number | string)[]): void;

```
Name | Type | Description  
---|---|---  
name | string | the name of the attribute to set  
value | number | string | (number | string)[] | the value of the attribute to set  
### setname
Set the name of the buffer
This method is only available in the new v8 javascript engine objects.
```
setname(name: string): void;

```
Name | Type | Description  
---|---|---  
name | string | the name of the buffer to set
