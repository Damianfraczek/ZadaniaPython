# Dana jest urna, w której znajduje się r kul czerwonych, g kul zielonych i b kul niebieskich (gdzie r + g + b ­ 4). Rozważmy proces, 
# w którym wyciągamy z urny bezzwracania cztery kule, numerując je. Napisz funkcję, która dla podanych liczb naturalnych r, g, b przybliża 
# eksperymentalnie prawdopodobieństwo, że tak wyciągnięte kule spełniają jednocześnie następujące warunki:
# • Co najmniej jedna kula jest czerwona.
# • Pierwsza i trzecia kula mają różne kolory.
# • Druga i trzecia kula mają ten sam kolor.
# • Czwarta kula nie jest zielona.
from random import *

def succes_rate(r, g, b):
    '''Funkcja obliczająca przybliżone prawdopodobieństwo wyciągnięcia czterech kul ze zwracaniem z urny, z uwzględnieniem podanych w zadaniu warunków'''
    hits = 0
    for _ in range(100000): #Uznałem, że 100 000 jest miarodajną liczbą powtórzeń pętli. 
        czerwone = ['red']*r
        zielone = ['green']*g
        niebieskie = ['blue']*b
        urna = czerwone + zielone + niebieskie #Lista wszystkich kul.
        pierwsza_kula = choice(urna) #Wybieramy losowo jedną kulę z urny.
        urna.remove(pierwsza_kula) #A następnie ją usuwamy z urny, ponieważ wyciągamy kule bez zwracania, reszta analogicznie.
        druga_kula = choice(urna)
        urna.remove(druga_kula)
        trzecia_kula = choice(urna)
        urna.remove(trzecia_kula)
        czwarta_kula = choice(urna)
        urna.remove(czwarta_kula)
        if (pierwsza_kula == 'red' or druga_kula == 'red' or trzecia_kula == "red" or czwarta_kula == 'red') and pierwsza_kula != trzecia_kula and druga_kula == trzecia_kula and czwarta_kula != 'green':
            hits +=1 
    return ("Prawdopodobieństwo wynosi: {}".format(hits/100000))

print(succes_rate(4,6,3))
    

