import socket
import pack1
import os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500
ip="192.168.148.1"
s.bind((ip,ps))
adclient=(ip,pc)
a=1
while exit!="exit":
	try:
		string="rfile"+str(a)
		f=open(string,'wb')
		pack1.rec(f,s,adclient)
		a=a+1
		data,addr=s.recvfrom(1024)
		exit = data
	except socket.error:
		print "Teri maa ka"
s.close()
