"""
Actually the Mediator Design Pattern is opposite of facade.
The Mediator and Facade patterns serve distinct purposes in software design.
The Mediator pattern facilitates communication between objects by introducing a mediator object,
promoting loose coupling and centralized control over interactions. In contrast,
the Facade pattern simplifies the interface to a subsystem, shielding clients from its complexities
by providing a unified and simplified interface. While the Mediator pattern focuses on managing interactions between objects,
the Facade pattern concentrates on simplifying access to a complex system, enhancing usability without altering its functionality."""

"""Step 1: Components
Define classes representing different components with a reference to the
Mediator."""


class Component:
    """
     Represents a component with business logic.
     """

    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, message):
        """
        Sends a message to the mediator.
        """
        self._mediator.notify(message)

    def receive(self, message):
        """
           Receives and processes messages from the mediator.
           """
        print(f"Component received message: {message}")


"""Step 2: Mediator Interface
Declare the Mediator interface for communication between components."""
from abc import ABC, abstractmethod


class Mediator(ABC):
    """
     Mediator interface declares communication methods.
     """

    @abstractmethod
    def notify(self, message):
        """
        Notify method for sending messages to components.
        """
        pass

"""Step 3: Concrete Mediator
Implement a concrete mediator that manages component interactions."""
class ConcreteMediator(Mediator):
      """
       Concrete Mediator manages communication between components.
      """
      def __init__(self):
        self._components = []

      def add_component(self, component):
            """
            Adds a component to the mediator.
            """
            self._components.append(component)

      def notify(self, message):
            """
            Notifies all components with the message.
            """
            for component in self._components:
                component.receive(message)




"""Client Code
Demonstrate the usage of the Mediator pattern."""
if __name__ == "__main__":
    # Create mediator
    mediator = ConcreteMediator()
    # Create components and link them to the mediator
    component1 = Component(mediator)
    component2 = Component(mediator)
    # Add components to the mediator
    mediator.add_component(component1)
    mediator.add_component(component2)
    # Send messages through components
    component1.send("Hello from Component 1")
    component2.send("Hi from Component 2")
"""
Output
Component received message: Hello from Component 1
Component received message: Hello from Component 1
Component received message: Hi from Component 2
Component received message: Hi from Component 2

"""