---
description: Create a named configuration of a UI object that can be recalled later
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/prototypes/
title: Prototypes
---

# Prototypes
**Prototypes** are configurations of object attributes that can be saved and recalled later. For example, you might have an object like a [slider](https://docs.cycling74.com/reference/slider/ "slider") that you've set up to have a certain size and to look a certain way. You could define a prototype from that slider, and then apply that prototype to make other sliders look the same way.
Prototypes are mostly used with UI objects, but you can use them for generic Max objects as well. For example, you might have a Jitter object with a complex state that you find yourself reusing often.
## Defining a Prototype
With an object selected, open the _Object_ menu and select `Save Prototype...` to define a new prototype. A dialog box will appear, allowing you to give the prototype a name.
![](https://docs.cycling74.com/images/d7406f1bc67617a208aca281dcb9efa5_518.webp) Defining a new prototype
## Applying a Prototype
Select the object to which you'd like to apply your prototype. Open the _Object_ menu and choose `Prototype > <name>`, where `<name>` is the name of your saved prototype. The object should change its text and/or appearance to match your saved prototype.
## Deleting a Prototype
Max prototypes are stored in files with the `.maxproto` extension. You can find these files the `Prototypes` folder in the [**Max 9 Folder**](https://docs.cycling74.com/userguide/search_path/#max-9-folder), which on macOS is in `~/Documents/Max 9` and on Windows is in `%USERPROFILE%\Documents\Max 9`. If you delete a `.maxproto` file from the `Prototypes` folder, it will no longer appear in the list of prototypes for the specified object.
## Prototypes in Packages
To include a prototype as part of a [Package](https://docs.cycling74.com/userguide/packages/), create a folder in your package directory named `prototypes`, and put any `.maxproto` files that you want to include into that directory. When a user installs your package, those prototypes will be available to them as well. This can be useful if your package has a consistent look and feel that you want to enable other users to reproduce.
