---
description: Create and manage user interfaces in Max for Live devices
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_userinterfaces/
title: User Interfaces in Max for Live
---

# User Interfaces in Max for Live
## Device Width and Height
By default, the _width_ of a device created in Max for Live is based on the contents of your device patcher. It will be slightly wider than the visible objects in your device. Alternatively, you can explicitly define the width of your device to any size. If you change your mind, you can always reset the device width to the default behavior. The _height_ of all Live devices is fixed at 169 pixels.
## Defining a Fixed Device Width
  * While your Max for Live device patcher window is open for editing, resize the window to be desired width you would like to see in Live.
  * Choose **Set Device Width** from the View Menu.
  * If desired, you now can resize the patcher window to a size convenient for editing. You will see a vertical line indicating the fixed width of the device. The width will update in Live the next time you save the device.


## Using a Dynamic Device Width
  * While your Max for Live device patcher window is open for editing, choose **Clear Device Width** from the View Menu. The next time you save the device, the width in Live will be determined by the contents of your patcher.


## Using Presentation Mode
Once you have your Max device up and running, you may want to present the user with only the user interface objects. Given the relatively small height of the Live Device view, it may be desirable to think of your interface separately from the logical position of the user interface objects in your patcher.
## Creating a Presentation
  * In the unlocked Patcher window for your Max for Live device patch. select the user interface objects you want to be visible in the Device Window by shift-clicking to select them.
  * Choose **Add to Presentation** from the Max for Live Object menu to add the objects to the Presentation layer. A pink border will appear around the object(s) you have selected.
  * Click the Presentation Mode button in the patcher toolbar to enter Presentation mode. When you switch to Presentation Mode, only objects you have added to the Presentation layer will be shown and the word **(presentation)** will appear in the title bar of the patcher window.
  * While in Presentation Mode, you can reposition and change the color of user interface object, and also use resizing handles to change the size of some user interface objects (if an object can be resized, it will had resizing handles.
  * When you are satisfied with the layout of your user interface, choose **Patcher Inspector** from the Max for Live View menu.
  * Check the `Open in Presentation` attribute.


