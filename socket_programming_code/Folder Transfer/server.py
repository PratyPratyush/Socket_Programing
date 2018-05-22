import socket
import package
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500

s.bind((host,ps))
addressclient=(host,pc)

data,addr=s.recvfrom(1024)
dirlen = int(data)
os.makedirs("receivefolder")
currdir = os.getcwd()
os.chdir('./'+"receivefolder")

a=1
while (dirlen >= a):
		string,addr=s.recvfrom(1024)
		print string
		f=open(string,'wb')
		package.recfile(f,s,addressclient)
		a=a+1
s.close()
		
