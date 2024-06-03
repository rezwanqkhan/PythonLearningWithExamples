from abc import ABC, abstractmethod


# Step 1 the subject

class Subject(ABC):
    def __init__(self):
        self.__observers = set()

    def attach(self, observer):
        # add an observer to the subject's list
        self.__observers.add(observer)

    def detach(self, observer):
        # remove an observer from the subject's list
        self.__observers.remove(observer)

    def notify_observers(self):
        # i = 1
        for observer in self.__observers:
            observer.update()
            # print(i)
            # i += 1


# step 2: the observer Interface
class observer(ABC):
    @abstractmethod
    def update(self):
        # abstract method for receiving updates.
        pass


# step 3: Concrete Observer
class ConcreteObserver(observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        # receive notification and print it
        print(f"{self.name} has been notified.")


# step 4: Client
if __name__ == "__main__":
    # Create subject
    subject = Subject()

    # Create Observers
    observer1 = ConcreteObserver("Observer1")
    observer2 = ConcreteObserver("Observer2")
    observer3 = ConcreteObserver("Observer3")
    observer4 = ConcreteObserver("Observer4")

    # attach observer to the subject
    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    subject.attach(observer4)

    # notify observer
    subject.notify_observers()

    subject.detach(observer4)
    print("\nobserver 4 deleted from list \n")

    subject.notify_observers()
