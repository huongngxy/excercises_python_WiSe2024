Zukunftswert = 100*(1+0.03)**10

print(Zukunftswert)

import math

P0 = 1 
minute = 60 
sekunde = 60
tage = 365
stunden = 24
i = 1
P4 = P0*math.e**i*minute*sekunde*stunden*tage


P = 1
t= 1 
i = 1
n = 365*24*60
A = P*(1+i/n)**(t*n)
print(A)

