class Book:

    def __init__(self, material, text, name, author, num_page, isbn, reserved):
        self.material = material
        self.text = text
        self.name = name
        self.author = author
        self.num_page = num_page
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        status_reserved = "Зарезервировано" if self.reserved else ""

        result = f'Название: {self.name}, Автор: {self.author}, страниц: {self.num_page}, материал: {self.material}'

        if status_reserved:
            result += f', {status_reserved}'

        return result


book_1 = Book('бумага', 'есть', "Идиот", "Достоевский", "500", "325423523", True)
book_2 = Book('шелк', 'есть', "Белые ночи", "Достоевский", "657", "48787876", False)
book_3 = Book('бумага', 'есть', "Белые", "Достоевский", "657", "48787876", True)
book_4 = Book('картон', 'есть', "Ночи", "Достоевский", "657", "48787876", False)
book_5 = Book('хлопок', 'нету', "неизвестно", "неизвестно", "0", "48787876", True)

print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)


class GroupBook(Book):
    def __init__(self, name, author, num_page, subject, group, reserved):
        super().__init__(material="бумага", text="есть", name=name, author=author, num_page=num_page,
                         isbn="неизвестно", reserved=reserved)

        self.subject = subject
        self.group = group

    def __str__(self):
        status_reserved = "Зарезервировано" if self.reserved else ""
        result_school = (f'Название: {self.name}, Автор: {self.author}, страниц: {self.num_page}, '
                         f'предмет: {self.subject}, класс: {self.group}')

        if status_reserved:
            result_school += f', {status_reserved}'

        return result_school


school_book_1 = GroupBook("Алгебра", "Иванов", "200", "Математика", "10", True)
school_book_2 = GroupBook("Стихи", "Пушкин", "200", "Литература", "9", False)

print(school_book_1)
print(school_book_2)
