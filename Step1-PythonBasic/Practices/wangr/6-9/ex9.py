# -*- coding: utf-8 -*-

# Here's some new strange stuff,remeber type is exactly.

# a = "10"
# a1 = "Hello"
# b = 10.0
# b1 = "10.0"
# 
# c = int(a)
# # c1 = int(a1)  报错；invalid literal for int() with base 10: 'Hello'
# c2 = int(b)
# # c3 = int(b1) 报错：invalid literal for int() with base 10: '10.0'
# 
# d = eval(a)
# # d1 = eval(a1) 报错 ：name 'Hello' is not defined
# # d2 = eval(b) 报错：eval() arg 1 must be a string or code object
# d3 = eval(b1)
# 
# # print "a is :",type(a)
# # print "b is ",type(a1)
# # print "a1 is ",type(b)
# # 
# # print a
# # print a1
# # print b
# 
# print "a and its type :%r %r" %(a,type(a))
# print "a1 and its type:%r %r" %(a1,type(a1))
# print "b and its type :%r %r" %(b,type(b))
# print "b1 and its type:%r %r" %(b1,type(b1))
# # print type(c)
# # # print type(c1)
# # print type(c2)
# 
# # print type(d)
# # # print type(d1)
# # # print type(d2)
# 
# print "c and its type :%r %r " %(c,type(c))
# print "c2 and its type:%r %r" %(c2,type(c2))
# 
# print "d and its type :%r %r " %(d,type(d))
# print "d3 and its type:%r %r" %(d3,type(d3))

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\n\nMar\nApr\nMay\"\n\tJun\nJul\nAug\n\\"
 
print "Here are the days: " ,days
print "Here are the months: " ,months
#之前的输出是%变量名，这里没有加%，与那种输出有什么区别？
print "Here are %r the days." % days
print "Here are : the days ",days
print "%r are %r the days." %(days,days)
print ":Here are : the days " ,days
print ":Here are : the days " ,days,days,days,months
 
print """
\"There's something going on here."
\'With the three double-quotes.'
\\We'll be able to type as much as wo like.\
Even 4 lines if wo want 4,or 5, or 6.
"""
# # 在后面加个\打印出来在同一行
# # 在末尾加\t就是两行展示的
print '''aaa\
bbb'''

print '''
\\yy\
kkkk
'''
print '''
\\yy\
\\\\
kkkk
'''