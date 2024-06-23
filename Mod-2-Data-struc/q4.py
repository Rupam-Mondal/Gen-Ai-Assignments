#1. Mutable

"""List is mutable, we can modify list after creation"""
list =[1 , 2 , 3 , 4 , 5]
list[0] = "Rupam"
print(list)

"""Tuple is immutable, we can not modify tuple after creation"""
tu = (1 , 2 , 3 , 4 , 5)
# tu[0] = "Rupam" This will throw a output
print(tu)

#2. Syntax

"""In case list we use Brakets"""
list1 = [1 , 2 , 3]
"""In casre tuple we use parathesis"""
tu1 = (1 , 2 , 3)

#3. Use case

"""List --> As class teacher said that we use list where we wanna modify 
    data time to time"""
"""Tuple --> In case of tuple we do not modify data frequently"""

"""List have many methods but tuple has less amount of in built method"""