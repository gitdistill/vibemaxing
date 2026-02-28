---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_04/
title: Compression on Real Instruments
---

Download Series Content and Patchers
# Compression on Real Instruments
Compressors can be used on any recording where there is a need for them. In the recording industry compression is routinely used on vocals, drums and bass. To try these out, you can open and use the tutorial patch, create your own compressor patch with an [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") object, or use your favorite VST plug-in compressor.
## Vocals
Using compression on vocal tracks can help make the lyrics more understandable. Singers will typically shape a phrase something like this:
![](https://docs.cycling74.com/images/ddd937d131bf7ee7c72c1eb71b1e7a16_320.webp)
This might sound lovely taken by itself, but when mixed with a typical band or piano accompaniment the weaker syllables “oh” and “where” will be masked out. Either that or you will get a Bing Crosby mix where the band sounds like it is in the next room. If you ask the singer to even the phrase out, they will be so uptight that there will be no expression at all. You can help these folks out with a bit of subtle processing.
The first processing you can apply is equalization. If the tracks are equalized properly, they can be made clear with minimal compression. Vocal equalization is a mild boost (3 dB or so) somewhere between 2 and 4 kHz. You tune it to the specific voice and what you are listening for is clear vowels. You then put the inverse equalization (a 3 dB cut at the same frequency) on all other tracks that might interfere (such as guitars), making a window in the spectrum for the voice to come through. With only a 3 dB change, you haven't made an obvious difference in the voice or any single instrument. Many microphones already have this sort of EQ boost built in, but you still need to cut the other tracks. (In fact, if they were recorded with the same microphones, you’ll need to cut them even more.)
The next thing to do is to add some compression. What you want to do is maintain as much of the singer's inflection as you can, while bringing out every syllable—or nearly every syllable. Play the track in bypass mode first and watch the meters. Make a note of the range covered and particularly the reading of the loudest spots. Set the threshold a bit below the loudest mark so the compressor is not working very hard. It will recover fastest and distort the least if it never gets into extreme change. (Remember, the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") object is a limiting compressor. Set the threshold at 0 and boost the input until the high point is just below this.)
Start with gentle (2:1) ratio and fast attack and release. Increase the ratio until the meters show the phrases have flattened out enough, generally within 12 to 6 dB throughout, and then slowly increase the attack time (reduce the rate). There will be a point where the voice suddenly starts jumping out. Keep it if you like it, but it will sound more natural if you back off of the setting a bit. Now increase the release time (decrease the rate) until the notes sustain well but you aren't getting bursts of breath.
For some singers, this procedure may be totally wrong—what you need to do is learn how the ratio, attack and release work with voices in general so you can respond to what you hear. Here are some situations to watch for:
  * A singer who does not sustain tones will benefit from short release times. Short release works like a guitar sustain pedal. On the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") you may want to tweak the gating threshold or progressive release parameters when you do this.
  * Some singers belt certain syllables. This is where the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") object shines—just reduce the threshold until the phrase evens out. With other devices, you may have to patch in a second limiter.
  * Some singer/microphone combinations will produce a lot of sibilance. A few compressors have a “de-essing” feature, which boosts the highs going into the measuring circuit. The hiss will then trigger extra gain reduction. The [omx.4band~](https://docs.cycling74.com/reference/omx.4band~ "omx.4band~") object can be used to do this.


## Bass
Bass players have to work hard to keep all of the notes even on their instrument. One reason for this is that the open notes are much more resonant than fretted ones. Amplifiers contribute their share of problems, and by the time you add the strangeness of close mic-ing a loudspeaker cone, the levels can vary widely. Unfortunately this interacts with a psychoacoustic quirk—our ears are less sensitive to soft bass tones than tones in the midrange, which paradoxically makes changes in the level of the bass more noticable. Compression can help; the amount of compression to use depends on the individual player, but it generally doesn’t have to be too heavy. When working with rock, you’ll need a lot to keep the bottom solid. The attack will vary according to the type of music. Jazz bass requires a smooth sound, so a quick attack will be used, but in hip hop the bass is almost a percussion part. Slow down the attack time to get a punchy sound. Avoid stretching the notes with slow release—it’ll sound muddy.
## Drums
If you only use overhead microphones for a drum set, all you want is peak limiting, because compression on cymbals usually sounds terrible. A snare microphone may be compressed if the head is dead or you want extra snare rattle, but a more effective approach is gating with a rather high threshold. That way most of the snare sound comes from the overheads, but the pop from the snare microphone will happen just a bit earlier and will give the rhythm a crisper sound. The gate keeps any leakage from the high hat out of the mix. To gate with the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~"), object, enable noise gating but not AGC.
Kick drum processing could fill an entire chapter of a book. In general, you are trying to find a balance between punch and mud. The compressor is used to suppress the ring while keeping or even amplifying the strike. A slow attack is indicated here, with the amount of compression determined by the length of ring from the drum.
Many times you will be trying to make up for the strange things drummers do to the kick drum to keep the sound from bleeding into other tracks. An untamed bass drum will ring quite a long time, and that very low frequency gets in everywhere. The result is you often see kicks with heads removed, holes cut in them, and various mutes attached. (The last one I recorded had a ten pound pillow in it.) The resulting sound is best described as “phlub”. One common trick is to use gated reverb. A fairly thick reverb is applied to the drum and fed through a compressor set up for external gating. The gate is controlled by the unprocessed sound of the drum, so you get a lot of extra sound, but it does not tail off like normal reverb. Some reverbs have gated settings, but you have little control over the effect.
## See Also
  * [omx.comp~ - OctiMax Compressor](https://docs.cycling74.com/reference/omx.comp~)
  * [omx.4band~ - OctiMax 4-band Compressor](https://docs.cycling74.com/reference/omx.4band~)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 1: Peak Limiting](https://docs.cycling74.com/learn/articles/17_msp_compress_01/)
  * [MSP Compression Tutorial 2: Basic Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_02/)
  * [MSP Compression Tutorial 3: Tweaking Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_03/)
  * [MSP Compression Tutorial 5: Multiband Compression 1](https://docs.cycling74.com/learn/articles/17_msp_compress_05/)
  * [MSP Compression Tutorial 6: Multiband Compression 2](https://docs.cycling74.com/learn/articles/17_msp_compress_06/)
  * [MSP Compression Tutorial 7: Keying](https://docs.cycling74.com/learn/articles/17_msp_compress_07/)
  * [MSP Compression Tutorial 8: Microsounds](https://docs.cycling74.com/learn/articles/17_msp_compress_08/)
  * [MSP Compression Tutorial 9: Ducking](https://docs.cycling74.com/learn/articles/17_msp_compress_09/)
  * [MSP Compression Tutorial 10: Controlling Feedback](https://docs.cycling74.com/learn/articles/17_msp_compress_10/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
