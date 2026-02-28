---
description: Bitmap image object handle
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/image/
title: class Image
---

# class Image
Bitmap image object handle
The Image object can be used to draw images in MGraphics or Sketch.
You can use [MGraphics.image_surface_draw()](https://docs.cycling74.com/apiref/js/mgraphics/#image_surface_draw "MGraphics.image_surface_draw\(\)") and [MGraphics.set_source_surface()](https://docs.cycling74.com/apiref/js/mgraphics/#set_source_surface "MGraphics.set_source_surface\(\)") to draw using a bitmap Image. Create an Image either using a file in Max's search path, or from an existing MGraphics context.
It is possible to load image files from disk, create images from instances of Sketch, or generate them manually. The Image object has several methods to assist in manipulating images once generated. Note that alphablending is on by default in sketch. Certain file formats which contain alpha channels such as PICT or TIFF may have their alpha channel set all off. File formats which do not contain an alpha channel such as JPEG, by default have an alpha channel of all on. If you are having trouble seeing an image when attempting to draw in an instance of Sketch, you may want to either turn off blending with gldisable("blend"), or set the alpha channel to be all on with clearchannel("alpha", 1.).
#### Example
```
function paint() {

		// Render a simple image
		var im = new Image("icon.png");
		mgraphics.image_surface_draw(im);

		// Render from an offscreen mgraphics
		var offscreen_ctx = new MGraphics(200, 200);
		offscreen_ctx.rectangle(10, 10, 50, 50);
		offscreen_ctx.set_source_rgba(1, 0, 0, 1);
		offscreen_ctx.fill();
		var im2 = new Image(offscreen_ctx);

		mgraphics.image_surface_draw(im2);
}

```

## Constructors
```
new Image(source: MGraphics);

```

Create a new bitmap image
Parameter | Type | Description  
---|---|---  
source | [MGraphics](https://docs.cycling74.com/apiref/js/mgraphics/ "MGraphics") | An [MGraphics](https://docs.cycling74.com/apiref/js/mgraphics/ "MGraphics") context  
```
new Image(filename: string);

```

Create a new bitmap image
Parameter | Type | Description  
---|---|---  
filename | string | A file in Max's search path  
```
new Image(width: number, height: number);

```

Create a new bitmap image
Parameter | Type | Description  
---|---|---  
width | number | Width of the image in pixels  
height | number | Height of the image in pixels  
```
new Image(source: Sketch);

```

Create a new bitmap image
Parameter | Type | Description  
---|---|---  
source | [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") | An [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") context  
## Properties
### size [number, number]
Get or set the size of the image
## Methods
### adjustchannel
Adjusts all channel values in the specified image channel
Adjusts all channel values in the image channel specified by the channel argument, by multiplying the channel value by the value specified by the scale argument and then adding the value specified by the bias argument. The resulting channel is clipped to the range 0.-1. Acceptable values for the channel argument are the strings: "red", "green", "blue", or "alpha".
```
adjustchannel(channel: "red" | "green" | "blue" | "alpha", scale: number, bias: number);

```
Name | Type | Description  
---|---|---  
channel | "red" | "green" | "blue" | "alpha" | "red" | "green" | "blue" | "alpha"  
scale | number | The scale factor to apply to the channel  
bias | number | The bias to add to the channel  
### alphachroma
Generate an alpha channel based on color similarity
Generates an alpha channel based on the chromatic distance from the specified RGB target color.
```
alphachroma(red: number, green: number, blue: number, tolerance: number?, fade: number?, minkey: number?, maxkey: number?): void;

```
Name | Type | Description  
---|---|---  
red | number | The red component of the target color  
green | number | The green component of the target color  
blue | number | The blue component of the target color  
tolerance | number? | defaults to 0  
fade | number? | defaults to 0  
minkey | number? | defaults to 0  
maxkey | number? | defaults to 1  
### blendchannel
Blend one channel from a source image into a channel of this image
Similar to the copychannel method, except supports a blend amount specified by the alpha argument. If the source object is not the same size as the destination object, then rectangle composed of the minimum width and height of each, is the rectangle of values which will be blended. Acceptable values for the channel arguments are the strings: "red", "green", "blue", or "alpha".
```
blendchannel(source: Image, alpha: number, source_channel: "red" | "green" | "blue" | "alpha", dest_channel: "red" | "green" | "blue" | "alpha"): void;

```
Name | Type | Description  
---|---|---  
source | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") | Source Image to blend from  
alpha | number | Blend amount (0-1)  
source_channel | "red" | "green" | "blue" | "alpha" | Source channel to blend from  
dest_channel | "red" | "green" | "blue" | "alpha" | Destination channel to blend into  
### blendpixels
Blend pixels from a source image into this image
Similar to the copypixels method, except supports alpha blending, including a global alpha value specified by the alpha argument. This global alpha value is multiplied by the source object's alpha channel at each pixel. Instances of Sketch do not contain an alpha channel, which is assumed to be all on. The source object can either be an instance of Image, or Sketch.
```
blendpixels(source: Image | Sketch, alpha: number, source_x: number, source_y: number, dest_x: number, dest_y: number, width: number, height: number): void;

```
Name | Type | Description  
---|---|---  
source |  [Image](https://docs.cycling74.com/apiref/js/image/ "Image") | [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") | Source Image to blend from  
alpha | number | Blend amount (0-1)  
source_x | number | X coordinate of the source region  
source_y | number | Y coordinate of the source region  
dest_x | number | X coordinate of the destination region  
dest_y | number | Y coordinate of the destination region  
width | number | Width of the region to blend  
height | number | Height of the region to blend  
### clear
Clear the image to the specified color
```
clear(red: number?, green: number?, blue: number?, alpha: number?): void;

```
Name | Type | Description  
---|---|---  
red | number? | Red channel value (0-1), defaults to 0  
green | number? | Green channel value (0-1), defaults to 0  
blue | number? | Blue channel value (0-1), defaults to 0  
alpha | number? | Alpha channel value (0-1), defaults to 1  
### clearchannel
Set all values in the specified channel to the given value
Sets all values in the image channel specified by the channel argument, to the value specified by the value argument. If the value argument is omitted, it defaults to 0. The resulting channel is clipped to the range 0.-1. Acceptable values for the channel argument are the strings: "red", "green", "blue", or "alpha".
```
clearchannel(channel: "red" | "green" | "blue" | "alpha", value: number?): void;

```
Name | Type | Description  
---|---|---  
channel | "red" | "green" | "blue" | "alpha" | The channel to modify  
value | number? | The value to set (0-1)  
### copychannel
Copies the channel values from the source object
Copies the channel values from the source object's channel specified by the source_channel argument to the destination object's channel specified by the destination_channel argument. The source object can only be an instance of Image (not Sketch). If the source object is not the same size as the destination object, then rectangle composed of the minimum width and height of each, is the rectangle of values which will be copied. Acceptable values for the channel arguments are the strings: "red", "green", "blue", or "alpha".
```
copychannel(source: Image, source_channel: "red" | "green" | "blue" | "alpha", dest_channel: "red" | "green" | "blue" | "alpha"): void;

```
Name | Type | Description  
---|---|---  
source | [Image](https://docs.cycling74.com/apiref/js/image/ "Image") |   
source_channel | "red" | "green" | "blue" | "alpha" |   
dest_channel | "red" | "green" | "blue" | "alpha" |   
### copypixels
Copy pixels from a source image into this image
Copies pixels from the source object to the location specified by the destination_x and destination_y arguments. The initial x and y offset into the source and size of the rectangle copied can be speified by the source_x, source_y, width and height arguments. If these are not present an x and y offset of zero and width and height equal to the source image is assumed. No scaling of pixels is supported. The source object can either be an instance of Image, or Sketch.
```
copypixels(source: Image | Sketch, source_x: number, source_y: number, dest_x: number, dest_y: number, width: number, height: number): void;

```
Name | Type | Description  
---|---|---  
source |  [Image](https://docs.cycling74.com/apiref/js/image/ "Image") | [Sketch](https://docs.cycling74.com/apiref/js/sketch/ "Sketch") |   
source_x | number |   
source_y | number |   
dest_x | number |   
dest_y | number |   
width | number |   
height | number |   
### flip
Flip the image
Flips the image horizontally and or vertically. Arguments can be 0 or 1, where 0 is no flip, and 1 is flip.
```
flip(horizontal: 0 | 1, vertical: 0 | 1): void;

```
Name | Type | Description  
---|---|---  
horizontal | 0 | 1 | 0 | 1  
vertical | 0 | 1 | 0 | 1  
### freepeer
Free the native C peer
Frees the image data from the native C peer (created when making an object), which is not considered by the JavaScript garbage collector, and may consume lots of memory until the garbage collector decides to run based JS allocated memory. Once called, the object is not available for any other use. It's not necessary to call this function, as the memory will be freed eventually, but you can call it whenever you're done with your object.
```
freepeer(): void;

```

### fromnamedmatrix
Create a new bitmap image from a named matrix
Copies the pixels from the jit.matrix object specified by matrixname to the image.
```
fromnamedmatrix(name: string): void;

```
Name | Type | Description  
---|---|---  
name | string | Unique name of a Max matrix  
### getpixel
Get the color of the pixel at the specified location
Returns an array containing the pixel value at the specified location. This array is ordered RGBA, i.e. array element 0 is red, 1, green, 2, blue, 3 alpha. Color values are floating point numbers in the range 0.-1.
```
getpixel(x: number, y: number): [number, number, number, number];

```
Name | Type | Description  
---|---|---  
x | number | X coordinate of the pixel  
y | number | Y coordinate of the pixel  
Return Value | [number, number, number, number] | An array containing the RGBA values of the pixel (0-1)  
### setpixel
Set the pixel at the specified location to the given color
Sets the pixel value at the specified location. Color values are floating point numbers in the range 0.-1.
```
setpixel(x: number, y: number, red: number, green: number, blue: number, alpha: number): void;

```
Name | Type | Description  
---|---|---  
x | number | X coordinate of the pixel  
y | number | Y coordinate of the pixel  
red | number | Red channel value (0-1)  
green | number | Green channel value (0-1)  
blue | number | Blue channel value (0-1)  
alpha | number | Alpha channel value (0-1)  
### swapxy
Swap the x and y axes of the image
Swaps the axes of the image so that width becomes height and vice versa. The effective result is that the image is rotated 90 degrees counter clockwise, and then flipped vertically.
```
swapxy(): void;

```

### tonamedmatrix
Copy the pixels from a named matrix to the image
Copies the pixels from the jit.matrix object specified by matrixname to the image.
```
tonamedmatrix(name: string): void;

```
Name | Type | Description  
---|---|---  
name | string | Unique name of a Max matrix
