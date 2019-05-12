import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.0.0.141', 9889)
host = '10.0.0.141'
port = 9899
#print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect( (host, port) )


try:
    
    # Send data
    #message = 'This is the message.  It will be repeated.'
    message = 'PORTNUM'
 #   print >>sys.stderr, 'sending "%s"' % message
    text = message.encode('utf-8')
    sock.sendall( text )

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    data = ''
	
    while data != 'quit':
        data = sock.recv(1024)
        #amount_received += len(data)
        print("Received from server: {}".format(data))
  #      print >>sys.stderr, 'received "%s"' % data

finally:
    #print >>sys.stderr, 'closing socket'
    sock.close()