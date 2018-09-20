obj=open("MyFile.txt","w")
obj.write("This is going in the file")
obj.close()
obj1=open("MyFile.txt","r")
s=obj1.read()
print s
obj.close()
obj2.open("MyFile.txt","r")
s1=obj2.read(20)
print s1
obj2.close()

print obj.name  #MyFile.txt
print obj.mode  #w or r (if obj2)
print obj.closed  #False

# r - read
# rb - read binary
# r+ - read and write, pointer at beginning
# w - write
# wb - write binary
# w+ - read and write, if file already exists it will overwrite or else create a new file
# wb+ - same as above but for binary file
# a - append
# ab - append binary

import os
os.remane("existingfile.txt", "newfile.txt")
os.remove("oldfile.txt") #Deletes file
os.mkdir("new") #Makes new directory
os.chdir("new") #Makes changes to current directory
print os.getcwd #Gives the current working directory
os.rmdir("new") #Removes a directory before removing the directory, the directory should be empty
