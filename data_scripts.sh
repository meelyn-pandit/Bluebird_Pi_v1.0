#!/bin/bash

sudo sh audio.sh &
sudo sh video.sh &
sudo python temp.py &
sudo python rpi_rfid.py &

wait

