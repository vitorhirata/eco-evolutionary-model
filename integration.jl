N0=175000/750.0
gamma=0.439
T=20.5
k=1.76e5




N(t)=k*N0*exp(gamma*t)/(k+N0*(exp(gamma*t)-1))
f(t)=(N(t))^2

quadgk(f,0,T)
quadgk(N,0,T)







c=1.0
b=5.0799
beta = 5.831E-6
delta = 1.6369
lamb = 150.54
ni = 507.21
r=348.145

e=2500.0
T=20.5



(N^2*((b+lamb)/r+lamb*beta)+N*c)*T*e
(lamb*beta*N^3/r+c*N^2/r+N*(b+lamb+ni))*T*e
