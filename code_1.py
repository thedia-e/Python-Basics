"""
EXAMPLE 1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
    """
    
formatted_output = (
    "Twinkle, twinkle, little star,\n"
    "\tHow I wonder what you are! \n"
    "\t\tUp above the world so high, \n"
    "\t\tLike a diamond in the sky. \n"
    "Twinkle, twinkle, little star, \n"
    "\tHow I wonder what you are"
)

print(formatted_output)
 
"""
EXAMPLE 2. Write a Python program to find out what version of Python you are using.
"""

import sys
print("Python version:", sys.version)
print("Version info:", sys.version_info)

"""
EXAMPLE 3.Write a Python program to display the current date and time.
"""

import datetime
print("Current date and time: ")
x = datetime.datetime.now()
print(x)

"""
print(now.strftime("%Y-%m-%d %H:%M:%S"))
strftime is used in the original site's solution to format the datetime object'
"""

"""
EXAMPLE 4.Write a Python program that calculates the area of a circle based on the radius entered by the user.
"""

from math import pi
radius = float(input("Enter radius: "))
area = pi*radius**2
print("Area of the circle is " , area)
"""print("The area of the circle with radius " + str(r) + " is: " + str(area))"""

"""
EXAMPLE 5.Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""
first_name = input("First name: ")
last_name = input("Last name: ")
print("Normal order:", first_name, " ", last_name)
print("Desired order:", last_name, " ", first_name)

"""
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print("Hello  " + lname + " " + fname)
"""

"""
EXAMPLE 6.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
"""
cs_numbers = input("Enter number sequence: ")
number_list = cs_numbers.split(",")
number_tuple = tuple(number_list)
print('List : ', number_list)
print('Tuple : ', number_tuple)

"""We should avoid using list and tuple as variable names since they are built-in functions."""

"""
EXAMPLE 7.Write a Python program that accepts a filename from the user and prints the extension of the file.
"""

filename = input("Enter filename and extension: ")
extension = filename.split(".")
print("Extension : " + repr(extension[-1]))

"""
EXAMPLE 8. Write a Python program to display the first and last colors from the following list.
"""

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])

"""
EXAMPLE 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
"""

exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)

"""
EXAMPLE 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""

def calculation(n):
    num_str = str(n)
    nn = int(num_str * 2)
    nnn = int(num_str * 3)
    calc = n + nn + nnn
    return calc

n = int(input("Enter an integer : "))
calc = calculation(n)    
print("The calculation = ", calc)































