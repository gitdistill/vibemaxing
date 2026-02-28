---
description: Convenient features that make it easier to work with objects and patch cords
group: Patching
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/patching_mechanics/
title: Patching Mechanics
---

# Patching Mechanics
The Max patching interface supports a handful of useful shortcuts called Patching Mechanics. These are enabled by default, and you can toggle them on and off using the _Enable Patching Mechanics_ preference in [Max's preferences](https://docs.cycling74.com/userguide/preferences_and_settings/). These shortcuts make it easier to work with your patcher by reducing the amount of precise clicking needed to create and arrange objects.
## Drag to create new objects
With the patcher unlocked, hold down `Shift``Alt` and drag an object to instantly create a new object connected to the first.
![](https://docs.cycling74.com/images/dce87b316b3fa1f2fcae49c8b375955c_320.webp)
## Create a new object along a patch cord
With a patch cord selected, press `Shift``n` to create a new object and insert it into the selected patch cord.
![](https://docs.cycling74.com/images/5f830bd0335fe173ca0c9f52b8ebe54f_320.webp)
## Insert and remove an object from a patch cord
Hold down `Shift` and drag an object into an existing patch cord, aligning its first inlet with the patch cord. Max will insert the selected object into the patch cord, replacing its existing connection. In the same way, hold down `Shift` and drag an object out of a patch cord to remove that object from the connection. Max will replace the connection with the selected object removed.
![](https://docs.cycling74.com/images/951a9e5cd1445b37b0414c9b9b9d3965_320.webp)
## Navigating the patcher selection with the keyboard
With an object selected, you can press `Alt``Up` to select a patch cord leading into the object. Pressing `Alt``Down` moves the selection to patch cords coming from the object. Then, `Alt``Left` and `Alt``Right` rotate your selection through patch cords.
![](https://docs.cycling74.com/images/9a92bbcc29ec72478ff45a19a41f2ea3_320.webp)
