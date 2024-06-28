def square(list):
    for i in range(0 , len(list)):
        list[i] = list[i] ** 2
    return list

print(square([1 , 2 , 3 , 4]))