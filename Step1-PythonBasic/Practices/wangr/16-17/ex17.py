# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists
from copy123 import copy_two

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

copy_two(from_file, to_file)

# # wo could do these two on one line too,how?
# in_file = open(from_file)
# indate = in_file.read()
# 
# print "The input file is %d bytes long" % len(indate)
# 
# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()
# 
# out_file = open(to_file,'w')
# out_file.write(indate)
# 
# print "Alright, all done."
# out_file.close()
# in_file.close()