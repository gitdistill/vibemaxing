---
description: Common conversions in Max, organized into a quick-reference cheat sheet
group: Patching
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/conversion/
title: Conversion Cheat Sheet
---

# Conversion Cheat Sheet
## Message to Audio
![](https://docs.cycling74.com/images/76b7e1c41581beb4d2e306f139692300_67.webp)
Convert a message to a signal without any smoothing
![](https://docs.cycling74.com/images/a2a124877825036e4330b3b42c65e46c_65.webp)
Convert a message to a signal with linear smoothing
![](https://docs.cycling74.com/images/e45e0e999e7bb020fe275e54570ec4d0_113.webp)
Convert a message to a signal with logarithmic smoothing
## Audio to Message
![](https://docs.cycling74.com/images/1babc25ec88397fc1c170741ce566a1a_95.webp)
Convert audio to a stream of messages
![](https://docs.cycling74.com/images/e218f808ba68b9f90ed93d909f227c2c_380.webp)
Analyze an audio stream for peaks, average, or RMS
## Signal to Event
![](https://docs.cycling74.com/images/d63274f82625b9f8b9ec1953dc15c8ac_156.webp)
Signal to Event
## Unit Conversions
![](https://docs.cycling74.com/images/a227525c3c9b70ac34ff1c2c8c3aca0f_179.webp)
Samples to Milliseconds
![](https://docs.cycling74.com/images/877445d1c9e1f5e330c8fb58082dbb8f_184.webp)
Frequency to MIDI Pitch
![](https://docs.cycling74.com/images/6fad1ffb784b1302b83605eea4ca7b35_212.webp)
Amplitude to Decibel
![](https://docs.cycling74.com/images/571a37a6906a6823313746e5b88df195_152.webp)
Note Value to Millisecond
See [Time Value Syntax](https://docs.cycling74.com/userguide/time_value_syntax/) for more details.
![](https://docs.cycling74.com/images/8c5f80dbf00b586ab3d02d562414d051_100.webp)
Tempo to Millisecond
This same patch will convert milliseconds to tempo (kinda cool huh?)
![](https://docs.cycling74.com/images/132bb61bc8dd060f7bf3554ce1d66421_222.webp)
Linear to Quadratic
## Multichannel
![](https://docs.cycling74.com/images/b471a9d7944064adef7facf9fb55ef42_180.webp)
Single channel to multichannel
![](https://docs.cycling74.com/images/1c8ab34b8cadc1da320a7504052119b7_155.webp)
Multichannel to separate channels
![](https://docs.cycling74.com/images/0620dd7b7393eadd41340777c9e744b8_259.webp)
Multichannel to stereo mixdown
## List to buffer~
![](https://docs.cycling74.com/images/dc5a8afc953e1fd319928d794a53ae4f_163.webp)
Fill using peek~
![](https://docs.cycling74.com/images/dac31e5d58e8a6f20e62b4d96f4e6c66_190.webp)
Fill using jit.buffer~
## buffer~ to List
![](https://docs.cycling74.com/images/e5a5106580a3d9c71bccce1e3303b65b_183.webp)
Using peek~ and zl.group
![](https://docs.cycling74.com/images/24587cea5167177b5b006b6bb4ac5b66_167.webp)
Using jit.buffer~ and jit.spill
## Audio to Matrix
![](https://docs.cycling74.com/images/e72679e412437363bd3b7a8cd69f18f6_191.webp)
Filling up a matrix
![](https://docs.cycling74.com/images/263ca220e2919c93a873ad19f6cfde87_379.webp)
Reading from a buffer
![](https://docs.cycling74.com/images/0c697e4ea1e27578e1071cffb59b2d48_394.webp)
Writing into a matrix
## Matrix to Audio
![](https://docs.cycling74.com/images/71e9d6e2613ff71c5b66553686de44ac_478.webp)
Scanning a matrix
![](https://docs.cycling74.com/images/bebdce933967428a0945e449e8424f85_228.webp)
Read a video as an audio signal
## Matrix to Texture
![](https://docs.cycling74.com/images/40b53946645575616bf28e4fb9bc8df1_160.webp)
Convert a matrix to a texture. It really is that simple.
## Texture to Matrix
![](https://docs.cycling74.com/images/f55661dc653a5416f02bb10fec83f2f2_372.webp)
Convert a texture to a matrix
## Matrix to Messages
![](https://docs.cycling74.com/images/d5a419b293c0181562aa34ab531a2b6a_312.webp)
Get cell values from a matrix as a list
![](https://docs.cycling74.com/images/7209b6d10e8ea3082af19295eed5dd87_208.webp)
Read a specific cell from a matrix
![](https://docs.cycling74.com/images/e2fdc9b4856a1bba7756926d40ecb95a_692.webp)
Get a representative number from a matrix
![](https://docs.cycling74.com/images/3a90b1e88c36fbf9aca7419f1da9b022_235.webp)
Output the cells of a matrix one by one
## Message to Matrix
![](https://docs.cycling74.com/images/7b30bd4e4cd3ee20caeaa7d008b6bbd2_272.webp)
Fill up a matrix using a list
![](https://docs.cycling74.com/images/46892dc346e4561acb14de117f4d05d8_151.webp)
Set a single cell in a matrix
## Matrix Upsampling/Downsampling
![](https://docs.cycling74.com/images/96b0eac29bf40a85244ab455723d317f_203.webp)
Downsample a matrix, no interpolation
![](https://docs.cycling74.com/images/cd7bdd1734d73f1a99f5874c6aeb8a37_217.webp)
Upsample a matrix with interpolation
## Matrix Color Conversion
![](https://docs.cycling74.com/images/0886163a0c60d7180772202de4789005_141.webp)
Red-Green-Blue to Hue-Saturation-Lightness
![](https://docs.cycling74.com/images/9d987a2a2ffc1a66c3b7a8d321b823c0_83.webp)
Red-Green-Blue to Luminance
![](https://docs.cycling74.com/images/b3886a6fc2307f588bad6152068ab8f4_180.webp)
More color space conversions
## Thread Priority Conversion
![](https://docs.cycling74.com/images/02b58b2495705feed752a3e846ed5552_119.webp)
Move a high-priority message to the low priority queue
![](https://docs.cycling74.com/images/83d2be8a827e4021530e5940806b66e2_105.webp)
Move a low-priority message to the high-priority scheduler
Note that this won't make the message get processed "sooner", but if you know what you're doing there may be situations where it's useful.
## Dictionaries
![](https://docs.cycling74.com/images/e1adb7a127705578bdf37b858a9a23a8_200.webp)
Convert a dictionary to a coll
![](https://docs.cycling74.com/images/e6781c25cea495330ae8c64953471dbb_275.webp)
Convert a coll to a dictionary
![](https://docs.cycling74.com/images/a5dabd7e7fc2546d98548ba5e127b6db_336.webp)
Add an array to a dictionary
## Number Formats
![](https://docs.cycling74.com/images/47494fb81767f30fe51a5ea021c57dff_111.webp)
Decimal to Hex
![](https://docs.cycling74.com/images/d3270fbb5356ea7c9733c995e9ba25ac_107.webp)
Hex to Decimal
![](https://docs.cycling74.com/images/1517d65cb4fedc31364a50a417c5dc42_227.webp)
Decimal to Binary
![](https://docs.cycling74.com/images/15c1bc9928a3355505415ecd47f941e5_138.webp)
Binary to Decimal
## String to Array
![](https://docs.cycling74.com/images/aa9123f400302906ae1aa79c9904dfc2_505.webp)
String to Array
## Array to String
![](https://docs.cycling74.com/images/273a37d1c40b21aad3156176da23ac0e_506.webp)
Array to String
## buffer~ to Array
![](https://docs.cycling74.com/images/9160a7ad18e5756cf33de6148993fddb_385.webp)
buffer~ to Array
## Array to buffer~
![](https://docs.cycling74.com/images/ff8d51a068996289445d64021ff0e7a9_264.webp)
Array to buffer~ using array.tobuffer
## Array to buffer~ (multiple channels)
![](https://docs.cycling74.com/images/915efa6bfc45a63b43107bddcc74e3b3_679.webp)
Each nested array is its own channel
