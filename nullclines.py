import numpy as np
import matplotlib.pyplot as plt

c=1
b=8
beta = 1.71E-5
delta = 1.16363
lamb = 150.068
ni = 314.461
r=132.659

def p3(N):
    return (ni-delta*(N/r-1)*(1-N*beta))/((N/r-1)*(b-c+(lamb-delta)*(1-N*beta)))

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
