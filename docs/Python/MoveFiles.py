##moves files from one folder to another folder

import os
import shutil

a = "C:/Users/Desktop/FOLDERA/" #Source Folder
b = "C:/Users/Desktop/FOLDERB/" #Destination Folder


def move(src, dest):
     files = os.listdir(src)
     y = 0
     for x, i in enumerate(files):
          shutil.move(src + i, dest)
          y = x + 1
          print i
     print str(y) + " files have been moved"
     if files == []:
          print "Folder is empty"

move(a,b)

#Source and Destination Folders can be changed by changing the a and b variables.
