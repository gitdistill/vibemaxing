---
description: Special coloring for different parts of an object box should make it
  easier to identify the functionality of a patcher
group: Colors
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/syntax_coloring/
title: Syntax Coloring
---

# Syntax Coloring
**Syntax Coloring** uses different colors for a word or number based on the type of token it is in a programming or data description language. Most modern text editors used for programming feature syntax coloring and Max is no exception. The standard text window will adjust text colors based on the [theme](https://docs.cycling74.com/userguide/color_themes/) and file type. Here are some examples:
![](https://docs.cycling74.com/images/ad82b9dfa15a943e8609023067c9352d_445.webp) JavaScript in the **default** theme ![](https://docs.cycling74.com/images/507b07e2b65453504759f3eaed4ecab5_392.webp) Dictionary Editor in the midlight-ash theme
## Enabling Object Box Syntax Coloring
To apply syntax coloring to the text in object boxes in a patcher, enable **Syntax Coloring** in the **Color and Theme** tab of the Preferences window.
![](https://docs.cycling74.com/images/bc2795a23881b151e8ee7df70b8d1f8a_478.webp)
This applies the current theme's syntax colors to object box text.
![](https://docs.cycling74.com/images/5a88483f5ea3f3aa3e91f9e1db57f50f_401.webp)
In the above example, four colors are used to color the text of object boxes.
  * the first word in the object box is the _object name_

![](https://docs.cycling74.com/images/adf7ecc971bfd457ce8c2dc9ba7c49d8_63.webp)
  * words starting with **@** are _attribute names_

![](https://docs.cycling74.com/images/25b1a9377edd44383e29de5736f84081_95.webp)
  * words or numbers after the object name but before the typed-in attributes are _object arguments_

![](https://docs.cycling74.com/images/8e5280ab118dbe1c4be9454bdff8b47c_45.webp)
  * words or numbers after the object name but before the typed-in attributes are _attribute arguments_

![](https://docs.cycling74.com/images/3775a6b741555f1cff10e0b971958f36_87.webp)
## Customizing Object Box Syntax Colors
You can override object box syntax colors set by themes in two ways:
  * Select a **Syntax Color Theme** other than _Theme Default_ in the **Color and Theme** tab of the Preferences window.

![](https://docs.cycling74.com/images/e86ac9f7193343bad24ee8fa7b2c0554_268.webp)
The various themes in the menu will not be equally legible with all themes, but they may work better for you than the default theme colors. Here's the **olivia** Syntax Color Theme used with the **default** Color Theme.
![](https://docs.cycling74.com/images/3cd48c8aed7eef77c115a94cb1a6b204_380.webp)
Note that Syntax Color Themes typically change only the four object box text colors, not the text editing window colors.
  * On a per-patcher basis, you can edit the four object box syntax colors in the [Format Palette](https://docs.cycling74.com/userguide/format_palette/) for the patcher. With no objects in the patcher selected, show the Format Palette and click the P icon at the far left.

![](https://docs.cycling74.com/images/5dd6e7eb3f6d18038597ce06369f2948_42.webp)
The Format Palette shows the default object, background, and text colors for the patcher. You'll want to locate the four **A** icons to the edit the syntax colors, Syntax Attribute Argument Color, Syntax Attribute Name Color, Syntax Object Argument Color, and Syntax Object Name Color.
![](https://docs.cycling74.com/images/83664bba56601e703d95254ace73ceaa_169.webp)
It's helpful to edit these colors with object boxes showing the various syntax elements in the patcher visible.
Once changed, the customized colors will apply to all object boxes in a patcher (but not its subpatchers). To apply your customized colors more easily to new patchers, you can save the patcher as a [template](https://docs.cycling74.com/userguide/templates/).
To apply the syntax colors to existing patchers, define a patcher-level [style](https://docs.cycling74.com/userguide/styles/). Choose **Define New Style** from the Style menu in the [Format Palette](https://docs.cycling74.com/userguide/format_palette/) when editing the patcher fonts and colors.
