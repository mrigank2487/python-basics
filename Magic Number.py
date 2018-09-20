num=input("Enter a number: ")
x=num
while num>9:
    summ=num
    s=0
    while summ>0:
        b=summ%10
        s=s+b
        summ=summ/10
    num=s
if num==1:
    print("{0} is a Magic Number".format(x))
else:
    print("{0} is not a Magic Number.".format(x))
    
