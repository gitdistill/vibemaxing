---
description: How to change the video engine in Max, and the differences between the various video engines.
group: Jitter
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/jitter/video_engine/
title: Video Engine
---

# Video Engine
The **Video Engine** is responsible for interfacing with the operating system to manages access to video hardware devices and to video files on disk.
## Changing the Video Engine
Max's _Video Engine_ preference allows users to switch the backend video implementation for all video objects.
![](https://docs.cycling74.com/images/50ff8097f3701c96fc4fd37074bab850_471.webp)
Objects affected include [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie"), [jit.record](https://docs.cycling74.com/reference/jit.record "jit.record"), [jit.playlist](https://docs.cycling74.com/reference/jit.playlist "jit.playlist"), and [jit.matrixset](https://docs.cycling74.com/reference/jit.matrixset "jit.matrixset"). Still image loading may be affected by the video engine for [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") and [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture"). Individual [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie"), [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab") and [jit.record](https://docs.cycling74.com/reference/jit.record "jit.record") objects may override the Video Engine application preference by typing `@engine`, followed by the engine name argument, into the Max object box.
Objects previously initialized are unaffected by a preference change, therefore open patches should be closed and reopened after switching the video engine.
## Platform Specifics
Max ships with support for two video engines on Mac platforms, **avf** (AVFoundation - the default) and **viddll** (Viddll - FFmpeg), and two on Windows, **viddll** (the default) and **qt** (DirectShow). The DirectShow based engine is named **qt** for historical reasons, and has limited functionality. Windows users wishing to install third-party codecs for the **qt** engine should follow the instructions [here](https://www.ableton.com/en/help/article/live-64-windows-video-playback/). The **viddll** engine utilizes the [FFmpeg](https://ffmpeg.org/) library to provide support for a wide variety of file formats and codecs. Both **avf** and **viddll** engines provide native playback support for [HAP](https://hap.video/) encoded video files.
## Codec and Format Support
Common supported codecs for movie file reading with [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") and [jit.playlist](https://docs.cycling74.com/reference/jit.playlist "jit.playlist") and file writing with [jit.record](https://docs.cycling74.com/reference/jit.record "jit.record") and [jit.matrixset](https://docs.cycling74.com/reference/jit.matrixset "jit.matrixset"):
  * H264
  * Photo-Jpeg
  * ProRes (422 and 4444)
  * Animation (**viddll** only)
  * Many additional formats and codecs when using **viddll**


Supported image types for file reading with [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") and [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture"):
  * JPEG
  * PNG
  * TIFF
  * GIF


## jit.grab
The [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab") object is unaffected by the video engine preference. On Mac, [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab") will use AVFoundation as the video digitizer, and on Windows DirectX is used. Additionally both platforms include native support for [Blackmagic](https://www.blackmagicdesign.com/) video input devices. See the _Blackmagic_ tab of the [jit.grab](https://docs.cycling74.com/reference/jit.grab "jit.grab") help file for more information.
