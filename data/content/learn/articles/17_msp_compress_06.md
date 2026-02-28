---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_06/
title: Multiband Compression 2
---

Download Series Content and Patchers
# Multiband Compression 2
## Mastering
Mastering for different qualities of playback gear is a special art. The major difference between systems is the bass response of the speakers. We would all like true response down to the limit of hearing, but physics and economics work against that. Most budget speaker systems bottom out at 100 Hz or so, the bass driver’s resonant frequency. If a speaker is resonant at 100 Hz, a 50 Hz signal will excite that resonance, and so will a 55 Hz signal. The result is that anything lower that the speaker is equipped to handle will just add mud to the low end. Mastering engineers know this and roll off the signal below 75 Hz or so. So, what’s left to offer someone who spends the money to get speaker with a good bass response? Instead of just throwing out the deep bass, we want to control it so that there’s something for good speakers to reproduce without getting the less expensive speakers overly excited. A multiband compressor is just the thing, because we can keep the bass full without crossing the line. (To do this properly you have to listen to the mix on appropriate speakers, which is why you often see low-end Radio Shack and Yamaha boxes in million dollar recording rooms.)
We also usually roll off the high end just a bit, as compressed highs keep the attacks crisp. However, if the level is too high the effect is overly bright.
The [omx.5band~](https://docs.cycling74.com/reference/omx.5band~ "omx.5band~") object compressor is detailed enough to provide this kind of fine control. (See the tutorial patcher.)
In addition to the features of the 4 band, the 5 band compressor features:
  * Five bands. The midrange is split into two, and the low bands are a bit lower.
  * An individual downward expander (noise gate) on each band.
  * Individual threshold and limiting on each band.
  * A switch on each band that sets what happens at the threshold. Amplification happens below the threshold, but you have your choice of limiting or unity gain above.
  * The Overall AGC is split into two bands, with the lower labeled _Bass Enhancement_. These are slow-acting circuits that keep the input where the compression can have best effect.
  * An extra “soft” clipper on the deep bass. Set this so small speakers aren’t thrown into resonance by notes below their range.
  * A “spatial enhancer.” This separates the channels of mixes that are nearly but not quite mono. (A very common mixing style, especially over the radio.) It does so by subtracting a bit of left from the right signal and vice versa, but only when the two are nearly the same. The parameters for this are desired difference between the side signal and the combined (mono) signal, maximum gain on the difference signals, and speed of response to changes in separation.


The presets in the [omx.5band~](https://docs.cycling74.com/reference/omx.5band~ "omx.5band~") object illustrate various kinds of processing curves. The “Universal” setting is just a general boost to the sound, with a 3-to-1 compression and no limiting. Bass enhancement is switched in for a bit of warmth. The “Pop” setting, on the other hand, sets a 50:1 compression with hard driven limiting in the lowest two bands. The gives a solid bottom to the sound. The “Hit Radio” settings are a compromise between the two. You will note that the times are all about the same, with appropriately slower attack and release in the low bands. “FM Radio” differs primarily in the high end, which is compressed a bit tighter than the pop and hit settings.
Since the [omx.5band~](https://docs.cycling74.com/reference/omx.5band~ "omx.5band~") object uses seven times as much CPU as the four-band version, it may not be appropriate for everyday use—but it will be perfect for a few tough tasks.
## See Also
  * [omx.4band~ - OctiMax 4-band Compressor](https://docs.cycling74.com/reference/omx.4band~)
  * [omx.5band~ - OctiMax 5-band Compressor](https://docs.cycling74.com/reference/omx.5band~)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 1: Peak Limiting](https://docs.cycling74.com/learn/articles/17_msp_compress_01/)
  * [MSP Compression Tutorial 2: Basic Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_02/)
  * [MSP Compression Tutorial 3: Tweaking Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_03/)
  * [MSP Compression Tutorial 4: Compression on Real Instruments](https://docs.cycling74.com/learn/articles/17_msp_compress_04/)
  * [MSP Compression Tutorial 5: Multiband Compression 1](https://docs.cycling74.com/learn/articles/17_msp_compress_05/)
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
