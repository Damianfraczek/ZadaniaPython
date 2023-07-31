# (a) Zaproponuj sposób reprezentacji „pozycji gry”, czyli planszy 7×6, w której pola mogą być puste lub zajęte przeż żetony pierwszego 
# lub drugiego gracza. Opisz ten sposób w komentarzu w pliku z rozwiązaniem:

# Jeżeli w danym polu na planszy 7x6 nie znajduje się, żaden żeton to w liście opisującej planszę gry znaduje się liczba 0, analogicznie 
# żeton pierwszego zawodnika oznaczamy liczbą 1, a drugiego liczbą 2. 

# (b) Napisz funkcję check winner(board), która sprawdza, czy pozycja reprezentowana przez board jest wygrana dla jednego z graczy. 
# Jeśli tak, funkcja powinna zwrócić numer zwycięskiego gracza. W przeciwnym wypadku powinna zwrócić None (również w przypadku pozycji remisowej).

def check_winner(board): #Sprawdzamy czy w jakimś wierszu nie ma 4 żetonów o tym samym kolorze obok siebie.
    for i in range(6): 
        for j in range(4):
                q = board[i][j]
                w = board[i][j+1]
                v = board[i][j+2]
                b = board[i][j+3]
                if (q == 1 and q == w and q == v and q == b):
                    return 1
                elif (q == 2 and q == w and q == v and q == b):
                    return 2
    for i in range(7): ##Sprawdzamy czy w jakiejś kolumnie nie ma 4 żetonów o tym samym kolorze obok siebie.
            for j in range(3):
                q = board[j][i]
                w = board[j+1][i]
                v = board[j+2][i]
                b = board[j+3][i]
                if (q == 1 and q == w and q == v and q == b):
                    return 1
                elif (q == 2 and q == w and q == v and q == b):
                    return 2
    for i in range(3): #Sprawdzamy skosy z góry na dół. 
        for j in range(4):
            q = board[i][j]
            w = board[i+1][j+1]
            v = board[i+2][j+2]
            b = board[i+3][j+3]
            if (q == 1 and q == w and q == v and q == b):
                return 1
            elif (q == 2 and q == w and q == v and q == b):
                return 2
    for i in range(3,6): #Sprawdzamy skosy z dołu do góry. 
        for j in range(4):
            q = board[i][j]
            w = board[i-1][j+1]
            v = board[i-2][j+2]
            b = board[i-3][j+3]
            if (q == 1 and q == w and q == v and q == b):
                return 1
            elif (q == 2 and q == w and q == v and q == b):
                return 2


gra1 = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [2,1,1,0,0,0,0], [1,2,2,2,2,0,0], [1,2,2,1,1,0,0]]  # 4 dwójki w jednym wierszu.

print(check_winner(gra1))

gra2 = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,1,0,0,0,0], [2,2,1,0,0,0,0], [2,2,1,0,0,0,0], [1,2,1,0,0,0,0]] # 4 jedynki w jednym wierszu.

print(check_winner(gra2))

gra3 =[[1,2,2,0,0,1,1], [2,2,1,0,1,2,1], [1,1,1,2,1,2,2], [2,1,2,1,2,2,1], [1,2,1,2,2,1,1], [2,2,1,1,2,2,1]] # 4 jedynki na skos z góry do dołu.

print(check_winner(gra3))

gra4 = [[2,2,1,2,1,1,2], [1,1,2,1,2,2,1], [2,2,2,1,1,1,2], [1,1,2,1,1,2,1], [2,2,1,2,2,2,1], [1,2,2,1,1,2,1]] # Remisowa plansza.

print(check_winner(gra4))

gra5 = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,2,0,0], [0,0,0,2,1,0,0], [0,0,2,1,2,0,0], [0,2,1,1,1,0,0]] # 4 dwójki na skos z dołu do góry.

print(check_winner(gra5))

# (c) (nieobowiązkowe) Napisz funkcję is valid position(board), która sprawdza, czy pozycja reprezentowana przez board jest legalna,
# czyli osiągalna w wyniku zwykłej rozgrywki (plansza nie jest legalna na przykład w sytuacji, gdy pod polem z żetonem znajduje 
# się pole puste).

def is_valid_position(board):
    for i in range(5):
        for j in range(7):
            k = board[i][j]
            l = board[i+1][j]
            if (k == 1 or k == 2) and l == 0:
                return "Jest nielegalna."
    return "Jest legalna."

print(is_valid_position(gra5))

gra6 = [[2,2,1,2,1,1,2], [1,1,2,1,2,2,1], [2,2,2,1,1,1,2], [1,1,2,1,1,2,1], [2,2,1,2,0,2,1], [1,2,2,1,1,2,1]]

print(is_valid_position(gra6))

                   
