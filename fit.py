import matplotlib.pyplot as plt
from numpy import *

def func (x):
    return 0



file_C = open('txt/tao-gillespie-varios1.txt', 'r')
file_t = open('txt/tao-gillespie-varios2.txt', 'r')

ydata = []
xdata = []
nulo = 0*xdata

for x in file_C:
    ydata.append(float(x))

for x in file_t:
    xdata.append(float(x))

z = polyfit(xdata, ydata, 10)
f = poly1d(z)

y_new = f(xdata)



plt.plot(xdata, y_new, 'r',linewidth=0.5)
plt.plot(xdata, ydata, 'b', linewidth=0.5)
#plt.axhline(y=0)
plt.title("Evolucao de C e o ajuste polinomial de ordem 10")
plt.axis([0.01, 0.035, 5000, 60000])
plt.xlabel("t")
plt.ylabel("C(t) - C_ajuste")
plt.show()
