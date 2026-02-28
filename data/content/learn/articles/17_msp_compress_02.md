---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_02/
title: Basic Compression
---

Download Series Content and Patchers
# Basic Compression
The _C2mBasicCompression_ patcher demonstrates some of the features of the compressor section of the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") object, which produces broadcast type compression and limiting. The signal source for this patch is in the steptone subpatcher. It generates a simple pattern of tones that gets louder and softer in 6 dB steps. The level of signal is shown in the meter labeled input. When the compressor is bypassed, this set of tones is heard with no processing. Uncheck the bypass box to hear the compressor in action.
## Threshold
With the opening settings in this patch, the compressor will keep all of the tones pretty much the same level at the output. Play with the threshold and you will see this level change. The center meter shows the internal action of the compressor. Gain is reduced as the bar drops.
If you have good speakers, you will notice the step tone generator produces a bit of distortion on the loudest notes. When the compressor is working, this distortion is heard on those same notes, no matter what the threshold setting. The moral illustrated here is that compression cannot fix problems that occur upstream in the recording process.
## Ratio
If you adjust the ratio down from the extreme setting, you will find the output levels begin to vary when input is below the threshold. (Parts of the signal above the threshold are still limited.) At a 1:1 ratio the output will follow the input. The most usable settings are generally 2:1 to 5:1, since this will maintain some shape to the phrase. You will see this when we start compressing actual signals.
There is a practical limit to how much a signal can be amplified. Below a certain point, all you are doing is bringing up noise. This limit is adjustable on the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~"), from 36 dB to 0. You'll find the range adjustment in the subpatcher labeled tweaks, which contains some (but by no means all) of the special parameters of the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") object. In hardware these are usually internal adjustments.
## Attack
Set the threshold to -10 and the compression ratio around 20:1. Now listen carefully to the attack portion of the tones. Compare this with the bypassed tone. It seems that the compressor is somehow accentuating the percussive aspect of the tone. Now reduce the attack rate a bit (this is the same as increasing attack time). You will hear even more pop in the sound. In fact, it will distort badly when the attack rate is too slow. Why? At the start of the sound, the compressor is amplifying as much as it can because there's no signal. When the sound level coming in increases faster than the compressor can respond, the internal gain will briefly be in the wrong mode, amplifying when it should be reducing. This will exaggerate the percussion effect. This kind of setting is known in the trade as “punching”, and is often applied to kick drums to give a strong sense of beat without overwhelming the band. This effect can be achieved with a bit more subtlety using the delay parameter as found in the tweaks subpatcher. The delay control delays the signal to the level detector. Naturally, threshold and ratio strongly affect this effect.
There is another tweak called smoothGain that will also affect this. Gain smoothing applies an envelope to the gain control. If you set gain smoothing to zero you will immediately hear why: the gain is actually changing in steps which produce a noise like a zipper. Gain smoothing affects the attack and release rates identically.
## Release
The step tone generator will also produce a steady low-pitched drone at -30 dB. If you turn it on while the step tones are running, you will hear the effect of the release rate Notice that the drone disappears when the step tone is above the threshold. That's to be expected, since the compressor is turning the entire signal down. In fact, if you watch the gain meter, you will note it accurately indicates the level of the drone. Listen to how the drone comes in — it comes up gradually, as the compression effect goes away. Now increase the ratio. The drone is louder between notes, and the pumping effect is more pronounced. Playing with the release time will provide some entertaining effects. At very short releases the drone pumping is quite noticeable, but if the release is too long, the step tones never get very loud and lose sync with the input. At the longest settings the drone goes away altogether.
Pumping makes background noise more annoying and can affect the reverberation on a voice or the sustain of a guitar. When an instrument with bass frequencies is mixed in with a sustaining instrument, the pumping effect is even worse. This is because a bass signal has to be stronger to 'sound' as loud as a signal in the treble range. As a result, even a reasonably soft bass sound will affect a piano. You can hear this effect by setting the swap toggle. This makes the stepped tone low frequency and the steady tone high frequency.
The [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") object overcomes this problem by dividing the bass signals off and treating them separately. The message dualBandEnable 1 as found in the tweaks subpatcher will turn this feature on. When dual band is enabled, bass signals have a lessened effect on the main band. (The gain indicator splits into two sections to show this.) Note that middle frequency signals will still control the bass level. Compression is often applied to individual bass tracks to control the resonance of open strings and add a bit of punch to uprights. If you are doing that, you don't want to be in dual mode.
## See Also
  * [omx.comp~ - OctiMax Compressor](https://docs.cycling74.com/reference/omx.comp~)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 1: Peak Limiting](https://docs.cycling74.com/learn/articles/17_msp_compress_01/)
  * [MSP Compression Tutorial 3: Tweaking Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_03/)
  * [MSP Compression Tutorial 4: Compression on Real Instruments](https://docs.cycling74.com/learn/articles/17_msp_compress_04/)
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
