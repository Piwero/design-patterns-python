# Design Principles

## Encapsulate what varies
It's a design principle that suggests isolating changing parts of a system within different objects or classes. This supports flexible design and reduces coupling between components. 
It allows changes to be kept within encapsulated components, without changing other parts of the system. 
This principle encourages code reusability, keeps system structure, and supports high cohesion and loose coupling, leading to more robust and scalable applications.

## Favour composition over inheritance
OO design principle that supports using composition, or combining simpler objects, instead of relying heavily on inheritance.
Composition allows for more dynamic and flexible designs, supporting loose coupling and flexibility.
It saves the need to change existing classes, lowering the risk of the fragile base class problem.
"Favor composition over inheritance" supports flexible and stable code reuse through composition, promoting loose coupling and avoiding problems with inheritance.

```python
# Instead of:
class Character:
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword!")

class Mage(Character):
    def attack(self):
        print("Mage casts a spell!")

# This is better:
class Character:
    def __init__(self, weapon):
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()

class Sword:
    def attack(self):
        print("Attacks with a sword!")

class Spell:
    def attack(self):
        print("Casts a spell!")
```

## Program to interfaces, not implementations 
OO design principle that suggests using interfaces or abstract classes as contracts for components, rather than specific implementations. 
This encourages loose coupling, flexibility, and extension in software systems. 
Components connect based on stated interfaces or abstract classes, allowing for interchangeable implementations. 
This method supports decoupling, freedom, and code reusability in object-oriented designs.

## Strive for loosely coupled designs
Two loosely coupled objects means that they can interact but they have little knowledge of each other. This offers a lot of flexibility. Design patterns examples include the observer pattern.
Loosely coupled designs permit us to build flexible OO applications that can be easily changed because they minimise the interdependency between objects.

## Open for extension and closed for modification
Suggests that you should be able to extend the behaviour of a class without changing the existing code.

## Depend on abstractions. Don't depend on concrete classes

Depending on abstractions means designing code that relies on interfaces or abstract classes instead of specific implementations. This approach promotes flexibility and loose coupling.

For example, let’s consider a media player application. With a concrete implementation approach, you would create separate classes for each media type, such as AudioPlayer and VideoPlayer. However, this tightly couples your code to specific implementations and makes it harder to add new media types without modifying existing code.

By depending on abstractions, you can define an abstract class or interface called MediaPlayer with a common play method. Multiple media player classes, like AudioPlayer and VideoPlayer, would implement this interface and provide their own play functionality. Your code can then operate on a list of MediaPlayer objects without needing to know the specific implementations.

This approach allows you to add new media types by creating classes that implement the MediaPlayer interface, without modifying existing code. It promotes code reuse, modularity, and makes your application more maintainable and scalable.

