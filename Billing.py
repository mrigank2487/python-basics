print("Enter price of 5 items" )
a=input("Item 1: ")
b=input("Item 2: ")
c=input("Item 3: ")
d=input("Item 4: ")
e=input("Item 5: ")
total=a+b+c+d+e
if total>=20000:
    print ("Current total: {0}".format(total))
    discount=(0.2*total)
    print ("Discount of 20% = {0}".format(discount))
    final=total-discount
    print("Total amount to be paid: {0}".format(final))
elif total<20000 and total>=15000:
    print ("Current total: {0}".format(total))
    discount=(0.15*total)
    print ("Discount of 15% = {0}".format(discount))
    final=total-discount
    print("Total amount: {0}".format(final))
elif total<15000 and total>=10000:
    print ("Current total: {0}".format(total))
    discount=(0.10*total)
    print ("Discount of 10% = {0}".format(discount))
    final=total-discount
    print("Total amount: {0}".format(final))
elif total<10000 and total>=5000:
    print ("Current total: {0}".format(total))
    discount=(0.05*total)
    print ("Discount of 5% = {0}".format(discount))
    final=total-discount
    print("Total amount: {0}".format(final))
elif total<5000:
    print ("Current total: {0}".format(total))
    print ("No Discount ")
    print("Total amount: {0}".format(total))
