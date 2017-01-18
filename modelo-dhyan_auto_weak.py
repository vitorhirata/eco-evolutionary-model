from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

c=1
b=8
beta = 1.71E-5
delta = 1.1
lamb = 8.08678
ni = 16428.137

T=.00002
P=1
b=b*T*P
c=c*T*P
beta = beta*P
ni = ni*T
lamb=lamb*T*P


t_max = .000135/T
t = arange(0,t_max, .00000001/T)
nmenos = ((lamb+b-c) -sqrt(((lamb+b-c))**2-4*lamb*beta*ni))/(2*lamb*beta)
nc_init = 800
x0 = array([nc_init])

def LV(x, t, b, c, beta, ni, lamb):
    return array([x[0]*x[0]*(b-c+lamb*(1-x[0]*beta))-ni*x[0] ])

for i in range(0,15):
    if nc_init*pow(1.35,i) < nmenos:
        x0 = array([nc_init*pow(1.35,i)])
    else:
        x0 = array([nc_init*pow(1.6,i)])
    x = odeint(LV, x0, t, (b,c, beta, ni, lamb))
    if x0[0] < nmenos:
        plt.semilogy(t, x, 'r-')
    else:
        plt.semilogy(t, x, 'b-')

plt.ylim(500,1100000)
plt.xlim(-0.1,t_max)
plt.xlabel("Dias")
plt.ylabel("Populacao total")
plt.title(r"$\nu$ = {}".format(ni))
plt.show()
