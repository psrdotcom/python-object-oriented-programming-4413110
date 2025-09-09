# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_method(self, newval: int):
        # Cannot modify value2 since the class is frozen (immutable)
        print(f"Attempted to set value2 to {newval}, but this class is immutable.")
    
# create an instance of the class
obj = ImmutableClass("Initial Value", 42)
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "New Value"  # Uncommenting this line will raise a FrozenInstanceError
# print(obj.value1)

# TODO: even functions within the class can't change anything
# obj.some_method(99)
# print(obj.value2)