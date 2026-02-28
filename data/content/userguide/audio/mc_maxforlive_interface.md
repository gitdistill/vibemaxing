---
description: Working with MC in Max for Live
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_maxforlive_interface/
title: MC and Max for Live
---

# MC and Max for Live
Max for Live devices receive audio input via [plugin~](https://docs.cycling74.com/reference/plugin~/ "plugin~") and send audio to Live via [plugout~](https://docs.cycling74.com/reference/plugout~/ "plugout~"). The mc.plugin~ and mc.plugout~ versions of these objects accept multi-channel inputs and outputs to be routed to and from Max for Live.
![](https://docs.cycling74.com/images/75ee659ac25c552a3af5807029a027fc_299.webp)
Devices created with multi-channel inputs and outputs will support multichannel routing within Live, as well as having the appropriate number of inlets and outlets when loaded into Max within the [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object. The current maximum channel count is 64.
