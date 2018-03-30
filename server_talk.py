import sys
import socket

s = socket.socket()
host = socket.gethostname()
port = 1247
s.bind((host,port))
s.listen(5)
while True:
	c, addr = s.accept()
	print("Connection accepted from " + repr(addr[1]))
	a = 'Server approved connection\n'.encode()
	c.send(a)
	#b = repr(addr[1]) + ' : ' + c.recv(1026)
	data = c.recv(1026)
	print(data)
	#print ("b'yes'")
	if data == b'yes':
		print("success!!")
	c.close()
