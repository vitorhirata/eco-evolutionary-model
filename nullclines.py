import numpy as np
import matplotlib.pyplot as plt

c=0.1
b=4
beta = 1.73E-5
delta = 10.1
lamb = 84
ni = 10.1967E4

def p3(N):
    return (ni-delta*N*(1-N*beta))/(N*((b-c)+(lamb-delta)*(1-N*beta)))

N = np.logspace(1, 5, 10000)

plt.figure()
plt.plot(N, p3(N), 'r')
plt.axhline(y=1,color='c')
plt.axhline(y=0,color='c')
plt.axvline(x=(lamb-delta-c)/(beta*(lamb-delta)),color='c')
#plt.plot([276,57800,59600],[1,0.086,1],'ko')
plt.title('Nullclines')
plt.xlabel("N")
plt.ylabel("p")
plt.axis([70, 100000, -0.1, 1.01])
plt.xscale('log')
plt.show()
