# Decorator Pattern
The Decorator Pattern is a design pattern in object-oriented programming that allows you to add additional behavior or capability to an object dynamically without affecting the original object's code. 
This pattern provides a versatile alternative to subclassing by allowing you to modify an object's behavior through composition rather than inheritance.

The basic idea of the Decorator Pattern is to wrap an existing object with one or more decorators that add additional behaviour to it. 
The decorators comply with the same interface as the object they decorate, so they can be used interchangeably with the original object. 
When you call a method on the decorated object, the decorator intercepts the call and adds its own behaviour before or after delegating to the original object to complete the operation.

# Example
```python
class Coffee:
    def get_cost(self):
        return 1.00

    def get_description(self):
        return "Coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 0.50

    def get_description(self):
        return self.coffee.get_description() + ", Milk"

coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)

print(coffee_with_milk.get_description())  # Output: Coffee, Milk
print(coffee_with_milk.get_cost())  # Output: 1.50
```