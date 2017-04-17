import numpy as np
import matplotlib.pyplot as plt

c=1.0
b=5.0799
beta = 1.7185E-5
delta = 1.6369
lamb = 150.54
ni = 73.90
r=348.145

def a11(N):
    return (b-c+lamb*(1-beta*N))*(N/r-1)-ni

def a12(N):
    return (-c+lamb*(1-beta*N))*(N/r-1)-ni

def a21(N):
    return (b+delta*(1-beta*N))*(N/r-1)-ni

def a22(N):
    return (delta*(1-beta*N))*(N/r-1)-ni


N = np.logspace(1.6, 4.8056, 100000)

plt.axvline(x=57800,color='k', linestyle = '--') # color='c'

plt.plot(N, a11(N), 'k', linewidth=1)
plt.plot(N, a12(N), 'r', linewidth=1)
plt.plot(N, a21(N), 'g', linewidth=1)
plt.plot(N, a22(N), 'c', linewidth=1)

plt.xlabel("Population (N)")
plt.ylabel("Payoff value")
plt.xlim([100, 100000])
plt.xscale('log')
plt.show()
