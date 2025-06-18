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

"""
Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions
A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc

Types of Encapsulation:
- Public Members: Accessible from anywhere.
- Protected Members: Accessible within the class and its subclasses.
- Private Members: Accessible only within the class.
"""

class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())

"""
Data Abstraction hides the internal implementation details while exposing only the necessary funtionality.
It helps focus on "what to do" rather than "how to do it"

Types of Abstraction:
- Partial Abstraction: Abstract class contains both abstract and concrete methods.
- Full Abstraction: Abstract class contains only abstract methods (like interfaces).
"""