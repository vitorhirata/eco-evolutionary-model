from numpy import *

#escala = 215000
escala = 1

a11 = 1.1/escala
a12 = 1.0/escala
a21 = 11.0/escala
a22 = 0.0/escala
ni = .1*escala
beta = 3.4/escala

p1=0
p2=1
p3 = (a22-a12)/(a11-a12-a21+a22)
N1 = (1 + sqrt(1-4*ni*(beta-a22)))/(2*(beta-a22))
N2 = (1 - sqrt(1-4*ni*(beta-a22)))/(2*(beta-a22))
N3 = (1 + sqrt(1-4*ni*(beta-a11)))/(2*(beta-a11))
N4 = (1 - sqrt(1-4*ni*(beta-a11)))/(2*(beta-a11))
X = (a11*(a22-a12)*(a22-a12)+(a12+a21)*(a22-a12)*(a11-a21)+a22*(a11-a21)*(a11-a21))/((a11-a21-a12+a22)*(a11-a21-a12+a22))
N5 = (1 + sqrt(1-4*ni*(beta-X)))/(2*(beta-X))
N6 = (1 - sqrt(1-4*ni*(beta-X)))/(2*(beta-X))
estN1 = 2*N1*(a22-beta)+1
estN2 = 2*N2*(a22-beta)+1
estN3 = 2*N3*(a11-beta)+1
estN4 = 2*N4*(a11-beta)+1
estN5 = 2*N5*(X-beta)+1
estN6 = 2*N6*(X-beta)+1
estp1 = a12-a22
estp2 = a21-a11
estp3 = a11-a21

print X

print "(%.2f, %.2f)." % (p1, N1),
if estp1 < 0:
    print "Eh estavel em p.    ",
else:
    print "Nao eh estavel em p.",
if estN1 < 0:
    print "Eh estavel em N."
else:
    print "Nao eh estavel em N."

print "(%.2f, %.2f)." % (p1, N2),
if estp1 < 0:
    print "Eh estavel em p.    ",
else:
    print "Nao eh estavel em p.",
if estN2 < 0:
    print "Eh estavel em N."
else:
    print "Nao eh estavel em N."

print "(%.2f, %.2f)." % (p2, N3),
if estp2 < 0:
    print "Eh estavel em p.    ",
else:
    print "Nao eh estavel em p.",
if estN3 < 0:
    print "Eh estavel em N."
else:
    print "Nao eh estavel em N."

print "(%.2f, %.2f)." % (p2, N4),
if estp2 < 0:
    print "Eh estavel em p.    ",
else:
    print "Nao eh estavel em p.",
if estN4 < 0:
    print "Eh estavel em N."
else:
    print "Nao eh estavel em N."

print "(%.2f, %.2f)." % (p3, N5),
if estp3 < 0:
    print "Eh estavel em p.    ",
else:
    print "Nao eh estavel em p.",
if estN5 < 0:
    print "Eh estavel em N."
else:
    print "Nao eh estavel em N."

print "(%.2f, %.2f)." % (p3, N6),
if estp3 < 0:
    print "Eh estavel em p.    ",
else:
    print "Nao eh estavel em p.",
if estN6 < 0:
    print "Eh estavel em N."
else:
    print "Nao eh estavel em N."
