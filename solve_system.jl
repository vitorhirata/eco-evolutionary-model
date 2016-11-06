using NLsolve

c=1
b=8
beta = 1.71E-5
n1=60000.0
n2=500.0
n3=58086.8
p=0.089

# lamb -> x[1], delta -> x[2], r -> x[3], ni -> x[4]

function f!(x, fvec)
  fvec[1] = ((x[1]+b-c)/x[3] + x[1]*beta +sqrt(((x[1]+b-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+b-c+x[4])/x[3]))/(2*beta*x[1]/x[3])-n1
  fvec[2] = ((x[1]+b-c)/x[3] + x[1]*beta -sqrt(((x[1]+b-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+b-c+x[4])/x[3]))/(2*beta*x[1]/x[3])-n2
  u = (x[1]-x[2]-c)/(beta*(x[1]-x[2]))
  fvec[3] = u-n3
  fvec[4] = (x[4]-x[2]*(u/x[3]-1)*(1-beta*u))/((u/x[3]-1)*(b-c+(1-beta*u)*(x[1]-x[2])))-p
end

df = DifferentiableMultivariateFunction(f!)
resultado = nlsolve(df, [150.068;1.16363;132.659;314.461])
println(resultado)
