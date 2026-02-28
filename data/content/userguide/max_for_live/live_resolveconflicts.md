---
description: Understand how to manage conflict resolution with device dependencies when freezing
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_resolveconflicts/
title: Resolving Conflicts in Frozen Devices
---

# Resolving Conflicts in Frozen Devices
The process of [freezing](https://docs.cycling74.com/userguide/m4l/live_freezing/) adds copies of files in the Max [search path](https://docs.cycling74.com/userguide/search_path/) to the device file. Consider the example shown below. A Max device called MyEffect contains an abstraction called _pumper_.
![](https://docs.cycling74.com/images/64b60a3e41bcbf7eab589b64140d76cc_350.webp)
If we freeze this device and save it, a copy of the pumper patcher file will be added to the device. If we now open pumper, modify it, and save the changes, the frozen device is unaffected. However, what happens if we decide we want to work on our MyEffect device some more? At this point, there are two different versions of Pumper, the one in the device, and the one saved on disk. Which one should we use?
## Overview of the Conflict Resolution and Unfreezing Process
Whenever you edit a frozen device, Max compares the files in the device with the versions on disk. If it spots differences, it disables the [unfreeze icon](https://docs.cycling74.com/userguide/m4l/live_unfreezing/) and unlock icons in the patcher toolbar and enables the resolve conflicts icon, as shown below.
![](https://docs.cycling74.com/images/443f68d8edda12cd9484200e6e4a0014_95.webp)
Before you can unfreeze a device with conflicts, you'll need to resolve them. Once you have decided which file(s) you wish to work with, both the version you want to keep _and_ the version you want to discard will be written into a special folder located in your computer's Desktop folder called Unfrozen Max Device Files. However, only the version you wish to keep will be in the search path. The other version is put into a Discarded folder that is kept out of the search path.
## Resolving Conflicts for a Frozen Device
  * Click the Resolve Conflicts icon in the patcher toolbar. The Resolve Conflicts window will open.
  * Use the Action pop-up menu for each listed file with a conflict to choose which version you wish to use.
  * Once all conflicts have been resolved, the icon in the patcher window toolbar will turn gray, its caption will indicate No Conflicts, and the Unfreeze icon will become enabled.
  * Click the [Unfreeze](https://docs.cycling74.com/userguide/m4l/live_unfreezing/) icon in the patcher window toolbar to unfreeze the device.


