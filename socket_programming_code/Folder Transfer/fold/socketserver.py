from socket import *

s = socket(AF_INET,SOCK_DGRAM)
UDP_IP = '127.0.0.1'
UDP_PORT = 5005
cp = 5001
s.bind((UDP_IP,UDP_PORT))
terminate="start"
while terminate =="start":
	data,addr = s.recvfrom(1024)
	s.sendto("success",(UDP_IP,cp))
	print "connectin from  ",addr
	print data
	check,addr=s.recvfrom(1024)
	terminate = check
s.close()
