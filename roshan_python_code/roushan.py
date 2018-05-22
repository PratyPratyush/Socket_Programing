import os
from os.path import isfile, join
import shutil

def fun(s_path,d_path):
	# if  os.path.exists(s_path):
	# 	head,tail=os.path.split(s_path)
	# 	d_path=d_path+"/"+tail
	# 	os.makedirs(d_path)
	# else:
	# 	print "Path not exist"
	# print "This is Folder path : "+path
	dirlist=os.listdir(s_path)
	dirlen = len(dirlist)
	dirlen=dirlen-1
	arr = []
	while(dirlen > -1):
		if not os.path.isfile(s_path+"/"+dirlist[dirlen]):
			# pat_name=s_path+"/"+dirlist[dirlen]
			arr.append(s_path+"/"+dirlist[dirlen]);
			os.makedirs(d_path+"/"+dirlist[dirlen])
		else:
			shutil.copy(s_path+"/"+dirlist[dirlen],d_path)			
			# print "File name : "+dirlist[dirlen]
			# statinfo=os.stat(path+"/"+dirlist[dirlen])
			# print "File Size : "+str(statinfo.st_size)
			# if statinfo.st_size == 0:
			# 	os.remove(path+"/"+dirlist[dirlen])
			# 	print "Removed File Name : "+dirlist[dirlen]
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





# value="this/jjk"+"/"+"abc"
# print value


# s_path="/home/praty/Desktop/check"
# d_path="/home/praty/Desktop/Dest"
# head ,tail=os.path.split(s_path)
# # os.makedirs(d_path+"/"+tail)
# print tail
# if os.path.exists(s_path):
# 	print "path exist"
















# shutil.copy(s_path,d_path)
# distutils.dir_util.copy_tree(s_path,d_path)

# path="/home/praty/Desktop/check/test.png"
# statinfo=os.stat(path)
# print statinfo.st_size
# if statinfo.st_size == 0:
# 	print "file size is zero"
# 	os.remove(path)
# 	print "file is deleted"
# path=raw_input("Enter path os file")
# path="/home/praty/Desktop/BlueOptima"
# dirlist=os.listdir(path)
# dirlen = len(dirlist)
# print dirlen
# arr = []
# # dirlen=dirlen-1
# i=0
# while (i < dirlen):
# 	print dirlist[i]
# 	arr.append(path+dirlist[i])
# 	i=i+1
# print arr.pop(-1)
# print arr.pop(0)
# print arr.pop(0)
# print dirlist[1]
# if not os.path.isfile(join(path,dirlist[1])):
#  	print "this is directory : "+dirlist[1]
#  	# print dirlist[1]
# else:
# 	print "else part this is file :"+dirlist[1]
# arr1 = []
# arr1.append("hi")
# l = len(arr1)
# print l
# print arr1.pop(0)
# l=len(arr1)
# print l
# if 
# =================================
# if os.path.isfile(join(path,dirlist[8])):
# 	print "this is file"
# if os.path.isfile(path+dirlist[0]):
# 	print "this is file"
# =======================================


# arr.append(path+dirlist[1])
# print arr[0]
# print arr[1]