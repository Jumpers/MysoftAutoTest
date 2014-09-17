# -*- coding: utf-8 -*-
# 
# formatter = "%r %r %r %r"
# 
# print formatter % (1,2,3,4)
# print formatter % ("one","two","three","four")
# print formatter % (True,False,False,True)
# print formatter % ("True",'False','''False''',True)
# # true 和  false 加不加引号都是输出原样，有什么区别呢？
# print formatter % (formatter,formatter,formatter,formatter)
# print formatter % (
#                     "I had this thing.",
#                     "That you could type up right.",
#                     "But it didn't sing.",
#                     "So I said goodnight."
#                     )

# print "I said:\"say hello to uncle\"to my son"  # 前后的双引号都要转义
# print """I said:\"say hello to uncle"to my son"""  #只用转义前面的双引号
# # 注意一个双引号与三个双引号中对双引号的转义区别：
# 
# 
# print "I said:'say hello to uncle'to my son"
# 
# print 'I said:\'''say hello to uncle\'''to my son'
# 
# print 'I said:\'say hello to uncle\'to my son' # 前后的双引号都要转义
# print '''I said:\'say hello to uncle'to my son''' #只用转义前面的双引号
# # 注意一个双引号与三个双引号中对双引号的转义区别：
# 
# print 'I said:"say hello to uncle"to my son'
# print 'I said:\"say hello to uncle"to my son'
 