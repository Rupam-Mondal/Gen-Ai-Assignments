def sum(list):
    sum = 0
    for i in list:
        if(i % 2 == 0):
            sum = sum + i
    return sum

print(f"Sum of even number = {sum([2 , 3 , 5 , 4 , 9 , 10])}")