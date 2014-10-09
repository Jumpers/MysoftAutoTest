#coding=utf-8
from sys import argv
script,filename=argv#传入的文件名称必须是文件的完成路径
txt=open(filename)
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again=raw_input(">")#传入的文件名称必须是文件的完成路径
txt_again=open(file_again)
print txt_again.read()

