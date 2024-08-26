class Book:

    def __init__(self, title, material_page, author, page_count, ISBN, reservation):
        self.title = title
        self.material_page = material_page
        self.author = author
        self.page_count = page_count
        self.ISBN = ISBN
        self.reservation = reservation


class SchoolBook(Book):

    def __init__(self, title, material_page, author, page_count, ISBN, reservation, subject, group, has_exercises):
        super().__init__(title, material_page, author, page_count, ISBN, reservation)
        self.subject = subject
        self.group = group
        self.has_exercises = has_exercises


textbook_1 = SchoolBook(title="Учебник по алгебре", material_page="Бумага", author="Иванов",
                        page_count=648,
                        ISBN="978-0-14-044910-5", reservation=False, subject="Алгебра", group="11в",
                        has_exercises=False)
textbook_1.reservation = True

textbook_2 = SchoolBook(title="Учебник по математике", material_page="Бумага", author="Петров", page_count=356,
                        ISBN="378-0-14-044910-4", reservation=False, subject="Математика", group="5А",
                        has_exercises=False)

book_1 = Book("Оно", "Бумага", "Стивен Кинг", 648, "978-0-14-044910-5",
              False)
book_2 = Book("Идиот", "Бумага", "Федор Достоевский", 750, "978-0-14-044911-6",
              False)
book_3 = Book("Тихий Дон", "Бумага", "Михаил Шолохов", 1267, "978-0-14-044912-7",
              False)
book_4 = Book("Унесенные ветром", "Бумага", "Маргарет Митчелл", 1468,
              "978-0-14-044913-8", False)
book_5 = Book("Казус Кукоцкого", "Бумага", "Людмила Улицкая", 689,
              "978-0-14-044914-9", False)

book_4.reservation = True

book_list = [book_1, book_2, book_3,book_4, book_5, textbook_1, textbook_2]

for one_book in book_list:
    reserved_book = ""
    if one_book.reservation is True:
        reserved_book = ", зарезервирована"

    if isinstance(one_book, SchoolBook) is True:
        print(f"Название: {one_book.title}, Автор: {one_book.author}, Страниц: {one_book.page_count},"
              f" Предмет: {one_book.subject}, Класс: {one_book.group}{reserved_book}")
    else:
        print(f"Название: {one_book.title}, Автор: {one_book.author}, Страниц: {one_book.page_count}, "
              f"Материал: {one_book.material_page}{reserved_book}")
