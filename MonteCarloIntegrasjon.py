from random import*

xmin = -3 #start for grafens x-verdier
xmaks = 3 #slutt for grafens x-verdier
N = 100000 #antall punkter
N1 = 0  #startverdi
N2 = 0  #startverdi

#funksjon
def f(x):
    return x**2+1

#min og max y-verdi
def ff(x):
    return 2*x

ymaks = f(xmaks)
ymin = ff(0)

#areal av boks
Aboks = (xmaks-xmin) * (ymaks-ymin)

#ilfeldige punkter innenfor boks
for i in range(N):
    x1 = uniform(xmin, xmaks)
    y1 = uniform (ymin, ymaks)
    if f(x1) < y1:  #telle punkter over grafen
        N1 += 1
    elif f(x1)> y1:  #telle punkter under grafen
        N2 += 1

#regne ut areal under graf
Forhold = N2/N
Arealundergraf = Forhold*Aboks
print ("Arealet under grafen ved Monte Carlo integrasjon er %g" %Arealundergraf)

#Simpsonsmetode
def simpsonmetoden (f,a,b,N): #definerer simpson
    areal = 0                 #startverdi for areal
    x = a                     #sluttverdi for x
    h = (b-a)/N               #kalkulerer steglengden
    for i in range(N):        #Løper over alle vedier
        areal += h/6*(f(x) + 4*f(x+0.5*h) + f(x+h)) #leger til arealet der på gamle
        x += h                #oppdaterer x med en steglengde
    return areal              #returnerer det totale arealet

svar = simpsonmetoden(f, xmin, xmaks, N)
print("Arealet under grafen ved bruk av Simpsons Metode blir %g" %svar)

