# Übung 4: 
# Meine Lösung: 
quad_zahl=[]

for i in range(1,10):
    if i%2 == 0:
        quad_zahl.append(i)
    else: 
        quad_zahl.append(i**2)
        print(quad_zahl)

quad_zahl

# Übung 5
# Meine Lösung: 


def geo_reihe1(r,a,n):
    Geo_Reihe = []
    for i in range(0,n-1):
        Geo_Reihe.append(a*r**i)
    return(Geo_Reihe)
geo_reihe1(0.5,1,10)
#print(Geo_Reihe)
#print(geo_reihe1(0.5,1,10))
#sum(Geo_Reihe)

# Lösung 2: 
a = 1
r = 0.5
n = 10
s_n = []
summe = 0

for k in range(0, n):
    summe += a * r**k
    s_n.append(summe)
    
print(s_n)

# Hausaufgabe 
# Meine Lösung: 
# geg. Laufzeit des Sparplans = 10 Jahre, 
# AK = 10,000.00
# jährliche Sparrate = 1,000.00
# Jährlicher Zinssatz = 1% 

def spar_funktion(AK, SR, Zinssatz, Laufzeit):
    Vermögen = []
    for i in range(1,Laufzeit):
        Gesamt_Kapital = AK*(Zinssatz+1)**i + (Zinssatz+i)*SR
        Vermögen.append(Gesamt_Kapital) 
    return(Vermögen)
spar_funktion(10000,1000,0.01,10)


