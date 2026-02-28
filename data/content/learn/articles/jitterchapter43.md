---
description: A Slab of Your Very Own
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter43/
title: Jitter Tutorial 43
---

Download Series Content and Patchers
# Tutorial 43: A Slab of Your Very Own
While there are many shaders that provided with the Jitter distribution, many of which can be composed to form more complicated operations, one of the most exciting aspects of Jitter’s shader support is that you can write your own. Writing shaders is fundamentally not a difficult process; however, it does involve text-based programming, so some understanding of a programming language like C, Java, or Javascript is recommended before you take a crack at writing a shader.
Since there are a few more things to consider once you take lighting and complex geometry into account, we are going to focus on the simple data processing of the [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") object. We will use the GLSL shader language for this Tutorial, but note that Jitter also supports programs written in Cg, as well as the ARB and NV assembly languages. Unfortunately it is out of the scope of the Jitter documentation to fully describe any of these languages. This Tutorial is meant to give you a very simple introduction to GLSL and demonstrate how to integrate shader code into a format Jitter understands. We will show you the basics of what you need to know and refer you to more authoritative sources to find out more. 
**Hardware Requirement:** To fully experience this tutorial, you will need a graphics card that supports programmable shaders--e.g. ATI Radeon 9200, NVIDIA GeForce 5000 series or later graphics cards. It is also recommended that you update your OpenGL driver with the latest available for your graphics card. On Macintosh, this is provided with the latest OS update. On PC, this can be acquired from either your graphics card manufacturer, or computer manufacturer.
## Mixing Multiple Sources
Let's start with a 4-source video mixer. This could already be accomplished with a handful of instances of either the provided math or compositing shaders, but it will be more efficient to do this all at once in a single shader. A mathematical formula for this 4 source mix might look something like the following, where _a_ , _b_ , _c_ , and _d_ are constants for how much of each input we want to accumulate.
output = a*input0 + b*input1 + c*input2 + d*input3
In GLSL, this might look something like the following:
```
uniform vec4 a;
uniform vec4 b;
uniform vec4 c;
uniform vec4 d;

void main (void)
{
   vec4 input0;
   vec4 input1;
   vec4 input2;
   vec4 input3;
   vec4 output;

   output = a*input0 + b*input1 + c*input2 + d*input3;
}

```

We’ve defined a few global variables: _a_ , _b_ , _c_ , and _d_ , as well as a function called main() that contains local variables _input0_ , _input1_ , _input2_ , _input3_ , and _c_ , and _d_. The vec4 type is a vector with four values, which typically refer to a point (x,y,z,w) in homogenous coordinates or a color (r,g,b,a). When we multiply two vec4 elements in GLSL as above, it is a pointwise multiplication, resulting in another vec4 where each element of the multiplication is the product of the same element from the two operands—e.g. with m = p*q: m.r =p.r*q.r; m.g =p.g*q.g; m.b =p.b*q.b; m.a =p.a*q.a.
This program is a fragment program, and our main function will be executed once for each fragment (or pixel) in the image. It has no knowledge about adjacent output pixels or when it is being run. This is what permits it to run several instances in parallel for multiple fragments in order to obtain such high performance. CPUs don’t have the same kind of restrictions, but then the computation is not inherently parallelizable. 
For detailed information about all things GLSL related (keywords, built in operators, built-in variables, syntax, etc.), we recommend reading the _OpenGL Shading Language Reference_ (aka “The Orange Book”) and the _OpenGL Shading Language Specification_. The specification is available online at _opengl.org_. There are also several tutorials online for GLSL such as the one hosted at _lighthouse3d.com_.
## Fragment Program Input and Output
The above code is valid GLSL and looks similar to our original formula. However, it won’t work yet. Right now we’ve declared variables for input and output, but these values aren’t actually making use of any input and not assigning any values to the output in the OpenGL pipeline. To get input, we need to sample values from textures, and to write to our output, we need to write to the built-in gl_FragColor variable. With this in mind, we make the following modifications to our code:
```
uniform vec4 a;
uniform vec4 b;
uniform vec4 c;
uniform vec4 d;

// define our varying texture coordinates
varying vec2 texcoord0;
varying vec2 texcoord1;
varying vec2 texcoord2;
varying vec2 texcoord3;

// define our rectangular texture samplers
uniform sampler2DRect tex0;
uniform sampler2DRect tex1;
uniform sampler2DRect tex2;
uniform sampler2DRect tex3;

void main (void)
{
   // sample our textures
   vec4 input0 = texture2DRect(tex0, texcoord0);
   vec4 input1 = texture2DRect(tex1, texcoord1);
   vec4 input2 = texture2DRect(tex2, texcoord2);
   vec4 input3 = texture2DRect(tex3, texcoord3);
vec4 output;

   // perform our calculation
   output = a*input0 + b*input1 + c*input2 + d*input3;

   // write our data to the fragment color
   gl_FragColor = output;
}

```

The varying keyword means that the parameter will be changing for each fragment. For example, _texcoord0_ will reference the interpolated (_x_ , _y_) pixel coordinate to extract from our leftmost input texture. We are able to sample this texture (i.e. get the color value associated with the texture coordinate) by calling the texture2DRect() function with the corresponding sampler ID and texture coordinate vector. The sampler2DRect data type and texture2DRect() function indicate that we are using _rectangular_ textures. Ordinary textures in OpenGL have dimensions restricted to powers of two for each dimension (e.g. 256x256) and the values are indexed with “normalized” coordinates (fractional values from 0.-1.). Rectangular textures on the other hand permit arbitrary dimensions (e.g. 720x480), and the coordinates are in terms of pixel position (e.g. 0.-720., and 0.-480.). In Jitter we use rectangular textures as our default texture type for increased performance when working with datasets that are not powers of two, as is often the case when working with video. Ordinary textures can still be used via the sampler2D data type and the texture2D() function, but they require that the input textures have been created with the `rectangle` attribute set to `0`.
## The Vertex Program 
The above code is now our complete GLSL fragment program, but it still won’t do anything yet, because it requires a vertex program pass on our texture coordinates. As the name suggests, the vertex program runs once for each vertex in the geometry. It is where any modification to the geometry is calculated, including the attachment of texture coordinates to that geometry. Values generated by the vertex program can be automatically interpolated across the surface of the geometry as we typically want to do with texture coordinates. For our vertex program, we will want to transform our vertex by the current model-view projection matrix, transform our texture coordinates by the current texture transform matrix (this is how we scale and possibly flip our rectangular texture coordinates), and then pass on our texture coordinates as varying values to our fragment program. Such a vertex program might look like this: 
```
// define our varying texture coordinates
varying vec2 texcoord0;
varying vec2 texcoord1;
varying vec2 texcoord2;
varying vec2 texcoord3;

void main( void )
{
   // the output vertex postion to the input vertex position
   // transformed by the current ModelViewProjection matrix
   gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;

// assign our varying texture coordinates to the
// input texture coordinate values transformed
// by the appropriate texture matrix. This is
// necessary for rectangular and flipped textures
   texcoord0 = vec2(gl_TextureMatrix[0] * gl_MultiTexCoord0);
   texcoord1 = vec2(gl_TextureMatrix[1] * gl_MultiTexCoord1);
   texcoord2 = vec2(gl_TextureMatrix[2] * gl_MultiTexCoord2);
   texcoord3 = vec2(gl_TextureMatrix[3] * gl_MultiTexCoord3);
}

```

## (JXS)
These programs together will perform all the hard work to process all of our pixel data, but we’re still missing one final component. In order for Jitter to load these programs and expose parameters to the user, we need to package these programs in a _Jitter XML Shader file_ (JXS). In this file we will specify user settable variables _a_ , _b_ , _c_ , and _d_ with default values, bind our multiple texture units so that the program can access them properly, define our programs, and bind our user variables to our program variables:
```
<jittershader name="fourwaymix">
   <param name="a" type="vec4" default="0.25 0.25 0.25 0.25" />
   <param name="b" type="vec4" default="0.25 0.25 0.25 0.25" />
   <param name="c" type="vec4" default="0.25 0.25 0.25 0.25" />
   <param name="d" type="vec4" default="0.25 0.25 0.25 0.25" />
   <param name="tex0" type="int" default="0" />
   <param name="tex1" type="int" default="1" />
   <param name="tex2" type="int" default="2" />
   <param name="tex3" type="int" default="3" />
   <language name="glsl" version="1.0">
     <bind param="a" program="fp" />
     <bind param="b" program="fp" />
     <bind param="c" program="fp" />
     <bind param="d" program="fp" />
     <bind param="tex0" program="fp" />
     <bind param="tex1" program="fp" />
     <bind param="tex2" program="fp" />
     <bind param="tex3" program="fp" />
     <program name="vp" type="vertex" source="43j-fourwaymix.vp.glsl" />
     <program name="fp" type="fragment" source="43j-fourwaymix.fp.glsl" />
   </language>
</jittershader>

```

The jittershader tag defines our shader with an optional name. The param tag defines a parameter to be exposed to the Max environment with a `name`, `type`, and optional default `value`. The language tag defines a block of programs in the specified language and version. The bind tag binds user-exposed parameters to variables in specific programs. Finally, the program tag defines our programs with a name, type, and source file. The source may optionally be embedded in the XML file itself by including it inside either an XML comment or CDATA block; this is the case with many of the shader files provided in the Jitter distribution. For a complete reference of XML tags available, please see _[Appendix C:](https://docs.cycling74.com/learn/articles/jitterchapter99_appendixc/) The JXS File Format_.
## Ready for Action
Now that all the pieces are in place, lets see our program do its job.
  * Open the Tutorial patch. Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box connected to the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") object.
  * Read in a movie for each instance of [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie"), using either those provided in the [message](https://docs.cycling74.com/reference/message/ "message") box objects or media of your own choosing.
  * Load the shader by sending the message `read 43j-fourwaymix.jxs` to the [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") object.

![The patch that puts it all together.](https://docs.cycling74.com/images/674a41ce2bf723533357943f64537be8_1024.webp) The patch that puts it all together.
You will notice that the [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") object has its inputs attribute set to `4`. This is necessary to have more than the default 2 inputs, as we want for our 4-way mix shader. Lastly, it is worth noting that for optimal performance when loading and compiling shaders, Jitter keeps a cache of all compiled shaders; it will only recompile the shader if it detects that the source files have been modified on disk. To flush the cache, you can send [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") the message `flush_cache`.
## Summary
In this tutorial we demonstrated how to build a shader from scratch in GLSL that mixes 4 input sources on the GPU via a [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") object. This was accomplished by writing a fragment program, a vertex program, and wrapping them in a Jitter XML Shader file so that our shader could be loaded into Jitter with parameters exposed to the user in Max. We also demonstrated the use of more than 2 inputs for the [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") object by using the `inputs` attribute.
## See Also
  * [Video and Graphics Tutorial 9: Building live video effects](https://docs.cycling74.com/learn/articles/jitterchapter00k_building-live-video-effects/)
  * [The JXS File Format](https://docs.cycling74.com/learn/articles/jitterchapter99_appendixc/)
  * [jit.gl.slab - Performs a GL accelerated grid-based evaluation](https://docs.cycling74.com/reference/jit.gl.slab)
  * [jit.gl.videoplane - GL accelerated video plane](https://docs.cycling74.com/reference/jit.gl.videoplane)
  * [jit.movie - Play or edit a movie](https://docs.cycling74.com/reference/jit.movie)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
