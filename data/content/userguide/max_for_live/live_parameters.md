---
description: Dealing with parameters and their interaction with Live sets
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_parameters/
title: Device Parameters in Max for Live
---

# Device Parameters in Max for Live
_Parameters_ are settings of Max for Live devices you want to store and/or automate in Live. In some cases, a parameter may be set once and never change. In other cases, you'll want to use Max objects to interact with parameter values by clicking and moving the mouse, by receiving MIDI data mapped to a parameter, or via Live [automation](https://docs.cycling74.com/userguide/m4l/live_automation/).
There are a few ways to add parameters to your device. The most straightforward method is to use Live UI objects. By default, each Live UI object and its corresponding value is stored in the Live set. Alternatively, you are able to configure Max UI objects to also have this behaviour and be stored in the Live document by setting [Parameter Mode Enable](https://docs.cycling74.com/userguide/m4l/live_parameters/) to true. Another option is to use [pattr](https://docs.cycling74.com/userguide/m4l/live_pattr/).
The [Parameters Window](https://docs.cycling74.com/userguide/m4l/live_parameterswindow/) shows all parameters currently associated with a device, and permits you to change parameter attributes in a single place. You can also change parameter attributes for individual objects by using the Parameter tab of the [Inspector](https://docs.cycling74.com/userguide/inspector/).
## Live UI Objects
Max for Live includes user interface objects designed to work with the parameter system whose names all begin with `live.`. These objects have some special abilities:
  * They allow you to set an initial state that will be recalled automatically when a device is instantiated, saved, or edited.
  * They work seamlessly with Live's MIDI and keyboard mapping capabilities.
  * If you choose to make the UI object's parameter automatable, you can control it with Live's automation facility.


In other respects, the Live UI objects act like ordinary Max user interface objects.
## Parameter Data Types
Parameters used in Max for Live can be one of four types:
  * integer: integer values with a range of up to 256 values (default 0-255)
  * floating-point: floating point values (no range restriction)
  * enum: an enumerated list of items
  * blob: parameters that cannot be automated but can be stored in presets. Non-automatable parameters may be any type of data you can store with a [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object: single values, lists, or strings.


### Working with Integer parameters requiring more than 256 values
The native integer representation is limited to the 0-255 range. If you need an integer type that exceeds this range then instead set the type to **Float** , and change the unit style to **Int**
  * Select an object and click the Inspector icon on the Patcher toolbar to show the object's [Inspector](https://docs.cycling74.com/userguide/inspector/)
  * Choose **Float** from the pull-down menu in the Type attribute's Value column.
  * Choose **Int** from the pull-down menu in the Unit Style attribute's Value column.


The native integer representation is limited to 256 values, with a default range of 0-255. When working with Live UI objects whose integer values will exceed this range, the Type attribute should be set to Float, and the Unit Style attribute should be set to Int:
Although the parameter value will be stored as a floating-point number, it will be displayed as an integer.
The native integer representation is limited to 256 values, with a default range of 0-255. When working with Live UI objects whose integer values will exceed this range, the Type attribute should be set to Float, and the Unit Style attribute should be set to Int: 
## Setting an initial state for a Live UI object
  * Select the Max for Live UI object and click the Inspector icon in the Patcher toolbar to show the object's [Inspector](https://docs.cycling74.com/userguide/inspector/).
  * Scroll down to the Parameter section to see the Parameter attributes.
  * Check the Initial Enable checkbox.
  * Enter a floating-point value for the Initial Value attribute.


## Setting an initial state for a standard Max UI object
  * Add a [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object to your patch, typing the parameter name you want to use as an argument to the object. Connect the pattr object's middle (bindto) outlet to the Max UI object.
  * Select the [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object and open the [Inspector](https://docs.cycling74.com/userguide/inspector/). Scroll down to the Parameter section to see the Parameter attributes.
  * Check the [Parameter Mode Enable](https://docs.cycling74.com/reference/pattr/#attr_parameter_enable) checkbox.
  * Check the Initial Enable checkbox.
  * Enter a floating-point value for the Initial Value attribute.


## Parameter Modulation
Parameters can be modulated by clip envelopes in Live according to one of four modes:
  * In _unipolar_ mode, the parameter value is modulated between the minimum range value (set using the `Clip Modulation Range` attribute) and its current value.
  * In _bipolar_ mode, the full modulation range of a parameter is equal to twice the distance between the current value and nearest boundary set using the parameter’s `Clip Modulation Range` attribute. If the current value is exactly halfway between the lower and upper ranges, the modulation range is equal to the total parameter range.
  * In _additive_ mode, the modulation range from the current value is equal to plus or minus one-half of the total range of the parameter. Values are truncated if they fall outside of the `Clip Modulation Range` attribute.
  * In _absolute_ mode, the current value is either the upper or lower bound of the modulation range. If the current value is less than half of the full parameter range, the modulation assumes a lower range of the current value minus the modulation range. If the current value is greater than half of the full parameter range, the modulation assumes the upper range is current value and the lower range is equal to the current value minus the modulation range value.


## Enabling Parameter Modulation
  * Select the parameter object ([pattr](https://docs.cycling74.com/reference/pattr/ "pattr") or Live UI) and open the inspector. Click the Parameter tab to show the parameter attributes.
  * Set the `Clip Modulation Mode` and, if applicable, the `Clip Modulation Range` attributes.


## Parameter Names
Max for Live provides several ways to give a parameterised object a name using attributes. These attributes can be set using the guidelink[Inspector][#inspector](https://docs.cycling74.com/reference/%23inspector/ "#inspector").
  * The `Scripting Name` attribute can be used to identify a UI object when used in conjunction with the Max [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") preset objects. When a UI object has a scripting name set, it will automatically appear in the [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/ "pattrstorage") object's inventory of parameter names when you add an [autopattr](https://docs.cycling74.com/reference/autopattr/ "autopattr") object to your Max patch as described in the [pattr Chapter 2](https://docs.cycling74.com/learn/articles/pattrchapter02/) tutorial.
  * The `Short Name` attribute can be used in conjunction with the `Display Parameter Name` attribute to label [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") and [live.slider](https://docs.cycling74.com/reference/live.slider "live.slider") object when you use them in a device.
  * The `Long Name` attribute is be used to identify a parameter to the Live application's Parameter automation and MIDI mapping. You can use a single name for all three of these attributes by checking the `Link to Scripting Name` attribute in the object's Inspector. You may find this to be a simple approach to managing paramter naming.


## Setting the display name for a parameter
  * Add a Max for Live UI object to your device. When the UI object first appears, it displays the name of the object itself.

![](https://docs.cycling74.com/images/6345a5091a06419c13bb2fc234a0d228_67.webp)
  * Select a the object and click the Inspector icon on the Patcher toolbar to show the object's [Inspector](https://docs.cycling74.com/userguide/inspector/).
  * Double-click in the Value column for the Short Name setting to show a cursor and text box. Type in a name for the parameter, followed by a carriage return. The Value column will be de-selected, and your parameter name will appear in the object's display.

![](https://docs.cycling74.com/images/87b48ef629a5e8c1d219945df57a86d0_67.webp)
Note: If your short name is too long, it will be automatically truncated. If you are using a [live.slider](https://docs.cycling74.com/reference/live.slider "live.slider") or [live.gain~](https://docs.cycling74.com/reference/live.gain~ "live.gain~") object, you can use resize the object manually by clicking in the lower right-hand corner of the object and dragging. If you are using a [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") object, you should enter a new horizontal value for the `Patching Rectangle` or `Presentation Rectangle` attributes using the object's Inspector.
## Setting a custom unit style
  * Select a Max for Live UI object and click the Inspector icon on the Patcher toolbar to show the object's [Inspector](https://docs.cycling74.com/userguide/inspector/).
  * Choose **Custom** from the Unit Style pulldown menu.
  * Double-click in the Value column of the Custom Units attribute to show a cursor and text box. Type in a string to be used for the custom unit style, followed by a carriage return. The Value column will be de-selected, and the name will be set.
You can type in custom unit strings as symbols (e.g. "Harmonic(s)"), in which case the parameter's value will be displayed in its 'Native' display mode, followed by the symbol (e.g. "12 Harmonic(s)" for an Int-typed parameter or "12.54 Harmonic(s)" for a Float-typed parameter). If you would like to have additional control over the numerical component displayed, you can enter a sprintf-style string (e.g. "%0.2f Bogon(s)", which would display a value such as ".87 Bogons").


## Controlling a parameter's visibility
  * You can change the visibility of a parameter by changing the `Parameter Visibility` setting in the [Inspector](https://docs.cycling74.com/userguide/inspector/). If this attribute is set to Automated and Stored, the parameter will be stored in the Live Set and presets, and will be available for automation. If this attribute is set to Stored Only, the value will be stored, but it will not be visible to Live's automation system. If this attribute is set to Hidden, it will neither be stored nor available for automation.
  * You may want to have a parameter Hidden when it affects other Max for Live parameters. This will prevent problems with overloading Live's undo buffer, and will also limit issues with preset storage.


