def fibo(n):
    a = 0
    b = 1
    c = 0
    for i in range(0 , n):
        yield a
        c = a + b
        a = b
        b = c



print(list(fibo(10)))