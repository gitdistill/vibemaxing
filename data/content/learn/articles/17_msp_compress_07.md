---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_07/
title: Keying
---

Download Series Content and Patchers
# Keying
In _keying_ , one sound turns another on (keying is sometimes referred to as “side-chain gating” and the “key” is sometimes called the side-chain signal). This can produce some interesting electronic music effects, such as drum rhythms imposed on a chorus. The patch shows the compression patch modified for keying. This did not require many changes—simply the separation of the control signal from the processed signal and the removal of the switch that triggers unity gain at the threshold. One more thing—the sense of the gain calculation (difference between the control and the threshold) is reversed by exchanging the leads on the math subpatch. Thus the amplification of the left signal is set by the level minus the threshold. When the control level is below the threshold this is negative, giving a reduction in gain.
This kind of patch can be fussy about levels, so an output gain is provided to give extra boost if needed.
With this setup, a signal in the left channel will not pass through unless a signal is present on the right channel. The ratio determines how much effect the control has on the left signal. If the ratio is set to 1:1, there is no effect at all. For ratios much above 2:1, there may be some distortion. The threshold determines how strong the control has to be to turn the left input on.
## See Also
  * [rampsmooth~ - Smooth an incoming signal](https://docs.cycling74.com/reference/rampsmooth~/)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 1: Peak Limiting](https://docs.cycling74.com/learn/articles/17_msp_compress_01/)
  * [MSP Compression Tutorial 2: Basic Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_02/)
  * [MSP Compression Tutorial 3: Tweaking Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_03/)
  * [MSP Compression Tutorial 4: Compression on Real Instruments](https://docs.cycling74.com/learn/articles/17_msp_compress_04/)
  * [MSP Compression Tutorial 5: Multiband Compression 1](https://docs.cycling74.com/learn/articles/17_msp_compress_05/)
  * [MSP Compression Tutorial 6: Multiband Compression 2](https://docs.cycling74.com/learn/articles/17_msp_compress_06/)
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
