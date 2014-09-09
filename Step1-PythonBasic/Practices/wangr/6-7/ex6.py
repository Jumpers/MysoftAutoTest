# -*- coding: utf-8 -*-
x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)
z = True
a = "I love my home! %r"
b = "I love my home! %s"
c = "I love my home! %d"
                                                                     
print x
print y
print "I said: %r." %x
print "I said: '%r'."
print "I said: '%r'." %x

print "I also said: '%s'." %y
print "I also said: %s," %y

print z 
print x + y
# print x + % z
print a % z
print b % z
print c % z
# print c % binary  z必须是TRUE或FALSE才能成功，其他变量不能成功，为什么？
# a、b、c在赋值时要在最后加上相应的%s等，后面的那个变量就是当做参数传到这个里面来

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
print joke_evaluation 

w = "This is the left side of ..."
e = "a string with a right side."

print w + e