---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/01_mspintro/
title: Introduction
---

Download Series Content and Patchers
# Introduction
## Signal processing in Max
MSP gives you over 200 Max objects with which to build your own synthesizers, samplers, and effects processors as software instruments that perform audio signal processing.
![](https://docs.cycling74.com/images/04a2beca0a522bb4131f3bbff9ddb7d1_476.webp) A filter and delay effect processor in MSP
As you know, Max enables you to design your own interactive programs that draw, play movies and sounds, respond to mouse and keyboard control, and integrate with outside devices through MIDI and other communications systems.
![](https://docs.cycling74.com/images/e8635c3495f78762de2f3c384fb1762a_631.webp)
## MIDI control with Max
With the addition of the MSP objects, you can also create your own digital audio device designs -- your own computer music _instruments_ -- and incorporate them directly into your Max programs. If you like, you can specify exactly how you want your instruments to respond to your control, and you can implement the entire system in a Max patch.
![](https://docs.cycling74.com/images/37728215d102a7201b2a15c5cd05c0ec_304.webp) MIDI control of a parameter of an audio process
MSP objects are connected together by patch cords in the same way as Max objects. These connected MSP objects form a _signal network_ which describes a scheme for the production and modification of digital audio signals. (This signal network is roughly comparable to the _instrument definition_ familiar to users of _Music N_ sound synthesis languages such as Csound.) The audio signals are played through the audio output jack of your computer, or through an installed sound card, using CoreAudio on the Macintosh or MME, DirectSound, or ASIO on Windows. If you're working with Max4Live, audio gets routed into and out of MSP through the Ableton Live software.
![](https://docs.cycling74.com/images/64403f0257da4f7a816de4b40edd7b72_490.webp) Signal network for an FM instrument
## How To Use This Manual
The MSP Documentation contains the following sections:
_Digital Audio_ explains how computers represent sound. Reading this chapter may be helpful if MSP is your first exposure to digital manipulation of audio. If you already have experience in this area, you can probably skip this chapter.
_How MSP Works_ provides an overview of the ideas behind MSP and how the software is integrated into the Max environment. Almost everyone will want to read this brief chapter.
_Audio Input and Output_ describes MSP support for Core Audio on Macintosh systems, support for DirectSound on Windows systems, and audio interface cards. It explains how to use the Audio Status window to monitor and tweak MSP performance.
_The MSP Tutorials_ are over 60 step-by-step lessons in the basics of using MSP to create digital audio applications. Each chapter is accompanied by a patch found in the MSP Tutorial folder. Like the Max Tutorials, chapters are grouped under headings that make it easier to find what you're looking for and navigate the tutorials by your subject of interest. The MSP Tutorials are grouped into thirteen sections:
  * **Basics:** This handful of chapters teaches you the fundamentals of working with digital audio in MSP, including working with simple oscillators and routing signals around within a network.
  * **Additive and Modulation Synthesis:** These chapters discuss some of the most common synthesis techniques that primarily involve the manipulation of _oscillators_ , including classic additive synthesis and digital FM synthesis.
  * **Sampling and Recording:** This section of the tutorials deals with manipulating audio data in MSP, as we look at working both with soundfiles stored on a hard drive and samples stored in the computer's memory.
  * **Filters and Subtractive Synthesis:** These chapters discuss techniques that revolve around the manipulation of complex sounds with _filters_ , including subtractive synthesis and audio equalization.
  * **Dynamics Processing:** This group of three tutorials discusses working with the _dynamics_ of audio signals to accomplish envelope following, audio peak limiting, and distortion.
  * **MIDI and MSP:** These tutorials show how to modify MSP patchers to simulate the basic functionality of commercial synthesizers, samplers, and effects units by allowing them to be controlled with MIDI input devices.
  * **Polyphony and Resource Management:** These chapters discuss how to get the most out of your system with MSP, including creating and managing more than one copy of an MSP [Abstraction](https://docs.cycling74.com/userguide/abstractions/) in order to create polyphonic sound engines.
  * **Sequencing:** This section discusses the use of MSP control signals to sequence audio and Max events.
  * **Panning:** This trio of tutorials discusses basic strategies for panning as well as demonstrating how to integrate MSP with multi-channel audio systems.
  * **Analysis:** These chapters go over common analysis techniques in the world of digital audio, from accurate level metering to Fourier analysis.
  * **Delays:** This group of chapters discuss the use of delay objects in MSP to create flangers, echo effects, harmonizers, and reverbs.
  * **Plug-ins:** These two tutorials show how to use VST effect and instrument plug-ins within MSP.
  * **Compression:** This last group discusses the **omx** group of objects which offer advanced dynamics processing within MSP.


Even if you were comfortable with other digital audio programming environments before getting started with MSP, you should at least check out the first tutorial, which covers setting up Max to make digital audio come out of your computer.
The _MSP Object Reference_ section describes the workings of each of the MSP objects. It's organized in alphabetical order.
## Finding Information
You can easily find specific information using the search bar at the top of this page. If you type in a term you will be shown a list of pages that feature the term, including object reference pages, snippets (parts of patchers that show the object in use) tutorials, and guide articles that feature the term.
## Other Resources for MSP Users
The help files found in the _max-help_ folder provide interactive examples of the use of each MSP object.
The _Max Examples_ folder contains a number of interesting and amusing demonstrations of what can be done with MSP.
The [Cycling'74 website](http://www.cycling74.com) provides the latest updates to our software as well as an extensive list of frequently asked questions and other support information. You will also find articles and interviews featuring artists and musicians who use Max/MSP/Jitter. All of the documentation for Max is available under the Support/Documentation tab.
The website also features an on-line Max discussion where you can ask questions about programming, exchange ideas, and find out about new objects and examples other users are sharing. For information on joining the discussion, as well as a guide to third-party Max resources, visit <http://www.cycling74.com/community>
Finally, if you're having trouble with the operation of MSP, send e-mail to _support@cycling74.com_ , and we'll try to help you. 

Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
