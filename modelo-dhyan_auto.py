from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

c=1.0
b=5.0799
beta = 5.831E-6
delta = 1.6369
lamb = 150.54
ni = 2480.0 #507.21 # 2480.0
r=348.145

T=.0004
P=1
b=b*T*P
c=c*T*P
beta = beta*P
ni = ni*T
lamb=lamb*T*P
r=r*P

t_max = .0027/T
t = arange(0,t_max, .00000001/T)
nmenos = ((lamb+b-c)/r + lamb*beta-sqrt(((lamb+b-c)/r + lamb*beta)**2-4*lamb*beta*(lamb+b-c+ni)/r))/(2*lamb*beta/r)
nc_init = 800
x0 = array([nc_init])

print(nmenos)
nmais = ((lamb+b-c)/r + lamb*beta+sqrt(((lamb+b-c)/r + lamb*beta)**2-4*lamb*beta*(lamb+b-c+ni)/r))/(2*lamb*beta/r)
print(nmais)

def LV(x, t, b, c, beta, ni, lamb, r):
    return array([x[0]*(x[0]/r-1)*(b-c+lamb*(1-x[0]*beta))-ni*x[0] ])

for i in range(0,17):
    x0 = array([nc_init*pow(1.5,i)])
    x = odeint(LV, x0, t, (b,c, beta, ni, lamb, r))
    if x0[0] < nmenos:
        plt.semilogy(t, x, 'r-')
    else:
        plt.semilogy(t, x, 'b-')

x0 = array([nmenos-50])
x = odeint(LV, x0, t, (b,c, beta, ni, lamb, r))
plt.semilogy(t, x, 'r-')

x0 = array([nmenos+50])
x = odeint(LV, x0, t, (b,c, beta, ni, lamb, r))
plt.semilogy(t, x, 'b-')

ni=ni/T
plt.ylim(500,1100000)
plt.xlim(-0.1,t_max)
plt.xlabel("Dias")
plt.ylabel("Populacao total")
plt.title(r"$\nu$ = {}".format(ni))
#plt.show()
