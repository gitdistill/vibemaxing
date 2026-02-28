---
description: How to structure a package, documentation for package developers
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/packages/
title: Packages
---

# Packages
Packages are a convenient means of bundling objects, media, patchers, and resources for distribution. Most of the time, if you're just looking to manage resources specific to a project, then a [**Project**](https://docs.cycling74.com/userguide/projects/) is probably what you're looking for. However, if you'd like to share your work more broadly, especially if you're building a reusable set of tools to submit to the [**Package Manager**](https://docs.cycling74.com/userguide/package_manager/), then packages are right choice.
A package is simply a folder adhering to a prescribed structure and placed in the appropriate folder. When Max launches, it will iterate through these packages and load them, making their resources available for use.
## Packages Folder
If a package is available in the [Package Manager](https://docs.cycling74.com/userguide/package_manager/), then you should use the package manager to install and uninstall that package. However, you can also install packages yourself, which can be useful if you want to use a package that's not currently in the package manager.
You can install a package by copying the package folder into Max's _packages_ folder. The user-specific packages folder is at `%HOMEDRIVE%%HOMEPATH%\Documents\Max 9\Packages` on Windows and `~/Documents/Max 9/Packages` on macOS. The other (system wide) location is in `/Users/Shared/Max 9/Packages` on MacOS, and `%HOMEDRIVE%\ProgramData\Max 9\Packages` on Windows.
You can uninstall a package by deleting it from the packages folder.
## Package Folder Structure
The name of each folder in a Max package determines how Max will load the files in that folder. Some of these folders will also be automatically included in Max's [**Search Path**](https://docs.cycling74.com/userguide/search_path/).
Folder | Search Path | Description  
---|---|---  
clippings | ✅ | Patchers to list in the "Paste From..." contextual menu when patching  
code | ✅ | Gen patchers  
collections |  | Collections to list in the File Browser that are associated with the package  
default-definitions |  | Definition info for Object Defaults support in UI externals  
default-settings |  | Saved color schemes for Object Defaults  
devices | ✅ | Max for Live devices (AMXDs)  
docs | ✅ | Reference pages and Vignettes to be accessible from the Documentation Window  
examples | ✅ | Example patchers and supporting material  
extensions | ✅ | Special external objects loaded on Max launch  
externals | ✅ | External objects  
extras | ✅ | Patchers to be listed in the "Extras" menu  
fonts | ✅ | Custom fonts available to Max when the Package is present  
help | ✅ | Help patchers and supporting material  
_icon.png_ |  | A PNG graphic file (500x500px) for display in the [Package Manager](https://docs.cycling74.com/userguide/package_manager/)  
init |  | Text files interpreted by Max at launch  
interfaces |  | Supporting files for objects to display in the top patcher toolbar and other Max integration.  
java-classes | ✅ | Compiled Java classes for use in mxj/mxj~. Place .jar folders in a 'lib' subfolder.  
java-doc |  | Documentation for Java classes  
javascript | ✅ | Javascript files to be used by js  
jsextensions | ✅ | Extensions to JS implemented as special externals or js files  
jsui | ✅ | Javascript files to be used by jsui, and listed in the contextual menu for jsui  
_license.txt_ or _license.md_ |  | Terms of use / redistribution of your package, in plain text or markdown  
media | ✅ | Media files to be included in the searchpath  
misc | ✅ | Anything  
patchers | ✅ | Patchers or abstractions to be included in the searchpath  
projects | ✅ | Projects to be included in the searchpath. Note that only the project file will be added to the searchpath.  
object-icons | ✅ | An SVG-format object icon for a particular Max object (named <objectname>.svg), used in the Object Browser  
object-prototypes |  | Object Prototypes will be listed in the contextual menu for a selected UI object  
_readme.txt_ or _readme.md_ |  | Information about your package, in plain text or markdown  
snippets |  | Snippets associated with this package  
source |  | Source code for external objects, ignored by Max  
support |  | Special location for DLL or dylib dependencies of external objects. Added to the DLL search path on Windows.  
templates |  |  [**Template**](https://docs.cycling74.com/userguide/templates/) patchers to be listed in the "File > New From Template" menu  
## package-info.json
The **package-info.json** file is the manifest of your package. It includes metadata about your package like its name and description, as well as including a list of important files in your package. If you're not familiar with the JSON format, it's a common format structured text built around numbers, strings, arrays and dictionaries.
### name
The name of the package. Should be unique among packages. This doesn't affect how the name of the package will appear in Max.
### displayname
This is the name of the package as it will appear in Max, both the Package Manager as well as other places.
### version
A [semantic versioning](https://semver.org) compatible string.
```
{
  "version": "0.6.0"
}

```

### author
Author string, for a single author.
### authors
Array of author strings, for multiple authors
```
{
  "authors" : [ "Arthur Author", "Otter Auter" ]
}

```

### description
Brief description. It's a good idea to list any dependencies here, or additional relevant information.
### tags
An array of strings containing developer-defined tags, if any.
```
{
  "tags" : [ "audio", "DSP", "visualization" ]
}

```

### website
If the package or author has a website, note it here.
### extensible
An integer (0 or 1) to indicate whether this package can be extended by another package. Package extension means that the extending package becomes logically part of the extensible package in terms of how it appears in the [File Browser](https://docs.cycling74.com/userguide/file_browser/) and Reference Window. For instance, the RISE package extends the extensible BEAP package. As such, RISE patchers and documentation are included in the BEAP package entries in the File Browser and Reference.
### extends
If the package _extends_ an _extensible_ package, note that package name here.
### max_version_min
The minimum Max version this package supports (or "none" if there is no specific minimum version).
```
{
  "max_version_min": "8.0.0"
}

```

### max_version_max
The maximum Max version this package supports (or "none" if there is no specific maximum version).
```
{
  "max_version_max": "none"
}

```

### os
Optionally restrict the installation of this package to certain platforms or architectures.
```
{
  "os": {
    "macintosh": {
      "min_version": "none",
      "platform": [ "x64", "aarch64" ]
    },
      "windows": {
        "min_version" : "none",
        "platform" : [ "x64" ]
    }
  }
}

```

The info above would indicate that this package can run on 64-bit Intel Windows and macOS computers, as well as 64-bit Apple Silicon-based computers (`aarch64`). `"x32"` would indicate 32-bit compatibility, although recent Max versions no longer support 32-bit OSs.
Note that the `min_version` fields on Windows use some specific strings to indicate specific OS versions: `"none"`, `"11"`, `"10"`, `"8.1"`, `"8"`, `"7"` and `"7SP1"` are the only ones which are relevant for modern Max.
On macOS, the `min_version` field should be a Semantic Versioning string matching a macOS version (e.g. `"10.5.2"` or `"12.5"`).
### homepatcher
If the package has a "landing patcher" in its `patchers` folder, note the patcher name here. This will be the package that opens when you click the _Launch_ button in the package's detail page in the Package Manager.
```
{
  "homepatcher": "name of the home patcher.maxpat"
}

```

### toolbar_icon
This lets you identify an SVG in your package that will be used as the package's icon in the left toolbar. Read more about this [below](https://docs.cycling74.com/userguide/packages/#the-left-toolbar).
### package_extra
Optional fields. You can put anything you want here, but Max won't use these values. The one exception is the `forcerestart` key.
#### package_extra.forcerestart
Set to 1 if you would like Max to prompt the user to restart after installing your package from the Package Manager.
```
{
  "package_extra": {
    "reverse_domain": "com.cycling74",
		"copyright": "Copyright (c) 2022 Cycling '74",
    "forcerestart": 1
  }
}

```

### filelist
While you may see this field in some `package-info.json`, it's automatically generated and not used for most packages. You should not include this property in your own `package-info.json`.
### c74install
You may also see this property in installed packages, but do not add this to your `package-info.json` file. It is automatically added by the Package Manager when installing packages.
### installdate
This is another field that is managed by the Package Manager. Do not add this to your `package-info.json` file.
## The Left Toolbar
If your package includes clippings or [**snippets**](https://docs.cycling74.com/userguide/snippets/), those will be shown in the _Modules_ menu in the [left toolbar](https://docs.cycling74.com/userguide/patcher_window/#left-toolbar). The user can also add a dedicated icon for your package by right-clicking on an empty space in the left toobar and adding your package. You can customize the appearance of this icon by adding an appropriate SVG file to your package.
You can point to this icon file in your package's `package-info.json` file, using the `"toolbar_icon"` field. For example,
```
"toolbar_icon" : "my_icon.svg"

```

Alternatively, if no "toolbar_icon" is defined in `package-info.json`, you can name the file `<packagename>_toolbar.svg` where `<packagename>` is case-sensitive and must match the [name](https://docs.cycling74.com/userguide/packages/#name) of your package, and Max will automatically use that file as the toolbar icon.
If you use this second method to name your icon, and your package name contains a space, then the icon file should use underscores instead of spaces. For example, if your package is named "My Package", then the icon file would need to have the name My_Package_toolbar.svg.
In either case, the SVG file should be placed in some subfolder of your package which is [included in the search path](https://docs.cycling74.com/userguide/packages/#package-folder-structure) -- we recommend the `misc/` folder.
If you do not include an icon in this way, a two-letter icon will be auto-generated from your package name.
## Submitting a Package
If you'd like your package to appear in the offical Package Manager, you should share it with us. Find the submission form on our website at <https://cycling74.com/support/submit-packages>.
