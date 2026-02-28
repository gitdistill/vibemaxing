---
description: How to define custom shader graphs using the JXS file format. Includes loading and connecting shaders, defining parameters, binding textures, and more.
group: Jitter
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/jitter/jxs_file_format/
title: The JXS File Format
---

# The JXS File Format
Jitter objects that work with shaders use a special shader description file format called **JXS** , or _Jitter XML Shader_. This file tells Max how to load a list of shaders and connect them up to Max. It includes a description, a list of textures and parameters, and a list of shaders. There must always be one vertex and fragment shader, and there can be an optional geometry shader. A typical JXS file looks like this:
```
<jittershader name="myshader">
  <!-- optional description -->
  <description>This is my shader</description>

  <!-- optional list of texture objects to bind -->
  <texture file="chilis.jpg" rectangle="0"/>  

  <!-- optional list of shader parameters -->
  <param name="myparam" type="vec3" default="1 2 3" >
    <description>This is my parameter</description>
  </param>

  <!-- optional list of shader state parameters -->
  <param name="modelViewProjectionMatrix" type="mat4" state="MODELVIEW_PROJECTION_MATRIX" />
  <param name="jit_position" type="vec3" state="POSITION" />
  <param name="jit_texcoord" type="vec2" state="TEXCOORD" />

  <!-- optionally include other glsl sources -->
  <include source="diffuse.glsl" program="vp" />

  <!-- list of language implementations -->
  <language name="glsl" version="1.5">

    <!-- list of binding targets for shader parameters -->
    <bind param="modelViewProjectionMatrix" program="vp" />
    <bind param="jit_position" program="vp" />
    <bind param="jit_texcoord" program="vp" />
    <bind param="myparam" program="fp" />

    <program name="vp" type="vertex">
      <![CDATA[
      #version 330 core
      
      in vec3 jit_position;
      in vec2 jit_texcoord;
      out jit_PerVertex {
        vec2 texcoord0;
      } jit_out;
      uniform mat4 modelViewProjectionMatrix;
      
      void main() {
        gl_Position = modelViewProjectionMatrix*vec4(jit_position, 1);
        jit_out.texcoord0 = jit_texcoord;
      }
      ]]>
    </program>
    <program name="fp" type="fragment">
      <![CDATA[
      #version 330 core
      
      in jit_PerVertex {
        vec2 texcoord0;
      } jit_in;
      layout (location = 0) out vec4 outColor;
      uniform sampler2D tex0;
      uniform vec3 myparam;
      void main() {
        outColor = vec4(myparam, 1) * texture(tex0, jit_in.texcoord0);
      }
      ]]>
    </program>
  </language>
</jittershader>

```

## The `jittershader` Tag
A JXS file opens with a `jittershader` tag. This tag has a single, optional attribute, the `name` attribute. This attribute is currently unused by Max, but by convention a JXS author should provide a descriptive name.
## The `description` tag
A `jittershader` may include a `description`. This description is also optional, but by convention this is a good place to document the intended behavior of a JXS file. Max may use this information when listing available shaders.
## The `texture` tag
A `jittershader` may have one or more textures, defined using a `texture` tag. The `file` attribute loads the texture from an image file, which may be any file in Max's [Search Path](https://docs.cycling74.com/userguide/jitter/search_path/).
```
<texture file="mytexture.jpg"/>

```

