import socket

#send packet
def send(f,s,addressserver):
	ackfix="0000"
	ackno=0
	while True:
		data=f.read(20000)
		ackno=ackno+1
		acknos=str(ackno)
		acknol=len(acknos)
		pos=len(ackfix)-acknol
		ackpacket=ackfix[0:pos]+acknos
		filepacket=ackpacket+data
		print "packet    "+acknos+"   sent "
		s.sendto(filepacket,addressserver)
		receivAck,addr=s.recvfrom(10)
		if receivAck==ackpacket:
			s.sendto('ack',addressserver)
		elif receivAck!=ackpacket:
			s.sendto('notack',addressserver)
			send(f,s,addressserver)
		if not filepacket[4:20000]:
			f.close()
			break
	return "fileover"

#receive packet
def recfile(f,s,addressclient):
	while True:
		recpacket,address=s.recvfrom(20004)
		s.sendto(recpacket[0:4],addressclient)
		ack,address=s.recvfrom(10)
		if ack=="ack":
			if recpacket[4:20004]:
				f.write(recpacket[4:20004])
			if not recpacket[4:20004]:
				f.close()
				break
		elif ack=="notack":
			recfile(f,s,addressclient)
	return 'fileover'












	 
