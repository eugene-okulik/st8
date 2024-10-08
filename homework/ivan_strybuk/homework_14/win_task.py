class Flowers:
    """
    name = "Название"
    color = "Цвет цветка"
    freshness = "Cвежесть цветка"
    stem_length_cm = "стебель длина"
    cost = "стоимость"
    life_time_in_days = "жизни_время"
    smell = "запах"
    """

    smell = True

    def __init__(self, name, color, freshness, stem_length_cm: int, cost: int, life_time_in_days):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length_cm = stem_length_cm
        self.cost = cost
        self.life_time_in_days = life_time_in_days


class FlowersHolland(Flowers):

    def __init__(self, name, color, freshness, stem_length_cm: int, cost: int, life_time_in_days: int):
        super().__init__(name, color, freshness, stem_length_cm, cost, life_time_in_days)


class FlowersBelarus(Flowers):

    def __init__(self, name, color, stem_length_cm: int, cost: int, life_time_in_days: int, freshness="average"):
        super().__init__(name, color, freshness, stem_length_cm, cost, life_time_in_days)


class Bouquet:

    def __init__(self, flowers):
        """ Принимаем список цветов 'flowers' и присваиваем имя 'l_flower' для использования внутри класса"""
        self.l_flower = flowers

    def add_flower(self, flower):
        """Метод для добавления в список 'l_flower' цветка поштучно"""
        self.l_flower.append(flower)

    def avg_life_time(self):
        """Среднее время жизни цветов в букете, без дробной части"""
        total_cost = sum([flower.life_time_in_days for flower in self.l_flower])
        return int(total_cost / len(self.l_flower))

    def sort(self, key):
        """Сортировка по переданному ключу.
          'getattr(l_flower, key= "name")' возвращает значение именованного атрибута объекта.
          Если он не найден, то возвращается значение по умолчанию, переданное с функцией."""
        self.l_flower.sort(key=lambda x: getattr(x, key))

    def search(self, key, value):
        """Поиск по ключ - значение"""
        return [flower for flower in self.l_flower if getattr(flower, key) == value]


# Создание экземпляров цветов
first_flower = FlowersHolland("tulip", "red", "fresh", 15, 3, 5)
second_flower = FlowersHolland("orchid", "blue", "average", 20, 20, 10)
third_flower = FlowersHolland("red rose", "red", "fresh", 30, 15, 5)
fourth_flower = FlowersHolland("white rose", "white", "fresh", 10, 5, 5)

first_flower_BY = FlowersBelarus("red rose", "red", 20, 10, 3)
second_flower_BY = FlowersBelarus("white rose", "white", 20, 10, 3)
third_flower_BY = FlowersBelarus("tulip", "orange/white", 10, 22, 3)
fourth_flower_BY = FlowersBelarus("aster", "blue/red", 30, 15, 5)

# Создание букета
list_flowers = [first_flower, second_flower]  # Изначальный список цветов.
my_bouquet = Bouquet(list_flowers)  # Передаем список в класс 'Bouquet' где он будет храниться в 'l_flower'
my_bouquet.add_flower(third_flower)  # Добавление цветка в список 'l_flower'.

# # можно посмотреть, что храниться в 'l_flower'
# list_flowers = my_bouquet.l_flower
# for one_flower in list_flowers:
#     print(one_flower.color)

avg_life = int(my_bouquet.avg_life_time())
print(f"Среднее время увядания букета: {avg_life} дней.")

my_bouquet.sort("cost")  # Ключь сортировки
print("Цветы в букете отсортированы по цене:", [flower.name for flower in my_bouquet.l_flower])

search_key, search_value = "stem_length_cm", 20
yellow_color = my_bouquet.search(search_key, search_value)
print(f"Цветы в букете с длинной стебля {search_value} см:", [flower.name for flower in yellow_color])
