"""
classes are blueprints for creating objects or they are collections of objects
"""

class Dog:
    species = "Canine" # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute

"""
An object is an instance of a class. It represents a specific implementation of the class and holds its own data
"""

#creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.age)
print(dog1.species)

"""
The self parameter is a reference to the current instance of the class.
It allows us to access the attributes and methods of the object.
"""

dog2 = Dog("Charlie", 5)

print(dog1.name, dog1.age, dog1.species) # access the instance and class attributes

"""
__init__ method is the constructor in python, automatically called when a new object is created. It initializes the attributes of the class
"""

"""
inheritance allows a class (child class) to acquire properties and methods of another class (parent class)
it supports hierarchical classsification and promotes code reuse
Types of inheritance:
- single inheritance: a child class inherits from a single parent class
- multiple inheritance: a child class inherits from more than one parent class
- multilevel inheritance: a child class inherits from a parent class, which in turn inherits from another class
- hierarchical inheritance: multiple child classes inherit from a single parent class
- hybrid inheritance: a combination of two or more types of inheritance.
"""
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

dog_l = Labrador('Caramel')
dog_l.display_name()

"""
polymorphism allows methods to have the same name but behave differently based on the object's context.
it can be achieved through method overriding or overloading.

Types of Polymorphism
- Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program. 
It allows methods or operators with the same name to behave differently based on their input parameters or usage. 
It is commonly referred to as method or operator overloading.

- Run-Time Polymorphism: This type of polymorphism is determined during the execution of the program. 
It occurs when a subclass provides a specific implementation for a method already defined in its parent class, 
commonly known as method overriding.
"""