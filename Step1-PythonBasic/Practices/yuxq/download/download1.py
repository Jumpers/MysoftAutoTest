import urllib2
print "downloading with urllib2"
url='http://xiazai.xiazaiba.com/Phone/Z/zhixing_2.1.8_XiaZaiBa.apk'
f=urllib2.urlopen(url)
data=f.read()
code=open('F://zhixing_2.1.8_XiaZaiBa.apk','wb')
code.write(data)
