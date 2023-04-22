# Strategy pattern

The Strategy pattern is a behavioural design pattern that allows objects to dynamically switch between different algorithms or strategies for performing a given task, based on the specific context or situation. It provides a way to encapsulate interchangeable algorithms, making them independent from the clients that use them, and allowing runtime selection of different strategies without changing the client's code.

In the Strategy design, there are three main components:

1. Context: It shows the context or the client that uses the strategies. It maintains a reference to the current strategy object and offers an interface for the clients to interact with the strategies.

2. Strategy: It defines an interface or an abstract class that encapsulates the common methods or behaviours that different concrete strategies must apply. The strategies encapsulate the different algorithms or approaches that can be used to perform a job.

3. specific Strategies: These are the specific implementations of the strategies. They implement the methods described by the Strategy interface, giving specific implementations of the algorithms or approaches to be used in a particular context.

The interaction between these components usually includes the Context object delegating the execution of a task to the currently assigned Concrete Strategy. The Context can switch between different Concrete Strategies at runtime, based on the specific requirements or conditions, without affecting the overall behaviour of the client code.

Here is an example:

```python

class Strategy:

    def do_task(self):

        pass




class ConcreteStrategyA(Strategy):

    def do_task(self):

        return "Strategy A"




class ConcreteStrategyB(Strategy):

    def do_task(self):

        return "Strategy B"




class Context:

    def __init__(self, strategy):

        self._strategy = strategy




    def set_strategy(self, strategy):

        self._strategy = strategy




    def execute_task(self):

        return self._strategy.do_task()




# Client code

strategy_a = ConcreteStrategyA()

strategy_b = ConcreteStrategyB()




context = Context(strategy_a)

result = context.execute_task()

print(result)  # Output: "Strategy A"




context.set_strategy(strategy_b)

result = context.execute_task()

print(result)  # Output: "Strategy B"

```






In this example, we have a Context object that can switch between ConcreteStrategyA and ConcreteStrategyB at runtime, based on the strategy set. The Concrete Strategies implement the `do_task()` method defined by the Strategy interface, giving their specific implementations. The Context delegates the execution of the job to the currently assigned Concrete Strategy, allowing the client code to switch between different strategies without changing its implementation.

The Strategy pattern is useful in cases where you need to provide different algorithms or behaviours for performing a task, and you want to decouple the specific implementations from the client code. It supports code flexibility, extensibility, and maintainability, allowing you to easily switch or add new strategies without modifying the client's code.
