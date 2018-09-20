a=input("Enter a number: ")
b=input("Enter another number: ")
c=input("Enter another number: ")
if a>b and a>c:
    print("The larger number is: {0}".format(a))
elif b>a and b>c:
    print("The larger number is: {0}".format(b))
elif c>a and c>b:
    print("The larger number is: {0}".format(c))

