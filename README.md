# Task-1

## Threshold-Transformation

### Links to understand these points:

- Histogram: https://www.youtube.com/watch?v=tUs7Glv7lpA
- Threshold: https://encord.com/blog/image-thresholding-image-processing/ & https://medium.com/geekculture/image-thresholding-from-scratch-a66ae0fb6f09

## Frequency domain filters and hybrid images
### Image Resize
- [Stack Overflow - Resizing Image Algorithm in Python](https://stackoverflow.com/questions/12447549/resizing-image-algorithm-in-python)
  
### Nearest Neighbor Interpolation
- [Sciencedirect - Nearest Neighbor Interpolation](https://www.sciencedirect.com/topics/engineering/nearest-neighbor-interpolation)
- [AskPython - K-Nearest Neighbors from Scratch](https://www.askpython.com/python/examples/k-nearest-neighbors-from-scratch)

### Low and High Pass Filters
- [YouTube - Low and High Pass Filters](https://www.youtube.com/watch?v=YVBxM64kpkU)

## Image Histogram
- [Introduction to Image Histograms](https://www.youtube.com/watch?v=2LhfSgrjdGo)
## Histogram Equalizing

### Overview
- [Link to Wikipedia Article. The General Idea.](https://en.wikipedia.org/wiki/Histogram_equalization)
- [Introduction to Histogram Equalization](https://youtu.be/WuVyG4pg9xQ?si=xJRGoeJSugTsbAHB)
- [Short and Straightforward -> opencv documentation](https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html)

### Common Intensity Transformation Functions (log, exp, negation) (***optional***)
- [Link to Geeks for Geeks Article and Explanation for Two Types of Histograms](https://www.geeksforgeeks.org/histogram-equalization-in-digital-image-processing/)
(Skip the math part)
### Color spaces - [A helpful video](https://www.youtube.com/watch?v=gnUYoQ1pwes) 
- [Conversion rules -> opencv documentation](https://docs.opencv.org/4.9.0/de/d25/imgproc_color_conversions.html#color_convert_rgb_lab)
- #### RGB Histogram (M.Sami's Part)
- #### Intensity level Histogram ( grey image )
- #### CIELAB 
    - [Easy explanation and 3 basic expirements - python image processing cookbook](https://subscription.packtpub.com/book/data/9781789537147/1/ch01lvl1sec03/transforming-color-space-rgb-lab)
    
    - [Code in cpp](https://web.archive.org/web/20120502065620/http://cookbooks.adobe.com/post_Useful_color_equations__RGB_to_LAB_converter-14227.html)
- #### HSL
- #### HSV 

### Histogram Equalizing methods
- #### Global Histogram Equalization (GHE)
     - Explanation of Global Histogram Equalization.

    - [Link to Numeric Example from an Indian YT Video](https://www.youtube.com/watch?v=Yd6QISby8kk)
    - [Another numeric example (and theoritical explanation, skip if you know it), skip if you got the first](https://www.youtube.com/watch?v=5-7xskk3aeo)

- #### Contrast Limiting Adaptive Histogram Equalization (CLAHE)
    - [OpenCV Python Histogram Equalization and CLAHE - YT Vid](https://www.youtube.com/watch?v=tn2kmbUVK50)
- #### Multipurpose Beta Optimized Bihistogram Equalization (MBOBHE).
    - [The original paper](https://onlinelibrary.wiley.com/doi/full/10.1002/cplx.21499)

### Some cool stuff 
 - #### pseudo coloring
 - #### negative coloring (rgb, cielab, ,,,,?)

## Normalization
- [Using These 5 Ways](https://blog.finxter.com/5-best-ways-to-normalize-an-image-in-opencv-python/)
