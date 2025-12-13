class Demo:
    def __init__(self):
        self.__data = "Hidden"

    def show(self):
        print(self.__data)

obj = Demo()
obj.show()
