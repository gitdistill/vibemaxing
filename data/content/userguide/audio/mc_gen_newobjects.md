---
description: Description of the mc_channel and mc_channelcount Gen operators
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_gen_newobjects/
title: MC Gen Operators
---

# MC Gen Operators
Two Gen operators are useful with [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") and [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen"):
  * **mc_channel** reports the current channel of the Gen patcher within [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") or [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") (starting at 1).
  * **mc_channelcount** reports the total number of channels (Gen instances) within [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") or [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen").

![](https://docs.cycling74.com/images/dc51b82030deca4a19b597384d9f7005_249.webp) These Gen operators make it possible to do voice-specific calculations. You can also connect them to the Gen [out](https://docs.cycling74.com/reference/out/ "out") operator to provide voice-specific identification signals or events outside the Gen context. ![](https://docs.cycling74.com/images/5be5f7b865039d604a805280659ccc27_596.webp)
When used in a patcher inside [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), [mcs.gen~](https://docs.cycling74.com/reference/mcs.gen~ "mcs.gen~"), or [gen](https://docs.cycling74.com/reference/gen/ "gen") (in other words, outside the context of the MC Wrapper), both operators output 1.
