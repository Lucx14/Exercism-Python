from __future__ import division
import math


def reduceFraction(x, y):
    d = math.gcd(x, y)
    x = x // d
    y = y // d
    return (x, y)


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        a, b = reduceFraction(self.numer, self.denom)
        x, y = reduceFraction(other.numer, other.denom)
        return a / b == x / y

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        a, b = reduceFraction(numer, denom)
        return Rational(a, b)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        a, b = reduceFraction(numer, denom)
        return Rational(a, b)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        a, b = reduceFraction(numer, denom)
        return Rational(a, b)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = other.numer * self.denom
        a, b = reduceFraction(numer, denom)
        return Rational(a, b)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if type(power) == int:
            if power >= 0:
                return Rational(self.numer ** power, self.denom ** power)
            return Rational(self.denom ** abs(power), self.numer ** abs(power))
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
