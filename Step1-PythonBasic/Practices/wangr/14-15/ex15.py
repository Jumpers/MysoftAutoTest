# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv
# 这里传入的文件名字必须是相应目录下文件的名字

# script, ex15_sample.txt = argv
# 报错：NameError: name 'ex15_sample' is not defined

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")
# 为什么 这里输入的文件名字必须是放在相应目录下的文件名字？不可以重新输入其他名字？
# 在相应目录下再放一个其他的文件，写这个文件的名字也不行，为什么？
 
txt_again = open(file_again)
  
print txt_again.read()
 
