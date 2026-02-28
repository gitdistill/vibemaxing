---
description: A library and toolchain that can take Max-like patches and export them as portable code
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/rnbo/
title: RNBO
---

# RNBO
[RNBO](https://rnbo.cycling74.com/) is a visual, graph-based programming language. Similar to [Gen](https://docs.cycling74.com/userguide/gen/_gen_overview/), RNBO runs in a special Max object called [rnbo~](https://docs.cycling74.com/reference/rnbo~/ "rnbo~"), a subpatcher with its own family of objects based off of Max objects.
![](https://docs.cycling74.com/images/609d16926be36b4170c2eab18fbf844a_774.webp) RNBO objects in a rnbo~ object
Anything you make in a RNBO subpatcher can be exported, to hardware and software targets like Raspberry Pi, VST and Audio Unit plugins. You can also export to C++ and JavaScript code for use in custom desktop applications and Web Audio contexts.
Most RNBO objects are designed to work the same as their Max counterparts. So if you're familiar with Max, it should be easy to work with RNBO. Gen also works inside of RNBO, which means you can embed your Gen work in a RNBO patcher and export it from Max. Other RNBO features include sample accurate events, host transport sync, MPE & MIDI support, automatic polyphony, and Ableton Link support.
RNBO is a paid add-on to Max. There are several resources available online if you'd like to learn more about RNBO.
Resource | Description  
---|---  
[RNBO Website](https://rnbo.cycling74.com/) | Main RNBO website  
[RNBO Guides](https://rnbo.cycling74.com/learn) | RNBO documentation and tutorials  
[RNBO Examples](https://rnbo.cycling74.com/explore) | RNBO in context, and examples of using RNBO  
[RNBO Objects](https://rnbo.cycling74.com/objects) | Object reference for RNBO namespace objects  
[RNBO C++ API](https://rnbo.cycling74.com/cpp) | Programming interface reference to link RNBO-exported code in a C++ app  
[RNBO JS API](https://rnbo.cycling74.com/js) | Programming interface reference to link RNBO-exported code in a JavaScript app
