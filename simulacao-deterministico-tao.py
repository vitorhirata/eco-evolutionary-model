from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

t = arange(0,7, .0001)

# parameters
a = 4
b = -1
c = 3
d = 0
beta = 0.0001

# initial condition:
# Order: numero C, numero D
x0 = array([100, 0])

# the function still receives only `x`, but it will be an array, not a number
def LV(x, t, a, b, c, d, beta):
    # in python, arrays are numbered from 0, so the first element
    # is x[0], the second is x[1]. The square brackets `[ ]` define a
    # list, that is converted to an array using the function `array()`.
    # Notice that the first entry corresponds to dV/dt and the second to dP/dt
    return array([ x[0]*(a*x[0]/(x[0]+x[1]) + b * x[1]/(x[0]+x[1]) + 1 - beta*(x[0]+x[1])),
                   x[1]*(c*x[0]/(x[0]+x[1]) + d * x[1]/(x[0]+x[1]) + 1 - beta*(x[0]+x[1]))])

# call the function that performs the integration
# the order of the arguments is as below: the derivative function,
# the initial condition, the points where we want the solution, and
# a list of parameters
x = odeint(LV, x0, t, (a, b, c, d, beta))

xarray = t
yarray = x[:,0]
data = np.array([xarray, yarray])
data = data.T
savetxt("txt/simulacao-deterministico.txt", data, fmt=['%f','%f'])

# plot the solution
#plot(t, x[:,0], 'r', linewidth=1.0)
#plot(t,x[:,0]+x[:,1]+ x[:,2], 'm', linewidth=2.0)
#xlabel('t') # define label of x-axis
#ylabel('Populations') # and of y-axis
#legend(['N'], loc='upper right')
#show()
