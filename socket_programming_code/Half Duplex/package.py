import socket

#send packet
def send(f,s,addressserver,filename):
	ackfix="0000"
	ackno=0
	ack=111
	retransmit=0
	while True:
		data=f.read(20000)
		#if data is None:
		#	print "End of file"
		#	f.close()
		#	break
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
			print "ACK - ",ack
			ack=ack+1
			s.sendto('ack',addressserver)
		elif receivAck!=ackpacket:
			s.sendto('notack',addressserver)
			send(f,s,addressserver)
			retransmit=retransmit+1
		if not filepacket[4:20000]:
			f.close()
			print "\n"
			print "File successfully Transfer "
			print "File name is : ",filename
			print "size of file is : ",ackno*20000
			print "Segment size : 20004 B"
			print "number of Segment :",ackno
			print "Number of ACK :",ackno
			print "Number of Retransmit packet : 0"
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
				print "Receive packet - ",recpacket[0:4]
				f.write(recpacket[4:20004])
			if not recpacket[4:20004]:
				f.close()
				break
		elif ack=="notack":
			recfile(f,s,addressclient)
	return 'fileover'












	 
