# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
from abc import ABC, abstractmethod
import math

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self) -> float:
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self) -> float:
        return math.pi * self.radius * self.radius


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self) -> float:
        return self.side * self.side
# ~~~~~~~~~ TEST CODE ~~~~~~~~~
# Uncomment the following line to see the error
#   g.calcArea()    # should raise an error since we can't instantiate the base class
# Uncomment the following line to see the error
#   g = GraphicShape()  # should raise an error since we can't instantiate the base class
# Uncomment the following line to see the error
#   g.calcArea()    # should raise an error since we can't instantiate the base class   

g = Circle(10)
c = Circle(10)

print(c.calcArea())
s = Square(12)
print(s.calcArea())
