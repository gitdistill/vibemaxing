---
description: The sidebar inspector lets you configure objects by changing attributes, and lets you change patcher-specific options
group: Max Interface
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/inspector/
title: Inspector
---

# Inspector
View and modify the internal state of any Max object using the inspector.
## Opening the Inspector
Open the inspector by clicking the _Inspector_ icon in the right toolbar.
![Close-up of the right toolbar, showing the Inspector icon.](https://docs.cycling74.com/images/908a5ba578d6ec760e4f98e0dcd7758e_206.webp) Opening the Inspector .
You can also select _Inspector_ from the _Object_ menu as another way to open or close the inspector. If you'd prefer to see the inspector in a separate window, select _Inspector Window_ from the _View_ menu instead.
## Inspector contents
The contents of the inspector are determined by the current selection. With a single object selected, the inspector will show all attributes for that object.
![The inspector sidebar, showing attributes for the selected click~ object.](https://docs.cycling74.com/images/9fe3ccc27211a1030c1203d5bf3ea670_556.webp) Inspecting an object
With multiple object selected, the inspector will show all attributes that are shared by the selected objects. Changing the value of a single attribute will update that attribute's value for all selected objects.
### Inspector Toolbar
The toolbar at the bottom of the inspector exposes several handy functions.
![Close cropped view of the inspector toolbar.](https://docs.cycling74.com/images/68ee9b6ee35a1d98bb10cb37ed66c8c2_451.webp) The inspector toolbar Icon Name | Function  
---|---  
[Modify Selected Item](https://docs.cycling74.com/userguide/inspector/#modifying-and-resetting-attributes) | Copy or change the value of an attribute.  
[Show Attribute Names](https://docs.cycling74.com/userguide/inspector/#attribute-names) | Show the programmatic ID of an attribute.  
[Show Column Header](https://docs.cycling74.com/userguide/inspector/#sorting-attributes) | Show the column headers for sorting.  
[Freeze Attribute](https://docs.cycling74.com/userguide/inspector/#freezing-attributes) | Freeze or unfreeze an attribute.  
Make Attribute in Patcher | Create an [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object in the patcher to modify the selected attribute.  
Show in Reference | Open the reference documentation for the selected object attribute.  
Show Object | Highlight and focus the selected object in the patcher view.  
### Finding your attribute
Some objects can have a lot of attributes. At the very top of the inspector window, a text input lets you display only those attributes whose text matches the contents of your filter. The match includes the attribute name, not just its display name, and so the filter text "var" will match the attribute `varname` with the display name "Scripting Name", even if _Show Attribute Name_ is not enabled.
![The text input at the top of the inspector window for filtering attributes.](https://docs.cycling74.com/images/6ead1ca192f1ac1245c59e1e2b2b5887_436.webp) Filtering the inspector
The tabs underneath the filter input select for attributes matching a given category. Attributes in the _Basic_ tab are the most common attributes for the selected object. Attributes under _Layout_ handle the positioning and appearance of the object. _Recent_ shows attributes most recently modified for the object, and the _All_ tab shows all attributes. Click and hold the _All_ tab to show the subcategories of all attributes, and pick one to open just the disclosure tab for that subcategory.
![The subcategory menu under All](https://docs.cycling74.com/images/ead5401e4ec87a1d55c0e6e433c57d0e_440.webp) Show subcategories under All
### Sorting attributes
It's possible to sort attributes by name or by value. In the bottom toolbar, click on the _Show Column Header_ icon in the bottom toolbar to reveal the headers of the inspector table.
![The inspector view, with 'Show Column Header' enabled, displaying the header for the table of attribute names and values.](https://docs.cycling74.com/images/17fc2ed5800be307bebfd194c47ac2a2_449.webp)
With the headers revealed, click on any header to sort all attributes based on the value of that column. Click on the header again to switch between ascending and descending sort.
### Dragging attributes
You can drag rows from the inspector into your Max patch. When you do so, Max will create a new [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object, configured to display the selected attribute. In this way you can quickly build an interface for controlling a particular set of attributes.
![](https://docs.cycling74.com/images/547cb049662cd211f4ba865d1594812e_311.webp) Drag and drop attributes from the inspector to create attrui objects
If you drag the attribute on top of an existing object, Max will automatically connect the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object to the target object. Finally, you can hold down the `option` key while dragging to display a popup menu with more options, including an option to create a [message](https://docs.cycling74.com/reference/message/ "message") box containing the current value of the attribute.
## Attribute Names
[Attributes](https://docs.cycling74.com/userguide/objects/#attributes) can be identified by their _Display Name_ , a brief, human-readable description, or by their _Scripting Name_ , a unique identifier used to fetch the attribute programatically. By default, the inspector hides the scripting name and shows only the display name. The _Show Attribute Name_ button in the inspector toolbar lets you toggle the visibility of the scripting name of each attribute.
![The inspector with "Show Attribute Names" enabled, revealing the scripting name of each attribute in the first column.](https://docs.cycling74.com/images/654803e98d87d93e9a37cbcab948c0e3_438.webp) Enable 'Show Attribute Names' to display the scripting name of each attribute.
## The Patcher Inspector
The _Patcher_ itself is, behind the scenes, just a Max object like any other. Many properties of the patcher, like the patcher background color, can be controlled by modifying the attributes of the patcher. To access the patcher inspector, open up the inspector with no object selected. An icon will appear at the top of the empty inspector view, which you can click to access the _Patcher Inspector_.
![An empty inspector, revealing the "Show Patcher Inspector" icon at the top of the inspector view.](https://docs.cycling74.com/images/5f376ed47bff79b17ad0484c6edd30aa_436.webp) An empty inspector, revealing the 'Show Patcher Inspector' icon at the top of the inspector view.
## Freezing Attributes
Most attributes, like font size or scripting name, are saved with the patcher and will be restored when you reopen the patcher later. However, some attributes are not stored by default, and will appear italicized in the object inspector.
![The inspector for the cycle~ object, showing the italic font used for the unsaved 'buffer' attribute, and the regular font used for the saved 'varname' attribute.](https://docs.cycling74.com/images/71a22b973d16997740536b2dc2bd4b65_373.webp) Unsaved attributes are shown in italics
If you want to save the value of an attribute, you can use the snowflake icon in the inspector toolbar to _freeze_ the attribute. Frozen attributes will embed their current value with the patcher, so that this value can be restored when the patcher is next opened. Once the attribute is frozen, the display name will show the frozen value of the attribute. It is also possible to freeze attributes that are normally saved with the patcher. Once an attribute is frozen in its way, the frozen value is the value that will be restored when the patcher is closed and reopened. It might be useful to freeze an attribute like this to "anchor" it to the frozen value, rather than its current value.
![The inspector view for a cycle~ object, showing the frozen 'frequency' attribute. The current value of the attribute is 440, and the frozen value is also 440.](https://docs.cycling74.com/images/828e7f5ec8a008896b33da9b18eb8cb2_349.webp) The frequency attribute, after it's been frozen.
## Modifying and Resetting Attributes
The _Modify_ icon in the bottom toolbar lets you copy, revert, and reset the value of a given attribute.
![Close cropped image of the inspector, showing the bottom toolbar, emphasizing the gear-shaped icon in the bottom left.](https://docs.cycling74.com/images/9a23847fc2a2bf2aac49f03620f8f5ce_407.webp) The gear icon in the left of the bottom toolbar
Select an attribute, then click on this icon to access several options related to the value of the attribute.
![The expanded view of the 'Modify Selected Item' menu, showing the options Copy Attribute, Revert Value, Set to Default Value, and Set to Frozen Value.](https://docs.cycling74.com/images/9942ea2b2d789a8ebff027a2e0dda92f_410.webp) The expanded 'Modify Selected Item' menu. Menu Item | Description  
---|---  
Copy Attribute | Copy the value of the attribute to the clipboard. Once the value is copied, you can paste the value to another attribute using the _Paste_ command from the _Edit_ menu.  
Revert Value | If the value of the attribute has been modified since the last time the inspector was opened, this option lets you set the attribute back to its original value.  
Set to Default Value | Reset the value of the attribute to its default. Not all attributes have a default value, so this option might not be enabled for all attributes.  
Set to Frozen Value | If you've frozen the attribute, establishing a new saved value for the attribute, you can use this option to set the attribute to the frozen value.
