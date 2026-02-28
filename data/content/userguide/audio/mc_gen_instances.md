---
description: MC gen objects can host one or multiple patches
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_gen_instances/
title: MC Gen Instances
---

# MC Gen Instances
When you create an [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") object, you are creating a hosting environment for multiple instances of a _Gen DSP_ patch. There are several ways to manage the contents of the object, based on how the _Gen DSP_ is loaded.
If you create an [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") object without a patcher name argument, you are working with the default, unnamed Gen DSP patch maintained by Gen. This patch is duplicated across all instances, and any changes to this patch will be propagated across all voices.
![](https://docs.cycling74.com/images/4916fbf111e94e0ec617450e6c5f65eb_476.webp)
## Using One Gen DSP File
When you load a single Gen DSP file into an [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") object, it is copied to all voices. If the patch is changed, the changes are immediately propogated to all voices as you edit.
![](https://docs.cycling74.com/images/0e09368fbdc0235db5adab43ee334cbc_491.webp)
## Using Multiple Gen DSP Files
You can load each [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") instance inside [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") with a different Gen DSP file. This is done using the `@values` wrapper message as a typed-in attribute. If fewer files are provided than channels are defined, the remaining channels will use the default Gen DSP patch.
![](https://docs.cycling74.com/images/906b06d5df7afa2d6fc196c6e723e7ab_299.webp)
In this case, if you make a change to one of the patches, it _will not_ propogate any changes to the other voices - each of the Gen DSP files is isolated from the others.
