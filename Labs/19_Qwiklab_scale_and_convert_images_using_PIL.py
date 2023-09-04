"""Project Problem Statement"""
# To complete this module, you'll need to write a script that processes a bunch of images. It turns out that your
# company is in the process of updating its website, and a design contractor has been hired to create some new icon
# graphics for the site. However, the contractor has delivered the final designs and they’re in the wrong format,
# rotated 90° and too large. You’re unable to get in contact with the designers and your own deadline is approaching
# fast. You’ll need to use Python to get these images ready for launch!
#
# So, how will you do this? You'll need to go through a folder full of images and operate with each of them. On each
# image, you'll use PIL methods like the ones we saw in the examples, and then write the new images in the right place.

# Your company is in the process of updating its website, and they've hired a design contractor to create some new icon
# graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too
# large. Oof! You're not able to get in contact with the designers and your own deadline is approaching fast. You'll
# need to use Python to get these images ready for launch.
#
# What you'll do
# Use the Python Imaging Library to do the following to a batch of images:
#
# Open an image
# Rotate an image
# Resize an image
# Save an image in a specific format in a separate directory

"""Download the file"""

# Your design contractor sent you the zipped file through his team drive. Download the file from the drive using the
# following CURL request:

# curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

# Output:
# student-04-c958860afa12@linux-instance:~$ curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
# awk: cannot open ./cookie (No such file or directory)
#   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                  Dload  Upload   Total   Spent    Left  Speed
#   0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
# 100  327k  100  327k    0     0   208k      0  0:00:01  0:00:01 --:--:-- 3412k

# List files using the command:

# ls

# Output:
# images.zip

# Unzip the file using the following command:

# unzip images.zip

# To list images from the images folder use the following command:

# ls ~/images

# Output:
# student-04-c958860afa12@linux-instance:~$ ls ~/images
# ic_add_location_black_48dp        ic_layers_clear_white_48dp             ic_local_mall_black_48dp
# ic_add_location_white_48dp        ic_layers_white_48dp                   ic_local_mall_white_48dp
# ic_beenhere_black_48dp            ic_local_activity_black_48dp           ic_local_movies_black_48dp
# ic_beenhere_white_48dp            ic_local_activity_white_48dp           ic_local_movies_white_48dp

# The images received are in the wrong format:
#
# .tiff format
# Image resolution 192x192 pixel (too large)
# Rotated 90° anti-clockwise
# The images required for the launch should be in this format:
#
# .jpeg format
#
# Image resolution 128x128 pixel
#
# Should be straight

"""Install Pillow"""

# We should change the format and size of these pictures, and rotate them by 90° clockwise. To do this, we'll use Python
# Imaging Library (PIL). Install pillow library using the following command:

# pip3 install pillow

# Python Imaging Library (known as Pillow in newer versions) is a library in Python that adds support for opening, manipulating, and saving lots of different image file formats.
#
# Pillow offers several standard procedures for image manipulation. These include:
#
# Per-pixel manipulations
# Masking and transparency handling
# Image filtering, such as blurring, contouring, smoothing, or edge finding
# Image enhancing, like sharpening and adjusting brightness, contrast or color
# Adding text to images (and much more!)

"""Write a Python script"""
# This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:
#
# Iterate through each file in the folder
# For each file:
# Rotate the image 90° clockwise
# Resize the image from 192x192 to 128x128
# Save the image to a new folder in .jpeg format
# Use a nano editor for this purpose. You can name the file however you'd like. And make sure to save the updated images
# in the folder: /opt/icons/
#
# You'll use lots of methods from PIL to complete this exercise. You can refer to Pillow
# https://pillow.readthedocs.io/en/stable/reference/index.html for detailed explanations and
# have a look at the tutorials https://pillow.readthedocs.io/en/stable/handbook/tutorial.html to help you build the
# script and complete the task.
#
# To save the file after editing, press Ctrl-O, Enter, and Ctrl-x.
#
# #!/usr/bin/env python3
# from PIL import Image
# import os
#
# directory = "images/"
# output_directory = "/opt/icons/"
#
# #The for loop to correct the badly formatted images.
# for filename in os.listdir(directory):
#     if filename != ".DS_Store":
#         im = Image.open(os.path.join(directory, filename))
#         im = im.rotate(-90)
#         im = im.resize((128,128))
#         im = im.convert("RGB")
#         im.save(os.path.join(output_directory, filename+".jpeg"))
# Once your script is ready, grant executable permission to the script file.

# chmod +x <script_name>.py

# Replace <script_name> with the name of your script.
#
# Now, run the file.

# ./<script_name>.py

# Replace <script_name> with the name of your script.
#
# On a successful run, this should produce images in the right format within the directory: /opt/icons/
#
# To view the updated images use the following command:

# ls /opt/icons

# Output:
# student-04-c958860afa12@linux-instance:~$ ls /opt/icons
# ic_add_location_black_48dp.jpeg             ic_local_dining_black_48dp.jpeg
# ic_add_location_white_48dp.jpeg             ic_local_dining_white_48dp.jpeg
# ic_beenhere_black_48dp.jpeg                 ic_local_drink_black_48dp.jpeg

# To check image properties, use the Python interpreter:

# python3

# Once the interactive shell opens, import the Image module from PIL:

# from PIL import Image

# Open any image from the folder, or you can use the following image:

# img = Image.open("/opt/icons/ic_edit_location_black_48dp")

# To view the format and size of the image:

# img.format, img.size

# Output:
# >>> img.format, img.size
# ('JPEG', (128, 128))

# Type exit() to exit from the Python interpreter.
