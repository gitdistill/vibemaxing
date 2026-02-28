---
description: Iterate through the files in a folder.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/folder/
title: class Folder
---

# class Folder
Iterate through the files in a folder.
#### Example
```
f = new Folder("patches");
// would try to find the patches folder in the search path
f = new Folder("Disk:/folder1/folder2");
// uses an absolute path

```

After creating a Folder object, you'll probably want to restrict the files you see while traversing it by setting the typelist property:
```
f.typelist = ["iLaF", "maxb", "TEXT"];
// typical max files

```

Check the file max-fileformats.txt inside the init folder in the Cycling ’74 folder for filetype codes and their associated extensions. As a Folder object traverses through the files, you can find out information about the current file using its file properties. You can also determine whether you've looked at all properties by testing the end property. The following code prints the names of all files found in the folder.
```
while (!f.end) {
 post(f.filename);
 post();
 f.next();
}

```

To finish with the Folder object, you can either delete it, or send it the close message if you might want to reuse it.
```
f.close();

```

Two types of properties of a Folder are available: some refer to the current file within the folder, and some refer to the Folder object’s state. Most of these properties are read-only.
## Constructors
```
new Folder(pathname: string);

```

Constructs a new instance of the `Folder` class
pathname can be in the search path or a complete pathname using Max path syntax.
Parameter | Type | Description  
---|---|---  
pathname | string | the name of a folder  
## Properties
### count number read-only
The total number of files of the specified type(s) contained in the folder.
### end boolean read-only
Non-zero (true) if there are no more files to examine in the folder, or if the pathname argument to the Folder object didn’t find a folder.
### extension string | null read-only
The extension of the current file's name, including the period. If there are no characters after the period, a null value is returned.
### filename string read-only
The name of the current file.
### filetype string | null read-only
The four-character code associated with the current file's filetype. These codes are listed in the file max-fileformats.txt, which is located at /Library/Application Support/Cycling ’74 on Macintosh and C:\Program Files\Common Files\Cycling ’74 on Windows. If there is no mapping for the file's extension, a null value is returned.
### moddate any[] read-only
An array containing the values year, month, day, hour, minute, and second with the last modified date of the current file. These values can be used to create a Javascript Date object.
### pathname string read-only
The full pathname of the folder
### typelist string[]
The list of file types that will be used to find files in the folder. To search for all files (the default), set the typelist property to an empty array.
## Methods
### close
Closes the folder. To start using it again, call the reset() function.
```
close(): void;

```

### next
Moves to the next file.
```
next(): void;

```

### reset
Start iterating at the beginning of the list of files. Re-opens the folder if it was previously closed with the close() function.
```
reset(): void;

```

