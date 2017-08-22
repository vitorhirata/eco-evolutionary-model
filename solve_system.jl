using NLsolve


beta = 1.7185E-5
c=2.2
r = 472.2

n1=59600.0
n2=516.0
n3=57800
p=0.086


#lamb -> x[1], delta -> x[2], b -> x[3], ni -> x[4]
function f!(x, fvec)
  fvec[1] = ((x[1]+x[3]-c)+r*x[1]*beta)/(beta*x[1])-n1-n2
  fvec[2] = r*(x[1]+x[3]-c+x[4])/(beta*x[1])-n1*n2
  u = (1-c/(x[1]-x[2]))/beta
  fvec[3] = u-n3
  fvec[4] = (x[3]*r-u*x[2]*(1-beta*u)+sqrt((x[3]*r-u*x[2]*(1-beta*u))^2+4*u*x[3]*r*(x[4]+x[2]*(1-beta*u))))/(2*x[3]*u)-p
end

df = DifferentiableMultivariateFunction(f!)
resultado = nlsolve(df, [150.0;140.0;4.0;56.4])
println(resultado)



#=
função com lambda, delta, r e ni como parametros

#lamb -> x[1], delta -> x[2], r -> x[3], ni -> x[4]
function f!(x, fvec)
  fvec[1] = ((x[1]+b-c)+ x[3]*x[1]*beta)/(beta*x[1])-n1-n2
  fvec[2] = x[3]*(x[1]+b-c+x[4])/(beta*x[1])-n1*n2
  u = (x[1]-x[2]-c)/(beta*(x[1]-x[2]))
  fvec[3] = u-n3
  fvec[4] = (b*x[3]-u*x[2]*(1-beta*u)+sqrt((b*x[3]-u*x[2]*(1-beta*u))^2+4*u*b*x[3]*(x[4]+x[2]*(1-beta*u))))/(2*b*u)-p
end


função com b, c, r e ni como parametros
# b -> x[1], c -> x[2], r -> x[3], ni -> x[4]
function f!(x, fvec)
  fvec[1] = ((lamb+x[1]-x[2])+ x[3]*lamb*beta)/(beta*lamb)-n1-n2
  fvec[2] = x[3]*(lamb+x[1]-x[2]+x[4])/(beta*lamb)-n1*n2
  u = (lamb-delta-x[2])/(beta*(lamb-delta))
  fvec[3] = u-n3
  fvec[4] = (x[1]*x[3]-u*delta*(1-beta*u)+sqrt((x[1]*x[3]-u*delta*(1-beta*u))^2+4*u*x[1]*x[3]*(x[4]+delta*(1-beta*u))))/(2*x[1]*u)-p
end

função com lambda, delta, beta e b como parametros

#lamb -> x[1], delta -> x[2], beta -> x[3], b -> x[4]
function f!(x, fvec)
  fvec[1] = ((x[1]+x[4]-c)/r + x[1]*x[3] +sqrt(((x[1]+x[4]-c)/r + x[1]*x[3])^2-4*x[3]*x[1]*(x[1]+x[4]-c+ni)/r))/(2*x[3]*x[1]/r)-n1
  fvec[2] = ((x[1]+x[4]-c)/r + x[1]*x[3] -sqrt(((x[1]+x[4]-c)/r + x[1]*x[3])^2-4*x[3]*x[1]*(x[1]+x[4]-c+ni)/r))/(2*x[3]*x[1]/r)-n2
  u = (x[1]-x[2]-c)/(x[3]*(x[1]-x[2]))
  fvec[3] = u-n3
  fvec[4] = (ni-x[2]*(u/r-1)*(1-x[3]*u))/((u/r-1)*(x[4]-c+(1-x[3]*u)*(x[1]-x[2])))-p
end


#lamb -> x[1], delta -> x[2], ni -> x[3], b -> x[4]



=#
