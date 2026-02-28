---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_05/
title: Multiband Compression 1
---

Download Series Content and Patchers
# Multiband Compression 1
It’s usually the case that the bass, drums, vocals and other instruments are individually compressed before they are mixed together. Sometimes this is not possible or desirable. For instance, a radio station or a DJ may wish for a louder and more consistent sound than assorted CDs happen to provide. Simple compression is seldom satisfactory for this situation, because sustained parts will be pumped by the vocals and drums. To prevent this, a multiband compressor treats each section of the audio spectrum independently; you can have a full bass and constant rhythm while still letting the voice be heard.
The multiband compressor has found creative uses beyond the original intent of spicing up FM radio. If you start with a fairly intense broadband headbanger mix, you can use the device to cram every last dB into every octave for that solid wall-of-sound effect. Or, with a bit of restraint, you can master a recording to give a comfortable experience on a wide range of playback systems.
## Spectral Balancing
Good arrangers know how to orchestrate a score to give a balance between bass and treble that is satisfying and keeps the listener’s attention. This is called _spectral balance_. A similar effect can be achieved by compressing bass, midrange, treble, and high frequencies for consistency and adjusting the levels of each to fit a curve that matches mid and treble, leaves slightly less bass, and somewhat lower top end. This curve comes from analyzing the overall response of many successful albums.
The 4-band compressor does a good job of solidifying a mix. The tutorial patch shows the [omx.4band~](https://docs.cycling74.com/reference/omx.4band~ "omx.4band~") object in action. This is a really complex gadget, far more than four compressors lashed together. There is quite a bit of processing before the band-specific auto gain controls (AGCs).
There is a downward expander first, with an adjustable threshold to sweep away noise and dirt. This is followed by an overall AGC, then the signal is split into four bands that are (approximately) deep bass, normal bass, midrange (where most of the music occurs) and highs. There is a second downward expander on the high section, since high frequency noise is especially annoying. Each band has a control for drive (the threshold is fixed at 0, so more input gain here means more compression), attack, release, and level into the final mix. There’s a final limiter to prevent any peaking.
Start by trying the three presets on some commercial music (probably already sort of squashed). Play with the outmix faders to get a sense of where the bands are. Now try some raw tracks and adjust drive, attack and release to get the sound as full as possible. As always, you get the most obvious effects when the meters are dancing.
The meters are rather enigmatic, but here’s what they mean, left to right:
  * Left/right input. Provide enough signal to get these pretty high.
  * Release Gating Threshold. Release gating locks all release times when the input gets low—it helps prevent pumping of background noise. The indicator goes high when release gating is on. (Note how the gain bars all stall.)
  * The two expanders, wideband and highs. This shows the gain of the expanders, so when they drop, signal is being shut down.
  * The left and right master AGC gain. Usually you want the attack and release fairly slow, as these are just meant to keep the overall level in the center of the dial.
  * The gain in the four bands. Unity gain is the lowest position.
  * Left and right limiting action. If these are pushing the floor, back off on the input.
  * Left and right output levels.


After a bit of practice you should be able to produce a full satisfying sound on any kind of material. The best test is to get it to sound like the same music when played back softly or loud.
## See Also
  * [omx.4band~ - OctiMax 4-band Compressor](https://docs.cycling74.com/reference/omx.4band~)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 1: Peak Limiting](https://docs.cycling74.com/learn/articles/17_msp_compress_01/)
  * [MSP Compression Tutorial 2: Basic Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_02/)
  * [MSP Compression Tutorial 3: Tweaking Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_03/)
  * [MSP Compression Tutorial 4: Compression on Real Instruments](https://docs.cycling74.com/learn/articles/17_msp_compress_04/)
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
