---
description: How to get rid of aliasing artifacts in Jitter
group: Polish Your Pixels
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/02-antialiasing/
title: Antialiasing
---

Download Series Content and Patchers
# Anti-aliasing
![](https://docs.cycling74.com/images/d0a5639350af4c15bdab8e45675be46d_937.webp)
Imagine looking at a digital image where the edges of objects aren’t smooth but appear jagged, like tiny staircases. This is a common problem called aliasing, where visuals don’t look as smooth as we’d like because the computer struggles to represent fine details at a limited resolution. Let's break down what aliasing means, why it happens, and how to fix it in Jitter.
Aliasing happens when complex images or detailed patterns are represented at a lower resolution than needed. Picture trying to draw a smooth curve using only square blocks—no matter how carefully you place them, you’ll end up with a blocky, stepped edge instead of a perfect curve. Aliasing arises when a continuous signal (e.g., an image or sound wave) is sampled at an insufficient rate, violating the Nyquist-Shannon sampling theorem. In computer graphics, this means that when an image or 3D model is rendered at a resolution that cannot fully capture its detail, the representation suffers from noticeable artifacts.
A variety of techniques have been developed to minimize aliasing. Such techniques are grouped under the umbrella term **anti-aliasing**.
In Jitter, there are several anti-aliasing methods we can use to reduce aliasing issues:
## Supersampling anti-aliasing (SSAA)
Supersampling (also called oversampling) is a technique used in image processing and computer graphics to reduce aliasing, which manifests as jagged edges or artifacts when representing high-resolution details on a low-resolution display. It works by rendering or processing the image at a much higher resolution than the final output, then applying a downscaling process to achieve smoother and more visually appealing results.
At its core, supersampling increases the number of samples taken per pixel. When an image is rendered, each pixel on the screen represents a single sample of the scene's light and color data. However, in supersampling, instead of a single sample, multiple samples are taken for each pixel by rendering the scene at a higher resolution. For example, if the target resolution is 1920x1080, supersampling at 4x might render the image at 7680x4320, effectively capturing 16 times the number of samples for each pixel.
Once the high-resolution image is generated, a filtering process is applied. This step combines the additional samples taken for each pixel to calculate an average value. The averaging smooths out abrupt transitions in color or brightness that cause the jagged edges or harsh lines associated with aliasing. By combining these samples into a single value per pixel, supersampling effectively captures the sub-pixel detail that would otherwise be lost.
The final step is downscaling. The high-resolution, filtered image is resized to the target resolution. This step preserves the smoothness and visual fidelity introduced during the filtering process. The result is a final image with significantly reduced aliasing.
This anti-aliasing method is highly effective in image processing. Operations such as rotations and distortions can introduce aliasing artifacts in the processed image. Aliasing can be mitigated by super-sampling the image prior to applying these transformations. Once the process is complete, the image is filtered and then downscaled to its original resolution.
![](https://docs.cycling74.com/images/5adc83ac0aa3517312f6378c96307f3c_1024.webp)
This is the same approach used in signal processing for reducing aliasing: upsample -> process -> low-pass filter -> downsample.
In Max there isn't a built-in option for super-sampling an image process, but you can create one yourself. On the CPU, you can upscale a jitter matrix using [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") and then filter and downscale it with [jit.dimop](https://docs.cycling74.com/reference/jit.dimop "jit.dimop").
![](https://docs.cycling74.com/images/cbdcf4b85f53ee54693168b73f08106d_591.webp)
On the GPU, you can upscale textures using [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture") and perform averaging and downscaling with [jit.gl.pix](https://docs.cycling74.com/reference/jit.gl.pix "jit.gl.pix") or custom shaders:
![](https://docs.cycling74.com/images/2efbe4239f3b45d3eda80e2feb84f66d_920.webp)
In the example above, we're performing a 6x upscale and downscale. In the GPU implementation, the filtering process is optimized by splitting it into two separate steps. Averaging is performed using a 6x6 square box kernel, which would require a total of 36 texture lookups if done in a single pass. However, square kernels are separable, meaning the filtering and downscaling can be applied separately along each dimension. This approach achieves the same mathematical result while reducing the number of texture lookups to 2N2N2N instead of N2N^2N2, where NNN represents the scaling factor.
While supersampling produces stunning results, it’s not without its challenges. Rendering an image at a much higher resolution means more processing power is required, which can slow things down. For still images, this isn’t much of an issue, but in real-time computer graphics applications, supersampling can be too demanding to use extensively.
> [!TIP] If performance is not a concern, I recommend using supersampling whenever an image undergoes a spatial resampling process, such as rotation, distortion. 
> ![](https://docs.cycling74.com/images/d02b122d6a900d6020e277932ec31598_806.webp)
## Full Scene Anti-Aliasing (FSAA)
FSAA is simply supersampling apllied on 3D renderings. FSAA solves aliasing issues by rendering the entire scene at a higher resolution than the display resolution. Once the high-resolution scene is rendered, FSAA averages the colors of the sub-pixels to compute the final color of each displayed pixel. The rendered high-resolution image is then downsampled (reduced) to the original display resolution. The result is a smoother final image that preserves the details while minimizing aliasing effects.
In Max, FSAA can be enabled by the attribute `@fsaa` of [jit.world](https://docs.cycling74.com/reference/jit.world "jit.world"), [jit.pworld](https://docs.cycling74.com/reference/jit.pworld "jit.pworld"), and [jit.gl.node](https://docs.cycling74.com/reference/jit.gl.node "jit.gl.node"). `@fsaa` enables 2x supersampling.
![](https://docs.cycling74.com/images/f16bea0f68df998ff3968792b4bb4f01_643.webp)
This method of anti-aliasing is highly effective but can be computationally intensive, as it involves doubling the resolution of the images being rendered.
## Temporal Anti-Aliasing (TAA)
Temporal Anti-Aliasing (TAA) is an advanced anti-aliasing technique that reduces aliasing artifacts by using information from previous frames in addition to the current frame to produce aliasing-free images. TAA takes samples from multiple frames over time (hence "temporal") and combines them. Unlike techniques that only use information from a single frame, TAA leverages data from past and current frames to determine the color of each pixel in the current frame.
TAA applies a sub-pixel jitter or shift to the camera's position between frames. This shift allows the rendering engine to gather more unique sub-pixel data over time. The sub-pixel offsets are small and imperceptible individually, but when combined over several frames, they result in higher-quality sampling and reduce aliasing. The samples from the current frame and previous frames are blended together. The algorithm accumulates and averages these samples to compute the final color of each pixel. A history buffer is maintained to store information from past frames, allowing the TAA algorithm to look back over time and use this data in the blending process. TAA incorporates motion vectors to account for object and camera movement. These vectors help track how each pixel has moved from frame to frame, ensuring that the accumulation of data aligns correctly and doesn't cause ghosting or blurring of moving objects.
In Max, TAA can be applied using the object [jit.gl.pass](https://docs.cycling74.com/reference/jit.gl.pass "jit.gl.pass") `@fxname` TAA.
![](https://docs.cycling74.com/images/77b76ef37262f324efc42d57f77b1887_636.webp) Left: TAA on; right: TAA off.
Careful consideration must be given to the placement of Temporal Anti-Aliasing (TAA) in an effects chain. TAA relies on color information across multiple frames, and to prevent ghosting artifacts, it restricts the color of each pixel to fall within the minimum and maximum color values of its eight neighboring pixels. This process, known as color clipping, is a critical aspect of TAA. To enhance the accuracy of color clipping, colors are first converted from RGB to the YCoCg color space. Without delving too deeply into technical details, this color space represents color using values strictly within the [0, 1] range. Consequently, it is important to ensure that TAA does not receive RGB values exceeding 1. Applying tone mapping before TAA guarantees that no values surpass this range.
TAA must be placed after tonemapping and before gamma correction.
![](https://docs.cycling74.com/images/e2b358ef220adca18daeff42ef306dfc_931.webp)
## Mipmapping
Imagine you’re playing a video game, and you’re looking at a wall in the distance. The wall is covered with a brick texture, and when you get closer, you can see the texture in full detail. But when you’re far away, you don’t really need that high level of detail—you just need enough texture to recognize it as a wall. This is where mipmapping comes in. Mipmapping is a clever trick used to make textures look nice (alias-free) from all distances.
When a texture (like a brick wall) is loaded, the computer automatically makes smaller versions of it, called mipmaps. Each mipmap is a scaled-down version of the original texture. So, if the original texture is 1024x1024 pixels, mipmaps would be created at 512x512, 256x256, 128x128, and so on, all the way down to a tiny 1x1 pixel version. When you’re far from the wall, the graphics engine will use one of the smaller mipmaps instead of the original high-resolution texture. As you get closer, it switches to larger mipmaps, and when you’re really close, it uses the full-resolution texture. This set of pre-filtered textures can reduce aliasing artifacts appearing on textured surfaces.
Mipmapping in Max is enabled at texture level: set [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture")'s `@mipmap` to "bilinear" or "trilinear" and disable `@rectangle`.
[jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture")'s `@rectangle` must be disabled (0) to enable mipmapping, as non-rectangular textures are required for creating the MIP levels.
![](https://docs.cycling74.com/images/bd66f74a6e8404b83b5591dc97be88c9_932.webp) ![](https://docs.cycling74.com/images/07df61a2738d7a3d3df2d2b1faea72f6_639.webp) Left: Mipmapping enabled; right: Mipmapping disabled.
Anti-Aliasing and mipmapping can coexist. We suggest always using both an anti-aliasing method and mipmapping combined.
![](https://docs.cycling74.com/images/a24648db32e9792c3cce31a8799cc0df_955.webp) Left: no anti-aliasing and no mipmapping. Center: mipmapping only (trilinear). Right: mipmapping (trilinear) + anti-aliasing (TAA).
These are the anti-aliasing methods currently available in Max, each suited to different scenarios. Some demand significant computational resources for higher-quality results, while others are optimized for real-time performance. Each method has its own strengths and limitations, and the best choice depends on the specific needs of your project and the balance you wish to strike between quality and efficiency.
## In summary
  * Consider supersampling spatial resampling effects, like rotation, distortion, scaling.
  * TAA must be placed after tonemapping and before gamma correction.
  * [jit.gl.texture](https://docs.cycling74.com/reference/jit.gl.texture "jit.gl.texture")'s `@rectangle` must be disabled (0) to enable mipmapping.
  * You can use both an anti-aliasing method and mipmapping combined.


## To learn more about
  * <https://www.techspot.com/article/2219-how-to-3d-rendering-anti-aliasing/>
  * <https://en.wikipedia.org/wiki/Mipmap>
  * <https://sugulee.wordpress.com/2021/06/21/temporal-anti-aliasingtaa-tutorial/>
  * <https://ziyadbarakat.wordpress.com/2020/07/28/temporal-anti-aliasing-step-by-step/>
  * <https://www.elopezr.com/temporal-aa-and-the-quest-for-the-holy-trail/>



Kind
    Tutorial 

Author
    Cycling '74 

Contributors
    Matteo Marson     Sam Tarakajian
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
