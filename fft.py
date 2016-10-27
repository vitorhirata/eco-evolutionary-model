import matplotlib.pyplot as plt
import scipy.fftpack
from numpy import *

file_C = open('txt/tao-gillespie-varios1.txt', 'r')
file_t = open('txt/tao-gillespie-varios2.txt', 'r')

C = []
C_fft = []

for x in file:
    C.append(float(x))


#C_fft = scipy.fftpack.fft(C)
time=linspace(0,len(C),num=len(C))

#foo = C + time

plt.plot(time, C)
plt.show()
#plt.hist(auto)
#plt.title("Histograma de C")
#plt.xlabel("C")
#plt.ylabel("Frequency")
