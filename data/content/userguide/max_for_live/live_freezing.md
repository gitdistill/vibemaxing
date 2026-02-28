---
description: A guide on freezing Max for Live devices
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_freezing/
title: Freezing Max for Live Devices
---

# Freezing Max for Live Devices
_Freezing_ a Max device prepares it for distribution. A frozen device contains files it needs to operate. These files might include subpatchers, audio files, image files, Javascript code, or third-party Max external objects. When you freeze a device that contains third-party external objects, you can include both Windows and Macintosh versions of the external in your Max search path, if you have them both. The frozen device will then will contain both versions, and will work on both platforms. Max analyzes your device to find any files it uses (called dependencies), and then combines these files with your device. When a frozen device is opened, the files inside the device are used, even if similarly named files reside on your disk in the Max [search path](https://docs.cycling74.com/userguide/search_path/).
## Freezing a Device
  * Click the Freeze button in the device window toolbar.


  * Choose **Save** from the File menu to save the device. The device is now frozen and is reloaded in Live in its frozen state.


Note that the device is not frozen immediately when you click the freeze button. It is frozen when you save it. Before saving, you can make further changes to the device after clicking the Freeze button by clicking the Freeze button again to unfreeze. When your changes are finished, click the Freeze button again, then choose **Save** from the File menu.
