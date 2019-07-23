# Tiny Circuits Bird House
This tutorial will guide you, step-by-step on how to build your own bird house from either the TinyCircuits Bird House Kit or from your own laser cut bird house. With this tutorial, you can livestream and save videos to YouTube, livestream to your own home network, or take a timelapse of your baby birds growing! This project is a fun activity that will hopefully get you closer to nature by observing adult and nestling birds in your own backyard! 

## Basic Raspberry Pi Setup.

### Installing NOOBS Operating Software

  The Raspberry Pi (RPi) runs off of a version of Linux called Raspbian. It is very similar to the standard version of Linux but comes with a graphical user interface (GUI) that is similar to your standard desktop. Many of the RPi kits that you find online will come with a micro SD card that has NOOBS pre-installed. If you are using your own micro SD card, then you will need to format the micro SD card to FAT32 by using: https://www.sdcard.org/downloads/formatter_4/. You will need to download this software to format your micro SD card.

  Once the SD card is formatted then download NOOBS by going to: https://www.raspberrypi.org/downloads/noobs/ on your own computer and download NOOBS (the regular version, not the LITE version) onto your computer by clicking the Download zip button. The download will take a while (usually 10-12 min).
  
    Once the download is complete, extract the files and copy them to the micro SD card.
    After the files are copied put the SD card into the micro SD card slot on the RPi and plug in the peripherals (keyboard, mouse, Wifi dongle if you need it) and finaly plug in your power source to turn on the RPi.
    You will see a screen asking you to install Raspbian. Click install at the top of the screen and wait until the operating system (OS) is installed.
    Once the OS is installed you are free to play around with the RPi!
  
 ### Configuring the Raspberry Pi:
On the toolbar, click the Raspberry icon, go to Preferences, and go to Configure Raspberry Pi. Go to the Interfaces tab and enable:

* Camera
* SSH
* VNC
* SPI
* SCK
* 1-Wire
* Remote GPIO

Click finish and reboot.

### Setting up the Pi Noir Camera
With your RPi off, connect the Raspberry Pi ribbon cable to the camera. The metal pins on the cable need to touch the metal pins on the camera import. If you open up the Terminal app and type the code:
	
	raspivid -o vid.h264
	
you can get a preview video.

### Turning off the Camera LED
You will notice that the LED camera has a red light on that will come on when the camera is recording video. We need to turn that off to avoid disturbing the birds. One way to to do this is to type:
	
	sudo nano /boot/config.txt
and add:
	
	disable_camera_led=1
to the botttom of the page.

### Install MP4Box
The PiNoir camera will only record in .h264. In order to make videos easy to analyze, we will convert the videos from .h264 to .mp4. To do this we will need to install the MP4Box library to the RPi, which we will use to convert the videos. Connect to the internet (use an ethernet cord if you have one) and in the Terminal program type:
	
	sudo apt-get install -y gpac
	
wait for the program to be installed and you should be good to convert the .h264 videos to .mp4 (see video.sh script).

### Automounting USB Drives
In order to easily extract the files from the RPi, it is nice to have a USB drive attached. However, unlike regular computers, you need to manually mount the USB drives in order to save files to the drive or access the files. Fortunately, there is a way to automount the USB drive so you can access it immediately after the RPi is booted. In the Terminal app type in:
	
	sudo mkdir /mnt/usbdisk
	
to make a new directory (folder) that recognizes the USB drive.

	sudo chown -R pi:pi /mnt/usbdisk
	
to own the new directory

	sudo nano /etc/fstab
	
to edit the fstab file

	UUID="your unique UUID address"	/mnt/usbdisk	vfat	auto,users,rw,uid=1000,gid=100,umask=0002	0	0
Click Ctrl X, then y. Reboot with the USB drive in the RPi and the RPi should recognize the USB drive. You should be able to access it by typing in the Terminal:

	ls /mnt/usbdisk/
if you see the files in there then you have access to it.

### Running scripts at RPi Boot
To activate the different sensors, you will need to execute the scripts. Since the RPis will be headless (not connected to a monitor), we will need to have the scripts be executed as the RPi boots up. To do this we will need to install the Crontab which is used to run scheduled scripts. In the Terminal App type in:

	crontab -e
Select editor 2 (/bin/nano) by clicking 2 then Enter. After all of the text you will type in:

	@reboot sudo sh data_scripts.sh &

Type Ctrl X to save the file, Y for the filename to not be changed and reboot! Now your data scripts should be automatically executed at startup.

# Setting up Static IP Address
Reference: http://www.circuitbasics.com/how-to-set-up-a-static-ip-on-the-raspberry-pi/

## 1. Find the default gateway IP, which is the local IP address of your network router
	
	route -ne
		
Look for the Gateway column look for the default gateway IP and make sure that under the Iface column it says wlan0 in the same row. For example, my gateway ip address was 192.168.1.254.

## 2. Find the IP addresses of the domain name servers by entering:

	cat /etc/resolv.conf
		
you will see:
	
	nameserver 192.168.1.254
	
Copy these IP addresses to a text editor on your computer or write them down for later.

## 3. Adding Static IP Address. At the terminal, enter:

`sudo nano /etc/dhcpcd.conf`

to edit the dhcpcd.conf and add the following code to the bottom of the file:
	
	interface wlan0
	static ip_address = 192.168.1.200/24
	static routers=192.168.1.254
	static domain_name_servers=192.168.1.254
	
for the `static ip_address` you will enter a number between 0-254, I use 200 because there is less of a chance of having 200 devices connected to your router.

Hit Ctrl X and then Y to save the changes to the dhcpcd.conf. 

Reboot by typing in the terminal:
		
	sudo reboot
# Power

Powering the RPi is the biggest challenge. You can either use a [RPi power cable](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00GF9T3I0/ref=asc_df_B00GF9T3I0/?tag=hyprod-20&linkCode=df0&hvadid=309707619534&hvpos=1o1&hvnetw=g&hvrand=11550608159140157147&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1023522&hvtargid=aud-643565131866:pla-634201303877&psc=1) or you can attempt to power the RPi remotely with a [5V battery](https://www.amazon.com/Portable-Charger-Anker-PowerCore-20100mAh/dp/B00X5RV14Y/ref=sr_1_3?keywords=anker+battery&qid=1563902722&s=electronics&sr=1-3) or a 5V battery and a solar set up (see below). If you do decide to use a battery alone, you will need to swap out the batteries every few days (20,000 mAh/300 mAh RPi current use = 66 hours). 

## Putting the RPi in low power mode

## Solar Setup - In Progress!
