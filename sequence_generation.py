# This is the fibonacci ratio, only that there ia a 0 before the fibonacci number
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 is the fib of 15
# 0010102030508013021034055089014402330377 is what we have

def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a, end='')
        print(0, b, end='')

        for i in range(2, n):
            c = a + b
            a = b
            b = c

            print(0, c, end='')

fib(15)