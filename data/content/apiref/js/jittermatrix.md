---
description: A named matrix which may be used for data storage and retrieval, resampling, and matrix type and planecount conversion operations.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/jittermatrix/
title: class JitterMatrix
---

# class JitterMatrix
A named matrix which may be used for data storage and retrieval, resampling, and matrix type and planecount conversion operations.
## Constructors
```
new JitterMatrix(planeCount?: number, dataType?: string, columns?: number, rows?: number);

```

Constructs a new instance of the `JitterMatrix` class
Parameter | Type | Description  
---|---|---  
_optional_ planeCount | number |   
_optional_ dataType | string |   
_optional_ columns | number |   
_optional_ rows | number |   
#### Example
```
var mymatrix = new JitterMatrix(4, "char", 320, 240);

```

## Properties
### adapt number
Matrix adaptation flag.
When this flag is set (1), the JitterMatrix will adapt to the incoming matrix planecount, type, and dimensions
### dim [number, number]
Matrix data dimensions
### dimstride [number, number]
Byte stride per dimension
### dstdimend number[]
Destination dimension end position (default = all dim values minus 1).
### dstdimstart number[]
Destination dimension start position (default = all 0).
### interp number
Matrix interpolation flag (default = 0). When the flag is set, the input matrix will be interpolated when copied to the internal matrix.
### name string
Name of the matrix (default = UID).
### planecount number
Number of planes in the matrix data (default = 4).
### planemap number[]
Maps input planes to output planes (default = 0 1 2 3 ...)
### size number
Total byte size of matrix.
### srcdimend number[]
Source dimension end position (default = all dim values minus 1).
### srcdimstart number[]
Source dimension start position (default = all 0).
### type string
The matrix data type (default = "char").
- "char": Char data (0-255) - "long": Long data - "float32": 32-bit floating point data - "float64": 64-bit floating point data
### usedstdim number
destdim use flag (default = 0).
When the flag is set, the destination dimension's attributes are used when copying an input matrix to an internal matrix.
### usesrcdim number
srcdim use flag (default = 0).
When the flag is set, the source dimension's attributes are used used when copying an input matrix to an internal matrix.
## Methods
### bang
Outputs the currently stored matrix
```
bang(): void;

```

### clear
Sets all matrix values to zero
```
clear(): void;

```

### copyarraytomatrix
Copy a tightly packed TypedArray to a JitterMatrix
This method is only available in the new v8 javascript engine objects. TypedArrays must match matrix type (Uint8 for char, Int32 for long, Float32 for float32 and Float64 for float64), and their size must match the tighly packed size of the matrix -- i.e. planecount * dim[0] * dim[1] ... * dim[n].
```
copyarraytomatrix(array: Uint8Array | Uint8ClampedArray | Int32Array | Float32Array | Float64Array): void;

```
Name | Type | Description  
---|---|---  
array | Uint8Array | Uint8ClampedArray | Int32Array | Float32Array | Float64Array | tightly packed TypedArray  
### copymatrixtoarray
Copy a JitterMatrix to a tightly packed TypedArray
This method is only available in the new v8 javascript engine objects. TypedArrays must match matrix type (Uint8 for char, Int32 for long, Float32 for float32 and Float64 for float64), and their size must match the tighly packed size of the matrix -- i.e. planecount * dim[0] * dim[1] ... * dim[n].
```
copymatrixtoarray(array: Uint8Array | Uint8ClampedArray | Int32Array | Float32Array | Float64Array): void;

```
Name | Type | Description  
---|---|---  
array | Uint8Array | Uint8ClampedArray | Int32Array | Float32Array | Float64Array | tightly packed TypedArray  
### exportimage
Export the current frame as an image file with the name specified
```
exportimage(filename: string, filetype?: string, useDialog?: number): void;

```
Name | Type | Description  
---|---|---  
filename | string | exported image filename  
_optional_ filetype | string | exported image file type; can be "png", "bmp", "jpeg", "macpaint", "photoshop", "pict", "qtimage", "sgi", "tga", and "tiff" (default = "png")  
_optional_ useDialog | number | a value of `1` will open a file dialog to enter image file settings  
### exportmovie
Export a matrix as a QuickTime movie
```
exportmovie(filename?: string, fps?: number, codec?: string, quality?: string, timescale?: number): void;

```
Name | Type | Description  
---|---|---  
_optional_ filename | string | exported movie filename (default = file dialog will open)  
_optional_ fps | number | frames per second (default = 30)  
_optional_ codec | string | one of "raw", "cinepak", "graphics", "animation", "video", "componentvideo", "jpeg", "mjpegb", "sgi", "planarrgb", "macpaint", "gif", "photocd", "qdgx", "avrjpeg", "opendmljpeg", "bmp", "winraw", "vector", "qd", "h261", "h263", "dvntsc", "dvpal", "dvprontsc", "dvpropal", "flc", "targa", "png", "tiff", "componentvideosigned", "componentvideounsigned", "cmyk", "microsoft", "sorenson", "indeo4", "argb64", "rgb48", "alphagrey32", "grey16", "mpegyuv420", "yuv420", and "sorensonyuv9" (default = "raw")  
_optional_ quality | string | one of "lossless", "max", "min", "low", "normal", and "high" (default = "max"). Note that the minimum quality is, in many cases, the codec's default quality. Use "low" quality for consistent results.  
_optional_ timescale | number | units per second (default = 600)  
### exprfill
Evaluate an expression to fill the matrix
If a plane argument is provided, the expression is applied to a single plane. Otherwise, it is applied to all planes in the matrix. See jit.expr for more information on expressions. Unlike the jit.expr object, there is no support for providing multiple expressions to fill multiple planes at once with different expressions. Call this method multiple times for each plane you wish to fill.
```
exprfill(plane: number, expression?: string): void;

```
Name | Type | Description  
---|---|---  
plane | number | matrix plane to apply to (default = all planes)  
_optional_ expression | string | expression to apply  
### fillplane
Fill the specified plane with a single value
```
fillplane(plane: number, value: number): void;

```
Name | Type | Description  
---|---|---  
plane | number | plane index  
value | number | value to fill with  
### float
Set all cells to the value specified by value(s) and output the data.
```
float(values: number | number[]): void;

```
Name | Type | Description  
---|---|---  
values | number | number[] | matrix value list whose length is equal to the dimcount  
### getcell
Sends the value(s) in the cell specified by position out the right outlet of the object as a list in the form "cell cell - position0 ... cell - positionN val plane0 - value ... planeN - value"
```
getcell(position: [number, number]): void;

```
Name | Type | Description  
---|---|---  
position | [number, number] | cell position  
### importmovie
Import a QuickTime movie into the matrix
```
importmovie(filename?: string, timeoffset?: number): void;

```
Name | Type | Description  
---|---|---  
_optional_ filename | string | filename of movie to import (default = file dialog)  
_optional_ timeoffset | number | import time offset (default = 0)  
### int
Set all cells to the value specified by value(s) and output the data.
```
int(values: number | number[]): void;

```
Name | Type | Description  
---|---|---  
values | number | number[] | matrix value list whose length is equal to the dimcount  
### jit_gl_texture
Copy a texture to the matrix
```
jit_gl_texture(texture_name: string): void;

```
Name | Type | Description  
---|---|---  
texture_name | string | GL texture name  
### list
Set all cells to the value specified by value(s) and output the data.
```
list(values: number[]): void;

```
Name | Type | Description  
---|---|---  
values | number[] | matrix value list whose length is equal to the dimcount  
### op
Perform jit.op operations on the matrix
```
op(operator: string, args: any): void;

```
Name | Type | Description  
---|---|---  
operator | string | the jit.op operator  
args | any | matrix name or constant args for the operator  
#### Example
```
var a = new JitterMatrix(4, "char", 320, 240);
var b = new JitterMatrix(4, "char", 320, 240);
b.setall(255, 255, 255, 255);
a.op("*", b);

```

