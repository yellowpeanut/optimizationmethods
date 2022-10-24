from math import *
import numpy as np
import matplotlib.pyplot as plt


def f(x1, x2):
    a = 0
    b = 1
    c = 2
    d = 3
    alf = 80
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def grad(x1, x2):
    # gradient vector
    h = 0.0001
    return [(f(x1+h,x2)-f(x1-h,x2))/(h*2), (f(x1,x2+h)-f(x1,x2-h))/(h*2)]


def gradient(e):
    N = 0
    h = 1
    x = [10, 10]
    gradvect = grad(x[0],x[1])
    while(pow(gradvect[0]+gradvect[1],2)>e):
        x = [x[0]-h*gradvect[0], x[1]-h*gradvect[1]]
        gradvect = grad(x[0], x[1])
        N += 1
    return x, N


def gradient_steepest(e):

    def f_x1h(x1, x2, gradx1):
        y = f(x1, x2)
        h = 0
        while(True):
            yh = f(x1 - (h + e) * gradx1, x2)
            if(yh<y):
                y = yh
                h += e
            else:
                break
        return h

    def f_x2h(x1, x2, gradx2):
        y = f(x1, x2)
        h = 0
        while(True):
            yh = f(x1, x2 - (h + e) * gradx2)
            if(yh<y):
                y = yh
                h += e
            else:
                break
        return h

    N = 0
    x = [10, 10]
    gradvect = grad(x[0],x[1])
    while(pow(gradvect[0]+gradvect[1],2)>e):
        x1h = f_x1h(x[0], x[1], gradvect[0])
        x2h = f_x2h(x[0], x[1], gradvect[1])
        x = [x[0]-x1h*gradvect[0], x[1]-x2h*gradvect[1]]
        gradvect = grad(x[0], x[1])
        N += 1
    return x, N


e = 0.0001
x1, N1 = gradient(e)
x2, N2 = gradient_steepest(e)
print("Gradient solution: ", x1,"\nIterations: ", N1, "\nSteepest gradient solution: ", x2,"\nIterations: ", N2)

levels = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.10, -0.05, -0.01, 0.0, 0.01, 0.05, 0.10,0.20,0.30, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
xg1 = np.arange(-3, 3.125, 0.125)
xg2 = np.arange(-3, 3.125, 0.125)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(f)
yg = f2(xg1, xg2)
cont = plt.contour(xg1, xg2, yg, levels=levels)
plt.plot(x1[0],x1[1],color="red", marker=".")
plt.plot(x2[0],x2[1],color="blue", marker=".")
plt.show()