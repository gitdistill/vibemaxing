---
description: Save the state of parameters for plug-ins, patchers, and RNBO devices
group: Parameters
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/snapshots/
title: Snapshots
---

# Snapshots
Snapshots let you save the state of parameters in your patcher. They are similar to the [pattr system](https://docs.cycling74.com/userguide/pattr/), but with some key differences:
  * Snapshots can be embedded with a patcher, and do not need to be saved as a separate JSON file.
  * There is no built-in mechanism to interpolate between snapshots.
  * Snapshots are global, containing all of the parameters in a given patcher, plugin, or device.
  * You can give snapshot slots a name


In general, snapshots give you less granular control than working with pattr, but require less configuration to work. Snapshots were designed with a few particular use cases in mind:
  * Saving and restoring the state of all [parameter-enabled](https://docs.cycling74.com/userguide/parameter_mode/) objects in a patch
  * Saving and restoring the state of a [VST or Audio Unit plugin](https://docs.cycling74.com/userguide/plugins/), or a Max for Live Device
  * Saving and restoring the state of a [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~") object.


Snapshots use the Parameter system to determine what to save; you will need to set the Parameter mode enable for each UI object whose state you wish to save.
## Patcher Snapshots
A patcher snaphot contains the state of all parameters in a patcher hierarchy. Since snapshots work with the [parameter system](https://docs.cycling74.com/userguide/parameter_mode/), an object must have [parameter mode enabled](https://docs.cycling74.com/userguide/parameter_mode/#enabling-parameter-mode) in order to be saved in a snapshot.
If you're unable to create new patcher snapshots, it might be because there are no parameter-enabled objects. Snapshots will only be enabled if there is at least one parameter-enabled object in your patcher. You can enable [parameter mode](https://docs.cycling74.com/userguide/parameter_mode/) on most UI objects from the [inspector](https://docs.cycling74.com/userguide/inspector/).
![](https://docs.cycling74.com/images/5ab9246d6ae019ac9555f4ea3b75b0c4_475.webp)
Here at the top of the _Snapshots_ sidebar view, you can see the text "patcher snapshots", indicating that these are snapshots that belong to the patcher itself. With nothing selected, the _Snapshots_ sidebar view will display patcher snapshots. If you select a [vst~](https://docs.cycling74.com/reference/vst~/ "vst~"), [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~"), or [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object, you'll see that the sidebar view updates to display snapshots for that object.
Patcher snapshots are saved and recalled at the top-level of a patcher hierarchy, but will save subpatcher parameters.
Subpatches can't have snapshots separate from the root patcher. If you need this kind of behavior, you can [create a Max for Live device](https://docs.cycling74.com/userguide/projects/#max-for-live-device-projects) and host it in a patcher with the [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~") object.
## Effects Snapshots
Effects snapshots store the parameter states of plugins, Max for Live devices, or RNBO devices hosted by [vst~](https://docs.cycling74.com/reference/vst~/ "vst~"), [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~"), or [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~") objects.
When you select one of these objects in your patcher window, the snapshots pane will display any snapshots associated with they selected device.
![](https://docs.cycling74.com/images/689ac30071676a2671faff684ef16d7e_918.webp)
Unlike patcher snaphsots, which are always saved with the patcher, effects snapshots are not embedded by default. Instead, they are saved in the [Max 9 Folder](https://docs.cycling74.com/userguide/search_path/#max-9-folder) in a folder called _Snapshots_. This means that when you create a snapshot for a VST, Audio Unit, or Max for Live Device, it's available throughout Max, no matter where it was created. See [embedding snapshots](https://docs.cycling74.com/userguide/snapshots/#embedding-snapshots) for more.
If you want to share a snapshot that you created, you can share the associated snapshot file located in the [Max 9 Folder](https://docs.cycling74.com/userguide/search_path/#max-9-folder). You can also use Max projects to automatically collect snapshot dependencies, which may make sharing snapshots easier.
The header/title bar for vst~ and amxd~ objects lets you create and recall new snapshots when the patcher window is locked. The camera icon creates snapshots, and the circular icon to the right will recall snapshots.
![](https://docs.cycling74.com/images/4d4f36b3cb90d7e3ce790c32c6059490_658.webp)
## Managing Snapshots
To view, create, load, rename, and delete snapshots, open the _Snapshots_ sidebar view by clicking the _Show Snapshots_ icon in the right toolbar.
All of the following snapshot options are also available by right-clicking on any snapshot. 
![](https://docs.cycling74.com/images/62e4eca445877fe13b10222739b96e1f_382.webp)
### Creating Snapshots
To create a new snapshot, click on the _Add a new Snapshot_ button in the bottom of the _Snapshots_ sidebar view.
![](https://docs.cycling74.com/images/b4e9a8e9894fba21295c78ee13be4151_404.webp)
### Recalling Snapshots
Recall a snapshot by either clicking on the triangle next to a snapshot, or by clicking on the _Restore Snapshot_ icon in the bottom toolbar.
![](https://docs.cycling74.com/images/dddcc4357d1a71becfdbec00c5f93d4d_377.webp)
### Renaming Snapshots
Rename a snapshot either by double-clicking on the name of a snapshot, or by clicking on the _Rename Snapshot_ icon in the bottom toolbar.
![](https://docs.cycling74.com/images/c6550a7edc6beb0b6142d0f90912e853_390.webp)
### Modifying Snapshots
You can modify a snapshot by clicking the _Take Snapshot_ button in the bottom toolbar. This will overwrite the currently selected snapshot with the current parameter values of the selected patcher or, device, or plugin.
![](https://docs.cycling74.com/images/f8d45ccd65a5d6cea89ed08c28f81668_382.webp)
### Deleting Snapshots
Delete a snapshot by clicking the _Delete the selected Snapshot_ icon in the bottom toolbar.
![](https://docs.cycling74.com/images/5ed317344b2112658aa5a45d164b8da9_399.webp)
## Embedding Snapshots
Patcher snapshots are always embedded with the patcher, but snapshots for plugins, amxds, and RNBO devices are not. Click on the circle icon next to any snapshot to embed it with the current patcher.
![](https://docs.cycling74.com/images/20de31b52781e5f57e4a8ea7ba62e386_386.webp)
Whether they are embedded or not, snapshots are always saved in the _Snapshots_ folder in the [Max 9 Folder](https://docs.cycling74.com/userguide/search_path/#max-9-folder). These snapshot files are named according to the name of the current patcher, so it's good practice to name your patcher file prior to creating snapshots.
### Usage with Projects
When you use a [vst~](https://docs.cycling74.com/reference/vst~/ "vst~"), [amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~"), or [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~") object as part of a [Max Project](https://docs.cycling74.com/userguide/projects/), any snapshots of that object become dependencies of the project. When you consolidate your project, those snapshots will be copied to the project directory. This lets you share your project with others, including any snapshots that the project might depend on.
## Usage with pattr
Snapshots can be easily integrated into your [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") workflow. Using a [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/ "pattrstorage") object along with [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") objects or an [autopattr](https://docs.cycling74.com/reference/autopattr/ "autopattr") object, the internal state of your VST, AU or AMXD can be recalled.
See the [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") and [autopattr](https://docs.cycling74.com/reference/autopattr/ "autopattr") help files for example usage (under the "snapshots" tab).
## Snapshot-enabled Messages
All snapshot-enabled objects ([amxd~](https://docs.cycling74.com/reference/amxd~/ "amxd~"), [vst~](https://docs.cycling74.com/reference/vst~/ "vst~"), [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~"), and [thispatcher](https://docs.cycling74.com/reference/thispatcher/ "thispatcher")) understand the messages:
  * `snapshot` [userpath (optional)] [index (optional)] [name (optional)]
  * `restore` [index (optional)]
  * `addsnapshot` [userpath (optional)] [index (optional)] [name - (optional)]
  * `deletesnapshot` [index]
  * `setsnapshotname` [index] [name]
  * `deletesnapshot` [index]
  * `setembedsnapshot` [index] [embedstate]
  * `movesnapshot` [srcindex] [dstindex]
  * `exportsnapshot` [srcindex] [userpath]
  * `importsnapshot` [dstindex] [userpath]


## JavaScript Snapshot API
For advanced users and those creating standalone patchers, Snapshots can be accessed via the Snapshots API. See the [JavaScript Snapshot API](https://docs.cycling74.com/apiref/js/snapshotapi/) for more information.
