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

def wait(s):
	print('Waiting for connection')
	while 1:
		#wait to accept a connection - blocking call
		conn, addr = s.accept()
		print('Connected with {}:{}'.format(addr[0], str(addr[1])))
		data = conn.recv(1024)

		# Data from Client on_connected
		print("Data rx from client: {}".format(data))

		# This can be a secret password client send to connect
		# to the server, 'PORTNUM' is used here
		if data != "PORTNUM":
			conn.send("DENIED")
			s.close()
			sys.exit()
		else:

			# Client successfully connected to server
			# Begin streaming data until receiving 'STOP'
			# command from Client.
			# 'STOP COMMAND' == 'TBD'
			conn.send("Connection Accepted")
			while 1:
#				data = conn.recv(1024)
#				if data == '/quit\n':
#					wait()
#				if len(data) == 0:
#					sys.exit(1)
#				else:
#					print data

				# Here we need to build the data string to send
				# Sample data located in data.txt in project folder.
				send_data = time.time()
				conn.send(str(send_data) + '\n')
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
def main():
	if len(sys.argv) < 2:
		print('Usage: python chatserve.py port_number')
		sys.exit(1)
	 
	# HOST = socket.gethostname()   # Symbolic name, meaning all available interfaces
	HOST = '10.0.0.141'
	PORT = int(sys.argv[1])
	 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print 'Socket created on ' + socket.gethostname() + ' Port: ' + sys.argv[1]
	 
	# Bind socket to local host and port
	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print('Bind failed. Error Code {}: Message {}'.format(str(msg[0]), msg[1]))
		sys.exit()
		
	# Start listening on socket
	s.listen(10)
	print('Socket now listening')
	wait(s)

	
if __name__ == "__main__":
	main()