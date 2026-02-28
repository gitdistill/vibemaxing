---
description: The Jitter Matrix, Part 2
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter00h_jitter-matrix-2/
title: Jitter Matrix Exploration - Part 2
---

Download Series Content and Patchers
# Video and Graphics Tutorial 6: Jitter Matrix Exploration Part 2
## Intro
While being able to control individual cells in a matrix can be useful, there are a lot of other ways to fill a matrix with data. We’ll look at filling a matrix from a few other sources in this chapter. 
## Setup
  * Open `jitter_core_-_6_-_Jitter_Matrix_Exploration_1.maxpat`


## Filling a Matrix
This example uses the `setcell` message in combination with an [uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object to rapidly fill a matrix.
Lock the patch and double-click the **patcher fillmatrix** object to open up the subpatcher. When you click the button on the main patcher labeled _fill_ , it sends a `bang` message to the **uzi 12** object, causing it to rapidly send values from 1 - 12 out the right outlet. These values correspond to the y (row) values. Each time a row is selected, another [uzi](https://docs.cycling74.com/reference/uzi/ "uzi") object then sends a `bang` message to **uzi 16** object which in turn sends out numbers for each x position or column. The x and y values are used both to determine which cell is being set and to calculate a value for each cell based on the mathematical equation in the [expr](https://docs.cycling74.com/reference/expr/ "expr") object. The equation is relatively unimportant. It could be any formula that generates interesting data. In this case, we've chosen a formula that will produce a sinusoidal gradation of brightness in each column, and then cause the overall brightness of the columns to increase from left to right (i.e., as x increases). The important thing is that the method generates properly formatted `setcell` messages, with x and y coordinates and a valid value (0-255) for each cell. 
![](https://docs.cycling74.com/images/292cf609d10b379ba517fa78a1d7cb26_220.webp) ![](https://docs.cycling74.com/images/177373de165906df405566af31b50feb_478.webp) The next method uses [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise"), a great way to generate random values for every cell in a matrix. Each time it receives a `bang` message, the [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") object creates a random matrix of the specified dimensions and plane count. The result is a totally random arrangement of pixels. ![](https://docs.cycling74.com/images/add418b2ed82b83978aca69899af3bb1_494.webp)
The third method uses a special object - [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr"). The [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr") object takes an input matrix and processes it based on the supplied expression. In the first example we are using [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") to supply the input matrix. Notice that the first set of expressions basically ignore the input values, only using the incoming matrix to determine the data type, plane count, and dimensions.
![](https://docs.cycling74.com/images/c7dc5b312b9b9f86754c62ad66a501aa_439.webp)
The second set uses the colorbars image and the _in[0]_ argument, which tells the object to use the value information for each cell of the incoming matrix (in this case, colorbars) as part of the calculation. For more on using [jit.expr](https://docs.cycling74.com/reference/jit.expr "jit.expr"), check out the [Demystifying Expressions in Jitter](https://cycling74.com/2010/03/08/demystifying-expressions-in-jitter/) tutorial.
![](https://docs.cycling74.com/images/5c5cf41e6d8a8911be29c09429f10a68_490.webp)
## Copying Matrix Data - srcdim and destdim
When we send a `jitter_matrix` message to another Jitter object, we tell the object to look up the matrix data somewhere in memory. By default, this usually means we are copying the entire matrix and then processing it with the same constraints. A 320x240 matrix going out is still a 320x240 matrix when it comes into the next destination. We’re going to look now at how to copy specific portions of a source matrix into a specific region of a destination matrix.
  * Open `jitter_core_-_6_-_Jitter_Matrix_Exploration_2.maxpat`


Here we use the [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") attributes _usesrcdim_ and _dstdim_ to control how the matrix coming from [jit.movie](https://docs.cycling74.com/reference/jit.movie "jit.movie") is copied into the [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object.
![](https://docs.cycling74.com/images/0d8c43f65c5e5f63b9ed6e73d39fef33_398.webp)
As you explore the patch, switch between the colorbars and sunset images to get a better sense of how it works. Try enabling _usesrcdim_ then manipulating the _srcdimstart_ and _srcdimend_ attribute values to select a portion of the color bars image to copy over. Next, try enabling _usedstdim_ and adjusting the start and end points to determine where in the matrix the image will be displayed. As you adjust the values, you may notice portions of the previous image are left behind. You can remove them by using the `clear` message or by opening the [gate](https://docs.cycling74.com/reference/gate/ "gate") next to the "auto clear" bubble.
Finally, when you are using a different number of pixels from one matrix to the next (either more or less), you will usually see some distortion or pixelation. Enabling the on _interp_ attribute (i.e. **@interp 1**) will minimize this effect by interpolating or smoothing the data.
![](https://docs.cycling74.com/images/ecfc5fe498f5c4539cbc130449c1041d_675.webp)
## Explore Further
Open `jitter_core_-_6_-_Jitter_Matrix_Exploration_3.maxpat`
This patch uses the _srcdim_ and _dstdim_ attributes to combine two images into a single [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix"). The secret here is that both [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") objects share the same name and are triggered in sequence. The data from the righthand image is copied into the [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object before the data on the left, which then triggers the output and display. Notice how the lefthand image supersedes (covers) the one from the right when overlapping coordinates are given. This is one of many cases in Jitter where you’ll want to make sure one thing happens before another. For this reason, the [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object is well-known among advanced Jitter users as an essential tool.
For even more matrix filling options, take a look at [jit.gradient](https://docs.cycling74.com/reference/jit.gradient "jit.gradient"), [jit.bfg](https://docs.cycling74.com/reference/jit.bfg "jit.bfg"), [jit.gen](https://docs.cycling74.com/reference/jit.gen "jit.gen")[jit.pix](https://docs.cycling74.com/reference/jit.pix "jit.pix"). 

Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
