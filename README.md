# Morphology-Operators

## Introduction
Basic python implementation that applies <b>border clearing</b> and <b>hole filling</b> to images using the<a href="https://scikit-image.org/"> scikit-image</a> library.
<ul style = "color: red;">
<li>Hole filling: the morphological operator receives a binary image as input and must return another binary image with the holes of the connected components closed;</li>
<li>Border clearing: the morphological operator receives a binary image as input and must return another binary image without related components that touch as sides (edges) of the image;,</li>
</ul>
A portuguese article was written analyzing the results. The article can be found in the folder: <i>docs</i>

<b>Third project of digital image processing</b>


## How it works
The process of border clearing and hole filling is explained in the book <a href ="https://www.pearson.com/us/higher-education/program/Gonzalez-Digital-Image-Processing-4th-Edition/PGM241219.html?tab=overview">Digital Image Processing</a> by Rafael C. Gonzalez and Richard E. Woods. The implementation was done using the function <a href=https://scikit-image.org/docs/dev/api/skimage.morphology.html#skimage.morphology.reconstruction> skimage.morphology.reconstruction</a> that allows morphological reconstruction by erosion or dilation.


## How to use

### Input
The application will look for images <b>in the same directory as the source code</b> (accepting jpeg, png and tif formats), asking which image do you want to load.
After that, you can select which operator is going to be used.

### Output
The output will be the image with the selected operator applied. A preview of the output will be shown in a new window by OpenCv, you can either save the image or not. <b>The saved image will be in the same directory as the source code</b>.

An example of output using filling holes operator (input on the left, output on the right):
<div style = "display: inline-block;">
  <img src="https://github.com/Dinista/Morphology-Operators/blob/main/Sample%20images/buraco.JPG" width="180">
  <img src="https://github.com/Dinista/Morphology-Operators/blob/main/Sample%20images/buracos_Fig0916.jpg" width="180">
</div>

An example of output using border clearing operator (input on the left, output on the right):
<div style = "display: inline-block;">
  <img src="https://github.com/Dinista/Morphology-Operators/blob/main/Sample%20images/borda.JPG" width="180">
  <img src="https://github.com/Dinista/Morphology-Operators/blob/main/Sample%20images/bordas_Fig0907.jpg" width="180">
</div>

### Dependencies
<ul style = "color: red;">
  <li>Numpy.</li>
  <li>OpenCv.</li>
  <li>Scikit-image.</li>
</ul>
