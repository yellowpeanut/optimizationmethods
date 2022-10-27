from math import *
import numpy as np
import matplotlib.pyplot as plt


def f(x1, x2):
    a = -2
    b = -1
    c = 1
    d = 2
    alf = 60
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def con1(x1, x2):
    return 4 * x1 * x1 - x2


def con2(x1):
    return x1


def in_constraints(X):
    if (con1(X[0], X[1]) <= 0) and (con2(X[0]) > 0):
        return True
    else:
        return False


def grad(x1, x2):
    # gradient vector
    h = 0.0001
    return [(f(x1 + h, x2) - f(x1 - h, x2)) / (h * 2), (f(x1, x2 + h) - f(x1, x2 - h)) / (h * 2)]


def interior_penalty(e):

    def fi(x1, x2):
        return min(0, con1(x1, x2))+min(0, con2(x1))

    def R(x1, x2):
        return f(x1, x2) + 1 / k * (1 / con1(x1, x2) + 1 / con2(x1))

    def gradR(x1, x2):
        h = 0.0001
        return [(R(x1 + h, x2) - R(x1 - h, x2)) / (h * 2), (R(x1, x2 + h) - R(x1, x2 - h)) / (h * 2)]

    def gradient(xx):
        h = 1
        gradvectR = gradR(xx[0], xx[1])
        while pow(gradvectR[0] + gradvectR[1], 2) > e:
            xx[0], xx[1] = [xx[0] - h * gradvectR[0], xx[1] - h * gradvectR[1]]
            print("help 3 ", xx, "vctr ", gradvectR)
        xx[2] = f(xx[0], xx[1])
        return xx

    x_list = []
    k = 1
    c = 10
    x = [10, 10, 0]

    # checking if the point in constraints, if it isn't, moving it towards constraints
    while fi(x[0], x[1]) != 0:
        h = 0.0001
        gv = [(fi(x[0] + h, x[1]) - fi(x[0] - h, x[1])) / (h * 2), (fi(x[0], x[1] + h) - fi(x[0], x[1] - h)) / (h * 2)]
        x[0], x[1] = [x[0] - gv[0], x[1] - gv[1]]
        print("help 1")

    x[2] = f(x[0], x[1])
    xn = gradient(x)

    while abs(x[2] - xn[2]) > e:
        print("help 2")
        k *= c
        x = xn
        x_list.append(xn)
        xn = gradient(x)

    return x, x_list


e = 0.0001
_x, _x_list = interior_penalty(e)
for i in range(len(_x_list)):
    print(i+1, ". x1: ", _x_list[i][0], " x2: ", _x_list[i][1], " y: ", _x_list[i][2], " k: ", pow(10, i))
print("Solution: ", _x[0], " ", _x[1])

levels = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.10, -0.05, -0.01, 0.0, 0.01, 0.05, 0.10,0.20,0.30, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
xg1 = np.arange(-3, 3.125, 0.125)
xg2 = np.arange(-3, 3.125, 0.125)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(f)
yg = f2(xg1, xg2)
cont = plt.contour(xg1, xg2, yg, levels=levels)
plt.plot(_x[0],_x[1],color="red", marker=".")
plt.show()