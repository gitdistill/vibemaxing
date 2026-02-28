---
description: List of Gen operators shared between DSP Gen and Jitter Gen
group: Gen
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/gen/gen_common_operators/
title: Gen Common Operators
---

# Gen Common Operators
The following Gen operators are common to all of Max's Gen family of objects. They can be used as operators in the [gen](https://docs.cycling74.com/reference/gen/ "gen"), [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") objects.
## Comparison
  * [!=p](https://docs.cycling74.com/reference/gen_common_neqp/), [neqp](https://docs.cycling74.com/reference/gen_common_neqp/) : Returns in1 if it does not equal in2, else returns zero. Equivalent to in1 * (in1 != in2)
  * [>](https://docs.cycling74.com/reference/gen_common_gt/), [gt](https://docs.cycling74.com/reference/gen_common_gt/) : Returns 1 if in1 is greater than in2, else returns zero.
  * [==](https://docs.cycling74.com/reference/gen_common_eq/), [eq](https://docs.cycling74.com/reference/gen_common_eq/) : Returns 1 if in1 equals in2, else returns zero.
  * [==p](https://docs.cycling74.com/reference/gen_common_eqp/), [eqp](https://docs.cycling74.com/reference/gen_common_eqp/) : Returns in1 if it equals in2, else returns zero. Equivalent to in1 * (in1 == in2).
  * [>=](https://docs.cycling74.com/reference/gen_common_gte/), [gte](https://docs.cycling74.com/reference/gen_common_gte/) : Returns 1 if in1 is equal to or greater than in2, else returns zero.
  * [>=p](https://docs.cycling74.com/reference/gen_common_gtep/), [gtep](https://docs.cycling74.com/reference/gen_common_gtep/) : Returns in1 if in1 is equal to or greater than in2, else returns zero. Equivalent to in1 * (in1 >= in2).
  * [>p](https://docs.cycling74.com/reference/gen_common_gtp/), [gtp](https://docs.cycling74.com/reference/gen_common_gtp/) : Returns in1 if in1 is greater than in2, else returns zero. Equivalent to in1 * (in1 > in2).
  * [<](https://docs.cycling74.com/reference/gen_common_lt/), [lt](https://docs.cycling74.com/reference/gen_common_lt/) : Returns 1 if in1 is less than than in2, else returns zero.
  * [<=](https://docs.cycling74.com/reference/gen_common_lte/), [lte](https://docs.cycling74.com/reference/gen_common_lte/) : Returns 1 if in1 is equal to or less than in2, else returns zero.
  * [<=p](https://docs.cycling74.com/reference/gen_common_ltep/), [ltep](https://docs.cycling74.com/reference/gen_common_ltep/) : Returns in1 if in1 is equal to or less than in2, else returns zero. Equivalent to in1 * (in1 <= in2).
  * [<p](https://docs.cycling74.com/reference/gen_common_ltp/), [ltp](https://docs.cycling74.com/reference/gen_common_ltp/) : Returns in1 if in1 is less than in2, else returns zero. Equivalent to in1 * (in1 < in2).
  * [max](https://docs.cycling74.com/reference/gen_common_max/), [maximum](https://docs.cycling74.com/reference/gen_common_max/) : The maximum of the inputs
  * [min](https://docs.cycling74.com/reference/gen_common_min/), [minimum](https://docs.cycling74.com/reference/gen_common_min/) : The minimum of the inputs
  * [!=](https://docs.cycling74.com/reference/gen_common_neq/), [neq](https://docs.cycling74.com/reference/gen_common_neq/) : Returns 1 if in1 does not equal in2, else returns zero.
  * [step](https://docs.cycling74.com/reference/gen_common_step/) : Akin to the GLSL step operator: 0 is returned if in1 < in2, and 1 is returned otherwise.


## Constant
  * [constant](https://docs.cycling74.com/reference/gen_common_constant/) : A constant value
  * [degtorad](https://docs.cycling74.com/reference/gen_common_degtorad/), [DEGTORAD](https://docs.cycling74.com/reference/gen_common_degtorad/) : Multiplicative constant to convert degrees to radians
  * [e](https://docs.cycling74.com/reference/gen_common_e/), [E](https://docs.cycling74.com/reference/gen_common_e/) : Base of the natural logarithm
  * [f](https://docs.cycling74.com/reference/gen_common_float/), [float](https://docs.cycling74.com/reference/gen_common_float/) : Either outputs a constant float or converts its input value to a float
  * [halfpi](https://docs.cycling74.com/reference/gen_common_halfpi/), [HALFPI](https://docs.cycling74.com/reference/gen_common_float/) : One half of the constant pi
  * [i](https://docs.cycling74.com/reference/gen_common_int/), [int](https://docs.cycling74.com/reference/gen_common_int/) : Either outputs a constant integer or converts its input value to an integer.
  * [invpi](https://docs.cycling74.com/reference/gen_common_invpi/), [INVPI](https://docs.cycling74.com/reference/gen_common_invpi/) : One over pi
  * [ln10](https://docs.cycling74.com/reference/gen_common_ln10/), [LN10](https://docs.cycling74.com/reference/gen_common_ln10/) : The natural log of 10
  * [ln2](https://docs.cycling74.com/reference/gen_common_ln2/), [LN2](https://docs.cycling74.com/reference/gen_common_ln2/) : The natural log of 2
  * [log10e](https://docs.cycling74.com/reference/gen_common_log10e/), [LOG10E](https://docs.cycling74.com/reference/gen_common_log10e/) : Log base 10 of the constant e
  * [log2e](https://docs.cycling74.com/reference/gen_common_log2e/), [LOG2E](https://docs.cycling74.com/reference/gen_common_log2e/) : Log base 2 of the constant e
  * [PHI](https://docs.cycling74.com/reference/gen_common_phi/), [phi](https://docs.cycling74.com/reference/gen_common_phi/) : 1+sqrt(5)2\frac{1 + sqrt(5)}{2}21+sqrt(5)​, the "golden" ratio
  * [pi](https://docs.cycling74.com/reference/gen_common_pi/), [PI](https://docs.cycling74.com/reference/gen_common_pi/) : The constant pi, the ratio of a circle's circumference to its diameter
  * [radtodeg](https://docs.cycling74.com/reference/gen_common_radtodeg/), [RADTODEG](https://docs.cycling74.com/reference/gen_common_radtodeg/) : Multiplicative constant to convert radians to degrees
  * [sqrt1_2](https://docs.cycling74.com/reference/gen_common_sqrt1_2/), [SQRT1_2](https://docs.cycling74.com/reference/gen_common_sqrt1_2/) : One over the square root of 2
  * [sqrt2](https://docs.cycling74.com/reference/gen_common_sqrt2/), [SQRT2](https://docs.cycling74.com/reference/gen_common_sqrt2/) : The square root of 2
  * [twopi](https://docs.cycling74.com/reference/gen_common_twopi/), [TWOPI](https://docs.cycling74.com/reference/gen_common_twopi/) : Two times pi


## Declare
  * [param](https://docs.cycling74.com/reference/gen_common_param/), [Param](https://docs.cycling74.com/reference/gen_common_param/) : Named parameters can be modified from outside the gen patcher. The first argument specifies the name of the parameter, the second argument the initial value.


## Expression
  * [expr](https://docs.cycling74.com/reference/gen_common_expr/) : Evaluates GenExpr code. Standard mathematical operators (+, -, *, / etc.) and gen patcher operators can be used. See the [GenExpr](https://docs.cycling74.com/userguide/gen/gen_genexpr/) documentation for more detail.


## Ignore
  * [pass](https://docs.cycling74.com/reference/gen_common_pass/) : Passes the value through unchanged.


## Input-output
  * [in](https://docs.cycling74.com/reference/gen_common_in/) : Defines an input for a gen patcher.
  * [out](https://docs.cycling74.com/reference/gen_common_out/) : Send output from a gen patcher


## Logic
  * [!](https://docs.cycling74.com/reference/gen_common_not/), [not](https://docs.cycling74.com/reference/gen_common_not/) : An input value of zero returns 1, any other value returns zero.
  * [&&](https://docs.cycling74.com/reference/gen_common_and/), [and](https://docs.cycling74.com/reference/gen_common_and/) : Returns 1 if both in1 and in2 are nonzero.
  * [bool](https://docs.cycling74.com/reference/gen_common_bool/) : Converts any nonzero value to 1 while zero passes through.
  * [or](https://docs.cycling74.com/reference/gen_common_or/), [||](https://docs.cycling74.com/reference/gen_common_or/) : Returns 1 if either in1 or in2 are nonzero.
  * [^^](https://docs.cycling74.com/reference/gen_common_xor/), [xor](https://docs.cycling74.com/reference/gen_common_xor/) : Returns 1 if one of in1 and in2 are nonzero, but not both.


## Math
  * [!%](https://docs.cycling74.com/reference/gen_common_rmod/), [rmod](https://docs.cycling74.com/reference/gen_common_rmod/) : Reverse modulo (remainder of second input / first input)
  * [!-](https://docs.cycling74.com/reference/gen_common_rsub/), [rsub](https://docs.cycling74.com/reference/gen_common_rsub/) : Reverse subtraction (subtract first input from second)
  * [%](https://docs.cycling74.com/reference/gen_common_mod/), [mod](https://docs.cycling74.com/reference/gen_common_mod/) : Modulo inputs (remainder of first input / second input)
  * [+](https://docs.cycling74.com/reference/gen_common_add/), [add](https://docs.cycling74.com/reference/gen_common_add/) : Add inputs
  * [-](https://docs.cycling74.com/reference/gen_common_sub/), [sub](https://docs.cycling74.com/reference/gen_common_sub/) : Subtract inputs
  * [/](https://docs.cycling74.com/reference/gen_common_div/), [div](https://docs.cycling74.com/reference/gen_common_div/) : Divide inputs
  * [absdiff](https://docs.cycling74.com/reference/gen_common_absdiff/) : Compute the absolute difference between two inputs using the equation abs(in1−in2)abs(in1-in2)abs(in1−in2).
  * [cartopol](https://docs.cycling74.com/reference/gen_common_cartopol/) : Convert Cartesian values to polar format. Angles are in radians.
  * [*](https://docs.cycling74.com/reference/gen_common_mul/), [mul](https://docs.cycling74.com/reference/gen_common_mul/) : Multiply inputs
  * [neg](https://docs.cycling74.com/reference/gen_common_neg/) : Negate input
  * [poltocar](https://docs.cycling74.com/reference/gen_common_poltocar/) : Convert polar values to Cartesian format. Angles are in radians.
  * [!/](https://docs.cycling74.com/reference/gen_common_rdiv/), [rdiv](https://docs.cycling74.com/reference/gen_common_rdiv/) : Reverse division (divide second input by first)


## Numeric
  * [abs](https://docs.cycling74.com/reference/gen_common_abs/) : Negative values will be converted to positive counterparts.
  * [ceil](https://docs.cycling74.com/reference/gen_common_ceil/) : Round the value up to the next higher integer
  * [floor](https://docs.cycling74.com/reference/gen_common_floor/), [trunc](https://docs.cycling74.com/reference/gen_common_trunc/) : Round the value down to the next lower integer (toward negative infinity)
  * [fract](https://docs.cycling74.com/reference/gen_common_fract/) : Return only the fractional component
  * [sign](https://docs.cycling74.com/reference/gen_common_sign/) : Positive input returns 1, negative input returns -1, zero returns itself.
  * [trunc](https://docs.cycling74.com/reference/gen_common_trunc/) : Round the value down to the next smaller integer (toward zero)


## Powers
  * [exp](https://docs.cycling74.com/reference/gen_common_exp/) : Raise the mathematical value e to a power
  * [exp2](https://docs.cycling74.com/reference/gen_common_exp2/) : Raise 2 to a power
  * [fastexp](https://docs.cycling74.com/reference/gen_common_fastexp/) : Approximated e to a power
  * [fastpow](https://docs.cycling74.com/reference/gen_common_fastpow/) : Approximated in1 to the power of in2
  * [ln](https://docs.cycling74.com/reference/gen_common_ln/), [log](https://docs.cycling74.com/reference/gen_common_log/) : The natural logarithm
  * [log10](https://docs.cycling74.com/reference/gen_common_log10/) : The logarithm base 10 of the input
  * [log2](https://docs.cycling74.com/reference/gen_common_log2/) : The logarithm base 2 of the input
  * [pow](https://docs.cycling74.com/reference/gen_common_pow/) : Raise in1 to the power of in2
  * [sqrt](https://docs.cycling74.com/reference/gen_common_sqrt/) : The square root of the input


## Range
  * [clamp](https://docs.cycling74.com/reference/gen_common_clamp/), [clip](https://docs.cycling74.com/reference/gen_common_clip/) : Clamps the input value between specified min and max. Ranges are inclusive (both min and max values may be output)
  * [fold](https://docs.cycling74.com/reference/gen_common_fold/) : Low and high values can be specified by arguments or by inlets. The default range is 0..1.
  * [scale](https://docs.cycling74.com/reference/gen_common_scale/) : Similar to the Max scale and MSP scale~ objects. Inputs are: 1) value to scale, 2) input lower bound, 3), input upper bound, 4) output lower bound, 5) output upper bound, 6) exponential curve. Default lower and upper bounds are zero and one; default exponential curve is 1 (linear). No bound clamping is performed. The high and low values can be reversed for inverted mapping.
  * [wrap](https://docs.cycling74.com/reference/gen_common_wrap/) : Low and high values can be specified by arguments or by inlets. The default range is 0..1.


## Route
  * [?](https://docs.cycling74.com/reference/gen_common_switch/), [switch](https://docs.cycling74.com/reference/gen_common_switch/) : Selects between the second and third inputs according to the boolean value of the first. If the first argument is true, the second argument will be output. Otherwise, the third argument will be output.
  * [gate](https://docs.cycling74.com/reference/gen_common_gate/) : Similar to the MSP gate~ object. It takes an argument for number of outputs (one is the default) and lets you choose which the incoming signal (at the right inlet) is sent to according to the (integer) value in the left inlet. A value of zero or less to the left inlet will choose no output; a value greater than the number of outlets will select the last outlet. Like gate~, un-selected outlets will send zero.
  * [mix](https://docs.cycling74.com/reference/gen_common_mix/) : Mixes (interpolates) between inputs a and b according to the value of the third input t, using linear interpolation. The factor (t) should vary between 0 (for a) and 1 (for b). If one argument is given, it specifies the mix (interpolation) factor.
  * [r](https://docs.cycling74.com/reference/gen_common_receive/), [receive](https://docs.cycling74.com/reference/gen_common_receive/) : Receive values from a named send. The send/receive pairs are only visible to each other within the same gen patcher. They will not send across gen patchers or sub-patchers.
  * [s](https://docs.cycling74.com/reference/gen_common_send/), [send](https://docs.cycling74.com/reference/gen_common_send/) : Send values to a named receive. The send/receive pairs are only visible to each other within the same gen patcher. They will not send across gen patchers or sub-patchers.
  * [selector](https://docs.cycling74.com/reference/gen_common_selector/) : Similar to the MSP selector~ object. In a Gen patcher it takes an argument for number of choices (one is the default). In GenExpr, the number of choices is determined by the number of arguments. The first input lets you choose which of the remaining inputs is sent to the output. A value of zero or less to the first input will result in a zero signal at the output; a value greater than the number of choices will select the last input.
  * [smoothstep](https://docs.cycling74.com/reference/gen_common_smoothstep/) : Smoothstep is a scalar interpolation function commonly used in computer graphics. The function interpolates smoothly between two input values based on a third one that should be between the first two. The returned value is clamped between 0 and 1. The slope (i.e. derivative) of the smoothstep function starts at 0 and ends at 0.


## Subpatcher
  * [gen](https://docs.cycling74.com/reference/gen_common_gen/) : Gen subpatcher or abstraction
  * [setparam](https://docs.cycling74.com/reference/gen_common_setparam/) : Set a param in a subpatcher from a parent patcher


## Trigonometry
  * [acos](https://docs.cycling74.com/reference/gen_common_acos/) : The arc cosine of the input (returns radians)
  * [acosh](https://docs.cycling74.com/reference/gen_common_acosh/) : The inverse hyperbolic cosine of the input
  * [asin](https://docs.cycling74.com/reference/gen_common_asin/) : The arc sine of the input (returns radians)
  * [asinh](https://docs.cycling74.com/reference/gen_common_asinh/) : The inverse hyperbolic sine of the input
  * [atan](https://docs.cycling74.com/reference/gen_common_atan/) : The arc tangent of the input (returns radians)
  * [atan2](https://docs.cycling74.com/reference/gen_common_atan2/) : Returns the angle to the coordinate (x,y) in radians.
  * [atanh](https://docs.cycling74.com/reference/gen_common_atanh/) : The inverse hyperbolic tangent of the input
  * [cos](https://docs.cycling74.com/reference/gen_common_cos/) : The cosine of the input (in radians)
  * [cosh](https://docs.cycling74.com/reference/gen_common_cosh/) : The hyperbolic cosine of the input
  * [degrees](https://docs.cycling74.com/reference/gen_common_degrees/) : convert radians to degrees
  * [fastcos](https://docs.cycling74.com/reference/gen_common_fastcos/) : The approximated cosine of the input (in radians)
  * [fastsin](https://docs.cycling74.com/reference/gen_common_fastsin/) : The approximated sine of the input (in radians)
  * [fasttan](https://docs.cycling74.com/reference/gen_common_fasttan/) : The approximated tangent of the input (in radians)
  * [hypot](https://docs.cycling74.com/reference/gen_common_hypot/) : Returns the length of the vector to (in1, in2).
  * [radians](https://docs.cycling74.com/reference/gen_common_radians/) : convert degrees to radians
  * [sin](https://docs.cycling74.com/reference/gen_common_sin/) : The sine of the input (in radians)
  * [sinh](https://docs.cycling74.com/reference/gen_common_sinh/) : The hyperbolic sine of the input
  * [tan](https://docs.cycling74.com/reference/gen_common_tan/) : The tangent of the input (in radians)
  * [tanh](https://docs.cycling74.com/reference/gen_common_tanh/) : The hyperbolic tangent of the input


## Waveform
  * [noise](https://docs.cycling74.com/reference/gen_common_noise/) : A random number generator


