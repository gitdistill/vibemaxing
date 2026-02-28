---
description: Properties and behavior of MC patch cords
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_patchcords/
title: MC Patchcords
---

# MC Patch Cords
MC patch cords carry multiple channels of audio simultaneously. This makes it easier to work with audio spatialization, complex synthesis voicings and explicitly polyphonic signals.
A patch cord will be multi-channel if it is connected to a multi-channel outlet of an MC object.
These patch cords have a distinctive appearance: they are blue and black (as opposed yellow and black single-channel patch cords). MC patch cords are also slightly thicker. You can quickly see how many channels are being used by hovering over the patch cord when the patcher is unlocked.
![](https://docs.cycling74.com/images/4c38a535f913144c91e9b781a858efd5_165.webp)
## Auto-Adding Multi-Channel Signals
With single-channel patch cords, connecting two signals into a single object inlet will _add_ the two signals before they are received by the object.
With multi-channel patch cords, this auto-adding also occurs, but it is more complex when the incoming multi-channel patchcords contain different numbers of channels.
When multi-channel signal patchcords are connected to a single inlet, the resulting signal will contain the number of channels from the patch cord with the greatest number of signals.
![](https://docs.cycling74.com/images/5a00ce46380fae0934c589002d1b61a1_281.webp)
