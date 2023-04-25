# Observer Pattern
The observer pattern is a software design pattern where a subject object keeps track of its observers and automatically calls one of their methods to notify them of any state changes.

It is frequently used in event-driven software to construct distributed event-handling systems. These systems typically refer to the subject as a "stream of events" or "stream source of events," while the observers are referred to as "sinks of events."

# Diagram
```mermaid
classDiagram
    class Subject {
        +observers : Observer[]
        +attach(o : Observer) : void
        +detach(o : Observer) : void
        +notify() : void
    }
    class Observer {
        +update() : void
    }
    class ConcreteSubject {
        -state : any
        +get_state() : any
        +set_state(state : any) : void
    }
    class ConcreteObserver1 {
        -state : any
        +update() : void
    }
    class ConcreteObserver2 {
        -state : any
        +update() : void
    }

    Subject --> Observer : observers
    ConcreteSubject <-- ConcreteObserver1 : subject
    ConcreteSubject <-- ConcreteObserver2 : subject
    Subject <|-- ConcreteSubject
    Observer <|-- ConcreteObserver1
    Observer <|-- ConcreteObserver2
```