from math import *
import numpy as np
import matplotlib.pyplot as plt
import random


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

    def gradient(x):
        xx = [x[0], x[1], x[2]]
        h = 0.01
        gradvectR = gradR(xx[0], xx[1])
        while pow(gradvectR[0] + gradvectR[1], 2) > e:
            xx[0] = xx[0] - h * gradvectR[0]
            xx[1] = xx[1] - h * gradvectR[1]
            gradvectR = gradR(xx[0], xx[1])
            #print(x, " ", xx)
            #print("help 3 ", xx, "vctr ", gradvectR)
        xx[2] = f(xx[0], xx[1])
        return xx

    x_list = []
    k = 1
    c = 10
    x = [random.randint(-100, 100), random.randint(-100, 100), 0]

    while not in_constraints(x):
        #h = 0.0001
        #gv = [(fi(x[0] + h, x[1]) - fi(x[0] - h, x[1])) / (h * 2), (fi(x[0], x[1] + h) - fi(x[0], x[1] - h)) / (h * 2)]
        #x[0], x[1] = [x[0] - gv[0], x[1] - gv[1]]
        #print("help 1 ", gv, " ", x)
        x = [random.randint(-100, 100), random.randint(-100, 100), 0]
        #print("yay ", x)

    x[2] = f(x[0], x[1])
    print("Initial x: ", x)
    xn = gradient(x)

    while abs(x[2] - xn[2]) > e:
        #print("help 2")
        k *= c
        x = [xn[0], xn[1], xn[2]]
        x_list.append(x)
        xn = gradient(x)
    if(len(x_list) > 0):
        x_list.pop()
        x = x_list[len(x_list)-1]


    return x, x_list


e = 0.0001
_x, _x_list = interior_penalty(e)
for i in range(len(_x_list)):
    print(i+1, ". x1: ", _x_list[i][0], " x2: ", _x_list[i][1], " y: ", _x_list[i][2], " k: ", pow(10, i))
print("Solution: ", _x[0], " ", _x[1])

levels = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.10, -0.05, -0.01, 0.0, 0.01, 0.05, 0.10,0.20,0.30, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
xg1 = np.arange(-5, 10.250, 0.250)
xg2 = np.arange(-5, 10.250, 0.250)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(f)
yg = f2(xg1, xg2)

x1i = np.linspace(0, 0, 100)
x2i = np.linspace(-5, 10.250, 100)
plt.plot(x1i, x2i, color="blue")

x11j, x22j = -5, -5
x1j, x2j = [], []
for i in range(100):
    x22j = x11j*x11j*4
    if(x22j > 10):
        x22j = 10
    x1j.append(x11j)
    x2j.append(x22j)
    x11j += 0.1525
plt.plot(x1j, x2j, color="green")

cont = plt.contour(xg1, xg2, yg, levels=30)
plt.plot(_x[0],_x[1],color="red", marker=".")
plt.show()
