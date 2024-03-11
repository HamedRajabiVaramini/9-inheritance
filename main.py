'''
simple_programming_

Main function is like the entry point of the program.
'''
from technical_nonfiction import TechnicalNonfiction
from fantasy import Fantasy
from science_fiction import ScienceFiction

def main():
    books = [TechnicalNonfiction("Clean Code", "Robert C. Martin"),
             ScienceFiction("Dune", "Frank Herbert"),
            Fantasy("The Hobbit", "J.R.R. TOlkien")]  
    for book in books:
        print(book)

if __name__ == "__main__":
    ''' 
    output is:
        Technical(Title:Clean Code, Author:Robert C. Martin)
        SiFi(Title:Dune, Author:Frank Herbert)
        Fantasy(Title:The Hobbit, Author:J.R.R. TOlkien)
    '''
    main()
