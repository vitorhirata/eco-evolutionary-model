from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

T=.000007
P=1
a_11 = 7*T*P
k = 58479.5/P
u = 4.1967E4*T
lamb=150*T*P
t_max = .00001/T

nmenos = (lamb+a_11 - sqrt((lamb+a_11)**2-4*u*lamb/k))/(2*lamb/k)
t = arange(0,t_max, .000000001/T)
nc_init = 100
x0 = array([100])

def LV(x, t, a_11, k, u, lamb):
    return array([x[0]*x[0]*(a_11+lamb*(1-x[0]/k))-u*x[0] ])

for i in range(0,22):
    x0 = array([nc_init*pow(1.8,i)])
    x = odeint(LV, x0, t, (a_11, k, u, lamb))
    if x0[0] < nmenos:
        plt.semilogy(t, x, 'r-')
    else:
        plt.semilogy(t, x, 'b-')

plt.ylim(50,1180000)
plt.xlim(-4000*t_max*T,t_max)
plt.xlabel("Dias")
plt.ylabel("Populacao total")
plt.title(r"$\nu$ = {}".format(u))
plt.show()
