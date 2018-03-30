import socket
import sys

print "Testing Server Connection"

s = socket.socket()
# host = '128.54.175.128'	# needs to be in quote
host = '100.82.252.58'
port = 1247
s.connect( (host, port) )
print s.recv(1024)
input = raw_input( 'type anything and click enter...\n' )
s.send(input.encode())
print "the message has been send"