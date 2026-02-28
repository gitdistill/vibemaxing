---
description: The File object provides a means of reading and writing files from JavaScript.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/file/
title: class File
---

# class File
The File object provides a means of reading and writing files from JavaScript.
## Constructors
```
new File(filename?: string, access?: FileTypes.FileAccess, typelist?: FileTypes.FourCharacterCode[]);

```

Create a file reference for reading or writing
By default, `typelist` is empty. If `filename` includes an extension, then it is not necessary to supply a `typelist`. If `filename` does not include an extension, then will look for a file with one of the extensions specified by `typelist`. Note that the four-character code may not match the file extension.
Given arguments, the `File` constructor will open the file automatically if the file can be opened.
Parameter | Type | Description  
---|---|---  
_optional_ filename | string | File to open. Can be relative, absolute, or anything in the Max search path  
_optional_ access | [FileTypes.FileAccess](https://docs.cycling74.com/apiref/js/filetypes/#type-fileaccess "FileTypes.FileAccess") | Access mode. Can be "read", "write", or "readwrite"  
_optional_ typelist |  [FileTypes.FourCharacterCode](https://docs.cycling74.com/apiref/js/filetypes/#type-fourcharactercode "FileTypes.FourCharacterCode")[] | Any of the four character codes in max-fileformats.txt  
#### Example 1
```
var f = new File("myfile.txt", "write");
post(f.isopen); // true, if myfile.txt is in the Max search path
f.close();

```

It's also possible to create an empty `File` object, and to configure it after the fact. In this case, the `File` object must be opened explicitly.
#### Example 2
```
var f = new File();
f.filename = "myfile.txt";
f.access = "write";
f.open();
post(f.isopen); // true, if myfile.txt is in the Max search path
f.close();

```

If for some reason the file could not be opened, then will return false.
## Properties
### access [FileTypes.FileAccess](https://docs.cycling74.com/apiref/js/filetypes/#type-fileaccess "FileTypes.FileAccess")
File access permissions: "read", "write", or "readwrite". By default, this value is "read".
### byteorder [FileTypes.FileEndianness](https://docs.cycling74.com/apiref/js/filetypes/#type-fileendianness "FileTypes.FileEndianness")
The assumed file byteorder (endianness): "big", "little", or "native". By default, this value is "native".
### eof number
The location of the end of file, in bytes. If set past the end of current file, `File` will append NULL bytes.
### filename string
The current filename.
### filetype [FileTypes.FourCharacterCode](https://docs.cycling74.com/apiref/js/filetypes/#type-fourcharactercode "FileTypes.FourCharacterCode")
The four-character code for the file type.
### foldername string read-only
The absolute path to parent folder.
### isopen boolean read-only
Return a true/false indicating if the File constructor is successful in finding and opening the file.
### linebreak [FileTypes.FileLineEndingStyle](https://docs.cycling74.com/apiref/js/filetypes/#type-filelineendingstyle "FileTypes.FileLineEndingStyle")
The line break convention to use when writing lines. Defaults to "native"
### position number
The current file position, in bytes. Set this to offset the file write position forward or backwards.
### typelist [FileTypes.FourCharacterCode](https://docs.cycling74.com/apiref/js/filetypes/#type-fourcharactercode "FileTypes.FourCharacterCode")[]
An array file type codes to filter by when opening a file. By default, this is the empty array.
## Methods
### close
Closes the currently open file.
```
close(text?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ text | string | unclear?  
### open
Opens the file specified by the filename argument. If no argument is specified, it will open the last opened file, or the value stored in the `filename` property. Check to see if the file was openend successfully.
```
open(filename?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ filename | string | the file to open  
### readbytes
Read bytes to an array
Reads and returns an array containing up to `count` numbers, read as bytes from the file, starting at the current file position. The file position is updated accordingly.
```
readbytes(count: number): number[];

```
Name | Type | Description  
---|---|---  
count | number | maximum number of bytes to read  
Return Value | number[] |   
### readchars
Read bytes to an array of single character strings
Reads and returns an array containing the single character strings, read as characters from the file, starting at the current file position. The file position is updated accordingly.
```
readchars(count: number): string[];

```
Name | Type | Description  
---|---|---  
count | number | maximum number of bytes to read  
Return Value | string[] |   
### readfloat32
Read from a file as 32-bit floating point numbers
Reads and returns an array containing the numbers read as 32-bit floating point numbers from the file, starting at the current file position. The byteorder property is taken into account when reading these values. The file position is updated accordingly.
```
readfloat32(count: number): number[];

```
Name | Type | Description  
---|---|---  
count | number | maximum number of floats to read  
Return Value | number[] |   
### readfloat64
Read from a file as 64-bit floating point numbers
Reads and returns an array containing the numbers read as 64-bit floating point numbers from the file, starting at the current file position. The byteorder property is taken into account when reading these values. The file position is updated accordingly.
```
readfloat64(count: number): number[];

```
Name | Type | Description  
---|---|---  
count | number | maximum number of floats to read  
Return Value | number[] |   
### readint16
Read from a file as 16-bit signed integers
Reads and returns an array containing the numbers read as signed 16-bit integers from the file, starting at the current file position. The byteorder property is taken into account when reading these values. The file position is updated accordingly.
```
readint16(count: number): number[];

```
Name | Type | Description  
---|---|---  
count | number | maximum number of integers to read  
Return Value | number[] |   
### readint32
Read from a file as 32-bit signed integers
Reads and returns an array containing the numbers read as signed 32-bit integers from the file, starting at the current file position. The byteorder property is taken into account when reading these values. The file position is updated accordingly.
```
readint32(count: number): number[];

```
Name | Type | Description  
---|---|---  
count | number | maximum number of integers to read  
Return Value | number[] |   
### readline
Read a line of text
Reads and returns a string containing up to `maximumCount` characters or up to the first line break as read from the file, starting at the current file position. The file position is updated accordingly The default maximum count value is 512. This can be increased by specifying a new maximum count as the argument.
```
readline(maximumCount: number): string;

```
Name | Type | Description  
---|---|---  
maximumCount | number | maximum string length to read  
Return Value | string |   
### readstring
Read a string of text
Reads and returns a string containing up to char_count characters as read from the file, starting at the current file position. Unlike , line breaks are not considered. The file position is updated accordingly.
```
readstring(count: number): string;

```
Name | Type | Description  
---|---|---  
count | number | maximum number of bytes to read  
Return Value | string |   
### writebytes
Write an array of bytes
Writes the numbers contained in the `bytes` argument as bytes to the file, starting at the current file position. The file position is updated accordingly.
```
writebytes(bytes: number[]): void;

```
Name | Type | Description  
---|---|---  
bytes | number[] | bytes to write  
### writechars
Write single character strings
Writes the single character strings contained in the `chars` argument as characters to the file, starting at the current file position. The file position is updated accordingly.
```
writechars(chars: string[]): void;

```
Name | Type | Description  
---|---|---  
chars | string[] | array of single character strings  
### writefloat32
Write numbers as 32-bit floating point numbers
Writes the numbers contained in the `floats` argument as 32-bit floating point numbers to the file, starting at the current file position. The byteorder property is taken into account when writing these values. The file position is updated accordingly.
```
writefloat32(floats: number[]): void;

```
Name | Type | Description  
---|---|---  
floats | number[] | array of numbers to write as float32  
### writefloat64
Write numbers as 64-bit floating point numbers
Writes the numbers contained in the `floats` argument as 64-bit floating point numbers to the file, starting at the current file position. The byteorder property is taken into account when writing these values. The file position is updated accordingly.
```
writefloat64(floats: number[]): void;

```
Name | Type | Description  
---|---|---  
floats | number[] | array of numbers to write as float64  
### writeint16
Write numbers as 16-bit signed integers
Writes the numbers contained in the `ints` argument as signed 16-bit integers to the file, starting at the current file position. The byteorder property is taken into account when writing these values. The file position is updated accordingly.
```
writeint16(ints: number[]): void;

```
Name | Type | Description  
---|---|---  
ints | number[] | array of numbers to write as int16  
### writeint32
Write numbers as 32-bit signed integers
Writes the numbers contained in the `ints` argument as signed 32-bit integers to the file, starting at the current file position. The byteorder property is taken into account when writing these values. The file position is updated accordingly.
```
writeint32(ints: number[]): void;

```
Name | Type | Description  
---|---|---  
ints | number[] | array of numbers to write as int32  
### writeline
Write a line of text
Writes the characters contained in the string argument as characters to the file, starting at the current file position, and inserts a line break appropriate to the `linebreak` property. The file position is updated accordingly.
```
writeline(text: string): void;

```
Name | Type | Description  
---|---|---  
text | string | the text to write  
### writestring
Write a string of text
Writes the characters contained in the string argument as characters to the file, starting at the current file position. Unlike , no line break is inserted. The file position is updated accordingly.
```
writestring(text: string): void;

```
Name | Type | Description  
---|---|---  
text | string | the text to write
