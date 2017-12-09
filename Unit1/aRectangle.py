class aRectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.area=l*w
        self.perimeter=(2*l)+(2*w)
        if l == w:
            self.is_square = True
        else:
            self.is_square = False


#    def area(self):
#        self.area = self.l * self.w
#        return self.area

#    def perimeter(self):
#        self.perimeter = (2 * self.l) + (2 * self.w)
#        return self.perimeter

    def __lt__(self, other):
        return self.area < other.area

    def ___le__(self, other):
        return self.area <= other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area

#    def is_square(self):
#        if self.l == self.w:
#            return True
#        else:
#            return False

    def __str__(self):
        return ("Width: " + str(self.w) + ", Length: " + str(self.l) + ", Area: " + str(self.area) + ", Perimeter: " + str(self.perimeter) + ", is Square: " + str(self.is_square) + "\n")
r = aRectangle(2,5)
r2 = aRectangle(2,2)
#r.area()
#r.perimeter()
#r.is_square()
#print(r, r2)
print(r > r2)
print(r < r2)
print(r != r2)