### read
Read Jitter binary data files (.jxf) into the matrix
```
read(filename?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ filename | string | binary data file to read (default = file dialog)  
### setall
Set all cells to the value(s) specified
```
setall(values: number | number[]): void;

```
Name | Type | Description  
---|---|---  
values | number | number[] | values to set  
### setcell
Set the cell specified to a value
Arguments are formatted like the `setcell` message to a jit.matrix in Max.
```
setcell(...args: any[]): void;

```
Name | Type | Description  
---|---|---  
args | any[] | the position, plane, planeNumber, value/values to set  
#### Example
Set cell (20, 30) to (0, 0, 255, 255):
```
mymatrix.setcell(20, 30, "val", 0, 0, 255, 255);

```

### setcell1d
Set a cell in a 1D matrix
```
setcell1d(pos: number, ...values: number[]): void;

```
Name | Type | Description  
---|---|---  
pos | number | cell position  
values | number[] | values to set at given position  
#### Example
Set cell (74) to (100, 100, 100, 0):
```
my1dmatrix.setcell1d(74, 100, 100, 100, 0);

```

### setcell2d
Set a cell in a 2D matrix
```
setcell2d(posX: number, posY: number, ...values: number[]): void;

```
Name | Type | Description  
---|---|---  
posX | number | first dimension of cell's position  
posY | number | second dimension of cell's position  
values | number[] | values to set at given position  
#### Example
Set cell (30, 20) to (255, 255, 0, 0):
```
my2dmatrix.setcell2d(30, 20, 255, 255, 0, 0);

```

### setcell3d
Set a cell in a 3D matrix
```
setcell3d(posX: number, posY: number, posZ: number, ...values: number[]): void;

```
Name | Type | Description  
---|---|---  
posX | number | first coordinate of a cell's position  
posY | number | second coordinate of a cell's position  
posZ | number | third coordinate of a cell's position  
values | number[] | values to set at given position  
#### Example
Set cell (30, 20, 40) to (100, 200, 300, 0):
```
my3dmatrix.setcell3d(30, 20, 40, 100, 200, 300, 0);

```

### setplane1d
Set a cell for a 1D matrix
```
setplane1d(pos: number, plane: number, value: number): void;

```
Name | Type | Description  
---|---|---  
pos | number | first coordinate  
plane | number | plane number  
value | number | value to set  
### setplane2d
Set a cell for a 2D matrix
```
setplane2d(posX: number, posY: number, plane: number, value: number): void;

```
Name | Type | Description  
---|---|---  
posX | number | first coordinate  
posY | number | second coordinate  
plane | number | plane number  
value | number | value to set  
### setplane3d
Set a cell for a 3D matrix
```
setplane3d(posX: number, posY: number, posZ: number, plane: number, value: number): void;

```
Name | Type | Description  
---|---|---  
posX | number | first coordinate  
posY | number | second coordinate  
posZ | number | third coordinate  
plane | number | plane number  
value | number | value to set  
### val
Set all cells to the value specified
```
val(value: number): void;

```
Name | Type | Description  
---|---|---  
value | number | value to set  
### write
Write matrix set as a Jitter binary data file (.jxf)
```
write(filename?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ filename | string | name of file to write to (default = file dialog)
