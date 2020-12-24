class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        self.stack1.append(element)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
        

n = Queue()
n.enqueue(5)
n.enqueue(6)
n.enqueue(7)
n.enqueue(8)
n.enqueue(9)
print(n.dequeue())
print(n.dequeue())


