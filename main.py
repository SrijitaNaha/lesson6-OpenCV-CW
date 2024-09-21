import cv2
import os
import time

# List of image files
image_files = ["ash.png","jerry.png", "pika.png", "tom.png"]

# Video codec and filename
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_filename = "output.avi"

# Get the dimensions of the first image
img = cv2.imread(image_files[0])
height, width, layers = img.shape

# Create a video writer
video = cv2.VideoWriter(video_filename, fourcc, 1.0, (width, height))

# Iterate over the image files and add them to the video
for file in image_files:
    img = cv2.imread(file)
    for _ in range(30):  # Write each image 30 times to create a 1-second delay
        video.write(img)

# Release the video writer
video.release()
