from math import log10 as ln
from math import sqrt

def f(x):
    return x*x*x + 1.5*x*x + 7


def halfdiv(a0, b0, e):

    N = 0
    x0 = (a0 + b0) / 2.0
    a = a0
    b = b0

    while((pow(0.75, N)*abs((b0-a0))) > e):
        x1 = (a + x0) / 2.0
        x2 = (x0 + b) / 2.0
        #print("x1 = ", x1 , "x2 = ", x2)
        if (f(x1) < f(x2)):
            b = x2
        else:
            a = x1
        x0 = (a + b) / 2.0
        N += 1

    return x0


def goldratio(a0, b0, e):

    a = a0
    b = b0

    x1 = (b-a) * 0.38
    x2 = (b-a) * 0.62
    y1 = f(x1)
    y2 = f(x2)

    while((b-a)>=e):
        #print("x1 = ", x1 , "x2 = ", x2)
        if (y1 < y2):
            b = x2
            x2 = x1
            y2 = y1
            x1 = (b-a) * 0.38
            y1 = f(x1)
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = (b-a) * 0.62
            y2 = f(x2)

    return (b-a) / 2.0


def fib(n):
    return int(pow(1+sqrt(5)/2, n))/sqrt(5)


def fibon(a0, b0, e):

    N = int(abs((b0-a0)/e))
    a = a0
    b = b0

    x1 = fib(N-2)/fib(N)*(b0-a0)
    x2 = fib(N-1)/fib(N)*(b0-a0)
    y1 = f(x1)
    y2 = f(x2)
    k = 1

    while(N > k):
        #print("x1 = ", x1 , "x2 = ", x2)
        if (y1 < y2):
            b = x2
            x2 = x1
            y2 = y1
            x1 = fib(N-2-k)/fib(N-k)*(b-a)
            y1 = f(x1)
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = fib(N-1-k)/fib(N-k)*(b-a)
            y2 = f(x2)
        k += 1

    return (b-a) / 2.0


a = -1.5
b = 6

e = 0.01

print("Half division min = ", halfdiv(a, b, e),
      "\nGolden ratio min = ", goldratio(a, b, e),
      "\nFibonacci min = ", fibon(a, b, e))
