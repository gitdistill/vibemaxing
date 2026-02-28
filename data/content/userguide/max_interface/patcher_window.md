---
description: Each of the Max toolbars, and other functions available in the Max window
group: Max Interface
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/patcher_window/
title: Patcher Window and Toolbars
---

# Patcher Toolbars
The top, left, right, and bottom of every Max window contain the toolbars. These icons allow you to access built-in Max content, configure the behavior of your patcher, quickly access objects to add to your patcher, and more.
## Customizing Toolbars
If you want, you can pin/unpin any of the toolbars by hovering over the toolbar and clicking on the triangular tab that appears in the middle of the toolbar. Hover over the hidden toolbar, near the border of the patcher, to bring the toolbar back.
![](https://docs.cycling74.com/images/eddb3c66e08fb36789efdc85fed70bbc_847.webp)
You can also customize each toolbar by adding or removing icons. To remove an icon, simply right-click on it and choose the _Remove_ option from the contextual menu.
![](https://docs.cycling74.com/images/4aa2594ecffdb70629b99cc1c5393c42_378.webp)
You can also add icons to your toolbars by right-clicking and selecting an _Add_ option from the contextual menu. Each toolbar has different options for which icons can be added.
  * **Right Toolbar** - Select _Add Browse Lessons_ to add a lesson browser.
  * **Bottom Toolbar** - This toolbar can add _Mute_ and _Solo_ buttons, which mute and solo the audio output of the patcher.
  * **Left Toolbar** - The most customizable of all, since you can add a browse icon for any installed [package](https://docs.cycling74.com/userguide/packages/) to this toolbar. You can also add an icon to open the [Package Manager](https://docs.cycling74.com/userguide/package_manager/).

![](https://docs.cycling74.com/images/0d6e5a9c765b6070366491917c512ff5_314.webp) The left toolbar, customized to include an icon for the BEAP package
If you want your toolbars to keep their configuration the next time you open Max, right-click and select _Save Toolbar as Default_. If you want to go back to the original toolbar configuration, select _Reset Toolbar to Factory Default_.
## Left toolbar
The left toolbar provides access to different collections of resources that you can use in your patcher. For a more detailed, dedicated view of all the files in Max's [search path](https://docs.cycling74.com/userguide/search_path/), use the [File Browser](https://docs.cycling74.com/userguide/file_browser/).
From top to bottom:
  1. [**Patcher List View**](https://docs.cycling74.com/userguide/patcher_window/#patcher-list-view)- List, sort, and filter all of the objects in the current patcher.
  2. [**Objects**](https://docs.cycling74.com/userguide/patcher_window/#object-browser)- Browse and filter all the objects in Max, including objects from installed [packages](https://docs.cycling74.com/userguide/packages/).
  3. [**Audio**](https://docs.cycling74.com/userguide/patcher_window/#audio-browser)- Contains all the audio in Max's [search path](https://docs.cycling74.com/userguide/search_path/), with options to filter by name and length.
  4. [**Video**](https://docs.cycling74.com/userguide/patcher_window/#video-browser)- Browse all the videos in Max's [search path](https://docs.cycling74.com/userguide/search_path/).
  5. [**Images**](https://docs.cycling74.com/userguide/patcher_window/#image-browser)- Browse all the images in Max's [search path](https://docs.cycling74.com/userguide/search_path/).
  6. [**Plug-ins**](https://docs.cycling74.com/userguide/patcher_window/#plug-ins-browser)- Displays both VST and Audio Unit [plug-ins](https://docs.cycling74.com/userguide/plugins/), as well as Max for Live devices (also known as AMXDs).
  7. [**Max for Live**](https://docs.cycling74.com/userguide/patcher_window/#max-for-live-browser)- Special snippets and objects for [Max for Live](https://docs.cycling74.com/userguide/max_for_live/) device development.
  8. [**Modules**](https://docs.cycling74.com/userguide/patcher_window/#module-browser)- Categorized selections of objects and snippets from installed [packages](https://docs.cycling74.com/userguide/packages/)
  9. [**Collections**](https://docs.cycling74.com/userguide/patcher_window/#collection-browser)- Resources from [collections](https://docs.cycling74.com/userguide/file_browser/#collections) as defined in the [File Browser](https://docs.cycling74.com/userguide/file_browser/).


Optionally, you can also add a browser view for _Gen DSP_ , _Gen Jitter_ , or any installed [package](https://docs.cycling74.com/userguide/packages/).
### Patcher List View
The Patcher List View, which only functions when the patcher is unlocked, shows all of the objects in the current patcher. Unlike the patcher view itself, which shows each object in its current [patching rectangle](https://docs.cycling74.com/userguide/patching/#patching-rect), this view simply displays the text of each object in a flat list.
The list view is helpful for locating, selecting, and operating on objects that might otherwise hard to find in complex patchers.
Move the cursor over any element in the list to highlight the associated object, and click to select it.
![](https://docs.cycling74.com/images/22a54133ea25f6efae41b9ef380be2a0_488.webp)
Objects within a subpatcher won't be included in the list, but you can double-click on a subpatcher object to open that subpatcher.
Type in the _Filter_ text entry at the top of the view to filter for objects matching specific text.
Use the _Sort by_ drop-down to change how objects are sorted in the list, and use the _Include_ drop-down to filter for _UI Objects_ , _Non-UI Objects_ , or _All Objects_.
![](https://docs.cycling74.com/images/5fbbd716b022a5ea0387046d993efaa9_488.webp) With Non-UI Objects selected, user interface objects like the toggle, numbox, and ezdac~ are all excluded from the object list.
When open, the list view will reflect the current selection in the patcher window. In addition, the list view display of objects with values such as [slider](https://docs.cycling74.com/reference/slider/ "slider") or [number](https://docs.cycling74.com/reference/number/ "number") will update as the values of those objects changes.
### Operations on List View Items
  * Click any item to select it in the patcher. Shift-click to select multiple items.
  * Click on the round **button** that appears at the left edge of a list view item to open the [Object Action Menu](https://docs.cycling74.com/userguide/action_menu/) for the object.

![](https://docs.cycling74.com/images/41191b98f1dd99553e7f77e4f59e6cca_226.webp)
  * **Double-click** on any list view item to perform the same action as double-clicking on the item in the patcher would perform. For instance, double-clicking on a patcher will open the object's patcher window.
  * Press **return** or enter on any selected object to send that object a `bang` message. For example, selecting a [button](https://docs.cycling74.com/reference/button/ "button") and pressing return will act as if you clicked on the button.


### Dragging and Dropping
The following browsers, including the [Object Browser](https://docs.cycling74.com/userguide/patcher_window/#object-browser), [Audio Browser](https://docs.cycling74.com/userguide/patcher_window/#audio-browser), etc., are convenient ways to find resources that you can add to your patch. Once you've found what you're looking for, you can just drag the resource into your patch to add it.
Depending on what kind of resource you're trying to add, the Max patcher will handle the drop in different ways. If you drag an audio file into your patch, Max will create a [playlist~](https://docs.cycling74.com/reference/playlist~/ "playlist~") object to play that file back. If you drag in a video file, Max will make a [jit.playlist](https://docs.cycling74.com/reference/jit.playlist "jit.playlist") object.
![](https://docs.cycling74.com/images/3ad0e59fcf7530e11f1a5a9801af2132_1024.webp) When you drop an audio file into your patch, Max will create and configure a playlist~ object to play back that file.
Some resources can give you multiple options as to how they should be handled. Hold down `Alt` (Windows) or `Option` (macOS) while dragging a resource into the patcher view to see all the available options.
![](https://docs.cycling74.com/images/5d971ba400379e922d39881cfed7fd34_524.webp) Hold down Alt/Option as you drag an audio file into your patcher to create a playlist~ object, an sfplay~ obect, a buffer~ object, or a message box configured for that audio file.
Finally, many Max object can handle resources of the appropriate kind. For example, if you drag an audio file over a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object, you'll see a blue border appear inside [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), indicating that it can perform a special action when you drop the file. Usually, if an object can load a file in response to an `open` or `read` message, then it can handle a drag-and-drop action with that same file type.
![](https://docs.cycling74.com/images/d405f482b5d23fbe3f5c8b04daa94704_972.webp) When you drag-and-drop an audio file on top of a buffer~ object, the buffer~ will read the audio file and resize itself to fit.
### Object Browser
The Object Browser shows you all the objects that Max has to offer, with a couple of controls to make it easier to find the object you're looking for.
Type into the _Filter_ text entry at the top to find objects matching specific text.
![](https://docs.cycling74.com/images/48fca76b183565d5d573541ed5a11210_321.webp)
Max has several _Math Operators_ , small objects that perform a simple math operation like addition or multiplication. By default, these objects are filtered from view, but you can select the _Show Math Operators_ checkbox to reveal them.
![](https://docs.cycling74.com/images/058a3d6b873c22753299e4307557a2bb_318.webp)
The browser view on the left groups objects by package, and then by category within a package. Click on a package to show all objects included in that package, and on a category to show just objects in that category.
![](https://docs.cycling74.com/images/c3335295ecb47ad07d14740521d48efe_317.webp)
Finally, notice the description view at the bottom of the browser, which will show a short summary when you roll over an object.
![](https://docs.cycling74.com/images/219bd4d704c608cea9804a358187cb97_279.webp)
### Audio Browser
The Audio Browser shows all of the audio samples in Max's [search path](https://docs.cycling74.com/userguide/search_path/). There are controls to filter by name and length, and a preview option to audition samples as well.
Type into the _Filter_ text entry at the top to find objects matching specific text.
![](https://docs.cycling74.com/images/e116b95abdf5c0638cd644564713abd6_315.webp)
You can deselect _Include Built-in Content_ to filter out any content that shipped with Max. This includes content from built-in packages, like _BEAP_ and _Jitter_.
With the _Duration_ filter active, you can use the slider to select only audio files that fall within a certain length.
![](https://docs.cycling74.com/images/3eb1381a82a42f87b16bc3c474720d11_315.webp) You could use a short duration filter to show only one-shots.
Hover over a sample and click the _Play_ triangle to preview the sample. While the sample is playing, the triangle will change to a _Pause_ icon that you can use to pause playback.
![](https://docs.cycling74.com/images/99da82f78e0e0ca9a12d28d4f8dc8880_319.webp)
If _Auto Preview_ is enabled, each sound sample will start playing as soon as you select it. With this option, you can use the arrow keys to move your selection up and down, quickly auditioning a large number of files.
Finally,the _Description_ view at the bottom of the browser will display the name of an audio file, the full path to that file on disk, the length of the file, the number of audio channels in the file, and the bit depth of samples in the file.
![](https://docs.cycling74.com/images/59c8a556396f37095a2930bc7f89f300_318.webp)
### Video Browser
The Video Browser shows all of the video files in Max's [search path](https://docs.cycling74.com/userguide/search_path/). There are controls to filter by name, and you can choose whether to view files as a list or by preview thumbnails.
![](https://docs.cycling74.com/images/0bb7063631e4ffa5c9048ee1063386ac_319.webp)
With _View by Preview_ enabled, video files will appear in a grid of video thumbnails. Hover over a thumbnail to see the name of the file, and click on it to preview the video. Finally, use the size controller above the thumbnails to adjust the size of the previews in the view.
![](https://docs.cycling74.com/images/f9ff4cbbe2b7ec1fed5713aadbdb1d1c_636.webp) Change the size of the previews to see more video files at once.
### Image Browser
The Image Browser shows all of the image files in Max's [search path](https://docs.cycling74.com/userguide/search_path/). Similar to the Video Browser, there are controls to filter by name, and you can choose whether to view files as a list or by preview thumbnails.
![](https://docs.cycling74.com/images/2228d302f481574f3b2b1846c4a68fcb_319.webp)
### Snippet Browser
The Snippet Browser shows you all of the [Snippets](https://docs.cycling74.com/userguide/snippets/) that Max has access to. Like the Video and Image Browsers, there are controls to filter by name, and you can choose whether to view files as a list or by preview thumbnails.
![](https://docs.cycling74.com/images/76923a482a9c76d3928d39029724d5a7_317.webp)
### Plug-ins Browser
The Plug-ins Browser shows you both VSTs and Audio Units [plug-ins](https://docs.cycling74.com/userguide/plugins/) that Max has scanned, as well as any [Max for Live](https://docs.cycling74.com/userguide/max_for_live/) devices (AMXDs) in the [search path](https://docs.cycling74.com/userguide/search_path/). Use the _Filter_ text entry to filter by name, and the _Recent_ tab so see plug-ins that you've used recently.
![](https://docs.cycling74.com/images/53fcc01e055b5715db2433503c731a98_318.webp)
### Max for Live Browser
The Max for Live Browser is organized to make Max for Live device development easier by bringing together objects, [abstractions](https://docs.cycling74.com/userguide/abstractions/), and [snippets](https://docs.cycling74.com/userguide/snippets/) for common tasks like handling MIDI, voice allocation, and audio synthesis. The snippets and abstractions under _Live API Browsers_ , _Live API Snippets_ and _Live API Objects_ are especially useful, since these provide solutions to many of the common programming challenges you'll run into when working with the [Live API](https://docs.cycling74.com/apiref/lom/)
![](https://docs.cycling74.com/images/29686a1ccaa0171b2ca780b8199b00c1_755.webp) One of the helpful snippets available in the Max for Live Browser
### Module Browser
The Modules Browser presents [snippets](https://docs.cycling74.com/userguide/snippets/) and [abstractions](https://docs.cycling74.com/userguide/abstractions/) from built-in and third party [packages](https://docs.cycling74.com/userguide/packages/) that you've installed. It's a powerful way to package authors to give you quick access to the best of what their tools are capable of. For example, the built-in BEAP package has categorized abstractions related to audio analysis, effects, and quantization, all organized into modules.
![](https://docs.cycling74.com/images/6bb6fbf976156057380241a7a93d3de4_696.webp) The BEAP compressor effect, loaded from the Modules Browser.
### Collection Browser
The [Collection](https://docs.cycling74.com/userguide/file_browser/#collections) Browser shows you all the collections that you've defined using the [File Browser](https://docs.cycling74.com/userguide/file_browser/). Collections give you total control over how your work is grouped, since a single collections can contain any kind of resource, including video clips, text files, and JavaScript code. You can define collections specific to a project or workflow, and use the Collections Browser to quickly access resources in that collection.
![](https://docs.cycling74.com/images/225c6a76067fe84ca687fe8206480309_571.webp) The built-in collection 'Sample Collection' demonstrates what a collection can do, and includes files of multiple media types.
## Top toolbar
The top toolbar contains various controls for changing the appearance of your patcher, along with quick access to many of the user interface objects available in Max.
![](https://docs.cycling74.com/images/53d61d13d9b94b2b3fdbb2d381669c9f_551.webp)
The _Show Browser_ icon reveals the most recent Browser view in the [Left Toolbar](https://docs.cycling74.com/userguide/patcher_window/#left-toolbar).
The _Zoom Dropdown_ lets you adjust the level of zoom in your Max patcher. You can also adjust the zoom level by pressing `⌘``=` (macOS) or `CTRL``=` (Windows) to zoom in, and `⌘``-` (macOS)or `CTRL``-` (Windows) to zoom out.
The _UI Object Palette_ gives you quick access to Max UI objects, organized by function. Click on icons with a disclosure triangle to see a selection of options within that category.
![](https://docs.cycling74.com/images/5b2bf7f37b1d5db020143f8f26abe3bc_539.webp)
The [Format Palette](https://docs.cycling74.com/userguide/format_palette/) button lets you adjust the style and appearance of objects in your patcher.
![](https://docs.cycling74.com/images/4a2e56563acc3e9efa21e34235c49940_729.webp)
Finally, the calendar button lets you access the calendar. This can be extremely useful when you want to know what patches you opened on a specific date.
![](https://docs.cycling74.com/images/20e90e2a0104cb1fedd5c7652fa81a00_354.webp)
## Right toolbar
The right toolbar lets you access the sidebar. Each button icon opens a different sidebar view. The [Search](https://docs.cycling74.com/userguide/sidebar_search/) icon lets you access Max's search, which can help you find objects, reference documentation, examples, and forum posts.
![](https://docs.cycling74.com/images/59f16e5d632662948dd4b43e21ceb654_405.webp)
The [Inspector](https://docs.cycling74.com/userguide/inspector/) icon will open the patcher and object inspector, which lets you view and edit the configuration of the objects in your patcher.
![](https://docs.cycling74.com/images/68ccf66b86b92ad4e83bf3f6f477e87e_405.webp)
The [Reference Sidebar](https://docs.cycling74.com/userguide/sidebar_reference/) gives a quick summary of the function of the selected object, along the messages and attributes that the selected object understands.
![](https://docs.cycling74.com/images/009095c62ab86830d14585f231e1cf3a_405.webp)
The [Max Console](https://docs.cycling74.com/userguide/max_console/) displays errors and warnings, in addition to the output of any print objects.
![](https://docs.cycling74.com/images/bd73803fbb2ce3a7ad42bf3a41900396_486.webp)
The [Snapshot](https://docs.cycling74.com/userguide/snapshots/) editor lets you view and edit any snapshots belonging to the current patcher.
![](https://docs.cycling74.com/images/f5fbaaca425392dc17c27c6fd4a2ab3a_404.webp)
The [Mapping](https://docs.cycling74.com/userguide/mapping/) button will be enabled if any objects in the current patcher support parameter mapping. From the mapping editor, you can view and configure MIDI and Keyboard mappings.
![](https://docs.cycling74.com/images/6c1b8086d8ff7c78b0f858350cac843b_404.webp)
You can use the [Global Record](https://docs.cycling74.com/userguide/recording/#global-record) button to quickly record the audio output of your patcher.
![](https://docs.cycling74.com/images/51a567cb2287a8f5ba0b2b8572285ec9_171.webp)
Above the volume control, the _Audio CPU Meter_ tells you how much of your computer's processing power you've used up with signal computation.
![](https://docs.cycling74.com/images/1a15eafedf565dff6da17a5fdbc9a418_171.webp)
If you have a [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") object in your patch, you can click on the _Audio CPU Meter_ to toggle the _FPS Meter_ for your graphics context. This shows you the rate of graphics processing in frames per second.
![](https://docs.cycling74.com/images/be2f969d5284679dea071cca646d6613_214.webp)
Finally, at the bottom of the right sidebar, the volume control lets you adjust the gain for any audio generated from this patcher. Each patcher has its own gain control.
![](https://docs.cycling74.com/images/4b58fafb2cba94a3b7bc80424db29d85_141.webp)
## Bottom toolbar
The bottom toolbar contains controls for changing how you interact with your patcher, including enabling/disabling an alignment grid, turning on signal processing, and more. You can right click on the bottom toolbar and select "Add Mute Audio" or "Add Solo Audio" to enable these optional icons.
![](https://docs.cycling74.com/images/90b99b04b1ad2d03bf33ed205c67a28f_448.webp)
From left to right, the first icon in the bottom toolbar controls [Locking](https://docs.cycling74.com/userguide/patching/#lockingunlocking), letting you lock/unlock your patcher.
![](https://docs.cycling74.com/images/e3f10c343fdd597fbb7b1146ad0eeb74_324.webp)
If you're looking at an instance of an [Abstraction](https://docs.cycling74.com/userguide/abstractions/), then the lock icon will change to a crayon. Clicking this icon will let you modify the orignal patcher.
![](https://docs.cycling74.com/images/336e536ca459d861e1cd3c7b372d7a7c_326.webp)
The [Operate While Unlocked](https://docs.cycling74.com/userguide/patching/#operate-while-unlocked) icon enables an interaction mode that lets you control UI objects in your patcher, even while the patcher is unlocked.
![](https://docs.cycling74.com/images/e7f3ccbd97d765838c6a0f7c7d2f81c0_325.webp)
The [_Patching Margin_](https://docs.cycling74.com/userguide/patching/#patching-margin) icon gives you a bit more room to work with, at the border of a patcher that fills up the entire view.
![](https://docs.cycling74.com/images/30818ae5f55b0486115d213184dfed2d_313.webp)
Clicking the [Presentation Mode](https://docs.cycling74.com/userguide/patching/#presentation-mode) icon will enable/disable presentation mode.
![](https://docs.cycling74.com/images/6c10363791eab52d04b86be72f84e82e_314.webp)
The _Patcher Windows_ button lets you access different views of the current patcher. Click "New View" to open a new window displaying the same contents as the current patcher. This can be useful if you want to look at two different parts of a large patcher at once, or if you want to view a patcher in presentation and patching mode at the same time. If you're looking at an instance of an [Abstraction](https://docs.cycling74.com/userguide/abstractions/), the option "Open Original" will be enabled, and selecting this option will open the original version of the abstraction. Finally, if you're looking at a subpatcher, the bottom of the menu will let you navigate up the patcher hierarchy to a parent patcher.
![](https://docs.cycling74.com/images/cbcf2f3cea29fd9370157ee37bb2fece_315.webp)
Clicking the _Show Objects Over Connections_ button toggles between displaying objects over patch cords, or patch cords over objects.
![](https://docs.cycling74.com/images/a5441a3200182bbdfb5347fa1da7b52d_320.webp)
The _Show Grid_ button will let you enable and disable an alignment grid for your patcher. You can control this same option by selecting _Grid_ from the _View_ menu, and this option works in conjunction with _Snap to Grid_ from the _Arrange_ menu.
![](https://docs.cycling74.com/images/9ae537e77bd9b9b67e8bad97f19f3bee_320.webp)
With some objects selected in your patcher, the [Snippet](https://docs.cycling74.com/userguide/snippets/) button will let you save a new snippet from your selection.
![](https://docs.cycling74.com/images/47214daa7e76880891b442e46c1f4858_321.webp)
The _Enable Debugging_ button will toggle [Debug Mode](https://docs.cycling74.com/userguide/debugging_and_probing/#debugging).
![](https://docs.cycling74.com/images/f9901f623bec4e3fdd1a1246f9a143d4_319.webp)
You can configure [MIDI Mapping](https://docs.cycling74.com/userguide/mapping/#midi-mapping) by clicking the _MIDI Mapping_ icon.
![](https://docs.cycling74.com/images/2a8c4792f98006053a6c442e11927b50_315.webp)
And you can configure [Keyboard Mapping](https://docs.cycling74.com/userguide/mapping/#keyboard-mapping) by clicking the _Keyboard Mapping_ icon.
![](https://docs.cycling74.com/images/0c7f2b5ff96938a9d0ae0cddffc623f8_316.webp)
When you hover over an object in your patcher, the **Clue Bar** will appear in the bottom toolbar. You can configure the appearance and behavior of the Clue Bar using the _Clues_ preference in the [Preference Window](https://docs.cycling74.com/userguide/preferences_and_settings/). If you click on the name of an object in the Clue Bar, Max will show you additional information about that object.
![](https://docs.cycling74.com/images/4dce40fe6efcd3478c71ad22af6d71a3_392.webp)
You can set the `@annotation` attribute on an object to customize the text that appears in the _Clue Bar_.
You can enable and disable the [Global Transport](https://docs.cycling74.com/userguide/transport/#accessing-the-global-transport) with the _Transport_ icon near the end of the bottom toolbar.
![](https://docs.cycling74.com/images/d9b2d1d0a6f885ae1267525fe6b1f69d_164.webp)
If you enable the optional _Mute_ and _Solo_ icons, these will appear to the right side of the bottom toolbar. These will let you silence audio in the current patcher, or silence all other non-soloed patchers, respectively.
![](https://docs.cycling74.com/images/3910e0a46a598156c5dc4e00fd7fe8f7_164.webp)
Finally, the _Audio On/Off_ button in the right corner or the bottom toolbar will let you enable or disable audio processing.
![](https://docs.cycling74.com/images/f13655b00d7898ed71862e90b9654609_171.webp)
If you enable local audio processing by way of a [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") object with `@local 1`, or with the `startwindow` message, the _Audio On/Off_ button will glow orange instead of blue.
![](https://docs.cycling74.com/images/8f855b4d7a5c67a1b75c6ca066c2c9d4_262.webp)
## Max for Live Window
The Max patcher window will look slightly different when displaying a [Max for Live](https://docs.cycling74.com/userguide/max_for_live/) device.
![](https://docs.cycling74.com/images/c36256f6e38316be27476b6f93aefb72_345.webp)
While in edit mode, the patcher will show a line indicating the vertical limit of the device. When editing the device directly from Live by pressing the _Edit_ buton, you cannot adjust the height of this line. However, if you open the `.amxd` file in Max, you may adjust the position of this line. Changing the position of this line will not affect the height of the device in Live.
### Toolbar changes
In the bottom toolbar, the _Freeze Device_ button lets you **Freeze** and unfreeze your Max for Live device.
![](https://docs.cycling74.com/images/538bce7a6e5f4897e294a7329d446070_208.webp)
The _Show Containing Project_ button will reveal the [Project](https://docs.cycling74.com/userguide/projects/) that contains the Max for Live device. The project is the place to configure properties of your Live device like whether it is an Audio Effect, MIDI Effect, or a MIDI Instrument, among others.
![](https://docs.cycling74.com/images/ad65ae6492b16eaac315597ad2c95201_331.webp)
Finally, the _Preview_ button will let you enable/disable preview for the Max for Live device (this button is only available when opening a device from Live by pushing the _Edit_ button). With **Preview** enabled, audio and MIDI will pass to and from Live, directly into your Max for Live device as you edit it. With Preview disabled, audio and MIDI will bypass your device until you finish editing it.
![](https://docs.cycling74.com/images/27da270cc94218811beda96816c2cb5c_271.webp)
## Gen Window
The window for a Gen patcher has its own toolbar buttons as well. These let you access the special objects supported in Gen, and give you control over when Gen compiles its code.
### Toolbar changes (Gen)
In the left toolbar, the _Gen Operators_ button gives you access to all of the operators supported in Gen, sorted by category. This will display a different set of objects depending on whether the patcher is a Gen DSP ([gen](https://docs.cycling74.com/reference/gen/ "gen") and [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") objects) or Gen Jitter ([jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix")) patcher.
![](https://docs.cycling74.com/images/11163c86546f65ece1e4a443dac30074_273.webp)
The next button in the left toolbar will be titled either _Gen DSP_ or _Gen Jitter_ , again depending on whether the patcher is a Gen DSP ([gen](https://docs.cycling74.com/reference/gen/ "gen") and [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") objects) or Gen Jitter ([jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen"), [jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"), and [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix")) patcher. This button lets you see built-in `.gendsp` and `.genjit` patchers, which are essentially [Abstractions](https://docs.cycling74.com/userguide/abstractions/) that are restricted to the Gen domain. Many of these Gen Abstractions are helpful starting points or useful building blocks.
![](https://docs.cycling74.com/images/c6d9f81e0a5beabfcad384a09e007769_274.webp)
In the bottom toolbar, the _Enable Auto-Compile_ and _Compile_ buttons let you decide when your patcher compiles. With **Auto-Compile** enabled, your patcher will compile whenever you make a change. If Auto-Compile is disabled, then you can press the _Compile_ button to direct Gen to compile your patcher whenever you're ready. Auto-Compile is enabled by default—disable it if you find that your patcher is taking a long time to compile.
![](https://docs.cycling74.com/images/f60205e1206f3a4a28b49d18f969ef5d_268.webp)
Finally, the _Code_ button in the right toolbar lets you open the **Code** sidebar. This lets you examine the Gen code that is generated from your patcher. If you want, you can copy-paste this into a Gen [codebox](https://docs.cycling74.com/reference/codebox/ "codebox").
![](https://docs.cycling74.com/images/9229e8f6b1f689088045eabdce2390f2_352.webp)
## RNBO window
The RNBO window is very similar to the Gen window, which shouldn't be surprising given that both generate code. The most important difference is the _Export_ button in the right toolbar, which gives you access to the **Export Sidebar**.
### Toolbar changes (RNBO)
In the left toolbar, the _RNBO Objects_ button will open a browser view for objects belonging to RNBO. You can sort these by category and filter them by name.
![](https://docs.cycling74.com/images/ec76be793b1ca58bb0ff11c903e2c122_271.webp)
Similar to Gen, RNBO patcher windows have _Enable Auto-Compile_ and _Compile_ buttons to let you decide when your patcher compiles. With **Auto-Compile** enabled, your patcher will compile whenever you make a change. If Auto-Compile is disabled, then you can press the _Compile_ button to direct RNBO to compile your patcher whenever you're ready. Auto-Compile is enabled by default—disable it if you find that your patcher is taking a long time to compile.
![](https://docs.cycling74.com/images/f60205e1206f3a4a28b49d18f969ef5d_268.webp)
If RNBO encounters an error while trying to compile your patcher, an error indicator will appear in the bottom toolbar. Click on the indicator to display the generated source code, which will show on which line the error occurred.
![](https://docs.cycling74.com/images/0ddbfa4512d6dafc87e2fe89863d537c_306.webp)
Finally, the _Show Export Sidebar_ button in the right toolbar lets you show and hide the **Export Sidebar** , from which you can export your RNBO patcher to any of its supported targets.
![](https://docs.cycling74.com/images/df6d686d8cd78ab408c15b212f3eef18_171.webp)
