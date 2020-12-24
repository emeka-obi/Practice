class Deque():
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def addFront(self,items):
        self.items.append(items)
    
    def addRear(self,items):
        self.items.insert(0,items)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)


d = Deque()
print(d.isEmpty())
d.addFront(5)
d.addFront(6)