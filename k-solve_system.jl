using NLsolve

function solveEDO()
  beta = 1.72E-5

  n1=59600.0
  n2=516.0
  n3=57800
  p=0.086

  finalResults = Array{Array{Float64}}(0)


  for A in 400*rand(10000)+100
    function f!(x, fvec)
      fvec[1] = (x[1]-x[2]+x[3]+A*beta*x[3])/(beta*x[3])  - n1 - n2
      fvec[2] = (x[1]-x[2]+x[3]+1)*A/(beta*x[3])  - n1*n2
      fvec[3] = (1-x[2]/(x[3]-x[4]))/beta-n3
      fvec[4] = (1/x[1])*(1/(n3/A-1)-x[2]*x[4]/(x[3]-x[4]))-p
    end

    df = DifferentiableMultivariateFunction(f!)
    r = try nlsolve(df, [3*rand();3*rand();3*rand();3*rand()]) catch r=nothing end # , method = :newton)

    if r!=nothing && converged(r) && minimum(r.zero) > 0 && (1/A-beta)^2-4*beta/(A*r.zero[4]) < 0 && r.zero[1]>r.zero[2]
      push!(finalResults, push!(r.zero, A))
    end
  end

  b=Float64[]
  c=Float64[]
  lamb=Float64[]
  delta=Float64[]
  r=Float64[]
  if length(finalResults)==0
    println("Sem respostas")
  else
    for v in finalResults
      push!(b, v[1])
      push!(c, v[2])
      push!(lamb, v[3])
      push!(delta, v[4])
      push!(r, v[5])
    end
    writedlm("txt/k-solve_system.txt", finalResults, "; ")
    println("b = ", mean(b), ", std = ", sqrt(var(b)/length(b)))
    println("c = ", mean(c), ", std = ", sqrt(var(c)/length(c)))
    println("lamb = ", mean(lamb), ", std = ", sqrt(var(lamb)/length(lamb)))
    println("delta = ", mean(delta), ", std = ", sqrt(var(delta)/length(delta)))
    println("r = ", mean(r), ", std = ", sqrt(var(r)/length(r)))
  end

end

solveEDO()




#beta=1.673E-5
#b = 0.061755689112537676, std = 0.00015386868863176282
#c = 0.06152802599808961, std = 0.0001624466050834935
#lamb = 1.880260385978254, std = 0.004675291108730277
#delta = 0.016113685436346743, std = 0.0002464598813897998
#r = 335.7539565685764, std = 0.29136546021592047


#beta=1.72E-5
#b = 0.0699655548427271, std = 0.00010960867795217175
#c = 0.012020033026126814, std = 2.5270994960534803e-5
#lamb = 2.0715009383290046, std = 0.0032388940991935323
#delta = 0.013276105090812085, std = 0.0010883343504094172
#r = 350.1322272336786, std = 0.17533334003977102
