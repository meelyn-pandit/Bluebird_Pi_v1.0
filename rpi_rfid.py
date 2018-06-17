import serial
from datetime import datetime

daytime = datetime.now().strftime("%m%d%y_%H:%M:%S")
serial = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

while True:
	string = serial.read(12)

	if len(string) == 0:
		print("Please insert a tag")
		continue
	else:
		logf = open("rfid_logfile.txt", "a")
		logf.write(string[1:11] + "_" + daytime + "\n")
		logf.close()
		print(string[0:15] + "_" + daytime)


