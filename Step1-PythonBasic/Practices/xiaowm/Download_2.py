import os
import sys
import urllib2
#url=r"http://xiazai.xiazaiba.com/Phone/Z/zhixing_2.1.8_XiaZaiBa.apk"
#df=urllib2.urlopen(url)
#file_size=int(df.info().getheaders("Content-Length")[0])
# try:
#   file_name=(str(df.info().getheaders("Content-Disposition")[0])).split('"')[1]
# except IndexError ,e :
#   file_name=str(url.split('/')[-1])
def getUrl():
	while True:
		url=raw_input("Pls input your url.")
		if url != None:
			break
	return url

def getDest():
	dir_path=raw_input("Pls input your destanation to store.")
	if dir_path == "":
		dir_path=r"c:\\"
	return dir_path

def getDF(url):
	df=urllib2.urlopen(url)
	return df

def getSize(df):
	file_size=int(df.info().getheaders("Content-Length")[0])
	return file_size


def getName(url,df):
	try:
		file_name=(str(df.info().getheaders("Content-Disposition")[0])).split('"')[1]
	except IndexError ,e :
		file_name=str(url.split('/')[-1])
	return file_name

def downloadFiles(full_path,df):
	file_size_dl=0
	block_sz=8192*50
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

if __name__ == '__main__':
	url=getUrl();
	df=getDF(url);
	dir_path=getDest();
	#print "dir_path is %s" % dir_path
	file_size=getSize(df);
	file_name=getName(url,df);
	full_path = dir_path+file_name;
	downloadFiles(full_path,df);
