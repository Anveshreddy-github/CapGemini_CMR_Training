class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    
    def display(self):
        print(f"The title of the book is {self.title} and its written by {self.author} and its isbn is : {self.isbn}")


def main():
    title=input("enter title:")
    author=input("enter author:")
    isbn=input("enter isbn :")
    p=Book(title,author,isbn)
    p.display()
main()