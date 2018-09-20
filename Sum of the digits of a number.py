a=input("Enter a number: ")
num=0
while a>0:
    b=a%10
    a=a/10
    num=num+b
print("The sum of the digits of the number is = {0}".format(num))
