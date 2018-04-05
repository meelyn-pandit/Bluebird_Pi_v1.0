# Bluebird_Pi_v1.0
Scripts for Raspberry Pi 2 Model B that will collect video, audio, and temperature data, as well as read PIT tags on a Mini Seeed 125kHz RFID reader.


I. Basic Raspberry Pi Setup:

  A. Installing NOOBS Operating Software
    1. The Raspberry Pi (RPi) runs off of a version of Linux called Raspbian. It is very similar to the standard version of Linux but comes with a graphical user interface (GUI) that is similar to your standard desktop. Many of the RPi kits that you find online will come with a micro SD card that has NOOBS pre-installed. If you are using your own micro SD card, then you will need to format the micro SD card to FAT32 by using: https://www.sdcard.org/downloads/formatter_4/. You will need to download this software to format your micro SD card.
    2. Once the SD card is formatted then download NOOBS by going to: https://www.raspberrypi.org/downloads/noobs/ on your own computer and download NOOBS (the regular version, not the LITE version) onto your computer by clicking the Download zip button. The download will take a while (usually 10-12 min).
    Once the download is complete, extract the files and copy them to the micro SD card.
    After the files are copied put the SD card into the micro SD card slot on the RPi and plug in the peripherals (keyboard, mouse, Wifi dongle if you need it) and finaly plug in your power source to turn on the RPi.
    You will see a screen asking you to install Raspbian. Click install at the top of the screen and wait until the operating system (OS) is installed.
    Once the OS is installed you are free to play around with the RPi!
  
  B. Configuring the Raspberry Pi:
    1. On the toolbar, click the Raspberry icon and go to Configure Raspberry Pi. Go to the Interfaces tab and enable:
			Camera
			SSH
			VNC
			1-Wire
			Remote GPIO
		Click finish and reboot.

II. Setting up the Pi Noir Camera
	A. With your RPi off, connect the Raspberry Pi ribbon cable to the camera. The metal pins on the cable need to touch the metal pins on the camera import. If you open up the Terminal app and type the code:
	
raspivid -o vid.h264
	
you can get a preview video.
	B. Turning off the Camera LED - You will notice that the LED camera has a red light on that will come on when the camera is recording video. We need to turn that off to avoid disturbing the birds. One way to to do this is to type:
	
	sudo nano /boot/config.txt
and add:
	
	disable_camera_led=1
to the botttom of the page.
	C. Install MP4Box - The PiNoir camera will only record in .h264. In order to make videos easy to analyze, we will convert the videos from .h264 to .mp4. To do this we will need to install the MP4Box library to the RPi. Connect to the internet (use an ethernet cord if you have one) and in the Terminal program type:
	
	sudo apt-get install -y gpac
wait for the program to be installed and you should be good to convert the .h264 videos to .mp4 (see video.sh script).

III. Automounting USB Drives - In order to easily extract the files from the RPi, it is nice to have a USB drive attached. However, unlike regular computers, you need to manually mount the USB drives in order to save files to the drive or access the files. Fortunately, there is a way to automount the USB drive so you can access it immediately after the RPi is booted.
	A. In the Terminal app type in:
	
	sudo mkdir /mnt/usbdisk
to make a new directory (folder) that recognizes the USB drive.

	sudo chown -R pi:pi /mnt/usbdisk
to own the new directory

	sudo nano /etc/fstab
to edit the fstab file

	/dev/sdal	/mnt/usbdisk	vfat rw, nosuid,nodev,relatime,uid=1000,gid=1000,fmask=0022,dmask=0077	0	4
Click Ctrl X, then y. Reboot with the USB drive in the RPi and the RPi should recognize the USB drive. You should be able to access it by typing in the Terminal:

	ls /mnt/usbdisk/
if you see the files in there then you have access to it.

IV. Running scripts at RPi Boot - to activate the different sensors, you will need to execute the scripts. Since the RPis will be headless (not connected to a monitor), we will need to have the scripts be executed as the RPi boots up. To do this we will need to install the Crontab which is used to run scheduled scripts. In the Terminal App type in:

	crontab -e
Select editor 2 (/bin/nano) by clicking 2 then Enter. After all of the text you will type in:

	@reboot sudo sh data_scripts.sh &
Type Ctrl X to save the file, Y for the filename to not be changed and reboot! Now your data scripts should be automatically executed at startup.
