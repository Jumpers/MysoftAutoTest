#ex10.py
# -*- coding: utf-8 -*-

print 'b\ab'
print 'a\ba'
print 'a\na'
print 'c\fc'
print 'd\rd'
print 'e\te'
print '\uf'
print "/","-","|","\\","|"

#好看的循环
j=1
while j <=10:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
        j = j + 1
print j


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat2

#格式化字符与转义序列合用

n = '\n'
nn = '\\n'
t = '\t'
tt = '\\t'
haha='\''


say = 'I%sm %s%s\t%r'% (haha,nn,n,n)
print say



