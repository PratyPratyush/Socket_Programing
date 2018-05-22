import socket
import pack1
import os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host_name=socket.gethostname()
#host = socket.gethostbyname(host_name)
ps=55000
pc=55500
host = "127.0.0.1"
print host
print host_name
#ip="192.168.148.1"
s.bind((host,ps))
adclient=(host,pc)
a=1
while exit!="exit":
		string="rfile"+str(a)
		f=open(string,'wb')
		pack1.rec(f,s,adclient)
		a=a+1
		data,addr=s.recvfrom(1024)
		exit = data
s.close()
