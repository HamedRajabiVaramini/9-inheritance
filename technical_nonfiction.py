'''
simple_programming_

This code defines Technical Nonfiction Book as a child of Book class
'''
from book import Book 

class TechnicalNonfiction(Book):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.genre = "Technical Nonfiction"

    def __str__(self):
        return f"Technical(Title:{self.title}, Author:{self.author})"