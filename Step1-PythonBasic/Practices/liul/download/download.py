#-*-coding:utf-8-*-
import os 
import sys 
import urllib2 
#����url
def getUrl():
    while True:
        try:
            url = raw_input("please input your url:")
            if url != r'http://www.baidu.com/img/bdlogo.png':#urlΪ�յ�������˳�
                print "���Ϸ������룡"    
        except IndexError ,e :
            #if url != r'http://www.baidu.com/img/bdlogo.png':#urlΪ�յ�������˳�
            #print "���Ϸ������룡"
            break
        return url

#���뱣��Ŀ¼    
def getDest():
    dir_path = raw_input("please input your destation to store:")
    if not (os.path.exists(dir_path)):#���Ŀ¼������
        return r"d:\\"
    return dir_path


#����ҳ��ȡ����
def getDF(url):
    df = urllib2.urlopen(url)
    return df


#��ȡ�ߴ�
def getSize(df):
    file_size = int(df.info().getheaders("Content-Length")[0])
    if(file_size >1024*1024 ):
        print "�ռ䲻��"
    return file_size

#��ȡ����,����url�����һ��/������
def getName(url,df): 
    try:
        file_name=(str(df.info().getheaders("Content-Disposition")[0])).split('"')[1] 
    except IndexError ,e : 
         file_name=str(url.split('/')[-1]) 
    return file_name 
 
#�����ļ�
def downloadFiles(full_path,df): 
     file_size_dl=0 
     block_sz=8192*50 
     f=open(full_path,'wb') 
     while True: 
         buffer = df.read(block_sz) 
         if not buffer: 
             break 
         file_size_dl += len(buffer) #�ļ���СΪ��λ������Ĵ�С֮��
         f.write(buffer) 
         status = r"%10d [%3.2f%%]" %(file_size_dl,file_size_dl*100.0/file_size) #��ʾ���ؽ���
         status = status+chr(8)*(len(status)+1) #
         print status, 
     f.close() 
     print "Got files dist file data %s" % file_size_dl 
 
#������
if __name__ == '__main__': 
     url = getUrl(); #��ȡurl��ַ
     print "url:%r" % url
     df = getDF(url); #��ȡurl��ҳ����
     dir_path = getDest(); #�������л�ȡ����Ŀ¼
     print "dir_path:%r" % dir_path 
     file_size = getSize(df); #��ȡ�ļ��ߴ�
     file_name = getName(url,df); #��ȡ�ļ�����
     full_path = dir_path+file_name; #��ȡ�ļ�����·�����ļ�����
     downloadFiles(full_path,df); #�����ļ�

    
 

