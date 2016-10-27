import numpy as np
import matplotlib.pyplot as plt

T=1#.000007
P=1
t_max = .0008/T
nc_init = 100.0
stepsize = t_max/100000.0
a_11 = 7*T*P
k = 58479.5/P
u = 4.1967E4*T
lamb=150*T*P
nmenos = (lamb+a_11 - np.sqrt((lamb+a_11)**2-4*u*lamb/k))/(2*lamb/k)
time = np.arange(0, t_max,stepsize)

def f(nc):
    return nc*nc*(a_11+lamb*(1-nc/k))-u*nc

for i in range(0,20):
    nc = nc_init*pow(1.6,i)
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

plt.ylim(50,1180000)
#plt.xlim(-0.1,7.1)
plt.xlabel("Dias")
plt.ylabel("Populacao total")
plt.title(r"$\nu$ = {}".format(u))
plt.show()
