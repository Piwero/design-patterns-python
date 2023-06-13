# Factory

Factory Method Pattern:
The Factory Method pattern is a creational design pattern that provides an interface for creating objects but allows subclasses to decide which class to instantiate. It encapsulates the object creation logic in a separate method, known as the factory method, which subclasses override to create specific objects.

Key Components:

	•	Product: Represents the objects that the factory method creates.
	•	Creator: Declares the factory method that returns a Product object. This can be an abstract class or an interface.
	•	Concrete Creator: Implements the factory method to create specific instances of the Product.

Example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

def client_code(factory: AnimalFactory):
    animal = factory.create_animal()
    sound = animal.speak()
    print(sound)

dog_factory = DogFactory()
client_code(dog_factory)  # Output: Woof!

cat_factory = CatFactory()
client_code(cat_factory)  # Output: Meow!
```

Explanation:
In this example, the Factory Method pattern is used to create different types of animals. The Animal abstract class defines the common interface for all animals. The Dog and Cat classes inherit from Animal and provide their own implementations of the speak() method.

The AnimalFactory abstract class declares the create_animal() method, which returns an instance of Animal. The DogFactory and CatFactory classes inherit from AnimalFactory and implement the create_animal() method to create specific animal instances.

The client code can use different factory objects (DogFactory and CatFactory) to create and interact with different types of animals without knowing the specific classes involved. This promotes loose coupling between the client and the specific animal classes.

Abstract Factory Pattern:
The Abstract Factory pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It encapsulates the creation of multiple objects that work together into a separate factory hierarchy.

Key Components:

	•	Abstract Product: Declares the interface that each specific product family must implement.
	•	Concrete Product: Represents a specific product family and implements the Abstract Product interface.
	•	Abstract Factory: Declares factory methods for creating Abstract Product objects.
	•	Concrete Factory: Implements the factory methods to create specific instances of the Abstract Product.

Example:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing Circle"

class Square(Shape):
    def draw(self):
        return "Drawing Square"

class AbstractShapeFactory(ABC):
    @abstractmethod
    def create_shape(self) -> Shape:
        pass

class CircleFactory(AbstractShapeFactory):
    def create_shape(self) -> Shape:
        return Circle()

class SquareFactory(AbstractShapeFactory):
    def create_shape(self) -> Shape:
        return Square()

def client_code(factory: AbstractShapeFactory):
    shape = factory.create_shape()
    drawing = shape.draw()
    print(drawing)
```