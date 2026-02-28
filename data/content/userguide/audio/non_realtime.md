---
description: Processing audio in non-real-time, for intensive or batch processing
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/non_realtime/
title: Non-real-time Processing
---

# Non-real-time Processing
Most of the time, Max is running in real-time. For every video and audio frame, Max produces just enough video and audio to fill that frame. If you tweak a parameter or modulate an effect, you can see and hear the result right away.
There are two main limitations to real-time processing:
  * Some processes are too computationally intensive to run in real-time.
  * It takes exactly as long to render a process in real-time as the resulting media. So, it takes 10 minutes to render a 10 minute video in real-time, even if it could have been processed faster.


By processing audio or video in non real-time, you can get around both of these limitations.
## Non-real-time Audio
In the _Audio Status Window_ select the _NonRealTime_ driver.
![](https://docs.cycling74.com/images/edf4ef2be372e9b62bb9a67e4a00bbc4_544.webp)
In non-real-time mode, hardware input and output are disabled. Audio processing runs independently of any physical scheduling priority, which essentially means that Max runs the audio thread as fast as possible. This means that patches designed to run in non-real-time mode have a typical structure:
  1. Some way to activate audio processing
  2. Some way to monitor the state of audio processing (often polling [dsptime~](https://docs.cycling74.com/reference/dsptime~/ "dsptime~") to measure elapsed processing time)
  3. An automatic way to disable audio processing


This patcher enables audio processing, waits 100 milliseconds, and then prints the elapsed time according to [dsptime~](https://docs.cycling74.com/reference/dsptime~/ "dsptime~"), which measures how many milliseconds of audio have been processed.
![](https://docs.cycling74.com/images/dd3a2e5ac046e80e590fb1c9cd0c8788_462.webp)
As you can see, about 10 seconds of audio have been processed in 100 milliseconds of real-time.
The typical way to capture audio output in non-real-time mode is to record to a file with [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~"). The following patcher synthesizes about a second of noise and captures the output.
## Non-real-time Video
Recording video in non-real-time is a bit simpler than recording audio in non-real-time. The easiest method is to use [jit.record](https://docs.cycling74.com/reference/jit.record "jit.record") with the `@realtime` attribute disabled. In this mode, every time [jit.record](https://docs.cycling74.com/reference/jit.record "jit.record") receives a matrix, it will be appended to the currently open video file. The frame rate of the output will be determined by the `@fps` attribute of the [jit.record](https://docs.cycling74.com/reference/jit.record "jit.record") object and _not_ by the real-time rate at which new matrices are recieved.
If you're using [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") or [jit.pworld](https://docs.cycling74.com/reference/jit.pworld "jit.pworld") to manage your virtual scene, set the `@enable` attribute to `0` to disable automatic rendering. In this configuration, you can send a `bang` to [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world") to manually render a single frame. If you're using [jit.gl.render](https://docs.cycling74.com/reference/jit.gl.render "jit.gl.render") to render a virtual scene to a texture, you can pass your texture through a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") to convert it before output.
![](https://docs.cycling74.com/images/9481fd6fbf876950b4624d8487724f5a_573.webp)
