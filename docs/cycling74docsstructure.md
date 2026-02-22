# General Docs Website Structure

1. User Guide (has landing page)
    - More on its structure below
2. Reference (no top level landing)
    - A. API Reference (landing page)
        - Live Object Model (landing page)
        - Max JS API (landing page)
        - Node For MAX API (landing page)
    - B. Object Reference (landing page)
        - more on its structure below
3. Learn (Has Landing page)
    - more on its structure below


# 1 User Guide

<loc>https://docs.cycling74.com/userguide/</loc>

this acts as landing page more useful for human consumption, although the sidebar navigation adds an additional layer of structure not present in the actual sitemap.

from the sidebar the user guide section and subsections are grouped into the following buckets:

1. Audio
2. Colors
3. Data
4. Debugging
5. Files
6. Gen
7. Jitter
8. Max Interface
9. MIDI
10. Parameters
11. Patching
12. Resuse and Organization
13. Scripting
14. Sharing
15. Timing
16. Max For Live

some of these buckets have an overview page that then indexes the sub section, some do not. Here is the sidebar nav for reference. Each of these items within the buckets correspond to a url. for e.g. ableton dsp: https://docs.cycling74.com/userguide/abl/, or color pallete: https://docs.cycling74.com/userguide/color_palette/

For the nested ones like MC the MC overview would be: https://docs.cycling74.com/userguide/mc/ and then the sub section MC and Gen goes to: https://docs.cycling74.com/userguide/mc/mc_gen/

- Overview
- New in Max

1. Audio
- Ableton DSP
- Frequency Domain
- MC Overview
- MC and Gen
- MC Wrapper
- Multi-Channel I/O
- Non-Real-Time
- Plugins
- Polyphony
- Recording
- RNBO
- Sample Accurate Messages

2. Colors
- Color Palette
- Color Themes
- Dynamic Colors
- Format Palette
- Styles
- Syntax Coloring

3. Data
- Arrays
- Dictionaries
- Integers and Floats
- Strings

4. Debugging
- Debugging and Probing
- Error Messages
- Illustration Mode
- Max Console

5. Files
- File Browser
- Filetypes
- Search Path

6. Gen
- Gen Overview
- Common Operators
- Gen Expr
- Gen~ Operators
- Jitter Operators

6. Jitter
- Depth and Blending
- Geometry
- Graphics Engine
- Graphics Processing
- Jitter Expr
- JXS File Format
- Matrices
- Render Passes
- Textures
- Video
- Video Engine

7. Max Interface
- Action Menu
- Documentation Window
- Extras Menu
- Inspector
- Object Reference
- Preferences
- Sidebar Search
- Toolbars

8. MIDI
- Mapping
- MIDI

7. Parameters
- OSC
- Parameter Connect
- Parameter Mode
- Presets and Interpolation
- Saving and Pattr
- Snapshots

8. Patching
- Conversion Cheat Sheet
- Messages
- Message Types
- Objects
- Patcher Lifecycle
- Patching
- Patch Cords
- Patching Mechanics
- Web Browser

9. Reuse and Organization
- Abstractions
- Bpatchers
- Custom UI Objects
- Externals
- Packages
- Package Manager
- Projects
- Prototypes
- Snippets
- Subpatchers
- Templates

10. Scripting
- Scripting Overview
- External Text Editor
- JavaScript
- Lua Overview
- Max Define Message
- Messages to Max
- REPL

11. Sharing
- Sharing Overview
- Projects
- Standalones and Collectives

12. Timing
- Scheduler
- Time Value Syntax
- Transport

13. Max for Live
- Overview
- Live API Overview
- Creating Devices
- User Interfaces
- Automation
- Sharing Devices
- Timing

# 2. Reference: Api Reference

## Landing page

<loc>https://docs.cycling74.com/apiref/</loc>

contains the following information:

```
API Reference
Max exposes several APIs—Application Programming Interfaces—that let you use code to control various systems in Max. You can write short scripts to automate simple tasks, or large programs that completely change the way Max behaves. Some of the APIs that Max offers:

Live Object Model: Use Max objects like live.object and live.path to read and modify the state of Ableton Live from within a Max for Live device. Also accessible from the JavaScript API.
Max JS API: Use the v8, v8ui and v8.codebox to embed JavaScript in a Max patch. Define custom objects, programmatically create objects and patch cords, and operate the Max application.
Node for Max API: Use the node.script and node.debug objects to launch custom Node.js scripts from Max. Send Max messages to a running Node process and fetch a result.

```

## Sub Landing Pages

Each api reference section has its own landing page with an overview and index of the doc entries.

- <loc>https://docs.cycling74.com/apiref/lom/</loc>
- <loc>https://docs.cycling74.com/apiref/js/</loc>
- <loc>https://docs.cycling74.com/apiref/nodeformax/</loc>

for example for the Live object Model:

```
LOM - The Live Object Model
Objects which comprise the Live API described by their structure, properties and functions. The Live Object Model lists a number of Live object classes with their properties and functions, as well as their parent-child relations through which a hierarchy is formed. Please refer to the Live API overview chapterfor definitions of the basic Live API terms and a list of the Max objects used to access it.

This document refers to Ableton Live version 12.3b9

Object Model Overview
Click on the classes to navigate to their description.
Expand

API Objects
Item	Description
Application	This class represents the Live application. It is reachable by the root path live_app ...
Application.View	This class represents the aspects of the Live application related to viewing the application....
Chain	This class represents a group device chain in Live.
ChainMixerDevice	This class represents a chain's mixer device in Live.
Clip	This class represents a clip in Live. It can be either an audio clip or a MIDI clip in the Arr...
Clip.View	Representing the view aspects of a Clip.
ClipSlot	This class represents an entry in Live's Session View matrix. The properties ...
[more lines...] 
```

