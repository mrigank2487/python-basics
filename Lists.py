a=[44,2,21,5,61]
b=[value**2 for value in a]
c=[value*3 for value in a]
L1=['Delhi','Goa','Mumbai','Chennai']
L2=[10,20,30,40,50,60]
L5=[1,2,[6,7,8]]
a.sort()
print(a)
d=a.pop(2)
print(d)
print(['Hey']*3)
print('Um'*3)        
print(L1[0:4:2])                      #Start:Stop:Step
print(L5[2][1])                       #Printing element from nested list
print(L5[1:3])                        #Printing the list elements
print (b)
print (c)
print (a)
print(sum(a))
print(sum(L2))
print(sum(a+L2))                     #Sum of the elements of 2 lists
a=[2,3,4,5]+list("45")               #Concantenate a list ---- Gets added as '4', '5' because "45" is a string
print(a)                             #Print concantenated list
a[1]=44                              #Substitute an element
print('New a is',a)                  #Print modified list
c=[]
c=a+b
print (c)

#Lists do not have data types. So it can be like: [1,2,[3,6,"Hiii"],["No","No"],8,9,10]

#-------------PRINTING ELEMENTS IN REVERSE------------------

i=1
while(i<len(a)): 
    print(a[-i])                      #While loop to print elements in reverse
    i+=1

#-------------------LINEAR SEARCH-------------------------


a=[]
for x in range(0,5):
    i=int(input("Enter the values: "))       #Inputs value             
    a.append(i)                              #Add value to array a. And this goes on beacause of the loop.
print("List of a =",a)
j=int(input("Enter number to be searched"))
x=0
c=0
while x<5:
    if j==a[x]:
        print ("x is",x)
        c+=1
    x=x+1
if c==0:
    print("Number does not exist")
