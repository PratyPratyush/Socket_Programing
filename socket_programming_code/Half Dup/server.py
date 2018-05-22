import socket
import package

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500

s.bind((host,ps))
addressclient=(host,pc)


terminate="sdf"

print 'you want to send = s and receive = r'
check=raw_input()

if check=='r':
	s.sendto('s',(host,pc))
else:
	s.sendto('r',(addressclient))


while terminate!="exit":
	if check=='r':
		f=open('rfile','wb')
		package.recfile(f,s,addressclient)
	elif check=='s':
		fileName=raw_input("Enter file name :")
		f=open(fileName,'rb')
		package.send(f,s,addressclient)
	elif check=='exit':
		terminate="exit"
		
	
	check,add=s.recvfrom(10)
s.close()
	

