def know_people(n):
    '''Funkcja zwracająca uporządkowaną listę numerów osób, któe znają co najmniej n osób'''
    slownik = {} #Tworzymy pusty słownik.
    with open('relacje.txt') as f: #Wczytujemy oba pliki.
        for line in f: 
            liczby = line.split() #Wyszczogólniamy poszczególne liczby.
            for x in liczby:
                slownik[x] = slownik.get(x, 0) + 1 #Zliczamy wystąpienia poszczególnych numerów. 
        lst = [(m, liczby) for liczby, m in slownik.items()] ##Przerabiamy słownik na listę par, gdzie pierwszym elementem jest liczba wystąpień wyrazu, a drugim wyraz.
        lst.sort(reverse = True) #Uporządkowywujemy listę.
        lista = [] #Tworzymy pustą listę.
        for i in lst:  #Tworzymy pętlę przechodzącą przez wcześniejszą listę, która dodaje numer osoby do nowej listy, o ile spełnia warunek. 
            if i[0] <= n: 
                lista.append(i[1])
        lista.sort()
        for i in lista:
            i = int(i)
        return lista

print(know_people(8))

def related_to_city(city_name):
    '''Funkcja zwracacają uporządkowaną listę numerów osób, które mieszkają lub znają kogoś mieszkającego w mieście o nazwie city name.'''
    lista1 = []
    lista2 = []
    lista3 = []
    with open('relacje.txt', encoding='utf8') as f,  open ('osoby.csv', encoding='utf8') as g: #Wczytujemy oba pliki.
        for line in g:
            ludzie = line.split(sep=';') #Dzielimy wyrazy w linijkach względem średnika.
            lista1.append(ludzie) #Dodajemy tak podzielone wyrazy do listy1.
        for i in lista1:
            if i[1] == city_name: #Przez pętlę dodajemy numery osób, które mieszkają w podanym mieście do nowej listy. 
                i[2] = i[2].strip('\n') #Usuwamy z numerów napis "\n"
                lista2.append(i[2])
        for line in f:  
            liczby = line.split() #Dzielimy plik na linikji.
            for j in lista2: #W pętli przyrównujemy numery, jeśli któraś linijka zawiera element liisty drugiej to dodajemy ten drugi element do nowej listy3.
                if liczby[0] == j and liczby[1] != j:
                    lista3.append(liczby[1])
                if liczby[1] == j and liczby[0] != j:
                    lista3.append(liczby[0])                    
        for j in lista2: #Dodajemy wszytskie elementy drugiej listy.
            lista3.append(j)
        for j in lista3: #Usuwamy powtarzające się wyrazy.
            for i in lista3:
                if j == i and j.index != i.index:
                    lista3.remove(i)
        lista3.sort() #Uporządkowywujemy listę.
        return lista3

#print(related_to_city('Gdańsk'))

def special_cities():
    '''Funckja zwracacająca uporządkowaną listę nazw miast, w których mieszka osoba, która zna dowolnego Patryka.'''
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    with open('relacje.txt', encoding='utf8') as f,  open ('osoby.csv', encoding='utf8') as g: #Wczytujemy oba pliki.
        for line in g:
            ludzie = line.split(sep=';') #Dzielimy wyrazy w linijkach względem średnika.
            lista1.append(ludzie) #Dodajemy tak podzielone wyrazy do listy1.
        for i in lista1:
            imie = i[0].split() #Wyodrębniamy samo imię, bez naziwska.
            if imie[0] =='Patryk': #Przez pętlę dodajemy numery osób, które mają na imię Patryk.
                i[2] = i[2].strip('\n') #Usuwamy z numerów napis "\n"
                lista2.append(i[2])
        for line in f:  
            liczby = line.split() #Dzielimy plik na linikji.
            for j in lista2: #W pętli przyrównujemy numery, jeśli któraś linijka zawiera element listy drugiej to dodajemy ten drugi element do nowej listy3.
                if liczby[0] == j and liczby[1] != j:
                    lista3.append(liczby[1])
                if liczby[1] == j and liczby[0] != j:
                    lista3.append(liczby[0])                    
        for j in lista3: #Usuwamy powtarzające się wyrazy.
            for i in lista3:
                if j == i and j.index != i.index:
                    lista3.remove(i)
        for j in lista3:  #Do listy nr 4 dodajemy nazwy miast, w których mieszka osoba, która zna dowolnego Patryka.
            for i in lista1:
                i[2] = i[2].strip('\n') #Usuwamy z numerów napis "\n".
                if j == i[2]:
                    lista4.append(i[1]) 
        for j in lista4: #Usuwamy powtarzające się wyrazy.
            for i in lista4:
                if j == i and j.index != i.index:
                    lista4.remove(i)
        lista4.sort() #Uporządkowywujemy listę.
        return lista4

