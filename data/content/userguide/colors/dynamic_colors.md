---
description: Dynamic colors automatically follow the active Max theme, so your interface
  can update its colors in different contexts.
group: Colors
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/dynamic_colors/
title: Dynamic Colors
---

# Dynamic Colors
**Dynamic Colors** automatically follow the active Max color theme, rather than remainining fixed. An object or a patcher can have a **Fixed Color** , like `1.0, 0.0, 1.0, 1.0`, which will not change when the current [**Color Theme**](https://docs.cycling74.com/userguide/color_themes/) changes. However, a color can also be specified by name. In this case, the actual color as it appears on screen is dynamic, and will change when the current color theme changes. You can get and set colors in the current theme using the [themecolor](https://docs.cycling74.com/reference/themecolor/ "themecolor") object.
## Max for Live
By default, dynamic colors are disabled for most Max objects, but are enabled for most Max for Live objects. When used in Max for Live, the dynamic colors of the Live category follow the active Live color theme as chosen in Live's Preferences. The Live dynamic colors and their values are also listed in the [live.colors](https://docs.cycling74.com/reference/live.colors "live.colors") object's help patcher.
## Selecting a Dynamic Color
### Using the Inspector
To set a dynamic color, open the [Inspector](https://docs.cycling74.com/userguide/inspector/) for an object and find the color attribute you want to change. Click in the value column to open the color picker. Select the _Dynamic_ tab at the top of the color picker.
![](https://docs.cycling74.com/images/6d2ea34ff82e8bd5c05f924468b1f910_413.webp)
Click the drop-down menu above the color swatch. From here you can select a color based on its dynamic color name. The first dropdown groups colors by category (e.g. Max Theme Colors, Inlet + Outlet), while the second dropdown lets you pick a specific color.
Hold `alt` (Windows) or `Option` (macOS) while clicking the dropdown to display the full range of available dynamic colors.
![](https://docs.cycling74.com/images/24e3d55aec9675ad8a3c655b5f00b491_291.webp) Dynamic color picker showing the colors for Inlets + Outlets
### Using a Message
Send an object a message like `elementcolor "Hot Inlet Circle Color"` to set the value of that attribute to a dynamic color. Since the name of a dynamic color might be multiple words, you may need to enclose the name of the dynamic color in quotes.
![](https://docs.cycling74.com/images/9d001fb3dc9d9cedb038758dda36cabc_266.webp) Someone set the elementcolor of this slider to be the same as a hot inlet.
A full overview of all Dynamic colors and their names can be found in the "view all" tab of the [themecolor](https://docs.cycling74.com/reference/themecolor/ "themecolor") object help patcher.
## Limitations
Dynamic colors do not work with [styles](https://docs.cycling74.com/userguide/styles/). Choosing a style to override a color will not shut off dynamic colors, and dynamic colors can not yet reliably be part of a style.
