#coding=utf-8
i=0 #统计回答正确的个数
j=0 #统计回答错误的个数

a1=(True and True)
b1=input("'True and True' is (True or False):")
if a1==b1:
    print "YES,you are right!"
    i+=1
else:
    print "NO,'True and True' is %r" % a1
    j+=1

a2=(False and True )
b2=input("'False and True' is (1 or 0):")
if (b2==1)==a2:
    print "YES,you are right!"
    i+=1
else:
    print "NO,'False and True' is %r" % a2
    j+=1


1 == 1 and 2 == 1 
"test" == "test" 
1 == 1 or 2 != 1 
True and 1 == 1 
False and 0 != 0 
True or 1 == 1 
"test" == "testing" 
1 != 0 and 2 == 1 
"test" != "testing" 
"test" == 1 
not (True and False) 
not (1 == 1 and 0 != 1) 
not (10 == 1 or 1000 == 1000) 
not (1 != 10 or 3 == 4) 
not ("testing" == "testing" and "Zed" == "Cool Guy") 
1 == 1 and not ("testing" == 1 or 1 == 0) 
"chunky" == "bacon" and not (3 == 4 or 3 == 3) 
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") 