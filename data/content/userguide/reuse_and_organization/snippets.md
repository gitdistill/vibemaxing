---
description: Create small, reusable collections of objects called snippets
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/snippets/
title: Snippets
---

# Snippets
A **Snippet** is a small group of objects, saved in a special format for easy reuse. You can create snippets from parts of a patcher that you find yourself using often, saving you the trouble of having to recreate the objects and connections from scratch.
![](https://docs.cycling74.com/images/9c290b80c0c43f005626b84fe525a756_235.webp) A snippet for a basic video display patch.
## Creating Snippets
Select the objects you'd like to include in a snippet. Click the _Save Snippet_ button in the bottom toolbar.
![](https://docs.cycling74.com/images/cb49ecabea210f091c79f904501a55c4_866.webp)
## Using Snippets
A dialog will appear, letting you name your snippet. Once you've saved your new snippet, you'll be able to add it to any patcher either [using the contextual menu](https://docs.cycling74.com/userguide/snippets/#via-the-contextual-menu) or [using the left sidebar](https://docs.cycling74.com/userguide/snippets/#via-the-left-sidebar).
## Adding Snippets to a Patcher
### Via the contextual menu
Right- or control-click an unlocked patcher where you'd like to paste your snippet. A contextual menu will appear. Select `Paste From > User Snippets` then choose the desired snippet from the submenu.
![](https://docs.cycling74.com/images/bff49869c38fa8fdf69a096d37576f38_637.webp)
The `Paste From` menu also lets you quickly add patchers and snippets from installed packages.
### Via the left sidebar
Click on the _Snippets_ tab in the left sidebar to open the _Snippets_ browser.
![](https://docs.cycling74.com/images/07489e5c48fbb6f74de067d7de01ee96_340.webp) Click to open the Snippets browser
The _Snippets Browser_ lets you browse snippets my name or by preview image. When viewing snippets by name, use the left column to filter by [**package**](https://docs.cycling74.com/userguide/packages/). When viewing by preview image, use the pop-up menu to filter by package. To filter snippets by name, use the **filter** text entry field at the top of the browser.
To add a snippet to your patcher, just drag it from the browser and drop it into an unlocked patcher.
![](https://docs.cycling74.com/images/15d1bd84dd5b0aa722c43a82396361e4_424.webp)
## Snippet Location
Snippets are saved in the _Snippets_ folder inside the [**Max 9**](https://docs.cycling74.com/userguide/search_path/#max-9-folder) folder. Snippet files have the `.maxsnip` extension. They are `.maxpat` format files that include a preview image.
You can add regular Max patcher files to the _Snippets_ folder as well. This will add that patcher to the `Paste From` section of the context menu.
## Using Snippets with Packages
[Packages](https://docs.cycling74.com/userguide/packages/) can include snippets as well. If you're authoring a package, either for your own use or for distribution through the [**Package Manager**](https://docs.cycling74.com/userguide/package_manager/), you can add snippets to your package. Create a folder called `Snippets` inside your package folder, and put whatever `.maxsnip` and `.maxpat` files you like into that folder.
