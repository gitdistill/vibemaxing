---
description: Using standard serial devices
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/communicationschapter02/
title: Serial Communication
---

Download Series Content and Patchers
# Communications Tutorial 2: Serial Communication
## Introduction
This tutorial covers the the topic of using _serial_ communication within Max. Any number of external devices use a serial protocol (e.g. RS-232, Bluetooth) to communicate with a computer, and serial streams can even be used for low-bandwidth communication between computers (think dial-up Internet!). Devices such as professional-level video mixers, DVD players, and theatrical lighting systems use serial interfaces to receive commands, and microcontroller systems used by the physical computing community rely on serial communication to transmit sensor data back to a computer.
For this tutorial we'll be using the example of serial communication with a very popular electronics prototyping platform called the _[Arduino](http://www.arduino.cc)_. It consists of a small microcontroller mounted on a prototyping board that is programmed by a C-like language. It can communicate back to a host computer using a serial line over USB. Even if you don't have an Arduino, the principles shown in this tutorial should give you enough insight to communicate with any serial device you need.
## The Arduino Code
Before we look at the Max patcher, below is the code that we've used for programming our Arduino in this tutorial. In this example, the Arduino doesn't read any sensor data or do anything particularly fancy: it just waits for _any_ input from the computer, then begins to stream a serial feed of numbers back. The code for the Arduino is here:
```
// Arduino Serial Tester
// rld, cycling'74, 3.2008

long randomvalue = 0; // random value
long countervalue = 0; // counter value
int serialvalue; // value for serial input
int started = 0; // flag for whether we've received serial yet

void setup()
{
  Serial.begin(9600); // open the arduino serial port
}

void loop()
{
  if(Serial.available()) // check to see if there's serial data in the buffer
  {
    serialvalue = Serial.read(); // read a byte of serial data
    started = 1; // set the started flag to on
  }

  if(started) // loop once serial data has been received
  {
    randomvalue = random(1000); // pick a new random number
    Serial.print(countervalue); // print the counter
    Serial.print(" "); // print a space
    Serial.print(randomvalue); // print the random value
    Serial.print(" "); // print a space
    Serial.print(serialvalue); // echo the received serial value
    Serial.println(); // print a line-feed
    countervalue = (countervalue+1)%1000; // increment the counter
    delay(100); // pause
  }
}

```

