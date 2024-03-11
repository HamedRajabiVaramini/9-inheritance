'''
simple_programming_

This code defines Fantasy Book as a child of Book class
'''
from book import Book 

class Fantasy(Book):
    def __init__(self, title, author):
        super().__init(title, author, "Fantasy")

    def __str__(self): # override the __str__ function
        return f"Fantasy(Title:{self.title}, Author:{self.author})"