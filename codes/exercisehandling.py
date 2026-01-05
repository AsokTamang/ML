class LibraryItem:
    def __init__(self,title):
        self.title = title
        self.is_borrowed = False
    def borrow_item(self):
        if self.is_borrowed:
            raise Exception(f"{self.title} is already borrowed and hasn't been returned yet")
        self.is_borrowed = True
        return f'{self.title} is borrowed'
    def return_item(self):
        if self.is_borrowed:   #if the book is borrowed then after returning or after this method, the book's borrowed condition will be false
            self.is_borrowed = False
            return f'{self.title} has been returned'
        return f'{self.title} is not from this library'

class Book(LibraryItem):
    def __init__(self,title,author):
        super().__init__(title)   #here super means we are accessing the attributes of parent class
        self.author = author
    def taken(self):
        return super().borrow_item()
    def returned(self):
        return super().return_item()

book=Book('The magic of thinking Big','David Schwarz')



class Journal(LibraryItem):
    def __init__(self,title,issue_number):
        super().__init__(title)
        self.issue_number = issue_number
nature = Journal('Nature',50)


try:
    print((book.taken()))
    book.taken()
except Exception as e:  #here Exception is whatever is returned from the method inside the try block
    print(e)



