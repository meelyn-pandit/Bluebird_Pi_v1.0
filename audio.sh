#!/bin/bash

arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -d 10800 --max-file-time 1800 -v /mnt/usbdisk/rpi_audio.wav
