---
description: The Jitter Matrix, Part 1
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter00g_jitter-matrix-1/
title: Jitter Matrix Exploration - Part 1
---

Download Series Content and Patchers
# Video and Graphics Tutorial 5: Jitter Matrix Exploration Part 1
## Intro
The Jitter Matrix is at the core of most of the visual processes you will use in Max - video is a grid of color data, and OpenGL geometry can are represented by a grid of points in space (x,y,z). They're both represented using the same kinds of matrices - understanding how to inspect, set, manipulate, and display that matrix information will open up countless doors.
## Setup
For this chapter, we’ll be working with pre-built patchers.
  * Open `jitter_core_-_5_-_Jitter_Matrix_Exploration_1.maxpat`


## Planes of a Matrix
We already know how to load and playback video - and now, we’ll look under the hood at what video is _made of_. Open up the example patch and take a look at the first section. 
![](https://docs.cycling74.com/images/e23793f6eae79b022d33d4c7a088bc8e_202.webp)
The [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") object is preloaded with an image of color bars. Video data is being sent out to a [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") as a matrix. We’re also sending that same matrix to a [jit.unpack](https://docs.cycling74.com/reference/jit.unpack "jit.unpack") object, a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object, and a [print](https://docs.cycling74.com/reference/print/ "print") object.
Video in jitter is composed of a 4-plane matrix - each of the four individual plane contains data on Alpha, Red, Green and Blue values, in that order. The [jit.unpack](https://docs.cycling74.com/reference/jit.unpack "jit.unpack") object breaks this apart and displays each plane separately as a grayscale image. (The argument to [jit.unpack](https://docs.cycling74.com/reference/jit.unpack "jit.unpack") determines the number of outputs that the object will have). Brighter pixels indicate higher intensity of the corresponding color. If you aren’t familiar with additive color (RGB), it can seem unintuitive - it reflects how colors of light behave in the real world rather than how colors are mixed using pigments. Once we have unpacked our matrix, we are free to manipulate the individual planes in any way we want. In this case, we are swapping the red and green planes before we recombine them using the [jit.pack](https://docs.cycling74.com/reference/jit.pack "jit.pack") object (as with [jit.unpack](https://docs.cycling74.com/reference/jit.unpack "jit.unpack"), the argument to [jit.pack](https://docs.cycling74.com/reference/jit.pack "jit.pack") determines the number of _inlets/planes_ that the object will have). 
![](https://docs.cycling74.com/images/fd8b57eb81c990020d154c7e25426759_431.webp)
On the right side of the patch, we use the `planemap` message to a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") to achieve the same result. When the [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object receives a `jit_matrix` message, it automatically fills with the values of the incoming matrix. The `planemap` message determines the order in which the data from the incoming matrix is used to fill the planes of the jit.matrix. Click on the various maps to see how they affect the image. The default is `planemap 0 1 2 3`, and tells the matrix to use plane 0 (alpha) from the incoming matrix as plane 0, 1 (red) as 1 and so on, resulting in an unaltered image. Switching the order of these planes, however, allows you to quickly substitute the values of one plane for another (i.e., `planemap 0 2 1 3`) or even one for multiple (i.e., `planemap 0 1 1 3`).
![](https://docs.cycling74.com/images/a79840b168968f572251d88994528c59_318.webp)
Instead of outputting an enormous list of values for every pixel (cell) in a matrix, jitter objects communicate using the `jit_matrix` message. Look at the [print](https://docs.cycling74.com/reference/print/ "print") object below the [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") and note that the message sent out by our movie object is `jit_matrix` followed by some numbers and letters. This message acts as an alias to the data contained in a matrix. You can also explicitly set the name of a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") using and argument (e.g. **jit.matrix mydata**) and access that data anywhere in a patch (for an in-depth discussion of matrix data, read the document). 
## The [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object
Video media automatically sets the state of all four planes of a matrix based on the data contained in the current video frame, but sometimes we will want to work with matrix data without using pre-recorded media. The [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object provides us with a blank slate to create whatever type of matrix we want.
The next section shows how we can set the value of any point in a matrix using the `setcell` message or all values at once using the `setall` message. 
  * Open `jitter_core_-_5_-_Jitter_Matrix_Exploration_2.maxpat`


In the example on the left, **jit.matrix 1 char 4 4** creates a one-plane matrix containing 16 pixels (4 rows and 4 columns).
![](https://docs.cycling74.com/images/7290a27e8dba2e697f5700c23d0d109c_131.webp)
The fact that the matrix has only one plane means it uses only one value per cell - creating a grayscale image. The value is _char data_ - integer values from 0-255, where 0 is solid black and 255 is solid white. Each pixel or cell in our matrix is addressed using x and y Cartesian coordinates, where the top left pixel is represented as cell 0 0. To manipulate your matrix, select x and y cells from 0-3 and then adjust the value. This composes a message in the format `setcell <x> <y> val <int>`.
Note that setting the contents of the matrix does not output the matrix. It is only output when it receives a `bang` message which we create here by using the [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object. 
![](https://docs.cycling74.com/images/8f7ef1cda0de03d10d259e1145eccb47_203.webp)
The right-hand example uses a 4-plane matrix that lets us to set ARGB (alpha, red, green, blue) data such as we find in video pixels. A [swatch](https://docs.cycling74.com/reference/swatch/ "swatch") object (whose _compatibility_ attribute is set to 1, which means that the object outputs integers between 0 - 255 istead of float values from 0. - 1.) is used to quickly set the RGB values.
![](https://docs.cycling74.com/images/9204600b3d8babbf98ee3b6449906e61_457.webp)
## Displaying the contents of a matrix
The [jit.cellblock](https://docs.cycling74.com/reference/jit.cellblock "jit.cellblock") object gives us a way to view the contents of our [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object. Notice that as you manipulate the values in your matrix, the changes are reflected in the cellblock display. When using multi-plane matrices with the [jit.cellblock](https://docs.cycling74.com/reference/jit.cellblock "jit.cellblock") object, the `plane` message allows you to specify which plane you are viewing the contents of. Sending a negative integer as the value allows you to see all at once.
![](https://docs.cycling74.com/images/bafd232c68e2c1bba3962e6f4e0b6612_595.webp)
The [jit.print](https://docs.cycling74.com/reference/jit.print "jit.print") object will print the incoming matrix values to the Max console, one row per line.
![](https://docs.cycling74.com/images/fdcd96f909d5a83e416b239274f6ca3e_163.webp)
Keep in mind that for many matrices, this is a lot of data for either [jit.print](https://docs.cycling74.com/reference/jit.print "jit.print") or [jit.cellblock](https://docs.cycling74.com/reference/jit.cellblock "jit.cellblock"). A full HD 1920x1080 video matrix would print 1080 lines with 1920 columns. At 4 values per cell, that's 8,294,400 values per frame! In many cases, viewing the data with a [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") is the quickest way to get a sense of the data. 

Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
