#-*-coding:utf-8-*-
#coding=utf-8
import sys 
def cmpList(str1,str2):
    resultlist=[]
    x=0
    len1=len(str1)
    len2=len(str2)
    len=len1 if len1<len2 else len2
    while x<len:
      if str1[x]<str2[x]:
        resultlist=[str1,str2]
        break
      elif str1[x]>str2[x]:
        resultlist=[str2,str1]
        break
      else:
        if x==len-1:
           resultlist=[str1,str2] if str1[x]<str2[x] else [str2,str1]
           break
        else:
           x+=1
           continue


def sort(list):
    list1=list[:]   
    result=[]
    lenlist=0
    if len(list1)<=1:
      result=result+list1
    else:
      while len(list1-1)>0:
       min = list1[0]
       for i in list1:
        result = cmplist(min,list1[i])[0]
       result.append(min)
       if min in list1:
        result.remove(min)
    return result

if __name__  ==  '__main__':
      list=['abc','acc','ase','dc','ab']
      print sort(list)
    



        
      