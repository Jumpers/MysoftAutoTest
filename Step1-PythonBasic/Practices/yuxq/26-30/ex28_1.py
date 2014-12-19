#coding=utf-8
i=0 #统计回答正确的个数
def Boolean_expressions_to_determine(expressions):
#1表示 True，0表示False
    k=0
    c=expressions
    a=eval(expressions) #将字符串转换成表达式
    b=input("%r is (1 or 0):" %c )
    if b== a:
        print "YES,you are right!"
        k+=1
    elif (b!=0) and (b!=1):
        k="break"
    else:
        if a==True:
            a=1
        elif a==False:
            a=0
        print "NO,%r is: %r" %(c,a)
    return k
        
tlist=["True and True","False and True","1 == 1 and 2 == 1",
       "'test' == 'test'","1 == 1 or 2 != 1","True and 1 == 1",
       "False and 0 != 0","True or 1 == 1",'"test" == "testing"',
       "1 != 0 and 2 == 1",'"test" != "testing"','"test" == 1',
       "not (True and False)","not (1 == 1 and 0 != 1)","not (10 == 1 or 1000 == 1000)",
       "not (1 != 10 or 3 == 4)",'not ("testing" == "testing" and "Zed" == "Cool Guy")',
       '1 == 1 and not ("testing" == 1 or 1 == 0)','"chunky" == "bacon" and not (3 == 4 or 3 == 3)',
       '3 == 3 and not ("testing" == "testing" or "Python" == "Fun")']
for t in tlist:
    j=Boolean_expressions_to_determine(t)
    if j=="break":
        break
    else:
        i+=j
print "total is %r,Right %r" %(len(tlist),i)
