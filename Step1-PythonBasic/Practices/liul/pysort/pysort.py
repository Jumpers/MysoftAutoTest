#-*-coding:utf-8-*-
import os 
import sys 
import urllib2
#从文件中读取字符串
def getString():
            #f = open(r'test.txt','w+')
            #s = raw_input("please input your string:")
            #print s
            #f.write(s)
            #f.close()
            f = open('test.txt','r')
            str_list = f.readlines()
            return str_list
    
#主函数
if __name__ == '__main__': 
     str_list = getString(); #获取string
     print "list:%r" % str_list
     str_list.sort()
     print "sorted list:%r" % str_list
     