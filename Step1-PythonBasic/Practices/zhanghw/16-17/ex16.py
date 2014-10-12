#ex16.py
# -*- coding:utf-8 -*-

from sys import argv
import os

#获取文件名

#script, filename = argv
#filename = raw_input('filename>>>>')
filename = r'd:\aa.txt'

#打印文件原始内容 
print "We're going to erase %r." % filename

#询问
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."

#打印做截断前操作前的文件内容 
target = open(filename, 'r')
print "truncate befor:\n%s" % target.read()
print "Truncating the file. Goodbye!"
target = open(filename, 'w+')

#截断
target.truncate()

#打印截断操作后的文件内容
print "truncate after:\n%s" % target.read()

#获取输入 
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."

#写入输入内容
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

#合并写入
line = line1 +"\n" + line2+"\n" + line3+"\n" 
#line = line1 + line2 + line3 
target.write(line)

print "And finally, we close it."
target.close() # 如果此处不做close，下面不进行重新打开而是直接read之后再close，就会得出一串乱七八糟的字符 ,why?

#打印出写入操作后的文件内容
target = open(filename, 'r')
print 'write after \n' + target.read()
#close
target.close()

#readline()  readlines()
