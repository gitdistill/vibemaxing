---
description: Working with multiple render passes to apply post-processing effects
group: Jitter
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/jitter/render_passes/
title: Render Passes
---

# Render Passes
Rendering means taking the elements of a scene, including the lighting, camera position, and the geometry of the objects in the scene, and using those to compute an image. After the initial pass, we can perform additional render passes to create postprocessing effects. These passes can use the initial image output, along with intermediary structures computed during the previous pass—for example the depth buffer—to produce another image. Depth of field is a classic example of a postprocessing effect, using the depth buffer to apply a blur proportional to the distance from the camera. Multiple passes can be chained together to produce complex effects.
Geometry First Render Depth Flow Camera Lights Depth of Field Motion Blur Final Render SCENE RENDER INTERMEDIATE PASSES
Typical graphics processing rendering pipeline
## Using jit.gl.pass
The [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") object provides a high-level, text-based way to describe a render pass. Working with a pass description file (a .jxp file), you can combine Jitter shaders defined in text (.jxs files) with Gen-based Jitter shaders (.genjit files) to create a final, complex shader with multiple stages.
Because a [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") object works with intermediate render targets like the depth buffer, it works differently from objects like [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") or [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"), which can work as simple video effects. The [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") object always works with a [jit.gl.node](https://docs.cycling74.com/reference/jit.gl.node "jit.gl.node") object, even if it's the internal [jit.gl.node](https://docs.cycling74.com/reference/jit.gl.node "jit.gl.node") object in a [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") object.
To work with a jit.gl.pass, geometry must have a material attached to it, for example by attaching a [jit.gl.material](https://docs.cycling74.com/reference/jit.gl.material "jit.gl.material") or a [jit.gl.pbr](https://docs.cycling74.com/reference/jit.gl.pbr "jit.gl.pbr") object.
The typical use pattern for [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") is to bind [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") to a [jit.gl.node](https://docs.cycling74.com/reference/jit.gl.node "jit.gl.node") object with the same name. Multiple [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") objects can be connected together to create complex effects. Finally, the texture output of the last jit.gl.pass object is connected to a [jit.gl.layer](https://docs.cycling74.com/reference/jit.gl.layer "jit.gl.layer") object to be displayed in the root rendering context.
![](https://docs.cycling74.com/images/db1810b270a1f1ae3148325c9c083bb2_980.webp) It's typical to use jit.gl.pass with jit.gl.node and jit.gl.layer.
When a [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") object is connected to a [jit.gl.node](https://docs.cycling74.com/reference/jit.gl.node "jit.gl.node"), the `@capture` attribute is controlled by the [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") object. It will be set automatically to accommodate for the render targets requested by all [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") effects bound to that node.
## The JXP File Format
To determine its behavior, a [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") object loads a Jitter Pass file: a specially-formatted XML file that defines one or more render passes. Every JXP file has a `<jitterpass>` node as its root.
```
<jitterpass>
    <!-- Pass definitions go here -->
</jitterpass>

```

Max includes several examples of common post-processing effects, implemented in the JXP format. Start with [motionblur](c74max://patcher/pass.motionblur.maxpat) and look for other examples in the same folder.
### The <pass> tag
The `<jitterpass>` tag can contain multiple `<pass>` tags, each of which defines one pass.
```
<jitterpass>
  <pass name="passname">
    <!-- Pass definition here -->
  </pass>
</jitterpass>

```

Each `<pass>` must have a name attribute, which is the identifier that a [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") will use with the `@fxname` attribute to load the pass definition. For built-in pass definitions, the `@fxname` attribute is sufficient to select the pass. To load a custom `pass` definition, use the `@file` attribute to load the custom pass file, followed by `@fxname` to load the specific pass.
![](https://docs.cycling74.com/images/0f9153474e228021d26ce980023d56ce_840.webp) jit.gl.pass loading a custom JXP file
### The <bind> tag
At the top of a `<pass>` tag, you can can use the `<bind>` tag to create a binding between Max attributes and shader parameters. Use the `name` attribute to define the name of the attribute as it will appear in Max. The `param` attribute will specify which shader parameter to bind to. The `param` attribute will bind to the first shader parameter among `<subpass>` tags with a matching name.
![](https://docs.cycling74.com/images/029fbd65e4be6e1068275eb96d03ea07_960.webp) The <bind> tag lets you bind shader parameters to Max attributes. A custom attribute will be created for each <bind> tag.
### The <inputs> tag
A `<pass>` tag can optionally contain an `<inputs>` tag containing one or more `<input>` tags specifying input source properties (see [source input](https://docs.cycling74.com/userguide/jitter/render_passes/#source-input)). The properties are exposed via [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture") attributes on the underlying render targets of the bound [jit.gl.node](https://docs.cycling74.com/reference/jit.gl.node "jit.gl.node") context. A common use case might be inverting the depth buffer clear value. Render target `erase_color` defaults to 0 0 0 0. Since the alpha component determines the depth, this default implies a depth clear value 0. To invert, specify a 1 for the alpha component of `erase_color` in the `<input>` tag for `source` NORMALS. The code below demonstrates this, and specifies `type` and `erase_color` per target.
```
<jitterpass>
  <pass name="passname">
    <inputs>
      <input source="COLOR" type="char" erase_color="0 0 0 1" />
      <!-- inverted depth clear value -->
      <input source="NORMALS" type="float16" erase_color="0 0 0 1" />
    </inputs>
    <!-- subpasses -->
  </pass>
</jitterpass>

```

Important to note, input sources are shared by all pass effects bound to a particular [jit.gl.node](https://docs.cycling74.com/reference/jit.gl.node "jit.gl.node") context. As a concequence any `<input>` tag attribute defined here will change that attribute for all active passes in the context.
### The <subpass> tag
Each `<pass>` tag contains one or more `<subpass>` tags. These `<subpass>` tags define which shader program to load, as well as how that shader should connect to the various input sources available (see [subpass sources](https://docs.cycling74.com/userguide/jitter/render_passes/#subpass-sources)). To load a shader, set the `file` attribute to load a Jitter shader (a `.jxs` file), or set the `gen` attribute to load a [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") shader (a `.genjit` file).
```
<jitterpass>
  <pass name="passname">
    <subpass file="cf.radialblur.jxs">
      <!-- subpass inputs -->
    </subpass>
    <subpass gen="kaleido.genjit">
      <!-- subpass inputs -->
    </subpass>
  </pass>
</jitterpass>

```

A `<subpass>` tag can also have a name, allowing it to be referred to as an input by other subpasses. Finally, a subpass can also use the `dimscale` attribute to scale the size of any dimension of the output texture, and the `rect` attribute to adjust or invert the subpass texture coordinates. See the object reference for [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") for more.
```
<jitterpass>
  <pass name="passname">
    <!-- a named subpass can be referred to by other subpasses -->
    <subpass file="cf.radialblur.jxs" name="subpass_name">
    </subpass>

    <!-- here dimscale will downsample (shrink) the output texture -->
    <subpass file="cf.radialblur.jxs" dimscale="0.5 0.5">
    </subpass>

    <!-- rect defines normalized texture coordinates, left-bottom-right-top -->
    <!-- used in this way, we could mirror the texture left to right-->
    <subpass file="cf.radialblur.jxs" rect="1 0 0 1">
    </subpass>

    <!-- >
  </pass>
</jitterpass>

```

### Subpass sources
The number of texture inputs to a subpass will depend on the number of texture inputs of its loaded shader. You can connect each input to a different source using the `<input>` child tag. The input to a subpass can be a named texture, another named subpass, or one of several special sources.
#### Named texture input
Use the `name` attribute to specify a named texture as input.
```
<jitterpass>
  <pass name="passname">
    <subpass file="cf.radialblur.jxs">
      <input name="named_texture" />
    </subpass>
  </pass>
</jitterpass>

```

### Source input
The `source` tag can get input from any of several special sources.
```
<jitterpass>
  <pass name="passname">
    <subpass file="hdr.bloom.jxs">
      <input source="VELOCITY" />
    </subpass>
  </pass>
</jitterpass>

```
Name | Description  
---|---  
COLOR | RGBA color render target  
NORMALS | normals in RBG, depth buffer in A  
VELOCITY | horizontal velocity in R, vertical velocity in G  
PREVIOUS | the preceeding subpass output  
HISTORY | the previous output (output from the previous frame) of the entire `<pass>`  
TEXTURE0...N | any of the textures, input as a list, to jit.gl.pass. If three texture names are bound to the `@texture` attribute of jit.gl.pass, refer to the first one with TEXTURE0, the second with TEXTURE1, and the third with TEXTURE2.  
SUBPASS0...N | any subpass output of the current `<pass>`. The first `<subpass>` is SUBPASS0, the second is SUBPASS1, and so on.  
ALBEDO | the albedo material component (non-[jit.gl.pbr](https://docs.cycling74.com/reference/jit.gl.pbr "jit.gl.pbr") materials use diffuse).  
ROUGHMETAL | material roughness in R and metalness G (non-[jit.gl.pbr](https://docs.cycling74.com/reference/jit.gl.pbr "jit.gl.pbr") materials use inverted shininess in R and shininess in G).  
ENVIRONMENT | the environment cubemap texture of the active [jit.gl.environment](https://docs.cycling74.com/reference/jit.gl.environment "jit.gl.environment"). Specifying will disable environment input on bound materials.  
Pass effects that request NORMALS, VELOCITY, ALBEDO, ROUGHMETAL, or ENVIRONMENT as input sources require [jit.gl.material](https://docs.cycling74.com/reference/jit.gl.material "jit.gl.material") or [jit.gl.pbr](https://docs.cycling74.com/reference/jit.gl.pbr "jit.gl.pbr") generated materials.
#### Subpass input
Use the `subpass` attribute to specify another subpass to use as input.
```
<jitterpass>
  <pass name="passname">
    <subpass file="cf.laplace.jxs" name="laplace">
      <input source="COLOR" />
    </subpass>
    <subpass file="hdr.bloom.jxs">
      <input subpass="laplace" />
    </subpass>
  </pass>
</jitterpass>

```

The output index of a multi-output `subpass` input type is specified using an "output" attribute and 0-based indexing. The previous frame of subpass input types can be requested using the history keyword and setting it to 1. For example to set second output of the previous frame as the input.
```
<input subpass="mysubpass" output="1" history="1" />

```

