---
description: Overview of gen features for MC, including expr and hot attributes
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_gen_newfeatures/
title: Gen Features for MC
---

# Gen Features for MC
New features have been added to Gen to support MC as well as to make integration of Gen easier with the remainder of your Max patching. The changes include:
## Create Simple Gen Patchers with `@expr`
You can use the `@expr` typed-in attribute with a [gen](https://docs.cycling74.com/reference/gen/ "gen"), [gen~](https://docs.cycling74.com/reference/gen~/ "gen~"), [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") or [mcs.gen~](https://docs.cycling74.com/reference/mcs.gen~ "mcs.gen~") object to specify a single line of Genexpr code.
![](https://docs.cycling74.com/images/38a5460044d1cc5e371e027a05d7af78_183.webp)
## Control [gen](https://docs.cycling74.com/reference/gen/ "gen") Execution with the `@hot` Attribute
By default, [gen](https://docs.cycling74.com/reference/gen/ "gen") triggers processing only when receiving a value in its left inlet. The `@hot` attribute will set any other inlet to be "hot" and trigger processing.
![](https://docs.cycling74.com/images/ab1b81fd8e3a20fd2a0de626141134b1_209.webp)
