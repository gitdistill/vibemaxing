---
description: List of Gen operators exclusive to gen~ or signal-rate Gen
group: Gen
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/gen/gen~_operators/
title: gen~ Operators
---

# gen~ Operators
The following Gen operators are unique to the [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") object, and operate in the audio domain.
## Buffer
  * [buffer](https://docs.cycling74.com/reference/gen_dsp_buffer/) : References a named [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object in the [gen~](https://docs.cycling74.com/reference/gen~/ "gen~") object's parent patch. The first argument specifies a name by which to refer to this data in other objects in the gen patcher (such as peek and poke); the second optional argument specifies the name of the external [buffer~](https://docs.cycling74.com/reference/buffer~/ "buffer~") object to reference (if ommitted, the first argument name is used). The first outlet sends the length of the buffer in samples; the second outlet sends the number of channels.
  * [channels](https://docs.cycling74.com/reference/gen_dsp_channels/) : The number of channels of a data/buffer object. The first argument should be a name of a data or buffer object in the gen patcher.
  * [cycle](https://docs.cycling74.com/reference/gen_dsp_cycle/) : An interpolating oscillator that reads repeatedly through one cycle of a sine wave. By default it is driven by a frequency input, but if the `@index` attribute is set to 'phase', it can be driven by a phase input instead.
  * [data](https://docs.cycling74.com/reference/gen_dsp_data/) : Stores an array of sample data (64-bit floats) usable for sampling, wavetable synthesis and other purposes. The first argument specifies a name by which to refer to this data in other objects in the gen patcher (such as peek and poke); the second optional argument specifies the length of the array (default 512 samples); and the third optional argument specifies the number of channels (default 1). The first outlet sends the length of the buffer in samples; the second outlet sends the number of channels.
  * [dim](https://docs.cycling74.com/reference/gen_dsp_dim/) : The length (in samples) of a data/buffer object. The first argument should be a name of a data or buffer object in the gen patcher.
  * [lookup](https://docs.cycling74.com/reference/gen_dsp_lookup/) : Index a data/buffer object using a signal, for waveshaping. The first argument should be a name of a data or buffer object in the gen patcher. The second argument specifies the number of output channels. Input signals in the range -1 to 1 are mapped to the full size of the data/buffer, with linear interpolation. The last inlet specifies a channel offset (default 0).
  * [nearest](https://docs.cycling74.com/reference/gen_dsp_nearest/) : Multi-channel lookup a data/buffer object (no interpolation). The first argument should be a name of a data or buffer object in the gen patcher. The second argument specifies the number of output channels. The input phase ranges from 0 to 1, and wraps outside this range. The last inlet specifies a channel offset (default 0).
  * [peek](https://docs.cycling74.com/reference/gen_dsp_peek/) : Read values from a data/buffer object. The first argument should be a name of a data or buffer object in the gen patcher. The second argument specifies the number of output channels. The first inlet specifes a sample index to read (no interpolation); indices out of range return zero. The last inlet specifies a channel offset (default 0).
  * [poke](https://docs.cycling74.com/reference/gen_dsp_poke/) : Write values into a data/buffer object. The first argument should be a name of a data or buffer object in the gen patcher. The second argument (or third inlet if omitted) specifies which channel to use. The first inlet specifies a value to write, while the second inlet specifies the sample index within the data/buffer. If the index is out of range, no value is written.
  * [sample](https://docs.cycling74.com/reference/gen_dsp_sample/) : Linear interpolated multi-channel lookup of a data/buffer object. The first argument should be a name of a data or buffer object in the gen patcher. The second argument specifies the number of output channels. The last inlet specifies a channel offset (default 0).
  * [splat](https://docs.cycling74.com/reference/gen_dsp_splat/) : Mix values into a data/buffer object, with linear interpolated overdubbing. The first argument should be a name of a data or buffer object in the gen patcher. The second argument (or third inlet if omitted) specifies which channel to use. The first inlet specifies a value to write, while the fractional component of the second inlet specifies a phase (0..1) within the data/buffer (indices out of range will wrap). Splat writes with linear interpolation between samples, and mixes new values with the existing data (overdubbing).
  * [wave](https://docs.cycling74.com/reference/gen_dsp_wave/) : Wavetable synthesis using a data/buffer object. The first argument should be a name of a data or buffer object in the gen patcher. The second argument specifies the number of output channels. The first inlet specifies phase (0..1), while the second and third inlets specify start/end sample positions within the data/buffer. The last inlet specifies a channel offset (default 0).


## Convert
  * [atodb](https://docs.cycling74.com/reference/gen_dsp_atodb/) : Convert linear amplitude to deciBel value
  * [dbtoa](https://docs.cycling74.com/reference/gen_dsp_dbtoa/) : Convert deciBel value to linear amplitude
  * [ftom](https://docs.cycling74.com/reference/gen_dsp_ftom/) : Frequency given in Hertz is converted to MIDI note number (0-127). Fractional note numbers are supported. The second input sets the tuning base (default 440).
  * [mstosamps](https://docs.cycling74.com/reference/gen_dsp_mstosamps/) : Convert period in milliseconds to samples
  * [mtof](https://docs.cycling74.com/reference/gen_dsp_mtof/) : MIDI note number (0-127) is converted to frequency in Hertz. Fractional note numbers are supported. The second input sets the tuning base (default 440).
  * [sampstoms](https://docs.cycling74.com/reference/gen_dsp_sampstoms/) : Convert period in samples to milliseconds


## Constants
  * [fftfullspect](https://docs.cycling74.com/reference/gen_dsp_fftfullspect/), [FFTFULLSPECT](https://docs.cycling74.com/reference/gen_dsp_fftfullspect/) : The pfft~ full spectrum flag (0/1)
  * [ffthop](https://docs.cycling74.com/reference/gen_dsp_ffthop/), [FFTHOP](https://docs.cycling74.com/reference/gen_dsp_ffthop/) : The pfft~ FFT hop size
  * [fftoffset](https://docs.cycling74.com/reference/gen_dsp_fftoffset/), [FFTOFFSET](https://docs.cycling74.com/reference/gen_dsp_fftoffset/) : The pfft~ FFT offset
  * [fftsize](https://docs.cycling74.com/reference/gen_dsp_fftsize/), [FFTSIZE](https://docs.cycling74.com/reference/gen_dsp_fftsize/) : The pfft~ FFT frame size
  * [samplerate](https://docs.cycling74.com/reference/gen_dsp_samplerate/), [SAMPLERATE](https://docs.cycling74.com/reference/gen_dsp_samplerate/) : The DSP samplerate. Will return 1000@interval\frac{1000}{@interval}@interval1000​ for event-rate [gen](https://docs.cycling74.com/reference/gen/ "gen").
  * [vectorsize](https://docs.cycling74.com/reference/gen_dsp_vectorsize/), [VECTORSIZE](https://docs.cycling74.com/reference/gen_dsp_vectorsize/) : The DSP vectorsize. Will return 1 for event-rate [gen](https://docs.cycling74.com/reference/gen/ "gen").


## DSP
  * [fixdenorm](https://docs.cycling74.com/reference/gen_dsp_fixdenorm/) : This operator detects denormal numbers and replaces them with zero. Note: As of Max 6.0 the x87 control flags are set to flush to zero and disable exception handling in audio processing, so denormal fixing should only be required for exported code. A denormal number is a floating point value very close to zero (filling the underflow gap). Calculations with denormal values can be up to 100 times more expensive, so it is often beneficial to replace them with zeroes. Denormals often occur in feedback loops with multipliers, such as filters, delays and exponential decays. Denormal detection is based on a bitmask. Note that feedback operators in gen~ (delay, history) apply fixdenorm to their input signals by default.
  * [fixnan](https://docs.cycling74.com/reference/gen_dsp_fixnan/) : This operator replaces NaNs with zero. A NaN (Not a Number) is a floating point data value which represents an undefined or unrepresentable value, such as the result of dividing by zero. Computations on NaNs produce more NaNs, and so it is often preferable to replace the NaN with a zero value. Note that division and modulo operators in gen~ protect against generating NaNs by default.
  * [isdenorm](https://docs.cycling74.com/reference/gen_dsp_isdenorm/) : This operator detects denormal numbers and returns 1 if the input is denormal, and zero otherwise. Note: As of Max 6.0 the x87 control flags are set to flush to zero and disable exception handling in audio processing, so denormal fixing should only be required for exported code. A denormal number is a floating point value very close to zero (filling the underflow gap). Calculations with denormal values can be up to 100 times more expensive, so it is often beneficial to replace them with zeroes. Denormals often occur in feedback loops with multipliers, such as filters, delays and exponential decays. Denormal detection is based on a bitmask. Note that feedback operators in gen~ (delay, history) apply fixdenorm to their input signals by default.
  * [isnan](https://docs.cycling74.com/reference/gen_dsp_isnan/) : This operator detects the presence of NaN values, returning 1 if the input is NaN, and zero otherwise. A NaN (Not a Number) is a floating point data value which represents an undefined or unrepresentable value, such as the result of dividing by zero. Computations on NaNs produce more NaNs, and so it is often preferable to replace the NaN with a zero value. Note that division and modulo operators in gen~ protect against generating NaNs by default.
  * [t60](https://docs.cycling74.com/reference/gen_dsp_t60/) : Given an input T, returns a number X such that, after T multiplications of a signal by X, that signal would be attenuated by 60 decibels. Roughly, -60db = 0db * pow(X, T). This could be used as a per-sample multiplier (X) to ensure a decay time (of T samples), for example. The name t60 is borrowed from the RT60 time used to measure reverberation time, which specifies the time taken for a signal to decay by 60db, as an approximation of fading to inaudibility.
  * [t60time](https://docs.cycling74.com/reference/gen_dsp_t60time/) : Estimates the decay time (in samples) of a given decay factor. That is, given a multiplier X, returns a number T such that, after T multiplications of a signal by X, that signal would be attenuated by 60 decibels. It is the dual of the t60 object.


## Feedback
  * [delay](https://docs.cycling74.com/reference/gen_dsp_delay/) : Delays a signal by a certain amount of time (specified in samples). The first argument specifies the maximum delay time (in samples, default samplerate). The second argument specifies the number of tap inlet/outlet pairs (default 1). The first inlet is the signal to be delayed. Additional inlets specify the delay time per tap (in samples). With `@feedback` 1, like history, delay allows feedback loops in the patcher, but minium delay is 1 sample. With `@feedback` 0, minimum delay time is zero samples (or more if `@interp` is cubic, spline, or spline6)
  * [history](https://docs.cycling74.com/reference/gen_dsp_history/) : The history operator allows feedback in the gen patcher through the insertion of a single-sample delay. The first argument is an optional name for the history operator, which allows it to also be set externally (in the same way as the param operator). The second argument specifies an initial value of stored history (defaults to zero).


## FFT
  * [fftinfo](https://docs.cycling74.com/reference/gen_dsp_fftinfo/) : fftinfo gets constant data about the FFT frames in a patcher loaded by pfft~. If it is used in a patcher that is not loaded by pfft~, it returns default constants instead.


## Filter
  * [change](https://docs.cycling74.com/reference/gen_dsp_change/) : Returns the sign of the difference between the current and previous input: 1 if the input is increasing, -1 if decreasing, and 0 if unchanging.
  * [dcblock](https://docs.cycling74.com/reference/gen_dsp_dcblock/) : A one-pole high-pass filter to remove DC components. Equivalent to the GenExpr: `History x1, y1; y = in1 - x1 + y1*0.9997; x1 = in1; y1 = y; out1 = y;`
  * [delta](https://docs.cycling74.com/reference/gen_dsp_delta/) : Returns the difference between the current and previous input.
  * [interp](https://docs.cycling74.com/reference/gen_dsp_interp/) : Smoothly mix between inputs, according to an interpolation factor in the range of 0 to 1 (first inlet). The @mode attribute can choose between linear or cosine interpolation to mix between two additional inlets, cubic or spline to mix between four inlets, and spline6 to mix between six inlets. The default mode is linear.
  * [latch](https://docs.cycling74.com/reference/gen_dsp_latch/) : Conditionally passes or holds input. The first inlet is the 'input' and the second inlet is the 'control'. When the control is non-zero, the input value is passed through. When the control is zero, the previous input value is output. It can be used to periodically sample & hold a source signal with a simpler trigger logic than the sah operator.
  * [phasewrap](https://docs.cycling74.com/reference/gen_dsp_phasewrap/) : Wrap input to the range -pi to +pi
  * [sah](https://docs.cycling74.com/reference/gen_dsp_sah/) : The first inlet is the 'input' and the second inlet is the 'control'. When the control makes a transition from being at or below the trigger value to being above the trigger threshold, the input is sampled. The sampled value is output until another control transition occurs, at which point the input is sampled again. The default threshold value is 0, but can be specified as the last inlet/argument. The `@init` attribute sets the initial previous value to compare to (default 0).
  * [slide](https://docs.cycling74.com/reference/gen_dsp_slide/) : Use the slide operator for envelope following and lowpass filtering. Related to the MSP [slide~](https://docs.cycling74.com/reference/slide~/ "slide~") object.


## Global
  * [elapsed](https://docs.cycling74.com/reference/gen_dsp_elapsed/) : The number of samples elapsed since the patcher DSP began, or since the last reset.
  * [mc_channel](https://docs.cycling74.com/reference/gen_dsp_mc_channel/) : If used within a patcher inside [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~"), the mc_channel operator will return the current channel index. Otherwise, it always returns 1.
  * [mc_channelcount](https://docs.cycling74.com/reference/gen_dsp_mc_channelcount/) : If used within a patcher inside [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~"), the mc_channelcount operator will return the channel count of the [mc.gen~](https://docs.cycling74.com/reference/mc.gen~ "mc.gen~"). Otherwise, it always returns 1.
  * [voice](https://docs.cycling74.com/reference/gen_dsp_voice/) : If used within a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") patcher, the voice operator will return the current voice index (similar to [thispoly~](https://docs.cycling74.com/reference/thispoly~/ "thispoly~")). Otherwise, it always returns 1.
  * [voicecount](https://docs.cycling74.com/reference/gen_dsp_voicecount/) : If used within a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") patcher, the voicecount operator will return the current voice count. Otherwise, it always returns 1.


## Integrator
  * [*=](https://docs.cycling74.com/reference/gen_dsp_mulequals/), [mulequals](https://docs.cycling74.com/reference/gen_dsp_mulequals/) : The object multiplies by, and then outputs, an internal value. This occurs at sample-rate, so the stored value can grow very large or very small, very fast. The value to be multiplied by is specified by either the first inlet or argument. The internal sum can be reset to the minimum by sending a nonzero value to the right-most inlet. The minimum value is 0 by default, but can be changed with the @min attribute. An optional maximum value can be specified with the @max attribute; values will wrap at the maximum.
  * [+=](https://docs.cycling74.com/reference/gen_dsp_plusequals/), [accum](https://docs.cycling74.com/reference/gen_dsp_accum/), [plusequals](https://docs.cycling74.com/reference/gen_dsp_plusequals/) : The object adds to, and then outputs, an internal sum. This occurs at sample-rate, so the sum can grow very large, very fast. The value to be added is specified by either the first inlet or argument. The internal sum can be reset to the minimum by sending a nonzero value to the right-most inlet. The minimum value is 0 by default, but can be changed with the @min attribute. An optional maximum value can be specified with the @max attribute; values will wrap at the maximum.
  * [counter](https://docs.cycling74.com/reference/gen_dsp_counter/) : Accumulates and outputs a stored count, similarly to Max's counter object, but triggered at sample-rate. The amount to accumulate per sample is set by the first input (incr). The count can be reset by a non-zero value in the second input (reset). The third inlet (max) sets a maximum value; the counter will wrap if it reaches this value. However if the maximum value is set to 0 (the default), the counter will assume no limit and count indefinitely. The first outlet outputs the current count, the second outlet outputs 1 when the count wraps at the maximum and zero otherwise, and the third outlet outputs the number of wraps (the carry count).


## Numeric
  * [round](https://docs.cycling74.com/reference/gen_dsp_round/) : Returns the integral value that is nearest to the input, with halfway cases rounded away from zero.


## Waveform
  * [phasor](https://docs.cycling74.com/reference/gen_dsp_phasor/) : A non-bandlimited sawtooth-waveform signal generator which can be used as LFO audio signal or a sample-accurate timing/control signal.
  * [rate](https://docs.cycling74.com/reference/gen_dsp_rate/) : The rate operator time-scales an input phase (such as from a phasor) by a multiplier. Multipliers less than 1 create several ramps per phase cycle.
  * [train](https://docs.cycling74.com/reference/gen_dsp_train/) : [train](https://docs.cycling74.com/reference/gen_dsp_train/ "gen_dsp_train") generates a pulse signal whose period is specifiable in terms of samples. The first input sets the pulse period (in samples). The second input sets the pulse width (default 0.5). The third inlet sets the phase of the 'on' portion (default 0.)
  * [triangle](https://docs.cycling74.com/reference/gen_dsp_triangle/) : A triangle/ramp wavetable with input to change phase offset of the peak value. The phase ranges from 0 to 1 (and wraps outside these values). With a duty cycle of 0, it produces a descending sawtooth; with a duty cycle of 1 it produces ascending sawtooth; with a duty cycle of 0.5 it produces a triangle waveform. Output values always bounded in 0 to 1.


## See Also
  * [mg_gen](https://docs.cycling74.com/userguide/mc/mc_gen/)


