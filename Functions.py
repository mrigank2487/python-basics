#Function definition

def sum(x,y):
    s=x+y
    print ("Sum of the numbers: ",s)

#Function Call

sum(10,20)
sum(20,30)

#Returning values

def add(a,b):
    print a+b
    return a+b

def msg():
    print("Hello")
    return
total=add(10,20)
print("Printing from calling function",total)
msg()
print ("All done")

#Function with default arguments

def message(Id, name, Age=21):
    print Id
    print name
    print Age
    return
message(Id=100, name='Raul', Age=22)
message(Id=101, name='Anil')
message(name='Mrigank', Id=200)    #Keyword arguments

#Anonymous functions
square=lambda x:x*x
print ("Square of number is", square(10))
