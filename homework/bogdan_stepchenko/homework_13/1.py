class Book:
    material = 'бумага'
    is_text = True

    def __init__(self, title, author, quantity_of_pages: int, ISBN: int, reserved=False):
        self.title = title
        self.author = author
        self.quantity_of_pages = quantity_of_pages
        self.ISBN = ISBN
        self.reserved = reserved


first_book = Book('Идиот', 'Достоевский', 500, 9999, True)
second_book = Book('451 градус по Фаренгейту', 'Брэдбери', 300, 9673)
third_book = Book('Ветра зимы', 'Мартин', 750, 5693)
fourth_book = Book('Зов предков', 'Лондон', 420, 4526)
fifth_book = Book('Зеленая миля', 'Кинг', 680, 7204)


print(f"Название: {first_book.title}, Автор: {first_book.author}, "
      f"страниц: {first_book.quantity_of_pages}, материал: {first_book.material}"
      f"{', зарезервирована' if first_book.reserved else ''}"
      f"{', текст присутствует' if first_book.is_text else ''}")

print(f"Название: {second_book.title}, Автор: {second_book.author}, "
      f"страниц: {second_book.quantity_of_pages}, материал: {second_book.material}"
      f"{', зарезервирована' if second_book.reserved else ''}"
      f"{', текст присутствует' if second_book.is_text else ''}")

print(f"Название: {third_book.title}, Автор: {third_book.author}, "
      f"страниц: {third_book.quantity_of_pages}, материал: {third_book.material}"
      f"{', зарезервирована' if third_book.reserved else ''}"
      f"{', текст присутствует' if third_book.is_text else ''}")

print(f"Название: {fourth_book.title}, Автор: {fourth_book.author}, "
      f"страниц: {fourth_book.quantity_of_pages}, материал: {fourth_book.material}"
      f"{', зарезервирована' if fourth_book.reserved else ''}"
      f"{', текст присутствует' if fourth_book.is_text else ''}")

print(f"Название: {fifth_book.title}, Автор: {fifth_book.author}, "
      f"страниц: {fifth_book.quantity_of_pages}, материал: {fifth_book.material}"
      f"{', зарезервирована' if fifth_book.reserved else ''}"
      f"{', текст присутствует' if fifth_book.is_text else ''}")


class SchoolBook(Book):
    def __init__(self, title, author, quantity_of_pages: int, ISBN: int,
                 subject, school_class: int, home_task: bool, reserved=False):
        super().__init__(title, author, quantity_of_pages, ISBN, reserved)
        self.subject = subject
        self.school_class = school_class
        self.home_task = home_task


first_school_book = SchoolBook('Математика', 'Сидоров', 250, 1000, 'Алгебра', 9, True, True)
second_school_book = SchoolBook('Литература', 'Петров', 320, 2000, 'Русская литература', 7, True)
third_school_book = SchoolBook('История', 'Никифоренко', 234, 300, 'История Беларуси', 11, False)

print(f"Название: {first_school_book.title}, Автор: {first_school_book.author}, "
      f"страниц: {first_school_book.quantity_of_pages}, материал: {first_school_book.material}"
      f", предмет: {first_school_book.subject}, класс: {first_school_book.school_class}"
      f"{', домашние задания присутствуют' if first_school_book.home_task else ''} "
      f"{', зарезервирована' if first_school_book.reserved else ''}")

print(f"Название: {second_school_book.title}, Автор: {second_school_book.author}, "
      f"страниц: {second_school_book.quantity_of_pages}"
      f", предмет: {second_school_book.subject}, класс: {second_school_book.school_class}"
      f"{', домашние задания присутствуют' if second_school_book.home_task else ''} "
      f"{', зарезервирована' if second_school_book.reserved else ''}")

print(f"Название: {third_school_book.title}, Автор: {third_school_book.author}, "
      f"страниц: {third_school_book.quantity_of_pages}"
      f", предмет: {third_school_book.subject}, класс: {third_school_book.school_class}"
      f"{', домашние задания присутствуют' if third_school_book.home_task else ''} "
      f"{', зарезервирована' if third_school_book.reserved else ''}")
