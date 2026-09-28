# Import ABC and abstractmethod
from abc import ABC, abstractmethod


# Abstract class
# ABC means this class can contain abstract methods
class Animal(ABC):

    # Abstract method
    # We only declare what the method should do.
    # We don't write its actual implementation here.
    @abstractmethod
    def sound(self):
        pass


# Child class
class Dog(Animal):

    # Providing implementation of abstract method
    def sound(self):
        print("Dog says: Woof Woof")


# Another child class
class Cat(Animal):

    # Providing implementation of abstract method
    def sound(self):
        print("Cat says: Meow")


# Creating objects
d = Dog()
c = Cat()


# Calling methods
d.sound()
c.sound()