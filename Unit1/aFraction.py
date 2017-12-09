#helper function--a function outside a class that is used by a method
#A mutator method -- a method with no return which modifies the object itself

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

class aFraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return aFraction((newnum // common), (newden // common))

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return aFraction(newnum // common, newden // common)

    def reciprocal(self):
        newnum = self.den
        newden = self.num
        return aFraction(newnum, newden)

    def simplify(self):
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common



f1=aFraction(1,2)
f2=aFraction(1,4)
f3=f1 + f2
print("addition should be 3/4--->", f3)

f4 = aFraction(12, 16)
f4.simplify()
print("simplify should be 3/4--->", f4)

f5 = aFraction(1,2)
f6 = aFraction(2,5)
f7 = f5 * f6
print("multiply should be 2/10, which simplifies to 1/5--->", f7)

f8 = aFraction(7, 8)
f9 = f8.reciprocal()
print("reciprocal should be 8/7--->", f9)




