class Bank:
    def __init__(self):
        self.__balance = 1000       # private variable can not access outside class

    def show(self):
        print("Balance:", self.__balance)

obj = Bank()
obj.show()
