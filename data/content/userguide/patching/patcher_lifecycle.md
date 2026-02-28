---
description: What happens when you open and close a patch, and in what order
group: Patching
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/patcher_lifecycle/
title: Patcher Lifecycle
---

# Patcher Lifecycle
## Opening a Patcher
In general, it's best practice not to make any assumptions about the order in which things will happen when Max opens up a saved patcher. If there's a way to use an object like [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") to make the order of messages explicit, it's usually a good idea to do so. However, when Max loads a new patcher it does initialize the patcher in specific phases.
![Max patcher stages of initialization](https://docs.cycling74.com/images/ba8238a30cbb95eae59be0dc43cdf80c_1011.webp) Max patcher stages of initialization
  1. [Object Initialization](https://docs.cycling74.com/userguide/patcher_lifecycle/#object-initialization)
  2. [Patchcord Connection](https://docs.cycling74.com/userguide/patcher_lifecycle/#patchcord-connection)
  3. [Parameter Initialization](https://docs.cycling74.com/userguide/patcher_lifecycle/#parameter-initialization)
  4. [_pattr_ Restoration](https://docs.cycling74.com/userguide/patcher_lifecycle/#pattr-restoration)
  5. [_loadbang_ and _loadmess_](https://docs.cycling74.com/userguide/patcher_lifecycle/#loadbang-and-loadmess)
  6. [_live.thisdevice_](https://docs.cycling74.com/userguide/patcher_lifecycle/#livethisdevice)
  7. [Window Activity](https://docs.cycling74.com/userguide/patcher_lifecycle/#window-activity)
  8. [Patcher Arguments](https://docs.cycling74.com/userguide/patcher_lifecycle/#patcher-arguments)
  9. [_dspstate~_ and Signal Processing](https://docs.cycling74.com/userguide/patcher_lifecycle/#dspstate-and-signal-processing)


### Subpatchers
Within a given phase, Max subpatchers are initialized before their parents. If a Max patcher contains a [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") object, and its subpatcher also contains a [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") object, the [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") in the subpatcher will always output a `bang` message before the parent. However, a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object in a parent patcher will initialize before any [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") objects output a `bang`, even if the [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") objects are in a child patcher, because _Object Initialization_ comes before _loadbang and loadmess_.
### Object initialization
Max creates all objects in the current patcher. For some objects, this may have synchronous behavior, where the behavior might otherwise be asynchronous. For example, when a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object is initialized, if a _file_ argument is provided, that file is loaded synchronously. After the patcher has loaded, sending a `replace` message to a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object triggers an asynchronous operation.
### Patchcord connection
After all of the objects in the patcher have been initialized, Max will rebuild all of the patchcord connections between objects. Importantly, since this happens after object initialization, Max messages sent between objects during the object initialization step might not be routed between objects as expected.
### Parameter initialization
Next, Max checks all objects for which [Parameter Mode](https://docs.cycling74.com/userguide/parameter_mode/) is enabled. For any such objects, if they have an initial value set, those objects will set their internal parameter value to that initial value, and then output their value.
Select _Reinitialize_ from the _Edit_ menu to set all parameters in the current patcher to their initial value.
###  _pattr_ Restoration
If there are any [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") objects with `@autorestore` enabled, Max will restore the last set value of each [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object, and then each [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object will output a value.
###  _loadbang_ and _loadmess_
Now that all objects have been initialized, [loadmess](https://docs.cycling74.com/reference/loadmess/ "loadmess") and [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") objects will generate their output.
### _live.thisdevice_
The [live.thisdevice](https://docs.cycling74.com/reference/live.thisdevice "live.thisdevice") object functions similarly to [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") in the context of a Max for Live device. In a regular Max patcher, [live.thisdevice](https://docs.cycling74.com/reference/live.thisdevice "live.thisdevice") is functionally the same as a [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") except [live.thisdevice](https://docs.cycling74.com/reference/live.thisdevice "live.thisdevice") objects will trigger after [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") objects.
### Window activity
After all objects have been initialized, and any [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") or [loadmess](https://docs.cycling74.com/reference/loadmess/ "loadmess") objects have sent their output, Max will create the window and bring it into focus. Any [active](https://docs.cycling74.com/reference/active/ "active") objects will now send an output.
### Patcher Arguments
Patcher arguments (arguments and attributes on a [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") object) are parsed by [patcherargs](https://docs.cycling74.com/reference/patcherargs/ "patcherargs") objects at the same time as [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") and [loadmess](https://docs.cycling74.com/reference/loadmess/ "loadmess") objects send their respective messages. However, the initial output of a [patcherargs](https://docs.cycling74.com/reference/patcherargs/ "patcherargs") object is deferred, and will be sent after the window is ready.
###  _dspstate~_ and signal processing
Finally, Max is ready to construct the signal processing graph and start audio processing for the patcher. This is the stage when all [dspstate~](https://docs.cycling74.com/reference/dspstate~/ "dspstate~") objects will send their outputs, reporting the current sample rate, DSP on/off status, etc.
## Closing a Patcher
Similar to the way Max builds up a patcher in stages when opening a new patcher, closing a patcher also breaks the patcher down in a standard order. Similar to opening a patcher, subpatches close before parent patches So, a [freebang](https://docs.cycling74.com/reference/freebang/ "freebang") in a subpatcher will send its bang before a [freebang](https://docs.cycling74.com/reference/freebang/ "freebang") in a parent patcher.
  1. [_closebang_](https://docs.cycling74.com/userguide/patcher_lifecycle/#closebang)
  2. [Freeing Objects](https://docs.cycling74.com/userguide/patcher_lifecycle/#freeing-objects)


### _closebang_
First, the closing the Max patcher window causes any [closebang](https://docs.cycling74.com/reference/closebang/ "closebang") objects to send a `bang` message. One interesting thing is that if you close a parent patcher window, with an open subpatcher containing a [closebang](https://docs.cycling74.com/reference/closebang/ "closebang") object, that object will _not_ send a `bang` message at this time. However, if you close the subpatcher window manually first, [closebang](https://docs.cycling74.com/reference/closebang/ "closebang") will send a `bang`.
### Freeing objects
Max goes through all of the objects in the patcher and frees them. This frees any memory or other resources that each object might have been holding on to. It also causes any [freebang](https://docs.cycling74.com/reference/freebang/ "freebang") objects to send a `bang` message.
