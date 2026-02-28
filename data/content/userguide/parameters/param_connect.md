---
description: Automatically bind parameters to UI objects
group: Parameters
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/param_connect/
title: Connecting Parameters
---

# Connecting Parameters
You can include an object called _param_ in [Gen](https://docs.cycling74.com/reference/gen_param/) and [RNBO](https://docs.cycling74.com/reference/rnbo_param/) that declares a **parameter**. Gen and [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~") parameters can be changed as **attributes** of the object. If you wanted to link a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") to control a [gen~ parameter](https://docs.cycling74.com/reference/gen_param/) you would have to do the following:
  * copy the Gen parameter's min, max and default to the [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial")'s `parameter_range`, `parameter_inital`, and `parameter_initial_enable`.
  * use [getattr](https://docs.cycling74.com/reference/getattr/ "getattr") to listen to the value of the Gen parameter, then patch the [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") to [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") and [getattr](https://docs.cycling74.com/reference/getattr/ "getattr") using a `set` message to avoid creating a feedback loop and another message box to prepend the attribute name to the value of the dial

![](https://docs.cycling74.com/images/203fb913dd154ca6a5c2b44f374bf9d1_355.webp)
Note that you have to copy this patching for _every_ parameter you want to control.
The `param_connect` attribute of many Max UI objects (including [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial")) provides a way to handle all of this with one step, as demonstrated below. In this example, we will connect a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") to a parameter inside [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") called `xyz`.
![](https://docs.cycling74.com/images/d9a82dd6a8389642a754eb9d6591afc2_494.webp)
Once this connection is established, the [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") will control the `xyz` parameter inside [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") and if the `xyz` parameter's value changes in Gen, the [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") will update to reflect the new value. Furthermore, because the Gen parameter is linked to a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial"), it can be automated in a Max for Live device or used to for state management in [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/ "pattrstorage") or [preset](https://docs.cycling74.com/reference/preset/ "preset").
## Supplier Objects
The list of **suppliers** —objects that define parameters connectable to UI objects via `param_connect` will continue to expand over time. It currently includes:
  * Gen ([gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), [gen](https://docs.cycling74.com/reference/gen/ "gen"), [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix"), and [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix") as well as all the Gen codebox variants such as [gen.codebox~](https://docs.cycling74.com/reference/gen.codebox~ "gen.codebox~")).
  * RNBO ([rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~"))
  * The ABL objects
  * [v8](https://docs.cycling74.com/reference/v8/ "v8") with attributes defined via scripts that call `declareattribute`
  * [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") objects that contain subpatchers with [param](https://docs.cycling74.com/reference/param/ "param") objects. For more information, refer to [Polyphony](https://docs.cycling74.com/userguide/polyphony/).
  * [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") (shader parameters)


Not all supplier objects will support every `param_connect` feature but all provide for bidirectional control.
## UI Objects
To verify if a UI object can be connected to a parameter, look in the _Behavior_ category in the [Inspector](https://docs.cycling74.com/userguide/inspector/). If the object is compatible, you'll see a _Connect to Parameter_ attribute:
![](https://docs.cycling74.com/images/05c66282b0823f99512138948a07b1ef_440.webp)
Generally, any UI object that is [_parameter-aware_](https://docs.cycling74.com/userguide/parameter_mode/)—in other words, an object with `parameter_enable` attribute—will be able to connect to a supplier object. While some UI objects such as [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") handle multiple values, only the first value will interact with a parameter of a supplier.
Some non-UI objects—[pattr](https://docs.cycling74.com/reference/pattr/ "pattr") for example—are also parameter-aware but they cannot connect to parameters of supplier objects.
## Establishing Connections
Connections to parameters are always established with the UI object you want to use for control and display. There are three ways to establish a connection:
  * Use the _Connect_ submenu of the [Object Action Menu](https://docs.cycling74.com/userguide/action_menu/)
  * Using the [Inspector](https://docs.cycling74.com/userguide/inspector/) on the selected UI Object, choose the desired parameter from menu for the _Connect to Parameter_ attribute
  * Send the message `param_connect <path ID>` to the UI object. To determine the path ID, combine the scripting name of the supplier object with the parameter name separated by double colons as follows: `gen~_AB::xyz`

![](https://docs.cycling74.com/images/0541e3e0c6afd942b2609ddd58c88334_310.webp)
To view the scripting name of an object, select the object and open the Inspector or choose _Name..._ from the Object menu.
Note that while multiple UI objects can be connected to the same parameter, a UI object can only control a single parameter.
To disconnect a UI object from its parameter, choose _None_ from the _Connect_ submenu of the [Object Action Menu](https://docs.cycling74.com/userguide/action_menu/).
## Visualizing Connections
To see the connected parameter for a UI object, hold down the Option / Alt key while the cursor is over the object. A line will connect the UI object and supplier as shown below:
![](https://docs.cycling74.com/images/7a11f97211e72dbe777b495b7adf7acd_475.webp)
You can also check the connection via the menu in [Object Action Menu](https://docs.cycling74.com/userguide/action_menu/) or [Inspector](https://docs.cycling74.com/userguide/inspector/). The menu shows a check mark next to the connected parameter name.
## Limitations
Connections between UI objects and supplier objects can only occur in the same patcher. If you put the supplier object in a subpatcher (for example, via [encapsulation](https://docs.cycling74.com/userguide/subpatchers/#encapsulating-and-de-encapsulating)), the connection will disappear.
Parameter connections are generally single-valued. Multi-valued parameter data and user interface objects are not yet fully supported.
