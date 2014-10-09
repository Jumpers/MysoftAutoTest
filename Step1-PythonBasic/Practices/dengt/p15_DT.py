#coding=utf-8
from sys import argv#引入包中的方法

script, filename = argv#在运行之前为filename其赋值

txt = open(filename)#将建立好的文件名赋值给变量txt

print "Here's your file %r:" % filename
print txt.read()#打开运行之前就创建好的文件，并读取里面的内容

print "Type the filename again:"
file_again = raw_input(">")#捕获键入的文件名

txt_again = open(file_again)#open方法是将文件转换成一个对象赋值给变量txt_again

print txt_again.read()#读取文件内容

