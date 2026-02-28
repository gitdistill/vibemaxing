---
description: Organize events in time with the transport, which has a tempo, time signature, and controls to start, stop, and rewind
group: Timing
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/transport/
title: Transport
---

# Transport
Most DAWs, especially those that organize audio and MIDI into tracks, have some notion of a _playhead_. When you tell the program to "play", the playhead represents the point in the current song or session at which play will resume. There are usually controls to play, stop, and loop playback, as well as some way to set the tempo and time signature. Max doesn't organize audio and MIDI into tracks and clips, but it does have a transport that you can use to organize events in time.
## Accessing the Global Transport
Open the **Global Transport** by choosing _Global Transport_ from the _Extras_ menu. This will bring up the Global Transport window, which is an interface to Max's shared global transport. All patches in Max can access this transport, and objects that work with the transport can react when the transport starts, stops, changes position, or changes tempo.
![The global transport window](https://docs.cycling74.com/images/38082fea173c8cff7e091c2efef38a5a_389.webp) The global transport window
## Controlling the Transport
From the _Global Transport_ window, you can start and stop the transport by clicking the _Activate_ button at the top of the window. It's also possible to start the global transport from the toolbar of any Max patcher. The _play_ button on the right of the bottom toolbar can start and stop the global transport.
![Transport controls in the patcher toolbar](https://docs.cycling74.com/images/a7b1101861b629ef65693eac767638d6_577.webp) Transport controls in the patcher toolbar
To change the tempo of the global transport from the patcher toolbar, option- or alt-drag up or down on the play button control. The current tempo will be displayed in a caption above the control.
The [transport](https://docs.cycling74.com/reference/transport/ "transport") object can also act as an interface to the global transport. This object lets you control all aspects of the transport, including play/pause state, tempo, and time signature, as well as retrieving the current play position.
## Named Transports
In addition to the global transport, it's also possible to create named transports using the `@name` attribute of a [transport](https://docs.cycling74.com/reference/transport/ "transport") object. All [transport](https://docs.cycling74.com/reference/transport/ "transport") objects with the same name essentially act as an interface to the same, shared transport, and this includes [transport](https://docs.cycling74.com/reference/transport/ "transport") objects in different Max patches.
The Global Transport has the reserverd name `internal`. If you send a [transport](https://docs.cycling74.com/reference/transport/ "transport") object the message `name internal`, that object will act as an interface to the global transport.
By default, objects like [metro](https://docs.cycling74.com/reference/metro/ "metro") and [timepoint](https://docs.cycling74.com/reference/timepoint/ "timepoint") refer to the Global Transport. To refer to a particular, named transport, use the `@transport` attribute of these objects.
![Two transport objects with the same name are an interface to one shared transport.](https://docs.cycling74.com/images/1f1f103b3a235c89ee95796a6402c5fb_702.webp) Two {transport} objects with the same name are an interface to one shared transport. Starting one will start the other, and visa versa.
## Max for Live
In a Max for Live device, the [transport](https://docs.cycling74.com/reference/transport/ "transport") object will be bound to Live's transport. You can send the object a `bang` to get the current state of Live's transport, but you can't control Live's tranport this way. Instead, use the Max for Live API to interface with the Live application `link to the relevant doc here`. Other named transports—transports not bound to the Live transport—are not supported.
## Transport Resolution
The resolution of the transport is always 480 PPQ (reference to the MIDI standard). When it comes to scheduling events, the transport uses the same [**Scheduler**](https://docs.cycling74.com/userguide/scheduler/) as all other events in Max, and so ultimately the resolution of the Max scheduler determines the resolution of transport events.
