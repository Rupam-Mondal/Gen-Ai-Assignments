# Python supports two types of loop like --> for , while
"""
for loop naturally used when we know how many times we have to 
iterate over any sequence on. How many times we want to execute
a particular block
"""
# for loop ex-->

list = [1 , 2 , 3 , 4 , 5]
sum = 0
for i in range(0 , len(list)):
    sum = sum + list[i]
print(sum)

"""
while loop is natuarraly used to execute a block as long as
the condition is true.
"""
list1 = [1 , 2 , 3 , 4 , 5]
i = 0
sum1 = 0
while i < 3:
    sum1 = sum1 + list1[i]
    i = i + 1

print(sum1)
