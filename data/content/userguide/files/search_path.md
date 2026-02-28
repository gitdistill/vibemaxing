---
description: Max finds files by name using the search path, defining where Max looks
group: Files
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/search_path/
title: Search Path
---

# Search Path
The **Search Path** is a collection of folders that Max looks through whenever it needs to find a file. It lets you reference files based on just their name, rather than their absolute path. To locate a file, Max looks in the following places, in order:
  * The folder containing the currently open patch
  * The [**project**](https://docs.cycling74.com/userguide/projects/) to which the current patcher belongs, if any
  * The [Max 9 Folder](https://docs.cycling74.com/userguide/search_path/#max-9-folder), including built-in patches and media, installed [**Projects**](https://docs.cycling74.com/userguide/projects/), and others
  * The folders in the current search path, in order


The [**File Browser**](https://docs.cycling74.com/userguide/file_browser/) lets you search, organize, and filter files in the current search path.
## Editing the Search Path
Edit the search path by selecting _File Preferences..._ from the _Options_ Menu. This will open the _File Preferences_ window.
![](https://docs.cycling74.com/images/ec8c21fa4930f699cb945d7cb0d36d3c_706.webp)
The paths to the folders for _User Library_ , _Global Library_ , _Examples_ , and _Snapshots_ are managed by Max and cannot be modified. If you want Max to search other folders when looking for files, you can add your own folders using this window.
Select any path and click the _Reveal in Finder_ buttom in the bottom toolbar to open that folder in _Finder_ or _File Explorer_.
### Adding a file to the search path
Click on the _Add Path_ button in the bottom-left of the window. This will add a new, empty row to the search path list. Click the _Choose_ button to open a dialog box that lets you browse for the folder you'd like to add to the search path. You can also name your path by double-clicking on the _Name_ field. If you'd like to include subfolders as well, check the _Subfolders_ box.
![](https://docs.cycling74.com/images/c065602b531214df09e338cbb2953975_706.webp)
### Removing a file from the search path
Select any path and click the _Remove Path_ button in the bottom toolbar to remove it from the search path.
### Listing all folders in the search path
You can click the _List Path_ button in the bottom toolbar to list all of the folders currently in the search path. This includes subfolders and can include _a lot_ of folders.
## Max 9 Folder
Max adds a folder to the _Documents_ directory called `Max 9`, containing files of different kinds that get added to Max as you work with it. This folder is located at `%HOMEDRIVE%%HOMEPATH%\Documents\Max 9\Library` on Windows and `~/Documents/Max 9/` on other operating systems.
The _Library_ and _Snapshots_ folders are automatically added to the search path. Folders in the _Paackages_ folder are also added, as each package is loaded.
  * _Collections_ - Collections that you make using the [File Browser](https://docs.cycling74.com/userguide/file_browser/#collections) get stored here
  * _Library_ - This folder is for your use. Whatever files you put in this folder will be included in Max's search path.
  * _Packages_ - Packages instlaled by the [Package Manager](https://docs.cycling74.com/userguide/package_manager/) get installed here.
  * _Palettes_ - Palettes that you create using the Color Picker get stored here.
  * _Projects_ - This is the default location to save [**projects**](https://docs.cycling74.com/userguide/projects/). Max will also unpack [**amxd**](https://docs.cycling74.com/userguide/plugins/#amxd-vs-other-plugins)s here.
  * _Prototypes_ - Any saved [**Prototypes**](https://docs.cycling74.com/userguide/prototypes/) will be stored here.
  * _Recordings_ - The default directory for audio [**Recordings**](https://docs.cycling74.com/userguide/recording/).
  * _Snapshots_ - New [**Snapshots**](https://docs.cycling74.com/userguide/snapshots/) get saved here.
  * _Snippets_ - When you create a [**Snippet**](https://docs.cycling74.com/userguide/snippets/), it gets stored here.
  * _Styles_ - New [**Styles**](https://docs.cycling74.com/userguide/styles/) get saved here.
  * _Templates_ - Saved [**Templates**](https://docs.cycling74.com/userguide/templates/) go to this directory.


## Path Objects
Several objects facilitate working with Max's search path:
Name | Description  
---|---  
[absolutepath](https://docs.cycling74.com/reference/absolutepath/ "absolutepath") | Convert a file name to an absolute path  
[conformpath](https://docs.cycling74.com/reference/conformpath/ "conformpath") | Convert file path styles  
[filepath](https://docs.cycling74.com/reference/filepath/ "filepath") | Manage and report on the Max search path  
[relativepath](https://docs.cycling74.com/reference/relativepath/ "relativepath") | Convert an absolute to a relative path  
[strippath](https://docs.cycling74.com/reference/strippath/ "strippath") | Separate filename from a full pathname  
### Path Prefixes
When resolving a file path, Max can use special path prefixes to locate files relative to a known location. For example, you could use the path `Patcher:/sources/my_patcher.maxpat` to locate a patcher relative to the current patcher, even if the patcher `my_patcher.maxpat` is not in the current [_search path_](https://docs.cycling74.com/userguide/search_path/). This works for all objects that can load files. The [absolutepath](https://docs.cycling74.com/reference/absolutepath/ "absolutepath") and [conformpath](https://docs.cycling74.com/reference/conformpath/ "conformpath") objects can be used to illustrate where Max is resolving these relative paths on disk.
Prefix | Description | Example  
---|---|---  
~: | path relative to the user's home folder | `~:/sources/my_patcher.maxpat`  
C74: | path relative to the Cycling '74 resources folder (on macOS, this is inside the application bundle `Max.app/Contents/Resources/C74/`, on Windows, this is the resources folder next to the `Max.exe` executable) | `C74:/sources/my_patcher.maxpat`  
C74_AU | Max-specific plugin directory for AudioUnit plugins. Mostly used with the `plug` message to [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") to disambiguate plugin types. | `C74_AU:/MyPluginName  
C74_VST | Max-specific plugin directory for VST plugins. Mostly used with the `plug` message to [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") to disambiguate plugin types. | `C74_VST:/MyPluginName  
C74_VST3 | Max-specific plugin directory for VST3 plugins. Mostly used with the `plug` message to [vst~](https://docs.cycling74.com/reference/vst~/ "vst~") to disambiguate plugin types. | `C74_VST3:/MyPluginName  
Usermax: | path relative to the [Max 9 folder](https://docs.cycling74.com/userguide/search_path/#max-9-folder) in the user's Documents folder | `Usermax:/sources/my_patcher.maxpat`  
Desktop: | path relative to the user's Desktop folder | `Desktop:/sources/my_patcher.maxpat`  
Tempfolder: | path relative to Max's temp folder (this folder will be automatically emptied when Max quits) | `Tempfolder:/sources/my_patcher.maxpat`  
Package: | path relative to the package specified in package-name | `Package:/miraweb/misc/app.js`  
Project: | path relative to the project (if any) containing the file loading object | `Project:/sources/my_patcher.maxpat`  
Patcher: | path relative to the patcher (if any) containing the file loading object | `Patcher:/sources/my_patcher.maxpat`  
## Projects
Projects collect and organize dependencies. All files in a given project will be able to locate other files in the same project. In addition, projects support [Project Search Paths](https://docs.cycling74.com/userguide/projects/#project-search-paths), which are extra search path folders specified by that project. For more details, see the documentation for [Projects](https://docs.cycling74.com/userguide/projects/).
Max for Live devices are just projects, and follow the same rules as projects when locating files using the search path.
## Standalones
Search paths in standalones work more or less the same as in regular Max, with a couple of small differences. Check out the documentation for [Standalones](https://docs.cycling74.com/userguide/standalones_and_collectives/) for more details.
