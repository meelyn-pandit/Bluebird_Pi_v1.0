#!/bin/bash

sudo sh /mnt/usbdisk/audio.sh &
sudo sh /mnt/usbdisk/video.sh &
sudo python /mnt/usbdisk/temp.py &
sudo python /mnt/usbdisk/rpi_rfid.py &

wait

