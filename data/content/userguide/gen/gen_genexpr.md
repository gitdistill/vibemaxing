---
description: Documentation for GenExpr, the expression language used by Gen and inside of Gen codebox
group: Gen
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/gen/gen_genexpr/
title: GenExpr
---

# GenExpr
GenExpr is the internal language used by Gen patchers. It is used to describe computations in an implementation agnostic manner. To perform actual computations, it is translated into machine code for the CPU or GPU by the various Gen objects ( [gen](https://docs.cycling74.com/reference/gen/ "gen"), [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), etc.). The GenExpr language can be used directly in Gen patchers with the [expr](https://docs.cycling74.com/reference/gen_common_expr/ "gen_common_expr") and [codebox](https://docs.cycling74.com/reference/gen_common_codebox/ "gen_common_codebox") objects. These objects analyze the expressions written in them and automatically construct the the appropriate number of inlets and outlets so that patchcords can be connected to the computations described within.
Note that there is absolutely no difference in terms of performance between describing computations with object boxes and the GenExpr language. When a Gen patcher is compiled, it all gets merged into a single representation, so use the approach that is most convenient for the problem.
![](https://docs.cycling74.com/images/e9665a3edd0fc6da53b7fda5d347be0e_250.webp)
## The Gen Patcher and the codebox Object
The GenExpr language is designed to complement the Max patching environment within Gen patchers. It provides a parallel textual mechanism for describing computations to be used in concert with the graphical patching paradigm of Max. As one example, the structural elements of user-defined GenExpr functions correspond closely to the structural elements of Max objects with their notions of inlets, outlets, arguments and attributes. Furthermore, the GenExpr language has keywords `in`, `in1`, `in2`, … and `out`, `out1`, `out2`, … that specifically refer to the inlets and outlets of the [expr](https://docs.cycling74.com/reference/gen_common_expr/ "gen_common_expr") or [codebox](https://docs.cycling74.com/reference/gen_common_codebox/ "gen_common_codebox") the GenExpr code is embedded in.
## Language Basics
The GenExpr language resembles C and JavaScript for simple expression statements; however, semicolons are only necessary when there are multiple statements. The codeboxes below all contain valid expressions in GenExpr. When there is a single expression with no assignment like in the far left codebox, the assignment to out1 is implied. Notice that it also doesn’t have a semicolon at the end. When there is only one statement, the semicolon is also implied.
![](https://docs.cycling74.com/images/e152866176e7fbda11e922ba14413016_645.webp)
For multi-line statements however, semicolons are required. The [codebox](https://docs.cycling74.com/reference/codebox/ "codebox") on the left doesn’t have them and will generate errors. The codebox on the right is correct.
![](https://docs.cycling74.com/images/252d59286f6181ab03ffed7b05e68fc7_666.webp)
The [expr](https://docs.cycling74.com/reference/gen_common_expr/ "gen_common_expr") operator is functionally the same as a [codebox](https://docs.cycling74.com/reference/gen_common_codebox/ "gen_common_codebox") but lacks the text editor features such as syntax highlighting and multi-line text display and navigation. [expr](https://docs.cycling74.com/reference/gen_common_expr/ "gen_common_expr") is most useful for short, one-line expressions, saving the effort of patching together a sequence of objects together that operate as a unit.
![](https://docs.cycling74.com/images/a5451892fc937c3bf12bedccfb059eac_452.webp)
An [expr](https://docs.cycling74.com/reference/gen_common_expr/ "gen_common_expr") or [codebox](https://docs.cycling74.com/reference/gen_common_codebox/ "gen_common_codebox") determines its number of inlets and outlets by detecting the `inN` and `outN` keywords where `N` is the inlet/outlet position. `in1` and `out1` are the left-most inlet and outlet respectively. For convenience, the keywords `in` and `out` are equivalent to `in1` and `out1` respectively.
Almost every object that can be created in a Gen patcher is also available from within GenExpr as either a function, a global variable, a declaration, or a constant. The number of inlets an object has corresponds to the number of arguments a function takes. For example, the object [atan2](https://docs.cycling74.com/reference/gen_common_atan2/ "gen_common_atan2") has two inlets and takes two arguments as follows:
```
out  = atan2( in1 ,  in2 )

```

## Parameters
Parameters declared in GenExpr behave just like [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") operators in a patch. They can only be declared in the main body of GenExpr code where inlets and outlets (_inN_ and _outN_) exist because they operate at the same level as object box Gen operators in the patcher.
![](https://docs.cycling74.com/images/a93529d1e4e9cc69b25431bb9122f595_340.webp)
A [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") declaration in GenExpr names a parameter and creates it if necessary. If there is a [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") object box with the same name as a [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") declared in GenExpr, the GenExpr [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") will simply alias the object box [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param"). If there isn't a [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") object box with the same name, one will be implicitly created. In the code above, offset aliases the object box [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") offset, while amp creates a new global [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param").
## Comments
Comments in GenExpr follow the C style syntax for both single-line and multi-line comments. Single-line comments start withand multi-line comments are defined by.
```
// this is a comment, below we sample an input 
pix = sample( in1 , norm);

```

## Multiple Return Values
Just as object boxes can have multiple inlets and outlets, function in GenExpr can take multiple arguments and can return multiple values. The object [cartopol](https://docs.cycling74.com/reference/gen_common_cartopol/ "gen_common_cartopol") has two inlets and two outlets. Similarly, in GenExpr the [cartopol](https://docs.cycling74.com/reference/gen_common_cartopol/ "gen_common_cartopol") function takes two arguments and returns two values. In code, this looks like r, theta = cartopol(x, y). Functions that return mutiple values can assign to a list of variables. The syntax follows the pattern:
```
var1, var2, var3, … = <expression>

```

When a function returns multiple values but assigns to only one value, the unused return values are simply ignored. When a return value is ignored, the GenExpr compiler eliminates any unnecessary calculations. The function [cartopol](https://docs.cycling74.com/reference/gen_common_cartopol/ "gen_common_cartopol") could be expanded out to
```
r, theta = sqrt(x*x+y*y), atan2(y, x)

```

If we remove theta and have instead
```
r = sqrt(x*x+y*y), atan2(y, x)

```

the compiler simplifies it to
```
r = sqrt(x*x+y*y)

```

In the reverse case where we only use theta, the Gen compiler will strip out the calculations for r
```
notused, theta = sqrt(x*x+y*y), atan2(y, x);
 out  = theta;

```

effectively becomes
```
theta = atan2(y, x);
 out  = theta;

```

Even for more complex examples where the outputs share intermediate calculations, the compiler eliminates unnecessary operations, so there is no performance penalty for not using all of a function’s return values.
Just as the left-hand side list of variable names being assigned to are separated by commas, the right-hand side list of expressions can also be separated by commas:
```
sum, diff = in1 + in2, in1 - in2 
out1, out2  = diff, sum

```

If there are more values on the left-hand side than on the right-hand side, the extra variable names are given a value of zero. For example,
```
out1, out2  =  in1

```

becomes
```
out1, out2  =  in1, 0

```

If any of the expressions in the right-hand side return more than one value, these additional values will be ignored unless the expression is the last item in the right-hand side list. This is complex to describe, but should be clear from these examples:
**Unused Return Values** The second return value gets discarded and cartopol is optimized:
```
r = cartopol(x, y)

```

**Extra Assignment Values** Zeros are assigned to extra assignment values:
```
x, y =  in1

```

becomes
```
x, y =  in1 ,  0

```

**Multiple Return Values in an Expression List** Only the last expression can return multiple values. cartopol’s second return value discarded, as it is not the last expression in the right-hand side:
```
r,  out1  = cartopol(x, y),  in1

```

Here cartopol returns both values, since it is in the last position:
```
out1 , r, theta =  in1 , cartopol(x, y)

```

The same principle applies when expressions are used as arguments to a function call. In this example, the two output values of poltocar connect to the two input values of min:
```
out  = min(poltocar( in1 ,  in2 ))

```

## Defining GenExpr Functions
Defining new functions in GenExpr happens in much the same way as other familiar programming languages. Since there are no types in GenExpr function arguments are specified simply with a name. A basic function definition with an equivalent patcher representation looks like the following. Note that functions must be declared **before** all statements:
![](https://docs.cycling74.com/images/1b5b532d25b880b5d5722e8b31ff8441_384.webp)
A function returning multiple values looks like:
![](https://docs.cycling74.com/images/7333f2cad5ae933396c91bdf3fd664ad_559.webp)
The cylinder operator in Jitter Gen objects is defined as:
![](https://docs.cycling74.com/images/88b1f311c2d218811cf5ea45d3f15462_690.webp)
While simple functions in GenExpr can be easily patched together, more involved functions like the above cylinder definition start to become unwieldy, especially if the function is used several times within the GenExpr code. This is the advantage of textual representations.
## Operator Attributes
![](https://docs.cycling74.com/images/369362087511f592b38a7ba78c38c4e8_637.webp)
In Gen patchers, some objects have attributes like the Jitter Gen operator [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample"), which as a `boundmode` attribute. In GenExpr, function arguments correspond to operator inlets and function return values correspond to outlets. Attributes are set using a key/value style argument. For example:
```
out  = sample( in , norm, boundmode= "mirror" );

```

will use a version of the [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") operator with a mirroring boundary behavior. The attribute is set with boundmode as the _key_ and "mirror" as its _value_. Since the concept of Max messages doesn't exist within Gen patchers, attributes for built-in operators are not dynamically modifiable. This holds equally in GenExpr. Such attribute values must be constants. If the attribute takes a numerical value, it cannot be assigned to from a variable.
### Attributes in Function Definitions
Attributes can also be defined for function definitions. Here, attributes can be dynamic, behaving in a similar manner to how [setparam](https://docs.cycling74.com/reference/gen_common_setparam/ "gen_common_setparam") interacts with subpatcher parameters. Attributes can be defined in one of two ways. With one syntax, the attribute is defined and given a default in the function signature. With the other, a [Param](https://docs.cycling74.com/userguide/gen_common_param/ "gen_common_param") object is declared in the function, adding the name of the parameter as an attribute to the function.
![](https://docs.cycling74.com/images/c3cf34fe69444d257a2878cc7aa23f25_754.webp)
With the first method, only the default value of the attribute can be defined. With the second method, other properties such as minimum and maximum values for the attribute can be set. By declaring a [param](https://docs.cycling74.com/reference/gen_common_param/ "gen_common_param") object, you get more control over how the attribute operates.
![](https://docs.cycling74.com/images/d9751451127aac2ab9e9119ac5402e2e_868.webp)
As with built-in operators, attributes of function definitions can be set with key-value syntax. In the above example, the `amp` attribute is given a value of 0.5 while the `offset` attribute is given a value of `in1 * 2`, which is an expression that is not constant but valid because `func` is a function definition. Note, however, that the `offset` attribute has minimum and maximum values defined, so any expression assigned to it will be clamped to that range.
## Abstractions as GenExpr Functions
Structurally, GenExpr functions are equivalent to Gen patchers. Both can have inputs, outputs and named parameters. In GenExpr, Gen patchers save as abstractions (.gendsp or .genjit files) can be used as functions. When the GenExpr interpreter encounters a function it can't find the definition of, it will use the current Max search paths to look for a Gen abstraction with the name of the function.
```
out1  = myAbstraction( in1 )

```

There is no definition of the function myAbstraction in the above code and it isn't a built-in operator, so Max will try to find a Gen abstraction with that name. The GenExpr interpreter will look for `myAbstraction.gendsp` in the case of [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") or `myAbstraction.genjit` in the case of the Jitter Gen objects [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), or [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix").
There are some caveats with using abstractions as GenExpr functions. GenExpr function names must be valid identifiers. An identifier in GenExpr is a sequence of characters starting with a letter or an underscore (`[a-z]`, `[A-Z]`, `_`) followed by any number of letters, numbers or underscores (`[a-z]`, `[A-Z]`, `[0-9]`, `_`). It is not uncommon for Max subpatchers to have other chartacters such as `~` or `.` in them. These are invalid characters when it comes to GenExpr function names, so if they're used in the name of a Gen abstraction, they cannot be used as GenExpr functions.
## Requiring GenExpr Files
When defining operators in GenExpr, it can be handy to keep them in a separate file so that they can be reused frequently without having to constantly re-type the operator definition in a codebox. To include GenExpr operators defined in a separate file, use the `require` operator. The `require` operator takes the name of a `.genexpr` file and loads its definitions. The following are all valid ways to require a `.genexpr` file:
```
require( "mylib" )
require( "mylib" );
require "mylib" 
require "mylib" ;

```

In the above code, calling `require` triggers the codebox to look for the file 'mylib.genexpr' using the Max [search path](https://docs.cycling74.com/userguide/search_path/). Required `.genexpr` files can also require other files. If a file is required more than once, it will only be loaded once.
GenExpr files can be created and edited using the built-in Max text editor. If a GenExpr file is required in a gen object and the file is edited and saved, the Gen object will detect that a file it depends on has changed through filewatching and recompile itself to reflect the new changes.
## Branching and Looping
Branching and looping is supported in GenExpr with `if/else`, `for` and `while` constructs. `if` statements can be chained together using `else if` an arbitrary number of times such that different blocks of code will be executed depending on different conditions. For example:
```
if (in  >  0.5) {
  out = cos(in * pi);
}
else if (in  >  0.25) {
  out  = sin( in *pi);
}
else {
  out  = cos(in * pi) * sin(in * pi);
}

```

Note that in the Jitter gen objects, `if` statements with vector-valued conditions will only use the first element of the vector to determine whether a block of code should be tested or not. `while` loops in GenExpr are similar to those in many other languages:
```
i = 0;
val = 0;
while (i < 10) {
  i += 1;
  // accumulate 
  val += i;
}
out  = val;

```

`for` loops are also similar to this in many other languages although there is no `++` operator in GenExpr to increment a loop counter. Instead, += can be used:
```
val = 0 ;
 for (i= 0; i <  10; i += 1) {
   // accumulate 
  val += i;
}
out  = val;

```

Since GenExpr is compiled on-the-fly, it can be easy to make a programming mistake and create an infinite loop. All of the gen objects have protections against infinite loops, so while an infinite loop might slow things down, it won't cause Max to get stuck and freeze.
Also, note that in many cases values in GenExpr are floating point, even loop counters. Floating point numbers can't exactly represent every number, sometimes a little fudge factor to account for this might be necessary. For example, this loop:
```
val = 0;
for (i = 0; i <= 1; i += 0.05) {
  // accumulate 
  val += i;
}
out = val;

```

will likely not reach 1.0 despite the `<=` operator because of floating point precision. Instead, write something like:
```
val = 0;
for (i = 0 ; i <= 1.04 ; i +=  0.05) {
  // accumulate 
  val += i;
}
out  = val;

```

to ensure that the `i` variable goes all the way to 1.
### Continue and Break
With looping constructs, GenExpr supports `break` and `continue` statements. `break` causes an early exit from a loop while `continue` causes the loop to start the next iteration without finishing the current one.
```
val = 0;
for (i = 0 ; i < 10; i += 1) {
  if (val > 20) {
    // bail early 
    break;
  }
  val += i;
}
out = val;

```
```
val = 0 ;
for (i = 0 ;i <  10; i +=  1) {
  if (val ==  6) {
    // skip an iteration 
    continue;
  }
  val += i;
}
out  = val;

```

## GenExpr and Jitter Inputs
Jitter Gen objects take both Jitter matrices ([jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix")) and/or textures ([jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture")) depending on the object. Within the Gen patcher the operator `in` represents both the input matrix or texture in its entirety _and_ the current cell of that input being processed. In most cases, the `in` operator represents the current cell being processed. The only time where it represents the entire input is with the [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") and [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest") operators. Only an `in` operator can be connected to the left input of [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") and [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest"), which are used to grab data from arbitrary locations within the input. The same holds true when [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") and [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest") are used in GenExpr.
![](https://docs.cycling74.com/images/8aee3e87d66a0bc2222b12d256285536_418.webp)
When GenExpr code is compiled, the inputs to [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") and [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest") are validated to ensure that their first arguments are actually Gen patcher inputs and an error thrown if this isn't the case. The validation process can track inputs even through function calls so [sample](https://docs.cycling74.com/reference/gen_jit_sample/ "gen_jit_sample") and [nearest](https://docs.cycling74.com/reference/gen_jit_nearest/ "gen_jit_nearest") can be used within functions without issue.
## GenExpr and Jitter Coordinate Operations
The coordinate operations in Jitter Gen patchers ([norm](https://docs.cycling74.com/reference/gen_jit_norm/ "gen_jit_norm"), [snorm](https://docs.cycling74.com/reference/gen_jit_snorm/ "gen_jit_snorm"), [cell](https://docs.cycling74.com/reference/gen_jit_cell/ "gen_jit_cell"), and [dim](https://docs.cycling74.com/reference/gen_jit_dim/ "gen_jit_dim")) are special-case operators that are a hybrid betwen operator and global variable. There are two equally valid syntaxes for using these operators:
```
out1  = norm * dim();

```

In the first instance above, [norm](https://docs.cycling74.com/reference/gen_jit_norm/ "gen_jit_norm") is syntactically a global variable while [dim](https://docs.cycling74.com/reference/gen_jit_dim/ "gen_jit_dim") is syntactically a function call. All of the coordinate operators follow this convention.
## Technical Notes
GenExpr is a type-less language. Variables are given types automatically by the compiler depending on the Gen domain and the Gen object’s inputs. Gen variables are also local-to-scope by default so they don’t have to be declared with a keyword like var as in JavaScript. Note that GenExpr has no array notation `[index]` as there is currently no notion of an array structure.
