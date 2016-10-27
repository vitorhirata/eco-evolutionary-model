import matplotlib.pyplot as plt
from numpy import *


file_C = open('txt/dai-gillespie-A2.txt', 'r')
file_t = open('txt/dai-gillespie-A1.txt', 'r')

ydata = []
xdata = []

for x in file_C:
    ydata.append(float(x))

for x in file_t:
    xdata.append(float(x))


plt.scatter(xdata, ydata, s=0.001, alpha=0.5)
#plt.plot(xdata, ydata, 'b', linewidth=0.5)
#plt.title("Evolucao de C e o ajuste polinomial de ordem 10")
plt.xlabel("t")
plt.ylabel("C(t) - C_ajuste")
plt.yscale('log')
plt.show()
