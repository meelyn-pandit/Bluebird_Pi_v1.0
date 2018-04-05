#!/bin/bash

filename="box_num"_$(date +"%m%d%y-%H%M%S")

arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -d 10 --max-file-time 1800 -v /mnt/usbdisk/$filename.wav
