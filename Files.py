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
