import socket
import package

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500

s.bind((host,ps))
addressclient=(host,pc)


terminate="sdf"
a=1
while terminate!="exit":
		string = "rfile"+str(a)
		f=open(string,'wb')
		package.recfile(f,s,addressclient)
		data,addr=s.recvfrom(1024)
		terminate=data
		a=a+1
s.close()
		
