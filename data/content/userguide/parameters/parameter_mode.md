---
description: Working with parameters, and enabling parameters for objects that support them
group: Parameters
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/parameter_mode/
title: Parameter Mode
---

# Parameter Mode
Some Max objects can define a **Parameter** , which is a simple representation of the current state of that object. Parameters define an interface between a Max patcher and some outside system for the purpose of presetting, automation and modulation. In a Max for Live device, parameters can be saved and recalled in the form of presets, and are exposed to Live **Automation** and **Modulation**. Even outside of Live, parameters let you set the initial value of an object, and can be saved and recalled by interacting with the [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") family of objects or [Snapshots](https://docs.cycling74.com/userguide/snapshots/). They can also map to MIDI events and the computer keyboard through Max's [Mapping System](https://docs.cycling74.com/userguide/mapping/).
!["A slider with parameter mode enabled"](https://docs.cycling74.com/images/da4cee6be2497366eef2e16c79fa1ad9_576.webp) This slider has enabled parameter mode, which creates a parameter 'Frequency' that can be controlled by a MIDI message.
Most Max UI objects and Max for Live UI objects support **Parameter Mode**. The [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") and [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") objects can also participate.
The [Parameters Window](https://docs.cycling74.com/userguide/parameter_mode/#parameter-window) shows all parameters currently associated with a patcher (or device), and permits you to change parameter attributes in a single place. You can also change parameter attributes for individual objects by using the Parameter tab of the [Inspector](https://docs.cycling74.com/userguide/inspector/).
## Enabling Parameter Mode
Many objects that support _Parameter Mode_ will have an attribute `@parameter_enable` or "Parameter Mode Enable". The Max for Live UI objects _always_ have their parameter enabled, and don't display that attribute.
!["The Parameter Mode Enable attribute"](https://docs.cycling74.com/images/8185d194e0b53ee742d7b4e71bda4f42_589.webp) The Parameter Mode Enable attribute
Activating _Parameter Mode_ for an object will create a parameter for that object. The object owns that parameter, and you can customize the behavior of the parameter through the parameter-related attributes on that object. Enabling the _Parameter Mode Enabled_ attribute will reveal all of the parameter-related attributes in the Inspector.
## Parameter Attributes
Name | Description  
---|---  
Visible to Mapping | When enabled, the parameter will be available for mapping to keyboard or MIDI input using [Max Mapping](https://docs.cycling74.com/userguide/mapping/)  
Order | Sets the order of recall of this parameter. Lower numbers are recalled first. See [Initial Value](https://docs.cycling74.com/userguide/parameter_mode/#initial-value).  
Link to Scripting Name | When enabled, the _Scriping Name_ attribute is linked to the _Long Name_ attribute. See [Parameter Names](https://docs.cycling74.com/userguide/parameter_mode/#parameter-names).  
Long Name | The internal, programmatic name of the parameter. Must be unique within the patcher hierarchy. See [Parameter Names](https://docs.cycling74.com/userguide/parameter_mode/#parameter-names).  
Short Name | The display name of the parameter, used in the user interface. See [Parameter Names](https://docs.cycling74.com/userguide/parameter_mode/#parameter-names).  
Type | Type of the parameter. In general this will be _Int_ (0-255), _Float_ (32-bit float), _Enum_ , or _Blob_. Some parameter types are disabled for certain objects.  
Range/Enum | The range of the parameter (for _Int_ or _Float_) or the members of the enumeration (for _Enum_ types). Unsupported for _Blob_ type parameters. See [Parameter Data Types](https://docs.cycling74.com/userguide/parameter_mode/#parameter-data-types).  
Enumeration Icons | Image files to be used in place of text on the Ableton Push controller, for parameters with the _Enum_ type.  
Modulation Mode | See [Parameter Modulation](https://docs.cycling74.com/userguide/parameter_mode/#parameter-modulation)  
Modulation Range | The _Modulation Range_ of the parameter, if enabled.  
Initial Enable | If enabled, the parameter will be set to an initial value when the patcher or device is loaded. When you turn this on, the current value of the parameter is stored as the initial value. See [Initial Value](https://docs.cycling74.com/userguide/parameter_mode/#initial-value).  
Initial Value | The parameter's initial vlaue, if _Initial Enable_ is enabled. See [Initial Value](https://docs.cycling74.com/userguide/parameter_mode/#initial-value).  
Unit Style | Changes how the value of the parameter will be displayed. For example, the _Pan_ style will display negative numbers as panning left, positive numbers as panning right, and zero as center pan.  
Custom Units | The format string used to to display the parameter's value, if _Custom_ is selected for _Unit Style_. Accepts sprintf-style format strings. See [Custom Units](https://docs.cycling74.com/userguide/parameter_mode/#custom-unit-styles).  
Exponent | Scales the exponential weight of the parameter's range. Values above `1` give the parameter more fine grained control near the low end of the parameter's range, while values between `0` and `1` give more fine grained control near the top end.  
Steps | The number of discrete steps between the minimum and maximum values of the parameter's range. Values are inclusive, so steps `4` with a range `10 40` will have the possible values `10`, `20`, `30`, and `40`.  
Update Limit (ms) | Limits the rate of updates when new values are triggered by automation.  
Defer automation output | When enabled, value updates that are triggered by automation are sent to the back of the [low priority queue](https://docs.cycling74.com/userguide/scheduler/#high-priority-and-low-priority-queues).  
Parameter Visibility | Determines whether parameters are hidden (to a host like Live), and whether their values are automatable. See [Parameter Visibility](https://docs.cycling74.com/userguide/parameter_mode/#parameter-visibility).  
## Initial Value
With Parameter Mode enabled, you can turn on the "Initial Enabled" attribute in order to set an initial value for the object. The object will restore this value when the patcher loads, as well as sending this value to any connected objects. For Live UI objects, you can also double-click on the object to restore its initial value. The "Order" attibute affects the order in which parameter-enabled objects are initialized. Objects with a lower value for their "Order" attribute will be initialized first.
![Attributes related to parameter initialization](https://docs.cycling74.com/images/a4f25975b568c29e56961a18bad5b399_477.webp) Attributes related to parameter initialization
### Reinitialize
Select _Reinitialize_ from the _Edit_ menu to set all parameters in the current patch to their _Initial Value_. See the [patching](https://docs.cycling74.com/userguide/patching/) guide for more information.
## Parameter Names
Parameter-enabled objects have three names associated with them: a **Scripting Name** , a **Short Name** , and a **Long Name**. The Long Name and Short Name attributes only affect the display of Live UI objects, and the visible name of the parameter when working in Live.
  * **Scripting Name** : The name of the _object_ as it appears to Max, this is a unique identifier that can be used to refer the object when you're scripting or using [pattr](https://docs.cycling74.com/reference/pattr/ "pattr"). Must be unique to the patcher.
  * **Long Name** : The name of the _parameter_ attached to the object. If you set up MIDI or Keyboard Mapping for the parameter, this is the name that you'll see in the **Mappings Sidebar**. It is also how the parameter will appear in Live. Must be unique to the entire patcher hierarchy.
  * **Short Name** : The display name of the parameter. This affects the display of Live UI objects like [live.slider](https://docs.cycling74.com/reference/live.slider "live.slider") and [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial"), which have a visible text label.


## Parameter Modulation
The "Modulation Mode" and "Modulation Range" attributes determine how **Modulation** from Live affects the value of the parameter (for more about Modulation, see Live's documentation). When the parameter is modulated, the modulation value is combined with the current value of the parameter and scaled by the modulation range to determine its final value.
### Unipolar
Modulation is between 100% and 0%. At 100%, the parameter isn't modulated at all. At 0%, the parameter takes on its minimum modulation value value. 
Unipolar Modulation Mod Range Parameter Value 0% 100%
Unipolar modulation mode
### Bipolar
Modulation is between -50% and 50%. The range of modulation depends on the current value of the parameter. The range shrinks as the parameter approaches its minimum or maximum value, so that even as it modulates it never exceeds those values. 
Bipolar Modulation Mod Range Parameter Value -50% 50%
Bipolar modulation mode. Notice that the range of the modulation is squished to 27 units on either side, so that the value after modulation never exceeds the maximum of 127.
### Additive
Additive modulation is the same as Bipolar, except the range of modulation never changes. Instead, modulation that would cause the parameter value to exceed its minimum or maximum value instead clips to that value. 
Additive Modulation Parameter Value -50% 50% clip clip
Additive modulation mode. 
### Absolute
Absolute modulation is not based on a percentage but rather the units of the parameter. No matter the range of the parameter, a modulation by 10 absolute units will always modulate by the same amount. Absolute modulation cannot be negative. 
Absolute Modulation Parameter Value +0st +30st +40st +20st +10st
Absolute modulation mode
## Parameter Data Types
The **Data Type** of a Max Parameter determines the internal storage format for the data.
  * **Float** : Can take on any value, including floating-point values, and can participate in Modulation from Live. The default storage type, and perfect for most applications.
  * **Int** : Can represent 256 distinct values, with a default range 0 to 255.
  * **Enum** : A list of items with user-configurable names. Cannot be modulated (but can be automated).
  * **Blob** : Parameters that cannot be automated or modulated, but can be stored in presets. These non-automatable parameters may be any type of data you can store with a [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object: single values, lists, dictionaries, arrays or symbols.


The Data Type only affects the internal storage format of the parameter, and does not change how the parameter's value is displayed. A parameter with the "Data Type" `Int` and the "Unit Style" `Float` will appear to be a decimal number, even though the value after the decimal will always be zero. Similarly, a parameter with the "Data Type" `Float` and the "Unit Style" `Int` will still display as if it were a whole number. In fact, this is the way to have a parameter with more than 256 values that still appears to be a whole number.
## Custom Unit Styles
The "Unit Style" attribute lets you change the units associated with your parameter, which for some objects will affect the way the value is displayed.
![Millisecond, decibel, and pan unit styles](https://docs.cycling74.com/images/7ef52d4c99ecfe1e37fe6652b400a30c_264.webp) Millisecond, decibel, and pan unit styles
If you like, you can define your own custom Unit Style. Select `Custom` as the value for the "Unit Style" attribute. The "Custom Units" attribute now lets you create your own units to follow the parameter value. You can use C-style format strings here, so `%0.2f Bogon(s)` would cause a parameter value of 15.5678 to display as `15.56 Bogon(s)`.
## Parameter Visibility
You can change the visibility of a parameter by changing the _Parameter Visibility_ attribute in the Inspector. If this attribute is set to `Automated and Stored`, the parameter will be stored in the Live Set and presets, and will be available for automation. If this attribute is set to `Stored Only`, the value will be stored, but it will not be visible to Live's automation system. If this attribute is set to `Hidden`, it will neither be stored nor available for automation.
You may want to have a parameter `Hidden` when it affects other Max for Live parameters. This will prevent problems with overloading Live's undo buffer, and will also limit issues with preset storage.
## Parameter Window
From the _View_ menu, select _Parameters_ to open the **Parameter Window** (this option will be disabled if your patcher does not contain any parameter-enabled objects). This window lists every parameter in the given patcher hierarchy.
!["The Parameter Window, listing the parameters amp, freq, and rate"](https://docs.cycling74.com/images/a42b0c73dc75a0636a41f8e55a69fcb5_739.webp)
### Updating parameters from the list
Because the Parameter Window lists all parameters in your patcher, it's a convenient place to change the name, range, initial value, and many other attributes of parameters in your patcher, without you needing to find the specific object that owns the parameter. Double-click on any cell in the parameter table to update the corresponding value for that parameter.
### Filtering and ordering parameters
In the top-right of the window, the _Filter Field_ lets you filter parameters by name. For example, typing "freq" into this field would show only parameters whose names contained the text string "freq".
Along the top of the parameter list, the table headers identify the kind of information displayed in each column. Click on a table header to sort parameters by the values in that column. Click again on the same header to toggle between an ascending and descending order. You can also drag on these column headers to reorder them.
### Customizing column headers
Right click on any column header to bring up a customization menu for column headers.
!["The Parameter Window, with a row containing the 'amp' parameter selected. A live.slider object that owns the 'amp' parameter has a yellow highlight in the patcher window."](https://docs.cycling74.com/images/d7c4c228ac8d89cdc15df3e3be1293a7_785.webp)
The commands "Auto-size this column" and "Auto-size all columns" will shrink the width of the column or columns to fit the text in the respective column.
Below these, the other menu options let you customize which columns will appear in the parameter list. Some columns have abbreviated names, for example the list option "I" refers to the parameter attribute "Initial Enable". You can hover over the header of any column to see the full name of that header, even if the title is abbreviated.
### Finding parameter objects
When you click to select a row in the parameter table, the object that owns that parameter will get a yellow highlight. You can also click the blue "P" button in that parameter's row and select "Reveal in Patcher" to show the same yellow highlight.
!["The Parameter Window, with a row containing the 'amp' parameter selected. A live.slider object that owns the 'amp' parameter has a yellow highlight in the patcher window."](https://docs.cycling74.com/images/4648090ad67f2b8f3fc9e0ad9d9d15b3_880.webp)
