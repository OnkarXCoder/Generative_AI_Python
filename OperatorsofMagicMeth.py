'''class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)
    def __truediv__(self,scalar):
        return Vector(self.x/scalar,self.y/scalar)
    def __repr__(self):
        return f"Vector({self.x},{self.y})"
x=Vector(2,3)
y=Vector(4,5)
print(x+y)
print(x-y)
print(x*2)
print(x/2)'''
class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        return ComplexNumber(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
        return ComplexNumber(self.real-other.real,self.imag-other.imag)
    def __mul__(self,other):
        return ComplexNumber(self.real*other.real-self.imag*other.imag,self.real*other.imag+self.imag*other.real)
    def __truediv__(self,other):
        denom=other.real**2+other.imag**2
        return ComplexNumber((self.real*other.real+self.imag*other.imag)/denom,(self.imag*other.real-self.real*other.imag)/denom)
    def __repr__(self):
        return f"ComplexNumber({self.real},{self.imag})"
x=ComplexNumber(2,3)
y=ComplexNumber(4,5)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
