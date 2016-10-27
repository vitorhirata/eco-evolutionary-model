import matplotlib.pyplot as plt
import numpy as np


c=1
b=8
beta = 1.71E-5
delta = 1
lamb = 150
ni = 4.1967E4

a11 = b-c
a12 = -c
a21 = b
a22 = 0.0

#N, p = np.meshgrid(np.arange(0, 0.32*escala, 0.01*escala), np.arange(0, 1, .03))
N, p = np.meshgrid(np.logspace(1.7, 5, 30), np.arange(0, 1, .03))

def p3(N):
    return (ni-delta*N*(1-N*beta))/(N*((b-c)+(lamb-delta)*(1-N*beta)))
Ns = np.logspace(1, 5, 10000)

dN = N*(a11*p*p+(a12+a21)*p*(1-p)+a22*(1-p)*(1-p))+N*(1-N*beta)*(p*lamb+delta*(1-p))-ni
dp = (p*(1-p)*(p*(a11-a21)+(1-p)*(a12-a22)+(1-N*beta)*(lamb-delta)))


dNorm = np.sqrt(dN*dN+dp*dp)

plt.figure()
Q = plt.quiver(N, p, dN/dNorm, dp/dNorm)
plt.title('Espaco de Fase')
plt.xlabel("N")
plt.ylabel("p")
plt.axis([65, 100000, -0.01, 1.01])
plt.xscale('log')
plt.plot(Ns, p3(Ns), 'r')
plt.show()



'''
a11 = 0.0000015
a12 = 0.0000005
a21 = 0.000005
a22 = 0.00000017
ni = 85
beta = 0.000019


a11 = 3
a12 = -1
a21 = 5
a22 = 0
ni = 0.1
beta = 2.4
'''
