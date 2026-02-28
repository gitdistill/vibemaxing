---
description: Externals are compiled Max objects that can be loaded and run dynamically by Max.
group: Reuse and Organization
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/externals/
title: Externals
---

# Externals
Under the hood, Max objects are basically small programs. The essence of Max is to create new behaviors by connecting these small programs together. Because of this modular design, third parties can extend the functionality of Max by programming their own objects. These objects are called **Externals** , since they're authored _externally_ to the main Max program.
Externals are like audio plug-ins for a DAW, they allow Max to be extended to support new objects at any time. Max actually ships with many externals and many more are available for free on the Internet.
Externals are bundles of executable code, stored in `.mxo` files on non-Windows operating systems, and `.mxe64` files on Windows. When an object receives a message, or when Max calculates a vector of audio data, it calls a function inside each object to perform the necessary computation.
## Installing Externals
In order to install an External, simply put the `.mxe64` or `.mxo` file into Max's [Search Path](https://docs.cycling74.com/userguide/search_path/). When Max launches, it scans its Search Path for any External files. If it finds any, it automatically adds them to internal database. Those objects will appear in Max's new object autocomplete, and you will be able to create a new object from any dicovered externals.
More complex externals may have dependencies that will need to be installed as well. For example, an external might rely on a Dynamic Library or `dll` to function. In general, follow the instructions provided by the external author to install correctly.
If the external you want to install is part of a [Max Package](https://docs.cycling74.com/userguide/package_manager/), then you don't need to do anything special to install it. The external wil be included automatically along with the rest of the package. If you're trying to install an external on its own, you can put it anywhere in the current Search Path. The `Library` folder, found at `%HOMEDRIVE%%HOMEPATH%\Documents\Max 9\Library` on Windows, and at `~/Users/Max 9/Library` on non-Windows operating systems, is a generic folder for storing files that you want to be included in Max's Search Path. It can be a useful place to store externals if you'd like them all to be in one place.
## Security
Externals are programs. Just like you wouldn't download and run a program from someone you don't trust, don't install any externals from untrusted sources either. Also, keep in mind that externals run as part of the main Max program. Whatever permissions you give Max, your externals will have those same permissions.
## Developing Externals
In order to communicate with the Max application, an external needs to tell Max what messages it responds to, how many inlets and outlets it has, whether it processes audio, and much more. All of this is accomplished using the Max SDK, a library of functions that can program can use to register as a Max external.
You can get the SDK, and learn to write your own externals, using the [SDK Documentation](https://cycling74.com/downloads/sdk).
In addition to the C SDK, there is also a C++ SDK called Min. This version of the SDK can streamline writing Max externals, and supports some advanced features not readily available to the C SDK. You can learn more about the Min SDK from the [Min SDK Documentation](http://cycling74.github.io/min-devkit/).
## Resolving Errors and Troubleshooting
When developing or installing new externals, you may see a message like the following when you try to load your external.
![](https://docs.cycling74.com/images/478c1695800e27c451d1cf7623e2bff2_478.webp)
This message, "could not load due to incorrect architecture", means that Max recognized the `.mxo` or `.mxe` file as an external, but could not execute the code inside that object because it was compiled for a different hardware architecture. This can happen when trying to use a 32-bit external while running a 64-bit version of Max, or when trying to use an external compiled for an Intel architecture while runnning an ARM (Apple Silicon). Usually the best solution is to find a version of the external that's compiled for the same architecture that you're trying to use (or to rebuild your own external with new build settings). However, on MacOS, it's also possible to run Max using Rosetta, which will let you use externals compiled for intel architecture. To do so, first quit Max, then right click on the application, choose `Get Info`, and then enable "Open using Rosetta".
![](https://docs.cycling74.com/images/8b785c2c034e76a2b2f4fb27f2b98c72_265.webp)
