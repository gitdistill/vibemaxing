---
description: Outline of various complexities when working with pattr in Max for Live
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_pattr/
title: Using {pattr} in Live Devices
---

# Using [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") in Live Devices
Live-specific user interface objects such as [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") save their state within Live documents and presets. If you want to use standard Max objects and have them interact with Live, you will have to enable the [Parameter Mode Enable](https://docs.cycling74.com/reference/pattr/#attr_parameter_enable) attribute in the [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object. This ensures that the data internal to [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") is also stored (and recalled) using Live's document.
## Enabling Parameter Mode
  * Select a [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object and click the [Inspector](https://docs.cycling74.com/userguide/inspector/) button in the Patcher toolbar to show the object's
  * Click the Parameter tab at the top of the inspector window to show the Parameter attributes.
  * Check the Parameter Mode Enable checkbox.

![](https://docs.cycling74.com/images/f06f191fdb151c1ac8c029d67934f09c_938.webp)
##  [autopattr](https://docs.cycling74.com/reference/autopattr/ "autopattr") Considerations
The [autopattr](https://docs.cycling74.com/reference/autopattr/ "autopattr") object provides an easy to way manage the state of standard Max objects, but it will not work with the parameter system, so objects that are attached to an [autopattr](https://docs.cycling74.com/reference/autopattr/ "autopattr") will not be seen by Live. If you want a pattr parameter to appear for modulation etc, you will need to add a [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object for each instance.
## Differences Between Max and Max for Live
Although the [pattr objects](https://docs.cycling74.com/learn/articles/pattrchapter01/) can be used in the context of Max for Live, there are some differences when compared to Max. You can read more about various limitations [here](https://docs.cycling74.com/userguide/m4l/live_limitations/). To better understand [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") we encourage you to visit the [pattr guide](https://docs.cycling74.com/userguide/pattr/).
