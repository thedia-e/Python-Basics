"""
EXAMPLE 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
"""

#docstring
print(abs.__doc__)
#len()
print(len.__doc__)
#sorted()
print(sorted.__doc__)

"""
EXAMPLE 12. Write a Python program that prints the calendar for a given month and year.
"""

import calendar
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
print(calendar.month(year, month)) 

"""
EXAMPLE 13. Write a Python program to print the following 'here document'.
"""
# Use triple double-quotes to create a multi-line string
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

"""
EXAMPLE 14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date
start_date = date(2014, 7, 2)
end_date = date(2014, 7, 11)
n_o_days = end_date - start_date
print(n_o_days.days)

"""
EXAMPLE 15. Write a Python program to get the volume of a sphere with radius six.
"""

from math import pi
print("Volume of a sphere with radius 6")
radius = 6
volume = (4/3) * pi * radius**3
print(volume)

""" 
pi = 3.1415926535897931
r = 6.0
V = 4.0/3.0 * pi * r**3
print('The volume of the sphere is: ', V)
"""

"""
EXAMPLE 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""

number = int(input("Enter a number: "))
if(number > 17):
    print(2 * (number - 17))
else:
    print((17 - number))

"""
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2
print(difference(22))
print(difference(14))
"""

"""
EXAMPLE 17. Write a  Python program to test whether a number is within 100 of 1000 or 2000.
"""

def test_number(number):
    return ((abs(1000 - number) <= 100) or (abs(2000 - number) <= 100))

#abs(x) function returns the absolute value of x as positive.

number = int(input("Enter a number: "))
print(test_number(number))

"""
EXAMPLE 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""

numbers = list(map(int, input("Enter three numbers with spaces between them:  ").split()))

if len(numbers) != 3:
    print("Please enter exactly three numbers.")

if len(set(numbers)) == 1:
    print(sum(numbers) * 3)
else:
    print(sum(numbers))

"""
def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
"""

"""
EXAMPLE 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""
#taken directly from the site
def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text

print(new_string("Array"))

print(new_string("IsEmpty"))

"""
EXAMPLE 20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""

def repeat_string(string1, n):
    if n < 0:
        return "Error: The number must be a non-negative integer."
    
    return ''.join([string1 for _ in range(n)])

string1 = input("Enter string: \n")
number = int(input("Enter a non-negative integer: "))

result = repeat_string(string1, number)
print("Resulting string:", result)









