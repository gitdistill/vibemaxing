---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_01/
title: Peak Limiting
---

Download Series Content and Patchers
# Peak Limiting
The patcher _C1mPeakLimiting_ illustrates the use of the [omx.peaklim~](https://docs.cycling74.com/reference/omx.peaklim~ "omx.peaklim~") object. You can see it in action by applying any signal with varying levels. Most pop music is heavily compressed, and won't do much here. Try raw drum recordings if you have any, or classical music or recordings of spoken word
The meters show the level of the input, the action of the amplifier, and the output level. If you increase the input gain, you will see the level increase to a point, but then the gain slams down so that the output won't be allowed to reach the distortion point. You can then lower the output gain to get the original signal level with the peaks removed, as shown in the figure below.
![](https://docs.cycling74.com/images/6f15673a8ba68c6259f0440e93fdd57b_271.webp) Figure 1. Peak limiting before (top) and after (Input +10 Threshold -1, output –10.)
If you raise the threshold, distortion can occur and will be very audible. If you lower the threshold, the gain indicator will be mostly in the low position, and the overall effect will be a lot quieter. Raising the output gain will restore the original signal level, but you will find quiet spots in the input contain things you didn't notice before. The overall impression of loudness should be much stronger than before. This is heavy limiting.
Figure 2 shows the before and after of heavy limiting on a drum track. You can see how the pop of the drums is stretched into a nearly continuous sound.
![](https://docs.cycling74.com/images/c417d7943f8f4132157f51afbb0c3383_280.webp) Figure 2. Input + 20, threshold - 12, output 0
The [omx.peaklim~](https://docs.cycling74.com/reference/omx.peaklim~ "omx.peaklim~") object has two modes that switch response times. Mode 0 is very fast and will suppress the shortest of transients. However, if the limiting is kicking in and out a lot, you will hear the signal get chopped up. Mode 1 is a bit more leisurely. This will allow peaks through in percussion tracks, but will sound nicer with vocal or instrumental material. The change is too subtle to show on the meters, but you should be able to hear it.
Peak limiting is often used as a safety net when recording unpredictable musicians. Many recorders have peak limiting built in. Heavy limiting gives a very full sound, but the increase in between-the-notes grunge makes the mix muddy. Generally, for sweetening sounds you will want to use a compressor that has more finesse.
## See Also
  * [omx.peaklim~ - OctiMax Peak Limiter](https://docs.cycling74.com/reference/omx.peaklim~)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 2: Basic Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_02/)
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
