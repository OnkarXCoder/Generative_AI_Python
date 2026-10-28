'''class Car:
    def __init__(self,window,door,engine):
        self.window = window
        self.door = door
        self.engine = engine
    
    def drive(self):
        print(f"Car is driving {self.window} {self.door} {self.engine}")
class Tesla(Car):

    def __init__(self,window,door,engine,autopilot):
        super().__init__(window,door,engine)
        self.autopilot = autopilot
    def drive(self):
        super().drive()
        print(f"Tesla is driving with autopilot {self.autopilot} {self.window} {self.door} {self.engine}")  
Tesla1=Tesla("4 windows","4 doors","electric engine","enabled")
Tesla1.drive()'''
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")

class Pet(Animal):
    def __init__(self,name,owner):
        super().__init__(name)
        self.owner = owner
    def speak(self):
        super().speak()
        print(f"{self.name} is a pet of {self.owner}")

class Dog(Pet):
    def __init__(self,name,owner,breed):
        super().__init__(name,owner)
        self.breed = breed
    def speak(self):
        super().speak()
        print(f"{self.name} is a {self.breed} dog")
dog1 = Dog("Buddy","Alice","Golden Retriever")
dog1.speak()