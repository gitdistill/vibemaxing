---
description: Extend the functionality of Max by installing packages from tool developers
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/package_manager/
title: Package Manager
---

# Package Manager
The **Package Manager** provides instant access to a regularly updated, curated selection of Max add-on content and tools. The Package Manager allows you to manage which [**Packages**](https://docs.cycling74.com/userguide/packages/) are currently installed in Max. From the package manager you can install new packages, enable/disable existing packages, update or downgrade installed packages, and launch the default patcher for a given pacakge.
To access the Package Manager, select _Show Package Manager_ from the _File_ menu.
## Browsing and Installing Packages
By default, the package manager opens in the _Browse Remote Packages_ view. letting you browse through packages that you do not currently have installed. You can instead view the list of currently installed packages by selecting _Installed Packages_ from the drop-down menu at the top of the window.
![](https://docs.cycling74.com/images/ac8d962ca6f894a58facc62b403ddc7d_756.webp)
Click on a package to inspect its details. This will show you information such as system requirements, a description of the package, and a link to the package author’s website.
![](https://docs.cycling74.com/images/376dedbb7ff1ffa729d16a1b6e71e735_755.webp)
To install a package, click the blue _Install_ button. Once a package is installed, click the _Launch_ button (if available) to view the Launch Patcher for the package. The _Show in Filebrowser_ button will open the package in the [File Browser](https://docs.cycling74.com/userguide/file_browser/), letting you see all the files included in the package.
## Managing Installed Packages
At the top of the package manager window, click the drop-down menu and select "Installed Packages". This will list all installed packages, including both those you installed through the package manager, as well as those you might have added by dropping them in the _Packages_ folder.
To disable a package without deleting it entirely, click the _Disable_ button after selecting the package. Max will ignore any files in a disabled package, but the package will remain downloaded and installed.
Many packages, including any packages that contain [externals](https://docs.cycling74.com/userguide/externals/), will require a restart of Max before changes take effect.
You can remove a package entirely by clicking the red _Uninstall_ button.
## Package Install Location
All packages are installed in your _User Packages Folder_ , located at `%HOMEDRIVE%%HOMEPATH%\Documents\Max 9\Packages` on Windows, and at `~/Users/Max 9/Packages` on macOS. You can install packages that aren't available in the package manager, including your own custom packages, by dropping them in this directory.
Note that if you install a package that is itself available on the Package Manager by dropping them in this directory, the Package Manager will warn of a conflict. We recommend installing a package via the Package Manager if available in order to stay informed of updates to that package.
Don't change the folder names for any packages installed using the package manager.
## Package Updates and Versions
The _Package Update_ icon in the bottom-right of the package manager window will highlight if there are updates available for any installed packages.
![](https://docs.cycling74.com/images/b4b51d09d02766add5ef99e164fa90be_624.webp)
Click on the _Package Update_ icon to show all packages with an available update.
![](https://docs.cycling74.com/images/42db74a37d1bd1967a7316a4d068d440_732.webp)
You can change the installed version of any package by clicking "Show All Available Versions" in the package detail view. If you have a self-installed Package that conflicts with a Package available in our online library, you will have the option to overwrite it with our version or ignore it and leave it unchanged.
![](https://docs.cycling74.com/images/2719283e7557bcacd5eb3735d5464bb7_628.webp)
The Package Manager itself is automatically updated with each version of Max. Occationally, you may be prompted to update the Package Manager when you open the window if an update is available.
