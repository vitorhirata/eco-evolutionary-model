using NLsolve

n1=1500 #1100
n2=175000 # 155000

#n1=9000
#n2=90000

c=1.0
b=5.0799
r=348.145
lamb = 150.54

#beta -> x[1], ni -> x[2]
function f!(x, fvec)
  fvec[1] = ((lamb+b-c)/r + lamb*x[1]-sqrt(((lamb+b-c)/r + lamb*x[1])^2-4*lamb*x[1]*(lamb+b-c+x[2])/r))/(2*lamb*x[1]/r)-n1
  fvec[2] = ((lamb+b-c)/r + lamb*x[1]+sqrt(((lamb+b-c)/r + lamb*x[1])^2-4*lamb*x[1]*(lamb+b-c+x[2])/r))/(2*lamb*x[1]/r)-n2
end


df = DifferentiableMultivariateFunction(f!)
resultado = nlsolve(df, [5.9E-6;610.687])
println(resultado)



#=
função com lambda e ni como parametros. strong alle

c=1.0
b=5.0799
beta = 5.8E-6
r=348.145

#lamb -> x[1], ni -> x[2]
function f!(x, fvec)
  fvec[1] = ((x[1]+b-c)/r + x[1]*beta-sqrt(((x[1]+b-c)/r + x[1]*beta)^2-4*x[1]*beta*(x[1]+b-c+x[2])/r))/(2*x[1]*beta/r)-n1
  fvec[2] = ((x[1]+b-c)/r + x[1]*beta+sqrt(((x[1]+b-c)/r + x[1]*beta)^2-4*x[1]*beta*(x[1]+b-c+x[2])/r))/(2*x[1]*beta/r)-n2
end



função com beta e ni como parametros. strong alle

c=1.0
b=5.0799
r=348.145
lamb = 150.54

#beta -> x[1], ni -> x[2]
function f!(x, fvec)
  fvec[1] = ((lamb+b-c)/r + lamb*x[1]-sqrt(((lamb+b-c)/r + lamb*x[1])^2-4*lamb*x[1]*(lamb+b-c+x[2])/r))/(2*lamb*x[1]/r)-n1
  fvec[2] = ((lamb+b-c)/r + lamb*x[1]+sqrt(((lamb+b-c)/r + lamb*x[1])^2-4*lamb*x[1]*(lamb+b-c+x[2])/r))/(2*lamb*x[1]/r)-n2
end





função com lambda e ni como parametros. Weak alle

c=1
b=8
beta = 1.71E-5

#lamb -> x[1], ni -> x[2]
function f!(x, fvec)
  fvec[1] = ((x[1]+b-c) -sqrt(((x[1]+b-c))^2-4*x[1]*beta*x[2]))/(2*x[1]*beta)-n1
  fvec[2] = ((x[1]+b-c) +sqrt(((x[1]+b-c))^2-4*x[1]*beta*x[2]))/(2*x[1]*beta)-n2
end

=#
