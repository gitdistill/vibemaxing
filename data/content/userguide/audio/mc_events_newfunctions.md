---
description: MC objects make list events, with one element for each channel
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_events_newfunctions/
title: Processing Events from MC Objects
---

# Processing Events from MC Objects
## Events and MC Values
It is often useful to obtain values from an audio signal and use them in event-level processing. With standard MSP signals, you can use the [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") object to get an instantaneous value from an audio signal at a regular interval.
![](https://docs.cycling74.com/images/bc2bb815f05f9bf1a5a4f167296822b1_117.webp)
In the case of multi-channel signals, things are more complex: at each measurement, you would get a list with a value for each input channel. Instead of producing a list, the [mc.snapshot~](https://docs.cycling74.com/reference/mc.snapshot~ "mc.snapshot~") object has an additional outlet that provides a **voice number**.
At each sampling interval, [mc.snapshot~](https://docs.cycling74.com/reference/mc.snapshot~ "mc.snapshot~") outputs each of the values from each of the incoming samples, but outputs the voice number before the signal value. This combination of values can be used with a routing object (like [mc.route](https://docs.cycling74.com/reference/mc.route "mc.route")) to send each value to a unique location. Alternatively, if you do want a list of all the snapshot values, [mc.makelist](https://docs.cycling74.com/reference/mc.makelist "mc.makelist") can do that for you.
![](https://docs.cycling74.com/images/edaa045ee7d642e0f32f77f49e44f01d_332.webp)
## Voice outputs from poly~ and mc.poly~
Similar to the [mc.snapshot~](https://docs.cycling74.com/reference/mc.snapshot~ "mc.snapshot~") object, both [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") and [mc.poly~](https://docs.cycling74.com/reference/mc.poly~ "mc.poly~") may have an additional voice output. This is only created when contained in a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") contains an event (non-signal) outlet.
![](https://docs.cycling74.com/images/1632c8bc79c04e4f8332f5570eadce0b_218.webp)
You can use the voice output, along with a routing object such as [mc.route](https://docs.cycling74.com/reference/mc.route "mc.route") to use the event output to control other parts of your patch.
![](https://docs.cycling74.com/images/cdf46324d080da0bc83e2bddf3959fcf_278.webp)
## See Also
[MC Event-Based Objects](https://docs.cycling74.com/userguide/mc/mc_events_newobjects/)
