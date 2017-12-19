import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#ni = 667.0
#beta = 1.673E-5

#c=1.0
#b=10.089
#delta = 150.869
#lamb = 299.9677
#r=162.42

#b, c, lamb, delta, r = [ni*0.0617, ni*0.061528, ni*1.88026, ni*0.01611368, 335.7539565685764]


c=1.0
b=5.0799
beta = 1.7185E-5
delta = 1.6369
lamb = 150.54
ni = 73.90
r=348.145

def p3(N):
    return (ni-delta*(N/r-1)*(1-beta*N))/((N/r-1)*(b-c+(1-beta*N)*(lamb-delta)))

N = np.logspace(2.6, 4.7756, 100000)



plt.plot(N, p3(N), 'k-') # 'r-'
plt.axhline(y=1, color='k', linestyle = '--') # color='c'
plt.axhline(y=0,color='k', linestyle = '--') # color='c'
plt.axvline(x=(lamb-delta-c)/(beta*(lamb-delta)),color='k', linestyle = '--') # color='c'
plt.axvline(x=r,color='k', linestyle = '--') # color='c'
plt.plot([516,57800,59600], [1,0.086,1],'ko')
#plt.title('Nullclines')
plt.xlabel("Population (N)")
plt.ylabel("Fraction of cooperators (p)")
plt.axis([70, 100000, -0.01, 1.01])
plt.xscale('log')
#plt.show()

matplotlib.rcParams.update({'font.size': 20})
plt.savefig('image/nullclines.eps', dpi=5000, bbox_inches = "tight", format="eps")
