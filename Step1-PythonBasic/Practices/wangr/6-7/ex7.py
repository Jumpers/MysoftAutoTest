# -*- coding: utf-8 -*-
s = 'snow'

print "Mary had a little lamb."
print "Its fleece was white as %s." %'snow'
print "Its fleece was white as %s." %s
print "Its fleece was white as %r." %'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd' that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = '''r'''
end10 = "g"
end11 = "e"
end12 = 'r'

# watch that comma at the end. try removing it to see what happens
print end1,end2+end3+end4+end5+end6,
print end7+end8+end9+end10+end11+end12
print end1,
print end2,
print end3,
# 最后一个print后面加不加逗号都不会打印出逗号 没影响

# print end1，print end2   # 报错 ：invalid syntax ---无效的语法
# print a,
# print b
# 这样打印出来就不会换行了，中间有一个空格，不能直接在逗号后面写print，还换行再写，这样打印就是在同一行