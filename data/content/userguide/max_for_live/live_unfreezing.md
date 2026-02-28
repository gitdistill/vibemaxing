---
description: A guide on un-freezing Max for Live devices
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_unfreezing/
title: Unfreezing Devices
---

# Unfreezing Devices
Frozen devices cannot be edited. If you receive a frozen device from someone else that you'd like to edit, or you want to edit one of your own frozen devices, you'll need to unfreeze it first. To understand the unfreezing process, it helps to know what's in a frozen device.
  * The main device patcher file
  * Abstractions used by the device
  * Third-party Max external objects
  * Audio, image, and data files used by objects in the device
  * Files added as explicit dependencies of the device By contrast, an _unfrozen_ device contains only the main device patcher file. All the other files the device uses are expected to be somewhere in the Max [search path](https://docs.cycling74.com/userguide/search_path/).


The unfreezing process ensures that all files in the frozen device (other than the main patcher) exist in the search path. It is designed so that you will never lose data. If there are conflicts, you are forced to [resolve those conflicts](https://docs.cycling74.com/userguide/m4l/live_resolveconflicts/) before you can unfreeze.
## Rules for Unfreezing
Here is a description of what Max does during the unfreezing process.
  * If a file exists in both the frozen device and the search path, and the file is identical (same modification date and size), no action is taken. This is typically what happens if you create a device, freeze it, and then unfreeze it.
  * If a file exists in the frozen device but does not exist in the search path, it is written to a subfolder (named after the device) of the Unfrozen Max Device Files folder in the Desktop folder. This might happen if you receive a frozen device from someone else and want to unfreeze it in order to modify it.
  * If a file exists in both the frozen device and the search path, but the file is different, then Max will take one of two actions depending on how you have chosen to resolve the conflict. An example file conflict is shown below.
  * If you choose **Use Device Version** , the version in the search path will be moved to a Discarded Files subfolder of the device's subfolder of the Unfrozen Max Device Files folder. Then the version of the file in the device will be written to the device's subfolder of the Unfrozen Max Device Files folder.
  * If you choose **Use Disk Version** , the version in the frozen device will be written to a Discarded Files subfolder of the device's subfolder of the Unfrozen Max Device Files folder. The version in the search path will be left untouched.


Discarded Files folders are not in the search path. However, subfolders created when unfreezing devices are in the search path. When Max starts up, it looks for the Unfrozen Max Devices Folder, then adds any folders only one level below to the search path. This is different from the way the search path is typically constructed by recursively adding all subfolders of folders you have specified.
