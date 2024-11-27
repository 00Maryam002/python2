# Image Processing with a 9x9 Filter to Generate 9 Scaled Images

This Python program processes an input image, resizing it to 900×900 pixels, and uses a 9×9 filter to generate 9 smaller 100×100 images. this approach uses the filter to systematically sample pixels from specific locations in the original image and maps them into distinct output images.

# Key Features

1.Image Resizing
The program ensures the input image is resized to 900×900 pixels, making it compatible with the filtering process

2.Filter-Based Sampling

 +A 9×9 filter is applied, starting at different positions for each of the 9 output images.
 +For each output image, pixels are selected with a step size of 9, ensuring no overlap or repeated pixels.
 
3.Output Images

+The program creates 9 blank 100×100 images.
+Each image represents a scaled version of the original but sampled from a unique starting point.

# How It Works

1.Input:The user provides the path to the input image.The image is resized to 900×900 if necessary.

2.Filter Application: 

+The program divides the original image into a grid of 9×9.
+Each filter starts at a unique position and samples pixels based on the grid.
+The sampled pixels are mapped into their respective positions in one of the 100×100 output images

3.Output: After processing, the 9 output images are displayed one by one.

# How to Run

+Ensure you have the Pillow library installed using:
pip install pillow
+Execute the script and provide the path to your image when prompted.

# What is this program useful for?

This program is ideal for creating scaled versions of an image where each output image captures details from different parts of the original. The unique sampling strategy ensures each image highlights a specific perspective of the source.
