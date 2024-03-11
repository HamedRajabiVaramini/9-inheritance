'''
simple_programming_

This code defines Science Fiction Book as a child of Book class
'''
from book import Book 

class ScienceFiction(Book):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.genre = "Science Fiction"

    def __str__(self):
        return f"SiFi(Title:{self.title}, Author:{self.author})"

