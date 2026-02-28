---
description: Overview of the difference between the mc.gen~, mcs.gen~ and mc.gen objects
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/mc/mc_gen/
title: MC and Gen
---

# MC and Gen
Gen and MC combine in the following objects:
  * [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~") contains individual instances of [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") via the [MC Wrapper](https://docs.cycling74.com/userguide/mc/mc_wrapper/), so it can take advantage of all the features available to any wrapped object.
  * [mcs.gen~](https://docs.cycling74.com/reference/mcs.gen~ "mcs.gen~"), like other _mcs.*_ objects, combines the separate Gen inputs and outputs defined by `inX` and `outX` operators into a multi-channels input and output.
  * [mc.gen](https://docs.cycling74.com/reference/mc.gen "mc.gen") contains multiple instances of the event-based [gen](https://docs.cycling74.com/reference/gen/ "gen") object. It has an additional outlet that informs Max of the voice number associated with any outgoing message.


## See Also
  * [Using mc.gen With the MC Wrapper](https://docs.cycling74.com/userguide/mc/mc_gen_event_wrapper/)
  * [MC Gen Instances](https://docs.cycling74.com/userguide/mc/mc_gen_instances/)
  * [Gen Features for MC](https://docs.cycling74.com/userguide/mc/mc_gen_newfeatures/)
  * [MC Gen Operators](https://docs.cycling74.com/userguide/mc/mc_gen_newobjects/)


