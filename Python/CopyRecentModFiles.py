import os
import shutil
import time

####Copies files from Branch Office folder to Home Office Folder.
####Script is intended to be run 24 hrs apart on each business day.
####Copies only files from the Branch Office where the modified time is
# less than 24 hrs from the current time

branch = '''insert path of source'''
home = '''insert path of destination'''

def copy(src, dest):
        files = os.listdir(src)
        for x, i in enumerate(files):
                branchModTime = os.path.getmtime(src + i)
                time24 = int(time.time()) - 86400
                if time24 <= branchModTime:
                        shutil.copy(src + i, dest)
                        print (x,i)
                        
                                       
copy(branch,home)


#### Reference Notes
## https://docs.python.org/2/library/os.path.html?highlight=mtime#os.path.getmtime
#os.path.getmtime(path)
#returns the file modified time in epoch time
#86400 is the number of seconds in 24 hours.

####Possible changes to the code could be to compare the modified times between
# the Home Office Folder and Branch Office Folder. Any time in the Branch Office
#Folder that is greater than the Home Office folder could be copied over. This
#would make it so that the script could be run at any time.


