import socket
import sys
import time

# --------------------------------------------------------------//
# Title:		Chatserve
# Author:		Jason Ghiraldini
# Date:			2017-02-12
# Descriptions:		Websocket Chat server that allows incoming 
#			connections.  Client/server take turns 
#			sending messages.  Either side can end 
#			connection by sending message '/quit'
# --------------------------------------------------------------//

def wait(): 
	print 'Waiting for connection'
	while 1:
		#wait to accept a connection - blocking call
		conn, addr = s.accept()
		print 'Connected with ' + addr[0] + ':' + str(addr[1])
		data = conn.recv(1024)
		print("Data rx from client: {}".format(data))
		if data != "PORTNUM":
			conn.send("DENIED")
			s.close()
			sys.exit()
		else:	
			conn.send("Connection Accepted")		
			while 1:
#				data = conn.recv(1024)
#				if data == '/quit\n':
#					wait()
#				if len(data) == 0:
#					sys.exit(1)
#				else:
#					print data
				
#				sendData = raw_input("Reply: ")
				sendData = time.time()
				conn.send(str(sendData) + '\n')
				time.sleep(1)
#				if(sendData == '/quit'):
#					wait()

# --------------------------------------------------------------//
# Input:	Beginning of main program
# Output:	NA
# Description:	Initializes websocket to wait for clients to 
#		connect. Server can disconnect to client by
#		sending '/quit' message.
# --------------------------------------------------------------//

if len(sys.argv) < 2:
	print 'Usage: python chatserve.py port_number'
	sys.exit(1)
 
HOST = socket.gethostname()   # Symbolic name, meaning all available interfaces
PORT = int(sys.argv[1])
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created on ' + socket.gethostname() + ' Port: ' + sys.argv[1]
 
# Bind socket to local host and port
try:
	s.bind(('10.0.0.141', PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
#Start listening on socket
s.listen(10)
print 'Socket now listening'
wait()
