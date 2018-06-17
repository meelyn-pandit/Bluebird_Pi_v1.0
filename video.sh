 #!/bin/bash

# Change box_num to whatever box number you are filming at, and keep the quotation marks!
filename="box_num"_$(date +"%m%d%y-%H%M%S")

# Capture 3 hours of continuous video at 640x480 and 150kB/s bit rate into a pivideo.h264 file:
raspivid -t 10800000 -a "Box Number" -a 12 -w 640 -h 480 -fps 25 -b 1200000 -o $filename.h264

# Wrap the raw video with an MP4 container: 
MP4Box -add $filename.h264 $filename.mp4

# Remove the source raw file, leaving the remaining pivideo.mp4 file to play
rm $filename.h264

