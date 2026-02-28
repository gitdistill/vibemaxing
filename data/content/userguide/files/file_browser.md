---
description: The File Browser is a graphical interface to the search path, and can find and group files.
group: Files
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/file_browser/
title: File Browser
---

# File Browser
The **File Browser** is a graphical interface to Max's [Search Path](https://docs.cycling74.com/userguide/search_path/), letting you view, search, and organize all the files that Max can access. It's helpful not only for finding your own files, but also for finding all of the content that comes with Max. You can also create **Collections** , which are like virtual folders that group together patchers and other media.
You can open the file browser from a Max patcher window by clicking the button in the left toolbar.
![](https://docs.cycling74.com/images/006532eb2c514d19297fa076b830522d_375.webp)
You can also select the _Show File Browser_ option from the _File_ menu.
## Browsing
From the navigation bar on the left of the File Browser window, you can view **Recently Used** items, **Recently Added** items.
![](https://docs.cycling74.com/images/ec791b36f09c72020b221d813a1c3947_255.webp)
You can also browse content by package, or browse all of the content that comes built-in with Max.
![](https://docs.cycling74.com/images/3ea210c2037e6845477889198ab761d9_256.webp)
## Adding Files to the Search Path
At the bottom of the File Browser window, there's a button that you can use to add files to the search path and, by extension, the file browser.
![](https://docs.cycling74.com/images/bb9fe62dbc20ebd93ad7ed3860944299_152.webp)
Clicking this button will bring up a system dialog box that you can use to browse for files or folders to add to Max's search path. If you select a file, that file will be visible and searchable in the file browser. To remove that file from the search path, right-click on the file and select _Remove from Search Path._
From the same dialog box you can also add a whole folder to Max's search path. Once you do, you can select _File Preferences_ from the _Options_ menu to view the path that you added. By default this will add that folder and all subfolders to the Max search path. You can remove the folder by selecting the folder and clicking the _Remove Path_ button at the bottom of the _File Preferences_ window.
![](https://docs.cycling74.com/images/3df62a0e57e38752b3113ee6d789fa8c_597.webp)
## Advanced Search
When you open the File Browser for the first time, or when you click on the _Question Mark_ button in the top-right of the window, you'll see a description of the advanced search syntax for the file browser. This lets you build search queries to narrow in on just the content you're looking for. For example, the search
```
package:BLOCKS kind:audio

```

will search only for audio files in the package _BLOCKS_. When you click on buttons in the left sidebar, you may notice that these change the contents of the search box. In fact, these buttons are just shortcuts to using the advanced search terms. Clicking on the _Recently Used_ button is exactly the same as starting a search with `recent:true`. Clicking on a button in the left sidebar and then adding additional search terms is a convenient way to build up a complex search term.
## Bookmarks
If you want to save a search query for later, you can click on the _Bookmark Search_ button in the top-right of the File Browser window, next to the search bar. This button creates a new **Saved Search** or **Bookmark** so you can easily find it again later. And once you've created a Saved Search, you can find it using the Saved Search button in the left sidebar.
![](https://docs.cycling74.com/images/2faf1c50343b1304c5c9ba169ce564a7_464.webp)
## Collections
**Collections** group together patchers, media, and saved searches. In addition to helping you stay organized, anything that you add to a Collection will also be added to the Max search path. You can also access a Collection from the sidebar in any Max patcher, making them convenient for accessing files that you use frequently.
![](https://docs.cycling74.com/images/0c8a66ddad166dd7a6e4c999b4e5a164_208.webp)
### Creating a Collection
Create a new Collection by clicking the _Create New Collection_ button in the bottom-left of the File Browser window.
![](https://docs.cycling74.com/images/61e59679b6b84dd3c30c23b2613468c5_200.webp)
It's also possible to right-click on any file in the File Browser and select _Add to Collection_ or _Create Collection with selected file_.
### Removing a Collection
To remove a collection, first open the collection in the File Browser. Then, click the _Garbage Can_ icon in the top-right of the collection viewer.
![](https://docs.cycling74.com/images/7e71a00c880a26fb5f44ef1092fcb7dc_460.webp)
