# Napisz własną klasę Fraction reprezentującą ułamki. Zaimplementuj następujące metody specjalne1:
from gcd import gcd
from simplify import simplify

class Fraction:
    def __init__ (self, numer=0, denom=1):
        self.numer, self.denom = simplify(numer, denom)
    def __abs__(self):
        return Fraction(abs(self.numer), self.denom)
    def __neg__(self):
        return Fraction(-self.numer, self.denom)
    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)
    def __add__(self, other_frac):
        lewy_licznik = self.numer * other_frac.denom
        prawy_licznik = self.denom * other_frac.numer
        return Fraction(lewy_licznik+prawy_licznik, self.denom*other_frac.denom)
    def __sub__(self, other_frac):
        lewy_licznik = self.numer * other_frac.denom
        prawy_licznik = self.denom * other_frac.numer
        return Fraction(lewy_licznik-prawy_licznik, self.denom*other_frac.denom)
    def __mul__(self, other_frac):
        return Fraction(self.numer*other_frac.numer, self.denom*other_frac.denom)
    def __truediv__(self, other_frac):
        return Fraction(self.numer*other_frac.denom, self.denom*other_frac.numer)
    def __eq__(self, other_frac):
        if self.numer == other_frac.numer and self.denom == other_frac.denom:
            return True
        else:
            return False
    def __lt__(self, other_frac):
        if self.numer*other_frac.denom < other_frac.numer*self.denom:
            return True
        else:
            return False
       

ulamek = Fraction(1,2)
ulamek1 = Fraction(1,3)
print(ulamek)
print(ulamek + ulamek1)
assert abs(Fraction(-1,2)) == Fraction(1,2)
assert Fraction(1,2) + Fraction(1,3) == Fraction(5,6)
assert str(Fraction(1,2)) == "1/2"
assert -(Fraction(1,3)) == Fraction(-1,3)
assert Fraction(2,7) - Fraction(1,14) == Fraction(3,14)
assert Fraction(1,2) * Fraction(3,4) == Fraction(3,8)
assert Fraction(2,3) / Fraction(4,5) == Fraction(5, 6)
assert Fraction(1,2) == Fraction(2,4)
assert Fraction(1,2) < Fraction(3,4)


    