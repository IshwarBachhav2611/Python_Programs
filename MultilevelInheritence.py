# creates chain like structure parent <- child <- grandchild
#parent class
class A:
    def showA(self):
        print("A")

#child class of A
class B(A):
    def showB(self):
        print("B")

#child calss of B
class C(B):
    def showC(self):
        print("C")

obj = C()
#calling class A & B methods Using Class C Object
obj.showA()
obj.showB()
obj.showC()
