---
description: How to give the sense of scale and distance
group: Polish Your Pixels
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/04-scale-and-distance/
title: Scale and Distance
---

Download Series Content and Patchers
# How to give a sense of scale and distance
Which of the two ducks is bigger?
![](https://docs.cycling74.com/images/2ce248f98ae7b5efa13f31a6885d8050_891.webp)
They are the same size, but some visual effects make us perceive the duck on the right as much bigger than the duck on the left. We, as human, estimate the size of objects through a combination of visual cues, learned experience, and context. Our brains use information from our eyes, as well as from our knowledge of the world, to interpret the relative size and distance of objects. In this guide, we'll explore how we can use Jitter to create effects that give the viewer a sense of size and scale.
## Familiarity and Context
This is an easy one: When we already know the typical size of an object, like a car or a person, we can estimate its size based on that knowledge. If we see something that looks like a car but appears unusually small, we might assume it’s further away. The objects around something in a scene also give clues. For instance, if we see a person standing next to a building, we understand the scale of each object based on the scene as a whole. We can use this to our advantage, for example, inserting some familiar objects of well-known size in the scene.
In a similar vein, we are used to seeing the world around us from a constant height—our height above the ground. Small objects are usually observed from above, and big ones from below.
## Atmospheric scattering
Atmospheric scattering occurs when sunlight or other light waves hit particles in the atmosphere, like dust, water droplets, and gas molecules, causing the light to scatter in different directions. This scattering effect influences how we see distant objects and is one of the main reasons why the sky looks blue during the day and sunsets look reddish.
Here's how it works: when we look at something far away—like a mountain range or a city skyline—the light bouncing off those distant objects travels through more of the atmosphere to reach our eyes. As it does, particles scatter the shorter blue and violet wavelengths, making distant objects appear hazy, less distinct, and sometimes even bluish. This haze makes distant objects seem "faded" compared to those nearby.
Atmospheric scattering also impacts our perception of distance and size. Because objects that are further away look blurrier and less vibrant, our brains interpret them as being far off, which helps us judge distance. Similarly, this effect can make faraway objects look smaller than they are because they lose clarity and detail as more of their light scatters. This natural "distance blur" adds depth to what we see and plays a significant role in creating a sense of scale in outdoor landscapes.
![](https://docs.cycling74.com/images/249e764b2f9cefbfcd92fb4c9babae7b_1024.webp) On the left, there's a scene rendered typically; on the right, atmospheric scattering was added
This atmospheric scattering effect is a strong visual cue for size and distance. It's much easier to see how far away the objects are, and your brain is saying: "Those donuts must be huge!"
According to Beer’s Law, light intensity diminishes exponentially with distance as it travels through a medium (like the atmosphere) filled with particles that scatter or absorb it. Essentially, the farther the light travels, the weaker it is because particles absorb or scatter part of it along the way.
I=I0⋅e−αxI = I_0 \cdot e^{-\alpha x}I=I0​⋅e−αx
  * III is the light intensity after it has traveled a certain distance xxx through the medium.
  * I0I_0I0​ is the initial intensity of the light before it enters the medium.
  * α\alphaα is the attenuation coefficient, which depends on the properties of the medium (such as concentration and the specific absorption/scattering properties of the particles within it).
  * xxx is the path length or distance the light travels through the medium.


In Max, atmospheric scattering can be added to a scene using the [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") FX named "atmospheric":
![](https://docs.cycling74.com/images/721a7329e398de82e5e769264d52193b_933.webp)
Control parameters are the factors of the Beer's law: `@density` multiplies the distance of the objects on srcreen, and `@color` specifies the rate of light absorption per color channel. `@density` and `@color` togheter consitute the α\alphaα factor. The pass also contains settings to create a ground fog effect.
## Virtual camera settings
The virtual camera settings significantly impact how we perceive the distance, size, and depth of objects in a scene. Just like a real camera, virtual camera settings such as field of view (FOV), focal length, and camera position influence how objects appear in terms of size and distance. Here’s a breakdown of the main settings and how they affect perception:
### Field of View (FOV)
Field of view represents the extent of the scene that the camera can "see" and is typically measured in degrees. It’s essentially the camera's angle of view. A wide field of view (e.g., above 60°) creates a more dramatic sense of depth but can distort objects at the edges, making close objects appear larger and distant objects smaller. This can exaggerate the sense of distance and make the scene feel expansive. A narrow field of view (e.g., below 30°) does the opposite, compressing the perceived space and making objects seem closer together, often giving a "zoomed-in" effect. In Max, you can set FOV using the `@lens_angle` attribute of [jit.gl.camera](https://docs.cycling74.com/reference/jit.gl.camera "jit.gl.camera").
![](https://docs.cycling74.com/images/095755b8fbc64c2a372e5fa701b7d4b9_1024.webp)
### Camera Position and Orientation
This refers to where the virtual camera is placed within the scene and the direction in which it's pointing. Camera height, distance from objects, and the viewing angle can greatly influence perceived size and distance. For example, low camera angles make objects appear larger and more imposing, especially when looking up at them. High camera angles create a "bird's-eye view" effect, making objects appear smaller and sometimes less significant.
### Depth of Field (DOF)
Depth of field (DOF) determines how much of the scene is in focus. A shallow DOF (where only a small part of the scene is sharply in focus) draws attention to a specific area, often creating a strong sense of foreground and background separation. A shallow depth of field can make objects outside the focal area look blurrier, enhancing the perception of depth and making the in-focus subject appear isolated or more distant from the rest of the scene. A deep depth of field, where everything is in focus, can flatten the scene slightly, as all objects appear equally sharp regardless of distance.
Im Max, you can create a depth of field effect using [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") `@fxname` "dof-hq". This effect replicates the behavior of a real camera.
![](https://docs.cycling74.com/images/f5294ae4e554d023f8ee0910411420ec_1024.webp)
The "dof-hq" pass is controlled by many parameters, but the main two are:
  * `@lens_focal_length`: The focal length of a camera is a fundamental optical property that defines how zoomed-in or zoomed-out an image appears. It’s typically measured in millimeters (mm) and describes the distance between the camera lens and its sensor or film when the lens is focused on a subject at infinity. In the context of DOF, the focal length affects the amount of depth blur. Shorter focal lengths tend to have a larger depth of field, keeping more of the scene in focus from front to back, which is helpful in capturing detailed landscapes. Longer focal lengths have a shallower depth of field, especially at wide apertures, which isolates subjects by keeping them sharp while blurring the background—ideal for portrait photography.

![](https://docs.cycling74.com/images/a7c4479318fac951b020ed965c8b1aa1_1024.webp)
  * `@lens_focal_distance`: Focal distance is the distance between the camera's lens and the point in the scene where objects appear sharp and in focus. This is different from focal length, which refers to the optical property of the lens itself. Use this attribute to decide which part of the scene must stand out and catch the viewer's attention.

![](https://docs.cycling74.com/images/4915b99e3dfeb76f33a3d63620d207b9_1024.webp)
You can active the attribute `@show_in_focus` to set "blur-hq" params precisely. The brighter the color, the sharper the image looks, and the red area shows which part of the scene is perfectly in focus.
![](https://docs.cycling74.com/images/e700b5c30a8e6eba9e700473ca44ccb8_1024.webp)
## In summary
  * Objects' scale perception is relative; leave some "clues" in the scene to let viewers determine the objects' size and distance.
  * Atmospheric scattering can make objects appear very far from the viewer; use [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") `@fxname atmospheric` if you need this effect.
  * Camera's settings and positioning influence objects' size perception.
  * Use [jit.gl.camera](https://docs.cycling74.com/reference/jit.gl.camera "jit.gl.camera")'s `@camera_angle` to flatten or exagerate the sense of depth.
  * Use [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") `@fxname dof-hq` to create a depth of field effect, to give a better sense of distance and drive viewer's attention.



Kind
    Tutorial 

Author
    Cycling '74 

Contributors
    Matteo Marson     Sam Tarakajian
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
