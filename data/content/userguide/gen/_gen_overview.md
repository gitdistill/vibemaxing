---
description: Overview of Gen, the graph-based programming language for low-level signal processing.
group: Gen
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/gen/_gen_overview/
title: Gen Overview
---

# Gen
Gen is a visual, graph-based programming language. It's syntax is extremely similar to Max, so similar that we program Gen patchers using the Max environment. However, Gen uses a different set of objects from Max—within a [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") subpatcher, you can only use Gen objects.
The main difference between Max and Gen is that while Max works by sending messages between instantiated objects, a Gen patcher is more like a description of how a patcher should be. In order to process audio or computer graphics, a Gen patcher is first used to generate code, which is then compiled and run in the Max environment.
## Why Use Gen?
  * You want to do low-level, visual programming, while still getting the performance of compiled C or GLSL code.
  * It's easier to describe your process using text code, but you want to use [codebox](https://docs.cycling74.com/reference/gen_common_codebox/ "gen_common_codebox"), rather than compiling a C object.
  * You need single-sample delay for signal processing techniques like filtering, synthesis, and physical modeling.
  * You want to design a graphics shader, but you don't want to write GLSL code.
  * You want to export your C or GLSL code, for use in an environment other than Max.


### Examples
  * arbitrary new oscillator and filter designs using single-sample feedback loops with [gen~](https://docs.cycling74.com/reference/gen~/ "gen~")
  * reverbs and physical models using networks of short feedback delays with [gen~](https://docs.cycling74.com/reference/gen~/ "gen~")
  * sample-accurate [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") processing such as waveset distortions with [gen~](https://docs.cycling74.com/reference/gen~/ "gen~")
  * efficient frequency-domain processing such as spectral delays using [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") inside [pfft~](https://docs.cycling74.com/reference/pfft~/ "pfft~")
  * custom video processing filters as fast as C compiled externals with [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), and graphics card accelerated with [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix")
  * geometry manipulation and generation with [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen")
  * particle system design with [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen")
  * iso-surface generation with distance fields in [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen")


### Performance Improvements
  * A chain of Gen objects compiles down into one single meta-object, removing the usual overhead that Max encounters when passing messages and signals between objects.
  * replacement for [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") with performance and interface improvements
  * You want to be able to have a simple way to make use of the GPU for image processing both in visual and textual form


## Working with Gen
Gen patchers are specialized for specific domains such as audio (MSP) and matrix and texture processing (Jitter). The Max Gen object is called [gen](https://docs.cycling74.com/reference/gen/ "gen"). The MSP Gen object is called [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"). The Jitter Gen objects are [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"). Each of these Gen objects contains within it a Gen patcher. While gen patchers share many of the same capabilities, each Gen object has functionality specific to its domain. For example, Gen patchers in [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") have delay lines while Gen patchers in [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") have vector types.
  * [A listing of operators common to all Gen objects](https://docs.cycling74.com/userguide/gen/gen_common_operators/)
  * [A listing of operators common to all gen~ objects](https://docs.cycling74.com/userguide/gen/gen~_operators/)
  * [A listing of operators common to all Gen Jitter objects](https://docs.cycling74.com/userguide/gen/gen_jitter_operators/)


## Creating a Gen Patch
Create a [gen](https://docs.cycling74.com/reference/gen/ "gen") or [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") object for message and signal processing, and create a [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), or [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") for image processing.
  * [gen](https://docs.cycling74.com/reference/gen/ "gen") — create a processing object that runs at message rate, using [gen common](https://docs.cycling74.com/userguide/gen/gen_common_operators/) and [gen dsp](https://docs.cycling74.com/userguide/gen/gen~_operators/) operators.
  * [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") — create a signal object that runs at signal rate, in Max's DSP chain, using [gen common](https://docs.cycling74.com/userguide/gen/gen_common_operators/) and [gen dsp](https://docs.cycling74.com/userguide/gen/gen~_operators/) operators.
  * [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") — create a matrix processing object that runs on the CPU. Uses [gen common](https://docs.cycling74.com/userguide/gen/gen_common_operators/) and [gen jitter](https://docs.cycling74.com/userguide/gen/gen_jitter_operators/) operators.
  * [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") — create a matrix processing object that runs on the CPU, but that's optimized to work on frames of video as opposed to more general matrix types. Always locked to 4 planes, but somewhat more efficient than jit.gen. Uses [gen common](https://docs.cycling74.com/userguide/gen/gen_common_operators/) and [gen jitter](https://docs.cycling74.com/userguide/gen/gen_jitter_operators/) operators.
  * [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") — create a texture processing object that runs on the GPU. Always locked to 4 planes, but much faster and more efficient than [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") or [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"). Compiles to GLSL code, which can be exported and run in other graphics processing environments. Uses [gen common](https://docs.cycling74.com/userguide/gen/gen_common_operators/) and [gen jitter](https://docs.cycling74.com/userguide/gen/gen_jitter_operators/) operators.


Whichever object you make, you'll get a Gen object that contains a Gen subpatcher. Just like a [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") object, you can double-click on the Gen object to see its contents. When you do, you'll see the default Gen patcher, which simply adds together its inputs.
![](https://docs.cycling74.com/images/c342b0a90756f4b3ac8baa37e47d5898_640.webp) A gen~ object, and its contents
Gen patchers can be embedded within the [gen](https://docs.cycling74.com/reference/gen/ "gen"), [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), etc. object, or can be loaded from external files (with `.gendsp` or `.genjit` file extensions respectively) using the `@gen` attribute of [gen](https://docs.cycling74.com/reference/gen/ "gen"), [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), etc. objects.
## Patching in Gen
Patching in Gen should feel very similar to patching in Max. The basic Max paradigms—making objects, connection them—are all the same.
The Gen patcher window has [some small differences](https://docs.cycling74.com/userguide/patcher_window/#gen-window) from the standard Max window, in order to facilitate patching in Gen.
### Conceptual differences between Max and Gen
  * In Max, objects send messages to each other. In Gen, there are no messages. All operations are synchronous, much like signal flow in Max. Because of this, there are no UI objects (sliders, buttons etc.). However the [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") operator can be used to receive message-rate controls from the normal Max world. There is no need to differentiate hot and cold inlets, or the order in which outlets "fire", since all objects and outlets always fire at the same time.
  * There are no `send` and `receive` operators in Gen patcher. Gen patchers are connected to the outside world through the [in](https://docs.cycling74.com/reference/gen_common_in/ "gen_common_in"), [out](https://docs.cycling74.com/reference/gen_common_out/ "gen_common_out"), and [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") operators. In [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), there are some additional operators such as [history](https://docs.cycling74.com/reference/gen_dsp_history/ "gen_dsp_history"), [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") and [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") that are controllable with messages to [gen~](https://docs.cycling74.com/reference/gen~/ "gen~").
  * The usual distinction between int and float numbers does not apply to Gen patchers. At the Gen patcher level, everything is a 64-bit floating point number.
  * The `codebox` is a special operator for Gen patchers, in which more complex expressions can be written using the [GenExpr](https://docs.cycling74.com/userguide/gen/gen_genexpr/) language.


## Auto-compile
Remember that Gen patchers must be compiled before they can run. By default, the compilation process occurs in the background while you are editing, so that you can see or hear the results immediately. This auto-compilation process can be disabled using the _Auto-Compile_ toggle in the Gen patcher toolbar. With auto-compilation disabled, click the _Compile_ icon to compile manually.
See the [Gen patcher differences](https://docs.cycling74.com/userguide/patcher_window/#gen-window) section of the [Patcher Window](https://docs.cycling74.com/userguide/patcher_window/) guide for more.
## Gen Operators
The fundamental processing object in Max is the Object, and the fundamental processing unit in Gen is the Gen Operator. You can call an operator by creating an object box in Gen, or by calling the operator as a function in [GenExpr](https://docs.cycling74.com/userguide/gen/gen_genexpr/) code.
![](https://docs.cycling74.com/images/4fb374fd8f018cbebc9da942e9738839_480.webp) Patching into a change operator is the same as calling the change function in GenExpr
Gen operators take arguments and attributes just like Max objects, but these are purely declarative. Since there is no messaging in Gen patchers, the attribute value set when the operator is created does not change. Attributes are most often used to specialize the implementation of the process the operator represents (such as setting a maximum value for `param` using the `@max` attribute.)
In many cases, the specification of an object’s argument effectively replaces the corresponding inlet. This is possible in Gen because there is no messaging and all processing is synchronous. For example, the `+` operator takes two inputs, but if an argument is given only one input needs to be specified as an inlet.
![](https://docs.cycling74.com/images/bf3dce4c98cac66444d34998a56f25b1_279.webp) If the + operator has an argument, it no longer needs a second inlet
An inlet with no connected patchcord uses a default value instead (often zero, but check the inlet assist strings for each operator). An inlet with multiple connections adds them all together, just like with signal patchcords.
![](https://docs.cycling74.com/images/2fe2b1256bc71d9e4d35165c34869a7c_391.webp) In gen and gen~, two patch cables connected to the same operator inlet will add together.
## Standard Operators
Many standard objects behave like the corresponding Max or MSP object, such as all arithmetic operators (including the reverse operators like `!-`, `!/` etc.), trigonometric operators (`sin`, `cosh`, `atan2` etc.), standard math operators (`abs`, `floor`, `pow`, `log`, etc.), boolean operators (`>`, `==`, `&&` (also known as `and`) etc.) and other operators such as `min`, `max`, `clip` (also known as `clamp`), `scale`, `fold`, `wrap`, `cartopol`, `poltocar` etc. In addition there are some operators in common with GLSL (`fract`, `mix`, `smoothstep`, `degrees`, `radians` etc.) and some drawn from the [jit.op](https://docs.cycling74.com/reference/jit.op "jit.op") operator list (`>p`, `==p`, `absdiff` etc.). There are several predefined constants available (`pi`, `twopi`, `halfpi`, `invpi`, `degtorad`, `radtodeg`, `e`, `ln2`, `ln10`, `log10e`, `log2e`, `sqrt2`, `sqrt1_2` and the same in capitalized form as `PI`, `TWOPI` etc), which can be used in place of a numeric argument to any operator.
![](https://docs.cycling74.com/images/29fe909279b13d3a5e01b4eaba075045_237.webp) Multiply by the constant pi using twopi or TWOPI.
## Argument Expressions
For all objects that accept numeric arguments (e.g. `[+ 2.]` or `[max 1.]`) argument expressions can be used in their place. Argument expressions are simple statements with known inputs such as constants, Gen patcher inputs, and parameter names. Many gen operators can be used as argument expressions, particularly the math operators ([sqrt](https://docs.cycling74.com/reference/gen_common_sqrt/ "gen_common_sqrt"), [cos](https://docs.cycling74.com/reference/gen_common_cos/ "gen_common_cos"), etc.). Argument expressions can help simplify Gen patchers where all that is needed is the calculation of a constant that isn't pre-defined, such as 3∗pi/23*pi/23∗pi/2. For example, in the patch below, there is a scale operator with an argument of `sqrt(2)*2`.
![](https://docs.cycling74.com/images/19f693ed1dc6c41cd30e8ebab4b53131_670.webp)
Similarly, the mul (*) operator has an argument expression of `1+in2`. Since `in2` is the GenExpr equivalent of `[in 2]`, it can be used in an argument expression.
## Send and Receive
[send](https://docs.cycling74.com/reference/gen_common_send/ "gen_common_send") and [receive](https://docs.cycling74.com/reference/gen_common_receive/ "gen_common_receive") within gen patchers can be used to connect objects without patchcords. In gen patchers, [send](https://docs.cycling74.com/reference/gen_common_send/ "gen_common_send") and [receive](https://docs.cycling74.com/reference/gen_common_receive/ "gen_common_receive") can only be used locally. They will not connect to [send](https://docs.cycling74.com/reference/gen_common_send/ "gen_common_send") and [receive](https://docs.cycling74.com/reference/gen_common_receive/ "gen_common_receive") objects in other gen patchers or gen subpatchers.
[send](https://docs.cycling74.com/reference/gen_common_send/ "gen_common_send") and [receive](https://docs.cycling74.com/reference/gen_common_receive/ "gen_common_receive") take a name argument that determines connectivity.
![](https://docs.cycling74.com/images/daca0d5db805d49a6f2e6bcad2969066_428.webp)
Using send and receive in a Gen patcher
There can be multiple [send](https://docs.cycling74.com/reference/gen_common_send/ "gen_common_send") and [receive](https://docs.cycling74.com/reference/gen_common_receive/ "gen_common_receive") objects with the same name without issue. If there are multiple [send](https://docs.cycling74.com/reference/gen_common_send/ "gen_common_send") objects with the same name, they will be summed just as if multiple patchcords were connected to the same inlet. If there are multiple [receive](https://docs.cycling74.com/reference/gen_common_receive/ "gen_common_receive") objects with the same name, they will all receive identical input from their corresponding [send](https://docs.cycling74.com/reference/gen_common_send/ "gen_common_send") objects.
## Subpatchers and Abstractions
Subpatchers and abstraction in Gen objects behave practically identically to standard Max subpatchers and abstractions. In Gen objects, subpatchers are created with the [gen](https://docs.cycling74.com/reference/gen_common_gen/ "gen_common_gen") operator. If the [gen](https://docs.cycling74.com/reference/gen_common_gen/ "gen_common_gen") operator is given the name of a Gen patcher as an argument, it will use it to set the titlebar of the subpatcher.
![](https://docs.cycling74.com/images/09f84d3d8709e9627b7328be28ab89b3_548.webp)
Using the gen operator to make subpatchers in Gen
Abstractions, as with standard max abstractions, are created by saving a Gen patcher, then instantiated by creating an object with the name of the saved Gen file to load as the abstraction. For example, if an operator named `differential` is created, gen will look for the file `differential.gendsp` with [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") and `differential.genjit` with the Jitter Gen objects. Instantiating abstractions this way is shorthand for setting the `@file` attribute on the [gen](https://docs.cycling74.com/reference/gen_common_gen/ "gen_common_gen") operator. For example, creating an operator `differential` is equivalent to `gen @file differential`. Abstractions of [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") and [gen](https://docs.cycling74.com/reference/gen/ "gen") patchers save with the `.gendsp` file extension and abstractions of [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") save with the `.genjit` file extension.
![](https://docs.cycling74.com/images/049a8812574065451a37c4767664f553_560.webp)
Save a Gen abstraction by choosing _Save As..._ from the _File_ menu when focused on a Gen subpatcher.
## Subpatcher/Abstractions and Parameters
Just like normal gen patchers, Gen subpatchers and abstractions can also contain parameters. When used in subpatchers and abstractions, parameters behave like named inlets with default values. If nothing is connected to a parameter in a subpatcher or abstraction, the parameter will be a constant and its value will be its default.
![](https://docs.cycling74.com/images/52fc2dbac7f096401d71128ba408d1d7_645.webp)
In the above example, the subpatcher has a parameter `@scale` with a default of 1. In the subpatcher's sidebar, we see this represented in the [GenExpr](https://docs.cycling74.com/userguide/gen_genexpr.md) code as
```
Param scale(1.);

```

However, in the parent Gen patcher, the parameter gets converted into a constant because nothing is connected to the parameter.
![](https://docs.cycling74.com/images/418acba52d63e59872875e9ef7b0f348_566.webp)
The first line in the parent patcher's GenExpr sidebar reads:
```
scale_1 = 0.;

```

This sets the `@scale` parameter to a constant value.
Since subpatcher and abstraction parameters don't create their own inlets to connect objects to, there is a special operator called [setparam](https://docs.cycling74.com/reference/gen_common_setparam/ "gen_common_setparam") that can be connected to any inlet for this specific purposes. [setparam](https://docs.cycling74.com/reference/gen_common_setparam/ "gen_common_setparam") connects all of its inputs to a named parameter in a subpatcher or abstraction. It requires an argument specifying the name of the parameter to connect to.
When [setparam](https://docs.cycling74.com/reference/gen_common_setparam/ "gen_common_setparam") is connected to a parameter, the parameter changes from being a constant to a dynamic variable equivalent to the value at the input of the [setparam](https://docs.cycling74.com/reference/gen_common_setparam/ "gen_common_setparam") object.
![](https://docs.cycling74.com/images/f6dc948cae126a065bc0ea31157a34e4_1024.webp)
Notice that the code in the parent subpatcher has changed from a constant to:
```
setparam_1 = in2;

```

`in` is conected to the inlet of the [setparam](https://docs.cycling74.com/reference/gen_common_setparam/ "gen_common_setparam") object so the scale parameter takes on that value.
## Setting Parameter Defaults
The default value for [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") objects within Gen patchers and subpatchers can be set either directly in the [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") object in the form `param paramnamevalue(s)` or in the containing [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") object box in the form `gen~ @paramname value(s)`. If a default is declared in both the [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") object and in the containing gen object box, the object box will override the value declared in the [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") object.
![](https://docs.cycling74.com/images/8b6ef50ddbeb685212ee57203113b5f4_504.webp) The parameter value @foo 21 in the top level overrides the default value of 74.
This also applies to Gen subpatchers and abstractions; however, object box declared values only go one patcher deep. So `gen~ @foo 10` would set the default for any [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") object named `foo` in the top-level [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") patcher, but not [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") objects named `foo` contained in Gen subpatchers and abstractions.
![](https://docs.cycling74.com/images/7cbc38e2074638ab4524b9924a66e172_833.webp)
## The gen~ Object
The [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") object is specifically for operating on MSP audio signals. Unlike MSP patching however, operations in a Gen patcher are combined into a single chunk of machine code, making possible many more optimizations that can make complex processes more efficient, and allow you to design processes which must operate on a per-sample level, even with feedback loops.
Working in [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") opens up scope to design signal processes at a lower level, even per-sample. Because of this, many operators take duration arguments in terms of samples (where the equivalent MSP objects would use milliseconds).
## gen~ Operators
In addition to the standard Gen operators , which are often similar to the equivalent MSP objects (such as `clip`, `scale`, `minimum`, `maximum`, etc.), many of the operators specific to the [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") domain mirror existing MSP objects to make the transition to [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") easier. There are familiar converters (`dbtoa`, `atodb`, `mtof`, `ftom`, `mstosamps`, `sampstoms`), oscillators (`phasor`, `train`, `cycle`, `noise`), and modifiers (`delta`, `change`, `sah`, `triangle`). In addition there are some lower-level operators to avoid invalid or inaudible outputs (`isnan`, `fixnan`, `isdenorm`, `fixdenorm`, `dcblock`).
A global value of `samplerate` is available both as an object, and as a valid value for an argument of any object.
![](https://docs.cycling74.com/images/476f79543926c55079c01ec2ffbe3b10_525.webp)
The samplerate value is available as an object and as a constant in codebox
## History
In general, the Gen patcher will not allow a feedback loop (since it represents a synchronous process). To create a feedback loop in [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), the [history](https://docs.cycling74.com/reference/gen_dsp_history/ "gen_dsp_history") operator can be used. This represents a single-sample delay (a Z−1Z-1Z−1 operation). Thus the inlet to the [history](https://docs.cycling74.com/reference/gen_dsp_history/ "gen_dsp_history") operator will set the outlet value for the next sample (put another way, the outlet value of the [history](https://docs.cycling74.com/reference/gen_dsp_history/ "gen_dsp_history") operator is the inlet value from the previous sample). Multiple [history](https://docs.cycling74.com/reference/gen_dsp_history/ "gen_dsp_history") operators can be chained to create Z−2Z-2Z−2, Z−3Z-3Z−3 delays, but for longer and more flexible delay operators, use the [delay](https://docs.cycling74.com/reference/gen_dsp_delay/ "gen_dsp_delay") operator.
![](https://docs.cycling74.com/images/3f4e740fd9a637399f03ecf20c44756b_522.webp)
You can use the History operator as an object or in codebox.
A history operator in a Gen patcher can also be named, making it available for external control, just like a [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") parameter.
## Delay
The [delay](https://docs.cycling74.com/reference/gen_dsp_delay/ "gen_dsp_delay") operator delays a signal by a certain amount of time, specified in samples. The maximum delay time is specified as an argument to the [delay](https://docs.cycling74.com/reference/gen_dsp_delay/ "gen_dsp_delay") object. You can also have a multi-tap delay by specifying the number of taps in the second argument. Each tap will have an inlet to set the delay time, and a corresponding outlet for the delayed signal.
The [delay](https://docs.cycling74.com/reference/gen_dsp_delay/ "gen_dsp_delay") operator can be used for feedback loops, like the history operator, if the `@feedback` attribute is set to 1 (the default). The `@interp` attribute specifies which kind of interpolation is used:
  * **none** or **step** : No interpolation.
  * **linear** : Linear interpolation.
  * **cosine** : Cosine interpolation.
  * **cubic** : Cubic interpolation.
  * **spline** : Catmull-Rom spline interpolation.


## Data and Buffer
For more complex persistent storage of audio (or any numeric) data, [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") offers two objects: [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") and [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer"), which are in some ways similar to MSP’s [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object. A [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") object has a local name, which is used by various operators in the Gen patcher to read and write the [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") contents, or get its properties.
![](https://docs.cycling74.com/images/474543e9936bcb7e8baca91f42ecbbb0_456.webp)
Reading the contents of a [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") can be done using the [peek](https://docs.cycling74.com/reference/gen_dsp_peek/ "gen_dsp_peek"), [lookup](https://docs.cycling74.com/reference/gen_dsp_lookup/ "gen_dsp_lookup"), [wave](https://docs.cycling74.com/reference/gen_dsp_wave/ "gen_dsp_wave"), [sample](https://docs.cycling74.com/reference/gen_dsp_sample/ "gen_dsp_sample") or [nearest](https://docs.cycling74.com/reference/gen_dsp_nearest/ "gen_dsp_nearest") operators. The first argument for all of these operators is the local name of a [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer"). They all support single- or multi-channel reading (the second argument specifies the number of channels, and the last inlet the channel offset, where zero is the default).
All of these operators are essentially the same, differing only in defaults of their attributes. The attributes are:
  * **index** specifies the meaning of the first inlet:
  * **samples** : The first inlet is a sample index into the [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer").
  * **phase** : Maps the range 0..1 to the whole [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") contents.
  * **lookup** or **signal** : Maps the range -1..1 to the whole [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") contents, like the MSP [lookup~](https://docs.cycling74.com/reference/lookup~/ "lookup~") object.
  * **wave** : Adds extra inlets for start/end (in samples), driven by a phase signal between these boundaries (0..1, similar to MSP’s [wave~](https://docs.cycling74.com/reference/wave~/ "wave~") object). `@boundmode` specifies what to do if the index is out of range:
  * **ignore** : Indices out of bounds are ignored (return zero).
  * **wrap** : Indices out of bounds repeat at the opposite boundary.
  * **fold** or **mirror** : Indices wrap with palindrome behavior.
  * **clip** or **clamp** : Indices out of bounds use the value at the bound. `@channelmode` specifies what to do if the channel is out of range. It has the same options as the `@boundmode` attribute.
  * **interp** specifies what kind of interpolation is used:
    * **none** or **step** : No interpolation.
    * **linear** : Linear interpolation.
    * **cosine** : Cosine interpolation.
    * **cubic** : Cubic interpolation.
    * **spline** : Catmull-Rom spline interpolation.

Operator | Defaults  
---|---  
[nearest](https://docs.cycling74.com/reference/gen_dsp_nearest/ "gen_dsp_nearest") | `@index phase @interp none @boundmode ignore @channelmode ignore`  
[sample](https://docs.cycling74.com/reference/gen_dsp_sample/ "gen_dsp_sample") | `@index phase @interp linear @boundmode ignore @channelmode ignore`  
[peek](https://docs.cycling74.com/reference/gen_dsp_peek/ "gen_dsp_peek") | `@index samples @interp none @boundmode ignore @channelmode ignore`  
[lookup](https://docs.cycling74.com/reference/gen_dsp_lookup/ "gen_dsp_lookup") | `@index lookup @interp linear @boundmode clamp @channelmode clamp  
[wave](https://docs.cycling74.com/reference/gen_dsp_wave/ "gen_dsp_wave") | `@index wave @interp linear @boundmode wrap @channelmode clamp`  
Accessing the spatial properties of a [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") objects is done using the `dim` and `channels` operators (or the outlets of the [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") or [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") object itself), and writing is done using `poke` (non-interpolating replace) or `splat` (interpolating overdub).
Briefly, [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") should be thought of as a 64-bit buffer internal to the [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") patcher, even though it can be copied to, and [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") should be thought of as an object which can read and write external [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") data. The full differences between [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") and [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") are:
  * A [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") object is local to the Gen patcher, and cannot be read outside of it. On the other hand, a [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") object is a shared reference to an external MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object. Modifying the contents in a Gen buffer is directly modifying the contents of the MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object it references.
  * The [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") object takes three arguments to set its local name, its length (in samples) and number of channels. The [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") object takes an argument to set its local name, and an optional argument to specify the name of an MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object to reference (instead of using the local name).
  * Setting the [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") attribute corresponding to a named [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") object copies in values from the corresponding MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), while for a named [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") object it changes the MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") referenced. The [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") object always has the size of the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object it references (which may change). The [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") object has the size of its initial definition, or the size of the [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object which was copied to it (whichever is smaller).
  * The [data](https://docs.cycling74.com/reference/gen_dsp_data/ "gen_dsp_data") object always uses 64-bit doubles, while the [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") object converts from the bit resolution of the MSP [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object (currently 32-bit floats) for all read and write operations, and may be less efficient.


## Event-rate Gen
The [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") object also has an event-rate version, called [gen](https://docs.cycling74.com/reference/gen/ "gen"). Internally, the event-rate [gen](https://docs.cycling74.com/reference/gen/ "gen") object supports all of the same operators as [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"). The only difference is that [gen](https://docs.cycling74.com/reference/gen/ "gen") is an event-rate object, and is not part of the audio graph. Like most event-rate objects, the first inlet to [gen](https://docs.cycling74.com/reference/gen/ "gen") is hot, and will trigger computation. However, you can also use the `@interval` attribute in conjunction with the `@active` attribute to enable an internal metronome, which will trigger computation at a consistent rate. When using the event-rate [gen](https://docs.cycling74.com/reference/gen/ "gen") object, the [samplerate](https://docs.cycling74.com/reference/gen_dsp_samplerate/) operator will return 1000@interval\frac{1000}{@interval}@interval1000​, and the [vectorsize](https://docs.cycling74.com/reference/gen_dsp_vectorsize/) operator will always return 1.
## Technical notes
All operations in [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") use 64-bit doubles.
The compilation process for [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") Gen patchers and GenExprs includes an optimization that takes into account the update rate of each operator, so that any calculations that do not need to occur at sample rate (such as arithmetic on the outputs of param operators) instead process at a slower rate (determined by the host patcher vector size) for efficiency.
## Jitter Gen Objects
There are three Gen objects in Jitter: [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"). The [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") and [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") objects process Jitter matrices similar to [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr"). The [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") object processes textures and matrices just like [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab"). The [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") object is a generic matrix processing object that can handle matrices with any planecount, type and dimension. [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"), on the other hand, are specifically designed for working with pixel data. They can handle data of any type, but it must be two dimensional or less and have at most four planes.
## Jitter Operators
### Coordinates
Jitter Gen patchers describe the processing kernel for each cell in a matrix or texture. As the kernel is processing the input matrices, a set of coordinates is generated describing the location of the current cell being processed. The objects are just like the operators in [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr"). They are [norm](https://docs.cycling74.com/reference/gen_jit_norm/ "gen_jit_norm"), [snorm](https://docs.cycling74.com/reference/gen_jit_snorm/ "gen_jit_snorm"), and [cell](https://docs.cycling74.com/reference/gen_jit_cell/ "gen_jit_cell"), with the [dim](https://docs.cycling74.com/reference/gen_jit_dim/ "gen_jit_dim") operator giving the dimensions of the input matrix.
  * [norm](https://docs.cycling74.com/reference/gen_jit_norm/ "gen_jit_norm") ranges from `[0, 1]` across all matrix dimensions and is defined as _norm = cell/dim_.
  * [snorm](https://docs.cycling74.com/reference/gen_jit_snorm/ "gen_jit_snorm") ranges from `[-1, 1]` across all matrix dimensions and is defined as _snorm = cell/dim*2-1_.
  * [cell](https://docs.cycling74.com/reference/gen_jit_cell/ "gen_jit_cell") gives the current cell index.


### Vectors
Since Jitter matrices represent arrays of vector (more than one plane) data, all Gen operators in Jitter can process vectors of any size, so Gen patchers once created work equally on any vector size. The basic binary operators `+`, `-`, `*`, `/`, and `%` can take vector arguments as in `[+ 0.5 0.25 0.15]`, which will create an addition operator adding a vector with the three components to its input. Also, the [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") operator can take vector default values as in `[param 1 2 3 4]`. Parameters can have up to 32 values in [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") and 4 values in [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix").
The [vec](https://docs.cycling74.com/reference/gen_jit_vec/ "gen_jit_vec") operator creates vector constants and packs values together in a vector. It takes default arguments for its components and casts all of its inputs to scalar values before packing them together.
![](https://docs.cycling74.com/images/cb8fd477ccec2aa34a95ee9cd14a9182_461.webp)
You can use the vec operator as an object or in a codebox
The `swiz` operator applies a swizzle operation to vectors. In GLSL and similar shading languages, vector components can be accessed by indexing the vector with named planes. For example in GLSL you might see
```
red = color.r

```

or
```
redalpha = color.ra

```

or even
```
val = color.rbbg

```

![](https://docs.cycling74.com/images/ce2b206ab007d8da7a289a915de85d90_475.webp)
Use the swiz operator as an object to pick certain planes. In a codebox, do swizzling with a dot operator.
This type of operation is referred to as _swizzling_. The [swiz](https://docs.cycling74.com/reference/gen_jit_swiz/ "gen_jit_swiz") operator can take named arguments using the letters `r`, `g`, `b`, `a`, as well as `x`, `y`, `z`, `w` in addition to numeric indices starting at `0`. The letters are convenient for vectors with four or less planes, but for larger vectors numeric indices must be used. The compilation process automatically checks any swiz operation so arguments indexing components larger than the vector being processed will be clamped to the size of the vector.
![](https://docs.cycling74.com/images/c5e354b101eb273abb822374a7bc3374_280.webp)
Out of bounds swiz operations will be clamped
In addition, there are the basic vector operations for spatial calculations. These are [length](https://docs.cycling74.com/reference/gen_jit_length/ "gen_jit_length"), [normalize](https://docs.cycling74.com/reference/gen_jit_normalize/ "gen_jit_normalize"), [cross](https://docs.cycling74.com/reference/gen_jit_cross/ "gen_jit_cross"), [dot](https://docs.cycling74.com/reference/gen_jit_dot/ "gen_jit_dot"), and [reflect](https://docs.cycling74.com/reference/gen_jit_reflect/ "gen_jit_reflect").
### Sampling
Sampling operators are one of the most powerful features of Jitter Gen patchers. Sampling operators take an input and a coordinate in the range `[0, 1]` as an argument, returning the data at the coordinate’s position in the matrix or texture. The first argument always has to be a Gen patcher input while the second argument is an N-dimensional vector whose size is equal to the dimensionality of the input it is processing. If the coordinate argument is outside of the range `[0, 1]`, it will be converted to a value within the range `[0, 1]` according to its boundmode function. Possible boundmodes are `wrap`, `mirror`, and `clamp`, where `wrap` is the default.
![](https://docs.cycling74.com/images/c8bd0a4f0221ca5358f68c0a2e4537e8_624.webp)
You can use the sample operator as an object or in codebox.
The two sampling operators in Jitter Gen patchers are [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") and [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest"). The [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") operator samples values form a matrix using N-dimensional linear interpolation. The [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest") operator will simply grab the value from the closest cell.
### Geometry
Jitter Gen patchers include a suite of objects for generating surfaces. These include most of the shapes available in the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object. Each surface function returns two values: the vertex position and the vertex normal. The geometry operators are [sphere](https://docs.cycling74.com/reference/gen_jit_sphere/ "gen_jit_sphere"), [torus](https://docs.cycling74.com/reference/gen_jit_torus/ "gen_jit_torus"), [circle](https://docs.cycling74.com/reference/gen_jit_circle/ "gen_jit_circle"), [plane](https://docs.cycling74.com/reference/gen_jit_plane/ "gen_jit_plane"), [cone](https://docs.cycling74.com/reference/gen_jit_cone/ "gen_jit_cone"), and [cylinder](https://docs.cycling74.com/reference/gen_jit_cylinder/ "gen_jit_cylinder").
### Color
There are two color operators in Jitter Gen patchers. They are [rgb2hsl](https://docs.cycling74.com/reference/gen_jit_rgb2hsl/ "gen_jit_rgb2hsl") and [hsl2rgb](https://docs.cycling74.com/reference/gen_jit_hsl2rgb/ "gen_jit_hsl2rgb"). These convert between the Red Green Blue color space and the Hue Saturation Luminance color space. If the input to these objects has an alpha component, the alpha will be passed through untouched.
## jit.gen
The [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") object is a general purpose matrix processing object. It compiles Gen patchers into native machine code representing the kernel of an N-dimensional matrix processing routine. It follows the Jitter matrix planemapping conventions for pixel data with planes [0-4] as the ARGB channels.
[jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") can have any number of inlets and outlets, but the matrix format for the different inputs and outputs is always linked. In other words, the matrix format (planecount, type, dimensions) of the first inlet determines the matrix format for all other inputs and outputs. [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") makes use of parallel processing just like other parallel aware objects in Jitter for maximum performance with large matrices.
How a matrix is processed by [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen") is dependent on the input planecount, type, and dimension of the input matrices. In addition, there is a `@precision` attribute that sets the type of the processing kernel. The default value for precision is `auto`. Auto precision automatically adapts the type of the kernel dependent upon the matrix input type. In `auto` mode, the following mapping between input matrix type and kernel processing type is used:
  * **char** maps to fixed
  * **long** maps to float64
  * **float32** maps to float32
  * **float64** maps to float64


Other possible values for the precision attribute are `fixed`, `float32`, and `float64`. Fixed precision is the only setting that doesn’t correspond to a Jitter matrix type. Fixed precision specifies a kernel type that performs a type of floating point calculation with integers using a technique called fixed-point arithmetic. It’s very fast and provides more precision than 8-bit char operations without incurring the cost of converting to a true floating-point type. However, fixed-point arithmetic calculations have more error that can sometimes be visible when using the sampling operators. If there are noticeable artifacts, simply increase the internal precision to `float32`.
## jit.pix
The [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") object is a matrix processing object specifically for pixel data. When processing matrices representing video and images, [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") is the best object. Internally, data is in RGBA format always. If the input has less than four planes, [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") will convert it to RGBA format according to the following rules:
  * 1-plane, Luminance format, L to LLL1 (Luminance for RGB and 1 for Alpha)
  * 2-plane Lumalpha format, LA to LLLA (Luminance for RGB and Alpha for Alpha)
  * 3-plane RGB format, RGB to RGB1 (RGB for RGB and 1 for Alpha)
  * 4-plane, ARGB format, ARGB to RGBA (changes the order of the channels internally)


The output of [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") is always a 4-plane matrix in ARGB format, which is the standard Jitter pixel planemapping. Like [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") compiles Gen patchers into C++ and makes use of Jitter’s parallel processing system. [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") also has a precision attribute that operates exactly the same was as it does in [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen").
## jit.gl.pix
The [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") object is a matrix and texture processing object specifically for pixel data that operates just like [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab"). The only difference between the two is that [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") compiles its patcher into GLSL while [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") reads it from a shader file. Like [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") uses an internal RGBA pixel format.
## Technical notes (Jitter Gen)
### **Numerical Values in the Kernel**
All numerical values in Jitter Gen patches are conceptually floating point values. This is the case even for fixed precision kernels. It is particularly important to remember this when dealing with char matrices. All char matrices are converted to the range `[0, 1]` internally. On output, this range is mapped back out to `[0, 255]` in the char type. A char value of 1 is equivalent to the floating point value of 1/2551/2551/255.
When using the comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`), it's particularly important to keep in mind the floating point nature of Gen patcher internal values because of their inherent imprecision. Instead of directly testing for equality for example , it's more effective to test for whther a value falls within a certain small range (epsilon). In the example below, the `absdiff` operator calculates how far a value is from 1/255 and then the `<` op tests to see if it's within the threshold of error.
![](https://docs.cycling74.com/images/2f8a081fdb9d8e1a54abbe23f9b593cc_387.webp)
Rather than testing for equivalence, test whether values are within some epsilon distance of a target value.
### jit.pix vs. jit.gl.pix
For the most part [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") will behave identically despite one being CPU-oriented and the other GPU-oriented. The differences have to do with differences in behavior between how matrix inputs are handled with [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") and how texture inputs are handled with [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix").
All of the inputs to [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") will adapt in size, type, and dimension to the left-most input. As a result, all input matrices within a [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") processing kernel will have the same values for the cell and dim operators. In [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"), inputs can have different sizes. In [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"), the values for the cell and dim operators are calculated from the properties of the left-most input (_in1_). A future version may include per-input cell and dim operators, but for now this is not the case.
Since the sampling operators take normalized coordinates in the range `[0, 1]`, differently sized input textures will still be properly sampled using the norm operator since its value is independent of varying input sizes. However, in [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") the [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") and [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest") operators behave differently than with [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"). How a texture is sampled is determined by the properties of the texture. As a consequence, sample and nearest behave the same in [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"). To enable nearest sampling, set the `@filter` attribute to nearest. For linear interpolation, set `@filter` to linear (the default).
## See Also
  * [mc_gen](https://docs.cycling74.com/userguide/mc/mc_gen/)


