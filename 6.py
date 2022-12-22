import matplotlib.pyplot as plt


def f(t, c1, c2):
    global lamb
    return lamb / (2 - 2 * lamb) * t * t / 2 + c1 * t + c2


def fa(c1, c2):
    return f(0, c1, c2)


def fb(c1, c2):
    return f(1, c1, c2)


def f1(t, c1):
    global lamb
    return lamb / (2 - 2 * lamb) * t + c1


def f1a(c1):
    return f1(0, c1)


def f1b(c1):
    return f1(1, c1)


def assume_f1a(xp1):
    global lamb
    t = 0
    return xp1 - (t * lamb / (2 - 2 * lamb))


def shooting(e, c2, xb):
    c1 = 0
    c2 = c2
    _f1a = 1.0
    xb_flist = []
    xb_found = .0
    f1a_high = None
    f1a_low = None
    while f1a_high is None or f1a_low is None:
        c1 = assume_f1a(_f1a)
        xb_found = fb(c1, c2)
        # print(xb_found, _f1a, "[ ", f1a_low, f1a_high, " ]")
        xb_flist.append(xb_found)
        if abs(xb_found - xb) <= e:
            break
        else:
            if xb_found > xb:
                # print("high")
                f1a_high = _f1a
                _f1a = _f1a - 10
            else:
                # print("low")
                f1a_low = _f1a
                _f1a = _f1a + 10
    while abs(xb_found - xb) > e:
        _f1a = (f1a_low + f1a_high) / 2.0
        c1 = assume_f1a(_f1a)
        xb_found = fb(c1, c2)
        # print(xb_found, _f1a, "[ ", f1a_low, f1a_high, " ]")
        xb_flist.append(xb_found)
        if xb_found > xb:
            f1a_high = _f1a
        else:
            f1a_low = _f1a
    return c1, xb_found, xb_flist


def S(c1, c2):
    return fb(c1, c2) - pow(f1b(c1), 2)


def findLamb(e, c2, xb, res):
    def appendVal():
        c1_arr.append(c1)
        xf_arr.append(xf)
        xf_list_arr.append(xf_list.copy())
        lamb_arr.append(lamb)

    def findDiff():
        appendVal()
        f_res = S(c1, c2)
        f_res_list.append(f_res)
        return abs(f_res - res)

    global lamb
    lamb_arr = [lamb]
    c1 = .0
    c2 = c2
    c1_arr = []
    xf = .0
    xf_arr = []
    xf_list = []
    xf_list_arr = []
    f_res_list = []
    lamb0 = [0.1, None]
    lamb1 = [None, None]
    diff = 0

    lamb = lamb0[0]
    c1, xf, xf_list = shooting(e, c2, xb)
    f_res = S(c1, c2)
    diff = abs(f_res - res)
    lamb0[1] = diff
    lamb += e
    c1, xf, xf_list = shooting(e, c2, xb)
    diff = findDiff()
    lamb1[0], lamb1[1] = lamb, diff
    while lamb1[1] < lamb0[1]:
        lamb += e
        c1, xf, xf_list = shooting(e, c2, xb)
        f_res = S(c1, c2)
        diff = abs(f_res - res)
        lamb0[0], lamb0[1] = lamb1.copy()
        lamb1[0], lamb1[1] = lamb, diff

    lamb = lamb0[0]
    c1, xf, xf_list = shooting(e, c2, xb)

    return c1, c1_arr, lamb_arr, xf_arr, xf_list_arr


def J(c1, c2):
    return pow(f1b(c1), 2)


lamb = 1.1
_e = 1e-5
_ta = 0
_tb = 1
_xa = 0
_xb = .25
_c2 = 0
_res = .08333

_c1, _c2_arr, _lamb_arr, _xf_arr, _xf_list_arr = findLamb(_e, _c2, _xb, _res)
#_c1, _xf, _xf_list = shooting(_e, _c2, _xb)
print("c1 = ", _c1, "\nc2 = ", _c2, "\nlambda = ", lamb, "\nS[x] = ", S(_c1, _c2))

t_points = []
x_points = []
n = 10
for i in range(n):
    t_points.append((_tb * i) / (n - 1))
    x_points.append(f(t_points[-1], _c1, _c2))

#print(t_points, "\n", x_points)
plt.plot(t_points, x_points)
plt.plot(t_points[-1], x_points[-1], ".")
plt.show()


#####################################################################
# old algorithms to find lamb
#####################################################################


#c1, xf, xf_list = shooting(e, c2, xb)
#_res = F(c1, c2)
#diff = abs(f_res - res)

# N = 0
# while N < 1000:
#    lamb = 0.1+e*N*100
#    diffff = findDiff()
#    print(lamb, diffff)
#    N+=1
# lamb = lamb0[0]
# diff = findDiff()
# lamb0[0], lamb0[1] = lamb, diff
# while diff <= lamb0[1]:
#    lamb1[0], lamb1[1] = lamb, diff
#    lamb *= 10
#    diff = findDiff()
# lamb1[0], lamb1[1] = lamb, diff
# print("*10")
# lamb1 = lamb0.copy()
# lamb0[0], lamb0[1] = lamb, diff
# lamb /= 10
# diff = findDiff()
# while diff <= lamb1[1]:
#    lamb1[0], lamb1[1] = lamb, diff
#    lamb /= 10
#    diff = findDiff()
#    print("/10")
# lamb1[0], lamb1[1] = lamb, diff

# while diff > e:
#    #print("eee", diff, lamb)
#    #print(lamb0, lamb1)
#    lamb = (lamb0[0] + lamb1[0]) / 2.0
#    diff = findDiff()
#    tlamb = lamb
#    lamb = (lamb0[0] + tlamb) / 2.0
#    diff0 = findDiff()
#    lamb = (lamb1[0] + tlamb) / 2.0
#    diff1 = findDiff()
#    lamb = tlamb
#    if diff0 < diff1:
#        lamb1[0], lamb1[1] = lamb, diff
#    else:
#        lamb0[0], lamb0[1] = lamb, diff
