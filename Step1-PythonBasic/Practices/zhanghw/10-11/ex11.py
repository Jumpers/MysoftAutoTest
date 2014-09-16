#ex11.py
# -*- coding: utf-8 -*-

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
#weight = raw_input()
weight = input()
print "So, you're %r old, %r tall and %r heavy.\n" % (
age, height, weight)
 


#先输入数字查看允许结果，再输入字符查看运行结果

i = 'T'
while i == 'T':
    raw_input_A = raw_input("raw_input: ")
    input_B = input("Input: ")
    type_A = type(raw_input_A)
    type_B = type(input_B)
    print 'type_A: %s \n type_B:%s'% (type_A,type_B)
    i = raw_input('结束输入任意字符结束输入，继续请输入\'T\'字符:')

else:
    print '\n输入结束 ！'

