'''
simple_programming_

This code defines Book class
'''
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Book(Title:{self.title}, Author:{self.author}, Genre:{self.genre})"

        
