---
description: Recording audio in Max
group: Audio
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/recording/
title: Recording and Exporting
---

# Recording and Exporting
## Recording Audio
When it comes to recording the audio output of your patcher, Max tries to give you lots of options to best fit your needs. **Global Record** is a simple "one-button" recording option suitable for most everyday recording. If you need a little bit more control, or you want to record more than two channels, you can use the **Quickrecord** extra. For programmatic recording, and for recording more than eight channels, you can use the [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") object, or export directly from a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object.
### File formats
Max objects can save audio to `aiff`, `wave`, `ogg`, `flac`, or `raw` formats. To record to an `mp3` or an `m4a`, export your audio from Max, and then process the result. Many programs can compress and convert audio; [ffmpeg](https://www.ffmpeg.org/) is a popular and free tool.
### Global Record
When you want to record the output of your patcher, just click the _Global Record_ button in the right toolbar.
![](https://docs.cycling74.com/images/a10e64dffc6a547538a921b20d3c1550_190.webp)
This will immediately start recording the first two channels of all patchers to a new audio file. The _Global Record_ button will change appearance while recording is taking place. If you want to see an animating red dot, instead of a filled white circle, enable the _Global Record Red Button_ in Max's [recording preferences](https://docs.cycling74.com/userguide/preferences_and_settings/#recording).
_Global Record_ will record to a folder named _Recordings_ in the [Max 9 Folder](https://docs.cycling74.com/userguide/search_path/#max-9-folder).
### Quickrecord
The **Quickrecord** extra also records the audio output of the Max application. You can open the Quickrecord extra by selecting `Quickrecord` from the _Extras_ menu. Under the hood, this extra uses the [adoutput~](https://docs.cycling74.com/reference/adoutput~/ "adoutput~") object, which acts as a tap into Max's audio output.
#### Recording to a directory
By default, Quickrecored will record to a directory. You can press the _Choose a directory_ button to select which directory Max should record to. When you do, you'll see the menu illuminate under the _Choose a directory_ button.
![](https://docs.cycling74.com/images/3950457dd0be2c3936ae91430151921d_407.webp)
Every time you press the _Record_ button, Max will add a new recording to the directory that you've selected. Max will format the name of the recording to reflect the date and time when you started the recording.
![](https://docs.cycling74.com/images/ba9ceef71cdc133040fd433fa1e56dbc_494.webp)
Remember to press the _Record_ button again when you're done to stop the recording. This is necessary to finalize the audio file.
#### Recording to a file
Click on the _Open a file_ button to select a file to which you'd like to record. Once you've picked a file, you'll see the user interface update to show the name of the file that you've chosen. You can click on the illuminated menu under the _Open a file_ button to see where your file will be recorded.
![](https://docs.cycling74.com/images/1a4ea36e0c9f3471bb0f9798623ea488_407.webp)
If you start recording again without opening a new file, Max will record over your original recording.
#### Multichannel
Quickrecord can record up to eight channels simultaneously. However, by default only the first two audio channels are enabled. In order to enable the other audio channels for recording, use the drop down menu under each channel to map each channel from Max to a channel in the recording.
![](https://docs.cycling74.com/images/d6b2b3fe4ed5cda570b565c9c0a0ef85_407.webp)
Each channel strip in the Quickrecord view represents a different channel in the recorded audio file. Using the menus in each channel strip, you can map an audio output from Max to each recorded channel. The default configuration maps output channel 1 to recording channel 1, and output channel 2 to recording channel 2. Set any channel to _Off_ to disable recording to that channel.
### Using [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~")
The [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") object (and the [mc.sfrecord~](https://docs.cycling74.com/reference/mc.sfrecord~ "mc.sfrecord~") object) is the programmatic interface to recording in Max. Each [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") object can record up to 64 channels at once, and multiple [sfrecord~](https://docs.cycling74.com/reference/sfrecord~/ "sfrecord~") objects can be active at the same time.
![](https://docs.cycling74.com/images/63d2d23928c12a84830c6a0f5aec7820_597.webp)
### Using [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~")
The [record~](https://docs.cycling74.com/reference/record~/ "record~") object can record directly to the contents of a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object, letting you record to memory in Max without saving your audio to disk. You can also use the [poke~](https://docs.cycling74.com/reference/poke~/ "poke~") object to write samples directly into a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"). Either way, after getting samples into a [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~"), you can send [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") a `write` messages to save the contents of the buffer to disk.
## Recording Video
For a full discussion of video recording, see this Jitter documentation on [Recording Video](https://docs.cycling74.com/userguide/jitter/video/#recording).
