from socket import *
import threading

s=socket(AF_INET,SOCK_DGRAM)
s1=socket(AF_INET,SOCK_DGRAM)

host="127.0.0.1"
#shost='192.16.0.2'
#chost='192.168.0.3'
sp=5000
sp1=6000
cp=5001
cp1=6001

s.bind((host,sp))
s1.bind((host,sp1))

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
	t= 'c'
	while t == 'c':
		if name=="Thread1":
			msg=raw_input("Enter message  :")
			s.sendto(msg,(host,cp))		
		elif name=="Thread2":
			data,addr=s1.recvfrom(1024)
			print "\n"
			print data,"address is ",addr
		#print "you want to continue = c or exit = exit"
		#d = raw_input()
		#s.sendto(d,(host,cp))
		#t = d

thread1 = myThread("Thread1")
thread2 = myThread("Thread2")

thread1.start()
thread2.start()
