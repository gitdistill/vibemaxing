---
description: All of the preferences in Max and their functions
group: Max Interface
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/preferences_and_settings/
title: Preferences
---

# Preferences
Use the **Preferences** window to control the behavior of the whole application, including audio driver settings, the default appearance of the patcher window, the behavior of the Max interface, scheduler parameters, and more. On Mac, _Preferences..._ `⌘``,` (macOS) appears in the application (Max) menu. On Windows, _Preferences..._ `CTRL``,` (Windows) appears in the Options menu.
  * [Audio](https://docs.cycling74.com/userguide/preferences_and_settings/#audio) - Configure audio I/O, sample rate, and other audio performance preferences
  * [Color and Theme](https://docs.cycling74.com/userguide/preferences_and_settings/#color-and-theme) - Choose a preset color scheme
  * [Console](https://docs.cycling74.com/userguide/preferences_and_settings/#console) - Configure the Max Console window
  * [Debugger](https://docs.cycling74.com/userguide/preferences_and_settings/#debugger) - Set the debug event queue size
  * [Files and Folders](https://docs.cycling74.com/userguide/preferences_and_settings/#files-and-folders) - Configure default folders
  * [Interface](https://docs.cycling74.com/userguide/preferences_and_settings/#interface) - Customize the user interface
  * [Jitter](https://docs.cycling74.com/userguide/preferences_and_settings/#jitter) - Select the graphics and video engines
  * [Jweb](https://docs.cycling74.com/userguide/preferences_and_settings/#jweb) - Configure integrated web browsing
  * [Language](https://docs.cycling74.com/userguide/preferences_and_settings/#language) - Localize the user interface
  * [Mixer](https://docs.cycling74.com/userguide/preferences_and_settings/#mixer) - Configure the audio mixer
  * [Mouse Wheel](https://docs.cycling74.com/userguide/preferences_and_settings/#mouse-wheel) - Enable the mouse wheel for zooming
  * [Node for Max](https://docs.cycling74.com/userguide/preferences_and_settings/#node-for-max) - Set options for using Node
  * [OSC](https://docs.cycling74.com/userguide/preferences_and_settings/#osc) - Open Sound Control network setup
  * [Patching](https://docs.cycling74.com/userguide/preferences_and_settings/#patching) - Customize your patching experience
  * [Plugins](https://docs.cycling74.com/userguide/preferences_and_settings/#plugins) - Set up plug-in scanning
  * [RNBO](https://docs.cycling74.com/userguide/preferences_and_settings/#rnbo) - Configure RNBO startup and logging
  * [Recording](https://docs.cycling74.com/userguide/preferences_and_settings/#recording) - Choose the audio quick recording format
  * [Scheduler](https://docs.cycling74.com/userguide/preferences_and_settings/#scheduler) - Customize scheduler performance settings
  * [Text Editing](https://docs.cycling74.com/userguide/preferences_and_settings/#text-editing) - Customize text editing


[Preferences Toolbar](https://docs.cycling74.com/userguide/preferences_and_settings/#preferences-window-toolbar) - Using the Preferences window toolbar
![](https://docs.cycling74.com/images/e526893da4d2c007ecb34dcddcd4e56d_640.webp) The preferences window with the Interface tab active
## Audio
|   
---|---  
Audio Driver | Choose an audio driver from the menu. Mac users will typically use _Core Audio_ while Windows user will use _MME_ (is this right?) or _ASIO_. The _NonRealTime_ driver permits you to capture audio processing to a sound file. For more information on the NonRealTime driver, refer to [Recording](https://docs.cycling74.com/userguide/recording/). To disable audio, choose _None_ as the driver.  
Input Device | Choose a device for audio input. For the selected audio driver, the Input Device menu will display the available audio input devices.  
Output Device | Choose a device for audio output. For the selected audio driver, the Input Device menu will display the available audio output devices.  
Other Driver Options | Depending on the selected audio driver, there may be more options available below the Output Device.  
Sampling Rate | Choose a sampling rate from the menu. Depending on the selected audio driver and hardware devices, the menu may display different available sampling rates. Typical available sampling rates are 44100, 48000, 88200, and 96000 Hz.  
I/O Vector Size | Set the number of samples received and set to the audio driver at one time. Smaller values may be more computationally expensive but typically result in lower I/O latency.  
Signal Vector Size | Set the number of samples computed at one time. Smaller values may be more computationally expensive. The maximum signal vector size is equal to the current I/O vector size. Very small vector sizes (1, 2) may not work properly.  
Overdrive | Set whether the Max scheduler runs in a separate high-priority thread. Overdrive is required for accurate timing.  
Scheduler in Audio Interrupt | Set whether the Max scheduler runs synchronously with audio processing, before each signal vector. When enabled, scheduler events are sample-accurate with respect to audio in most cases.  
CPU Limit | Establish whether audio processing should be skipped if the computation exceeds a set percentage of the available CPU. The default setting of 0 does not limit the amount of audio processing.  
## Color and Theme
|   
---|---  
Color Theme | Select an available [Theme](https://docs.cycling74.com/userguide/customization/themes/) that configures colors used for the user interface. Themes also supply default colors for the patcher and objects.  
Follow Live Theme | Select how Max responds to color theme changes in Live. When set to `On` the color theme selected in Live will be used when Max is launched from Live to edit a Max for Live device. When set to `Persist`, the last color theme selected in Live when Max launched to edit a Max For Live device will be used in Max when it is launched directly as an application. When to `Off` the Live theme will never be used in Max, potentially leading to color differences in the appearance of a device in Live and Max.  
Syntax Color Theme | Select a theme for patcher syntax coloring that overrides the default colors in the chosen theme. When set to _Theme Default_ the default theme colors are used for syntax coloring. Note that the syntax color theme is reset to _Theme Default_ when you choose a different color theme.  
Syntax Coloring | When enabled, text in object boxes will be colorized. The colors used will reflect the curent Color Theme or Syntax Color Theme.  
## Console
|   
---|---  
Max Console Dequeue Chunk Size | The maximum number of lines posted in the [Max Console](https://docs.cycling74.com/userguide/max_console/) per update. Increasing the value above the default (128) will make the console more responsive but could slow down redrawing elsewhere.  
Max Console Font Name | Choose a font for the console from the menu or open the font panel. You can also change the console font and size by choosing Show Fonts from the Object menu when the Max console is the frontmost window.  
Max Console Font Size | Size of the font used in the Max console.  
Max Console Queue Size | The total number of lines to the Max console that can be posted by objects such as [print](https://docs.cycling74.com/reference/print/ "print") before an update occurs.  
## Debugger
|   
---|---  
Illustration Mode Event Queue Size | When using [Illustration Mode](https://docs.cycling74.com/userguide/illustration_mode/) or the debugger, this value, if non-zero, limits the number of pending events stored from actions such as a running [metro](https://docs.cycling74.com/reference/metro/ "metro") object, moving a slider, or incoming MIDI.  
## Files and Folders
|   
---|---  
Add Patchers to the Search Path on Save | If enabled, patcher files outside the [search path](https://docs.cycling74.com/userguide/search_path/) will be added to the search path and become visible in the File Browser.  
Default Folder for Max for Live Device Projects | Newly created Max for Live projects will be saved to this folder by default.  
Default Folder for Projects | Newly created [Projects](https://docs.cycling74.com/userguide/projects/) will be saved to this folder by default.  
Default Patcher Template | The selected [Template](https://docs.cycling74.com/userguide/templates/) will be used each time you create a patcher using New Patcher in the File menu. Any template can be used via the New From Template submenu.  
Save Dependency Paths | When enabled, Max saves the full paths for some dependencies in patcher files. Max can use these paths as a fallback if a file isn't currently in the [search path](https://docs.cycling74.com/userguide/search_path/). Disabling this option is useful for source control applications, so that the contents of a patcher file doesn't change based on the computer or user where it was last edited.  
URL Proxy | Enter a URL to use as a proxy service for web access. This is used by the [maxurl](https://docs.cycling74.com/reference/maxurl/ "maxurl") object as well as other web-based Max features such as the [search sidebar](https://docs.cycling74.com/userguide/sidebar_search/).  
## Interface
|   
---|---  
Arrow Keys Scroll Patcher | When enabled, you can scroll a window using the keyboard arrow keys.  
Clue Bar Shown by Default | When enabled, the Clue Bar will be shown for newly opened patcher windows. Changing this preference will not change the Clue Bar visibility in existing windows.  
Clues in Toolbar | When set to _Enabled_ , clues will be shown in the bottom toolbar and disappear after a few seconds, permitting you to use the documentation menu if shown. When set to _Enabled (Hide on Mouse Over)_ , the clue text will disappear when the cursor enters the bottom toolbar. To show the documentation menu in this case, press the ? or ^ keys while the clue is visible. Clues are always shown in the Clue Bar instead of the bottom toolbar if the Clue Bar is currently visible.  
Check for Updates Automatically | When enabled, Max will alert you if new software updates are available.  
Export Image Resolution (DPI) | Sets the DPI (dots per inch) resolution for PNG images exported from Max via the Export Image... command in the File menu. Supports 72, 96, 150, and 300 DPI.  
Native Font Panel (Mac only) | When enabled, uses the OS font panel instead of the one provided by Max.  
Recover Edits After Crash | Sets how edits to a patcher are restored after a crash. When set to _Always_ , previous patcher edits will be restored when Max is restarted. When set to _Never_ , no edits will be restored. If set to _Ask_ , you'll be prompted at startup whether to restore patcher edits.  
Restore Windows on Launch | If enabled, Max will attempt to re-open all previously open patcher windows when launched.  
Show Scroll Bars | Sets the window scroll bar style. When set to _Dynamically_ , scroll bars appear when using a mouse wheel or mousing over the edge of a window. When set to _Always_ , scroll bars appear if content in a window can be scrolled. When set to _System Default_ , the system-wide user preference determines the scroll bar style.  
Space Bar Accepts Autocompletion | If enabled, a space bar will accept the currently highlighted autocompletion value. If disabled, the space bar will insert a space into an object box without inserting the autocompletion text.  
## Jitter
|   
---|---  
Default Cache Size | Set the default cache size (in gigabytes) for jit.movie and jit.playlist objects when instantiated using viddll the engine.  
Default GL Context | Set the name of the default GL context. When a context is set, any GL or animation object that doesn’t have a user provided context will be added to the default context. A [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world"), [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window"), or [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object of the same name as the default must also be instantiated.  
Graphics Engine | Select the [Graphics Engine](https://docs.cycling74.com/userguide/jitter/graphics_engine/)  
Video Engine | Select the [Video Engine](https://docs.cycling74.com/userguide/jitter/video_engine/)  
## jweb
|   
---|---  
Remote Debugging Port | Sets the remote debugging port for jweb / CEF. After a port is set, restart Max and open a patcher with a jweb object that has web content loaded. Then open a web browser, navigate to `http://localhost:[port number]`, and a link to each jweb instance in max will apear for debugging.  
Force jweb Render Mode | When set to _Onscreen_ or _Offscreen_ , all [jweb](https://docs.cycling74.com/reference/jweb/ "jweb") objects will render in one of these two modes, no matter how they are configured individually. Mostly useful for debugging. Requires a Max restart to take effect.  
## Language
|   
---|---  
Language | Select the language used in the interface. The menu will only show _English (en)_ unless Max was installed with the available Japanese installer.  
## Mixer
|   
---|---  
Enable Mixer Crossfade (Adds Latency) | When set to _On_ , Max will crossfade between new and old versions of your editing operations when audio is turned on.  
Enable Mixer Parallel Processing | When enabled, audio in each top-level patchers will be processed in its own thread.  
Mixer Crossfade Latency | Set the latency of the mixer when crossfading editor operation in milliseconds.  
Mixer Crossfade Ramp Time | Sets the cross-fade time (in milliseconds) used during an editing crossfade (if enabled).  
## Mouse Wheel
|   
---|---  
Mouse Wheel Zoom Direction | If set to _Standard_ , zooming follows the same direction as mouse wheel scrolling. If set to _Reversed_ , zooming increases in the opposite direction to scrolling.  
Mouse Wheel Zoom Sensitivity | Sets the mouse scroll wheel sensitivity when used for zooming in and out of a patcher window. Set to 0 to disable zooming with the mouse wheel.  
## Node for Max
|   
---|---  
Enable Node for Max Logging | When enabled, Node for Max objects will write `console.log` messages to a log file.  
Debug Log Filename | File name of the log file that Node for Max will write, if Node for Max logging is enabled.  
Debug Log Folder | Folder in which Node for Max will write its log file, if Node for Max logging is enabled.  
## OSC
|   
---|---  
Send OSC Default | Enable / disable sending OSC. Can be overridden by each patcher in the patcher inspector.  
Default Remote UDP Address | Remote UDP address to send OSC to when enabled. Can be overridden by each patcher in the patcher inspector.  
Default Remote UDP Port | Remote UDP port to send OSC to when enabled. Can be overridden by each patcher in the patcher inspector.  
Receive OSC Default | Enable / disable listening for OSC. Can be overridden by each patcher in the patcher inspector.  
Default Local UDP Port | Local UDP port to listen for OSC on when enabled. Can be overridden by each patcher in the patcher inspector.  
Enable OSCQuery Server | Enable / disable an http server to serve OSCQuery requests. Individual patchers can add or remove themselves from the list of OSCQuery sources.  
OSCQuery Port | Local http port to listen for OSCQuery requests on.  
OSC Address Prefix Type | What kind of prefix to add, if any, to OSC addresses generated by Max.  
OSC Address Prefix | The prefix to add to OSC addresses generated by Max.  
OSC Value To Send | Whether to send raw (scaled) values, normalized values if they exist, or both.  
Use /param Prefix For Parameters | Whether to add the prefix `/param` to addresses generated by Max.  
OSC Enabled Default | Enable / disable OSC by default for individual objects. Can be overridden in the inspector for each OSC-capable object.  
## Patching
|   
---|---  
Assistance Bubbles | When enabled, bubbles appear to describe an object's inlets and outlets when you move the cursor over them. When disabled, the descriptions appear in the Clue Bar.  
Box Snap Margin | Sets the horizontal snap margin in pixels. The snap margin is the space within which the position or size of an object will automatically be changed to match nearby objects.  
Curved Patch Cords | When disabled, patch cords will be straight and have sharp corners. See examples below of the appearance of patch cords depending on the setting of Curved Patch Cords. ![](https://docs.cycling74.com/images/2c7f55fc290c8781dec32fc1bf324f1c_100.webp) Curved patch cords enabled ![](https://docs.cycling74.com/images/0a02c28d2c5fa1775181ba194d4a8ac9_100.webp) Curved patch cords disabled  
Disable Window Animation (Windows only) | Disabling window animation may improve real-time performance of the application.  
Edit Operations Trigger Loadbang | When enabled, any [loadbang](https://docs.cycling74.com/reference/loadbang/ "loadbang") or [loadmess](https://docs.cycling74.com/reference/loadmess/ "loadmess") objects present in what is pasted or restored when performing an Undo or Redo operation will produce output.  
Enable Patching Mechanics | When enabled, shortcuts as defined in [Patching Mechanics](https://docs.cycling74.com/userguide/patching_mechanics/) will be available.  
Exit on Last Window Closed (Windows only) | When enabled, Max will quit when the last application window is closed. When disabled, the Max console window will appear once all windows are closed to avoid quitting the application.  
High DPI Rendering (Windows only) | On compatible Windows OS versions, enables a higher resolution display for the application which may involve using more than one physical screen pixel per logical pixel. This can improve the appearance of fonts and other graphics at the possible cost of decreated overall graphics performance.  
Keep Duplicated Objects in View | When enabled, duplicated objects will be placed inside the current visible area of the patcher window. When disabled, objects will be dulplicated relative to original object position and may end up outside the visible area of the patcher window.  
Layout Bubbles | When enabled, coordinate information will appear in a bubble when moving or resizing an object. When disable, this information will appear in the Clue Bar.  
Mouse Position Determines Auto-Connection | If enabled, a new auto-connected object will be created just below or above an inlet or outlet that is closest to the current mouse location. If disabled, new auto-connected objects will always connect to the first inlet or outlet, though the object will be created at the mouse location.  
Patch Cord Wiggle Time (ms) | Sets the time, in milliseconds, of the patch cord "wiggle" animation during patching. Set this value to 0 to disable wiggling.  
Prioritize Patch Cords | When enabled, patch cords will be selected if they are over a box.  
Segmented Patch Cords | When enabled, clicking on outlet starts a segmented patch cord. When disabled, you need to shift-click in order to make a segmented cord.  
## Plugins
|   
---|---  
Audio Plug-In Scanning | If set to _Minimal/Fast_ , audio plug-in scanning will look for audio plug-ins files, but will not test or verify them. If set to _Complete/Slow_ , audio plug-in scanning will load and verify each plug-in before making it available to the application. Complete scanning will also scan through "shell" plug-ins that contain multiple other plug-ins.  
Full Scan | Click the _scan_ button to start a manual scan for audio plug-ins.  
## RNBO
|   
---|---  
Start RNBO Server on Launch | When enabled, the RNBO server will start when Max is first launched. When disabled, the RNBO server will not start until the first [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~") object is created.  
RNBO Log Filename | File name of the log file that RNBO will write. If unspecified, RNBO will not write to a log file.  
RNBO Log Folder | Folder in which RNBO will write its log file, if RNBO logging is enabled.  
RNBO Log Level | Set to _Debug_ to log all messages, set to _Error_ to log only error messages.  
## Recording
|   
---|---  
Global Record Format (WAV) | The bit depth and numeric type for audio files recorded with [Global Record](https://docs.cycling74.com/userguide/recording/#global-record)  
Global Record Red Button | When enabled, the Global Record button will be red while recording is active.  
## Scheduler
|   
---|---  
Event Interval (ms) | The approximate minimum time, or throttle limit, (in milliseconds) between handling of low-priority events. For advanced use.  
Overdrive | When enabled, time-critical tasks in the Max scheduler run at a higher priority, increasing timing accuracy.  
Prioritize Scheduler Accuracy Over CPU Usage | When enabled, improves the accuracy of the scheduler potentially at the cost of increased CPU usage. Only relevant when Overdrive is on and Scheduler in Audio Interrupt is off.  
Poll Throttle | The number of events that are handled together in one tick of the scheduler. For advanced use.  
Queue Throttle | The number of events that are handled together at low priority. For advanced use.  
Redraw Queue Throttle | Scheduler performance parameter that sets the maximum number of patcher UI update events to process at a time. Lower values can lead to more processing power available to other low-priority Max processes, and higher values make the user interface more responsive (especially when using many bpatchers). For advanced use.  
Refresh Rate (fps) | The rate limit (in fps) at which Max will update the UI for user interface objects.  
Scheduler Slop (ms) | Scheduler performance parameter that, roughly, balances accuracy with CPU efficiency. For advanced use.  
## Text Editing
|   
---|---  
Always Use External Text Editor | When enabled, Max will use an [external text editor](https://docs.cycling74.com/userguide/external_text_editor/) you specify using the External Text Editor preference when editing text files for objects such as [coll](https://docs.cycling74.com/reference/coll/ "coll") and [dict](https://docs.cycling74.com/reference/dict/ "dict").  
Edit Box Text on Click | When enabled, one click will begin editing the text in an object box, rather than two clicks.  
External Text Editor | Choose an application to use as an [external text editor](https://docs.cycling74.com/userguide/external_text_editor/).  
Typing Edits Selected Box | When enabled, typing with an object selected will automatically start editing that object's text.  
## Preferences Window Toolbar
|   
---|---  
|  **Modify Selected Item** displays a menu for acting on the selected preference. _Copy Attribute_ copies the current value of the preference to the clipboard. _Revert Value_ , which will be enabled if you've changed a preference, restores the value that was set when you first opened the Preferences window.  
|  **Show Preferences Folder** switches to the Finder (Mac) or Explorer (Windows) and opens the Settings folder where Max stores its preferences. The file `maxpreferences.maxpref` contains the settings edited in the Preferences window.  
|  **Audio I/O Mappings** opens an editor window where you can assign virtual channels (those used in [adc~](https://docs.cycling74.com/reference/adc~/ "adc~") and [dac~](https://docs.cycling74.com/reference/dac~/ "dac~")) to real channels on the currently selected audio input and output devices. If you're using stereo audio input and output devices, virtual channels 1 and 2 are assigned to real channels 1 and 2 by default. For more information, refer to [Audio Channels](https://docs.cycling74.com/userguide/audio_channels/).  
|  **Audio Driver Setup** opens Audio MIDI Setup (Mac) or the Sounds and Audio Devices Properties panel (Windows) to configure your audio setup at the operating system level.  
]> |  **Audio On/Off** turns audio on or off globally.
