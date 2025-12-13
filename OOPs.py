# 1. ABSTRACTION (ABC Module)
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


# 2. INHERITANCE (Single Inheritance)
class Dog(Animal):
    def sound(self):
        return "Bark"


# 3. MULTILEVEL INHERITANCE
class Puppy(Dog):
    def behavior(self):
        return "Playful"


# 4. MULTIPLE INHERITANCE
class Father:
    def height(self):
        return "Tall"

class Mother:
    def color(self):
        return "Fair"

class Child(Father, Mother):
    pass


# 5. HIERARCHICAL INHERITANCE
class Vehicle:
    def type(self):
        return "Transport"

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass


# 6. POLYMORPHISM
# Runtime Polymorphism (Method Overriding)
class Bird:
    def fly(self):
        return "Birds can fly"

class Ostrich(Bird):
    def fly(self):
        return "Ostrich cannot fly"

# Compile-Time Polymorphism (Method Overloading simulation)
class Math:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a


# 7. ENCAPSULATION
class Bank:
    def __init__(self):
        self.__balance = 1000  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance



# MAIN CODE – SHOW ALL OUTPUTS

print("ABSTRACTION:", Dog().sound())

# Inheritance
puppy = Puppy()
print("Single Inheritance:", puppy.sound())
print("Multilevel Inheritance:", puppy.behavior())

child = Child()
print("Multiple Inheritance Height:", child.height())
print("Multiple Inheritance Color:", child.color())

car = Car()
bike = Bike()
print("Hierarchical Inheritance Car:", car.type())
print("Hierarchical Inheritance Bike:", bike.type())

# Polymorphism
print("Runtime Polymorphism:", Ostrich().fly())

m = Math()
print("Compile-Time Polymorphism add(10,20):", m.add(10, 20))
print("Compile-Time Polymorphism add(10,20,30):", m.add(10, 20, 30))

# Encapsulation
b = Bank()
b.deposit(500)
print("Encapsulation Balance:", b.get_balance())
