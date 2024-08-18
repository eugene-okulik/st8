class Book:
    material = 'бумага'
    content = 'текст'

    def __init__(self, author, title, pages, isbn, reserved=False):
        self.author = author
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

# если зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага

    def reservation(self):
        if self.reserved:
            self.reserved = 'зарезервирована'
            print(
                f'Название:{self.title}, Автор: {self.author}, страниц: {self.pages}, '
                f'материал: {self.material}, {self.reserved}'
                  )
        else:
            print(
                f'Название:{self.title}, Автор: {self.author}, страниц: {self.pages},'
                f' материал: {self.material}'
            )


book1 = Book('J. K. Rowling', 'Harry Potter and the Sorcerers Stone', 100, 9780807286004)
book1.reserved = True
book2 = Book('Harlan Coben', 'I Will Find You', 200, '9781781100349')
book3 = Book('Taylor Jenkins Reid', 'Daisy Jones & the Six', 300, 9780606323451)
book4 = Book('J. K. Rowling', 'Harry Porter', 400, 9780807286005)
book5 = Book('Barbara Kingsolver', 'Demon Copperhead', 500, 8606323457)

book1.reservation()
book2.reservation()
book3.reservation()
book4.reservation()
book5.reservation()


class Second(Book):
    def __init__(self, author, title, pages, isbn, subject, classroom, exercise, reserved=False):
        super().__init__(author, title, pages, isbn, reserved)
        self.subject = subject
        self.classroom = classroom
        self.exercise = exercise


book_class1 = Second(' Пирютко О. Н.', 'Алгебра для 5х классов', 343,
                     8606323456, 'maths', 5, None)
book_class1.reserved = True
book_class2 = Second('Юхнель Н. В.', 'Английский дл 9х классовd', 215,
                     8601223457, 'english', 9, None)
book_class3 = Second(' Волков А. В,', 'Математика для 2х классов', 111,
                     8606224457, 'maths', '2', None)


# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9


def reservation_class(self):
    if self.reserved:
        self.reserved = 'зарезервирована'
        print(
            f'Название:{self.title}, Автор: {self.author}, страниц: {self.pages}, '
            f'предмет: {self.subject}, класс: {self.classroom}, {self.reserved}'
        )
    else:
        print(
            f'Название:{self.title}, Автор: {self.author}, страниц: {self.pages}, '
            f'предмет: {self.subject}, класс: {self.classroom}')


book_class1.reservation()
book_class2.reservation()
book_class3.reservation()
