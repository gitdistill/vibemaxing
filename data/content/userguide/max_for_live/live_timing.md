---
description: Managing timing and synchronization in Max for Live devices
group: Max For Live
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/m4l/live_timing/
title: Timing and Synchronization in Max for Live
---

# Timing and Synchronization in Max for Live
The Live transport is a clock source for the Max [tempo-based time system](https://docs.cycling74.com/userguide/time_value_syntax/).
## Implementation Notes
  * By default, all [transport](https://docs.cycling74.com/reference/transport/ "transport") objects in Live devices (those without names) synchronize to the Live transport.
  * Named [transport](https://docs.cycling74.com/reference/transport/ "transport") objects do not synchronize to Live unless you set the `clocksource` attribute to the name `live`.
  * If two device instances contain [transport](https://docs.cycling74.com/reference/transport/ "transport") objects that share the same name, they will run independently.
  * The tempo-based timing system synchronizes to Live even in [preview mode](https://docs.cycling74.com/userguide/m4l/live_preview/). However, there may be disruptions in the continuity of timing when switching into or out of preview mode.


