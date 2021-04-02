class complexNumbers():
    i = -1 ** 0.5
    "complex number = realPart + imaginary part * i"
    def __init__(self, realPart =  1.0, imaginaryPart = 1.0):
        self._realPart = float(realPart)
        self._imaginaryPart = float(imaginaryPart)

    def addingComplexNumbers(self, realPart, imaginaryPart):
        self._realPart = self._realPart + float(realPart)
        self._imaginaryPart = self._imaginaryPart + float(imaginaryPart)
    
    def subtractingComplexNumbers(self, realPart, imaginaryPart):
        self._realPart = self._realPart - float(realPart)
        self._imaginaryPart = self._imaginaryPart - float(imaginaryPart) 
      
    def printingComplexNumbers(self):
       return f"{self._realPart} + {self._imaginaryPart}i"


    

              
c =  complexNumbers(1,5)
c.addingComplexNumbers(5.9, 6.2)
c.subtractingComplexNumbers(5,7)
print(c.printingComplexNumbers())
