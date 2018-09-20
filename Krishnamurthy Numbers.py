a=input("Enter a number to check if it is a Krishnamurthy number: ")
n=a
sum=0
while a>0:
    r=a%10
    fac=1
    for i in range(1,r+1):
        fac=fac*i
        i=i+1
    sum=sum+fac
    a=a/10
    
if sum==n:
    print ("{0} is a Krishnamurthy number".format(n))
else:
    print ("{0} is not a Krishnamurthy Number".format(n))


    

