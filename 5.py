from math import *
import numpy as np
import matplotlib.pyplot as plt
import random


def f(x1, x2):
    a = 0
    b = 0
    c = 1
    d = 2
    alf = 45
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def con1(x1, x2):
    return x1*x2+54


def con2(x1, x2):
    return 3*x1+x2-6


def in_constraints(X):
    if (con1(X[0], X[1]) <= 0) and (con2(X[0], X[1]) == 0):
        return True
    else:
        return False


def grad(xi):
    x1 = xi[0]
    x2 = xi[1]
    h = 0.0001
    return [(f(x1 + h, x2) - f(x1 - h, x2)) / (h * 2), (f(x1, x2 + h) - f(x1, x2 - h)) / (h * 2)]


def gradf(xi):
    h = 0.1
    x = xi.copy()
    gradvect = grad(x)
    while(pow(gradvect[0]+gradvect[1],2)>e):
        x = [x[0]-h*gradvect[0], x[1]-h*gradvect[1], 0]
        gradvect = grad(x)
    x[2] = f(x[0], x[1])
    return x.copy()


def interior_penalty(e):

    def R(x1, x2):
        return f(x1, x2) + k * max(0.0, pow(con1(x1, x2), 2)) + k * pow(con2(x1, x2), 2)

    def gradR(x1, x2):
        h = 0.0001
        return [(R(x1 + h, x2) - R(x1 - h, x2)) / (h * 2), (R(x1, x2 + h) - R(x1, x2 - h)) / (h * 2)]

    def gradient(xi):
        xx = xi.copy()
        h = 0.00001
        gradvectR = gradR(xx[0], xx[1])
        xxt = [xx[0]+2*e, xx[1]+2*e, 0]
        xxt[2] = R(xxt[0], xxt[1])
        xx[2] = R(xx[0], xx[1])
        N = 0
        while abs(xx[2]-xxt[2]) > e:
            xxt = xx.copy()
            xx[0] = xx[0] - h * gradvectR[0]
            xx[1] = xx[1] - h * gradvectR[1]
            xx[2] = R(xx[0], xx[1])
            gradvectR = gradR(xx[0], xx[1])
            N+=1
            #print(x, " ", xx, " ", k)
            print("help 3 ", xx, "vctr ", gradvectR, "x ", x)
        xx[2] = f(xx[0], xx[1])
        return xx

    def powell(xi):
        dlt = e
        x1 = xi[0]
        x2 = xi[1]

        y1 = R(x1, x2)

        # print("yes", " y1: ", y1)
        while (True):
            # print("aaaaaa")
            hF = False
            vF = False
            dF = False

            rt = 0
            lt = 0
            tp = 0
            bt = 0

            # horizontal
            x1 += dlt
            y2 = R(x1, x2)
            x1 -= dlt
            if (y2 <= y1):
                hF = True
                x1 += dlt
                while (y2 <= y1):
                    # print("1 x1: ", x1, "x2: ", x2)
                    y1 = y2
                    rt += 1
                    x1 += dlt
                    y2 = R(x1, x2)
                x1 -= dlt
            else:
                x1 -= dlt
                y2 = R(x1, x2)
                while (y2 <= y1):
                    # print("2 x1: ", x1, "x2: ", x2)
                    hF = True
                    y1 = y2
                    lt += 1
                    x1 -= dlt
                    y2 = R(x1, x2)
                x1 += dlt

            # vertical
            x2 += dlt
            y2 = R(x1, x2)
            x2 -= dlt
            if (y2 <= y1):
                vF = True
                x2 += dlt
                while (y2 <= y1):
                    # print("3 x1: ", x1, "x2: ", x2)
                    y1 = y2
                    tp += 1
                    x2 += dlt
                    y2 = R(x1, x2)
                x2 -= dlt
            else:
                x2 -= dlt
                y2 = R(x1, x2)
                while (y2 <= y1):
                    # print("4 x1: ", x1, "x2: ", x2)
                    vF = True
                    y1 = y2
                    bt += 1
                    x2 -= dlt
                    y2 = R(x1, x2)
                x2 += dlt

            # diagnal
            if (rt > 0):
                if (tp > 0):
                    x1 += dlt * rt
                    x2 += dlt * tp
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("5 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 += dlt * rt
                        x2 += dlt * tp
                        y2 = R(x1, x2)
                    x1 -= dlt * rt
                    x2 -= dlt * tp
                else:
                    x1 += dlt * rt
                    x2 -= dlt * bt
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("6 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 += dlt * rt
                        x2 -= dlt * bt
                        y2 = R(x1, x2)
                    x1 -= dlt * rt
                    x2 += dlt * bt
            elif (lt > 0):
                if (tp > 0):
                    x1 -= dlt * lt
                    x2 += dlt * tp
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("7 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 -= dlt * lt
                        x2 += dlt * tp
                        y2 = R(x1, x2)
                    x1 += dlt * lt
                    x2 -= dlt * tp
                else:
                    x1 -= dlt * lt
                    x2 -= dlt * bt
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("8 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 -= dlt * lt
                        x2 -= dlt * bt
                        y2 = R(x1, x2)
                    x1 += dlt * lt
                    x2 += dlt * bt

            if ((hF == False) and (vF == False) and (dF == False)): break

        xx = [x1, x2, 0]
        xx[2] = f(xx[0], xx[1])

        return xx

    x_list = []
    k = 1
    c = 10
    x1 = random.randint(-100, 100)
    x2 = 6 - 3*x1
    while(not in_constraints([x1, x2])):
        x1 = random.randint(-100, 100)
        x2 = 6 - 3 * x1
    x = [x1, x2, 0]

    x[2] = f(x[0], x[1])
    print("Initial x: ", x)
    x = gradf(x)
    xn = powell(x)

    while abs(x[2] - xn[2]) > e:
        #print("help 2")
        k *= c
        #if x[2]> xn[2]:
        #    x = xn.copy()
        #else:
        #    break
        x = xn.copy()
        x_list.append(x)
        xn = powell(x)
    #if(len(x_list) > 1):
        #x_list.pop()
        #x_list.pop()
        #x = x_list[len(x_list)-1]

    return x, x_list


e = 0.0001
_x, _x_list = interior_penalty(e)
for i in range(len(_x_list)):
    print(i+1, ". x1: ", _x_list[i][0], " x2: ", _x_list[i][1], " y: ", _x_list[i][2], " k: ", pow(10, i))
print("Solution: ", _x[0], " ", _x[1])

if con1(_x[0], _x[1])<=0:
    print("Point is in constrains!")

levels = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.10, -0.05, -0.01, 0.0, 0.01, 0.05, 0.10,0.20,0.30, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
xg1 = np.arange(-20, 20.250, 0.250)
xg2 = np.arange(-20, 20.250, 0.250)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(f)
yg = f2(xg1, xg2)

x11i, x22i = -20, -20
x1i, x2i = [], []

x11j, x22j = -20, -20
x1j, x2j = [], []

for i in range(100):
    x22i = -54/x11i
    x22j = 6 - 3*x11i

    if x22i > 20:
        x22i = 20
    if x22i < -20:
        x22i = -20
    if x22j > 20:
        x22j = 20
    if x22j < -20:
        x22j = -20

    x1i.append(x11i)
    x2i.append(x22i)
    x1j.append(x11i)
    x2j.append(x22j)

    x11i += 0.41

plt.plot(x1i, x2i, color="blue")

plt.plot(x1j, x2j, color="green")

cont = plt.contour(xg1, xg2, yg, levels=30)
plt.plot(_x[0],_x[1],color="red", marker=".")
plt.show()

def in_constraints(X):
    if (con1(X[0], X[1]) <= 0) and (con2(X[0], X[1]) == 0):
        return True
    else:
        return False
