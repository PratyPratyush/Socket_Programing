import socket
import pack1
import time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host_name=socket.gethostname()
#host =socket.gethostbyname(host_name) 
ps=55000
pc=55500
host = "127.0.0.1"
print host
print host_name
s.bind((host,pc))
adserver=(host,ps)
string = raw_input("Enter file name") 
f=open(string,'rb')
while exit!="exit":
	try:
		pack1.send(f,s,adserver,string)
	except socket.timeout:
		print "Retrying"
	print "you want to continue = c or exit = exit"
	exit = raw_input()
	s.sendto(exit,adserver)
s.close()
