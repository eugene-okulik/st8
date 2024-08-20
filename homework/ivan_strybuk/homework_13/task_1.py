class Book:
    material_pages = "бумага"
    presence_of_text = True

    def __init__(self, title_of_book: str, author: str, number_of_pages: int, isbn: str, book_in_reserve=False):
        self.title_of_book = title_of_book
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.book_in_reserve = book_in_reserve

    def book_info(self):
        list_info = (f"Название: {self.title_of_book}, Автор: {self.author},"
                     f" страниц: {int(self.number_of_pages)}, материал: {self.material_pages}")
        if self.book_in_reserve:
            list_info += ", зарезервирована"
        return list_info


class SchoolBook(Book):

    def __init__(self, title_of_book: str, author: str, number_of_pages: int, isbn: str, object_type: str, grade: int,
                 availability_of_tasks=False, book_in_reserve=False):
        super().__init__(title_of_book, author, number_of_pages, isbn, book_in_reserve)
        self.object_type = object_type  # предмет (типа математика, история, география)
        self.grade = grade  # класс (школьный класс, для которого этот учебник)
        self.availability_of_tasks = availability_of_tasks  # наличие заданий (bool)

    def book_info(self):
        list_info = (f"Название: {self.title_of_book}, Автор: {self.author},"
                     f" страниц: {int(self.number_of_pages)}, предмет: {self.object_type},"
                     f" класс: {int(self.grade)}")
        if self.book_in_reserve:
            list_info += ", зарезервирована"
        return list_info


first_book = Book("Властелин колец", "Джон Р. Р. Толкин", 1120,
                  "978-5-17-085132-4")
second_book = Book("Унесенные ветром", "Маргарет Митчелл", 992,
                   "5-699-17166-5")
third_book = Book("11/22/63", "Стивен Кинг", 800,
                  "978-985-18-1878-1")
fourth_book = Book("Отверженные", "Виктор Гюго", 1284,
                   "978-5-389-06864-3")
fifth_book = Book("Улисс", "Джеймс Дж.", 1216,
                  "978-5-389-07139-1")

fourth_book.book_in_reserve = True  # пометьте одну книгу как зарезервированную

print(first_book.book_info())
print(second_book.book_info())
print(third_book.book_info())
print(fourth_book.book_info())
print(fifth_book.book_info())
print("-" * 8)

school_first_book = SchoolBook("Белорусский язык", "Джон", 2024,
                               "001-08-19-002024-1", "Белорусский язык", 5,
                               True, False)
school_second_book = SchoolBook("Алгебра", "Боб", 2024,
                                "002-08-19-002024-2", "Математика", 9, book_in_reserve=True)
school_third_book = SchoolBook("История Белоруси", "Чиж", 2024,
                               "003-08-19-002024-3", "История", 8)

school_third_book.book_in_reserve = True

print(school_first_book.book_info())
print(school_second_book.book_info())
print(school_third_book.book_info())
