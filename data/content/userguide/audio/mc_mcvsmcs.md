---
description: Differences between mc and mcs family of objects
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_mcvsmcs/
title: MC vs MCS Objects
---

# MC vs MCS Objects
As you work with MC you'll encounter a few objects beginning with **mcs**.
The "s" stands for **single** , meaning that an MCS object is a single instance with a single multi-channel input and a single multi-channel output. An example is [mcs.gen~](https://docs.cycling74.com/reference/mcs.gen~ "mcs.gen~") : If you make a Gen patcher containing **in 1** , **in 2** , and **in 3** operators, a normal [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") object would show three inlets:
![](https://docs.cycling74.com/images/c0e84305fbbdebf65f90855242a4d4bf_577.webp)
The [mcs.gen~](https://docs.cycling74.com/reference/mcs.gen~ "mcs.gen~") version of this patch would have only one multi-channel inlet. You can connect a multi-channel patch cord to this inlet and it will distribute the first three channels to the corresponding [in](https://docs.cycling74.com/reference/in/ "in") operators. Likewise, multiple outlets are provided as a single multi-channel outlet.
![](https://docs.cycling74.com/images/27d71bf658dc729d7051c05f417261c4_819.webp)
By contrast, if you made an [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") with this same Gen patcher, you would see an object with three inlets and two outlets. Each of these inlets corresponds to the [in](https://docs.cycling74.com/reference/in/ "in") operator within the Gen patcher, but with [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") there are multiple instances of the Gen patcher running inside the MC wrapper, so multichannel signals connected to these inlets are distributed to each Gen instance.
![](https://docs.cycling74.com/images/5ffad367ef7d23f3c402e9e42d48b269_385.webp)
Another group of MCS objects deal with multichannel [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") data. If you create a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object with four channels of audio data, the [mcs.play~](https://docs.cycling74.com/reference/mcs.play~ "mcs.play~") object will combine all four output channels of this audio data into one multichannel output. By contrast, [mc.play~](https://docs.cycling74.com/reference/mc.play~ "mc.play~") lets you create multiple "players" of the same data in the MC Wrapper.
In deciding whether you want the MC or MCS version of [play~](https://docs.cycling74.com/reference/play~/ "play~"), ask yourself whether you want to play one copy of a sound with multiple channels, or several copies of the same sound you can control independently.
