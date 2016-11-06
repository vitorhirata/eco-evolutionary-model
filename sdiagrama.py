from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

t = arange(0,.05, .000003)

# parameters
c=1
b=8
beta = 1.71E-5
delta = 1.16363
lamb = 150.068
ni = 314.461
r=132.659

# initial condition:
# Order: N, p
x0=[]
x0.append([80000, 0.3])
x0.append([42000, 0.03])
x0.append([500, 0.9])
x0.append([4100, 0.1])
x0.append([3000, 0.5])
x0.append([200, 0.2])
x0.append([150, 0.1])
x0.append([180, 0.9])
x0.append([300, 0.6])
x0.append([1544.4, 0.01])
x0.append([250, 1])
x0.append([300, 1])


def p3(N):
    return 276.0/N

def p33(N):
    return (ni-delta*(N/r-1)*(1-N*beta))/((N/r-1)*(b-c+(lamb-delta)*(1-N*beta)))

# the function still receives only `x`, but it will be an array, not a number
def LV(x, t, b, c, beta, delta, lamb, ni, r):
    # in python, arrays are numbered from 0, so the first element
    # is x[0], the second is x[1]. The square brackets `[ ]` define a
    # list, that is converted to an array using the function `array()`.
    # Notice that the first entry corresponds to dV/dt and the second to dP/dt
    return array([ x[0]*(x[0]/r-1)*(b-c)*x[1]+x[0]*(x[0]/r-1)*(1-x[0]*beta)*(x[1]*lamb+delta*(1-x[1]))-ni*x[0],
                   (x[0]/r-1)*x[1]*(1-x[1])*(-c+(1-x[0]*beta)*(lamb-delta)) ])

# call the function that performs the integration
# the order of the arguments is as below: the derivative function,
# the initial condition, the points where we want the solution, and
# a list of parameters

for i in range(12):
    x = odeint(LV, x0[i], t, (b, c, beta, delta, lamb, ni, r))
    plot(x[:,0],x[:,1],'k', linewidth=1.5)

# Coloca a nullcline
N = arange(270, 40000, 1)
#plot(N,p3(N),'b',linewidth=3)
plot(N,p33(N),'r',linewidth=2)
#Coloca pontos
plot([490,57800,59600],[1,0.086,1],'ko')

#plot the solution
title('')
xlabel("N")
ylabel("p")
axis([65, 100000, -0.01, 1.01])
xscale('log')
show()
