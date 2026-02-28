---
description: Combine multiple signal channels into one patch cord, and use mc objects to process signals in parallel
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/
title: MC
---

# MC
**MC** supports multiple channels of audio in a single patchcord. It also allows standard Max audio objects to operate on many channels of audio at the same time.
Signal [visualization](https://docs.cycling74.com/userguide/mc/mc_visualization/) objects such as [meter~](https://docs.cycling74.com/reference/meter~/ "meter~") and [scope~](https://docs.cycling74.com/reference/scope~/ "scope~")will adapt themselves to multichannel input signals.
The [MC Wrapper](https://docs.cycling74.com/userguide/mc/mc_wrapper/) holds multiple instances of Max audio objects in a single object box. Wrapped object names start with **mc** , for instance [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~") is the MC-wrapped [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object. The wrapper also offers many powerful features for controlling multiple objects.
In addition to MC wrapper objects, [MC-specific objects](https://docs.cycling74.com/userguide/mc/mc_signals_newobjects/) aid in multichannel signal manipulation.
## Topics
  * [Spatialization](https://docs.cycling74.com/userguide/mc/mc_spatialization/) - Working with multiple channels over multiple speakers or output channels
  * [Polyphony](https://docs.cycling74.com/userguide/mc/mc_polyphony/) - Managing polyphony with MC
  * [Gen](https://docs.cycling74.com/userguide/mc/mc_gen/) - MC and Gen
  * [Events](https://docs.cycling74.com/userguide/mc/mc_events_newobjects/) - Events and MC objects
  * [Mixing and Panning](https://docs.cycling74.com/userguide/mc/mc_mixing_panning/) - Up- and down-mixing, multi-speaker panning, and signal routing
  * [Plug-ins](https://docs.cycling74.com/userguide/mc/mc_plugins/) - Hosting plug-ins in MC
  * [Dynamic Routing](https://docs.cycling74.com/userguide/mc/mc_dynamic_routing/) - Sending multi-channel signals to different places


