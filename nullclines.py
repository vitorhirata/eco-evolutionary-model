import numpy as np
import matplotlib.pyplot as plt

beta = 1.7185E-5
c=0.770919
b=14.57413
delta = 441.615
lamb = 556.558
ni = 39.2078
r=482.5397

def p3(N):
    X = b-c+(1-beta*N)*(lamb-delta)
    return ((X*r-N*(1-beta*N)*delta)+np.sqrt((X*r-N*(1-beta*N)*delta)**2+4*N*X*r*((1-beta*N)*delta+ni)))/(2*N*X)

def p33(N):
    return r/N


N = np.logspace(2.6, 7, 100000)

plt.plot(N, p3(N), 'k-') # 'r-'
plt.plot(N, p33(N), linestyle = '--') # 'r-'
plt.axhline(y=1, color='k', linestyle = '--') # color='c'
plt.axhline(y=0,color='k', linestyle = '--') # color='c'
plt.axvline(x=(lamb-delta-c)/(beta*(lamb-delta)),color='k', linestyle = '--') # color='c'
plt.axvline(x=r,color='k', linestyle = '--') # color='c'
plt.plot([516,57800,59600],[1,0.086,1],'ko')
#plt.title('Nullclines')
plt.xlabel("Population (N)")
plt.ylabel("Fraction of cooperators (p)")
plt.axis([70, 100000, -0.01, 1.01])
plt.xscale('log')

print(p3(516.0), p3(57800))

plt.show()
