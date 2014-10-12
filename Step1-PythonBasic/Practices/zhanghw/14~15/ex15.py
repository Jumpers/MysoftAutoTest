#ex15.py
# -*- coding:utf-8 -*-


#from sys import argv
#script, filename = argv

import os

#filename = raw_input('filename>>>>')
filename = r'd:\aa.txt'
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()


#输入

filetext =  raw_input('filetext>>>')  
#写入
txt = open(filename,'a')
txt.write(filetext)
txt.close()


#展示 
txt = open(filename)
print "new text:"+txt.read()
