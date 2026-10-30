class Shape:
    def area(self):
        print("Calculating area of shape")
class Circle(Shape):
    def __init__(self,rad):
        self.rad = rad
    def area(self):
        super().area()
        return 3.14*self.rad**2
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        super().area()
        return self.length*self.width
def print_area(shape):
    print(f"Area: {shape.area()}")

rec=Rectangle(5,10)
cir=Circle(7)
print_area(rec)
print_area(cir)
