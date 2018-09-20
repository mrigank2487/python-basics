#Modules are used to categorize code in python into small parts. A module is simply a file, where classes, functions and variables are defined. Grouping similar code into a single file makes it easy to access.

def add(a,b):
    c=a+b
    print c
    return
# Save the above code in a file named addition.py

import addition
addtion.add(10,20)
addition.add(30,40)   #Use file name to use function or variable in that file

#We can import multiple modules
import addition,subtraction,multiplication

#Using from import statement
from area import square, triangle     #Square and triangles are functions
square(10)
triangle(5,6)    #Call function directly if using from statement

