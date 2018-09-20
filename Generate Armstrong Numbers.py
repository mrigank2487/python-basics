
i=0
print ("The Armstrong numbers are: ")
while i<1001:
    n=i
    sum=0
    while n>0:
        r=n%10
        n=n/10
        sum=sum+(r*r*r)
    if sum==i:
        print i
    i=i+1
    


    
