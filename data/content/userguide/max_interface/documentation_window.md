---
description: How to use the documentation window itself to find guides, reference pages, and package documentation
group: Max Interface
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/documentation_window/
title: The Documentation Window
---

# Documentation Window
The **documentation window** gives you combined access to core parts of Max's documentation.
  * **User Guide** : Full-page explanation of Max, its systems, and how to work with them.
  * [**Object Reference**](https://docs.cycling74.com/userguide/object_reference/): Detailed descriptions of individual objects, including all the messages and attributes that each object understands
  * [**Package Documentation**](https://docs.cycling74.com/userguide/package_manager/): Guides specific to a particular package, written by the package author


In addition to this, each object also has its own [help file](https://docs.cycling74.com/userguide/objects/#help-files-and-reference), which demonstrates the object's functionality in the context of a working patcher. And there is even more documentation online. The [**JavaScript API**](https://docs.cycling74.com/apiref/js/) is one example of API documentation, listing all of the functions and classes you can use to extend Max with JavaScript. Finally, you can find [examples and tutorials](https://docs.cycling74.com/learn/) online as well, which introduce concepts gradually and show some of what's possible with Max.
## Using the Documentation Window
Open the documentation window by selecting _User Guide_ from the _Help_ menu. This will open the documentation window, focusing on the User Guide.
![](https://docs.cycling74.com/images/b078c8346eac7da75011d6f3b7ea2ef7_800.webp)
As mentioned earlier, the in-app documentation is divided into three main sections: the User Guide, Object Reference, and Package Documentation. You can navigate through the different parts of the documentation window using the icons at the top of the window.
![](https://docs.cycling74.com/images/5b7643ff25af38353bfb3571baf2e077_542.webp)
  * **Back** : Navigates to the previously visited page
  * **Forward** : After navigating back, returns to the original page
  * **Documentation Home** : Go to the documentation home page
  * **History** : Click to display a list of recently visited pages
  * **User Guide** : Show the User Guide
  * **Object Reference** : List and search the available Max [objects](https://docs.cycling74.com/userguide/objects/)
  * **Package Documentation** : Show documentation for installed [packages](https://docs.cycling74.com/userguide/package_manager/)
  * [**Search**](https://docs.cycling74.com/userguide/documentation_window/#searching-the-documentation): Open the search view
  * **Open Online Version** : Open the documentation online


The left side of the documentation window shows the **navigation** for the current documentation area. In the User Guide, this lists user guide pages organized by topic. You can click the _Hide Navigation_ icon to toggle the navigation display.
![](https://docs.cycling74.com/images/2876125a787b4857ad531271c47b908b_631.webp) The Navigation icon lets you hide and show the navigation.
The navigation lets you jump from page to page, but you can also quickly jump through the contents of a particular page by using the in-page navigation. If you make the documentation window wider, the _On this Page_ navigation will appear.
![](https://docs.cycling74.com/images/b7b05c9593a05e54f120219ee734e14d_730.webp) The page navigation appears when the documentation window is wide enough
## Using the Object Reference
Click the _Reference_ icon to display the object reference list.
![](https://docs.cycling74.com/images/f7bd1d79776e173fa8afe16af5fbd2d8_819.webp)
On the left side of the page, you'll see the object reference navigation, which groups objects by built-in section for native objects, and by package name for objects from third-party [package](https://docs.cycling74.com/userguide/package_manager/). Click on any entry in the navigation to list objects from that section.
On the right side of the page, above the object listing, you can use the drop down menu to further refine the list of objects by category. For example, in the _Gen_ section, you can select the _buffer_ category from the drop down to see only Gen objects that deal with [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/ "gen_dsp_buffer") objects.
![](https://docs.cycling74.com/images/0744ece604aeffba60b0aab9cd8b288f_827.webp)
Click on an object to view the reference documentation for a specific object. Use the _Open Help_ button at the top of the object reference page to open the [help patcher](https://docs.cycling74.com/userguide/objects/#help-files-and-reference) for that object. Under that button, you'll see extensive reference for the object, including the arguments, attributes, and messages that the object understands.
![](https://docs.cycling74.com/images/7fcf5696ce78a62cdc404ff109866000_618.webp) The reference documentation for the pattr object
Next to the entry for every attribute, argument, and message, you'll see the expected [type](https://docs.cycling74.com/userguide/message_types/) for that entry. For arguments, you'll also see the keyword _optional_ appear if the value is optional, as well as any default value the argument may have.
If you make the documentation window wide enough, you'll see _On this Page_ navigation, including a disclosure triangle to list arguments, attributes, and messages.
![](https://docs.cycling74.com/images/dd14ad853af6975f72028891fe87e7c6_269.webp) On this Page navigation for the pattr object
## Using the Package Documentation
Click the _Packages_ icon to display the package documentation.
![](https://docs.cycling74.com/images/c71fd48845fc536eadb96771d2f1b9f7_801.webp)
On the left side of the page, you'll see a list of installed packages. If the package authors have written any Guides, Topics, or Tutorials, you'll see those appear in the center of the documentation window. Once you click on a particular entry, you'll see that entry appear.
![](https://docs.cycling74.com/images/a734279b7a280ad0e17c56bd0308c8af_801.webp)
At the top of a package documentation page, you'll see **breadcrumbs** showing you the path to the current page. You can click _Package Docs_ to return to the package documentation home page, or on the name of the page to see just the documentation for that package.
## Searching the Documentation
Click the _Search_ icon in the top-right of the window to display the search view.
![](https://docs.cycling74.com/images/6a6ea1c76c05adc15b7cd899feecfd7d_781.webp)
When you search, you'll see results from the User Guide, Object Reference, and Package Docs, but you'll also see results from online as well, including API Reference and RNBO results. If there are more than a few results in a given category, click _More Results_ to view a page of results from just that category.
![](https://docs.cycling74.com/images/d05021fb7c69ac5363e811953e2f02ca_780.webp) Documentation search results with the search term 'matrix'
