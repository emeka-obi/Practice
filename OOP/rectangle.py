
class rectangle():
    length = 1
    width = 1
    def __init__(self, length, width):
        self.setLength(length)
        self.setWidth(width)

    def setLength(self, length):
        if isinstance(length, float) == True and 0.0 < length < 20.0:
            self._length = length
        else:
            raise ValueError("Enter a value for length that follows the given parameters")

    def setWidth(self, width):
        if isinstance(width, float) == True and 0.0 < width < 20.0:
            self._width = width
        else:
            raise ValueError("Enter a value for width that follows the given parameters")

    def perimeter(self):
        return 2*self._length + 2*self._width

    def area(self):
        return self._length * self._width 


r = rectangle(9.0, 5.0)
print(r.perimeter())
print(r.area())
