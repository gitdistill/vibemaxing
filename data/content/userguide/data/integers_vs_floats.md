---
description: Knowing the difference between integers and floats is important to working with Max.
group: Data
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/integers_vs_floats/
title: Integers and Floats
---

# Integers and Floats
Max is fairly strict about how it deals with integer and floating point numbers. At a low level, integers and floats are two of the fundamental data types that objects can pass between each other, and many objects will handle the two data types differently.
## Integers and Floats in Max
Integers are whole numbers, while floats can represent values with a decimal component. In Max, many objects operate in either a "floating point mode" or an "integer mode". This is a common source of bugs, since integer-mode objects will convert from float to int before processing, discarding any values after the decimal point.
![A message box containing a 5, connected to a division object with the argument 4, connected to an integer numbox and a floating point numbox.](https://docs.cycling74.com/images/0620ae34caa7dd38c7ce836edcafa043_168.webp)
In this classic example, the result of the division `5 / 4` is computed as `1.25`, but displays as `1` in an integer numbox. This is the expected behavior, but sometimes it can be subtle when an object is in integer-mode.
![A message box containing a 5, connected two division objects. The first divides by 4 without a decimal, while the second divides by 4., including the decimal. Two floating point numboxes compare the result.](https://docs.cycling74.com/images/eb7de94bcc3f08cad378cab2f15814d7_166.webp)
The object containing a `/`, defining a division operation, can operate either in "integer mode" or "floating-point mode" depending on whether the argument has a decimal or not. As you can see, the integer-mode object will truncate any decimal component.
![An integer box containing a 500, connected to a scale object with the arguments '0 1000 0 1'. The scale is connected to a floating point box containing '0.'. The top integer box is connected to another scale object with arguments '0 1000 0 1.', and that scale object is connected to a floating point numbox containing '0.5'."](https://docs.cycling74.com/images/619dbb6ff21b4c6ec016018f602299a9_237.webp)
The [scale](https://docs.cycling74.com/reference/scale/ "scale") object behaves similarly—so long as all of the arguments are integers, the object will be in "integer mode", and the output will be truncated to an integer value. The [scale](https://docs.cycling74.com/reference/scale/ "scale") object on the left demonstrates this behavior. However, if any of the arguments to [scale](https://docs.cycling74.com/reference/scale/ "scale") contains a decimal, then the object will be in "floating point mode", and the output will be a float, even if the input is an integer.
![A floating point numbox containing '4.5', connected to a trigger object with the arguments 'f i', connected to two floating point numboxes, containing 4.5 and 4"](https://docs.cycling74.com/images/b3adc91e4aefaa17c1298d81d80d3de9_173.webp)
Some objects, like [pack](https://docs.cycling74.com/reference/pack/ "pack"), [pak](https://docs.cycling74.com/reference/pak/ "pak"), and [trigger](https://docs.cycling74.com/reference/trigger/ "trigger"), can be configured to cast their inputs to floats or integers. A [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object with the arguments `f` and `i`, as pictured, will cast its input to a float for the leftmost outlet, and to an integer for the rightmost. As you can see, the floating point box on the right displays the truncated value.
Lastly, it's worth mentioning the [typeroute](https://docs.cycling74.com/reference/typeroute/ "typeroute") object, which can route messages by their type, separating out integers from floats.
A handful of other objects, in particular objects to do with simple math operations, will exhibit special behavior for integers and floats. When in doubt, check the help files and object reference documentation for more information.
## Technical Details
In Max, integers are whole numbers. All integers are 64-bit, so the smallest integer that can pass between objects is -9,223,372,036,854,775,808, and the largest is 9,223,372,036,854,775,807. Floating point numbers in Max are also 64-bit (double precision). Messages can contain positive or negative numbers with a magnitude as large as 1030810^{308}10308, or as small as 10−30810^{-308}10−308. Unlike integers, floating point numbers are not evenly spaced. There are as many floating point numbers between 0 and 1 as there are between 1 and 1030810^{308}10308. This may or may not be spiritually significant.
## Gen + RNBO
Unlike Max, Gen and RNBO do not use integers for any internal computation. If you really want Max-style integer math, for example truncating the result of a division operation, then you're best off using the [trunc](https://docs.cycling74.com/reference/gen_common_trunc/ "gen_common_trunc") object for Gen, and the [trunc](https://docs.cycling74.com/reference/rnbo_trunc/ "rnbo_trunc") object for RNBO.
