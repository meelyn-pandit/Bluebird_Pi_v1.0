import sys
import urllib2
from time import sleep
import board
import busio
import tinycircuits_bme280
import glob
import datetime

#Enter API key here
myAPI = 'XNX4ASNMC4G2HA71'

#URL where we will send the data
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = tinycircuits_bme280.TinyCircuits_BME280_I2C(i2c, 1)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

temp = "%0.1f C" % bme280.temperature
humid = "%0.1f %%" % bme280.humidity
press = "%0.1f hPa" % bme280.pressure
alt = "%0.2f meters" % bme280.altitude

#Send data to thingspeak 

conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s' % (temp,humid,press,alt)
print conn.read()

#Closing the connection
conn.close()

sleep(30)

# f = open('/home/pi/sensor_data.txt','a') #Creates a text file that will store the environmental data

# data_header = "DateTime","Temperature(*C)","Humidity (%)","Pressure (hPa)","Altitude (m)" #Data header will be printed everytime this script is run
# header = str(data_header)
# f.write(header + '\n')

# while True:
    # print("\nTemperature: %0.1f C" % bme280.temperature)
    # print("Humidity: %0.1f %%" % bme280.humidity)
    # print("Pressure: %0.1f hPa" % bme280.pressure)
    # print("Altitude = %0.2f meters" % bme280.altitude)
    # now = datetime.datetime.now()
	# timestamp = now.strftime("%m/%d/%Y %H:%M:%S") #Datetime printed as one string
	# print(timestamp)
	# data = timestamp,bme280.temperature,bme280.humidity,bme280.pressure,bme280.altitude
	# textdata = str(data)
	# f.write(textdata+'\n')
	# time.sleep(60) #60s delay, can increase or decrease depending on how often you want to collect the data
