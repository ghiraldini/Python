#!/usr/bin/env python

import time

outfile = "time_stamp.txt"

f = open(outfile, "w")
while True:
	print("Writing to file: {}, TIME: {}}]".format(outfile, str(time.time()))
	f.write(str(time.time()) + "\n")
	time.sleep(1)
			
	
