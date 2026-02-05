from abc import ABC, abstractmethod

class demo(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(demo):
    def say_hello(self):
        return "Hi!"

dev = English()
print(dev.say_hello())