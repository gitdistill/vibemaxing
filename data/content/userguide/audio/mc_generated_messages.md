---
description: The MC Wrapper lets you treat all the objects within it as a space that can be changed globally with a single message
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_generated_messages/
title: Generating Values for All MC Wrapper Instances
---

# Generating Values for All MC Wrapper Instances
The MC Wrapper lets you treat all the objects within it as a "space" that can be changed globally with a single message. Here are some approaches using built-in wrapper functions. You can also generate your own control schemes using the lower-level `@applyvalues` message.
## Generating Random Values
To generate a random space of values for all wrapper instances, use the `deviate` message. The first argument to the message is the "width" of the deviation. The second argument is the center value. Here is an example of changing the frequency of all oscillators in an [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~") object. As the slider value is increased, the range of values ("width") increases. When the slider is set to 0, values generated will be 440 because the width is 0.
![](https://docs.cycling74.com/images/2958a20c947aa1be7ba8dcee801a930c_224.webp)
Optionally, you can specify an attribute or message that will be used instead of a float or int. Here is `deviate` applied to the `@cutoff` attribute of the [lores~](https://docs.cycling74.com/reference/lores~/ "lores~") object. It may help to think of the syntax of wrapper generation messages as follows: the first argument is the operating parameter (how, for example, `deviate` will do its job), and everything that follows is the message that it will use to change the value of an instance.
![](https://docs.cycling74.com/images/0fb94adcb80c4190d37bceb8ebf070ae_307.webp)
## Generating a Range of Values
To set instances within the wrapper to a range of values, use the `spread` message. This message follows the same syntactical pattern as the `deviate` message. The first argument is the beginning of the range to generate, and the second argument is the end of the range. If the end is above the beginning, the first wrapper will receive the lowest value. If it's negative, the first instance will receive the highest value. The `spread` message has three variants that specify how the range is calculated. `spreadinclusive` includes both the first and second values in the range. `spreadexclusive` exclusives both the first and second values from the range. And `spreadincludesecond` includes the second value but not the first. By convention `spread` is the same as `spreadincludfirst`; it includes the first value but not the second value. The following examples show the differences in these variations:
![](https://docs.cycling74.com/images/a616dadac15e81f4408f029b02cf55d3_719.webp)
## Generating an Exponential Series
To generate an exponentially increasing or decreating series of values applied to all instances in the wrapper, use the `exponential` or `scaledexponential` messages. The first argument is the value of the exponent in the series and the second argument is the base that is raised to the exponent. Negative exponents cause values to increase over the series while positive exponents cause values to approach zero. The `scaledexponential` variant divides values in the series by the number of instances in the wrapper, resulting in an overall range that is independent of the number of instances.
## Generating a Harmonic Series
To generate a harmonic series of values applied to all instances in the wrapper, use the `harmonic` and `subharmonic` messages. Each message assigns the first instance in the wrapper to the first harmonic (or subharmonic), which is given by the second argument (the fundamental frequency) and subsequent harmonics or subharmonics to successive wrapper instances.
The first argument is a multiplier on the harmonic calculations, typically this is set to 1 for a harmonic series. As an example, here are the first harmonics and subharmonics for 500:
![](https://docs.cycling74.com/images/5b8ea0644dca09487458b85879d612a5_262.webp)
## Your Own Generating Algorithm
In addition to the built-in MC Wrapper messages, you can define your own algorithms to control a space of channels:
  * Javascript can produce an list of values to be used with the `applyvalues` message
  * the [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") object can calculate distinct per-channel values with the **mc_channel** operator
  * the [mc.generate~](https://docs.cycling74.com/reference/mc.generate~ "mc.generate~") object can generate and update values for objects in the MC Wrapper at signal rate


