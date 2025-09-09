# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    __secret = "This is a secret"
    __booklist = None

    # TODO: double-underscore properties are hidden from other classes
    # print(Book.__secret)  # this will raise an exception
    # but can still be accessed like this:
    # print(Book._Book__secret)  # this will work, but is not recommended

    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    @staticmethod
    def get_secret():
        return Book.__secret
    @staticmethod
    def get_book_list():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"Book type must be one of: {Book.BOOK_TYPES}")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book Types: ", Book.get_book_types())

# TODO: Create some book instances
b1 = Book("War and Peace", "HARDCOVER")
b2 = Book("The Catcher in the Rye", "PAPERBACK")
b3 = Book("The Great Gatsby", "EBOOK")

# TODO: Use the static method to access a singleton object
thebooks = Book.get_book_list()
thebooks.append(b1)
thebooks.append(b2)
thebooks.append(b3)
for b in thebooks:
    print(f"{b.title} ({b.booktype})")

