class LibraryItem:
    def __init__(self,title):
        self.title = title
        self.is_borrowed = False
    def borrow_item(self):
        if self.is_borrowed:
            raise Exception(f'{self.title} is already borrowed')
        self.is_borrowed = True
        return f'{self.title} is borrowed'
    def return_item(self):
        if self.is_borrowed:   #if the book is borrowed then after returning or after this method, the book's borrowed condition will be false
            self.is_borrowed = False
            return f'{self.title} has been returned'
        return f'{self.title} is not from this library'
maths = LibraryItem('AI/ML')
print(maths.borrow_item())
print(maths.return_item())
print(maths.return_item())
