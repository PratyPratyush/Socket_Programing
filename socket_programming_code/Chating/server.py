from socket import *

s=socket(AF_INET,SOCK_DGRAM)
s1=socket(AF_INET,SOCK_DGRAM)
host = '127.0.0.1'
sp=5000				# sp -----> cp
cp=5001				# sp1 -----> cp1
sp1=6000
cp1=6001
s.bind((host,sp))
s1.bind((host,sp1))
t='c'

while t=='c':
	msg=raw_input("Enter your message:  ")
	s.sendto(msg,(host,cp))
	#----------------
	data,addr=s1.recvfrom(1024)
	print data," address is ---",addr
	#----------------------
	msg1=raw_input("Enter again message: ")
	s1.sendto(msg1,(host,cp1))
	#-------------------
	print'you want to continue = c or exit = exit  :'
	t=raw_input()
	s.sendto(t,(host,cp))
s.close()
s1.close()

	
	
