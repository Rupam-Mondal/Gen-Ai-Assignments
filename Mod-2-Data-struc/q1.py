"""
string slicing is a process of accessing some part
of a string. We can specify initial index and final index
as well as number of step to jump while slicing


suppose s is a string
so we can use slice like --> s[Initial:Final(Exclusive):Step]
"""
#Ex-->

s = "Rupam"
print(s[0:3:1]) #Also we can write s[0:3]

print(s[0:3:2]) #Output is --> Rp

print(s[2:]) #If we do not mention last index 
#it will go upto end

print(s[:3])#If we do not mention first index 
#it will start slicing from start