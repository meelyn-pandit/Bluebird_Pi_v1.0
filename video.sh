#!/bin/bash

# Capture 3 hours of continuous video at 640x480 and 150kB/s bit rate into a pivideo.h264 file:
raspivid -t 10000 -a "Box Number" -a 12 -w 640 -h 480 -fps 25 -b 1200000 -o /mnt/usbdisk/box_num.h264

# Wrap the raw video with an MP4 container: 
MP4Box -add /mnt/usbdisk/box_num.h264 /mnt/usbdisk/box_num.mp4

# Remove the source raw file, leaving the remaining pivideo.mp4 file to play
rm /mnt/usbdisk/box_num.h264

