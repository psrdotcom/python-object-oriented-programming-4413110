# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func() -> float:
    return round(random.uniform(10, 100), 2)

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "Unknown Title"
    author: str = "Unknown Author"
    pages: int = 0
    price: float = field(default_factory=price_func)

b1 = Book()
b2 = Book("War and Peace", "Leo Tolstoy", 1225,
            39.95)  # override defaults
print(b1)
print(b2)