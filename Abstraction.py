import math
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        self.area=0
    @abstractmethod
    def take_input(self):
        pass
    @abstractmethod
    def find_area(self):
        pass
    @abstractmethod
    def disp_area(self):
        pass
class Circle(Shape):
    def __init__(self):
        self.r=0
        super().__init__()
    def take_input(self):
        self.r=int(input("enter the radius:"))
    def find_area(self):
        self.area=math.pi*self.r**2
    def disp_area(self):
        print(self.area)
class Rectangle(Shape):
    def __init__(self):
        self.l=0
        self.b=0
        super().__init__()
    def take_input(self):
        self.l=int(input("enter the length:"))
        self.b=int(input("enter the breadth:"))
    def find_area(self):
        self.area=self.l*self.b
    def disp_area(self):
        print(self.area)

class Triangle(Shape):
    def __init__(self):
        self.h=0
        self.l=0
        super().__init__()
    def take_input(self):
        self.h=int(input("enter the height:"))
        self.l=int(input("enter the length:"))
    def find_area(self):
        self.area=(self.h*self.l)/2
    def disp_area(self):
        print(self.area)

def geometry(ref):
    ref.take_input()
    ref.find_area()
    ref.disp_area()

def main():
    c=Circle()
    r=Rectangle()
    t=Triangle()

    geometry(c)
    geometry(r)
    geometry(t)

main()
