# Factory

## The Factory method

The Factory Method is a design pattern that provides an interface for producing objects while delegating real object creation to subclasses. It wraps the object creation logic, allowing for object creation flexibility without tightly coupling client code to specific classes. The Factory Method pattern is made up of a base class or interface that defines the common creation method and concrete subclasses that use this method to generate individual objects. This approach allows for extension and flexibility by allowing for the addition of new subclasses to build distinct variations of objects. The "open-closed" approach is promoted by the Factory Method, which allows code to be open for extension but closed for modification.

It is typically used in cases where producing objects of similar types is required, but the actual type is determined at runtime or can vary depending on certain conditions.

```python
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ProductFactory(ABC):
    @abstractmethod
    def create_product(self) -> Product:
        pass
 ```
Next, you create concrete implementations of Product and ProductFactory. For example:

```python
class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"

class ConcreteProductFactoryA(ProductFactory):
    def create_product(self) -> Product:
        return ConcreteProductA()

class ConcreteProductFactoryB(ProductFactory):
    def create_product(self) -> Product:
        return ConcreteProductB()
 ```
Now, in your code, you can use the ProductFactory to create instances of the desired products without explicitly knowing their implementations. Here's an example:

```python
def client_code(factory: ProductFactory):
    product = factory.create_product()
    result = product.operation()
    print(result)

factory_a = ConcreteProductFactoryA()
client_code(factory_a)  # Output: ConcreteProductA operation

factory_b = ConcreteProductFactoryB()
client_code(factory_b)  # Output: ConcreteProductB operation
```
By utilizing the Factory Method pattern, you can separate the object creation logic from the client code. This promotes flexibility and allows you to easily introduce new product types by creating additional ConcreteProduct subclasses and corresponding ConcreteProductFactory implementations.


