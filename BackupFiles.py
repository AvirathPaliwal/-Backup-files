import os
import shutil

src = input('Enter Your Source Folder  :  ')
dest = input('Enter Your Destenation  :  ')

src = src + '/'
dest = dest + '/'

filelist= os.listdir(src)

for files in filelist:
    shutil.move(src+files,dest)
