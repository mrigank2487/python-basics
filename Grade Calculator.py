print("Enter marks attained to calculate final grade: ")
a=input("Subject 1: ")
b=input("Subject 2: ")
c=input("Subject 3: ")
d=input("Subject 4: ")
e=input("Subject 5: ")
total=a+b+c+d+e
percentage=(total/5)
print percentage
if percentage>=93:
    print("Final Grade: A")
elif percentage<93 and percentage>=90:
    print("Final Grade: A-")
elif percentage<90 and percentage>=87:
    print("Final Grade: B+")
elif percentage<87 and percentage>=84:
    print("Final Grade: B")
elif percentage<84 and percentage>=80:
    print("Final Grade: B-")
elif percentage<80 and percentage>=76:
    print("Final Grade: C+")
elif percentage<76 and percentage>=72:
    print("Final Grade: C")
elif percentage<72 and percentage>=65:
    print("Final Grade: D")
elif percentage<65:
    print("Final Grade: F")
