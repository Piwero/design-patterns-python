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

## Loosely coupled
Two loosely coupled objects means that they can interact but they have little knowledge of each other. This offers a lot of flexibility. Design patterns examples include the observer pattern.
Loosely coupled designs permit us to build flexible OO applications that can be easily changed because they minimise the interdependency between objects.