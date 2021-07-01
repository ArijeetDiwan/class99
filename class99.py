import os
#os.getcwd()

#os.mkdir("d:/python/Class 99/MyFolder")
#os.mkdir("./MySecondFolder")

#os.chdir("d:/python/Class 99/MySecondFolder/") 
#need to check chdir
os.chdir("C:\\")
pr=os.getcwd()
print(pr)
#os.rmdir("d:/python/Class 99/MySecondFolder")



#List Files and Sub-directories
import os 
pq=os.listdir("d:\python")
#need to check listdir
print(pq)

import shutil

f=open('D:/python/Class99/class99.txt','r')
f1=open('D:/python/Class99/Class99btackup.xt','w')

# Syntax: shutil.copyfileobj(src,dst)
shutil.copyfileobj(f,f1)

f.close()
f1.close()