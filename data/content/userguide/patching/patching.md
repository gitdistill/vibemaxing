---
description: How to create, connect, and configure objects.
group: Patching
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/patching/
title: Patching
---

# Patching
The word **patching** describes everything that you do as part of creating a Max patcher, including adding, positioning, configuring, and connecting objects.
## Locking/Unlocking
A new Max patcher is **unlocked** by default. Unlocking a patcher is also called putting the patcher in **edit mode**.. When unlocked, you can use the mouse and keyboard to create, delete, move, and connect objects. You can click and drag in the background of a patcher to start a selection, and drag to select multiple objects.
![](https://docs.cycling74.com/images/46b987f810d021a457125fda9b8908ad_285.webp)
When the patcher is locked, you can no longer modify objects using the mouse and keyboard (you can still edit the patcher via [scripting](https://docs.cycling74.com/userguide/scripting_overview/)). Instead, you can operate user interface (UI) objects (sliders, dials, buttons, etc.) by clicking and dragging on them. You could say that you unlock a patcher to work on it, and then lock the patcher to perform with it.
![](https://docs.cycling74.com/images/37f2bb8b31269cd6fe7e6a69917b67e7_297.webp) Lock the patcher to control UI objects like sliders
While the patcher is unlocked, you can still operate UI objects as if the patcher were locked by holding the `⌘` (macOS) key or the `CTRL` (Windows) key. This is convenient if you want to adjust an object quickly without locking.
You can lock the patcher by clicking the _Lock_ icon in the [bottom toolbar](https://docs.cycling74.com/userguide/patcher_window/#bottom-toolbar), or by selecting _Edit_ from the _View_ menu.
### Modify read-only
If you open an [_abstraction_](https://docs.cycling74.com/userguide/abstractions/), or if you're viewing the contents of a [_bpatcher_](https://docs.cycling74.com/userguide/bpatchers/), [poly~](https://docs.cycling74.com/reference/poly~/ "poly~"), [pfft~](https://docs.cycling74.com/reference/pfft~/ "pfft~"), or any other object that loads a separate patcher, the _Edit_ icon will be disabled and replaced by the _Modify read-only_ icon. A read-only patcher cannot be unlocked by pressing `⌘``e` (macOS) key or the `CTRL``e` (Windows) key—you must click on the _Modify read-only_ icon to unlock a read-only patcher. This is to help you avoid accidentally modifying a patcher that other patchers might depend on.
![](https://docs.cycling74.com/images/d836766644a45e1279b5b7b42648af8b_378.webp) Patchers that load in read-only mode must be unlocked by clicking the Modify read-only icon.
### Operate While Unlocked
With _Operate While Unlocked_ enabled, you can adjust user interface objects using the mouse even while the patcher is unlocked (in _Edit_ mode). You can enable this mode by clicking the _Operate While Unlocked_ icon in the [bottom toolbar](https://docs.cycling74.com/userguide/patcher_window/#bottom-toolbar), or by selecting _Operate While Unlocked_ from the _View_ menu.
In this mode, hold down `shift` while clicking to select UI objects without changing their value. You can also select a UI object by clicking its border. Hold down `shift` and start dragging a UI object to move it, then release `shift` once you've started dragging.
To perform actions with UI objects that require the `option` key, hold down the `option` and `⌘` (macOS) or `CTRL` (Windows) keys.
## Creating Objects
With the patcher unlocked, create a new object by pressing the `n` key, or by double clicking. You can also drag in an object from the [top toolbar](https://docs.cycling74.com/userguide/patcher_window/#top-toolbar). Once a new object is created, keyboard focus moves to the text field in the new object.
![](https://docs.cycling74.com/images/69b88a1355af26552ff02a26a6dd2cc2_161.webp) A new object, with keyboard focus.
For more on creating objects, understanding objects, and learning about objects, see the dedicated [Objects](https://docs.cycling74.com/userguide/objects/) page in the User Guide.
## Positioning Objects
With the patcher unlocked, click and drag on an object to move it. If multiple objects are selected, the objects will move as a unit. You can also use the arrow keys to make fine adjustments, or hold `shift` and press the arrow keys to make large adjustments. As you move objects around your patcher, the the [_Clue Bar_](https://docs.cycling74.com/userguide/patcher_window/#bottom-toolbar) will show you how your action will affect the object's position.
![](https://docs.cycling74.com/images/9fb2601857d9f81181b3a3dc973060c0_437.webp)
### Pixel alignment
If an object has a position with fractional values, it will no longer align precisely with the pixels used for display on your screen. This can cause subtle aliasing issues that can affect how objects look. One way this can happen is if you try to reposition an object while the patcher view is [zoomed](https://docs.cycling74.com/userguide/patching/#zooming).
![](https://docs.cycling74.com/images/48081c603b81f7421fa14b59bfd8dc25_522.webp) These two multislider objects are displaying the same data, but because the object on the bottom is not pixel-aligned, the slider bars look blurry.
There is a [patcher attribute](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector) called `@integercoordinates` or _Snap to Pixel_ that enforces whole number coordinates for all objects in the patcher. You can also select any number of objects that you'd like to align to the pixel grid and select _Apply Grid > Apply 1x1 Pixel Grid_ from the _Arrange_ menu to move all selected objects to integer coordinates.
## Copying Objects
Select a group of objects and select _Copy_ from the _Edit_ menu to copy them to the clipboard. Select _Paste_ to paste those objects into the patch. You can also select _Duplicate_ to copy-paste with a single command. Finally, you can hold `option` (macOS) or `alt` (Windows) while dragging a group of selected objects to copy them before dragging.
After you _Paste_ or _Duplicate_ a group of objects, you can reposition the newly created group of objects. When you do, Max will remember the offset from the original object group. This lets you quickly create a large number of evenly-spaced object groups.
  1. Select a group of objects
  2. Copy and paste (or duplicate) that group
  3. Reposition the pasted group
  4. Select _Paste_ or _Duplicate_ to paste a new group with the same spacing.

![](https://docs.cycling74.com/images/82115adbb514da9644be0ca1bb49222f_277.webp) Paste or duplicate multiple times after spacing.
### Copy Compressed
The _Copy Compressed_ command from the _Edit_ menu will copy a group of objects as compressed text. You can share this text anywhere, and restore the objects from compressed text simply by pasting, or by using the _New From Clipboard_ command from the _File_ menu. See the [copy compressed](https://docs.cycling74.com/userguide/sharing/#copy-compressed) section of the [Sharing](https://docs.cycling74.com/userguide/sharing/) page for more information.
## Resizing Objects
When any number of objects are selected, you can resize those objects by clicking and dragging on the white resize handles that appear. Hold shift while dragging to maintain aspect ratio while adjusting size. Note that some objects, like the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") object, have an intrinsic aspect ratio that cannot be changed.
![](https://docs.cycling74.com/images/d1f95bb5a3cf9f1f87640cfbcf1cff8a_502.webp) Resize an object using the white resize handles that appear when an object is selected.
Objects that display text, like non-UI objects, [comment](https://docs.cycling74.com/reference/comment/ "comment")s and [message](https://docs.cycling74.com/reference/message/ "message") boxes, have a fixed height that will not change while resizing. Instead, changing the width of the object will reflow its text. Hold shift while dragging to change the size of object's font while adjusting its width.
![](https://docs.cycling74.com/images/3a5716236d9aba0ac832db707975ce32_1008.webp) Hold shift while adjusting the size of a text object to change its font size along with its height.
For text objects like [comment](https://docs.cycling74.com/reference/comment/ "comment") and [message](https://docs.cycling74.com/reference/message/ "message"), you can select _Fix Width_ from the _Object_ menu to adjust the width of the object to fit its text.
![](https://docs.cycling74.com/images/ba4b50c4ef3c942de0299902c63e86a9_332.webp) Use the Fix Width menu command to adjust the width of text objects.
### Patching Rectangle
The position of an object in a patcher is called its **Patching Rectangle**. These four numbers determine the distance of the object from the left and top edge of the patcher, as well as its width and height. This value is also exposed as an object [attribute](https://docs.cycling74.com/userguide/objects/#attributes) called `@patching_rect`, and can be adjusted from the [inspector](https://docs.cycling74.com/userguide/inspector/).
![](https://docs.cycling74.com/images/8784d633411eda18360ed44794ccc65e_520.webp) An object's position is determined in part by its @patching_rect attribute
## Aligning Objects
You can align objects by selecting one of the _Align_ options from the _Arrange_ menu. You can align objects by their left, top, right, or bottom edge, or by their vertical or horizontal center. Most of the time, you can simply press `⌘``j` (macOS) or `CTRL``j` (Windows) for the _Auto Align_ command, which will align objects automatically based on whether they take up more vertical or horizontal space.
![](https://docs.cycling74.com/images/178fdc6a48b77068dd8e2805a9a486df_353.webp) Since these objects take up more vertical space, the Auto Align command will align their left edge.
## Distributing Objects
You can distribute objects, either vertically or horizontally, equalizing the space between each object in either direction. Select one of he _Distribute_ options from the _Arrange_ menu, or press `shift``option``⌘``h` (macOS) or `shift``option``CTRL``h` (Windows) for horizontal spacing, or press `shift``option``⌘``v` (macOS) or `shift``option``CTRL``v` (Windows) for vertical spacing. After distributing, adjustment handles will appear around the objects, which you can use for further equal-space adjustments.
![](https://docs.cycling74.com/images/138e18cb18c973600351298b42364afe_379.webp) After distributing, you can use handles for further refinement.
## Grouping Objects
If you want to maintain the spacing between objects, even if one of them is moved, you can assign them to a **group** by selecting _Group Objects_ from the _Arrange_ menu. When one memeber of a group is selected, the whole group will have a thin black border.
When you resize a group using the resize handles, Max will scale the spacing between objects, rather than the objects themselves.
## Presentation Mode
Max is designed both as a visual programming environment and as a tool for building user interfaces. It's easy to design an interface simply by sizing and positioning objects as you'd like them to appear. However, when you want to perform with or demonstrate your patch, you might want to hide or reposition certain objects. By using **Presentation Mode** , you can configure a special appearance for your patch, showing just the most important objects.
![](https://docs.cycling74.com/images/fe61bef511825babb4ca4152b806de40_538.webp) On the left, the patcher as it appears normally. On the right, the same patcher in presentation mode. Only the objects that have been selected for presentation mode appear.
In order to add an object to Presentation Mode, select it and then choose _Add to Presentation_ from the _Object_ menu. Once added, the object will have a pink border. If you no longer want to see the object in Presentation Mode, select _Remove from Presentation_ from the _Object_ menu.
Adding an object to Presentation Mode simply enables the `@presentation` or _Include in Presentation_ attribute.
You can toggle between Presentation Mode and Patching Mode by selecting the _Presentation_ icon from the [bottom toolbar](https://docs.cycling74.com/userguide/patcher_window/#bottom-toolbar), or by selecting _Presentation_ from the _View_ menu. An object can have a different size and position in Presentation Mode than in Patching Mode. When you toggle between the two, you will see objects animate to their new positions and sizes. In addition, you'll notice that the `@patching_rect` and `@presentation_rect` object attributes will be different, reflecting the two distinct positions for the object.
![](https://docs.cycling74.com/images/cba0eb3469b191bbafb81a3544afc756_731.webp) The selected slider has different values for @patching_rect and @presentation_rect, and the @presentation attribute is enabled.
If you want a patcher to open in Presentation Mode by default, enabled the _Open in Presentation_ [attribute](https://docs.cycling74.com/userguide/objects/#attributes) in the [patcher inspector](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector). This can be especially useful for [bpatchers](https://docs.cycling74.com/userguide/bpatchers/) that you intend to use as high-level modules.
## Object Ordering
Whenever you add a new object to your patcher, Max adds it on top of any existing objects. By selecting _Send Backward_ or _Send to Back_ from the _Arrange_ menu, you can instead have other objects draw on top of the selcted object. The commands _Bring Forward_ and _Bring to Front_ instead cause an object to be rendered on top of other objects.
![](https://docs.cycling74.com/images/1add872dd225ea4d8037a5d9c1d460e2_250.webp) After selecting Send Backward, the newly created dial renders behind the cycle~ object.
By making parts of some objects transparent, you can create compound UI object by layering existing objects in a clever way. You might find the attribute `@ignoreclick` useful in this case.
## Foreground and Background
Max patchers provide a simplified implementation of a layering system, with a foreground and a background layer. The main goal of this system is to make it easier to separate documentation objects like [comment](https://docs.cycling74.com/reference/comment/ "comment") and [panel](https://docs.cycling74.com/reference/panel/ "panel") from logical objects that affect the behavior of the patcher. Objects in the background will always be rendered behind objects in the foreground, though both may appear in Presentation Mode.
By default, all objects are added to the foreground. You can add an object to the background by selecting _Include in Background_ from the _Arrange_ menu. You can hide and show the background and foreground by selecting _Hide Background_ and _Hide Foreground_ from the _View_ menu. It can also be very useful to lock the background, which you can do by selecting _Lock Background_ from the _View_ menu. When the background is locked, objects in the background cannot be selected. This makes it possible to rearrange objects in the foregroudn without background objects getting in the way.
![](https://docs.cycling74.com/images/bdad3e6da04001a47354204d513d98c0_377.webp) The panel object (drawing the rounded rectangle border) cannot be selected, because it's included in the background and the background is locked.
## The Grid
To make it easier to lay out objects visually, you can enable the grid by selecting _Grid_ from the _View_ menu, or by clicking the _Grid_ icon in the [bottom toolbar](https://docs.cycling74.com/userguide/patcher_window/#bottom-toolbar). The grid is only visible when the patcher is in _Edit_ mode, and will disappear when the patcher is locked.
![](https://docs.cycling74.com/images/4faea3e35b587c30d50d84a5b5913769_152.webp) Enabling the grid may make object layout more consistent and readable.
By default, the grid is simply a visual indicator, and objects will not be aligned to the grid while dragging. Choose _Snap to Grid_ from the _Arrange_ menu, and objects will always be alignd to the grid when you reposition them with the mouse. With this option enabled, objects will also snap to the grid when you resize them. While repositioning or resizing, you can hold down the `⌘` (macOS) or `CTRL` (Windows) key to temporarily disable snapping.
![](https://docs.cycling74.com/images/4675560eed16c9919d1aba7f9207b4a1_534.webp) Object before and after grid-alignment
After enabling _Snap to Grid_ , objects that were positioned without this option enabled may not be aligned to the grid, and will not be aligned automatically. To align existing objects to the grid, select _Apply Grid > Apply Current Grid to Position_ or _Apply Grid > Apply Current Grid to Position and Size_ from the _Arrange_ menu.
You can change the size of the grid using the _Grid Size_ [patcher attribute](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector), visible from the [patcher inspector](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector).
![](https://docs.cycling74.com/images/cc28a4cc3216615ca59eb80b88f863c6_446.webp) The Grid Size attribute in the patcher inspector
## Routing Patch Cords
To keep your patcher looking clean and organized, you can create [segmented patch cords](https://docs.cycling74.com/userguide/patch_cords/#segmented-patch-cords), or you can have Max [route the patch cords](https://docs.cycling74.com/userguide/patch_cords/#aligning-and-routing-patch-cords) for you automatically. Routed patch cords are segmented in a way that tries to use only right angles while also avoiding intersecting other objects.
![](https://docs.cycling74.com/images/e880488db7359797964de3f0ba88f6ec_290.webp) A patch cord after automatic routing
## Changing Colors
You can change the appearance of most parts of the patcher, including the color of objects, patch cords, and the patcher background. Color changes can be applied individually, or as a [style](https://docs.cycling74.com/userguide/styles/) across the whole patch.
  * Change the color and appearance of the patcher itself using the [patcher inspector](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector).
  * Change the appearance of objects by adjusting each object's individual [attributes](https://docs.cycling74.com/userguide/objects/#attributes), by setting a [style](https://docs.cycling74.com/userguide/styles/) for each object, or by setting a [style](https://docs.cycling74.com/userguide/styles/) for the patcher.
  * You can also change the [color of patch cords](https://docs.cycling74.com/userguide/patch_cords/#coloring-patch-cords) in your patcher.


## Zooming
You can adjust the zoom level of your patcher, either zooming in to make more precise adjustments, or zooming out to see more objects at once.
  * Find a precise zoom level using the _Zoom_ control in the [top toolbar](https://docs.cycling74.com/userguide/patcher_window/#top-toolbar).
  * Select _Zoom In_ from the _View_ menu to zoom in, or _Zoom Out_ from the _View_ menu to zoom out.
  * Press `z` to zoom in, or `shift``z` to zoom out.
  * Use the two finger "pinch" gesture to zoom in or out with precise control.


## Multiple Views
It's possible to open multiple views of the same patcher. This could let you view a patcher in patching and [presentation mode](https://docs.cycling74.com/userguide/patching/#presentation-mode) at the same time, or view a patch at two different zoom levels at once.
Create a new view of the current patcher using the _Patcher Window_ icon in the [_Bottom Toolbar_](https://docs.cycling74.com/userguide/patcher_window/#bottom-toolbar).
You can also create a new view of a [_bpatcher_](https://docs.cycling74.com/userguide/bpatchers/) by right-clicking the bpatcher and selecting `Object > New View` from the contextual menu.
![](https://docs.cycling74.com/images/4ca80c6a1f633599107b591399bec341_650.webp)
## Patcher Attributes
Behind the scenes, the patcher is a Max [object](https://docs.cycling74.com/userguide/objects/) like any other, and many aspects of the patcher can be controlled with [attributes](https://docs.cycling74.com/userguide/objects/#attributes).
  * Whether the patcher opens in presentation mode
  * The color of the patcher background
  * The spacing of the grid
  * Whether the [toolbars](https://docs.cycling74.com/userguide/patcher_window/) are pinned or unpinned


Access these patcher attributes by using the [patcher inspector](https://docs.cycling74.com/userguide/inspector/#the-patcher-inspector) in the Inspector sidebar.
## Key Commands
As you patch, you'll find there are several things that you'll do very frequently:
  * Creating a new object
  * Adding a comment
  * Showing a highlight
  * Viewing a list of recently created objects
  * Adding a button, slider, or toggle


All of these common actions have a **Key Command** associated with them. You can press a single keyboard key (`n` to make a new object, `r` to view recent objects, etc.) to perform the associated action. Most importantly, you can press `x` at any time to view a list of all available key commands.
![](https://docs.cycling74.com/images/2072edae4b9831d046b69591ffd461ab_327.webp) Press x anywhere in an unlocked patcher to view a list of key commands.
## Patching Mechanics
The Max patching interface supports a handful of useful shortcuts called Patching Mechanics. These are enabled by default, and you can toggle them on and off using the _Enable Patching Mechanics_ preference in [Max's preferences](https://docs.cycling74.com/userguide/preferences_and_settings/). These shortcuts make it easier to work with your patcher by reducing the amount of precise clicking needed to create and arrange objects. See [Patching Mechanics](https://docs.cycling74.com/userguide/patching_mechanics/) for more information.
## Finding Objects and Text
Select _Find..._ from the _Edit_ menu to search for text in your patcher. Max will display a search interface at the top of your patcher view.
![](https://docs.cycling74.com/images/051583db7b79903766af4d2206d00f6e_591.webp)
As you enter your search text, Max will show you all of the objects whose text matches your query. It can also identify objects that do not match in the current patcher, but which match in some [subpatcher](https://docs.cycling74.com/userguide/subpatchers/). Click on the _in a subpatcher_ text in the search interface to reveal the subpatcher with the matching object.
![](https://docs.cycling74.com/images/051583db7b79903766af4d2206d00f6e_591.webp) The 'effects' subpatcher contains a cycle~ object, so the search view indicates that there are additional matches within a subpatcher.
## Patching Margin
By default, Max will only allow scrolling only until the object in the bottom-right of your patcher is just in view. That means that even if the current view is full of objects, you won't be able to scroll to reveal more empty space.
![](https://docs.cycling74.com/images/ac2dfc903b178c69e488df14ec176293_592.webp) Even though the patcher view is full, there still aren't any scroll bars.
You might prefer to allow scrolling no matter what, so that you can always scroll in order to have more empty space to patch in. Enable the _Patching Margin_ icon in the [bottom toolbar](https://docs.cycling74.com/userguide/patcher_window/#bottom-toolbar) in order to add additional space to the patcher view to the bottom and right.
![](https://docs.cycling74.com/images/5d4b10c837c6665995126e19233b5974_592.webp) With Patching Margin enabled, scroll bars appear when in Edit Mode, giving you more room to patch in
## Reinitialize
You can bring a patcher back to an initial state by selecting _Reinitialize_ from the _Edit_ menu. This has two effects:
  * Sends a `loadbang` to the patcher, triggering any [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") objects in the patcher.
  * Resets all [parameters](https://docs.cycling74.com/userguide/parameter_mode/) to their initial value.


Reinitialize works especially well with patchers that take advantage of [parameter-aware](https://docs.cycling74.com/userguide/parameter_mode/) objects
