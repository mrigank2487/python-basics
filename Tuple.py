#Tuples are like Lists but immutable (Cannot change it). Instead of using [] use ()

ex1=(10,20,'Jay',56.8)
ex2="a",10,15.55 #If () is not used, by default it is a tuple
tuple1=() #Empty tuple
tuple1=(10) #Single value

#Nesting a tuple
T1='a',"Rajesh",10.10
T2=T1,(10,20,30)
print T1
print T2

#Slice notatopn can be used for Tuples. [StartIndex:EndIndex]
#Adding, replicating, slicing tuples remains the same as Lists. CANNOT update tuple.

data=(10,20,30)
data[0]=50
print data #Gives an error as tuples are immutable
