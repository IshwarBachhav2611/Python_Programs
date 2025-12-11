from abc import ABC, abstractmethod

class Animal(ABC):       # Abstract class
    @abstractmethod
    def sound(self):     # Abstract method
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# a = Animal()  # Error: Cannot instantiate abstract class
d = Dog()
c = Cat()

print(d.sound())  # Bark
print(c.sound())  # Meow
