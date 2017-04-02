import os




####I wrote this script to creates a set of test text files.

##Since the volume of text files was what i was after and not content,
#I used range to create files and to fill the files content with a range of numbers.


def CreateFiles(noOfFiles, x): #(Number of Files, content)
    
    a = range(x) #creates the content of files with a range of numbers

    b = "This file is created by a code genius (well she would like to be)"
    # adds the string to each file.
    
    fileName = "NameOfFile"

    for i in range(noOfFiles): #the parameter to create test files
        newFile = open(fileName + str(i)+".txt", "w")
        newFile.write(str(a) + b) #content in files
        newFile.close()
    print "done"

CreateFiles(3, 50)

#note to self: **String and range needs to be formatted but not that important for this purpose**
#note to self: **Also, for crying out loud, think of more clever text!

###Script could be used for other purposes.
#An idea would be a set of qoutes in numbered variables that could be used with
#range so that content in each file would be different.



