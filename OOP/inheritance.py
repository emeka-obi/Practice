class Quadrilateral():
    length = 1
    width = 1
    def __init__(self, length, width):
        self.setLength(length)
        self.setWidth(width)
    
    def setWidth(self, width):
        if self.width >  0 and isinstance(width, float) == True:
            return ValueError("Enter a number greater than 0 and a non float type")
        else:
            self.width = width

    def setLength(self, length):
        if self.length >  0 and isinstance(length, float) == True:
            return ValueError("Enter a number greater than 0 and a non float type")
        else:
            self.length = length

    
    def findArea(self):
        return self.length * self.width

class Square(Quadrilateral):

    def __init__(self, length, width):

        Quadrilateral.__init__(self, length, width)
    
    def  getArea(self):
        return Quadrilateral.findArea(self)

       
s = Square(5,6)
print(s.getArea())


import math

from math import sin


print(sin(50))