import numpy as np
import matplotlib.pyplot as plt

e=0.004
t_max = 7
nc_init = 800.0
stepsize = 0.001
a_11 = 7*e
k = 58479.5
u = 8.8E5*e
lamb=150*e
nmenos = (lamb+a_11 - np.sqrt((lamb+a_11)**2-4*u*lamb/k))/(2*lamb/k)
time = np.arange(0, t_max,stepsize)

def f(nc):
    return nc*(a_11+lamb*(1-nc/k))-u

for i in range(0,20):
    nc = nc_init*pow(1.5,i)
    key = True
    X=[]

    if nc < nmenos:
    	key = False

    for j in time:
        X.append(nc)
        k1C = stepsize * f(nc)
        k2C = stepsize * f(nc + k1C / 2)
        k3C = stepsize * f(nc + k2C / 2)
        k4C = stepsize * f(nc + k3C)
        nc = nc + (k1C + 2 * k2C + 2 * k3C + k4C) / 6.0

    if key == False:
        plt.semilogy(time, X, 'r-')
    else:
        plt.semilogy(time, X, 'b-')

plt.ylim(700,1180000)
plt.xlabel("Dias")
plt.ylabel("Populacao total")
plt.title(r"$\nu$ = {}".format(u))
plt.show()
