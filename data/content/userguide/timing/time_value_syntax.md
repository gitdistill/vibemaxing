---
description: Max uses a special syntax to define units of time that are relative to given time signature
group: Timing
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/time_value_syntax/
title: Time Value Syntax
---

# Time Value Syntax
Most Max objects that deal with timed events, like [metro](https://docs.cycling74.com/reference/metro/ "metro"), [phasor~](https://docs.cycling74.com/reference/phasor~/ "phasor~"), and [pipe](https://docs.cycling74.com/reference/pipe/ "pipe"), can represent time in multiple ways. In general these fall into two categories: **Fixed** time values and **Tempo-relative** time values. Fixed values express time in milliseconds or some other absolute units. Tempo-relative values depend on the current tempo and time signature, as set by a [transport](https://docs.cycling74.com/reference/transport/ "transport") object (or the **Global Transport**).
## Fixed Time Values
![Some objects using Fixed time values](https://docs.cycling74.com/images/703e2f1af55fc4a37ee32dce625732f1_382.webp) Some objects using Fixed time values Unit | Format | Example | Notes  
---|---|---|---  
milliseconds |  `ms` suffix | `100 ms` | The default for objects like [metro](https://docs.cycling74.com/reference/metro/ "metro")  
hours/minutes/seconds |  `:` between each number | `01:03:45.250` | 1 hour, 3 minutes, 45 seconds, and 250 milliseconds. The millisecond value after the decimal is optional.  
hours/minutes/seconds | list of 3 or 4 numbers, followed by `hh:mm:ss` | `1 3 45 250 hh:mm:ss` | An equivalent option for representing time in terms of hours/minutes/seconds/milliseconds  
samples |  `samples` suffix | `1000 samples` | The actual duration will depend on the sample rate  
frequency |  `hz` suffix | `5 hz` | The inverse of milliseconds, so `2 hz` is equivalent to `500 ms`.  
## Tempo-relative Time Values
![Some objects using Tempo-relative time values](https://docs.cycling74.com/images/d6247cd57be6265120a8ddc07045e403_370.webp) Some objects using Tempo-relative time values
All Tempo-relative Time Values can be expressed in terms of **ticks** , where one tick is 1/4801/4801/480 of a quarter note (equivalently, there are 480 ticks in one quarter note).
Unit | Format | Example | Notes  
---|---|---|---  
ticks |  `ticks` suffix | `100 ticks` | In places where only tempo-relative time values are allowed, such as the `@quantize` attribute of the [metro](https://docs.cycling74.com/reference/metro/ "metro") object, values in ticks can be specified as a single number. In places where both fixed and tempo-relative units are accepted, such as the `@interval` attribute of a [metro](https://docs.cycling74.com/reference/metro/ "metro") object, a value in ticks must be followed by `ticks` to be interpreted as ticks instead of milliseconds.  
note values | see "Note Values" table | `4nt` | Symbols that abbreviate musical note time values—see the table below for recognized values.  
bars/beats/units |  `.` between each number | `2.4.240` | 2 bars, 4 beats, 240 ticks. When you need to use a single value, bars/beats/units can be separated by periods.  
bars/beats/units | three numbers | `2 4 240` | When you can pass a list of values, bars/beats/units can be specified by separate numbers like this. When an object will accept Fixed or Tempo-relative time values, you can add `bbu` to make sure the list is understood as bars/beats/units and not hours/minutes/seconds.  
## Note Values in Ticks
Note | Ticks | Interpretation  
---|---|---  
1nd | 2880 ticks | Dotted whole note  
1n | 1920 ticks | Whole note  
1nt | 1280 ticks | Whole note triplet  
2nd | 1440 ticks | Dotted half note  
2n | 960 ticks | Half note  
2nt | 640 ticks | Half note triplet  
4nd | 720 ticks | Dotted quarter note  
4n | 480 ticks | Quarter note  
4nt | 320 ticks | Quarter note triplet  
8nd | 360 ticks | Dotted eighth note  
8n | 240 ticks | Eighth note  
8nt | 160 ticks | Eighth note triplet  
16nd | 180 ticks | Dotted sixteenth note  
16n | 120 ticks | Sixteenth note  
16nt | 80 ticks | Sixteenth note triplet  
32nd | 90 ticks | Dotted thirty-second note  
32n | 60 ticks | thirty-second note  
32nt | 40 ticks | thirty-second-note triplet  
64nd | 45 ticks | Dotted sixty-fourth note  
64n | 30 ticks | Sixty-fourth note  
128n | 15 ticks | One-hundred-twenty-eighth note  
## Positions vs Intervals
Some objects will interpret a Tempo-relative value in bars/beats/units as a _position_ , while others will interpret the same value as an _interval_. For example, the [timepoint](https://docs.cycling74.com/reference/timepoint/ "timepoint") object fires an event at a point in time, and would interpret the bars/beats/units value `1 1 0 bbu` as a point in time on the first beat of the first measure—in other words at time zero. Attributes like the `@quantize` attribute of [metro](https://docs.cycling74.com/reference/metro/ "metro") on the other hand wil interpret the same value `1 1 0 bbu` as an _interval_ of one bar and one beat, or 5 beats in 4/44/44/4 time (interval, quantization, and delay attributes of objects are generally time intervals).
The [translate](https://docs.cycling74.com/reference/translate/ "translate") object has a `@mode` attribute that can convert time units as either intervals or positions.
