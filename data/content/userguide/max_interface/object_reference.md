---
description: Access detailed documentaion of every object, including messages and attributes that the object understands
group: Max Interface
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/object_reference/
title: Object Reference
---

# Object Reference
Every object in Max not only has a dedicated [**help file**](https://docs.cycling74.com/userguide/help_files/), but also a reference page. This page completely describes the object's behavior, inlcuding:
  * A short and long description of the object's functionality
  * The Arguments and attributes that can configure the object
  * The symbols that the object understands
  * Other related object and documentation


## Sidebar
You can view an abbreviated form of the full reference for an object by clicking on the _Reference_ icon in the right sidebar.
![](https://docs.cycling74.com/images/70b1c3266f17a57ac33591dd7b7dab11_183.webp)
The reference sidebar view will display reference documentation for whichever object is currently selected in the patcher.
![](https://docs.cycling74.com/images/940aa65d5da3779ebe8ae1e003e0607c_565.webp) With the buffer~ object selected, the sidebar view displays reference documentation for that object.
### Filtering the sidebar
The top of the sidebar view shows a short description of the object. Using the text field above the description, you can filter the contents of the sidebar view to find the entry that you're looking for.
![](https://docs.cycling74.com/images/b948495a7c573177d53f525fd26da19e_522.webp)
### Arguments
The first section of the reference list view is for arguments. In this section, you can see all of the arguments that the object expects. Next to the name of the argument, you will see a short description of what the argument does. Click on an argument to select it, and a detailed description of that argument will appear at the bottom of the view.
![](https://docs.cycling74.com/images/dd33cb179242646043187329108b98ea_440.webp)
### Messages
Under the arguments section, the [**messages**](https://docs.cycling74.com/userguide/messages/) section lists all of the messages that the object can understand. Click on a message to see a detailed description of that message at the bottom of the view.
![](https://docs.cycling74.com/images/1f8c1d7ec0111973769ec0fd9c067fa4_440.webp)
You can drag and drop a row from the _Messages_ section into an unlocked patcher. When you do, a message box will appear in the patcher.
![](https://docs.cycling74.com/images/a41454b4f9f26b240750000793516eb5_588.webp)
### Attributes
The [**attributes**](https://docs.cycling74.com/userguide/objects/#attributes) section lists all of the selected object's attributes. As in the other sections, click on the attribute to see a detailed description of the attribute in the detail view at the bottom of the sidebar reference.
You can also drag and drop a row from the _Attributes_ section into an unlocked patcher. When you do, an [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object will appear in the patcher, pre-configured to select for the named attribute.
### See also
The last section of the sidebar reference is the _See Also_ section. This section lists related objects and documentation. You can double-click on any object in this section to open the [help file](https://docs.cycling74.com/userguide/help_files/) for that object, and you can double-click on any piece of documentation in this section to open it.
![](https://docs.cycling74.com/images/b5508dcc5a8aa4059930eb35aabe63d6_440.webp)
### Navigation
Use the buttons in the _Navigation Bar_ at the bottom of the view to quickly jump to related pages.
![](https://docs.cycling74.com/images/066b0d3042b47837028726e06f8d0470_411.webp)
  * _Show Previous Object_ — Jump to the sidebar reference for the last selected object.
  * _Show Next Object_ — After pressing _Show Previous Object_ , navigate forwards again.
  * _Open Full Reference_ - Show the [**Full Reference**](https://docs.cycling74.com/userguide/object_reference/#full-reference) for the selected object.
  * _Open Help File_ — Open the [help file](https://docs.cycling74.com/userguide/help_files/) for the selected object.


## Full Reference
### Accessing the full reference
You can access the full reference for a selected object in a variety of ways.
Right-click on the object and select _Open Reference_ from the contextual menu.
![](https://docs.cycling74.com/images/0640995126a0d50b8a2fb2a536f11bef_316.webp)
From the object [action menu](https://docs.cycling74.com/userguide/action_menu/), select _Reference_.
![](https://docs.cycling74.com/images/34d579fb484d41454ad2c326c4fd5d6f_278.webp)
With the object selected, click on the object name in the clue bar, and select _Reference_ from the menu.
![](https://docs.cycling74.com/images/3b3e37ebb4a421399e4ed731e5e98e69_421.webp)
Select the object, then select _Open Reference_ from the _Help_ menu.
![](https://docs.cycling74.com/images/2f8581b7c57436b8d82eda5352e7bae1_534.webp)
Finally, you can open the reference sidebar, and then click the _Open Full Reference_ button in the bottom navigation bar.
![](https://docs.cycling74.com/images/9bd96a5c7bc0b3e56ab9d3111a2e88c9_455.webp)
### Using the full reference
The full reference for an object is an extended version of the abbreviated reference available in the sidebar view. At the top of the reference document, you'll see the name of the object, a short and long description, a longer discussion about the object, and a button to open the help file. At the very top, you'll see breadcrumbs that show the path to the reference file in Max's documentation.
![](https://docs.cycling74.com/images/74cd5352bfe9ad392cedf0f8bb5dfe9a_801.webp)
The left side of the page shows the location of this reference document in Max's overall documentation. The primary Max documentation categories are listed here, in addition to a section _Package Documentation_ that lists all the documentation for [installed packages](https://docs.cycling74.com/userguide/package_manager/).
![](https://docs.cycling74.com/images/c1669204570a8f05881015329d52eff8_812.webp)
On the right side of the page, you'll see a navigation menu similar to the section categories from the sidebar reference view. From here you can jump to any section on the page, including the documentation for each argument, attribute, and message that the object supports. Additionally, the _Output_ section describes what messages or signals the object will send out.
![](https://docs.cycling74.com/images/17ab81b78e4fded61c632b319050fed0_807.webp)
In the _Arguments_ section, you'll see a detailed description of each argument. In addition to a description, you'll see the text `OPTIONAL` if the argument is optional, and you'll see the expected type of the argument as well. If the type is `[number]`, it means that the argument can be an int or a float.
![](https://docs.cycling74.com/images/1e057a75cfa614574f993246839d1852_425.webp)
The _Attributes_ section lists attributes in a similar way. Note that for some attributes, you may see a special label indicating the version of Max in which this attribute was introduced.
![](https://docs.cycling74.com/images/fadd259dcac2d0f7326d335118d2179d_489.webp)
The _Messages_ section lists all of the messages to which the object responds. A message will have the special symbol `(mouse)` to indicate how the object will respond to mouse clicks. The symbol `signal` indicates how the object will handle signal inputs.
![](https://docs.cycling74.com/images/2fde95730235576173fa22ba5f9da7db_433.webp)
Finally, the _Output_ section will describe what kinds of messages and signals the object generates. This optional section is most common for signal objects.
![](https://docs.cycling74.com/images/5eb863485ec408d19d818ce9f71876e3_433.webp)
### Object parent classes
The full reference for an object documents every message and attribute for that object. Some objects have many, many messages and attributes, especially objects that have a **parent class**.
Max objects don't have a strict notion of inheritance like you might find in object-oriented programming languages like C++. However, certain Max object do have a parent class from which the inherit many common messages and attributes. For example, the [jit.gl.gridshape](https://docs.cycling74.com/reference/jit.gl.gridshape "jit.gl.gridshape") object inherits from the _Common_ object class and the _OB3D_ object class.
  * **Common** - The class that all objects with an _object box_ inherit from. Adjust things like the font, background color, and the annotation.
  * **OB3D** - The parent class for all objects that manage an object in a 3D computer graphics scene. Attributes let you control things like the matrix transform and the color.


In the reference page for an object like this, you'll see a list of object parent classes with a disclosure triangle next to each.
![](https://docs.cycling74.com/images/e9567d536fcd60ef055a91afcd732724_475.webp)
Click on the disclosure triangle to see the attributes or messages that the current object inherited from the given parent class.
![](https://docs.cycling74.com/images/0757eea0676dcdd52c6912e0ec20c270_617.webp) Some of the messages that all objects from the OB3D object class will respond to
