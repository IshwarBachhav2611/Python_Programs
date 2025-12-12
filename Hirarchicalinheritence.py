#base class 
class Parent:
    def show_parent(self):
        print("Parent class")

#derive class 1
class Child1(Parent):
    def show_child1(self):
        print("Child 1 class")
#derive class 2
class Child2(Parent):
    def show_child2(self):
        print("Child 2 class")


obj1 = Child1()
obj2 = Child2()
obj1.show_parent()
obj2.show_parent()
