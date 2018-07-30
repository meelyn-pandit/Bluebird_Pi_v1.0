# Raspberry Pi RFID reading for Seeed Studio Mini 125Khz RFID module
import serial, operator
from datetime import datetime
rfid = serial.Serial("/dev/ttyAMA0")
daytime = datetime.now().strftime("%m%d%y_%H:%M:%S")
rfid.baudrate = 9600
rfid.timeout = 5                # Need a timeout in case we read less than 5 bytes

def verify(data):
    """Check the validation bit (the last one) by XORing the first four bytes."""
    ints = map(ord, list(data))
    if (len(ints) != 5):
        return False
    return ints[-1] == reduce(operator.xor, ints[:-1])

def id(data):
    """Print out the hex string for some bytes. Don't include validation byte."""
    return "".join("{:02x}".format(ord(c)) for c in list(data)[:-1])

while True:
        data = rfid.read(5)
        if verify(data):
                logf = open("rfid_logfile.txt", "a")
                logf.write(data + "_" + daytime +" \n")
                logf.close()
                print("Read ID: ", id(data) + "_" + daytime)
        else:
                data == 0
                print("Please insert a tag")
                continue
