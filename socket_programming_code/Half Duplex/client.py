import socket
import package
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500

s.bind((host,pc))
addressserver=(host,ps)

terminate="start"
check,add=s.recvfrom(10)
print check



while terminate!="exit":
	if check=='s':
		fileName=raw_input("Enter file name :")
		f=open(fileName,'rb')
		package.send(f,s,addressserver,fileName)
	elif check=='r':
		f=open('rserver','wb')
		package.recfile(f,s,addressserver)

	print "You wnat to send = s or receive = r or for exit = exit"
	check=raw_input()
	if check=='r':
		s.sendto("s",addressserver)
	elif check=='s':
		s.sendto("r",addressserver)
	elif check=='exit':
		terminate="exit"
		s.sendto("exit",addressserver)
s.close()


