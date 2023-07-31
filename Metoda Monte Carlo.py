# Przybliż eksperymentalnie pole figury (A \ B) ∪ (B \ A) ⊂ R2, gdzie:
# • A to koło o środku (2, 1) i promieniu 5,
# • B to prostokąt (tj. zbiór punktów ograniczonych tym prostokątem) o wierzchołkach (4, 0),(7, 6),(3, 8) i (0, 2).

from matplotlib.pyplot import scatter, show, title
from random import uniform

def approximate_area(n):
    '''Funkcja obliczająca przybliżone pole figury metodą Monte Carlo'''
    rolls = 0
    hits = 0
    rolls1 = 0
    hits1 = 0
    rolls2 = 0
    hits2 = 0
    gx, gy = [], []
    hx, hy = [], []
    gx1, gy1 = [], []
    hx1, hy1 = [], []
    gx2, gy2 = [], []
    hx2, hy2 = [], []


    for _ in range(n): #Liczymy pole koła.
        x, y = uniform(-3, 8), uniform(-4, 8)
        rolls += 1
        if (x -2)** 2 + (y -1)** 2 <= 25:
            hits += 1
            gx.append(x)
            gy.append(y)
        else:
            hx.append(x)
            hy.append(y)
    for _ in range(n): #Liczymy pole kwadratu.
        x, y = uniform(-3, 8), uniform(-4, 8)
        rolls1 += 1
        if y <= 2*x+2 and y >= 2*x -8 and y >= -(1/2)*x+2 and y <= -(1/2)*x +(19/2):
            hits1 += 1
            gx1.append(x)
            gy1.append(y)
        else:
            hx1.append(x)
            hy1.append(y)
    for _ in range(n): #Liczymy pole części wspólnej kwadratu i koła.
        x, y = uniform(-3, 8), uniform(-4, 8)
        rolls2 += 1
        if y <= 2*x+2 and y >= 2*x -8 and y >= -(1/2)*x+2 and (x-2)**2 + (y-1)**2 <= 25:
            hits2 += 1
            gx2.append(x)
            gy2.append(y)
        else:
            hx2.append(x)
            hy2.append(y)
    result = "{}/{}, Pole kola wynosi = {}".format(hits, rolls, 132 * hits / rolls)
    print(result)
    result1 = "{}/{}, Pole kwadratu wynosi = {}".format(hits1, rolls1, 132 * hits1 / rolls1)
    print(result1)
    result2 = "{}/{}, Pole czesci wspolnej figur wynosi = {}".format(hits2, rolls2, 132 * hits2 / rolls2)
    print(result2)
    wynik = print("Pole szukanej figury wynosi = {}".format(132*hits / rolls + 132 * hits1 / rolls1 - 2*132 * hits2 / rolls2))
    return wynik


if __name__ == "__main__":
    approximate_area(100000)