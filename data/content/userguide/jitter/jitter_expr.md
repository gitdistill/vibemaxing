---
description: The Jitter expression language, used by the jit.expr object to define per-pixel calculations.
group: Jitter
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/jitter/jitter_expr/
title: Jitter expr
---

# Jitter expr
This document describes the Jitter expression language syntax. This is the language used for the [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") object, as well as the `exprfill` message to a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") objects. This expression will be evaluated once for each cell in the input, in order to generate an output matrix with the same matrix dimensions as the input.
You could make a [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") that passes through input unchanged.
```
jit.expr @expr in[0]

```

Or you could use an expression to add the first and second inputs together:
```
jit.expr @expr in[0] + in[1]

```

Or do something more sophisticated, like apply a vignette mask:
```
jit.expr @expr (1-hypot(snorm[0],snorm[1]))*in[0]*2.

```

## Inputs
Reference the inputs to the expr object with `in`. Get the first input with `in[0]`, the second with `in[1]`, and so on. Use `p` to get a specific plane of the input, where `in[0].p[0]` accesses the first plane of the first input, `in[0].p[1]` gets the second plane of the first input, and so on.
The [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") object defaults to two inputs, but you can increase the number of inputs with the `@inputs` attribute.
To get the cell coordinates, use either `cell`, `norm`, or `snorm`. The index is used to select the dimension, so `cell[0]` is the cell coordinate in the x direction (first dimension), `cell[1]` is the cell coordinate in the y direction, and so on. You can also use `dim` to get the dimensions of the matrix in any direction.
Finally, it's also possible to access any named matrix by simply using the name of that matrix instead of `in`. With a matrix named `my_matrix`, use `my_matrix` to access the contents of that matrix at the current cell coordinates, or `my_matrix.p[0]` to access the first plane of that matrix.
Name | Description  
---|---  
in[0-31] | Input matrix cell contents, corresponding plane  
in[0-31].p[0-31] | Input matrix cell contents, specific plane  
cell[0-31] | Cell coordinates of the current cell  
norm[0-31] | Normalized (0 to 1) cell coordinates  
snorm[0-31] | Signed normalized (-1 to 1) cell coordinates  
dim[0-31] | Matrix dimension size  
matrixname[0-31] | Named matrix cell contents, corresponding plane  
matrixname[0-31].p[0-31] | Named matrix cell contents, specific plane  
## Functions and Operators
Within a Jitter expression, Jitter operators can be applied as functions. For the most part, these are the same operators as are defined for the `jit.op` object. Some of these can be applied as infix operators, for example `in[0] + in[1]` for the `+` operator. Others are called as functions, with commas between arguments, like `absdiff(in[0], in[1])`.
Instead of the Jitter operators `>p` and `<p`, use the function calls `gtp(val, test)` and `ltp(val, test)`.
### Arithmetic
Name | Description  
---|---  
`pass` | pass left input, no operator  
`*` | multiplication (also `mult`)  
`/` | division (also `div`)  
`+` | addition (also `add`)  
`-` | subtraction (also `sub`)  
`+m` | addition modulo (char only) (also `addm`)  
`-m` | subtraction modulo (char only) (also `subm`)  
`%` | modulo (also `mod`)  
`min` | minimum  
`max` | maximum  
`abs` | absolute value (unary)  
`avg` | average  
`absdiff` | absolute value of difference  
`fold` | folding/mirrored modulo (float only)  
`wrap` | wrapping/positive modulo (float only)  
`!pass` | pass right input, no operator  
`!/` | right input divided by left input (flipped)  
`!-` | right input minus left input (flipped)  
`!%` | right input modulo left input (flipped)  
`ignore` | leave previous output value  
### Trigonometric
(float32/float64 only, unary except atan2)
Name | Description  
---|---  
`sin` | sine  
`cos` | cosine  
`tan` | tangent  
`asin` | arcsine  
`acos` | arccosine  
`atan` | arctangent  
`atan2` | arctangent (binary)  
`sinh` | hyperbolic sine  
`cosh` | hyperbolic cosine  
`tanh` | hyperbolic tangent  
`asinh` | hyperbolic arcsine  
`acosh` | hyperbolic arccosine  
`atanh` | hyperbolic arctangent  
### Bitwise
(long/char only)
Name | Description  
---|---  
`&` | bitwise and  
`|` | bitwise or  
`^` | bitwise xor  
`~` | bitwise compliment (unary)  
`>>` | right shift  
`<<` | left shift  
### Logical
Name | Description  
---|---  
`&&` | logical and  
`||` | logical or  
`!` | logical not (unary)  
`>` | greater than  
`<` | less than  
`>=` | greater than or equal to  
`<=` | less than or equal to  
`==` | equal  
`!=` | not equal  
`>p` | greater than (pass)  
`<p` | less than (pass)  
`>=p` | greater than or equal to (pass)  
`<=p` | less than or equal to (pass)  
`==p` | equal (pass)  
`!=p` | not equal (pass)  
### Exponential/Logarithmic/Other
(float32/float64 only, unary except hypot and pow)
Name | Description  
---|---  
`exp` | e to the x  
`exp2` | 2 to the x  
`ln` | log base e  
`log2` | log base 2  
`log10` | log base 10  
`hypot` | hypotenuse (binary)  
`pow` | x to the y (binary)  
`sqrt` | square root  
`ceil` | integer ceiling  
`floor` | integer floor  
`round` | round to nearest integer  
`trunc` | truncate to integer  
## Matrix Operators
Many Jitter **Matrix Operators** can be used inside of a Jitter expression as well. These are the functional equivalent of Jitter objects like `jit.clip`, objects that perform a simple operation on their matrix inputs. There is no exhaustive list of these, but if there's a simple Jitter object that you'd like to use in an expression, chances are it will work. You could use the following expression to convolve two matrices.
```
jit.expr @expr "jit.convolve(in[0], in[1])"

```

If the Jitter matrix operator can be configured with attributes, those can be supplied as an attribute list following the other arguments to the matrix operator. The following would constrain the values in each plane to be between 0.2 and 0.8.
```
jit.expr @expr "jit.clip(in[0], @min 0.2 @max 0.8)"

```

## Basis Function Generators
The basis function generators from the [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg") object can also be used inside of an expression. These work in much the same way as [matrix operators](https://docs.cycling74.com/userguide/jitter/jitter_expr/#matrix-operators).
```
jit.expr @expr "noise.gradient(norm[0]*2, norm[1]*2, @seed 313)"

```

### Distance functions
Name | Description  
---|---  
distance.chebychev | Absolute maximum difference between two points  
distance.euclidean | True straight line distance in Euclidean space  
distance.euclidean.squared | Squared Euclidean distance  
distance.manhattan | Rectilinear distance measured along axes at right angles  
distance.manhattan.radial | Manhattan distance with radius fall-off control  
distance.minkovsky | Exponentially controlled distance  
### Filter functions
Name | Description  
---|---  
filter.box | Sums all samples in the filter area with equal weight  
filter.gaussian | Weights samples in the filter area using a bell curve  
filter.lanczossinc | Weights samples using a steep windowed sinc curve  
filter.mitchell | Weights samples using a controllable cubic polynomial  
filter.disk | Sums all samples inside the filter's radius with equal weight  
filter.sinc | Weights samples using an un-windowed sinc curve  
filter.catmullrom | Weights samples using a Catmull-Rom cubic polynomial  
filter.bessel | Weights samples with a linear phase response  
filter.triangle | Weights samples in the filter area using a pyramid  
### Transfer functions
Name | Descrpition  
---|---  
transfer.step | Always 0 if value is less than threshold, otherwise always 1  
transfer.smoothstep | Step function with cubic smoothing at boundaries  
transfer.bias | Polynomial similar to gamma but remapped to unit interval  
transfer.cubic | Generic 3rd order polynomial with controllable coefficients  
transfer.saw | Periodic triangle pulse train  
transfer.quintic | Generic 5th order polynomial with controllable coefficients  
transfer.gain | S-Shaped polynomial evaluated inside unit interval  
transfer.pulse | Periodic step function  
transfer.smoothpulse | Periodic step function with cubic smoothing at boundaries  
transfer.sine | Periodic sinusoidal curve  
transfer.linear | Linear function across unit interval  
transfer.solarize | Scales given value if threshold is exceeded  
### Noise functions
Name | Description  
---|---  
noise.cellnoise | Coherent blocky noise  
noise.checker | Periodic checker squares  
noise.value.cubicspline | Polynomial smoothed pseudo-random values  
noise.value.convolution | Convolution filtered pseudo-random values  
noise.sparse.convolution | Convolution filtered pseudo-random feature points  
noise.gradient | Directionally weighted polynomially interpolated values  
noise.simplex | Simplex weighted pseudo-random values  
noise.voronoi | Distance weighted pseudo-random feature points  
noise.distorted | Domain distorted combinational noise  
### Fractal functions
Name | Description  
---|---  
mono | Additive fractal with global simularity across scales  
multi | Multiplicative fractal with varying simularity across scales  
multi.hybrid | A hybrid additive and multiplicative fractal  
multi.hetero | Heterogenous multiplicative fractal  
multi.ridged | Multiplicative fractal with sharp ridges  
turbulence | Additive mono-fractal with sharp ridges  
## Constants
There's also a handful of constants ready as well. An expression like `in[0] * DEGTORAD` would convert a matrix full of degrees to a matrix full of radians.
Name | Description  
---|---  
PI | Ratio of a circle's circumference to its diameter  
TWOPI | Twice the value of pi  
HALFPI | Half the value of pi  
INVPI | One over pi  
DEGTORAD | Scale factor to convert degrees to radians  
RADTODEG | Scale factor to convert radians to degrees  
E | Base of the natural logarithm  
LN2 | Natural logarithm evaluated for 2  
LN10 | Natural logarithm evaluated for 10  
LOG10E | Log base 10 evaluated for e  
LOG2E | Log base 2 evaluated for e  
SQRT2 | Square root of 2  
SQRT1_2 | One over the square root of 2
