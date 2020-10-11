#prompt user to enter the start path and file name, search recursively for the given
#file name starting at the given path, when file is found, display the full path to the file. 

import os

def search(filename):
	startpath='C:\\Users'
	for root, dirs, files in os.walk(startpath):
		if filename in files:
			print(root,filename)
	print("Done!!!")
	input()
try:
	name=input("filename:")
	search(name)
except:
	print("Error")


