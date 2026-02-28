---
description: Organize together multiple patchers, along with their dependencies, into a project. Projects make it easy to share complex patchers with lots of media files
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/projects/
title: Projects
---

# Projects
**Projects** collect and organize dependencies associated with a patcher or set of patches. These dependencies can include patches, media files, code, and third-party externals.
Projects also extend the main Max [**search path**](https://docs.cycling74.com/userguide/search_path/). All files in a project can locate other files in the same project.
  * Project-specific elements are loaded before any other files on the Max search path.
  * Project-specific assets don't have to be added to the main Max search path, isolating them from other patches and Projects.
  * You can switch between global and Project-local assets.
  * Using projects lets you reduce the number of folders in Max's global search, which can improve patcher loading and editing speed.


## Creating Projects
You can start with a new empty project, or create a project from an existing patcher.
  * To create a new empty project, choose _New Project_ from the _File_ menu. This action creates a Max Project at the location specified. By default, this is `~/Documents/Max/Projects` (Mac) or `(User Folder)\My Documents\Max\Projects` (Win). Projects can be saved anywhere, but it is recommended to use the default location.
  * To create a project from your existing open patcher, choose _Save as Project_ from the _File_ menu. This will close and re-open your patcher as a project.


Once the project is created, you don't need to save it: projects are saved automatically as you edit them.
## Project Window
![Project Window](https://docs.cycling74.com/images/661d1b6f8cd0e7698a93d6cc90adf2d1_412.webp)
  1. Category header: Files in your project are automatically assigned to a category, like "Patchers", "Media", "Code", or "Data". Categories are only shown if there are matching files in the project.
  2. Patcher opened with project: A project may contain one or more "top-level patchers". These are displayed in bold in the _Project_ window, and are automatically opened when the project is loaded.
  3. Dependencies: Files local to a project are shown in regular, non-italic text. Dependencies of project files are shown in a darker color, and if those files are only found on the global Max search path, they are shown in italics. Dependencies cannot be removed from a project from the _Project_ pindow.
  4. Add files to Project: To add files to a project, they can be created from scratch, patchers can be created from templates, and existing files can be added to projects. Files can be removed by right-clicking on the file name in the _Project_ window and selecting "Remove from Project." Alternatively, you can highlight the name and use the backspace or delete key on your keyboard.
  5. Details view: When toggled on and a file from the list is selected, details about the file are shown, including the name, kind and absolute path of the file. If the file is a dependency (whether explicit or implicit), a link is shown to highlight the patchers in the file list which use it. Also shown is whether the file is opened with the project or not.
  6. Hierarchical and flat view modes: Hierarchical view lists all dependencies underneath the file which depends on them. Flat view sorts all files, whether dependencies or not, into a flat list.
  7. Manage project: From the _Manage Project_ menu, you can 
     * consolidate and deconsolidate. Consolidation copies all dependencies to the local project folder. De-consolidation removes any files which can be found on the global Max search path from your local project directory.
     * archive. Similar to consolidation, archiving creates a copy of all files needed by the project. Unlike consolidation, archiving creates a new ".maxzip" archive file that can be saved and distributed as a single file.
     * build collectives and applications.
     * export as a Max for Live device.
  8. Project settings: Open the _Project Inspector_ window, the _Project Seach Path_ window, or the _Open Actions_ text window.
  9. Reload Project: Refreshes the _Project_ window.
  10. Show Project folder: Opens the project's location on disk.


## Project Inspector
The Project Inspector allows you to set preferences for the project's behavior.
  * Always Localize Project Items: When enabled, files added to a project will always be copied to the project's folder before being included in the project. (default = off)
  * Hide Project Window After Opening: When enabled (and only if the project contains patchers which are marked "Open on Project Load"), the project window will not be visible after the Project opens. You can open the _Project_ window later by click on the _Show Containing Project_ button in the patcher's toolbar. (default = off)
  * Keep Project Folder Organized: When enabled, files in the project's folder are automatically sorted into appropriate subfolders based on the file's category. (default = on)
  * Show Patcher Dependencies: When enabled, implicit dependencies are displayed in the _Project_ window. (default = on)
  * Development Path Type: When enabled, allows you to specify the path type for the folder specified in the Development Path setting. Options are disabled, relative, and absolute.
  * Development Path: Allows you to choose a project-specific folder for development of Max for Live projects. When set, all device files for the project will be saved to and referenced from this location. When disabled, the project uses the global folder `~/Documents/Max 8/Max for Live Devices` (Mac) or `(User Folder)\My Documents\Max 8\Max for Live Devices` (Win).


## Editing Files in a Project
To edit a patcher or text file from a project, double-click on the file's name in the project window. Alternatively, right-click on the file's name in the project window and choose Open from the contextual menu.
When editing a patcher from a project, a new icon will appear in the bottom toolbar. You can use this icon to return to the project window from the patcher.
![](https://docs.cycling74.com/images/fabe07574f6aa7408c867cf0beaaea05_732.webp)
If you edit a patcher by opening the patcher file directly, rather than opening the parent project first, Max won't be able to use the project context to resolve any [_search path_](https://docs.cycling74.com/userguide/search_path/) dependencies. Some dependencies may be found in the wrong location (globally rather than project-locally), and some may not be found at all. For this reason, if you're working with a project, be sure to open the project before editing any child patchers.
## Project Search Paths
Within a project, patchers and other kinds of files may be marked either global or local. Files marked global tell Max to use the file found on the global search path, if available. Files marked local tell Max to use the file found on the Project's search path first, if available. You also have the ability to publish a file to the global search path or to localize a file to your project's search path.
The project-local search path consists of:
  1. Project-local folders: Projects maintain a folder on your hard drive. The contents of this folder (and its subfolders) are preferentially searched when Max is looking for files requested by project members. New files added to a project are created inside this folder by default, and you can manually add files to it, too.
  2. Singleton folders: Projects can reference files which are neither in the Max global search path, nor in the project folder. When searching for files, the folders containing these "singletons" are searched (non-recursively), as well.
  3. Project search paths: Projects also maintain a list of additional folders to be searched when locating project assets. This list works similarly to the list found in Max's File Preferences... window, but is used only by the project.


Dependencies are always presumed to be local. If no local version can be found, the global version will be used.
## Open Actions
Project Open Actions allow you to specify what Max configuration options are loaded when apProject opens.
In the Open Actions text edit window, you can write various messages to Max. For example, messages such as `;dsp takeover 1` or `;max overdrive 1` will enable Scheduler in Audio Interrupt and Overdrive, respectively. When the project is loaded (or reloaded via the _Reload Project_ button in the _Project_ toolbar), the Open Actions will be executed.
## Max for Live Device Projects
All Max for Live devices are projects. There are a few differences between regular Max projects and Max for Live device projects:
  * The default location for Max for Live Device Projects is `~/Documents/Max 8/Max for Live Devices` (Mac) or `(User Folder)\My Documents\Max 8\Max for Live Devices` (Win)
  * Unfreezing a device will unpack the device's assets to the project's folder, rather than to the "Unfrozen Max Device Files" folder on the Desktop.
  * Conflicts are now auto-resolved in favor of the Device version (although you can override this in the Resolve Conflicts window if you need to).
  * The Archive... item in the _Manage Project_ toolbar menu creates a datestamped ".zip" archive of a frozen copy of the current device.
  * Freezing a device will include all files listed in the _Project_ window (both explicit and implicit items).


Freezing a device which utilizes 3rd party externals will automatically collect and freeze the externals for other Max platforms if they can be found in Max's (or the project's) search path. For instance, freezing a device which uses `myextern.mxe64` on Windows will include `myextern.mxo` (macOS) externals if they are available. None of these need to be added explicitly to the project.
