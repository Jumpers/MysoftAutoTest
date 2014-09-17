#coding=utf-8
fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
fat_cat2="""
I'll do a list2:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print fat_cat
print fat_cat2
print "响铃符：\n","\a"#为什么打印出来的是方格？
print "退格符：\n","hello\bworld"#为什么打印出来的是方格？
print "进纸符（换页符）:\n","hello\fworld"#为什么打印出来的是方格？
print "\N{sdfsdf}"#这个原样输出了，这个符号干啥用的？
print "回车符:\n","hello\rworld"
print "水平制表符：\n","hello\tworld"

#一下2个是什么作用？区别是什么？
print "\uFEDC"
print "\Uffffffff"

print "垂直制表符：\n","hello\vworld"#为什么打印出来的是方格？

print "\o111"
print "\x66"

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r"%i,

