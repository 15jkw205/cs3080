def fib(n):
    if n < 2:
        return 1

    return fib(n-2) + fib(n-2)

for i in range(20):
    print("fib(%2d) = %6d" % (i, fib(i)))