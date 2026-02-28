---
description: Create algorithms for controlling objects in the MC wrapper for mc.gen
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_gen_event_wrapper/
title: Using mc.gen with the MC Wrapper
---

# Using [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") with the MC Wrapper
The MC Wrapper contains a [set of messages](https://docs.cycling74.com/userguide/mc/mc_messages_to_wrapper/) that offer high-level algorithmic control over a set of individual objects. For example, using the `deviate` message with changing values for ranges you can generate and apply a set of random values for signal object parameters such as oscillator frequency.
For more possibilities than those offered by the basic wrapper messages, the [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") object offers a way to create algorithms for controlling objects in the wrapper. As an example, we will show an example using the `@expr` mode of Gen to create a simple range.
_(Note: This feature is already available as the`spread` message to the wrapper but it illustrates a basic pattern you can customize.)_
##  [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") Connections
The [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") object is not an audio object; it accepts and produces only Max messages. However, [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") uses the MC Wrapper; it contains multiple [gen](https://docs.cycling74.com/reference/gen/ "gen") objects. Specify the number inputs using the @chans attribute.
Since [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") uses the MC Wrapper, you can connect an audio signal to one of its inputs and it will auto-adapt its channel count. (We will use this trick in our complete example below.)
The [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") object contains an extra rightmost outlet that outputs a voice number immediately before any values come out its other outlets. This permits identification of the [gen](https://docs.cycling74.com/reference/gen/ "gen") instance that is sending output. The [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target"), [mc.route](https://docs.cycling74.com/reference/mc.route "mc.route"), and [mc.makelist](https://docs.cycling74.com/reference/mc.makelist "mc.makelist") objects make it simple to use voice outlet for further isolation of [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") output.
## Using MC Operators
To generate a range of control values, one for each wrapper instance, we will need to use the MC-specific [mc_channel](https://docs.cycling74.com/reference/mc_channel/ "mc_channel") and [mc_channelcount](https://docs.cycling74.com/reference/mc_channelcount/ "mc_channelcount") operators in our Gen expression. A formula for generating the range is:
`out_channel = min + (max - min) * (channel  / number_of_channels)`
This will scale a range evenly over a space defined by min and max. We will use `in1` as our range minimum and `in2` as our range maximum. As a Gen expression, this would be:
`out1 = in1 + (in2 - in1) \* (mc_channel / mc_channelcount)`
![](https://docs.cycling74.com/images/5e36f59df9578b773eef111ada69887a_461.webp)
## Target Connections
Now we want to use the rightmost **voice** outlet of [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") in conjunction with [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target") to control an object in the MC Wrapper. In this example, we will control the frequencies of a bank of sawtooth oscillators in [mc.saw~](https://docs.cycling74.com/reference/mc.saw~ "mc.saw~").
![](https://docs.cycling74.com/images/73d0565ee5d5d1f985650ceda5a57526_483.webp)
By connecting the rightmost outlet of [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") to [mc.target](https://docs.cycling74.com/reference/mc.target "mc.target"), the per-voice range value is properly routed to the correct [saw~](https://docs.cycling74.com/reference/saw~/ "saw~") instance inside [mc.saw~](https://docs.cycling74.com/reference/mc.saw~ "mc.saw~").
