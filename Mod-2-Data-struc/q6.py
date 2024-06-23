#Tuples

"""1. Immutable Records"""

# Tuples are used for representing data records that
# should not change throughout the program execution.

tu = (1 , 2 , 3 , 4)
# tu[0] = "Rupam" this will give error

"""2. Return multiple values"""

# Tuples are often used to 
# return multiple values from a function

def op():
    return 12 , "Rupam"
print(op())

#Set

#1. Unique elements
"""To store unique elements in a set"""
s = {1 , 1 , 1 , 1 , 2}
print(s) #{1 , 2}

#2. When we wanna remove duplicate from list
"""Removing duplicates from a list"""

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(set(my_list))
print(unique_elements)  # Output: [1, 2, 3, 4, 5]
