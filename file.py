import os
import sys


fileobj = open(sys.argv[1])
filecontents = fileobj.readlines()

print filecontents

fileobj.close()
