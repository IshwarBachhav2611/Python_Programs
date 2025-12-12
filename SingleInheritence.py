#one parent with one child

#parent class 
class A:
    def showA(self):
        print("Class A")

#child class
class B(A):
    def showB(self):
        print("Class B")

obj = B()
# calling parent class method using child class object
obj.showA() 
obj.showB()
