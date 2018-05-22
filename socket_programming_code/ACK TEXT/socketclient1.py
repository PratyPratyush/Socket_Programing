from socket import *

s = socket(AF_INET,SOCK_DGRAM)
UDP_IP = "127.0.0.1"
UDP_PORT = 5001
sp = 5005
s.bind((UDP_IP,UDP_PORT))
terminate = "start"
while terminate =="start":
	print 'Enter Message'
	mes = raw_input()
	s.sendto(mes,(UDP_IP,sp))
	ack,add = s.recvfrom(1024)
	print 'acknowledge - ',ack
	print"you want to continue = c or exit = exit"
	check = raw_input()
	if check =='c':
		s.sendto("start",(UDP_IP,sp))
	elif check =="exit":
		s.sendto("exit",(UDP_IP,sp))
		break
s.close()
