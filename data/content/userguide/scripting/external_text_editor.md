---
description: How to configure Max to use an external text editor, rather than the built-in editor
group: Scripting
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/external_text_editor/
title: External Text Editor
---

# External Text Editor
Objects like [coll](https://docs.cycling74.com/reference/coll/ "coll"), [js](https://docs.cycling74.com/reference/js/ "js"), [jsui](https://docs.cycling74.com/reference/jsui/ "jsui"), and [node.script](https://docs.cycling74.com/reference/node.script "node.script") have an internal state that references a body of text. For editing the state of these objects, Max has a built-in text editor. However, you can also use an external text editor if you prefer.
## Editing an Object's Text
For any objects that have some internal text, you can open the text editor for that object by double-clicking on the object. There's also a menu command to open the text editor. For example, with a [coll](https://docs.cycling74.com/reference/coll/ "coll") object selected, choose _Edit coll Object's Contents_ from the _File_ menu to open the text editor. By default, this will use Max's internal text editor.
![](https://docs.cycling74.com/images/9cfaa0cf0f3cd13bcc4b87490412f61b_323.webp)
## Using an External Editor
To use an external editor, open [Max's preferences](https://docs.cycling74.com/userguide/preferences_and_settings/) and enable _Always use External Text Editor_.
![](https://docs.cycling74.com/images/23958b38fa94a409db3c46b1895fa2fd_457.webp)
With this option enabled, Max will use whatever text editor application is the system default when opening a given file. If you set a value for "External Text Editor", them Max will always use that application when opening a text file.
![](https://docs.cycling74.com/images/8682a0f7fcc6ef71750baa7438ad087b_457.webp)
## Required File on Disk
If you've enabled _Always use External Text Editor_ , you may see a dialog appear when you try to open up a text-based object for editing.
![](https://docs.cycling74.com/images/c0ce57756011a259ba1cb3ee30ef1ad0_506.webp)
When using Max's internal text editor, Max can display the contents of an object as text without creating an actual file on disk. However, when using an external text editor, Max must save an actual file before it can open the object contents with an external editor. Choose "Yes" to save a file on disk. After creating the file, Max will open the file in your chosen external text editor.
