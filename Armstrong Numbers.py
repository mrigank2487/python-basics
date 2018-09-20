a=input("Enter a number: ")
n=a
sum=0
while n>0:
    r=n%10
    n=n/10
    sum=sum+(r*r*r)
if sum==a:
    print ("{0} is an Armstrong number".format(a))
else:
    print ("{0} is not an Armstrong Number".format(a))


    