A `texture` may be modified, using any attribute of the [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture") object.
```
<texture file="gn.gradperm.png" rectangle="0" filter="none none" wrap="repeat repeat" mipmap="none" anisotropy="0" />

```

Bind a texture to a parameter using the `unit` attribute. This defaults to zero, and so may be omitted if there is only one texture parameter.
```
<!-- The texture has unit="1", so binds to texture tex_rand with default="1" -->
<param name="tex_normals" type="int" default="0" />
<param name="tex_rand" type="int" default="1" />
<texture file="random-tex.png" type="float16" unit="1" rectangle="0" filter="none none" wrap="repeat repeat"/>	

```

See [texture parameters](https://docs.cycling74.com/userguide/jitter/jxs_file_format/#texture-parameters) for more details about binding Max textures to shader programs.
## Parameters and the `param` tag
Use the `param` tag to create parameters, which define bindings between values available in Max and shader variables. These can bind to numerical Max values, to Jitter textures, or to specific state variables calculated by the graphics engine. A parameter may contain a description.
```
<jittershader>
    <param name="myparam" type="float" default="1.0">
        <description> A parameter description </description>
    </param>
</jittershader>

```

A parameter must also have a type. Parameter types can be most of the primitive types defined by the _glsl_ standard.
Type | Description  
---|---  
bool | boolean type  
int | integer type, **also used for texture input**  
float | float-width number type  
double | double-width number type  
bvec2, bvec3, bvec4 | boolean vector of length 2, 3, or 4  
ivec2, ivec3, ivec4 | integer vector of length 2, 3, or 4  
vec2, vec3, vec4 | float vector of length 2, 3, or 4  
dvec2, dvec3, dvec4 | double vector of length 2, 3, or 4  
mat2 | two-by-two matrix  
mat3 | three-by-three matrix  
mat4 | four-by-four matrix  
### Numeric parameters
Create a binding to a numerical value in Max by creating a `param` tag without a `state` attribute.
```
<jittershader>
    <param name="myparam" type="float" default="1.0" />
</jittershader>

```

Set this value in Max using the `param` message.
![](https://docs.cycling74.com/images/cc6bc7fc90f591f856d4b3bb9b3f7022_226.webp)
Set a numeric parameter with a Max message.
### Texture parameters
To define a texture parameter, a `param` should have the type "int" and a default value that matches the parameter index. Max will recognize that this "int" param represents a texture if the `param` is later bound to a sampler type, for example a _sampler2DRect_ or a _sampler2D_.
```
<jittershader>
  <!-- Two input textures -->
  <param name="image1" type="int" default="0" />
  <param name="image2" type="int" default="1" />
  
  <param name="modelViewProjectionMatrix" type="mat4" state="MODELVIEW_PROJECTION_MATRIX" />
  <param name="textureMatrix0" type="mat4" state="TEXTURE0_MATRIX" />
  <param name="textureMatrix1" type="mat4" state="TEXTURE1_MATRIX" />
  <param name="jit_position" type="vec3" state="POSITION" />
  <param name="jit_texcoord" type="vec2" state="TEXCOORD" />
  <language name="glsl" version="1.5">
    <bind param="image1" program="fp" />
    <bind param="image2" program="fp" />
    <bind param="modelViewProjectionMatrix" program="vp" />
    <bind param="textureMatrix0" program="vp" />
    <bind param="textureMatrix1" program="vp" />
    <bind param="jit_position" program="vp" />
    <bind param="jit_texcoord" program="vp" />
    <program name="vp" type="vertex">
      <![CDATA[
      #version 330 core
      
      in vec3 jit_position;
      in vec2 jit_texcoord;
      out jit_PerVertex {
        vec2 texcoord0;
        vec2 texcoord1;
      } jit_out;
      uniform mat4 modelViewProjectionMatrix;
      uniform mat4 textureMatrix0;
      uniform mat4 textureMatrix1;
      
      void main() {
        gl_Position = modelViewProjectionMatrix*vec4(jit_position, 1.);
        jit_out.texcoord0 = vec2(textureMatrix0 * vec4(jit_texcoord, 0., 1.));
        jit_out.texcoord1 = vec2(textureMatrix1 * vec4(jit_texcoord, 0., 1.));
      }
    ]]>
    </program>
    <program name="fp" type="fragment">
      <![CDATA[
      #version 330 core
      
      // texcoords
      in jit_PerVertex {
        vec2 texcoord0;
        vec2 texcoord1;
      } jit_in;
      
      layout (location = 0) out vec4 outColor;
      
      // samplers
      uniform sampler2DRect image1;
      uniform sampler2DRect image2;
      void main() {
        vec4 im1 = texture(image1, jit_in.texcoord0);
        vec4 im2 = texture(image2, jit_in.texcoord1);
        outColor = im1 + im2;
      }
    ]]>
    </program>
  </language>
</jittershader>

```

In Max, you can set these textures using a texture list, or using the inlets of a [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") object.
![](https://docs.cycling74.com/images/f945bdc37e62d120a276ccf62690038d_669.webp)
Setting the texture inputs of a shader
### State parameters
Parameters can also bind to shader state variables, built-in uniform variables that expose the graphics engine state to JXS shader programs. To create a `param` bound to a state variable in this way, use the `state` attribute.
```
<param name="itvmat" type="mat3" state="NORMAL_MATRIX" />

```

Available shader parameter state bindings are listed below.
#### Model View and Projection Matrices
|  |   
---|---|---  
WORLD_MATRIX | mat4 | transforms into world coordinates, also known as model matrix  
VIEW_MATRIX | mat4 | transforms into current camera view, also known as eye  
MODELVIEW_MATRIX | mat4 | combined view and model (world) transform  
PROJECTION_MATRIX | mat4 | current camera projection transform  
VIEW_PROJECTION_MATRIX | mat4 | combined projection and view transform  
PREV_VIEW_PROJECTION_MATRIX | mat4 | previous frame VIEW_PROJECTION_MATRIX  
MODELVIEW_PROJECTION_MATRIX | mat4 | combined projection view and model transform  
PREV_MODELVIEW_PROJECTION_MATRIX | mat4 | previous frame MODELVIEW_PROJECTION_MATRIX  
NORMAL_MATRIX | mat3 | orients the normals in eye space  
CAM_PROJECTION_MATRIX | mat4 | provides the current rendering camera's projection matrix; in most cases is equivalent to PROJECTION_MATRIX except in cases where a full-screen quad is rendering, e.g. in a jit.gl.slab/pix (or jit.gl.pass).  
#### Camera
|  |   
---|---|---  
CAMERA_POSITION | vec3 | camera position in world space  
CAMERA_DIRECTION | vec3 | camera direction in world space  
VIEWPORT | vec2 | the pixel size of rendering window  
INVERSE_VIEWPORT | vec2 | the inverse of the viewport dims  
NEAR_CLIP | float | camera near clipping distance  
FAR_CLIP | float | camera far clipping distance  
FAR_CORNER | vec3 | far corner of the view frustrum  
#### Light
Shaders used in Jitter can reference up to eight simultaneous lights. To create a `param` bound to the state of a particular light, use a `state` attribute with a value like LIGHT0_POSITION to bind to the position of the first light, LIGHT1_POSITION to bind to the position of the second light, and so on.
|  |   
---|---|---  
LIGHT_VIEWPROJ_MATRIX0-7 | mat4 | scene seen from the light position  
LIGHT_RANGE0-7 | float | distance reached by the light  
LIGHT0-7_POSITION | vec3 | position of the light  
LIGHT0-7_DIRECTION | vec3 | direction of the light  
LIGHT0-7_AMBIENT | vec4 | ambient light color  
LIGHT0-7_DIFFUSE | vec4 | diffuse light color  
LIGHT0-7_SPECULAR | vec4 | specular light color  
LIGHT0-7_CUTOFF | float | the spotlight cutoff in degrees  
LIGHT0-7_EXPONENT | float | the spotlight exponent defining dropoff from cone center  
#### Material
|  |   
---|---|---  
AMBIENT | vec4 | material ambient color  
DIFFUSE | vec4 | material diffuse color  
SPECULAR | vec4 | material specular color  
EMISSION | vec4 | material emission color  
COLOR0 | vec4 | object color  
#### Texture
Similar to lights, Jitter shaders can reference up to eight texture inputs. For each one, create a `param` bound to the state of a particular texture with an indexed key for `state`. So TEXTURE0_MATRIX will bind to the texture transform matrix of the first texture, TEXTURE1_MATRIX to bind the texture transform matrix of the second texture, and so on.
|  |   
---|---|---  
TEXTURE0-7_MATRIX | mat4 | Texture tranform matrix for textures 0-7  
TEXDIM0-7 | vec2 | Texture dimentions for textures 0-7  
#### Time
Jitter provides time, frame and date based state parameters, useful for tasks like animating values and seeding random number generators in your shader program. `TIME` and `FRAME` will be specific to a particular shader program, whereas `GLOBAL_TIME`, `DELTA_TIME`, `CONTEXT_FRAME`, and `DATE` will be uniform for all shader programs running in a particular context.
|  |   
---|---|---  
TIME | float | time in seconds since program compilation  
GLOBAL_TIME | float | time in seconds since context initialization  
DELTA_TIME | float | time in seconds since previous frame  
FRAME | int | frame count since program compilation  
CONTEXT_FRAME | int | frame count since context initialization  
DATE | vec4 | year, month, day, time in seconds  
### Matrix transformations
You can apply a matrix transformation to any `param` with a _mat4_ `type`, using the `transform` attribute.
```
<param name="itvmat" type="mat4" state="VIEW_MATRIX" transform="INVERSE_TRANSPOSE" />

```

Recognized matrix transformations include `IDENTITY`, `TRANSPOSE`, `INVERSE` and `INVERSE_TRANSPOSE`.
### Vertex attributes
Several built-in vertex attributes are available via the following state tags:
|   
---|---  
POSITION | vec3  
TEXCOORD | vec2  
NORMAL | vec3  
TANGENT | vec3  
BITANGENT | vec3  
COLOR | vec4  
VERTEX_ATTR | user-defined  
VERTEX_ATTR0 | user-defined  
VERTEX_ATTR1 | user-defined  
VERTEX_ATTR2 | user-defined  
VERTEX_ATTR3 | user-defined  
The state tags VERTEX_ATTR and VERTEX_ATTR0 through VERTEX_ATTR4 are for custom vertex attributes. Define the `param` tag like so:
```
<param name="pvel" type="vec4" state="VERTEX_ATTR" />

```

and in the vertex program:
```
in vec4 pvel;

```

To set the values of custom vertex attributes from the patcher, send [jit.gl.mesh](https://docs.cycling74.com/reference/jit.gl.mesh "jit.gl.mesh") the `vertex_attr_matrix` message followed by the name of a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") containing the attribute values. The example patcher [custom.vertex.attribute](c74max://patcher/custom.vertex.attribute.maxpat) demonstrates this.
## Shaders and the `language` tag
After the description, textures, and parameters are declared, the `language` tag includes the shader definitions themselves.
```
  <!-- list of language implementations -->
  <language type="glsl" version="1.0">

    <!-- list of binding targets for shader parameters -->
    <bind param="myparam" program="vp"/>

    <!-- vertex and fragment programs -->
    <program name="vp" type="vertex" source="sh.passthru.xform.vp.glsl"/>
    <program name="fp" type="fragment">
        <![CDATA[
            // entry point
            void main()
            {
                gl_FragColor=vec4(0.5, 0.5, 0.5, 1.0);
            }
        ]]>
    </program>
</language>

```

The language tag includes the `type`, which will always be "glsl", as well as the `version`. Shader versions 1.5 or higher are treated as "modern" shaders, whereas anything lower will be treated as legacy and transformed automatically before getting passed to the graphics engine.
### The `bind` tag
The `bind` tag binds declared parameters to variables in any one of the shader programs.
```
<jittershader>
    <param name="myparam1" type="vec3" default="3.0 4.0 5.0" />
    <param name="myparam2" type="float" default="0" />

    <language type="glsl" version="1.5">

    <bind param="myparam1" program="vp" />
    <bind param="myparam2" program="fp" />

    <program name="vp" type="vertex">
    <![CDATA[
        uniform vec3 myparam1;

        void main() {
            // ... the vertex program
        }
    ]]>
    </program>

    <program name="fp" type="fragment">
    <![CDATA[
        uniform float myparam2;

        void main() {
            // ... the fragment program
        }
    ]]>
    </program>

    </langauge>
</jittershader>

```

The `param` attribute of a `bind` tag identifies a parameter with that name. The `program` attribute directs that parameter to a particular program. Within the program, the parameter is bound to the variable with the same name.
The `type` of the `param` tag should match the type of the variable in the vertex, fragment, or geometry shader program. One exception is for [texture parameters](https://docs.cycling74.com/userguide/jitter/jxs_file_format/#texture-parameters). The type of the `param` for a texture parameter should be `int`, and it should be bound to a variable with a "Sampler" type, like `Sampler2D` or `Sampler2DRect`.
### The `include` tag
After binding parameters but before declaring shaders, you can use the `include` tag to include external _glsl_ sources. These can be any files in the Max search path.
```
<bind param="FrontMaterialParameters" program="vp" />
<bind param="LightingParameters" program="vp" />

<include source="diffuse.glsl" program="vp" />
<include source="specular.glsl" program="vp" />

<program name="vp" type="vertex">

```

### The `program` tag
A `program` tag contains the actual shader program. The `name` of a `program` tag can be anything, and is used by the `bind` tag to bind external parameters to program variables. The `type` attribute of a `program` tag can be `vertex`, `fragment`, or `geometry`. To define the shader program itself, a program can use the `source` attribute to specify a `.glsl` file, or the contents of the `program` tag can be character data containing the glsl shader program itself.
```
<language type="glsl" version="1.0">
    <program name="vp" type="vertex" source="sh.passthru.xform.vp.glsl"/>
    <program name="fp" type="fragment">
        <![CDATA[
        void main()
        {
            gl_FragColor=vec4(0.5, 0.5, 0.5, 1.0);
        }
        ]]>
    </program>
</language>

```

