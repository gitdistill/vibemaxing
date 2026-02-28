---
description: Use OpenSoundControl to control parameters in Max, and send OSC out of Max
group: Parameters
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/OSC/
title: OpenSoundControl (OSC)
---

# OpenSoundControl
With [OpenSoundControl](https://opensoundcontrol.stanford.edu) (OSC) support, Max can be controlled by any OSC-compatible device or application, and can also send OSC messages to control other OSC-enabled systems.
OSC can be enabled in Max in two ways:
  1. Through the built-in UDP server, which you can activate for the whole application in [Max's preferences](https://docs.cycling74.com/userguide/preferences_and_settings/), or for a specific patcher using the [patcher inspector](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector).
  2. By using the [param.osc](https://docs.cycling74.com/reference/param.osc "param.osc") object.


Once enabled, [**parameters**](https://docs.cycling74.com/userguide/parameter_mode/) are automatically given _OSC addresses_ , which have the following structure:
`/<patcher name>/param/<parameter name>/<attribute name>`
The different components that make up the address are configurable globally and locally in each patcher. Using these addresses, you can get and set the values of the following parameter attributes:
Parameter attribute | OSC address | Description  
---|---|---  
Long Name | `/longname` | The unique name of the parameter  
Short Name | `/shortname` | The short name used for display  
Scripting Name | `/scriptname` | The scripting name associated with the object that hosts the parameter  
Parameter Type | `/type` | The type of the parameter, one of `float`, `int`, `enum`, `blob`, `file`  
Visibility | `/visibility` | The parameter's visibility in the parameter system. Changing this value will not affect the visibility of this parameter to the OSC system. See the OSC Enable attribute.  
Minimum | `/min` | The parameter's minimum value, if it has one (i.e. if it's an `int`, `float`, or `enum`  
Maximum | `/max` | The parameter's maximum value, if it has one (i.e. if it's an `int`, `float`, or `enum`  
Exponent | `/exponent` | The parameter's exponent, if it has one (i.e. if it's an `int`, `float`, or `enum`  
Raw Value | `/raw` | The raw (scaled) value of the parameter. This address container is optional if the raw value is the only value present in the OSC bundle. See the OSC Value Mode attribute.  
Normalized Value | `/normalized` | The normalized (`[0,1]`) value of the parameter. This address container is optional if the raw value is the only value present in the OSC bundle. See the OSC Value Mode attribute.  
##  [osc.codebox](https://docs.cycling74.com/reference/osc.codebox "osc.codebox")
[osc.codebox](https://docs.cycling74.com/reference/osc.codebox "osc.codebox") can be used to display the contents of an OSC packet using JSON syntax. It's worth mentioning that OSC is a binary format--it has no human-readable form. The use of JSON syntax to represent OSC should be considered an approximation of the underlying binary data.
## OSCQuery
[OSCQuery](https://github.com/Vidvox/OSCQueryProposal) is a method of describing the capabilities of an OSC server. An http server can be configured to serve OSCQuery requests in Max by enabling OSCQuery in the general preferences.
Once enabled, an OSCQuery request can be generated with a URL like `http://localhost:30339`. All patchers with parameters exposed as OSC will be present in the OSCQuery response. Individual patchers can be excluded from the OSCQuery response using the option in the patcher inspector.
## The `FullPacket` Message
Objects that accept and produce OSC do so using a message called `FullPacket`. This message is passed with two arguments, and should be considered opaque, i.e. these arguments are not to be manipulated as normal max values.
An important property of the FullPacket message is that it is transient and **must not be stored** in objects like the message box, zl.reg, etc.
