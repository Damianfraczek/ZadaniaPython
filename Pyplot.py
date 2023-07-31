# Wiadomo, że an → π, bn → π i cn → π gdy n → ∞, zatem π można przybliżać każdym z ciągów (an),(bn) i (cn).
# Narysuj wykresy (bezwzględnych) błędów tych oszacowań. Dobierz odpowiednio rodzaj skali i zakresy wartości.
import matplotlib.pyplot as plt
from math import pi

#an
lst1 = [4*(((-1)**0)/(2*0+1))] # Tworzymy listę, której pierwszym wyrazem jest pierwszy wyraz ciągu an.
for i in range(1,100): #W pętli tworzymy kolejne elementy listy, które są kolejnymi wyrazami ciągu an.
    a = 4*(((-1)**i)/(2*i+1))
    lst1 = lst1 + [a+lst1[i-1]]
print(lst1)
for i in range(100): #W pętli obliczamy bezwględny błąd szacowań każdego wyrazu ciągu względem liczby pi.
    lst1[i] = abs(pi-lst1[i])
#Pozostałe dwa ciągi analogicznie.

k = range(100)
plt.plot(k, lst1)

#bn
lst2 = [2*(((2*0+2)**2)/((2*0+1)*(2*0+3)))]
for i in range(1,100):
    b = ((2*i+2)**2)/((2*i+1)*(2*i+3))
    lst2 = lst2 + [(b*lst2[i-1])]
for i in range(100):
    lst2[i] = abs(pi-lst2[i])

plt.plot(k, lst2)

#cn
lst3 = [(16**0)*(4/(8*0+1) - 2/(8*0+4) - 1/(8*0+5) - 1/(8*0+6))]
for i in range(1,100):
    c = (16**(-i))*(4/(8*i+1) - 2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6))
    lst3 = lst3 + [c+lst3[i-1]]
for i in range(100):
    lst3[i] = abs(pi-lst3[i])

plt.plot(k, lst3)
plt.xlabel('Wartość n')
plt.ylabel('Bezwględny błąd oszacowań funkcji')
plt.title('Wykresy bezwzględnych błędów oszacowań ciągów an, bn, cn') 
plt.legend(['an', 'bn', 'cn']) 
plt.yscale("log")
plt.show()