#print(special_cities())

def special_cities2():
    '''Funkcja zwracająca uporządkowaną listę nazw miast, w których mieszka osoba, która zna kogoś, kto zna dowolnego Patryka.'''
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    with open('relacje.txt', encoding='utf8') as f,  open ('osoby.csv', encoding='utf8') as g: #Wczytujemy oba pliki.
        for line in g:
            ludzie = line.split(sep=';') #Dzielimy wyrazy w linijkach względem średnika.
            lista1.append(ludzie) #Dodajemy tak podzielone wyrazy do listy1.
        for i in lista1:
            imie = i[0].split() #Wyodrębniamy samo imię, bez naziwska.
            if imie[0] =='Patryk': #Przez pętlę dodajemy numery osób, które mają na imię Patryk.
                i[2] = i[2].strip('\n') #Usuwamy z numerów napis "\n"
                lista2.append(i[2])
        for line in f:  
            liczby = line.split() #Dzielimy plik na linikji.
            for j in lista2: #W pętli przyrównujemy numery, jeśli któraś linijka zawiera element listy drugiej to dodajemy ten drugi element do nowej listy3.(osoby w relacji z Patrykiem.)
                if liczby[0] == j and liczby[1] != j:
                    lista3.append(liczby[1])
                if liczby[1] == j and liczby[0] != j:
                    lista3.append(liczby[0])                    
        for j in lista3: #Usuwamy powtarzające się wyrazy.
            for i in lista3:
                if j == i and j.index != i.index:
                    lista3.remove(i)
        f.close()
        g.close()
    with open('relacje.txt', encoding='utf8') as f,  open ('osoby.csv', encoding='utf8') as g: #Wczytujemy oba pliki.
        for line in f: #W pętli przyrównujemy numery, jeśli któraś linijka zawiera element listy trzeiej to dodajemy ten drugi element do nowej listy4.(osoby, które są w relacji z kimś kto jest w relacji z jakimś Patrykiem.)
            liczby = line.split()
            for j in lista3:
                if liczby[0] == j and liczby[1] != j:
                    lista4.append(liczby[1])
                if liczby[1] == j and liczby[0] != j:
                    lista4.append(liczby[0])
        for j in lista4: #Usuwamy powtarzające się wyrazy.
            for i in lista4:
                if j == i and j.index != i.index:
                    lista4.remove(i)
        for j in lista4:  #Do listy nr 5 dodajemy nazwy miast, w których mieszka osoba, która zna kogoś, kto zna dowolnego Patryka.
            for i in lista1:
                i[2] = i[2].strip('\n') #Usuwamy z numerów napis "\n".
                if j == i[2]:
                    lista5.append(i[1]) 
        for j in lista5: #Usuwamy powtarzające się wyrazy.
            for i in lista5:
                if j == i and j.index != i.index:
                    lista5.remove(i)
        lista5.sort() #Uporządkowywujemy listę.
        return lista5

#print(special_cities2())