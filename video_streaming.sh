#!/bin/bash
#sets up unix script

###Code to stream to YouTube. If you ahve a YouTube channel your videos will be saved to your channel.
#You will need to enter your own Stream URL and Stream name/key, which can be found on your YouTube Stream preview. Be sure to remove the brackets (<>) when you enter in your Stream key
raspivid -o - -t 0 -w 1280 -h 720 -fps 25 -b 4000000 -g 50 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/<Stream name/key here!>
