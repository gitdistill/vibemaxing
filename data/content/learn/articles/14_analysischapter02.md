---
description: Looking at MSP signal data within the patcher
group: MSP Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/14_analysischapter02/
title: Oscilloscopes and Spectroscopes
---

Download Series Content and Patchers
# MSP Analysis Tutorial 2: Oscilloscope and Spectroscope
There are times when seeing a picture of a signal is instructive. in the real world, this is done with an oscilloscope, which shows a graph of amplitude over time. Max has two ways to do this. The old school method uses a dedicated [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") object, and the new school method uses jitter. The new has not replaced the old, there are applications for each.
There are two problems to overcome when plotting a graph of a signal in real time. First of all, in order for your eye to follow a time-varying signal, an excerpt of the signal must be captured and displayed for a certain period of time (long enough for you really to see it). Therefore, the graph must be displayed periodically, and will always lag a bit behind what you hear. Second, there aren't enough pixels on the screen for you to see a plot of every single sample (at least, not without the display being updated at blinding speed), so the display has to use a single pixel to summarize many samples.
## Old School: [scope~](https://docs.cycling74.com/reference/scope~/ "scope~")
The [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") object shows up as a rectangular display subdivided with a faint grid. When audio is on, there is a horizontal line showing the waveform connected to the left inlet. (This line is called the _trace_.) The principle of operation is simple. A group of samples is gathered and a composite value is calculated and placed at one point in a buffer. The process repeats until the buffer is full. When the buffer is full, lines are drawn from point to point across the display. The number of samples per point is set by the `calccount` attribute (this can be changed by an int in the left inlet). The number of points is set by the `buffer size` attribute (this can be changed by an int in the right inlet). Getiing a useful display depends on the selection of `calccount` and `buffer size`, and those depend on what you are trying to show.
### Showing Waveforms
  * Select `sine` on the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") in the tutorial patch.


When a steady signal is applied to [scope~](https://docs.cycling74.com/reference/scope~/ "scope~"), what you see depends on the relationship between the frequency, sampling rate, `calccount` and `buffer size`. `Buffer size` should be as high as possible, so set it to the width of the object up to the maximun of 256. In general, the lower `calccount` is, the more detail is shown, (it is effectively downsampling the waveform) so it's usually best to start at 2. Use more for very low frequency, but 16 will get you down to 10 Hz.
Chances are a steady waveform won't look too steady—it will drift across the display. (OK, it will probably whizz across the display!) The solution to this problem is the `trigger` attribute, which defaults to `0:off` but should usually be set to `1:up`. This will lock the display to a certain value in the waveform: `triglevel`. If triggering is on, the [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") object will wait for the wave to cross the `triglevel` in the indicated direction before if begins a new display cycle. Thus a simple waveform will usualy show nice and steady. With a complex waveform, `triglevel` may need some adjustment for best results.
  * Choose triangle in the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu").
  * Use the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object to set `trigger` to `up`.
  * Use the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") object to adjust `triglevel`.


Note how the wave slides back and forth as `triglevel` is changed from -1 to 1.
### Showing Oscillograms
  * Connect a music signal to your audio interface and select `input` on the umenu in the tutorial patch.


Sometimes we want to look at the long term behavior of a signal. This is akin to turning the sweep rate of a hardware oscilloscope way down. You see the envelope of the signal rather than the individual waves. The equivalant setting on [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") is a high value of `calccount`. 128 would be a good start. The first thing you will notice is the display takes forever to update. How long? Well, the number of samples needed to fill the dissplay is `calccount` * `buffer size`, so divide this by the sampling rate to get the numebr of seconds between updates. With a `calccount` of 128 and `buffer size` 256, the update time comes out 0.75 seconds. The same math will help estimate the `calccount` appropriate to showing a complete waveform—you want the calculation to match the period of the wave: one over the frequency.
### What do the gridlines mean?
The [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") is divided into a grid by horizontal and vertical lines. The center horizontal line marks the zero point. The other horizontals are simply halfway to the edges. The values at the top and bottom are set by the `range` attribute, which defaults to ±1.0. The meaning of the vertical lines depends on `calccount` and `buffer size`. As mentioned above, the product of these divided by the sample rate determine the _display period_. The vertical lines divide this by 8. So if `calccount` is 2 and `buffer size` 256, the _display period_ will be 0.0116 at 44.1 kHz. The inverse of this gives the frequency of a waveform that would exactly fill the window, so 86.1 Hz should just fit. The time interval represented by the vertical lines is about 1.5 ms.
### X-Y Display
  * Connect a stereo music signal to your audio interface and open the X-Y subpatch.


If you connect an audio signal to the right inlet of [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") that signal will be used to determine the X location (left to right) of each point. If the same signal is connected to left and right, you get a diagonal line from lower left to upper right. If the signal in the right is an out of phase version of the left, the line slants the other way. When a stereo signal is connected, the result is sort of a scribble, and you can estimate the phase difference of left and right by the width and slope of the shape.
If you connect geometric waveforms to both inlets of [scope~](https://docs.cycling74.com/reference/scope~/ "scope~"), you can generate some interesting evolving shapes. These shapes are called Lissajous figures, and are worth some exploration in themselves. The [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") help file has some examples.
## New School: [jit.catch~](https://docs.cycling74.com/reference/jit.catch~ "jit.catch~") and [jit.graph](https://docs.cycling74.com/reference/jit.graph "jit.graph")
We can also display waveforms in Jitter with the [jit.catch~](https://docs.cycling74.com/reference/jit.catch~ "jit.catch~") and [jit.plot](https://docs.cycling74.com/reference/jit.plot "jit.plot") objects. [Jit.catch~](https://docs.cycling74.com/reference/Jit.catch~ "Jit.catch~") takes samples from an audio signal and packs them into a one dimensional matrix. The number of samples per matrix is set by the `framesize` attribute, and has exactly the same meaning as the `calccount` * `buffer size` calculation in [scope~](https://docs.cycling74.com/reference/scope~/ "scope~"). [Jit.catch~](https://docs.cycling74.com/reference/Jit.catch~ "Jit.catch~") has several operation modes, but the one we are interested is `mode 3`, which is triggered in an oscilloscope-like way. Of course [jit.catch~](https://docs.cycling74.com/reference/jit.catch~ "jit.catch~") requires a series of bangs to prompt the output of matrices.
[Jit.graph](https://docs.cycling74.com/reference/Jit.graph "Jit.graph") displays data in one dimensional matrices in a two dimension array of char. Connect that between [jit.catch~](https://docs.cycling74.com/reference/jit.catch~ "jit.catch~") and a [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"), and you have a waveform display. Jit.graph also has modes, which determine the style of display:
0: Points 1: Lines 2: Area 3: Bi-polar area 4: bars
Lines is the most scope-like.
The threshold feature in jit.catch~ is a bit odd in that the threshold point is always placed in the `middle` of the matrix. Thus, if you adjust `framesize`, the waveform will remain centered in the display. That also means that the trigger direction (`trigdir`) has to be set in the down (1) mode to match what [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") does with the same wave. The display can be further altered with the `rangelo` and `rangehi` attributes which set the values that hit the bottom or top of the display. There is also a height attribute, which sets the vertical dimension of the matrix. This should be set to match the height of the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") to avoid size conversion artifacts.
The choice between using [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") or Jitter to display audio depends on what you want to do. If an audio display is needed in the patch, [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") is usually the best choice. If you want to process the image further à la iTunes, Jitter is the way to go.
## Plotting a spectrum
Two popular buzzwords in the DSP community are _time domain_ and _frequency domain_. _Time domain_ simply means we are graphing how signal values change over time, as we have shown above. The _frequency domain_ shows audio at one moment in time, but shows the Fourier frequency content. Thus the graph (called a _spectrogram_) has frequency across the bottom. You will remember the Fourier theorm states that any waveform can be deconstructed into a sum of sine waves. A spectrogram plots the amplitude of those sine waves. We will go into detail in _[Analysis Chapter 4: Simple Fourier Analysis](https://docs.cycling74.com/learn/articles/14_analysischapter04/)_. Here we will just explore a simple way to display a spectrogram.
### Spectrogram
  * Select `triangle` in the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") and set the frequency to 440 Hz


The [spectroscope~](https://docs.cycling74.com/reference/spectroscope~/ "spectroscope~") object displays a lovely spectrogram right out of the box. The peaks in the trace show the frequency and amplitude of the partials in the triangle waveform. In an ideal system, these peaks would be thin lines, but the algorithm required to show a spectrum in real time produces "skirts" at the bottom of the peaks. The main attribute to be aware of is the frequency axis scaling, which is chosen by the `logfreq` attribute and shown as `Display Frequency Axis Scale` in the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui"). In _linear mode_ the entire audible range of 20-22 kHz is evenly spaced left to right. The spectroscope~ display should show a nice set of evenly spaced harmonics. It's actually every other harmonic, as you can see by selecting `rectangle`. If you choose `input` most of the action will be crowded into the left side. That's because music is mostly confined to a fairly low range of frequencies.
  * Select `Display frequency axis scale` in the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") attached to the [spectroscope~](https://docs.cycling74.com/reference/spectroscope~/ "spectroscope~") object and choose `Logarithmic Scale`.
  * Select `sine` in the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu") and set the frequency to 43 Hz.


In logarithmic mode, _octaves_ are evenly spaced across the display. The display should show a wide peak about a third of the way in. (Ignore what is to the left of the peak—the display resolution is only 43 Hz, so anything below that is garbage.) Now change the frequency to 86 Hz and note how the peak moves. As you step up octaves: 129, 172, 215, etc., the peak will move an equal amount. The peak will get narrower, too. The 43 Hz band of resolution is less of the total as we move up. Now select `input`. The music fills the display nicely.
Both modes of display are very useful: Linear mode shows the harmonic structure of steady waveforms and logarithmic mode shows the tonal balance of music in an intuitive way.
### Sonogram
We can get both time domain and frequency domain information in one display by choosing sonogram mode.
  * Select `Display mode` in the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") and choose `Sonogram`.
  * Select `input` in the [umenu](https://docs.cycling74.com/reference/umenu/ "umenu").


You should now see an image drawn with streaks of black, grey, and white. A sonogram is a two dimensional plot showing time across the bottom and frequency from bottom to top. The amplitude at each point is represented by the darkness of the color. As you listen to the music you will see how the low notes and high notes show up and even see the harmonic structure of the sound. (The `logfreq` mode affects sonograms also.) For an extra special treat, select `sonogram color` in the [attrui](https://docs.cycling74.com/reference/attrui/ "attrui") and choose `color`. Now the intensity of the frequency components show as red fading through yellow and green to purple.
The [spectroscope~](https://docs.cycling74.com/reference/spectroscope~/ "spectroscope~") object can be customized in varioius ways, including vertical orientation, drawing or scrolling mode, reverse direction, and colors. You can also restrict the range to display to get more detail in a small speace.
## Summary
The [scope~](https://docs.cycling74.com/reference/scope~/ "scope~") object gives an oscilloscope view of a signal, graphing amplitude over time. Waveforms can also be displayed in the Jitter matrix format by [jit.catch~](https://docs.cycling74.com/reference/jit.catch~ "jit.catch~") and [jit.graph](https://docs.cycling74.com/reference/jit.graph "jit.graph"). The [spectroscope~](https://docs.cycling74.com/reference/spectroscope~/ "spectroscope~") object can display frequency content as either a dynamic spectrogram or as a moving sonogram.
## See Also
  * [scope~ - Signal oscilloscope](https://docs.cycling74.com/reference/scope~/)
  * [jit.catch~ - Convert audio signal to jitter matrix](https://docs.cycling74.com/reference/jit.catch~)
  * [jit.graph - Display values in one dimensional matrix in two dimensions](https://docs.cycling74.com/reference/jit.graph)
  * [spectroscope~ - Display frequency content of audio signal](https://docs.cycling74.com/reference/spectroscope~/)



Kind
    Tutorial 

Categories
    Audio     Analysis 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
