import socket
import package
import os
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
ps=55000
pc=55500

s.bind((host,pc))
addressserver=(host,ps)
foldername=raw_input("Enter folder name")
dirlist = os.listdir(foldername)

dirlen = len(dirlist)
s.sendto(str(dirlen),(host,ps))
#os.chdir('./'+foldername)
os.chdir(foldername)
i=1
j=0
while (dirlen >= i):
	s.sendto(dirlist[j],(host,ps))
	f=open(dirlist[j],'rb')
	package.send(f,s,addressserver,str(dirlist[j]))
	i=i+1
	j=j+1
	
s.close()
	
