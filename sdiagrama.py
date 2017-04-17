import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from scipy.integrate import odeint

def add_arrow_to_line2D(
    axes, line, arrow_locs=[0.2, 0.4, 0.6, 0.8],
    arrowstyle='-|>', arrowsize=1.5, transform=None):
    """
    Add arrows to a matplotlib.lines.Line2D at selected locations.

    Parameters:
    -----------
    axes:
    line: list of 1 Line2D obbject as returned by plot command
    arrow_locs: list of locations where to insert arrows, % of total length
    arrowstyle: style of the arrow
    arrowsize: size of the arrow
    transform: a matplotlib transform instance, default to data coordinates

    Returns:
    --------
    arrows: list of arrows
    """
    if (not(isinstance(line, list)) or not(isinstance(line[0],
                                           mlines.Line2D))):
        raise ValueError("expected a matplotlib.lines.Line2D object")
    x, y = line[0].get_xdata(), line[0].get_ydata()

    arrow_kw = dict(arrowstyle=arrowstyle, mutation_scale=10 * arrowsize)

    color = line[0].get_color()
    use_multicolor_lines = isinstance(color, np.ndarray)
    if use_multicolor_lines:
        raise NotImplementedError("multicolor lines not supported")
    else:
        arrow_kw['color'] = color

    linewidth = line[0].get_linewidth()
    if isinstance(linewidth, np.ndarray):
        raise NotImplementedError("multiwidth lines not supported")
    else:
        arrow_kw['linewidth'] = linewidth

    if transform is None:
        transform = axes.transData

    arrows = []
    for loc in arrow_locs:
        s = np.cumsum(np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2))
        n = np.searchsorted(s, s[-1] * loc)
        arrow_tail = (x[n], y[n])
        arrow_head = (np.mean(x[n:n + 2]), np.mean(y[n:n + 2]))
        p = mpatches.FancyArrowPatch(
            arrow_tail, arrow_head, transform=transform,
            **arrow_kw)
        axes.add_patch(p)
        arrows.append(p)
    return arrows




t = np.arange(0,.1, .000003)

# parameters
c=1.0
b=5.0799
beta = 1.7185E-5
delta = 1.6369
lamb = 150.54
ni = 73.90
r=348.145

# initial condition:
# Order: N, p
x0=[]
x0.append([80000, 0.3])
x0.append([42000, 0.03])
x0.append([1200, 0.6])
x0.append([4100, 0.1])
x0.append([3000, 0.5])
x0.append([500, 0.4])
x0.append([400, 0.1])
x0.append([330, 0.88])
x0.append([300, 0.6])
x0.append([1393.0, 0.01])
x0.append([440, 1])
x0.append([600, 1])
x0.append([17000, 0.25])
x0.append([450, 0.75])
x0.append([670, 0.2])


def p3(N):
    return 516.0/N

def p33(N):
    return (ni-delta*(N/r-1)*(1-beta*N))/((N/r-1)*(b-c+(1-beta*N)*(lamb-delta)))

# the function still receives only `x`, but it will be an array, not a number
def LV(x, t, b, c, beta, delta, lamb, ni, r):
    # in python, arrays are numbered from 0, so the first element
    # is x[0], the second is x[1]. The square brackets `[ ]` define a
    # list, that is converted to an array using the function `array()`.
    # Notice that the first entry corresponds to dV/dt and the second to dP/dt
    return np.array([ x[0]*(x[0]/r-1)*(b-c)*x[1]+x[0]*(x[0]/r-1)*(1-x[0]*beta)*(x[1]*lamb+delta*(1-x[1]))-ni*x[0],
                   (x[0]/r-1)*x[1]*(1-x[1])*(-c+(1-x[0]*beta)*(lamb-delta)) ])

# call the function that performs the integration
# the order of the arguments is as below: the derivative function,
# the initial condition, the points where we want the solution, and
# a list of parameters


fig, ax = plt.subplots(1, 1)


for i in range(15):
    X = odeint(LV, x0[i], t, (b, c, beta, delta, lamb, ni, r))

    x = X[:,0]
    y = X[:,1]

    # print the line and the markers in seperate steps
    line = ax.plot(x, y, 'k-')

    arrow_locs=np.linspace(0.01, 0.9, 6)
    if i == 4:
        arrow_locs = np.append(arrow_locs, (0.9698, 0.9716, 0.974))

    add_arrow_to_line2D(ax, line, arrow_locs)



# Coloca a nullcline
N = np.arange(400, 40000, 1)
#plot(N,p3(N),'b',linewidth=3)
plt.plot(N,p33(N),'k--',linewidth=1.5) # 'r-'
#Coloca pontos
plt.plot([516,57800,59600],[1,0.086,1],'ko')

#plot the solution
plt.title('')
plt.xlabel("Population (N)")
plt.ylabel("Fraction of cooperators (p)")
plt.axis([65, 100000, -0.01, 1.01])
plt.xscale('log')
plt.show()
