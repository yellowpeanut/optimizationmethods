from math import *
import numpy as np
import matplotlib as plt


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


def simplex(e):

    def l3(arr):
        return arr[2]

    maxK = 100000
    n = 2
    a = 1
    b = 2
    g = 0.5
    k = 0.5
    x1 = [-2, -4, 0]
    x2 = [x1[0]+x1[0]*k, x1[1], 0]
    x3 = [x1[0], x1[1]+x1[1]*k, 0]
    x1[2] = f(x1[0], x1[1])
    x2[2] = f(x2[0], x2[1])
    x3[2] = f(x3[0], x3[1])
    x = [x1, x2, x3]

    sig2 = 0
    for i in range(1, n + 1):
        ff = 0
        for j in range(1, n + 1):
            ff += x[j][2]/(n+1)
        sig2 += pow(x[i][2]-ff, 2)/(n+1)

    while(sqrt(sig2)>=e):
        x1[2] = f(x1[0], x1[1])
        x2[2] = f(x2[0], x2[1])
        x3[2] = f(x3[0], x3[1])
        x.sort(key=l3)

        xc = [(x[0][0] + x[1][0]) / n, (x[0][1] + x[1][1]) / n, 0]
        xc[2] = f(xc[0], xc[1])
        y0 = f(xc[0]-xc[2], xc[1]-xc[2])
        x0 = [(1+a)*xc[0]-a*x[2][0], (1+a)*xc[1]-a*x[2][1], 0]
        x0[2] = f(x0[0], x0[1])
        y0 = f(x0[0] - y0, x0[1] - y0)
        if(y0<x[0][2]):
            xr = [(1-b)*xc[0]-b*x0[0], (1-b)*xc[1]-b*x0[1], 0]
            xr[2] = f(xr[0], xr[1])
            yr = f(xr[0]-xr[2], xr[1]-xr[2])
            if(yr<y0):
                x[2] = xr
            else:
                x[2] = x0
        elif(y0<=x[1][2]):
            x[2] = x0
        elif(y0<x[2][2]):
            xg = [(1-g)*xc[0]+g*x0[0], (1-g)*xc[1]+g*x0[1], 0]
            xg[2] = f(xg[0], xg[1])
            yg = f(xg[0]-xg[2], xg[1]-xg[2])
            if(yg<x[2][2]):
                x[2] = xg
        else:
            xg = [(1-g)*xc[0]+g*x[2][0], (1-g)*xc[1]+g*x[2][1], 0]
            xg[2] = f(xg[0], xg[1])
            yg = f(xg[0] - xg[2], xg[1] - xg[2])
            if(yg<x[2][2]):
                x[2] = xg
            else:
                for i in range(1, n + 1):
                    x[i][0] = x[i][0] - (x[i][0] - x[0][0]) / 2
                    x[i][1] = x[i][1] - (x[i][1] - x[0][1]) / 2

        sig2 = 0
        for i in range(1, n + 1):
            ff = 0
            for j in range(1, n + 1):
                ff += x[j][2] / (n + 1)
            sig2 += pow(x[i][2] - ff, 2) / (n + 1)
        maxK -=1
        if(maxK<=0): break

    return [(x[0][0]+x[1][0]+x[2][0])/3, (x[0][1]+x[1][1]+x[2][1])/3]


e = 0.01

print("Powell's solution: ", powell(e), "\nSimplex solution: ", simplex(e))


#xg1, xg2 = np.mgrid[-10:10:5j, -10:10:5j]

#xg1 = np.arange(-10, 10, 0.5)
#xg2 = np.arange(-10, 10, 0.5)
#xx1, xx2 = np.meshgrid(xg1, xg2)
#yg = f(xx1, xx2)
#fgr, cont = plt.subplots()
#cont.contour(yg)

#plt.show()
