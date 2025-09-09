# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod
import math

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def toJSON(self) -> str:
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return round(math.pi * (self.radius ** 2), 2)

    def toJSON(self) -> str:
        return f"{{'Circle': {str(self.calcArea())}}}"
# c = GraphicShape()  # This will raise an error

c = Circle(10)
print(c.calcArea())
print(c.toJSON())