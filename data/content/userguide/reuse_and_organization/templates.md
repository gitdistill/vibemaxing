---
description: A template is a starting point for a Max patcher, which you can save and make into the default
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/templates/
title: Templates
---

# Templates
Templates are a starting point for a Max patcher. You can save any patcher as a template, and then rather than starting from a blank patcher, you can use your saved patcher as a starting point. Templates maintain [patcher-level formatting](https://docs.cycling74.com/userguide/format_palette/#patcher-level-formatting) including fonts and colors, so if you create a template with a patcher [style](https://docs.cycling74.com/userguide/styles/), the style will be included in your template.
## Using Templates
Select _New From Template_ from the _File_ menu to see a list of saved templates, including built-in templates. Choose a template from the list and it will open in a new patcher window.
## Creating Templates
To create a template from a Max patcher, choose _Create Template..._ from the _File_ menu. A dialog box will appear that contains the name of a Max template file (the default filename will be based on the filename of the currently open Max patch).
![Max patcher with a modal dialog revealing asking for the name of the new template](https://docs.cycling74.com/images/a722a862e63f7026892be63ef648a21a_718.webp) The modal dialog asks for a name for the new template.
## Default Template
You can choose a template to be the **default template** for the whole Max application. Once you do, any new patcher that you create will be based on that template, rather than the typical empty patcher.
### Setting a new default template
When you save a new template, you can check the `Default for New Patchers` checkbox to make the saved template the new default.
![](https://docs.cycling74.com/images/f60610e1e9baa7a535e9e3590cbab9b0_503.webp)
If you want to make an existing template the default, set the _Default Patcher Template_ preference in the _Preferences_ window. See the [Default Patcher Template](https://docs.cycling74.com/userguide/preferences_and_settings/#files-and-folders) section in the Preferences reference for details.
## Templates in Packages
If you're authoring a [**Package**](https://docs.cycling74.com/userguide/packages/), whether for your own use, to share with your colleagues, or to publish to the [**Package Manager**](https://docs.cycling74.com/userguide/package_manager/), you can include templates in that package as well. This can be really useful, for example as a way to demonstrate the functionality of your package.
To add a template to your package, create a folder called `templates` in your package folder. Any `.maxpat` files that you put in this folder will be available as templates. Once someone installs your package, they should see your custom templates listed in the dropdown whenever they choose `File > New From Template`.
