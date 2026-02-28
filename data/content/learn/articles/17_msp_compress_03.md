---
description: ''
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/17_msp_compress_03/
title: Tweaking Compression
---

Download Series Content and Patchers
# Tweaking Compression
There are more messages used to control the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") object than controls on many compressors. Using these messages gives you unprecedented access to the inner workings of the object and let you adjust the behavior for a wide variety of sounds. In addition to Threshold, ratio, Attack, and Release, the following messages are available: (Try them out in patcher _C3mTweakingCompression_.)
  * `channelCoupling` : Stereo signals naturally have different levels on each side. If one channel triggers compression but the other does not, the relative levels of the channels will be changed. This will result in a movement of the sound image. Therefore equal compression is applied to both channels even if only one needs it. Normally, the amount of compression is determined by the stronger channel at any moment. If `channelCoupling` is set to 1, compression will follow the left channel. On 2 the right channel determines the action.
  * `SmoothGain` :Since the level detector works in discrete steps, applying the level measurement directly to the gain control would result in stepped action or “zipper noise”. To prevent this, an envelope (similar to [line~](https://docs.cycling74.com/reference/line~/ "line~")) is applied to the control signal. `SmoothGain` controls the time of this envelope.
  * `Delay` : This message delays the application of the measurement to the amplifier control. This will allow fast peaks through for an extra punchy sound. Combined with a fast attack time, this will produce strong but very short drum kicks, perfect for hip hop.
  * `Sidechain` : A Sidechain filter applies the inverse vocal EQ described in the next tutorial to the measurement circuit. This will reduce the effect of vocals on the output level, useful if you are compressing a full mix. It will keep the voice from pushing down sustaining parts such as organ.
  * `NoiseGate` : Noise gating is almost always necessary when you compress audio from the real world. For instance, if you are recording a guitar amp, the compressor will emphasize the amp hum between notes. To help prevent this, the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") has a built-in noise gate. When enabled, this applies downward expansion to any signal below the `ngThreshold`. There are no attack and release controls because gating is normally applied to very quiet signals.
  * `Release` : The three messages `gatingLevel`, `freezeLevel`, and `progressiveRelease` make automatic adjustments to the release timer based on the input signal. Signals below the freeze level will not trigger any amplification. Signals above this but below gating level will have a slow release. Progressive release speeds up the release time on stronger inputs. This means that softer signals (where the ear is less sensitive to dynamic change) will not be as compressed as loud ones.
  * `LimEnabled` : This message puts an absolute limit on the strength of the output signal. This prevents a signal overload when the controls are set for punching.


## Parameter Messages
The OMX objects send messages from the third outlet when parameters are changed. These are in parameter lists, which contain 7 fields:
1.Scope 0 = global, 1 = presetable, 2 = end of list.
2.Name of parameter.
3.Current value.
4.Maximum value.
5.Minimum value
6.Display value.
7.Units – this is _arbitrary_ for most items.
The parameter values are arbitrarily scaled, most from 0 to 100. Some of these can be converted to familiar units. Any dB parameter can be converted by looking at the value shown when set at 0 – that’s the minimum value (100 corresponds to 0 dB). Divide 100 by this value to get the scaling factor. Then to set a value, add the absolute of the minimum and multiply by the absolute of the scaling factor, like this:
  * To convert agcThreshold (range from –36 to 0) use an [expr](https://docs.cycling74.com/reference/expr/ "expr") object with the following arguments: (36 + $i1) * 2.77.
  * To convert ngThreshold (range from –90 to 0) use an [expr](https://docs.cycling74.com/reference/expr/ "expr") object with the following arguments: (90 + $i1) * 1.11. It’s probably easier to capture the numbers coming out in the parameter messages and display those.
  * Ratio uses exponential values. To convert the numbers given to ratio use an [expr](https://docs.cycling74.com/reference/expr/ "expr") object with the following arguments: ln($f1) / ln (1.04).


## Presets
With so many parameters, some method for recalling combinations of settings is essential. The compressors have a few presets built in (selectable using the `ChoosePreset` message), but the ultimate solution will be to save the entire setup in a [coll](https://docs.cycling74.com/reference/coll/ "coll") or [pattr](https://docs.cycling74.com/reference/pattr/ "pattr") object. The `SaveSettings` message will give you a dump of all of the parameters.
## Metering
The right outlet provides gain metering if enabled with the `meters` message. The outputs are a list ready to be connected to a [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") object. The list for the [omx.comp~](https://docs.cycling74.com/reference/omx.comp~ "omx.comp~") shows left and right values for AGC gain, noise gate and limiter. The `meterRate` message determines how often these are sent. Alternately, you can get the values using the `meterData` message. The meters for the 4-band and 5- band compressors are quite elaborate.
## See Also
  * [omx.comp~ - OctiMax Compressor](https://docs.cycling74.com/reference/omx.comp~)
  * [Introduction: What is Compression?](https://docs.cycling74.com/learn/articles/17_msp_compress_00/)
  * [MSP Compression Tutorial 1: Peak Limiting](https://docs.cycling74.com/learn/articles/17_msp_compress_01/)
  * [MSP Compression Tutorial 2: Basic Compression](https://docs.cycling74.com/learn/articles/17_msp_compress_02/)
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
