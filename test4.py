class Book():
    def __init__(self, title, author, is_borrowed):
        self.title = title 
        self.author = author
        self.borrowed = is_borrowed 
    def borrow(is_borrowed):
        if is_borrowed == True:
            print("Book is borrowed")
    def return_book(is_borrowed):
        is_borrowed = False
        print("Book is returned")
book_1 = Book("Great Gatsby", "Scott F Fitzgerald" True)