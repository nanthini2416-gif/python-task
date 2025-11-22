from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class lion(animal):
    def sound(self):
        print("Lion Roars")

class tiger(animal):
    def sound(self):
        print("tiger growls")


l=lion()
t=tiger()

l.sound()
t.sound()
