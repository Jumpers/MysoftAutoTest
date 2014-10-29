import os
import sys
import urllib2

url=r"http://xiazai.xiazaiba.com/Phone/Z/zhixing_2.1.8_XiaZaiBa.apk"
df=urllib2.urlopen(url)
file_size=int(df.info().getheaders("Content-Length")[0])
#file_name=(str(df.info().getheaders("Content-Disposition")[0])).split('"')[1]
file_name=str(url.split("/")[-1])
file_size_dl=0
block_sz=8192*50
dir_path=r"c:\\"
full_path=dir_path+file_name
f=open(full_path,'wb')
while True:
	buffer = df.read(block_sz)
	if not buffer:
		break
	file_size_dl+=len(buffer)
	f.write(buffer)
	status=r"%10d [%3.2f%%]" %(file_size_dl,file_size_dl*100.0/file_size)
	status=status+chr(8)*(len(status)+1)
	print status,
f.close()
print "Got files dist file data %s" % file_size_dl