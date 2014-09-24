#-*-coding:utf-8-*-
#\t是table键，空两格
tabby_cat = "\tI'm tabbed in."
#\n是用来换行的
persian_cat = "I'm split\non a line."
#\\，在转义字符前加上一个转义字符，输出的是\
backslash_cat = "I'm \\ a \\ cat."
#"""之间的内容赋予了fat_cat这个变量
fat_cat = """
I‘ll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
#在没有输入后面的三个引号时，一直提示错误
"""

#打印后面的变量
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


