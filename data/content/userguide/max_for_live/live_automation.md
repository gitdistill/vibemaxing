---
description: Automation and how to access automation data in Max for Live
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_automation/
title: Automation
---

# Automation
Parameters of a device whose `Parameter Visibility` attribute is set to Automated and Stored are available in Live's automation editor (visible in the Arrangement view). The automation editor permits you to draw curves or other control information that will change parameter values automatically as the arrangement plays. The parameter data type determines the type of automation editor shown. More on this topic soon. Another way parameter values can be changed automatically is by using clip envelopes to modulate parameter values. While automation sets the absolute value of a parameter, modulation adjusts the value up or down from its current value.
## Modulating a Max for Live Device Parameter
  * Click on a Max for Live user interface object to select it and click on the Inspector icon in the toolbar to show the Inspector.
  * If you have not already done so, choose Int or Float from the `Type` attribute's pull-down menu to set the parameter type.
  * Choose the modulation mode you want to use from the `Clip Modulation Mode` attribute's pull-down menu to set the parameter.
  * In the Live application, select the parameter, choose a modulation source, and enable modulation as you would with any normal Live device parameter.


## Parameter Automation Data at Audio Rates
While getting parameter automation data from the Live application at message rates for use in your Max for Live device is common, some devices require that you receive parameter automation data from the Live applcation at higher and more accurate rates. Any Max for Live device can receive its parameter automation data in the form of a sample-accurate audio-rate ramp using the [live.param~](https://docs.cycling74.com/reference/live.param~ "live.param~") object.
The [live.param~](https://docs.cycling74.com/reference/live.param~ "live.param~") object takes as an argument the name of an automatable parameter to which it is bound. Any change to the automatable parameter's output value will be send out the outlet of the [live.param~](https://docs.cycling74.com/reference/live.param~ "live.param~") object at signal rate.
![](https://docs.cycling74.com/images/5e4b135ace6f2bb1d4e047f4989aa81e_318.webp)
## See Also
  * [Parameters](https://docs.cycling74.com/userguide/m4l/live_parameters/)
  * [Pattr](https://docs.cycling74.com/userguide/m4l/live_pattr/)


