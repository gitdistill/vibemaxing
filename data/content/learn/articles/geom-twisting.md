---
description: Examples of what you can do with a Jitter geometry when you twist it.
group: Jitter Geometry
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/geom-twisting/
title: Twisting
---

Download Series Content and Patchers
# Fun with Twisting Geometries
I had an idea that it might be kind of fun to explore what you could do with twisting around various Jitter geometries. The first example is a sort of straightforward answer to "how do you make a shape that twists and untwists itself?" I don't entirely know what the second example is.
## Twisty Life Saver
Open the patch _twisty-life-saver.maxpat_.
![](https://docs.cycling74.com/images/154f1fe32d4a4c6df067298c461191c6_1024.webp)
If you just watch the animation for a second, you'll see what I was going for here. First the torus twists on one side, then it untwists itself, then it does the same thing on the other side. The key to making this all work is very precise timing.
![](https://docs.cycling74.com/images/bf72818bbde90b1c397a519c5e9f219a_945.webp)
If you pop open the subpatch _[p precise-timing]_ , you'll see what's going on. Every four seconds is divided into four phases: twist right, untwist right, twist left, and untwist left. The left branch of the patch manages updating the twist angle, and the right branch flips the axes of the two [jit.geom.twist](https://docs.cycling74.com/reference/jit.geom.twist "jit.geom.twist") objects, so that the first work on the right side of the shape, and then the left.
![](https://docs.cycling74.com/images/dcc73fd7defdc71ee7af7d6fe5e2b95c_231.webp)
One kind of cute touch with this patch is the striped texture that we apply to the surface of the torus. You can see that the generated texture just makes a bunch of stripes, but if you look at the left and right edges, you can see that one color always matches with the other. That means that when the texture is applied to the torus, everything lines up seamlessly.
## Pattern Wheel
Open up the patch _pattern-wheel.maxpat_.
![](https://docs.cycling74.com/images/15b4b5aaf3c38110b551cd7333fa241d_1024.webp)
I made this patch sort of by accident when I was trying to make the other one. It's much simpler, although you could argue it makes more complex shapes.
By default, the torus is twisting around the Y axis. Of course, a torus has radial symmetry about the Y axis (in its default orientation anyway), so this doesn't change the surface of the shape much. But when we apply a checkerboard texture, you can see lots of cool patterns. Maybe those patterns have some connection to prime numbers or something.
If you want, you can twist the torus about a different axis. Since a torus does not have the right symmetry here, you'll get a mess, but it might be a cool mess.
![](https://docs.cycling74.com/images/a302645d232554efc10069fef92ac3ff_875.webp) X axis and Z axis twisting can still look kind of cool. 

Kind
    Example 

Author
    Cycling '74 

Contributors
    Sam Tarakajian
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
