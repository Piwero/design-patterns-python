# Basic principles of Object Oriented Programming
## 1. Encapsulation
Encapsulation is the technique of hiding data implementation by restricting access to public methods.
```python
class Employee:
    def __init__(self):
        self.name = ""
        self.dob = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob
```
## 2. Abstraction
Abstract means that a class is not linked with any particular instance, and that a class's interface is good enough to use.
Using abstract class/Interface we express the purpose of the class rather than the actual implementation.
```python
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    # Abstract method
    @abstractmethod
    def make_sound(self):
        pass

# Concrete class that inherits from Animal
class Dog(Animal):

    # Implementation of abstract method
    def make_sound(self):
        print("Woof!")

# Concrete class that inherits from Animal
class Cat(Animal):

    # Implementation of abstract method
    def make_sound(self):
        print("Meow!")

# Instantiate objects
dog = Dog()
cat = Cat()

# Call abstract method on objects
dog.make_sound()  # Output: "Woof!"
cat.make_sound()  # Output: "Meow!"
```

## 3. Inheritance
Inheritances expresses "is-a" and/or "has-a" relationships between two things. It is based on class inheritance or interface implementation.
```python
# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("The animal makes a generic sound.")

# Child class inheriting from Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("The dog barks.")

    def fetch(self):
        print("The dog fetches a ball.")

# Child class inheriting from Animal class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        print("The cat meows.")

    def scratch(self):
        print("The cat scratches furniture.")

# Create instances of Dog and Cat classes
dog = Dog("Buddy", "Labrador")
cat = Cat("Fluffy", "Gray")

# Access attributes and methods of parent class Animal
print(dog.name)             # Output: Buddy
print(cat.species)          # Output: Cat
dog.make_sound()           # Output: The dog barks.
cat.make_sound()           # Output: The cat meows.

# Access attributes and methods of child class Dog
print(dog.breed)           # Output: Labrador
dog.fetch()                # Output: The dog fetches a ball.

# Access attributes and methods of child class Cat
print(cat.color)           # Output: Gray
cat.scratch()              # Output: The cat scratches furniture.
```

## 4. Polymorphism
Polymorphism means one name many forms. It is done using method overloading and method overriding.
