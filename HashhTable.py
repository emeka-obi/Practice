class Table():

    def __init__(self, size):

        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):

        hashValue = self.hashfunction(key, len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data

        else:

            if self.slots[hashValue] == key:
                self.data[hashValue] = data

            else:
                nextslot = self.rehash(hashValue, len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot  =self.rehash(nextslot, len(self.slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

        #The hash function

    def rehash(self, oldhash, size):
        return(oldhash + 1) % size

    
    def get(self,key):
        
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))

                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self,key, data):
        return self.put(key, data)






h = Table(5)

h[1] = "one"
h[2] = "two"
h[3] = "three"


print(h[1])