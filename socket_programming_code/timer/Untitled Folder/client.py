import socket
import pack1
import time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500
ip="192.168.148.1"
s.bind((ip,pc))
adserver=(ip,ps)
string = raw_input("Enter file name") 
f=open(string,'rb')
while exit!="exit":
	try:
		pack1.send(f,s,adserver,string)
		#s.timeout(5.0)
	except socket.timeout:
		print "Retrying"
		#time.sleep(1)
		#continue
	print "you want to continue = c or exit = exit"
	exit = raw_input()
	s.sendto(exit,adserver)
s.close()
