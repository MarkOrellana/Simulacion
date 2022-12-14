import random
print
print «este programa le indicara un valor aproximado de pi por el metodo montecarlo»
print
print «ingrese un numero natural n que indicara el numero de veces a iterar el proceso»
print
n=input(«n = «)
print
i=0.0
j=0.0
while j<=n:
x=random.random()
y=random.random()
if x**2+y**2<=1:
i=i+1
j=j+1
print "un valor aproximado de pi es", (i/j)*4
print
print "gracias por usar este programa"
print