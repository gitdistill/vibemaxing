---
description: The JXS File Format
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter99_appendixc/
title: Appendix C
---

Download Series Content and Patchers
# Appendix C: The JXS File Format
## The Jitter Shader Description File
Jitter provides a means of encapsulating shader parameters and programs through an XML based shader description file (_JXS_). This _JXS_ file offers an easy way of setting up any required OpenGL state to achieve a particular effect, without any additional patcher related work.
The _JXS_ file may contain a list of parameters and textures, followed by a set of language dependent implementations for the shader's vertex and fragment programs.
Each language implementation must specify both a vertex and a fragment program. These programs may either reference external files, or be stored inline within a CDATA section or an XML comment. Programs for each language implementation will be loaded and bound in the order that they are listed in the _JXS_ file. If a particular language implementation fails to compile, the next implementation will be used, until a successful candidate is found.
Inside of the language implementation declaration, any shader parameter previously specified must be identified with a bind tag that indicates which shader program should receive the parameter's values.
The following listing outlines the format of a typical _JXS_ file:
```
<jittershader name="myshader">
  <!-- optional description -->
  <description>This is my shader</description>

  <!-- optional list of texture objects to bind -->
  <texture file="mytexture.jpg"/>

  <!-- optional list of shader parameters -->
  <param name="myparam" type="vec3" default="3.0 4.0 5.0">
    <description>This is my parameter</description>
  </param>

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
</jittershader>

```

Note that the XML document must be well-formed with matching opening/closing tags.
## JXS Shader State Variables
Jitter provides several built in uniform variables that expose OpenGL state to _JXS_ shader programs. These can be accessed by specifying the variable name in the state attribute of the XML param tag For exmaple:
```
<param name="itvmat" type="mat3" state="NORMAL_MATRIX" />

```

Available shader parameter state bindings are listed below.
### Model View and Projection Matrices
  * **WORLD_MATRIX** (mat4)
  * **VIEW_MATRIX** (mat4)
  * **MODELVIEW_MATRIX** (mat4)
  * **PROJECTION_MATRIX** (mat4)
  * **VIEW_PROJECTION_MATRIX** (mat4)
  * **MODELVIEW_PROJECTION_MATRIX** (mat4)
  * **PREV_MODELVIEW_PROJECTION_MATRIX** (mat4)
  * **NORMAL_MATRIX** (mat3)


### Camera
  * **CAMERA_POSITION** (vec3)
  * **CAMERA_DIRECTION** (vec3)
  * **VIEWPORT** (vec2)
  * **INVERSE_VIEWPORT** (vec2)
  * **NEAR_CLIP** (float)
  * **FAR_CLIP** (float)
  * **FAR_CORNER** (vec3)


### Light
  * **LIGHT_VIEWPROJ_MATRIX _0-7_** (mat4)
  * **LIGHT_RANGE _0-7_** (float)
  * **LIGHT _0-7_ _POSITION** (vec3)
  * **LIGHT _0-7_ _DIRECTION** (vec3)
  * **LIGHT _0-7_ _AMBIENT** (vec4)
  * **LIGHT _0-7_ _DIFFUSE** (vec4)
  * **LIGHT _0-7_ _SPECULAR** (vec4)
  * **LIGHT _0-7_ _CUTOFF** (float)
  * **LIGHT _0-7_ _EXPONENT** (float)


### Material
  * **AMBIENT** (vec4)
  * **DIFFUSE** (vec4)
  * **SPECULAR** (vec4)
  * **EMISSION** (vec4)


### Texture
  * **TEXTURE _0-7_** _MATRIX (mat4)
  * **TEXDIM _0-7_** (vec2)


## Matrix Transformations
Matrix variables (_mat3_ and _mat4_ type variables) can be transformed in specified ways using the **transform** attribute of the XML _param_ tag:
```
<param name="itvmat" type="mat4" state="VIEW_MATRIX" transform="INVERSE_TRANSPOSE" />

```

Available matrix transformations include:
  * **IDENTITY**
  * **TRANSPOSE**
  * **INVERSE**
  * **INVERSE_TRANSPOSE**


## Vertex Attributes
Jitter _JXS_ shader programs are able to access custom vertex attributes via the **VERTEX_ATTR** state tag:
```
<param name="pvel" type="vec4" state="VERTEX_ATTR" />

```

and in the vertex program:
```
attribute vec4 pvel;

```

To set the values of custom vertex attributes from the patch, send [jit.gl.mesh](https://docs.cycling74.com/reference/jit.gl.mesh "jit.gl.mesh") the `vertex_attr_matrix` message followed by the name of a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") containing the attribute values. The example patch `custom.vertex.attribute.maxpat` demonstrates this.
Additionally there are several built in vertex attributes available via the following state tags:
  * **POSITION** (vec3)
  * **NORMAL** (vec3)
  * **TANGENT** (vec3)
  * **BITANGENT** (vec3)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
