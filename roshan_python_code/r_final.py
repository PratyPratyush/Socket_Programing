import os
from os.path import isfile

def fun(path):
	print "This is Folder path : "+path
	dirlist=os.listdir(path)
	dirlen = len(dirlist)
	dirlen=dirlen-1
	arr = []
	while(dirlen > -1):
		if not os.path.isfile(path+"/"+dirlist[dirlen]):
			arr.append(path+"/"+dirlist[dirlen]);
		else:
			print "File name : "+dirlist[dirlen]
			statinfo=os.stat(path+"/"+dirlist[dirlen])
			print "File Size : "+str(statinfo.st_size)
			if statinfo.st_size == 0:
				os.remove(path+"/"+dirlist[dirlen])
				print "Removed File Name : "+dirlist[dirlen]
		dirlen=dirlen-1
	while( len(arr) > 0):
		fun(arr.pop(0))
	return



path="/home/praty/Desktop/File"
fun(path)