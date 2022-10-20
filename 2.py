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
    #return 100*pow((x2-x1*x1), 2)+pow((1-x1), 2)

def powell(h):
    dlt = h/100
    x1 = 15
    x2 = 10

    y1 = f(x1, x2)

    #print("yes", " y1: ", y1)
    while (True):
        #print("aaaaaa")
        hF = False
        vF = False
        dF = False

        rt = 0
        lt = 0
        tp = 0
        bt = 0

        # horizontal
        x1 += dlt
        y2 = f(x1, x2)
        x1 -= dlt
        if (y2 <= y1):
            hF = True
            x1 += dlt
            while (y2 <= y1):
                #print("1 x1: ", x1, "x2: ", x2)
                y1 = y2
                rt += 1
                x1 += dlt
                y2 = f(x1, x2)
            x1 -= dlt
        else:
            x1 -= dlt
            y2 = f(x1, x2)
            while (y2 <= y1):
                #print("2 x1: ", x1, "x2: ", x2)
                hF = True
                y1 = y2
                lt += 1
                x1 -= dlt
                y2 = f(x1, x2)
            x1 += dlt

        # vertical
        x2 += dlt
        y2 = f(x1, x2)
        x2 -= dlt
        if (y2 <= y1):
            vF = True
            x2 += dlt
            while (y2 <= y1):
                #print("3 x1: ", x1, "x2: ", x2)
                y1 = y2
                tp += 1
                x2 += dlt
                y2 = f(x1, x2)
            x2 -= dlt
        else:
            x2 -= dlt
            y2 = f(x1, x2)
            while (y2 <= y1):
                #print("4 x1: ", x1, "x2: ", x2)
                vF = True
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
                    #print("5 x1: ", x1, "x2: ", x2)
                    dF = True
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
                    #print("6 x1: ", x1, "x2: ", x2)
                    dF = True
                    y1 = y2
                    x1 += dlt * rt
                    x2 -= dlt * bt
                    y2 = f(x1, x2)
                x1 -= dlt * rt
                x2 += dlt * bt
        elif (lt > 0):
            if (tp > 0):
                x1 -= dlt * lt
                x2 += dlt * tp
                y2 = f(x1, x2)
                while (y2 <= y1):
                    #print("7 x1: ", x1, "x2: ", x2)
                    dF = True
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
                    #print("8 x1: ", x1, "x2: ", x2)
                    dF = True
                    y1 = y2
                    x1 -= dlt * lt
                    x2 -= dlt * bt
                    y2 = f(x1, x2)
                x1 += dlt * lt
                x2 += dlt * bt

        if((hF == False) and (vF == False) and (dF == False)): break

    xx = [x1, x2]

    return xx


def nelder_mead(e):
    def l3(arr):
        return arr[2]

    n = 2
    a = 1
    b = 0.5
    g = 2
    k = 0.5
    x1 = [-15, -40, 0]
    x2 = [x1[0] + x1[0] * k, x1[1], 0]
    x3 = [x1[0], x1[1] + x1[1] * k, 0]
    x1[2] = f(x1[0], x1[1])
    x2[2] = f(x2[0], x2[1])
    x3[2] = f(x3[0], x3[1])
    x = [x1, x2, x3]

    ff = (x[0][2] + x[1][2] + x[2][2]) / 3
    sig2 = (pow(x[0][2] - ff, 2) + pow(x[1][2] - ff, 2) + pow(x[2][2] - ff, 2)) / 3

    while (sqrt(sig2) >= e):
        x1[2] = f(x1[0], x1[1])
        x2[2] = f(x2[0], x2[1])
        x3[2] = f(x3[0], x3[1])
        x.sort(key=l3)

        xc = [(x[0][0] + x[1][0]) / 2, (x[0][1] + x[1][1]) / 2, 0]
        xc[2] = f(xc[0], xc[1])
        xr = [xc[0]+a*(xc[0]-x[2][0]), xc[1]+a*(xc[1]-x[2][1]), 0]
        xr[2] = f(xr[0],xr[1])
        if(xr[2]<x[2][2]):
            xe = [xc[0]+g*(xc[0]-x[2][0]), xc[1]+g*(xc[1]-x[2][1]), 0]
            xe[2] = f(xe[0], xe[1])
            #expand
            if (xe[2] < x[2][2]):
                x[2] = xe
            #reflect
            else:
                x[2] = xr
        #reflect
        elif(xr[2]<x[1][2]):
            x[2] = xr
        elif(xr[2]<x[2][2]):
            xcon = [xc[0] + b * (xc[0] - x[2][0]), xc[1] + b * (xc[1] - x[2][1]), 0]
            xcon[2] = f(xcon[0], xcon[1])
            #outside contract
            if(xcon[2]<=xr):
                x[2] = xcon
            #shrink
            else:
                for i in range(1, n + 1):
                    x[i][0] = (x[i][0] + x[0][0]) / 2
                    x[i][1] = (x[i][1] + x[0][1]) / 2
                    x[i][2] = f(x[i][0], x[i][1])
        else:
            xcon = [xc[0] + b*(x[2][0]-xc[0]), xc[1] + b*(x[2][1]-xc[1]), 0]
            xcon[2] = f(xcon[0], xcon[1])
            #inside contract
            if(xcon[2]<x[2][2]):
                x[2] = xcon
            #shrink
            else:
                for i in range(1, n + 1):
                    x[i][0] = (x[i][0] + x[0][0]) / 2
                    x[i][1] = (x[i][1] + x[0][1]) / 2
                    x[i][2] = f(x[i][0], x[i][1])

        ff = (x[0][2] + x[1][2]+x[2][2]) / 3
        sig2 = (pow(x[0][2] - ff,2) + pow(x[1][2] - ff,2) + pow(x[2][2] - ff,2)) / 3

    return [(x[0][0] + x[1][0] + x[2][0]) / 3, (x[0][1] + x[1][1] + x[2][1]) / 3]

e = 0.001

pwll = powell(e)
nlmd = nelder_mead(e)
print("Powell's solution: ", pwll, "\nSimplex solution: ", nlmd)

levels = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.10, -0.05, -0.01, 0.0, 0.01, 0.05, 0.10,0.20,0.30, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
xg1 = np.arange(-3, 3.125, 0.125)
xg2 = np.arange(-3, 3.125, 0.125)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(f)
yg = f2(xg1, xg2)
cont = plt.contour(xg1, xg2, yg, levels=levels)
plt.plot(pwll[0],pwll[1],color="red", marker=".")
plt.plot(nlmd[0],nlmd[1],color="blue", marker=".")
plt.show()
