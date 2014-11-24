#-*-coding:utf-8-*-
#引入参数包
from sys import argv
#赋值
script, user_name = argv
#这个不知道是干嘛的
prompt = '>'
#打印两个传入的两个参数
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
#手动输入值raw_input和argv有什么不同raw_input是在运行时输入，而argv是在运行前输入
likes = raw_input(prompt)
#raw_input的用法是怎样的？
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)