Even if the specifics of the Arduino programming language are not familiar, you can look at the comments for each line and see what's happening. The microcontroller initializes itself and opens up a serial port running at `9600`_baud_ - this is the speed at which it will communicate with our Max patcher. It then enters a loop in which it checks to see if we've sent it any data and, once we do, starts streaming numbers back to the computer. It generates a number that _counts_ from `0` to `1000` over and over again, a _random_ number (in the same range), and an _echo_ of the last value we've sent into the chip. These three values are printed (as if on a terminal) over the serial line.
## Looking at the [serial](https://docs.cycling74.com/reference/serial/ "serial") object
Take a look at the tutorial. It consists of a [serial](https://docs.cycling74.com/reference/serial/ "serial") object at the top with some supporting logic at the output that eventually drives an [lcd](https://docs.cycling74.com/reference/lcd/ "lcd") graph of the data coming from the Arduino. The Max [serial](https://docs.cycling74.com/reference/serial/ "serial") object is used for communication with serial devices that don't have special drivers that put them in another category (e.g. MIDI or HID). These generic devices communicate with Max over a serial _port_ , which is specified as the first argument to the object. In Max these ports are _lettered_ (`a`, `b`, etc.). Click on the `print`[message](https://docs.cycling74.com/reference/message/ "message") box at the top of the patcher: the available serial ports on your computer will appear in the Max Console, along with their letter mappings. The Arduino should appear there, along with any other serial devices you may have. If necessary, you can change the letter argument to the [serial](https://docs.cycling74.com/reference/serial/ "serial") object by unlocking the patcher and retyping the object.
In addition to the serial port, the [serial](https://docs.cycling74.com/reference/serial/ "serial") object takes a number of additional arguments to set up the communications _protocol_. The second argument of the object sets the _baud rate_ , and needs to match that of the Arduino we're using. Since we've told the Arduino to transmit data at `9600` baud, we put the same argument to our [serial](https://docs.cycling74.com/reference/serial/ "serial") object. Additional arguments to the object allow us to specify the number of _data bits_ , _stop bits_ , and the _parity_ (even or odd) of the device we're talking to. Since the Arduino is a fairly typical device, the default settings will work.
## Transmitting and polling data
The [serial](https://docs.cycling74.com/reference/serial/ "serial") object can both _transmit_ and _receive_ serial data. It transmits data by taking a _byte_ (an integer in the range of `0` - `255`) in its inlet and sending it over the selected serial port. These bytes can represent command values or can be translated into ASCII (the same numbers output from the [key](https://docs.cycling74.com/reference/key/ "key") object). In order to receive data, the [serial](https://docs.cycling74.com/reference/serial/ "serial") object must be _polled_ (just like [mousestate](https://docs.cycling74.com/reference/mousestate/ "mousestate")) - when a `bang` is received by the object, it empties its internal buffer of any waiting serial messages and sends them sequentially (as bytes) out its outlet.
Assuming that our Arduino is loaded with our program (above) and connected to the computer, we should be able to talk to it provided the [serial](https://docs.cycling74.com/reference/serial/ "serial") object is set to the correct port. Turn on the [metro](https://docs.cycling74.com/reference/metro/ "metro") object with the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box. As you can see from the [number](https://docs.cycling74.com/reference/number/ "number") box attached to the object, nothing will happen. This is because, in our Arduino code, we _wait_ for the computer to communicate with the microcontroller first.
Type the number `10` into the [number](https://docs.cycling74.com/reference/number/ "number") box attached to the [serial](https://docs.cycling74.com/reference/serial/ "serial") object and hit return. Assuming the [serial](https://docs.cycling74.com/reference/serial/ "serial") object transmitted the byte correctly, you should see numbers begin to appear out of the object. Turn on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") labeled **1** to print the "raw" serial data in the Max Console.
## Formatting the data
You'll notice that the numbers appearing in the Max Console from the "raw" serial output don't seem to make much sense. This is because the Arduino is transmitting its values as ASCII, as if they were typed on a computer. Thus, the number `15` is represented as ASCII value `49` ("1") followed by ASCII value `53` ("5"). Spaces between our three values are represented by the ASCII for a space (`32`), and each set of three numbers is terminated by a carriage return and a line feed (ASCII `13` followed by `10`). To use these values in Max, we need to first _group_ them together and then _convert_ them from ASCII into a human-readable string.
Uncheck the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") labeled **1** and check the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") labeled **2**. This prints out the output of the [zl](https://docs.cycling74.com/reference/zl/ "zl")`group` object in the patcher. The [zl](https://docs.cycling74.com/reference/zl/ "zl") object is taking sequences of these ASCII values and grouping them into a _list_ ; the [select](https://docs.cycling74.com/reference/select/ "select") object above the [zl](https://docs.cycling74.com/reference/zl/ "zl") forces the list to be output (and cleared) whenever a `13` (carriage return) is received. In addition, it eliminates line-feed (ASCII `10`) characters from the stream. Since the right outlet of [select](https://docs.cycling74.com/reference/select/ "select") outputs anything not selected by the object, the rest of the values pour into the [zl](https://docs.cycling74.com/reference/zl/ "zl"). As a result, the Max Console will show a list of ASCII values that should represent three numbers separated by spaces (ASCII `32`).
Uncheck the **2**[toggle](https://docs.cycling74.com/reference/toggle/ "toggle") and turn on the **3**[toggle](https://docs.cycling74.com/reference/toggle/ "toggle"). This shows the output from the [itoa](https://docs.cycling74.com/reference/itoa/ "itoa") object, which takes the grouped list and converts the integers into their relevant ASCII characters. As a result, the Max Console should show something that finally makes sense given our Arduino code: we should see a value counting from `0` to `1000` followed by a random value followed by `10` (the byte we _sent_ to the microcontroller earlier).
The [itoa](https://docs.cycling74.com/reference/itoa/ "itoa") object creates a Max _symbol_ , which is readable by us for the purposes of debugging, but not quite what we need for our patcher. While we recognize that the message is a list of three integers, objects like [unpack](https://docs.cycling74.com/reference/unpack/ "unpack") will not. The [fromsymbol](https://docs.cycling74.com/reference/fromsymbol/ "fromsymbol") object _parses_ a symbol, separating different types of data based on white-space; as a result, our symbol becomes converted into a list of three integers, which the [unpack](https://docs.cycling74.com/reference/unpack/ "unpack") object can split apart. Note that the [number](https://docs.cycling74.com/reference/number/ "number") boxes out of the [unpack](https://docs.cycling74.com/reference/unpack/ "unpack") correctly show our values. Change the [number](https://docs.cycling74.com/reference/number/ "number") box at the top again, and you will see that the third value out of the [serial](https://docs.cycling74.com/reference/serial/ "serial") object will update accordingly.
Take a look at the drawing part of the patcher and see how it works. Like many of our [lcd](https://docs.cycling74.com/reference/lcd/ "lcd") -based examples, it simply visualizes the [serial](https://docs.cycling74.com/reference/serial/ "serial") object's output, in this case making a graph based on the counter (x), random value (y), and echoed byte (color). These values could easily be applied to control whatever you like.
## Summary
The Max [serial](https://docs.cycling74.com/reference/serial/ "serial") object provides the capability to communicate to and from standard serial devices within Max. It transmits and receives data as single bytes; objects such as [zl](https://docs.cycling74.com/reference/zl/ "zl"), [itoa](https://docs.cycling74.com/reference/itoa/ "itoa"), and [fromsymbol](https://docs.cycling74.com/reference/fromsymbol/ "fromsymbol") can be used to make sense of it all.
## See Also
  * [serial - Send and receive characters from serial ports and cards](https://docs.cycling74.com/reference/serial/)
  * [itoa - Convert integers to ASCII characters](https://docs.cycling74.com/reference/itoa/)
  * [fromsymbol - Transform a symbol into individual numbers/messages](https://docs.cycling74.com/reference/fromsymbol/)



Kind
    Tutorial 

Category
    Communication 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
