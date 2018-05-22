import socket
def send(f,s,adserver,filename):
	flag = 0
	while True:
		if flag == 0:
			data = f.read(20000)
		if data=="":
			s.sendto(data,adserver)
			f.close()
			break
		s.sendto(data,adserver)
		flag = 0
		try:
			s.settimeout(5)
			ack,addr=s.recvfrom(1024)
			break
		except socket.error,exc:
			print "Eception -----",exc
			print "resend packet"
			flag = 1
			continue
			
		

def rec(f,s,adclient):
	flag = 0
	while True:
		repacket,addr=s.recvfrom(20000)
		if flag==0:
			print "flag ----- ",flag
			flag=1
		else:
			s.sendto('ack',adclient)
			flag=1
		if repacket=="":
			f.close()
			break
		if flag==1:
			print "writing data"
			f.write(repacket)
