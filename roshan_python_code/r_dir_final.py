import os
from os.path import isfile
import shutil

def fun(s_path,d_path):
	dirlist=os.listdir(s_path)
	dirlen = len(dirlist)
	dirlen=dirlen-1
	arr = []
	while(dirlen > -1):
		if not os.path.isfile(s_path+"/"+dirlist[dirlen]):
			arr.append(s_path+"/"+dirlist[dirlen]);
			os.makedirs(d_path+"/"+dirlist[dirlen])
		else:
			shutil.copy(s_path+"/"+dirlist[dirlen],d_path)			
		dirlen=dirlen-1
	while( len(arr) > 0):
		va = arr.pop()
		head,tail=os.path.split(va)
		fun(va,d_path+"/"+tail)


s_path="/home/praty/Desktop/check"
d_path="/home/praty/Desktop/Dest"
head,tail=os.path.split(s_path)
d_path=d_path+"/"+tail
os.makedirs(d_path)
fun(s_path,d_path)