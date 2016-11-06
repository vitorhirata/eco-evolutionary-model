from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

c=1
b=8
beta = 1.71E-5
lamb = 150.068
delta = 1.16363
ni = 614.461
r=132.659

T=.00002
P=1
b=b*T*P
c=c*T*P
beta = beta*P
ni = ni*T
lamb=lamb*T*P
r=r*P

t_max = .0008/T
t = arange(0,t_max, .000000001/T)
nmenos = ((lamb+b-c)/r + lamb*beta -sqrt(((lamb+b-c)/r + lamb*beta)**2-4*lamb*beta*(lamb+b-c+ni)/r))/(2*lamb*beta/r)
nc_init = 150
x0 = array([nc_init])

def LV(x, t, b, c, beta, ni, lamb):
    return array([x[0]*(x[0]/r-1)*(b-c+lamb*(1-x[0]*beta))-ni*x[0] ])

for i in range(0,14):
    x0 = array([nc_init*pow(1.7,i)])
    x = odeint(LV, x0, t, (b,c, beta, ni, lamb))
    if x0[0] < nmenos:
        plt.semilogy(t, x, 'r-')
    else:
        plt.semilogy(t, x, 'b-')

plt.ylim(100,1180000)
plt.xlim(-4000*t_max*T,t_max)
plt.xlabel("Dias")
plt.ylabel("Populacao total")
plt.title(r"$\nu$ = {}".format(ni))
plt.show()
