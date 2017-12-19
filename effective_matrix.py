import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

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

#### Seta configuracoes iniciais
ax = plt.figure().add_subplot(111)
plt.xlabel(r"Population ($N \times 10^4$)")
plt.ylabel("Effective Payoffs")
plt.xticks([55000, 56000,57000, 57800,59000, 60000, 61000])
ax.xaxis.set_ticklabels(['5.5', '5.6','5.7', r'$N_3$', '5.9', '6.0', '6.1'])

#### Legendas
ax.text(56400, 560, 'Harmony\nGame', fontsize = 18)
ax.text(58200, 100, 'PD\nGame', fontsize = 18)
ax.text(54700, 780, r'$\overline{a_{21}}$', fontsize = 18)
ax.text(54700, -130, r'$\overline{a_{22}}$', fontsize = 18)
ax.text(56300, 300, r'$\overline{a_{12}}$', fontsize = 18)
ax.text(59050, 300, r'$\overline{a_{11}}$', fontsize = 18)

###  Plota as curvas
N = np.arange(54500, 61000, 50)
plt.axvline(x=57800,color='k', linestyle = '--', linewidth = 1.5)
plt.axvline(x=55814.2,color='k', linestyle = ':', linewidth = 1.5)
plt.axvline(x=59784,color='k', linestyle = ':', linewidth = 1.5)
plt.plot(N, a11(N), 'k', linewidth=1.8) # 'k',
plt.plot(N, a12(N), 'k', linewidth=1.8) # 'r'
plt.plot(N, a21(N), 'k', linewidth=1.8) # 'g'
plt.plot(N, a22(N), 'k', linewidth=1.8) # 'c'
plt.axis([54500, 61000, -500, 1000])
#plt.show()

#ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
#ax.ticklabel_format(style="sci",axis="x",scilimits=(0,0))
matplotlib.rcParams.update({'font.size': 20})
plt.savefig('image/effective.eps', dpi=5000, bbox_inches = "tight", format="eps")

#### Grafico do espaco inteiro
#N = np.logspace(1.6, 4.8056, 100000)
#plt.xlim([100, 100000])
#plt.xscale('log')
