from math import *


def f(x1, x2):
    a = 0
    b = 1
    c = 2
    d = 3
    alf = 80
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def powell(e):
    dlt = e
    x1 = -150
    x2 = 1

    y1 = f(x1, x2)
    x1 += dlt
    y2 = f(x1, x2)

    rt = 0
    lt = 0
    tp = 0
    bt = 0

    print("yes", " y1: ", y1, " y2: ", y2)
    while (abs(y1 - y2) > e):
        print("aaaaaa")
        rt = 0
        lt = 0
        tp = 0
        bt = 0

        # horizontal
        if (y2 <= y1):
            while (y2 <= y1):
                print("1")
                y1 = y2
                rt += 1
                x1 += dlt
                y2 = f(x1, x2)
            x1 -= dlt
        else:
            x1 -= dlt*2
            y2 = f(x1, x2)
            while (y2 <= y1):
                print("2")
                y1 = y2
                lt += 1
                x1 -= dlt
                y2 = f(x1, x2)
            x1 += dlt

        # vertical
        x2 += dlt
        y2 = f(x1, x2)
        if (y2 <= y1):
            while (y2 <= y1):
                print("3")
                y1 = y2
                tp += 1
                x2 += dlt
                y2 = f(x1, x2)
            x2 -= dlt
        else:
            x2 -= dlt * 2
            y2 = f(x1, x2)
            while (y2 <= y1):
                print("4")
                y1 = y2
                bt += 1
                x2 -= dlt
                y2 = f(x1, x2)
            x2 += dlt

        # diagnal
        if (rt > 0):
            if (tp > 0):
                x1 += dlt * rt
                x2 += dlt * tp
                y2 = f(x1, x2)
                while (y2 <= y1):
                    print("5")
                    y1 = y2
                    x1 += dlt * rt
                    x2 += dlt * tp
                    y2 = f(x1, x2)
                x1 -= dlt * rt
                x2 -= dlt * tp
            else:
                x1 += dlt * rt
                x2 -= dlt * bt
                y2 = f(x1, x2)
                while (y2 <= y1):
                    print("6")
                    y1 = y2
                    x1 += dlt * rt
                    x2 -= dlt * bt
                    y2 = f(x1, x2)
                x1 -= dlt * rt
                x2 += dlt * bt
        else:
            if (tp > 0):
                x1 -= dlt * lt
                x2 += dlt * tp
                y2 = f(x1, x2)
                while (y2 <= y1):
                    print("7")
                    y1 = y2
                    x1 -= dlt * lt
                    x2 += dlt * tp
                    y2 = f(x1, x2)
                x1 += dlt * lt
                x2 -= dlt * tp
            else:
                x1 -= dlt * lt
                x2 -= dlt * bt
                y2 = f(x1, x2)
                while (y2 <= y1):
                    print("8")
                    y1 = y2
                    x1 -= dlt * lt
                    x2 -= dlt * bt
                    y2 = f(x1, x2)
                x1 += dlt * lt
                x2 += dlt * bt
        x1 += dlt
        y2 = f(x1,x2)

    x1 -= dlt
    #x1 -= dlt*(rt+1)
    #x1 += dlt*lt
    #x2 -= dlt*tp
    #x2 += dlt*bt

    X = {x1,x2}

    return X


e = 0.01

print("Powell's solution: ", powell(e))
