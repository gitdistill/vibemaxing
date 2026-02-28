---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_08/
title: Microsounds
---

Download Series Content and Patchers
# Microsounds
We usually use the noise gate to keep from amplifying things that should not be heard when compressing. Sometimes these in-between sounds are very interesting in themselves. I like to record very tiny sounds, like the ticking of a mechanical stopwatch. When doing that, I use quite a lot of compression to bring up the ting of the spring while keeping the grind of the winding at a reasonable level. The tutorial patch is set up for this. Compression is applied to signals that are below the threshold, and signals above are unchanged. This leaves the notes essentially alone, but the sounds between the notes are brought out. (This is how a guitar sustain pedal works.) Of course there is a lot of junk at very low levels we don’t want to hear, so the patch has a second threshold; levels below this threshold are unaffected.
## Expansion
The tutorial patcher has one more trick. The ratio can be set below 1:1. Fractional ratios give expansion, where soft sounds are made softer. This can restore tracks that have been over compressed, or separate out the loudest sounds in a pattern.
## See Also
  * [rampsmooth~ - Smooth an incoming signal](https://docs.cycling74.com/reference/rampsmooth~/)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 1: Peak Limiting](https://docs.cycling74.com/learn/articles/17_msp_compress_01/)
  * [MSP Compression Tutorial 2: Basic Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_02/)
  * [MSP Compression Tutorial 3: Tweaking Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_03/)
  * [MSP Compression Tutorial 4: Compression on Real Instruments](https://docs.cycling74.com/learn/articles/17_msp_compress_04/)
  * [MSP Compression Tutorial 5: Multiband Compression 1](https://docs.cycling74.com/learn/articles/17_msp_compress_05/)
  * [MSP Compression Tutorial 6: Multiband Compression 2](https://docs.cycling74.com/learn/articles/17_msp_compress_06/)
  * [MSP Compression Tutorial 7: Keying](https://docs.cycling74.com/learn/articles/17_msp_compress_07/)
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
