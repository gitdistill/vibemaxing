---
description: Properly utilising symbols unique to Max for Live
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_symbols/
title: Using Symbols in Max for Live
---

# Using Symbols in Max for Live
The "name space" in Max is global - when you have objects that have names associated with them such as [coll](https://docs.cycling74.com/reference/coll/ "coll"), [send](https://docs.cycling74.com/reference/send/ "send"), [receive](https://docs.cycling74.com/reference/receive/ "receive"), [table](https://docs.cycling74.com/reference/table/ "table"), or [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), you can share data between Max for Live devices. In these cases, the Max name space is shared, but the "signal processing space" is independent - each Max for Live device processes its audio or data separately.
## Defining a unique symbol name
If you want a named object to be unique to a device, use three dashes (**---**) to start the name of your [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") or [send](https://docs.cycling74.com/reference/send/ "send") / [receive](https://docs.cycling74.com/reference/receive/ "receive") destination (e.g. `s ---filtercutoff`).
When your patch is initialized, it will replace the three dashes with a unique-to-Live number (e.g. `s 024filtercutoff`);
