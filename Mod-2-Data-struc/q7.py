#1. Add
"""we can add a new key-value pair to a dictionary by simply 
assigning a value to a new key."""

d = {"name" : "Rupam" , "Age" : 30}
d["Gender"] = "Male"
print(d)

#2. Modify
d["name"] = "Avik"
print(d)

#3.  Delete
del d["Age"]
print(d)
d.pop("name")
print(d)