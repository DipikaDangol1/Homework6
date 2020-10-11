import os
import sys

path=sys.argv[1]
if os.path.exists(path):
	print ("true")
	#file exists
else:
	print("False")
monitor_path="C:\Python\Homework6\Test1.txt"
isFile=os.path.isfile(monitor_path)
print(isFile)
