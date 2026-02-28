---
description: Open a view into a subpatcher with a bpatcher, letting you create modular abstractions with custom user interfaces.
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/bpatchers/
title: bpatchers
---

# Using bpatchers
A [bpatcher](https://docs.cycling74.com/reference/bpatcher/ "bpatcher") embeds the interface of a patcher inside a box in its parent patcher.
![](https://docs.cycling74.com/images/b0613710c69a7b8ebc9d022b9981c98e_247.webp) The audio processing patcher in the center of this patcher is inside a bpatcher.
## Creating a [bpatcher](https://docs.cycling74.com/reference/bpatcher/ "bpatcher")
You can create a bpatcher either by creating one from scratch, or by [transforming](https://docs.cycling74.com/userguide/action_menu/#transform--patcher-to-bpatcher) an abstraction or subpatcher into a bpatcher.
### Starting with an Empty bpatcher
Create a new object (by pressing the `n` key for example), then type the name `bpatcher`. A bpatcher will replace the object box when you click outside the box.
![](https://docs.cycling74.com/images/793f5cdaf1f65f71908613f455f97411_208.webp) An empty bpatcher, immediately after creation
An empty bpatcher won't do anything. Setting the bpatcher's `@name` or "Patcher File" attribute will assign a patcher file within the search path to load. After a file is loaded, enable the `@embed` (_Embed Patcher in Parent_) attribute to save the contents of the file in the parent patcher.
You can also assign a file to a bpatcher by dragging a patcher file onto the object from the [File Browser](https://docs.cycling74.com/userguide/file_browser/) or one of the left sidebar browsers.
### Starting with a Patcher File
  * To turn a named patcher file into a bpatcher, start by pressing the `e` key. After the object box appears, type the file's name into the box, then click outside of the box. A bpatcher containing the file will replace the object box. For more details, see [Patcher Appearance in bpatchers](https://docs.cycling74.com/userguide/bpatchers/#patcher-appearance-in-bpatchers) below.
  * If you hold down the Option key while dragging a patcher file into a empty space in a patcher window, you'll see a contextual menu with several options. The _Create a bpatcher_ option will let you create a bpatcher directly with the contents of the .maxpat file. 
![](https://docs.cycling74.com/images/3744873db7f91f2e75db0a9fc4058020_426.webp)
  * Finally, you can drag any patcher file onto a bpatcher to replace the file the bpatcher currently uses.


### Converting a Subpatcher or Abstraction
Given any subpatcher or abstraction, you can also open the [Action Menu](https://docs.cycling74.com/userguide/action_menu/#transform--patcher-to-bpatcher) and select _Transform > Patcher to Bpatcher_ to convert to a bpatcher. You can also transform a bpatcher to a subpatcher or abstraction with the same menu.
## Opening the Contained Patcher
Choose _Open_ from the bpatcher's [Action Menu](https://docs.cycling74.com/userguide/action_menu/) to view and edit the bpatcher's contained patcher in a separate window.
### Editing an embedded patcher
If you open an embedded bpatcher from a [bpatcher](https://docs.cycling74.com/reference/bpatcher/ "bpatcher") object in the parent patcher, it may open in read-only mode. In this mode, you must click the _Modify read-only_ icon to unlock it for editing. See [Modify read-only](https://docs.cycling74.com/userguide/patching/#modify-read-only) for more information.
## Presentation View
By default, a bpatcher will display its patcher's patching view. If you want to display the [Presentation View](https://docs.cycling74.com/userguide/patching/#presentation-mode) instead, enable the `@openinpresentation` (_Open in Presentation_) attribute in the patcher file the bpatcher contains (_not_ the bpatcher itself) using the [Patcher Inspector](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector).
## Changing the Patcher's Offset
Often you'll want to set up a bpatcher to have a dynamic display, changing its presentation depending on some value. The best way to achieve this is by changing the `@offset` attribute of the bpatcher object, which will shift the origin of the displayed view by the desired horizontal and vertical amount. Since bpatcher is a slightly unusual object, you have to set this attribute using a [thispatcher](https://docs.cycling74.com/reference/thispatcher/ "thispatcher") object in the embedded subpatcher. See the bpatcher [help file](https://docs.cycling74.com/userguide/objects/#opening-a-help-file) for more details.
![](https://docs.cycling74.com/images/2b7010b8755205349037eb57241b7c45_876.webp) Overview of the offset technique for adjusting the display of a bpatcher
## Embeded vs Referenced Patchers
As mentioned above, a bpatcher can either refer to an existing patcher file or embed its contents in its parent. The differences are similar to subpatchers and abstractions. When you enable the `@embed` attribute on a bpatcher, the contents of the bpatcher will be saved with the parent patcher.
If `@embed` is not enabled, the bpatcher references a patcher file specified in its `name` attribute. As with abstractions, changes to the original file will update every bpatcher that refers to that file. See [abstractions](https://docs.cycling74.com/userguide/abstractions/) for more detailed information on working with bpatchers that reference patcher files.
## Patcher Appearance in bpatchers
As mentioned above, when loading a patcher file, the bpatcher will use the `openinpresentation` attribute of the patcher to determine whether to show it in patching or presentation mode.
In addition, the patcher file can control the bpatcher's initial size and appearance when using the `e` command to create the object.
  * To assign a default size for the bpatcher, use the `openrect` (_Fixed Initial Window Location_). The x and y coordinates of the openrect are ignored, but the width and height will be assigned to the bpatcher's initial width and height.
  * If `openinpresentation` is enabled and `openrect` is not set, the enclosing rectangle for all objects that belong to the presentation will be used as the bpatcher's initial size.


As an example, this patcher contains a [function](https://docs.cycling74.com/reference/function/ "function") object that has been added to the presentation.
![](https://docs.cycling74.com/images/af7ef1b1ddcdbc01c8b4fc333ae529a7_499.webp)
When using the `e` command and typing this patcher file's name, the resulting bpatcher frames the [function](https://docs.cycling74.com/reference/function/ "function") object as shown below.
![](https://docs.cycling74.com/images/65d7e7c8c3dd828ef2d581738da548a6_350.webp)
