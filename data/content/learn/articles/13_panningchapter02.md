---
description: Mixing multiple sources in a stereo context
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/13_panningchapter02/
title: Stereo panning
---

Download Series Content and Patchers
# MSP Panning Tutorial 2: Stereo panning
## Panning and Balance
The concept of "panning" is really about placing a monaural signal in a stereo sound field. If the source material is stereo to begin with, we are concerned with _balance_ , which adjusts the relative strength of the left and right channel. It would seem that we should ensure that the signal does not change in loudness as we change the balance (assuming left and right are the same level to start with) but that is not actually possible. The perceived loudness from the combination of two signals depends strongly on the nature of the signals. If the two signals are exactly the same, two copies will combine to be 6dB louder than one alone. If the signals have nothing in common, combining them will only provide a 3dB boost. Most stereo signals are similar in the left and right channels, but not identical. Combining them is somewhere between 3 and 6dB louder than either alone. Thus, a balance control (or pan for that matter) should probably produce about 4.5 dB of extra gain when the control is at either extreme.
**Technical Note:** The similarity of one signal to another is their _correlation_. If you add two copies of the same signal, you get a signal of twice the amplitude, which, once you have gone through the math of converting to decibels, is a 6 dB change. If you add two uncorrelated signals, such as different sources of noise, components will statistically add about half the time, so the sum of those will be a 3 dB increase. Correlation can be negative, in which case the sum of the signals is softer than either. Negative correlation usually is the result of one signal being 180° out of phase.
## Balancing act
  * Double click the subpatch named Balance to open it. Click the `startwindow` message to turn audio on.


There is a subpatcher named `stereo_source` on the left side of the patch. That contains a simple tone mechanism, an [sfplay~](https://docs.cycling74.com/reference/sfplay~/ "sfplay~") object loaded with a short stereo file, and an [adc~](https://docs.cycling74.com/reference/adc~/ "adc~") object so you can apply your choice of program material. The [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") labeled "Play" starts the tone genereator and muisc playback. There is a [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") object to select which source is heard.
  * Select `tones` on the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu").


You should hear two tones pulsing together. These include a low pitch in the left channel and a higher pitch in the right channel. Adjust your listening equipment so they are the same level. Now play with the Balance slider. The relative strengths of left and right should be apparent. You can return to equal any time by douple clicking on the [loadmess](https://docs.cycling74.com/reference/loadmess/ "loadmess") object. But wait, they aren't equal, are they? The strength of each tone in shown in the two float [number](https://docs.cycling74.com/reference/number/ "number") boxes labeled "Coefficients", and they aren't quite the same. That's because 64 is not exactly in the middle of the range of 0 through 127 as discussed in the last tutorial. However, the difference only amounts to 0.137 dB, and I doubt anyone's speakers are that well matched. Certainly no stereo signal is going to be that precise.
This patch introduces yet another crossfading formula (often used for pan as well as balance). This is an exponential curve, similar to what you get with audio hardware. You see this:
pow($f1,0.75)
in two [expr](https://docs.cycling74.com/reference/expr/ "expr") objects. The pow() function raises the first number (base) to the power of the second number (exponent). With an exponent that ranges from 0 to 1, the result will produce a sagging curve from 0 to 1. If you watch the [number](https://docs.cycling74.com/reference/number/ "number") boxes labled "Gain in dB" you will see little change for each side until the slider is in the last stage of its journey. This fits the sensitivity of the ear fairly well. Choose the music options on the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") to get a sense of the subtle diferences. As you play with the balance, keep an eye on the meter at the very bottom of the patch. This shows the sum of left and right, and should always be about the same.
Other parts of the patch should be familiar by now. There is a combination of `$1 20` message and [line~](https://docs.cycling74.com/reference/line~/ "line~") object to prevent crackles when the slider is changed, and a signal multiply ([*~](https://docs.cycling74.com/reference/*~/ "*~")) object for each channel to do the gain change.
## Blending in
  * Turn off audio, close the Balance patch and open the `blend` subpatch.


We sometimes need to convert a stereo signal to mono, and this can be done simply by adding the left and right channels and reducing the volume a bit. The amount to reduce the volume should be 3 to 6 dB as discussed above. A more useful control is a _blend_ which allows a gradual reduction in separation.
The `Blend` subpatcher takes a very direct approach to the problem. First, a mono signal is created. In this case a reduction of 6 dB is in order to prevent any possibility of an overload. This is accomplished by a [*~](https://docs.cycling74.com/reference/*~/ "*~") object with an argument of 0.5. Then each channel becomes a balanced combination of the original chanel and the mono signal. This is done with the blend control already developed. The colored objects in the patch trace the signal flow—green for the left channel signals, red for right, and yellow for the combination of the two. The blue [line~](https://docs.cycling74.com/reference/line~/ "line~") object controls the original left and right channels together.
  * Now use the `startwindow` message to turn audio on. (We don't want the closed subpatchers playing to confuse what we hear.) Experiment with the "Balance" slider and note how the width of the sound image changes.


## MS and Width
There is a little used but elegant recording technique called _Middle-Side_ or just _MS_. Recordings in this style are made with two microphones placed as close together as possible, often two elements within the same body. One mic is either omnidirectional (and picks up everything) or cardioid facing forward. This is the _Middle_ signal. The other mic is a figure 8 type turned sideways (with the dead zone pointing toward the stage). This will pick up only sources from the left or right, but nothing from the center. In addition, signals that originate on the right will be inverted in phase. This is the _Side_ signal. The conversion from MS format to Stereo is simple—the left channel is the sum of the middle and side signals, and the right channel is the difference of the two.
There is a fair amount of discussion about the merits of MS recording, but one important benefit is that it is easily converted to mono—you simply use the Middle signal. A related benefit is you can control the width of the stereo image by changing the amount of side signal added or subtracted from the middle. Microphones built into video cameras often use this technique to "zoom" audio. We can also use this technique to process the width of normal stereo signals.
  * Open the `MS Width` subpatch.


The `MS Width` subpatch uses the same stereo sources as the other patches, but converts them to MS format by adding both channels (Middle) and subtracting Right from Left (Side). The width slider controls the amount of side signal in a simple linear fashion. The conversion back to stereo is made by [+~](https://docs.cycling74.com/reference/%2B~/ "+~") objects. The left channel gets the sum of middle and side, while the side is inverted (by [*~](https://docs.cycling74.com/reference/*~/ "*~") object with an argument of -1) and added to middle to create the right channel. The result is the same as the blend operation, but acheived in a simpler way.
## Summary
Stereo signals cannot be panned in the sense of turning a camera left or right, but the impression that a source was more to the right or left can be affected by the _balance_ or relative strength of the left and right channel. The stereo effect can be diminished by _blending_ the two channels, which affects the apparent _width_ of the sound stage. These effects can be accomplished in MSP with the most basic objects.
## See Also
  * [scale -](https://docs.cycling74.com/reference/scale/)
  * [expr -](https://docs.cycling74.com/reference/expr/)
  * [*~ -](https://docs.cycling74.com/reference/*~/)
  * [+~ -](https://docs.cycling74.com/reference/+~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
