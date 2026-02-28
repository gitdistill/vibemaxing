---
description: Using downsampled signal chains to generate Max data
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/11_polychapter03/
title: Audio-rate Control Data
---

Download Series Content and Patchers
# Polyphony Tutorial 3: Audio-Rate Control Data
## Low-frequency oscillators
This tutorial looks at using the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object to generate low-frequency oscillators (LFOs) to generate control-rate data for Max objects. There are many tasks in Max (such as graphics) that don't require control updates at audio rate (44,100 per second, or higher), and simply need to receive new values regularly at a lower speed. For example, a video processing patcher running at 30 frames per second would only need new information for all of its parameters every 33 milliseconds. At the same time, MSP signal generators make excellent choices for designing periodic sources of control information. The [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object has a simple way to _downsample_ the audio processing in an abstraction, so that it can be used to create control-rate data in Max without the CPU overhead of working at audio rate.
  * Take a look at the tutorial patcher. Turn on the [dac~](https://docs.cycling74.com/reference/dac~/ "dac~") (on the right) and the [metro](https://docs.cycling74.com/reference/metro/ "metro") (on the left) using the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") objects. You should see a line being drawn in the [lcd](https://docs.cycling74.com/reference/lcd/ "lcd") object on the right of the patcher. At any point, you can hit the space bar to `clear` the drawing.
  * In the [number](https://docs.cycling74.com/reference/number/ "number") boxes labeled `X` and `Y`, type `1.` and `1.3`, respectively. Look at the curve drawn in the [lcd](https://docs.cycling74.com/reference/lcd/ "lcd"). Clear the [lcd](https://docs.cycling74.com/reference/lcd/ "lcd") with the space bar and change the values to `1.` and `4.`. Notice that when the values are in an integer ratio the pattern begins redrawing itself after a while. Try your own numbers, or changing them as they go.


Using cosine waves of different frequencies as the X and Y inputs of a drawing surface (such as an oscilloscope) creates something called _lissajous_ curves. These patterns visually describe complex harmonic motion, so that X and Y patterns in simple ratios will create pre-determined repeating shapes.
## Using [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~")
  * Double-click one of the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") objects to see inside the `polylfo1~` abstraction.


Notice how simple our abstraction seems, with an [in](https://docs.cycling74.com/reference/in/ "in") object allowing use to set the frequency of a [cycle~](https://docs.cycling74.com/reference/cycle~/ "cycle~") object. A second [in](https://docs.cycling74.com/reference/in/ "in") object provides `bang` messages to a [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~"). The [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") object allows us to capture single values of MSP signals as floating-point numbers generated as Max events. Whenever a [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") receives a `bang`, it _samples_ the current MSP signal at its inlet and outputs that one sample as a floating-point value. In our tutorial, this value then goes to an [out](https://docs.cycling74.com/reference/out/ "out") object, and back into our main patcher.
## Changing abstractions
  * Close the abstraction `polylfo1~` and return to the main tutorial patcher. Click on the [message](https://docs.cycling74.com/reference/message/ "message") boxes in the middle that begin with the message `patchername`. The `patchername` message _reloads_ a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object with a new abstraction. Notice the effect on the drawing, depending on which you select and whether it applies to the X or Y [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object. Select `polylfo2~` and double-click the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object to see it.


The `polylfo2~` abstraction does the same as `polylfo1~`, but generates its output as a sawtooth wave rather than a cosine wave. The [phasor~](https://docs.cycling74.com/reference/phasor~/ "phasor~") object generates ramps from `0` to `1`, so we scale the output to go between `-1` and `1` with the [*~](https://docs.cycling74.com/reference/*~/ "*~") and [-~](https://docs.cycling74.com/reference/-~/ "-~") objects before we sample it with the [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~")
  * Switch one of the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") objects to `polylfo3~` and look inside.


The `polylfo3~` object generats a triangular output by using a [triangle~](https://docs.cycling74.com/reference/triangle~/ "triangle~") object. The [triangle~](https://docs.cycling74.com/reference/triangle~/ "triangle~") object wraps a [phasor~](https://docs.cycling74.com/reference/phasor~/ "phasor~") around a midpoint, essentially translating it into a triangular waveform. This object outputs values between `-1` and `1`, so it doesn't require any scaling.
## Resampling arguments
  * Close any open abstractions and return to the main patcher. Look at the arguments to the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") objects.


When working with an abstraction inside of a [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object, you can decide to work at a lower or higher _sampling rate_ than your main MSP patcher. This rate is not specified directly, but as a divisor or multiplier of the main rate. The arguments `up 2` will make the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") run at twice the sampling rate of the main patcher. The arguments `down 8`, as shown here, run the audio within the [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") objects at one _eighth_ the normal speed (i.e. 5.5125kHz if the main patcher runs at 44.1kHz). Since we're only sampling our oscillator values once every frame of the drawing (set by the [metro](https://docs.cycling74.com/reference/metro/ "metro") speed at 50Hz or every 20ms), this is more than enough resolution for our control data.
  * Mix and match different LFO curves by choosing different [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") abstractions run at different frequencies. Notice how the Lissajous curves behave with the different waveforms.


## Summary
The [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") object can work at a different sampling rate than its host MSP patcher. The `up` and `down` arguments allow you to specify a multiplier or divisor for the main sampling rate. When designing LFOs (low frequency oscillators), it's often useful to use massively downsampled MSP patchers inside of [poly~](https://docs.cycling74.com/reference/poly~/ "poly~") objects to generate the curves efficiently. the [snapshot~](https://docs.cycling74.com/reference/snapshot~/ "snapshot~") object allows you to sample a single value from an MSP signal in response to a `bang`.
## See Also
  * [snapshot~ - Convert signal values to numbers](https://docs.cycling74.com/reference/snapshot~/)



Kind
    Tutorial 

Category
    Audio 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
