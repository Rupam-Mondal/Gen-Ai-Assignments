"""
Mutable objects can be changed after their creation.
This means you can modify their content without 
changing their identity. ex--> list , dictionary
"""
#ex -->

list = [1 , 2 , 3 , 4 , 5]
list[0] = 33 #There will be no error as list is mutable

"""
Immutable objects cannot be changed after their creation. 
Any modification attempts will 
result in the creation of a new object. ex--> string , tuple etc
"""

s = "Rupam"
s[0] = 'A' #This will give a error becxause s is immutable