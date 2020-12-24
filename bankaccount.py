class Bank_Account():
    def __init__(self):
        self.queue = []
        self.d = {}

    def store_transaction(self, name, transaction):

        self.d[name] = transaction
        self.queue.insert(0, transaction)

    def get_transaction(self, name):

        last_transaction = self.queue.pop()

        if self.d[name] != last_transaction:
            return "Girl you dont got no money!!"
        else:
            return last_transaction


myAccount = Bank_Account()
myAccount.store_transaction('Emeka', 500)
myAccount.store_transaction("Autumn", 200)
print(myAccount.get_transaction('Autumn'))




