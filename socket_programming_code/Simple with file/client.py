import socket
import package
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500

s.bind((host,pc))
addressserver=(host,ps)

terminate="start"


while terminate!="exit":
		fileName=raw_input("Enter file name :")
		f=open(fileName,'rb')
		package.send(f,s,addressserver,fileName)
		print "you want to continue = c or exit = exit "
		string = raw_input()
		s.sendto(string,(host,ps))
		terminate=string
s.close()
	
