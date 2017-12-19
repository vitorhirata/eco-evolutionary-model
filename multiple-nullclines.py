import numpy as np
import matplotlib
import matplotlib.pyplot as plt

c=1.0
b=5.0799
beta = 1.7185E-5
delta = 1.6369
lamb = 150.54
r=348.145

def p3(N, ni):
    return (ni-delta*(N/r-1)*(1-beta*N))/((N/r-1)*(b-c+(1-beta*N)*(lamb-delta)))

N = np.logspace(2.5441, 4.7756, 100000)
#Allni = [1, 30, 200, 500, 1000, 2000, 3000, 5000]
Allni = [1, 30, 200, 400, 800]

N3 = (lamb-delta-c)/(beta*(lamb-delta))
for ni in Allni:
    plt.plot(N,p3(N,ni),'k-')
    plt.scatter(N3,p3(N3,ni), s=50, color='k')


plt.plot(N, p3(N, 73.90), 'k-', linewidth=2.5) # 'r-'
plt.scatter(N3,p3(N3,ni), s=30, color='k')


plt.text(320, 0.06, '1')
plt.text(560, 0.15, '30')
plt.text(670, 0.24, '73.9')
plt.text(1100, 0.35, '200')
plt.text(1600, 0.45, '400')
plt.text(2600, 0.54, '800')

#plt.text(1800, 0.52, '500')
#plt.text(2700, 0.6, '1000')
#plt.text(4500, 0.75, '2000')
#plt.text(6700, 0.85, '3000')
#plt.text(12000, 0.9, '5000')

#plt.axhline(y=0,color='k', linestyle = '--')



#plt.axhline(y=1, color='k', linestyle = '--') # color='c'
#plt.axhline(y=0,color='k', linestyle = '--') # color='c'
#plt.axvline(x=(lamb-delta-c)/(beta*(lamb-delta)),color='k', linestyle = '--') # color='c'
#plt.axvline(x=r,color='k', linestyle = '--') # color='c'
#plt.plot([516,57800,59600],[1,0.086,1],'ko')
#plt.title('Nullclines')
plt.xlabel("Population (N)")
plt.ylabel("Fraction of cooperators (p)")
plt.axis([70, 100000, -0.02, 1.01])
plt.xscale('log')
#plt.show()


matplotlib.rcParams.update({'font.size': 20})
plt.savefig('image/multiple-nullclines.eps', dpi=5000, bbox_inches = "tight", format="eps")
