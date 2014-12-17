#-*-coding:utf-8-*-
import os 
import sys 
import urllib2 
#输入url
def getUrl():
    while True:
        try:
            url = raw_input("please input your url:")
            if url != r'http://www.baidu.com/img/bdlogo.png':#url为空的情况下退出
                print "不合法的输入！"    
        except IndexError ,e :
            #if url != r'http://www.baidu.com/img/bdlogo.png':#url为空的情况下退出
            #print "不合法的输入！"
            break
        return url

#输入保存目录    
def getDest():
    dir_path = raw_input("please input your destation to store:")
    if not (os.path.exists(dir_path)):#如果目录不存在
        return r"d:\\"
    return dir_path


#打开网页获取内容
def getDF(url):
    df = urllib2.urlopen(url)
    return df


#获取尺寸
def getSize(df):
    file_size = int(df.info().getheaders("Content-Length")[0])
    if(file_size >1024*1024 ):
        print "空间不足"
    return file_size

#获取名字,返回url中最后一个/的名字
def getName(url,df): 
    try:
        file_name=(str(df.info().getheaders("Content-Disposition")[0])).split('"')[1] 
    except IndexError ,e : 
         file_name=str(url.split('/')[-1]) 
    return file_name 
 
#下载文件
def downloadFiles(full_path,df): 
     file_size_dl=0 
     block_sz=8192*50 
     f=open(full_path,'wb') 
     while True: 
         buffer = df.read(block_sz) 
         if not buffer: 
             break 
         file_size_dl += len(buffer) #文件大小为多次缓存区的大小之和
         f.write(buffer) 
         status = r"%10d [%3.2f%%]" %(file_size_dl,file_size_dl*100.0/file_size) #显示下载进度
         status = status+chr(8)*(len(status)+1) #
         print status, 
     f.close() 
     print "Got files dist file data %s" % file_size_dl 
 
#主函数
if __name__ == '__main__': 
     url = getUrl(); #获取url地址
     print "url:%r" % url
     df = getDF(url); #获取url网页内容
     dir_path = getDest(); #从命令行获取保存目录
     print "dir_path:%r" % dir_path 
     file_size = getSize(df); #获取文件尺寸
     file_name = getName(url,df); #获取文件名称
     full_path = dir_path+file_name; #获取文件保存路径及文件名称
     downloadFiles(full_path,df); #下载文件

    
 

