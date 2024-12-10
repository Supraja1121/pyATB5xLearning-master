from abc import ABC, abstractmethod

class GearBox(ABC):
    @abstractmethod
    def setgear(self):
        pass

class Engine(GearBox):

    @abstractmethod
    def start(self):
        super().setgear()
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def drive(self):
        self.start()
        self.stop()

co=Car()
co.drive()
