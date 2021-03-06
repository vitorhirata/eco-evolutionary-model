using NLsolve

function solveEDO()
  ni = 667.00
  beta = 1.7185E-5
  c = 50.549

  n1=59600.0
  n2=516.0
  n3=57800
  p=0.086

  finalResults = Array{Array{Float64}}(0)

  for c in 70*rand(10000)
    #lamb -> x[1], delta -> x[2], r -> x[3], b -> x[4]
    function f!(x, fvec)
      fvec[1] = ((x[1]+x[4]-c)/x[3] + x[1]*beta +sqrt(((x[1]+x[4]-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+x[4]-c+ni)/x[3]))/(2*beta*x[1]/x[3])-n1
      fvec[2] = ((x[1]+x[4]-c)/x[3] + x[1]*beta -sqrt(((x[1]+x[4]-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+x[4]-c+ni)/x[3]))/(2*beta*x[1]/x[3])-n2
      u = (x[1]-x[2]-c)/(beta*(x[1]-x[2]))
      fvec[3] = u-n3
      fvec[4] = (ni-x[2]*(u/x[3]-1)*(1-beta*u))/((u/x[3]-1)*(x[4]-c+(1-beta*u)*(x[1]-x[2])))-p
    end

    df = DifferentiableMultivariateFunction(f!)
    r = try nlsolve(df, [rand()*150+10;rand()*100;rand()*300;rand()*100]) catch r=nothing end # , method = :newton)

    if r!=nothing && converged(r) && minimum(r.zero) > 0
      push!(finalResults, push!(r.zero, c))
    end


  end

  if length(finalResults)==0
    println("Sem respostas")
  else
    ni = 667.00
    beta = 1.7185E-5
    for v in finalResults
      lamb=v[1]
      delta=v[2]
      r=v[3]
      b=v[4]
      c=v[5]
      if (delta/r + delta*beta)^2-4*beta*delta*(delta+b-c+ni)/r < 0
        println(v)
      end
    end
  end
end

solveEDO()


#=
função com lambda, delta, r e ni como parametros

#lamb -> x[1], delta -> x[2], r -> x[3], ni -> x[4]
function f!(x, fvec)
  fvec[1] = ((x[1]+b-c)/x[3] + x[1]*beta +sqrt(((x[1]+b-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+b-c+x[4])/x[3]))/(2*beta*x[1]/x[3])-n1
  fvec[2] = ((x[1]+b-c)/x[3] + x[1]*beta -sqrt(((x[1]+b-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+b-c+x[4])/x[3]))/(2*beta*x[1]/x[3])-n2
  u = (x[1]-x[2]-c)/(beta*(x[1]-x[2]))
  fvec[3] = u-n3
  fvec[4] = (x[4]-x[2]*(u/x[3]-1)*(1-beta*u))/((u/x[3]-1)*(b-c+(1-beta*u)*(x[1]-x[2])))-p
end


função com b, c, r e ni como parametros

# b -> x[1], c -> x[2], r -> x[3], ni -> x[4]
function f!(x, fvec)
  fvec[1] = ((lamb+x[1]-x[2])/x[3]+lamb*beta + sqrt(((lamb+x[1]-x[2])/x[3]+lamb*beta)^2-4*beta*lamb*(lamb+x[1]-x[2]+x[4])/x[3]))/ (2*beta*lamb/x[3]) - n1
  fvec[2] = ((lamb+x[1]-x[2])/x[3]+lamb*beta - sqrt(((lamb+x[1]-x[2])/x[3]+lamb*beta)^2-4*beta*lamb*(lamb+x[1]-x[2]+x[4])/x[3]))/ (2*beta*lamb/x[3]) - n2
  u = (lamb-delta-x[2])/(beta*(lamb-delta))
  fvec[3] = u-n3
  fvec[4] = (x[4]-delta*(u/x[3]-1)*(1-beta*u))/((u/x[3]-1)*(x[1]-x[2]+(1-beta*u)*(lamb-delta)))-p
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



#lamb -> x[1], delta -> x[2], r -> x[3], b -> x[4]
function f!(x, fvec)
  fvec[1] = ((x[1]+x[4]-c)/x[3] + x[1]*beta +sqrt(((x[1]+x[4]-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+x[4]-c+ni)/x[3]))/(2*beta*x[1]/x[3])-n1
  fvec[2] = ((x[1]+x[4]-c)/x[3] + x[1]*beta -sqrt(((x[1]+x[4]-c)/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+x[4]-c+ni)/x[3]))/(2*beta*x[1]/x[3])-n2
  u = (x[1]-x[2]-c)/(beta*(x[1]-x[2]))
  fvec[3] = u-n3
  fvec[4] = (ni-x[2]*(u/x[3]-1)*(1-beta*u))/((u/x[3]-1)*(x[4]-c+(1-beta*u)*(x[1]-x[2])))-p
end


#lamb -> x[1], c -> x[2], r -> x[3], b -> x[4]
function f!(x, fvec)
  fvec[1] = ((x[1]+x[4]-x[2])/x[3] + x[1]*beta +sqrt(((x[1]+x[4]-x[2])/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+x[4]-x[2]+ni)/x[3]))/(2*beta*x[1]/x[3])-n1
  fvec[2] = ((x[1]+x[4]-x[2])/x[3] + x[1]*beta -sqrt(((x[1]+x[4]-x[2])/x[3] + x[1]*beta)^2-4*beta*x[1]*(x[1]+x[4]-x[2]+ni)/x[3]))/(2*beta*x[1]/x[3])-n2
  u = (x[1]-delta-x[2])/(beta*(x[1]-delta))
  fvec[3] = u-n3
  fvec[4] = (ni-delta*(u/x[3]-1)*(1-beta*u))/((u/x[3]-1)*(x[4]-x[2]+(1-beta*u)*(x[1]-delta)))-p
end


=#
