These are instructions of how to implement Project 1

Tested on home laptop using two instances of flip1 and flip servers through putty interface.

1.	Unzip Files and place on flip server
2.	Use 'make' to compile chatclient program
3.	Use 'python chatserve.py PORTNUMBER' to start server 
4.	Use ./chatclient  hostname   PORTNUMBER
5.	Enter client Handle name
6.	Connection will be established when user automatically sends "PORTNUM" to server.
7.	Connection display will be shown on client side.
8.	Client begins chat with messges.
9.	Server can respond to client ("Reply: ") prompt.
10.	Either side can terminate the connection by sending 'quit' in message.
11.	Server will continue to wait for connections until Interrupt signal is sent (Ctrl-C)
