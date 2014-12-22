#-*-coding:utf-8-*-
import sys
def cmpList(str1,str2,order='Asce'):
    '''
    1.比较两个字符串的大小，并根据排序顺序进行排序；
    2.返回一个根据排序顺序进行排序的序列；
    '''
    resultList=[]
    if order=='Asce':
        x=0
        len1=len(str1)
        len2=len(str2)
        loopNum=len1 if len1<len2 else len2
        while x < loopNum:
            if str1[x]<str2[x]:
                resultList=[str1,str2]
                break
            elif str1[x]>str2[x]:
                resultList=[str2,str1]
                break
            else:
                if x==loopNum-1:
                    resultList=[str1,str2] if len(str1)<len(str2) else [str2,str1]
                    break
                else:
                    x+=1
                    continue
    elif order=='Desc':
        x=0
        len1=len(str1)
        len2=len(str2)
        loopNum=len1 if len1<len2 else len2
        while x < loopNum:
            if str1[x]>str2[x]:
                resultList=[str1,str2]
                break
            elif str1[x]<str2[x]:
                resultList=[str2,str1]
                break
            else:
                if x==loopNum-1:
                    resultList=[str1,str2] if len(str1)>len(str2) else [str2,str1]
                    break
                else:
                    x+=1
                    continue                
    return resultList

def sort(list1,order='Asec'):
    list2=list1[:]
    resultList=[]
    tempLoop=0
    if len(list2)<=1:
        resultList=resultList+list2
    else:
        if order=='Asce':
            while len(list2)-1>0:
                min=list2[0]
                for x in range(len(list2)-1):
                    min=cmpList(min, list2[x+1], order)[0]
                resultList.append(min)
                if min in list2:
                    list2.remove(min)
            if len(list2)==1:
                resultList.append(list2[0])
                
        elif order=='Desc':
            while len(list2)-1>0:
                max=list2[0]
                for x in range(len(list2)-1):
                    max=cmpList(max, list2[x+1], order)[0]
                resultList.append(max)
                if max in list2:
                    list2.remove(max)
            if len(list2)==1:
                resultList.append(list2[0])
        else:
            print 'the order parameter is not vaild.'
            sys.exit()
    return resultList

if __name__=='__main__':
    list2=['1a','aa','b2','bb','c!c','c']
    print sort(list2,'Asce')
    print sort(list2,'Desb')


