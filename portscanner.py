#!/bin/python

import sys
import socket
from datetime import datetime

#Define our targets
if len(sys.argv) ==2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to ipv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 portscanner.py <ip>")
	
#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

#check time scan initiated
t1 = datetime.now()

try:
	for port in range(50,85): # or scan the whole range 1,65535
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("Port {}: is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
#Check time again
t2 = datetime.now()

#Find out How long it took to run the script
total = t2 - t1	
	
print('Scan Completed in:',total)
