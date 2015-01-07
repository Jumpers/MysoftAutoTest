#coding=utf-8
def compare_str(str1,str2):#比较2个字符串的大小
    #判断并比较2个西字符串的长度，len_min为最短字符串的长度，str_longer为最长字符串的值
    len1=len(str1)
    len2=len(str2)
    if len1<=len2:
        len_min=len1
        str_longer=str2
        str_shorter=str1
    elif len1>len2:
        len_min=len2
        str_longer=str1
        str_shorter=str2
    else:
        len_min=len1
        str_longer=str2
        str_shorter=str1
    #比较2个字符串的大小    
    for i in range(0,len_min):
        if str1[i]<str2[i]:
            min=str1
            max=str2
            return(min,max)
        elif str1[i]>str2[i]:
            min=str2
            max=str1
            return(min,max)
        elif str1[i]==str2[i] and i==len_min-1:
            min=str_shorter
            max=str_longer
            return(min,max)
                    
def compare_list(list):#对列表的字符串进行排序
    paixu_list=list[:]#分片赋值
    len_list=len(paixu_list)
    for i in range(len_list,1,-1):
        for j in range(0,i-1):
            paixu_list[j],paixu_list[j+1]=compare_str(paixu_list[j],paixu_list[j+1])
    return paixu_list

def start():
    #键盘输入序列，输入*为结束输入操作
    list=[]
    t=raw_input('>')
    while t!='*':
        list.append(t)
        t=raw_input('>')

    print r'排序后的序列是:', compare_list(list)
    print r'原始序列是:', list

while input(r"是否开始使用该排序？输入1开始使用，输入0结束:"):
    start()
            