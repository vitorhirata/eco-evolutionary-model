from numpy import *
import matplotlib.pyplot as plt

c=1.0
b=5.0799
beta = 5.831E-6
delta = 1.6369
lamb = 150.54
r=348.145


k1 = -2.49E-8
k2 = 3.37E-10

Nestavel=[]
Ninstavel=[]
ni = range(100,25000,10)
niEst=[]
niInst=[]

for i in range(0,len(ni)):
    variacao = ((lamb+b-c)/r + lamb*beta)**2-4*lamb*beta*(lamb+b-c+ni[i])/r
    if (variacao > 0):
        Nestavel.append(((lamb+b-c)/r + lamb*beta+sqrt(((lamb+b-c)/r + lamb*beta)**2-4*lamb*beta*(lamb+b-c+ni[i])/r))/(2*lamb*beta/r))
        niEst.append(ni[i]) #niEst.append(k1*ni[i]+k2*ni[i]*ni[i])
        if ni[i] > 1000:
            Ninstavel.append(((lamb+b-c)/r + lamb*beta-sqrt(((lamb+b-c)/r + lamb*beta)**2-4*lamb*beta*(lamb+b-c+ni[i])/r))/(2*lamb*beta/r))
            niInst.append(ni[i]) #niInst.append(k1*ni[i]+k2*ni[i]*ni[i])


plt.semilogy(niEst, Nestavel,'k', linewidth=2) # 'b-'
plt.semilogy(niInst, Ninstavel, 'k--', linewidth=2) # 'r-'
plt.xlabel(r"Dilution ($ \nu $)")
plt.ylabel("Population (N)")
#plt.ylim(150,1000000)
#plt.xlim(0,25000)
plt.show()

# Em 667 os pontos fixos sao aproximadamente 110069 e 885



#1800 encontro deles
#2,31 E6 encontro nosso

#nosso tem um fator de 1283.3
