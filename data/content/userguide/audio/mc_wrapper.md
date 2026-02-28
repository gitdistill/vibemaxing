---
description: The permits you to control all of the objects at once with one message or target individual objects.
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_wrapper/
title: MC Wrapper
---

# MC Wrapper
When you type [mc.cycle~](https://docs.cycling74.com/reference/mc.cycle~ "mc.cycle~") into an object box, one or more traditional [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") objects are embedded inside the **MC Wrapper**.
The wrapper holds multiple instances of audio objects such as [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~"). It permits you to control all of the objects at once with one message or target individual objects. It also manages multi-channel connections to other MC objects. For the most part, this is done transparently and you don't have to think about the wrapper too much. But wrapped objects share some [useful messages and attributes](https://docs.cycling74.com/userguide/mc/mc_messages_to_wrapper/) not availble in the "unwrapped" versions.
A general rule of thumb is that if there is an MSP object xxx~, mc.xxx~ will be xxx~ in the MC Wrapper. But this is not always the case. Exceptions include:
  * Objects that perform I/O: [mc.adc~](https://docs.cycling74.com/reference/mc.adc~ "mc.adc~"), [mc.dac~](https://docs.cycling74.com/reference/mc.dac~ "mc.dac~"), [mc.ezadc~](https://docs.cycling74.com/reference/mc.ezadc~ "mc.ezadc~"), [mc.plugin~](https://docs.cycling74.com/reference/mc.plugin~ "mc.plugin~"), [mc.plugout~](https://docs.cycling74.com/reference/mc.plugout~ "mc.plugout~"), [mc.ezdac~](https://docs.cycling74.com/reference/mc.ezdac~ "mc.ezdac~"), [mc.sfplay~](https://docs.cycling74.com/reference/mc.sfplay~ "mc.sfplay~"), and [mc.sfrecord~](https://docs.cycling74.com/reference/mc.sfrecord~ "mc.sfrecord~"). In these cases, you don't need multiple copies of objects, you just need multi-channel inputs and outputs to the outside world
  * UI objects including gain sliders ([mc.live.gain~](https://docs.cycling74.com/reference/mc.live.gain~ "mc.live.gain~"), [mc.gain~](https://docs.cycling74.com/reference/mc.gain~ "mc.gain~"), [mc.multigain~](https://docs.cycling74.com/reference/mc.multigain~ "mc.multigain~")) and [signal visualization objects](https://docs.cycling74.com/userguide/mc/mc_visualization/) including [scope~](https://docs.cycling74.com/reference/scope~/ "scope~"), [meter~](https://docs.cycling74.com/reference/meter~/ "meter~"), [levelmeter~](https://docs.cycling74.com/reference/levelmeter~/ "levelmeter~") and [spectroscope~](https://docs.cycling74.com/reference/spectroscope~/ "spectroscope~"). The **mc.** is optional and does nothing for these objects, as they auto-adapt to the number of channels of a multichannel input signal.
  * [mc.tapin~](https://docs.cycling74.com/reference/mc.tapin~ "mc.tapin~"), [mc.tapout~](https://docs.cycling74.com/reference/mc.tapout~ "mc.tapout~"), [mc.send~](https://docs.cycling74.com/reference/mc.send~ "mc.send~"), [mc.receive~](https://docs.cycling74.com/reference/mc.receive~ "mc.receive~") : these can be thought of as I/O objects to internal memory buffers
  * Any objects begining with [mcs](https://docs.cycling74.com/userguide/mc/mc_mcvsmcs/) which are single instances of audio objects whose inputs and/or outputs are combined into a single multi-channel inlet and/or outlet
  * MC objects specific to [multi-channel signal manipulation](https://docs.cycling74.com/userguide/mc/mc_signals_newobjects/)


