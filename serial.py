# sudo apt-get install python-pip
# If installed:
#   python -m pip uninstall serial 
# python -m pip install pyserial
# 
# This script is used for setting a GPS to only output GPRMC NMEA sentences
#
import glob
import time
from functools import partial
import serial 

ser = serial.Serial("/dev/ttyS1",4800, timeout=1)
ser.close()
time.sleep(0.2)
ser.open()
time.sleep(0.2)
  
ser.write("$PGRMO,,4" + '\r\n')
time.sleep(1)
ser.write("$PGRMO,GPGGA,0" + '\r\n')
time.sleep(1)
ser.write("$PGRMO,GPGSA,0" + '\r\n')
time.sleep(1)
ser.write("$PGRMO,GPGSV,0" + '\r\n')


print("waiting for msg...")
time.sleep(2)

for i in range(20):
	msgq=ser.readline()
	print(msgq)

ser.close()

