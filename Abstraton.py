from abc import ABC,abstractmethod
class Vehicle(ABC):
    def drive(self):
        print("Driving Vehicle")
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Starting Car Engine")
def operate_vehicle(vehicle):
    vehicle.drive()
    vehicle.start_engine()
car=Car()
operate_vehicle(car)