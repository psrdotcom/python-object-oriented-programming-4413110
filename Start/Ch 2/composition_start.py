# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []

    # add a chapter to the book
    def addchapter(self, chapter):
        self.chapters.append(chapter)

    # get the total page count of the book
    def getbookpagecount(self):
        total = 0
        for chapter in self.chapters:
            total += chapter.pages
        return total

# Author and Chapter classes to be used as components of Book
class Author:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __str__(self):
        return f"{self.first} {self.last}"
    
class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

# create the objects and compose them together
auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)
# add chapters to the book
b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))
# print out the book details
print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
print(type(b1))
print(dir(b1))
print(b1.__dict__)
print(b1.author.__dict__)
for c in b1.chapters:
    print(c.__dict__)