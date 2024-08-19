"""
Создайте класс book с атрибутами:

материал страниц
наличие текста
название книги
автор
кол-во страниц
ISBN
флаг зарезервирована ли книга или нет (True/False).
Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
Создайте несколько (штук 5) экземпляров разных книг.
После создания пометьте одну книгу как зарезервированную.
Распечатайте детали о каждой книге в таком виде:
Если книга зарезервирована:

Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
если не зарезервирована:

Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
"""


class Book:
    is_reserved = False
    page_material = str('Paper')
    text_is_availability = bool(True)

    def __init__(self, name, author, page_quantity, isbn, is_reserved):
        self.name = name
        self.author = author
        self.page_quantity = page_quantity
        self.isbn = isbn
        self.is_reserved = is_reserved

    def book_details(self):
        if self.is_reserved:
            print(
                f"Name: {self.name}, Author: {self.author}, Pages: {self.page_quantity}, "
                f"Material: {self.page_material}. - Reserved"
            )

        else:
            print(
                f"Name: {self.name}, Author: {self.author}, Pages: {self.page_quantity}, Material: {self.page_material}"
            )


idiot = Book('idiot', 'dostoevky', 300, 'isbsfaifdso', is_reserved=False)
necronomicon = Book('Necronomicon', 'unknown', 666, 'sssssssss', is_reserved=True)
the_holy_booble = Book('The Holy Booble', 'Cat Pettus', 202, 'smaasksadkdsak', is_reserved=False)
wild_sheep = Book('A Wild Sheep Chase', 'Haruki Murakami', 353, 'sdfsdfdsf', is_reserved=False)
martin_Eden = Book('Martin Eden', 'Jack London', 480, 'aaaaaaaaaa', is_reserved=True)

necronomicon.book_details()
idiot.book_details()
the_holy_booble.book_details()
wild_sheep.book_details()
martin_Eden.book_details()

"""Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:

предмет (типа математика, история, география),
класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
наличие заданий (bool)
Создайте несколько экземпляров учебников.
После создания пометьте один учебник как зарезервированный.
Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:

Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
если не зарезервирован:

Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9"""


class SchoolBooks(Book):
    school_subject = str()
    grade = int
    homework = bool()

    def __init__(self, name, author, page_quantity, isbn, school_subject, grade, homework, is_reserved):
        super().__init__(name, author, page_quantity, isbn, is_reserved)
        self.school_subject = school_subject
        self.grade = grade
        self.homework = homework

    def school_books_details(self):
        if self.is_reserved:
            print(
                f"Name: {self.name}, Author: {self.author}, Pages: {self.page_quantity}, "
                f"Subject: {self.school_subject}, Grade: {self.grade}. - Reserved"
            )

        else:
            print(
                f"Name: {self.name}, Author: {self.author}, Pages: {self.page_quantity}, "
                f"Subject: {self.school_subject}, Grade: {self.grade}"
            )


history = SchoolBooks('History of ancient Rome', 'biba.buba', 333, 'isbnqsas', 'history', 2, True, is_reserved=False)
math = SchoolBooks('Algebra for primary school', 'galya ivanovna', 250, 'yiiiii', 'math', 1, True, is_reserved=True)

history.school_books_details()
math.school_books_details()
