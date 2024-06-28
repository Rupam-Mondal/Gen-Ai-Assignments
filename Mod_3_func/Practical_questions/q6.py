def power(n):
    for i in range(1 , n):
        yield i ** 2


g = power(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
