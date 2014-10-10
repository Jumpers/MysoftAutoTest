from sys import argv

script,filename=argv

aread=open(filename)

print aread.read()

aread.close()