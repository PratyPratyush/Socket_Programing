from socket import *
import threading

s=socket(AF_INET,SOCK_DGRAM)
s1=socket(AF_INET,SOCK_DGRAM)

host="127.0.0.1"
#shost='192.168.0.5'
#chost='192.168.0.3'
sp=5000
sp1=6000
cp=5001
cp1=6001

s.bind((host,cp))
s1.bind((host,cp1))

class myThread( threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name = name
		
	def run(self):
		#print"Starting Thread",self.name
		fun(self.name)
		print"Exit Thread",self.name
		s.close()
		s1.close()

def fun(name):
	t = 'c'
	while t == 'c':
		if name=="Thread1":
			data,addr=s.recvfrom(1024)	
			print "\n"	
			print data," address - ",addr
		elif name=="Thread2":
			msg=raw_input("Enter message : ")
			s1.sendto(msg,(host,sp1))
		#da,addr=s.recvfrom(1024)
		#t=da
		

thread1 = myThread("Thread1")
thread2 = myThread("Thread2")

thread1.start()
thread2.start()
