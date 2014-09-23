# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third, forth = argv

fifth = raw_input("fifth:")
# raw_input 和 argv 的区别：在于用户输入参数的时间不一样
# raw_input（）是在脚本运行过程中需要用户输入的
# argv 是用户执行命令前就要输入参数的值

print "The script is called:", script  # script是脚本，传递的是要执行的脚本的路径和名称
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
# print argv
print "Your forth variable is:", forth

fifth = raw_input("fifth:")
# raw_input 和 argv 的区别：在于用户输入参数的时间不一样
# raw_input（）是在脚本运行过程中需要用户输入的
# argv 是用户执行命令前就要输入参数的值
print fifth

print type(script)
print type(first)
print type(second)
print type(third)
print type(forth)


# 要传参数才能正常运行，否则不论有几个参数都会报错：script, first, second, third = argv
# ValueError: need more than 1 value to unpack

# 传参数的方法一：运行按钮->run configurations->arguments->run arguments栏输入参数->点击run
# 传参数的方法二：在命令行输入cmd->输入Python E:\workspace\MysoftAutoTest\Step1-PythonBasic\Practices\yuxq\12-13\ex13.py 参数值->enter
# 采用命令行时一定要注意是当前脚本的路径及名称！！！
# 采用方法二中Python后面的路径和脚本名称就是传到script的值，采用方法一是默认本脚本的名称及路径
# 如果传入script的值是其他的脚本的路径和名称则执行就是其他的脚本，而不是本脚本

# 在命令行可以输出汉字，用方法二输出的汉字无法显示，这是编辑器的问题
