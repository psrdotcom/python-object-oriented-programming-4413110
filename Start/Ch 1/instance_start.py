# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, 'price'):
            return float(self.price)
        else:
            return 0.0
    def set_price(self, newprice):
        self.price = newprice

    def set_discount(self, percent):
        if percent > 0 and percent < 1:
            self.price = self.price * (1 - percent)

    def get_description(self):
        return f"{self.title} by {self.author}, {self.pages} pages: ${self.price}"
    

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "J.D. Salinger", 277, 29.99)

# TODO: print the price of book1
print(b1.get_price())

# TODO: try setting the discount
b1.set_price(b1.get_price() * 0.8)
print(b1.get_price())

# TODO: properties with double underscores are hidden by the interpreter
print(b1.get_description())
# print(b1.__price)  # this will raise an exception
# but can still be accessed like this:
# print(b1._Book__price)  # this will work, but is not recommended

print(b2.get_description())
b2.set_discount(0.25)
print(b2.get_description())
