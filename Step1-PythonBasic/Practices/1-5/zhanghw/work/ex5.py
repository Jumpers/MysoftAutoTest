# ex5.py
# -*- coding: utf-8 -*-
# %d %s %r %f %x

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)

print('输出浮点数字：%f'%0.005)
print('输出百分比数字：%f%%'%10.8)

#%r %s 的区别
#%r--不管什么都打印出来，比如如下字符 ，会把str1中的单引号作为字符打印出来 
str1 = 'ab'

print '%r'%str1 
print '%s'%str1