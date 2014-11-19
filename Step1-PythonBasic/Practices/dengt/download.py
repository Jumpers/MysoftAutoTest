import os
import sys
import urllib2

def geturl():
    url = raw_input("Give me an url!hurry up! you son of @#$%\n")
    return url

def getfull_path(url):
    file_name = str(url.split("/")[-1])
    dir_path = raw_input("Tell me where you want to put it.\n Give you an example:'c:\\'\n")
    full_path = dir_path + file_name
    return full_path

def getsize(df):
    file_size=int(df.info().getheaders("Content-Length")[0])
    return file_size

def getdf(url):
    df = urllib2.urlopen(url)
    return df

def isdownloaded(full_path,df):
    file_size_dl=0
    block_sz=8192*50
    f=open(full_path,"wb")
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
    
if __name__ == '__main__' :
    url = geturl()
    full_path = getfull_path(url)
    df = getdf(url)
    file_size = getsize(df)
    isdownloaded(full_path,df)
    