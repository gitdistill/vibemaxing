---
description: Sending messages direclty to the global max object, to script and control the whole application
group: Scripting
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/controlling_max_with_messages/
title: Controlling Max with Messages
---

# Controlling Max with Messages
Just like you can control objects by sending them messages, you can also send messages directly to the Max application. This lets you do things like:
  * Get/set the value of various [**Max Preferences**](https://docs.cycling74.com/userguide/preferences_and_settings/)
  * List all of the currently loaded Max externals
  * Move the mouse cursor
  * Hide/show the menu bar


To send a message directly to Max, create a message box starting with a semicolon followed by the symbol `max`, `jitter`, or `dsp`, to send a message directly to max itself, the Jitter engine, or the audio engine. You don't need to connect the message box to anything, simply trigger it to send the message.
![](https://docs.cycling74.com/images/08a926027b27f0755b808893c5260224_339.webp) Messages boxes beginning with a semicolon send their message directly to the Max application
## Messages to `max`
### buildcollective
Builds a collective using a patcher previously opened with [openfile](https://docs.cycling74.com/userguide/controlling_max_with_messages/#openfile). The collective is named with the output filename. The filename should be a full path (e.g. `Desktop/somecollective.mxf`), and it must have the `.mxf` extension.
; max buildcollective patchername outputfile  Name | Type | Description  
---|---|---  
patchername | symbol | The symbol associated with the patcher that should be bundled into a collective  
outputfile | symbol | Name of the output file  
### checkpreempt
Sends the current Overdrive mode to a [receive](https://docs.cycling74.com/reference/receive/ "receive") object
; max checkpreempt $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### clean
Clear the dirty flag, causing Max not to show a _Save Changes_ dialog when you close a window or quit, even if there are patchers that have been modified. This is useful in conjunction with the [quit](https://docs.cycling74.com/userguide/controlling_max_with_messages/#quit) message below.
; max clean 
### clearmaxwindow
Clear the Max Console.
; max clearmaxwindow 
### closefile
Closes a patcher file previously opened with the [openfile](https://docs.cycling74.com/userguide/controlling_max_with_messages/#openfile)
; max closefile $patchername  Name | Type | Description  
---|---|---  
patchername | symbol | Symbol associate with the file  
### crash
Terminate Max, generating a standard crashlog. When relaunched, The Max application will perform standard crash recovery (if crash recovery is enabled in the Max preferences).
; max crash 
### db.exportmetadata
Write the metadata information currently stored in the database to a file. An optional argument can be used to specify a filename. If no filename is specified, the metadata is backed up to a file in your preferences folder.
; max db.exportmetadata $filename  Name | Type | Description  
---|---|---  
filename | symbol | (optional) backup file filename  
### db.importmetadata
Load metadata information from a previously stored file into the Max database. An optional argument can be used to specify a filename - when no argument is specified, Max will look for a backup file from a previous call to db.exportmeta in your preferences folder.
; max db.importmetadata $filename  Name | Type | Description  
---|---|---  
filename | symbol | (optional) backup file filename  
### db.reset
Rebuild the internal database, used by the [**File Browser**](https://docs.cycling74.com/userguide/file_browser/) and others.
; max db.reset 
### debug
Enable/disable sending Max's internal debugging output to the Max Console. This debug information may be of limited use for anyone who isn't debugging Max itself.
; max debug $onoff  Name | Type | Description  
---|---|---  
onoff | number | 0 or 1 to enable/disable debug messages  
### disablevirtualmididestinations
Activate to disable the creation of virtual sources by the Core MIDI driver. When set to zero (enabling virtual sources) the virtual sources are created again.
; max disablevirtualmididestinations $offon  Name | Type | Description  
---|---|---  
offon | number | 0 or 1 to disable/enable virtual sources  
### enablepathcache
Enable/disable Max's search path cache. This should only be done if you notice unusual behavior when opening files.
; max enablepathcache $onoff  Name | Type | Description  
---|---|---  
onoff | number | 0 or 1 to enable/disable path cache  
### externaleditor
Sets the text editor used for editing text file content, such as saved coll files, text files and JavaScript code.
; max externaleditor $editorname  Name | Type | Description  
---|---|---  
editorname | symbol | Name of the external text editor  
### externs
Print all of the external objects currently loaded to the [**Max Console**](https://docs.cycling74.com/userguide/max_console/).
; max externs 
### fileformat
Associate a filename extension with a particular four-character [**filetype**](https://docs.cycling74.com/userguide/filetypes/). For example, the message `max fileformat .tx TEXT` associates the extension .tx with TEXT (text) files. This allows a user to send a message `read george` and locate a file with the name `george.tx`. It also ensures that files with the extension `.tx` will appear in a standard open file dialog where text files can be chosen.
; max fileformat extension filetype  Name | Type | Description  
---|---|---  
extension | symbol | File extension to associate with a character code  
filetype | symbol | Filetype character code  
### fixwidthratio
Set the ratio of the box to the width of the text when the user chooses _Fix Width_ from the _Object_ menu. The default value is 1.0. A value of 1.1 would make boxes wider than they needed to be, and a value of 0.9 would make boxes narrower than they need to be.
; max fixwidthratio $ratio  Name | Type | Description  
---|---|---  
ratio | number | box width to text width ratio  
### getarch
Send the currently running Max architecture (always 'x64') to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object.
; max getarch $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getdefaultpatcherheight
Send the current default patcher height in pixels to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object (See also the [setdefaultpatcherheight](https://docs.cycling74.com/userguide/controlling_max_with_messages/#setdefaultpatcherheight) message to Max.)
; max getdefaultpatcherheight $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getdefaultpatcherwidth
Send the current default patcher width in pixels to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object (See also the [setdefaultpatcherheight](https://docs.cycling74.com/userguide/controlling_max_with_messages/#setdefaultpatcherwidth) message to Max.)
; max getdefaultpatcherwidth $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getenablepathcache
Report whether the path cache is enabled to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object. (See also the [enablepathcache](https://docs.cycling74.com/userguide/controlling_max_with_messages/#enablepathcache) message to Max.)
; max getenablepathcache $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### geteventinterval
Report the event interval to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object. (See also the [seteventinterval](https://docs.cycling74.com/userguide/controlling_max_with_messages/#seteventinterval) message to Max.)
; max geteventinterval $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getfixwidthratio
Report the current fix width ratio value to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object. (See also the [fixwidthratio](https://docs.cycling74.com/userguide/controlling_max_with_messages/#fixwidthratio) message to Max.)
; max getfixwidthratio $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getpollthrottle
Report the current poll throttle value to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object. (See also the [setpollthrottle](https://docs.cycling74.com/userguide/controlling_max_with_messages/#setpollthrottle) message to Max.)
; max getpollthrottle $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getqueuethrottle
Report the current queue throttle value to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object. (See also the [setqueuethrottle](https://docs.cycling74.com/userguide/controlling_max_with_messages/#setqueuethrottle) message to Max.)
; max getqueuethrottle $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getrefreshrate
Report the current refresh rate in frames per second (fps) to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object. (See also the [refreshrate](https://docs.cycling74.com/userguide/controlling_max_with_messages/#refreshrate) message to Max.)
; max getrefreshrate $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getruntime
Send a 1 to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object if the current version of Max is a runtime version, and a 0 if not.
; max getruntime $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getslop
Send the scheduler slop value to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object. (See also the [setslop](https://docs.cycling74.com/userguide/controlling_max_with_messages/#setslop) message to Max.)
; max getslop $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getsysqelemthrottle
Send the maximum number of patcher UI update events processed at a time to the named receive object. (See also the [setsysqelemthrottle](https://docs.cycling74.com/userguide/controlling_max_with_messages/#setsysqelemthrottle) message to Max.)
; max getsysqelemthrottle $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getsystem
Send the name of the system (macintosh or windows) to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object.
; max getsystem $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### getversion
Send the Max version number as a decimal value, which needs to be converted to a hexidecimal value (e.g. Max version 7.3.4 is reported as '1844'), and output from the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object.
; max getversion $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### hidecursor
Hides the cursor if it is visible.
; max hidecursor 
### hidemenubar
Hides the menu bar.
; max hidemenubar 
### htmlref
Look for a file called `<filename>.html` in the search path. If found, a web browser is opened to view the page. This opens _local_ html files, not remote web addresses.
; max htmlref $filename  Name | Type | Description  
---|---|---  
filename | symbol | Name of the file to open  
### launchbrowser
Opens a web browser to view the given URL.
; max launchbrowser $url  Name | Type | Description  
---|---|---  
url | symbol | URL to open  
### maxcharheightforsubpixelantialiasing
Set a threshold font size (in points) for native subpixel aliasing. Since the look of subpixel antialiasing may be undesirable when working with large fonts as compared to regular antialiasing, this attribute lets you specify a threshold font size; if a font is larger than the specified size, it will be rendered using regular rather than subpixel antialiasing.
Note that Max honors your computer's system preferences - Max won't use subpixel aliasing if you've disabled it for your system. Setting this attribute value to zero value is 0 will always use regular antialiasing, and setting a very high value will always use subpixel antialiasing (unless it is disabled in system preferences).
; max maxcharheightforsubpixelantialiasing $pointheight  Name | Type | Description  
---|---|---  
pointheight | number | threshold font size (in points) for native subpixel aliasing  
### maxinwmenu
Enable/disable the special _Status_ option in the _Window_ menu bar item. This is only available when using runtime version of Max _and_ an active custom menubar object. The _Status_ option will allow users to see the [Max Console](https://docs.cycling74.com/userguide/max_console/). Defaults to 1 (enabled).
; max maxinwmenu $onoff  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable the _Status_ option to show the Max Console  
### maxwindow
Displays the Max Console. If the Max Console if not currently open, the window will be displayed. If the window is currently open, it will bring it to the front.
; max maxwindow 
### midilist
Prints the names of all current MIDI devices in the [Max Console](https://docs.cycling74.com/userguide/max_console/). (See also MIDI Messages to Max, below.)
; max midilist 
### notypeinfo
(macOS only) Enable/disable saving files with traditional macOS four-character type information. By default, Max does save this information in files.
; max notypeinfo $onoff  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable saving files with traditional macOS four-character type information  
### objectfile
The word objectfile, followed by two symbols that specify an object name and a file name, Create a mapping between an external object and its filename. For example, the [*~](https://docs.cycling74.com/reference/*~/ "*~") object is in a file called `times~` so at startup Max executes the command `max objectfile *~ times~`.
; max objectfile objectname filename  Name | Type | Description  
---|---|---  
objectname | symbol | Name of the object to associate  
filename | symbol | External object filename to associate  
### openfile
The word openfile, followed by two symbols that specify an reference name and a file name or path name, attempts to open the patcher with the specified name. If successful, the patcher is associated with the reference symbol, which can be passed as argument to the [buildcollective](https://docs.cycling74.com/userguide/controlling_max_with_messages/#buildcollective) and [closefile](https://docs.cycling74.com/userguide/controlling_max_with_messages/#closefile) messages to Max. The `openfile` message is intended for batch collective building.
; max openfile namehandle filename  Name | Type | Description  
---|---|---  
namehandle | symbol | Name to associate with the open patcher  
filename | symbol | Name of the patcher to open  
### paths
List the current search paths in the Max Console. There is a button in the File Preferences window that does this.
; max paths 
### preempt
Toggle [Overdrive](https://docs.cycling74.com/userguide/scheduler/#overdrive) mode.
; max preempt $onoff  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable overdrive  
### pupdate
Move the mouse cursor to a global screen position.
; max pupdate xposition yposition  Name | Type | Description  
---|---|---  
xposition | number | Horizontal screen coordinate  
yposition | number | Vertical screen coordinate  
### purgemididevices
Purge the missing MIDI device cache. Max maintains a cache of the MIDI Setup settings for known, but detached MIDI devices. Send this message to 'forget' any missing devices.
; max purgemididevices 
### quit
Quit the Max application, equivalent to choosing _Quit_ from the _File_ menu. If there are unsaved changes to open files, and you haven't sent Max the [clean](https://docs.cycling74.com/userguide/controlling_max_with_messages/#clean) message, Max will ask whether to save changes.
; max quit 
### refresh
Update all Max consoles.
; max refresh 
### refreshrate
Set the rate limit, in frames per second, at which the UI for user interface objects is updated. Better visual performance can be achieved - at the cost of a slight performance decrease in Jitter, and little or no performance decrease for audio processing - by specifying a higher frame rate.
; max refreshrate $rate  Name | Type | Description  
---|---|---  
rate | number | Refresh rate (fps)  
### relaunchmax
Close and relaunch the Max application.
; max relaunchmax 
### runtime
Conditionally send a message to Max if the given value matches the "runtime" status of Max. For example, the message `; max runtime 0 externs` will send the `externs` message to Max _only_ if the active Max application is not a runtime-only version.
; max runtime runtimeflag message  Name | Type | Description  
---|---|---  
runtimeflag | number | Flag to match for the current runtime status  
message | symbol | Message to send if the runtime flag matches  
### sendinterval
Send the current scheduler interval to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object.
; max sendinterval $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### sendapppath
Send the path of the Max application to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") object.
; max sendapppath $receive  Name | Type | Description  
---|---|---  
receive | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### setdefaultpatcherheight
Set the default patcher height in pixels. Must be greater than 100.
; max setdefaultpatcherheight $height  Name | Type | Description  
---|---|---  
height | symbol | Default patcher height  
### setdefaultpatcherwidth
Set the default patcher width in pixels. Must be greater than 100.
; max setdefaultpatcherwidth $width  Name | Type | Description  
---|---|---  
width | symbol | Default patcher width  
### seteventinterval
Set the time between invocations of the event-level timer (The default value is 2 milliseconds). The event-level timer handles low priority tasks like drawing user interface updates and playing movies.
; max seteventinterval $interval  Name | Type | Description  
---|---|---  
interval | symbol | Low priority timer interval  
### setmixergbitmode
Set the state of the Enable Mixer Crossfade preference for top-level patcher mixers. A value of 0 sets the preference to `Off`, 1 to `On`, and 2 to `Auto`.
; max setmixergbitmode $mode  Name | Type | Description  
---|---|---  
mode | number | Enable Mixer Crossfade preference  
### setmixerlatency
Set the Mixer Crossfade Latency preference for top-level patcher mixers to the specified number of milliseconds.
; max setmixerlatency $latency  Name | Type | Description  
---|---|---  
latency | number | Mixer latency in milliseconds  
### setmixerparallel
Enable/disable the Enable Mixer Parallel Processing preference for top-level patcher mixers.
; max setmixerparallel $onoff  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable mixer parallel processing  
### setmixerramptime
Set the Mixer Crossfade Ramp Time preference for top-level patcher mixers to the specified number of milliseconds.
; max setmixerramptime $time  Name | Type | Description  
---|---|---  
time | number | Ramp time in milliseconds  
### setmirrortoconsole
Enable/disable mirroring of Max Console posts to the system console (default off). The system console is available on macOS using Console.app, or on Windows using the DbgView program (free download from Microsoft).
; max setmirrortoconsole $onoff  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable mirror to system console  
### setsleep
Set the time between calls to get the next system event, in 60ths of a second. The default value is 2.
; max setsleep $interval  Name | Type | Description  
---|---|---  
interval | number | Interval in 60ths of a second between system event polls  
### setpollthrottle
Set the maximum number of events the [**scheduler**](https://docs.cycling74.com/userguide/scheduler/) executes each time it is called (The default value is 20). Setting this value lower may decrease accuracy of timing at the expense of efficiency.
; max setpollthrottle $chunksize  Name | Type | Description  
---|---|---  
chunksize | number | Number of events the executed per scheduler tick  
### setqueuethrottle
Set the maximum number of events handled at low-priority each time the low-priority queue handler is called (The default value is 2). Changing this value may affect the responsiveness of the user interface.
; max setqueuethrottle $chunksize  Name | Type | Description  
---|---|---  
chunksize | number | Number of events executed per low-priority queue handler tick  
### setslop
Set the scheduler slop value - the amount of time a scheduled event can be earlier than the current time before the time of the event is adjusted to match the current time. The default value is 25 milliseconds.
; max setslop $slop  Name | Type | Description  
---|---|---  
slop | number | Slop time in milliseconds  
### setsysqelemthrottle
Set the maximum number of patcher UI update events to process at a time. Lower values can lead to more processing power available to other low-priority Max processes, and higher values make the user interface more responsive (especially when using many bpatchers).
; max setsysqelemthrottle $chunksize  Name | Type | Description  
---|---|---  
chunksize | number | Number of patcher UI events to process per tick  
### showcursor
Show the cursor if it is hidden.
; max showcursor 
### showmenubar
Show the menu bar if it was hidden with [hidemenubar](https://docs.cycling74.com/userguide/controlling_max_with_messages/#hidemenubar)
; max showmenubar 
### size
Print the number of symbols in the symbol table in the Max Console.
; max size 
### system
Conditionally send a message to Max if the Operating System condition matches. The operating system can be `windows` or `macintosh`. For example, the message `; max system windows externs` will send the message `externs` to Max only on a Windows operating system.
; max system systemflag message  Name | Type | Description  
---|---|---  
systemflag | number | Flag to match for the current operating system `windows` or `macintosh`  
message | symbol | Message to send if the system flag matches  
### useexternaleditor
Enable/disable using an external editor for text. If enabled, any situation where an external editor can be used will launch the editor. If disabled, an external editor will only be used when selected from the menu.
; max useexternaleditor $onoff  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable the external editor  
### useslowbutcompletesearching
Enable/disable complete file searching. When enabled, it causes files not found in Max's cache of the search path to be searched in the file system. This is necessary only in extremely rare cases where the file cache does not update properly. One such case is copying a file into the search path using a version of the Mac OS prior to 10.5.5 over a network. This option may cause patcher files to be loaded more slowly. The setting defaults to off with each launch of the application, and is not stored in the user's preferences.
; max useslowbutcompletesearching $onoff  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable the complete file searching  
## MIDI Configuration Messages
### createoutport
Creates a new port for the specified driver. This is only possible on macOS machines. Windows is unsupported. On macOS, specifying the `coremidi` driver name creates a virtual output port you can use to communicate with other MIDI applications, while specifying the `augraph` driver name creates another port exclusively assigned to the DLS synthesizer.
;#SM createoutport portname drivername  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port to create  
drivername | symbol | Name of the driver to create  
### deleteoutport
On macOS, deletes a port created with the [createoutport](https://docs.cycling74.com/userguide/controlling_max_with_messages/#createoutport) message. `drivername` and `portname` should be the same as the arguments originally passed to `createoutport`.
;#SM deleteoutport portname drivername  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port to delete  
drivername | symbol | Name of the driver to delete  
### driver loadbank
On macOS, loads a type 1 or 2 DLS Bank, where `filename` is the name of an existing DLS bank file, and `portname` is the name of the port that will use this bank. If portname is omitted, all DLS ports will use the bank. The folder `/Library/Audio/Sounds/Banks` is added to the search path when looking for a DLS bank file.
;#SM driver loadbank filenaem portname  Name | Type | Description  
---|---|---  
filename | symbol | Name of the DLS bank file to load  
portname | symbol | Name of the port that will use the bank  
### driver loadbank 0
Load the default General MIDI DLS bank
;#SM driver loadbank 0 $portname  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port that will use the bank  
### driver reverb
Enable/disable reverb. Off by default in `augraph`
;#SM driver reverb onoff portname  Name | Type | Description  
---|---|---  
onoff | number | Enable/disable reverb  
portname | symbol | Name of the port  
### driver latency
(midi_mme only) Set the MIDI Output Latency in milliseconds
;#SM driver latency mstime portname  Name | Type | Description  
---|---|---  
mstime | number | Latency in milliseconds  
portname | symbol | Name of the port  
### inportinfo
Send information about MIDI input ports to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") objects. The information is contained in an list message with the following elements:
Element | Type  
---|---  
the port's name | symbol  
the port's driver name | symbol  
the port's unique ID | int  
the port's abbreviation | int  
the port's channel offset | int  
whether the port is enabled or disabled | one if enabled, zero if disabled  
whether the port was created dynamically | one if yes, zero if no  
;#SM inportinfo portname receivename  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port  
receivename | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### outportinfo
Send information about MIDI output ports to the named [receive](https://docs.cycling74.com/reference/receive/ "receive") objects. The information is contained in an `infolist` list message. See [inportinfo](https://docs.cycling74.com/userguide/controlling_max_with_messages/#inportinfo) for a description if the `infolist` list elements.
;#SM outportinfo portname receivename  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port  
receivename | symbol | Name of the target [receive](https://docs.cycling74.com/reference/receive/ "receive") object  
### createinport
(macOS only) Add a virtual MIDI input port, where `portname` is the name you assign to the port, and drivername should be set to `coremidi`. Other MIDI applications can send messages to Max using this port.
;#SM createinport portname drivername  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port to create  
drivername | symbol | Name of the driver, should always be `coremidi`  
### deleteinport
Deletes a port created with the [createinport](https://docs.cycling74.com/userguide/controlling_max_with_messages/#createinport) message. `drivername` and `portname` should be the same as the arguments originally passed to `createinport`.
;#SM deleteinport portname drivername  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port to create  
drivername | symbol | Name of the driver, should always be `coremidi`  
Ports created with the `createoutport` and `createinport` messages are not saved as a part of your MIDI setup preferences.
## Messages to `midi`
These are technically messages to Max, but specifically to MIDI configuration object owned by Max. So to send one of these messages, use a format like:
; max midi <message> <message-arguments>
### portabbrev
Set the abbreviation for a given MIDI port.
; max midi portabbrev inorout portname $abbrev  Name | Type | Description  
---|---|---  
inorout | symbol | Must be `innum` for an input port or `outnum` for an output port  
portname | symbol | Name of the port  
abbrev | number | The abbrevation to use for the port. 0 is for no abbrev (- in menu), 1 for 'a' and 26 for 'z'.  
### portenable
Enable/disable a given MIDI port. All ports are enabled by default.
; max midi portenable portname onoff $inorout  Name | Type | Description  
---|---|---  
portname | symbol | Name of the port  
onoff | number | 1 for enable, 0 for disable  
inorout | number | 1 for output, 0 for input  
### portoffset
Similar to [portabbrev](https://docs.cycling74.com/userguide/controlling_max_with_messages/#portabbrev), but offset is the channel offset added to identify input or output ports when a MIDI object can send to or receive from multiple ports by channel number. Must be a multiple of 16 (e.g. `max midi portoffset innum PortA 16` sets the channel offset for PortA device to 16).
; max midi portoffset inorout portname $offset  Name | Type | Description  
---|---|---  
inorout | symbol | Must be `innum` for an input port or `outnum` for an output port  
portname | symbol | Name of the port  
abbrev | number | The port offset, which must be a multiple of 16.  
## Messages to `dsp`
### cpulimit
Sets a utilization limit for the CPU. Above this limit, MSP will not process audio vectors until the utilization comes back down, causing a click. If the cpu limit is set to either 0 or 100, there will be no limit checking done.
; dsp cpulimit $limit  Name | Type | Description  
---|---|---  
limit | number | The cpu limit in a range of `[0-100]`  
### inremap
Maps a physical device input channel to a logical input channel.
; dsp inremap physical_input logical_input  Name | Type | Description  
---|---|---  
physical_input | int | Physical device input number  
logical_input | int | Logical device input number  
### iovs
Sets the I/O vector size.
; dsp iovs $size  Name | Type | Description  
---|---|---  
size | type | Vector Size, should be a power of 2  
### open
Opens the Audio Status window.
; dsp open 
### outremap
Maps a physical device output channel to a logical output channel.
; dsp outremap physical_output logical_output  Name | Type | Description  
---|---|---  
physical_output | int | Physical device output number  
logical_output | int | Logical device output number  
### set
Turns the audio on (`1`) or off (`0`). It is equivalent to clicking on a [ezadc~](https://docs.cycling74.com/reference/ezadc~/ "ezadc~") or [ezdac~](https://docs.cycling74.com/reference/ezdac~/ "ezdac~") object.
; dsp set $status  Name | Type | Description  
---|---|---  
status | int | New audio status - on / off  
### setdriver
Sets a new audio driver based on its index into the currently generated menu of drivers created by he [adstatus](https://docs.cycling74.com/reference/adstatus/ "adstatus") driver object.
If the argument is a symbol instead of an index and names a valid driver, the new driver is selected by name. An additional symbol argument may be used to specify a "subdriver" (for example, ASIO drivers use _ASIO_ as the name of the driver and _PCI-324_ as a subdriver name that specifies a specific device).
; dsp setdriver index subdriver_name  Name | Type | Description  
---|---|---  
index | int or symbol | The index or name of the driver  
_optional_ subdriver_name | int or symbol | The name of the subdriver  
### sigvs
Sets the I/O signal vector size.
; dsp sigvs $size  Name | Type | Description  
---|---|---  
size | type | Vector Size, should be a power of 2  
### sr
Sets a new sampling rate in Hertz.
; dsp sr $samplerate  Name | Type | Description  
---|---|---  
samplerate | number | Samplerate in Hertz  
### start
Turns the audio on.
; dsp start 
### status
Opens the Audio Status window.
; dsp status 
### stop
Turns the audio off.
; dsp stop 
### takeover
Turns Scheduler in Audio Interrupt mode on (`1`) or off (`0`). It is equivalent to clicking on the `Audio Interrupt` checkbox in the Audio Status window. `Overdrive` must be on in order for this change to be reflected.
; dsp takeover $status  Name | Type | Description  
---|---|---  
status | int | On (`1`) or off (`0`)  
### timecode
Starts (`1`) or stops (`0`) timecode reading by any audio drivers that support the feature (ASIO 2).
; dsp timecode $status  Name | Type | Description  
---|---|---  
status | int | Start (`1`) or stop (`0`) reading  
### wclose
Closes the Audio Status window.
; dsp wclose 
## Messages to `jitter`
### cursor
Macintosh only
Toggles cursor visibility on / off.
; jitter cursor $status  Name | Type | Description  
---|---|---  
status | int | On (`1`) or Off (`0`)  
### html_ref
Launches the reference file for an object in the Max search path.
; jitter html_ref $name  Name | Type | Description  
---|---|---  
name | symbol | Name of the object  
### javaload
Toggles Jitter Java support on / off.
; jitter javaload $status  Name | Type | Description  
---|---|---  
status | int | On (`1`) or Off (`0`)  
### launch_browser
Launches the specified URL in the default system web browser.
; jitter launch_browser $url  Name | Type | Description  
---|---|---  
url | symbol | URL to open  
### menubar
Macintosh only
Toggles menubar visibility on or off. Similar to Max's `showmenubar` , and `hidemenubar` messages.
When using in conjunction with the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object's fullscreen attribute, it is recommended that the [jit.window](https://docs.cycling74.com/reference/jit.window "jit.window") object's _fsmenubar_ attribute is used instead of Jitter's `menubar` message, in order to prevent possible "pixel trash".
; jitter menubar $status  Name | Type | Description  
---|---|---  
arg | int | On (`1`) or Off (`0`)  
### parallel
Toggles parallel processor support. The default is on if the machine has multiple processors (or cores), and otherwise off.
; jitter parallel $status  Name | Type | Description  
---|---|---  
arg | int | On (`1`) or Off (`0`)  
### parallelthreads
Specifies the number of threads used for parallel processor support. Default is the number of processors (or cores).
; jitter parallelthreads $count  Name | Type | Description  
---|---|---  
count | int | Number of threads to use  
### parallelthresh
Specifies matrix cellcount above which parallel processors are used. Default is 10000 cells.
; jitter parallelthresh $cellcount  Name | Type | Description  
---|---|---  
cellcount | type | Treshold at which parallel processors are used.  
### pollthrottle
Sets the number of scheduler events to process per scheduler tick. Equivalent to Max's `setpollthrottle` message.
; jitter pollthrottle $count  Name | Type | Description  
---|---|---  
count | int | Events to process per scheduler tick  
### queuethrottle
Sets the number of low priority queue events to process per low priority queue service. Equivalent to Max's `setqueuethrottle` message.
; jitter queuethrottle $count  Name | Type | Description  
---|---|---  
count | int | Number of low priority queue events to process
