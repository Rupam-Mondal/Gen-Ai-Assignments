import math as m


def prime(n):
    for i in range(2 , int(m.sqrt(n)) + 1):
        if  n % i == 0:
            return "This is not prime"
        
    return "This is prime"

print(prime(12))