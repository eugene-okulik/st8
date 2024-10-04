class Book:
    materialBook = 'paper'
    textInside = True

    def __init__(self, authorBook, nameBook, pages, ISBN, reserved) -> None:
        self.authorBook = authorBook
        self.nameBook = nameBook
        self.pages = pages
        self.ISBN = ISBN
        self.reserved = reserved

    def reservation(self):
        if self.reserved:
            print(f'Название: {self.nameBook}, Автор: {self.authorBook}, страниц:{
                  self.pages}, материал: {self.materialBook}, зарезервирована')
        else:
            print(f'Название: {self.nameBook}, Автор: {self.authorBook}, страниц:{
                  self.pages}, материал: {self.materialBook}')


book1 = Book('Dorothy Graham', 'Software Testing',
             273, '978-1-4737-6479-8', True)
book1.reserved = True
book2 = Book('Robert C. Martin', 'Clean Code', 260, '978-1-4747-6479-8', False)
book3 = Book('Andy Hun', 'The Pragmatic Programmer',
             100, '978-3455-42525', False)

book1.reservation()
book2.reservation()
book3.reservation()
