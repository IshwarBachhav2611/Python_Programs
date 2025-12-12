#One Child with multiple parent class

# baseclass 1
class A:
    def a(self): 
        print("A")
# baseclass 2 
class B:
    def b(self): 
        print("B")

# derived class of A and B
class C(A, B):
    pass


obj = C()
obj.a()
obj.b()
