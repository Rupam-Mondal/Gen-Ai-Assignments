List1 = [1 , 2 , 3 , 4]

#Access --> we can use indexing
print(List1[0])

#Modify --> These are some example of list modify

List1.append("Rupam")
print(List1)
List1[0] = "Avik"
print(List1)

#Delete element from list

del List1[1]
print(List1) # 2 will be deleted
#We can also delete some slice
del List1[1:3]
print(List1)