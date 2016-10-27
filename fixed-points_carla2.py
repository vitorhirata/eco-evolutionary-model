from numpy import *
import matplotlib.pyplot as plt

e=1

c=1.0*e
b=8.0*e
beta = 1/58479.5
lamb = 150.0*e

Nestavel=[]
Ninstavel=[]
ni = range(0,2400000,100)
ni2=[]

for i in range(0,len(ni)):
    Nestavel.append((lamb+b-c+sqrt((lamb+b-c)*(lamb+b-c)-4*ni[i]*beta*lamb))/(2*beta*lamb))
    if ni[i] > 100000:
        Ninstavel.append((lamb+b-c-sqrt((lamb+b-c)**2-4*ni[i]*beta*lamb))/(2*beta*lamb))
        ni2.append(ni[i])

plt.semilogy(ni, Nestavel,'b', linewidth=2)
plt.semilogy(ni2, Ninstavel, 'r', linewidth=2)
plt.xlabel("Diluicao")
plt.ylabel("Populacao")
plt.ylim(300,600000)
plt.show()
