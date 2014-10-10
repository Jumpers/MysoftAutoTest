#运行错误，需要查找资料
filename=raw_input("filename:")
txt=open(filename,'w+')
txt.write('line1''\n''line2''\n''line3''\n')
print txt.read()
txt.close()
