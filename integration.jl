
#########Modelo deles ##########

theta=750.0
N0=175000/theta
gamma=0.472
T=20.5
k=1.95e5


int_nasc = k*log((k+N0*(exp(gamma*T)-1))/k)
int_morte = k*N0*(gamma*T/N0+log((N0+(k-N0)*exp(-gamma*T))/k)/N0+1/k-1/(N0+(k-N0)*exp(-gamma*T)))
int_theta = N0*(theta-1)


N(t)=k*N0*exp(gamma*t)/(k+N0*(exp(gamma*t)-1))
f(t)=(N(t))^2

gamma*quadgk(N,0,T)[1]
(gamma/k)*quadgk(f,0,T)[1]

N_estavel= k*(1-theta*exp(-gamma*T))/(1-exp(-gamma*T))

###   Modelo nosso ####3

c=1.0
b=5.0799
beta = 5.831E-6
delta = 1.6369
lamb = 150.54
ni = 507.21
r=348.145

e=2500.0
T=1

N= 174993.2



(N^2*((b+lamb)/r+lamb*beta)+N*c)*T*e     #nasce
(lamb*beta*N^3/r+c*N^2/r+N*(b+lamb+ni))*T*e  #morre



N*(N/r-1)*(b-c+lamb)*T*e
(N*N*(N/r-1)*beta*lamb+ni*N)*T*e
