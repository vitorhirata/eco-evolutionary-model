import numpy as np
import matplotlib.pyplot as plt

t_max = int(250)
nc_init = 400000
nd_init = 0
stepsize = 0.00003
k = 140000
u = 8000

n=[0,0]
n[0]=nc_init
n[1]=nd_init

A=[[0,0],[0,0]]
A[0][0]=0.000001
A[0][1]=0.0001
A[1][0]=0.0001
A[1][1]=0.0001

A=np.array(A)
n=np.array(n)

Xc = list(0 for i in range(0,t_max))
Xd = list(0 for i in range(0,t_max)) 
time = list(i for i in range(0,t_max))

Xc[0] = n[0]
Xd[0] = n[1]



for t in range(1, t_max):
	F= A.dot(n)

	
	aux = n[0] + t * stepsize * (n[0] * (F[0] + 1 - (n[0]+n[1])/k)- u*n[0]/(n[0]+n[1]))
	n[1] = n[1] + t * stepsize * (n[1] * (F[1] + 1 - (n[0]+n[1])/k)- u*n[1]/(n[0]+n[1]))
	n[0] = aux	

	if n[0] > 500000000 or n[1] > 50000000:
		break
	

	Xd[t]=n[1]
	Xc[t]=n[0]
	

plt.semilogy(Xc,'r-')
plt.plot(Xd,'b-')
plt.ylim(700,1000000)
plt.show()

