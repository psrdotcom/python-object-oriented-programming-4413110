# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# TODO: create instances of the class
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# TODO: print the class and property
print(book1.title, book1.author)
print(book2.title, book2.author)
print(type(book1))
print(dir(book1))
print(book1.__dict__)
print(book2.__dict__)
# --- IGNORE ---