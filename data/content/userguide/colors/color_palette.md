---
description: How to select and edit colors in Max, and the difference between fixed and dynamic colors
group: Colors
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/color_palette/
title: Color Palette
---

# Color Palette
The **color palette** lets you select and edit colors used by Max objects. There are two types of colors used in Max, **fixed** and [**dynamic**](https://docs.cycling74.com/userguide/dynamic_colors/). Fixed colors are specified by RGB color values -- for example, black is 0, 0, 0 -- while dynamic colors are specified by name, and may change dynamically when the Max or Live theme changes.
You can use the color palette to select either fixed and dynamic colors. Certain color attributes in Max objects can also be specified as gradients -- continuous transitions between two fixed colors.
## Displaying the Color Palette
The color palette can be accessed in two places, the [Inspector](https://docs.cycling74.com/userguide/inspector/) or the [Format Palette](https://docs.cycling74.com/userguide/format_palette/).
### Colors in the Inspector
With a user interface object such as a [button](https://docs.cycling74.com/reference/button/ "button") or [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") selected, open the Inspector. You'll see some color attributes:
Click any of the color swatches next to the name of the attribute. The Color Palette will open.
![](https://docs.cycling74.com/images/fb254b0600ba67168def8fedba8a2770_205.webp)
### Colors in the Format Palette
Select a user interface object, then click the format palette icon in the top toolbar.
![](https://docs.cycling74.com/images/676dcc9afa316eb887a0919402a9dfe1_416.webp)
The format palette will open. Click any of the colors shown, and the color palette will drop down to edit that color.
![](https://docs.cycling74.com/images/02921af46bed9e01fc0990b5d3fc9518_206.webp)
## Picking a Fixed Color
Select the _Fixed_ tab at the top of the color palette if it is not already showing.
![](https://docs.cycling74.com/images/515d3e9bed5eb52024cfee70390a3146_63.webp)
The top control shows the current color within a hue space.
![](https://docs.cycling74.com/images/49809dee345cacd7b1113804b7516390_206.webp)
The middle control shows the current color within a brightness and saturation space. Click and/or drag in either space to modify the current color. The Max object's color changes as you drag.
Below the color editors, you'll find some _variation controls_. By default, the chosen variation is _mix with black_. When you click on _mix with black_ , you'll see a menu with other color variations.
![](https://docs.cycling74.com/images/e24e47bf5d7f7b42445eae2c911975c0_124.webp)
Here's Pentad, which creates five variations of the selected color according to hue.
![](https://docs.cycling74.com/images/18e0d6d28f974ec48cba613de9c25e93_199.webp)
Click on any color variant to make it the selected color.
If you're not happy with your changes, choose _Undo_ from the Edit menu to go back to the previously chosen color.
## Managing Color Collections in Palettes
Below the color variation control, there is a 10 x 3 grid of squares. By default, the grid is empty, ready for you to save your own colors. As you move the mouse over an empty square, a plus sign appears. Click in a square to save the current color in a palette.
![](https://docs.cycling74.com/images/915022450c41e63f7013f8ca90b2e136_199.webp)
To save the current color over an existing color, hold down the shift key and click on the color you want to replace.
There are three **user palettes** for storing your own color collections. You don't need to save changes to the palette; the updated colors will be loaded every time you launch Max.
### Saving Palettes
To export the current state of a user palette for sharing, click on the current palette name (`user palette 1` for example), then choose _Export user palette 1..._ from the menu. Files are saved with the extension `.maxpalette`.
### Built-in Palettes
The palette menu beneath the grid lists about a dozen read-only paletes built into Max. Choosing a named palette will replace the colors in the grid.
### Importing Palettes
To import previously exported palette, choose _Import..._ from the palette menu and select the desired `.maxpalette` file.
## Using Dynamic Colors
**Dynamic colors** are named elements of [color themes](https://docs.cycling74.com/userguide/color_themes/) you can use to ensure the user interface elements in your patchers or Max for Live devices are coordinated with the larger environment. When the user changes the theme, dynamic colors update to reflect the color values in the theme.
The [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") object as well as other UI objects whose names begin with `live` use dynamic colors within a Live theme so'll they'll fit in with the rest of the Live UI. You can assign dynamic colors to any object however.
## Using the Dynamic Color Picker
Click on the _Dynamic_ tab of the color palette.
If the current color is already dynamic, it will be highlighted within its color set (for example, _Max Theme Colors_). If the current color is fixed, the _Live Theme Colors_ will be shown. As you mouse over the grid of colors, you'll see the color name displayed above the grid. Click on a color to choose it.
![](https://docs.cycling74.com/images/41baf2b5a2a3d807a8a3d4847804a1f7_205.webp)
If you prefer to choose the dynamic color by name, click on the name above the grid to see a menu of all colors in the set by name.
### About Live Colors
There are about 70 entries in the set of Live Theme Colors. The menu can be a bit overwhelming, so it can help to learn the most commonly used colors in objects. [live.dial](https://docs.cycling74.com/reference/live.dial "live.dial") makes use of 11 colors of which the following are significant:
  * **Control Range On** -- the range of the control when active
  * **Control Range Off** -- the range of the control when inactive
  * **Control On** or **Control On Variant** -- the control's value when active
  * **Control Off** -- the control's value when inactive
  * **Border Color (Focus)** -- the border around the control when it has keyboard focus
  * **Control Needle On** -- the control needle when active
  * **Control Needle Off** -- the control need when inactive
  * **Text Color** -- the text color


Many of the other theme colors in the menu are used in the Live UI for indicating selection or a special modes, so they could potentially be confusing if used for controls in a UI.
## Exploring Other Color Sets and Themes
To choose another set of dynamic colors, click _Live Theme Colors_ and choose a set from the menu.
![](https://docs.cycling74.com/images/aaa1d41f27a9e82e7602c934927e2851_132.webp)
Most of the time you'll want to use either Live Theme Colors or Max Theme Colors; these two items appear at the top of the menu. The other sets represent different colors used in the Max interface. For example, _Max Console_ is the collection of colors used to display text and backgrounds in the [Max Console](https://docs.cycling74.com/userguide/max_console/).
### Using Gradients
A small number of Max user interface object background colors can be specified as gradients. The background of a [message](https://docs.cycling74.com/reference/message/ "message") box is one example. The **Gradient** editor in the color panel is only available if the color you're editing can be a gradient.
To use the gradient editor:
  * Make a new [message](https://docs.cycling74.com/reference/message/ "message") box
  * Show the inspector for the message box
  * Click on the color swatch for `Background Color` to edit it. The color palette is in gradient mode.

![](https://docs.cycling74.com/images/c36f4b05f01fdd3e925e5f2d182ef8ab_398.webp)
The gradient editor has three components. First, you can change either of the two colors that make up the gradient using the _active edit color selection_ :
![](https://docs.cycling74.com/images/5b5c64ff033e369e4f432a3471503cf6_65.webp)
Second, you can edit the gradient parameters by clicking on the pencil icon.
![](https://docs.cycling74.com/images/b52c804e6fecc27b2bb053b77e9d5f88_27.webp)
The gradient editor will appear.
![](https://docs.cycling74.com/images/d8576b10323bc95c35dcf06bfac494d4_205.webp)
The following animation demonstrates the basic operation of the gradient editor, setting the gradient angle, the blend point, and the size of the blend region.
![](https://docs.cycling74.com/images/4d25acfbc24b19e25c99fe20db3f2db6_120.webp)
With gradient compatible background color attributes, you're not obligated to use a gradient.
To switch to a solid color, click on _Gradient_ and choose _Color Fill_ from the menu.
![](https://docs.cycling74.com/images/c6e2cb40607ce47a366d95876d93d8f7_97.webp)
## Using the Color Picker
A final option for editing fixed colors is the standard _Color Picker_ accessed by clicking the circular color icon near the top of the color palette.
![](https://docs.cycling74.com/images/c376e41c0ce593efb6da7031915b2f35_69.webp)
## Copying and Pasting Colors
To moving color values from the color palette to other applications, click **#** above the color grid.
![](https://docs.cycling74.com/images/f412fc99393313ce07039d0d8cdb1d61_254.webp)
You can Copy the current color to the clipboard in either hex (_Copy Hex Value_) or float (_Copy Float Value_).
To import a color value into the color palette from another application, choose _Paste_. The color palette accepts values as four floating-point numbers or a hex string, which can optionally be preceded by a pound sign (`AEFC06` or `#AEFC06`).
