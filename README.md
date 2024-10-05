# exVision: BasicToolkit

> [!WARNING]  
> The "exVision-BasicToolkit" repository was the initial version of our work, containing basic computer vision and image processing tools. While the core logic functions properly, the GUI application may not perform efficiently. For a more organized and optimized version with additional features and better resource management, please refer to the <a href="https://github.com/Computer-Vision-Spring-2024/exVision">exVision</a> repository.

## Table of Contents

1. [Overview](#overview)
2. [Getting Started with the GUI](#getting-started-with-the-gui)
3. [Acknowledgments](#acknowledgments)
4. [References](#references)
   - [Threshold-Transformation and Frequency Domain Filters](#threshold-transformation-and-frequency-domain-filters)
     - [Useful Links for Understanding](#useful-links-for-understanding)
     - [Image Resizing and Interpolation](#image-resizing-and-interpolation)
     - [Low and High Pass Filters](#low-and-high-pass-filters)
     - [Common Intensity Transformation Functions (Optional)](#common-intensity-transformation-functions-optional)
   - [Image Histograms and Equalization](#image-histograms-and-equalization)
   - [Histogram Equalization Methods](#histogram-equalization-methods)
     - [Global Histogram Equalization (GHE)]
     - [Contrast Limiting Adaptive Histogram Equalization (CLAHE)]
     - [Multipurpose Beta Optimized Bihistogram Equalization (MBOBHE)]
     - [Additional Topics]
   - [Normalization](#normalization)
   - [Hough Line Transform](#hough-line-transform)


## Overview

BasicToolkit is a PyQt desktop application that offers basic image processing tools and classical computer vision techniques built from scratch. It includes the following features:
  - Additive Noise: Uniform, Gaussian, and Salt & Pepper noise
  - Filters: Mean, Median, and Gaussian filter
  - Edge Detection: Canny, Laplacian, Prewitt, Roberts, Sobel
  - Equalization and Normalization
  - Frequency Filters and Hybrid Images
  - Local and Global Thresholding

Want to know more? Refer to [the latest version of the documentation](README-Assets)!

Also, in this folder, you will find the pure implementation of these features along with the from-scratch implementation of the [Active Contouring (SNAKES)](implementation_logic_without_Ui/active_contouring_snakes) and [Hough Transform](implementation_logic_without_Ui/hough_transformation) that aren't integrated in the GUI in this repo, but they're in the <a href="https://github.com/Computer-Vision-Spring-2024/exVision">exVision</a> repo.

## Getting Started with the GUI

> Don't use this version :) Refer to the <a href="https://github.com/Computer-Vision-Spring-2024/exVision">exVision</a> repository.

## Acknowledgments

Refer to [this organization's README](https://github.com/Computer-Vision-Spring-2024#acknowledgements) for more details about contributors and supervisors. 

## References

### Threshold-Transformation and Frequency Domain Filters

#### Useful Links for Understanding

- **Histogram**: [Watch this video on histograms](https://www.youtube.com/watch?v=tUs7Glv7lpA)
- **Thresholding**: Learn about [image thresholding](https://encord.com/blog/image-thresholding-image-processing/) and [thresholding from scratch](https://medium.com/geekculture/image-thresholding-from-scratch-a66ae0fb6f09)
  
#### Image Resizing and Interpolation

- **Image Resizing Algorithm**: [Stack Overflow discussion](https://stackoverflow.com/questions/12447549/resizing-image-algorithm-in-python)
- **Nearest Neighbor Interpolation**: Read about nearest neighbor interpolation on [ScienceDirect](https://www.sciencedirect.com/topics/engineering/nearest-neighbor-interpolation) and [K-Nearest Neighbors from Scratch](https://www.askpython.com/python/examples/k-nearest-neighbors-from-scratch)

#### Low and High Pass Filters

- [Watch this video](https://www.youtube.com/watch?v=YVBxM64kpkU).
  
#### Common Intensity Transformation Functions (Optional)

- **Learn about log, exp, and negation transformations**: [GeeksforGeeks article](https://www.geeksforgeeks.org/histogram-equalization-in-digital-image-processing/) (Skip the math part)

### Image Histograms and Equalization

- **Introduction to Histograms**: [Watch this tutorial](https://www.youtube.com/watch?v=2LhfSgrjdGo)
- **Histogram Equalization Overview**: [Wikipedia article](https://en.wikipedia.org/wiki/Histogram_equalization) and [OpenCV tutorial](https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html)
- **Introduction to Histogram Equalization**: [Watch this video](https://youtu.be/WuVyG4pg9xQ?si=xJRGoeJSugTsbAHB)
- **Overview of Color Spaces**: [Watch this helpful video](https://www.youtube.com/watch?v=gnUYoQ1pwes) and read about [conversion rules](https://docs.opencv.org/4.9.0/de/d25/imgproc_color_conversions.html#color_convert_rgb_lab)

- **Types of Histograms**
  - *RGB Histogram*
  - *HSL*
  - *HSV*
  - *Intensity Level Histogram (Grey Image)*
  - *CIELAB*: Learn more in the [Python Image Processing Cookbook](https://subscription.packtpub.com/book/data/9781789537147/1/ch01lvl1sec03/transforming-color-space-rgb-lab) and explore [code in C++](https://web.archive.org/web/20120502065620/http://cookbooks.adobe.com/post_Useful_color_equations__RGB_to_LAB_converter-14227.html)


### Histogram Equalization Methods

- **Global Histogram Equalization (GHE)**: 
  - [Explanation with a numeric example](https://www.youtube.com/watch?v=Yd6QISby8kk)
  - [Another example with theoretical explanation](https://www.youtube.com/watch?v=5-7xskk3aeo)

- **Contrast Limiting Adaptive Histogram Equalization (CLAHE)**: 
  - [Watch the OpenCV tutorial](https://www.youtube.com/watch?v=tn2kmbUVK50)

- **Multipurpose Beta Optimized Bihistogram Equalization (MBOBHE)**:
  - [Read the original paper](https://onlinelibrary.wiley.com/doi/full/10.1002/cplx.21499)

- **Additional Topics**

  - Pseudo Coloring
  - Negative Coloring (RGB, CIELAB, etc.)

### Normalization

- [Learn 5 ways to normalize an image](https://blog.finxter.com/5-best-ways-to-normalize-an-image-in-opencv-python/)


### Hough Line Transform

- **Hough Line Transform**: <a href="https://medium.com/@st1739/hough-transform-287b2dac0c70">Explanation</a> and <a href="https://medium.com/@alb.formaggio/implementing-the-hough-transform-from-scratch-09a56ba7316b">Implementation</a>
