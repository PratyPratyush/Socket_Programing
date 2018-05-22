import socket
import time
def send(f,s,adserver,filename):
	flag=0
	while True:
		try:
			if flag==0:
				data = f.read(1024)
			if data=="":
				s.sendto(data,adserver)
				f.close()
				break
			s.sendto(data,adserver)
			flag=0
			print "sending.....Data"
			time.sleep(0.25)
			s.settimeout(25.0)
			ack,addr=s.recvfrom(1024)
		except socket.error:
			print "Retrying....."
			time.sleep(1)
			flag=1
			continue
			
		

def rec(f,s,adclient):
	while True:
		try:
			repacket,addr=s.recvfrom(1024)
			if repacket=="":
				f.close()
				print "REceive File successfully"
				break
			print "writing data"
			f.write(repacket)
			s.sendto('ack',adclient)
		except socket.error:
			print "Retrying"
			continue