with each of these entry description corresponding to their url:

- <loc>https://docs.cycling74.com/apiref/lom/application/</loc>

# 3 Reference: Object Reference

For the object reference the landing page: <loc>https://docs.cycling74.com/reference/</loc

is a paginated (73 pages of 25 entries) index of all objects with an entry description in the following format:

```
Name | Description | Package
!- | Subtraction object (inlets reversed) | Max
```
with each entry corresponding to its url <loc>https://docs.cycling74.com/reference/!-/</loc>

In addition the objects are organized via the following packages:

- Ableton DSP
- Gen
- jit.mo
- Jitter
- Jitter FX
- Jitter Geometry
- Jitter Tools
- Max
- Max for Live
- max-mxj
- maxforlive-elements
- MC
- Mira
- MSP
- Node for Max
- VIDDLL

As well as `kind` which is an independent tagging layer diff then above.

- Gen Common Operator
- Gen DSP Operator
- Gen Jit Operator
- Max Object
- Refpage

# 4 "Learn" Section structure

## Landing Page

<loc>https://docs.cycling74.com/learn/</loc>

The Learn landing page has a list of the 6 tutorial series at the top

1. Max Tutorials
2. MSP Tutorials
3. Jitter Tutorials
4. Custom Drawing with JavaScript
5. Jitter Geometry Tutorial
6. Polish Your Pixels

With each having a description like so:

```
Max Tutorials
Core Max tutorial series, showing how to create patches, take input from MIDI controllers, manipulate data, and drive dynamic processes
```

And at the bottom it is a paginated index (20 pages of 10 entries) of all articles with an entry for each article like so:

```
Tutorial
Quickstart
Introduction to drawing with MGraphics
```

## Series landing pages

<loc>https://docs.cycling74.com/learn/series/</loc>

The series landing pages organize the articles into a series, index each tutorial article and adding some description

this is just an excerpt of the max tutorials landing page. where each line item corresponds to its url like: 
<loc>https://docs.cycling74.com/learn/articles/midichapter01/</loc

```
MIDI
Basics — Getting MIDI input and output

Note Management — Generating and managing note events

Parsing — Decoding and encoding MIDI streams

Basic Sequencing — Playing back MIDI sequence data

Advanced Sequencing — Recording and manipulating MIDI sequences

Data
Data Viewing — Visualizing data streams

Data Scaling — Mapping and scaling numerical information

Gesture Capture — Recording and playing back captured input

Cellblock — Working with a visual spreadsheet interface

List Processing — Manipulation of lists of data

Communications
Human-Interface Devices — Working with game controllers

Serial Communication — Using standard serial devices

UDP Networking — Passing messages over a network
```

## Series Article pages

All articles belong to a series. also many article pages include a `see also` section that connect to the object reference pages:

for e.g. <loc>https://docs.cycling74.com/reference/midiin/</loc>

```
See Also
midiin - Output incoming MIDI bytes

midiout - Sent integers as raw MIDI data

notein - Output incoming MIDI note messages

noteout - Send MIDI note-on and note-off messages

ctlin - Output incoming MIDI control change messages

ctlout - Send MIDI control change messages

midiinfo - Set a pop-up menu with current names of MIDI devices

gswitch2 - Switches the right inlet between two outputs
```

# Userguide Overview:

```
User Guide
Welcome to the Max user guide. This guide covers everything to do with how Max works, including the fundamentals of objects, messages, and patchers; the different parts of the Max interface; and how to do things like process sound and work with graphics.

If you're new to Max, you might find it useful to read how to use this documentation

This documentation is also available in PDF format, for viewing offine.

New in Max 9
If you're a long-time Max user and you want to see what's new in Max 9, check out this overview.

Demos
If you want to see some of what you can do with Max, check out these demos:

Name	Description
JavaScript Codebox	Mix textual and visual programming with inline codebox supporting modern JavaScript
Jitter Geometry	Half-edge structures for shapes that you can morph and distort
Ableton DSP	Use Ableton DSP algorithms for synthesis, modulation, and effects
Tutorials
These tutorials can guide you through working with Max step-by-step.

Working with Max - The basics of working with Max, including setting up timers and events, building a user interface, handling input from the webcam, and generating sound.
Signal Processing - How to generate and manipulate audio signals, extacting automation from real-time audio signals, and working with samples.
Video Processing - Setting up a graphics environment, making dynamic visualizations, and generating audio-reactive effects.
Jitter Geometry - Using the jit.geom objects, introduced in Max 9, to manipulate dynamic geometry using the half-edge structure.
If you want to get inspired with even more Max examples, check out our Examples Gallery

API Reference
Max exposes several APIs—Application Programming Interfaces—that let you use code to control various systems in Max. You can write short scripts to automate simple tasks, or large programs that completely change the way Max behaves. Some of the APIs that Max offers:

JavaScript API: Use the v8, v8ui and v8.codebox to embed JavaScript in a Max patch. Define custom objects, programmatically create objects and patch cords, and operate the Max application.
Live Object Model: Use Max objects like live.object and live.path to read and modify the state of Ableton Live from within a Max for Live device. Also accessible from the JavaScript API.
Node for Max: Use the node.script and node.debug objects to launch custom Node.js scripts from Max. Send Max messages to a running Node process and fetch a result.
```