---
description: Using the action menu to explore, transform, and interact with objects in your patcher.
group: Max Interface
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/action_menu/
title: Action Menu
---

# Action Menu
The [Action Menu](https://docs.cycling74.com/userguide/action_menu/) lets you explore, transform, and interact with objects in your patcher. It groups together common operations on an object, like viewing its attributes or messages. It also gives you access to Transformations, which are a powerful way to refactor your patcher.
## Viewing the Action Menu
With the patcher unlocked, hover near the middle-left side of the object until a green arrow appears.
![A cycle~ object with the action menu "green arrow" visible on the left side](https://docs.cycling74.com/images/165bb8130ec5b49d31abfe1280f8c3a8_120.webp)
Click the arrow to reveal the action menu.
## Parts of the Action Menu
![An open action menu, revealing the options: Attributes, Messages, Files, Prototype, Transform, Inspector, Style, Help, Reference, Edit](https://docs.cycling74.com/images/cabfabb5952a2305559ce42c5b1d1685_586.webp) Name | Description  
---|---  
Attributes | Lists the current state of all the object's attributes. Select an attribute from the Attributes submenu to create an [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object attached to the object, configured with the given attribute.  
Messages | Select a message from the Messages submenu to create a message box attached to the object containing the given message. You'll typically want to type in an argument after the message name in the newly created message box.  
Files | If the object can read in a file, like [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") or [jit.movie~](https://docs.cycling74.com/reference/jit.movie~ "jit.movie~"), then this option will list all compatible files in Max's [search path](https://docs.cycling74.com/userguide/search_path/). Selecting any one will load that file into the object.  
Prototypes | Select a prototype from the submenu to replace the object with a new version containing a collection of attributes. See [prototypes](https://docs.cycling74.com/userguide/action_menu/#prototype).  
Apply Changes | Choose a prototype from the submenu to apply the collection of attributes to the object. See [prototypes](https://docs.cycling74.com/userguide/action_menu/#prototype).  
Connect | (UI objects only.) Assign a connectable parameter. See [Connecting Parameters](https://docs.cycling74.com/userguide/param_connect/).  
Transform | Transformations defined for this object. See [transform](https://docs.cycling74.com/userguide/action_menu/#transform).  
Inspector | Open the [inspector](https://docs.cycling74.com/userguide/inspector/) for this object.  
Style | Choose a [style](https://docs.cycling74.com/userguide/styles/) for this object.  
Help | Open the help patcher for this object.  
Reference | Open the object reference for this object.  
Edit | Perform the same action as double-clicking on the object. For example [js](https://docs.cycling74.com/reference/js/ "js") and [coll](https://docs.cycling74.com/reference/coll/ "coll") open a text editor to edit their contents. MIDI objects such as [noteout](https://docs.cycling74.com/reference/noteout/ "noteout") display a menu of MIDI ports.  
### Additions
Some objects, like [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") for example, may add their own actions to the action menu. In this case, gen~ adds the "Reset Parameters" option which, as you might expect, resets all the parameters of the gen~ object in question.
![](https://docs.cycling74.com/images/3521fcd1f01ae521e2a7e611546dfc6d_232.webp)
## Using the Action Menu
The action menu provides quick access to two of the most powerful ways to modify an object in place: transforms and prototypes.
### Transform
Transformations let you change the way an object is represented, without changing its behavior. Usually you'd do this because it's more convenient to work with an object in a different representation.
#### Transform > Changed Attributes to Arguments
![A metro object connected to an attrui with the text 'active' and the active attribute enabled. An arrow points to another metro object with the same text and active attribute, except the text '@active 1' has been added to the object box.](https://docs.cycling74.com/images/f7ef3396fb0dffd1314aa642cff3cb9a_407.webp)
This option takes all of the attributes on the given object that have been modified from their original state, and includes them as initial attribute values in the object box. This can be a useful alternative to freezing [attributes](https://docs.cycling74.com/userguide/objects/#attributes), and is a handy way to "lock in" the current state of an object.
#### Transform > Multi Channel Version / Single Channel Version
![A cycle~ object with an arrow pointing to an mc.cycle~ object.](https://docs.cycling74.com/images/361a99d933dd3fc98e06243b1f42ca36_307.webp)
Convert between single- and multi-channel versions of an MSP object. Usually this will involve adding or removing the `mc.` prefix.
#### Transform > Patcher to Bpatcher
![A subpatcher object with the text "p subpatcher" and an arrow pointing to a bpatcher containing a slider object.](https://docs.cycling74.com/images/8be9c9fb0508a3c556945ef416a4329b_530.webp)
This extremely useful option converts a [subpatcher](https://docs.cycling74.com/userguide/subpatchers/) to a [bpatcher](https://docs.cycling74.com/userguide/bpatchers/). If you end up adding interface controls to a subpatcher, this is a great way to expose the [presentation view](https://docs.cycling74.com/userguide/patching/#presentation-mode) of your subpatcher at the top level.
### Prototype
![The transformation menu for a slider object, expanded to reveal all of the prototypes defined for a slider. ](https://docs.cycling74.com/images/5dafd250d2a7e93fac6ece29a3a1ffe6_273.webp)
[Prototypes](https://docs.cycling74.com/userguide/prototypes/) store configurations of a given object, such as the range and colors of a slider. Choosing an item from the Prototype submenu replaces the object with the prototype. Choosing an item from the Apply Changes submenu updates the existing object with the changed attributes stored in the prototype file.
