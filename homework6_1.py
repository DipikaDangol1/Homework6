import os
import sys

path=sys.argv[1]
if os.path.exists(path):
	print ("true")
	#file exists
else:
	print("False")
